import numpy as np
import librosa
import librosa.display
from time import time


start = int(time() * 1000)
y, sr = librosa.load("bastille.wav")

S_full, phase = librosa.magphase(librosa.stft(y))
S_filter = librosa.decompose.nn_filter(S_full, aggregate=np.median, metric='cosine',width=int(librosa.time_to_frames(2, sr=sr)))
S_filter = np.minimum(S_full, S_filter)

margin_i, margin_v = 2, 10
power = 2
mask_i = librosa.util.softmask(S_filter,margin_i * (S_full - S_filter),power=power)
mask_v = librosa.util.softmask(S_full - S_filter, margin_v * S_filter, power=power)

S_foreground = mask_v * S_full
S_background = mask_i * S_full

S_for = librosa.istft(S_foreground)

end = int(time() * 1000)

print(end - start, "ms Berechnungszeit")