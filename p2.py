import numpy as np
import matplotlib.pyplot as plt
 
f = 1
f2 = 1.05
f3 = 2
A = 1
t = np.linspace(0, 1, 512)
sygnal = A*np.sin(2*np.pi*f*t)
sygnal2 = A*np.sin(2*np.pi*f2*t)
sygnal3 = A*np.sin(2*np.pi*f3*t)
 
plt.plot(t, sygnal, label='f = 1Hz')
plt.plot(t, sygnal2, label = 'f = 1.05Hz')
plt.plot(t, sygnal3, label = 'f = 3Hz')

legend = plt.legend(loc='upper right', shadow=True, fontsize='medium')
plt.show()

plt.show()