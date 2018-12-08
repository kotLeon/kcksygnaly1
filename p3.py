import numpy as np
import matplotlib.pyplot as plt
 
f = 1
omega1 = np.pi/6
omega2 = np.pi
A = 1
t = np.linspace(0, 1, 512)
sygnal = A*np.sin(2*np.pi*f*t)
sygnal2 = A*np.sin(2*np.pi*f*t + omega1)
sygnal3 = A*np.sin(2*np.pi*f*t + omega2)
 
plt.plot(t, sygnal, label='bez przesunięcia')
plt.plot(t, sygnal2, label = 'przesunięcie o pi/6')
plt.plot(t, sygnal3, label = 'przesunięcie o pi')

legend = plt.legend(loc='upper right', shadow=True, fontsize='medium')
plt.show()

plt.show()