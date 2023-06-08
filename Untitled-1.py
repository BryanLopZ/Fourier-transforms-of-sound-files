
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy.signal import find_peaks

ruta = r"C:\Users\usuario\Downloads\Proyecto\Phonemas\A13_20.wav"
x, fs = sf.read(ruta)
X = np.fft.fft(x)
Spectre = np.fft.fftshift(np.abs(X))
N = len(Spectre) 
w = np.linspace(-fs/2,fs/2,N)

frecuencias = np.fft.fftfreq(len(x), 1/fs)

picos, _= find_peaks(Spectre, distance = 100)
#print(picos)
picos_ordenados = sorted(picos, key=lambda i: Spectre[i], reverse=True)
primero = picos_ordenados[1]
Segundo = picos_ordenados[3]
Tercero = picos_ordenados[5]

prim_arm = np.abs(w[primero]) #le pongo el valor absoluto porque algunos picos quedan en frecuencias negativas, para obtener el valor real
seg_arm = np.abs(w[Segundo])
ter_arm = np.abs(w[Tercero])

print(prim_arm, seg_arm, ter_arm)

np.savetxt('archivo.txt', picos_ordenados)
plt.plot(w,Spectre)
plt.show()

#Nota: checar bien lo de los indices, algunos salian negativos