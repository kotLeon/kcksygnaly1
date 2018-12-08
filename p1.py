import numpy as np
import matplotlib.pyplot as plt
 
f = 3
A = 1
A2 = 0.5 
A3 = 3
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)
sygnal2 = A2*np.sin(2*np.pi*f*t)
sygnal3 = A3*np.sin(2*np.pi*f*t)

 
plt.plot(t, sygnal, label='A=1')
plt.plot(t, sygnal2, label='A=0.5')
plt.plot(t, sygnal3, label='A=3')

legend = plt.legend(loc='upper right', shadow=True, fontsize='medium')
plt.show()