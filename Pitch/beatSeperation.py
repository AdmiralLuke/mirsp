import numpy as np
import librosa
import librosa.display
from time import time 

def median_filter(spectrogram, axis, window_size):
    if axis == 1:
        spectrogram = spectrogram.T
    filtered_spectrogram = np.zeros_like(spectrogram)
    spectrogram = np.pad(spectrogram, ((window_size//2, window_size//2), (0, 0)), mode="reflect")
    
    for left in range(spectrogram.shape[0] - window_size + 1):
        window = spectrogram[left:(left + window_size), :]
        filtered_window = np.median(window, axis=0)
        filtered_spectrogram[left, :] = filtered_window
    
    return filtered_spectrogram.T if axis == 1 else filtered_spectrogram


start = int(time() * 1000)
# hier kann jeder beliebige Song geladen werden
y, sr = librosa.load("nggup.wav")
n_fft = 2048
hop_length = n_fft // 2

spectrogram = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
power = np.abs(spectrogram)**2
logpower = np.log(power + 1)

window_size_percussive = 250  # Hz
window_size_percussive = int(window_size_percussive / (sr / n_fft))
if window_size_percussive == 0:
    raise ValueError("percussive window size 0")
if not window_size_percussive % 2:
    window_size_percussive += 1

window_size_harmonic = 1.  # sekunden
window_size_harmonic = int(window_size_harmonic / (hop_length / sr))  # fesntern
if window_size_harmonic == 0:
    raise ValueError("harmonic window size 0")
if not window_size_harmonic % 2:
    window_size_harmonic += 1

percussive_filtered = median_filter(power, 0, window_size_percussive)
harmonic_filtered = median_filter(power, 1, window_size_harmonic)

beta = 1.3
percussive_binary_mask = np.where(percussive_filtered >= beta * harmonic_filtered, 1., 0.)
harmonic_binary_mask = np.where(harmonic_filtered > beta * percussive_filtered, 1., 0.)
residual_binary_mask = mask = 1 - percussive_binary_mask - harmonic_binary_mask


percussive_masked = logpower * percussive_binary_mask
harmonic_masked = logpower * harmonic_binary_mask
residual_masked = logpower * residual_binary_mask
allmax = np.max([percussive_masked.max(), harmonic_masked.max(), residual_masked.max()])
end = int(time() * 1000)

percussive_spectrogram = spectrogram * percussive_binary_mask
inverted_percussive = librosa.istft(percussive_spectrogram, win_length=n_fft, hop_length=hop_length)

print("Berechnungszeit:", end - start)
