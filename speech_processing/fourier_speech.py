'''requires scipy, numpy and matplotlib '''
from scipy.io import wavfile
fs, data = wavfile.read('./m01oo.wav')

'''
#Simulate data with two sin (50Hz & 80Hz) tones
fs = 44100
import numpy as np
N = 22000
T = 1.0 / fs
x = np.linspace(0.0, N*T, N)
data = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)'''

print(fs)
print(len(data))

from scipy.fftpack import fft
fdata = fft(data)


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#plt.plot(data)
#plt.show()

afdata = abs(fdata)
lafdata = len(afdata)

#If you want to see both positive and negative frequecies in the spectrum
#ffdata = np.concatenate([afdata[lafdata/2:],afdata[:lafdata/2]])
#x = np.linspace(-fs/2, fs/2, len(data))

#If you want to see only positive frequencies in the spectrum
ffdata = afdata[:lafdata/2]
x = np.linspace(0, fs/2, len(data)/2)

plt.plot(x,ffdata)
plt.show()
