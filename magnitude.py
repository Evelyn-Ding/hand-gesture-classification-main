# list to keep track of things
# function to do the math


# objective: create a time-domain graph that tracks the magnitude with respect to time (like tracking acceleration wrt time)
# the magnitude is the difference between two (x,y) coordinates between 2 frames
# magnitude is calculated as sqrt(x^2+y^2) and captures the change in the two points (as 1 Dimension)
# magnitude allows you to see how much the hands has moved in order to track the severity of the tremor 

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
# %matplotlib qt
textfile = open('centerLog.txt',"r")
data = np.loadtxt(textfile, delimiter = ',')
#diffdata = numpy.diff(data, axis=0)
plt.figure()
rdata = np.sqrt(data[:,1]**2+data[:,0]**2) 
#freq, time, zxx = signal.stft(rdata, 30, nperseg=256)
#plt.pcolormesh(time, freq, np.abs(zxx), vmin=0, vmax = 10, shading='gouraud')
framePerSec = 30
freq = np.arange(0,np.size(rdata))*framePerSec/np.size(rdata)
plt.plot(freq,20*np.log10(np.abs(np.fft.fft(rdata - np.mean(rdata)))))
plt.figure()
plt.plot(rdata)
plt.show()

