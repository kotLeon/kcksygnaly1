import numpy as np
import matplotlib.pyplot as plt
 
f = 3
t = np.linspace(0, 1, 256)
sygnal = np.cos(2*np.pi*f*t)
plt.plot(t, sygnal, label = 'fp = 256Hz')
 
t = np.linspace(0, 1, 25)
sygnal = np.cos(2*np.pi*f*t)
plt.plot(t, sygnal, label = 'fp = 25Hz')

t = np.linspace(0, 1, 10)
sygnal = np.cos(2*np.pi*f*t)
plt.plot(t, sygnal, label = 'fp = 10Hz')

legend = plt.legend(loc='upper right', shadow=True, fontsize='medium')
 
plt.show()