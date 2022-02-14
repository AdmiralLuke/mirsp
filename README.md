## Software-Projekt Music Information Retrieval

#### Thema
* erkennung, welche Instrumente in einem Song/Stück eingesetzt wurden
* Nutzerangaben verwenden, um eventuelles NN zu trainieren

#### Konzept
* Browseranwendung (über WebServer gehostet) wo Nutzer ein beliebigen Song hochladen kann
* im Hintergrund wird errechnet, welche Instrumente in dem Stück sein können 
* Genauigkeit errechnen, zu wie viel % sich das System "sicher" ist
* Nutzer können anschließend angeben, welche Instrumente richtig erkannt wurden vom System -> kontinuierliche Verbesserung

#### Verwendete Elemente
* C++ / C : Parallelisierung der Berechnung um ein schnelles Ergebnis zu bekommen
* Typescript / Javascript für die Browseranwendung
* Java für FrontEnd
* Python für Berechnungen (librosa-Bibliothek,...) und evtl. Deep Learning
* SQL: Datenbankeinbindung
