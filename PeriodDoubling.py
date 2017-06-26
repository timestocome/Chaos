
# https://github.com/timestocome


import numpy as np 
import matplotlib.pyplot as plt 


t_range = 100
t = np.arange(0, t_range) / 10

f = 40.
V = 2.0

v_t = V * np.sin(2 * np.pi * f * t)



v_1 = V * np.sin(2 * np.pi * 1. * t)
v_2 = V * np.sin(2 * np.pi * 2. * t)
v_3 = V * np.sin(2 * np.pi * 4. * t)
v_4 = V * np.sin(2 * np.pi * 8. * t)
v_5 = V * np.sin(2 * np.pi * 16. * t)
v_6 = V * np.sin(2 * np.pi * 32. * t)




plt.figure(figsize=(12,12))
plt.suptitle("Period doubling in a diode circuit")

plt.subplot(6,1,1)
plt.plot(v_1, label="f = 1/1")
plt.legend(loc='best')

plt.subplot(6,1,2)
plt.plot(v_2, label="f = 2/1")
plt.legend(loc='best')

plt.subplot(6,1,3)
plt.plot(v_3, label="f = 4/1")
plt.legend(loc='best')

plt.subplot(6,1,4)
plt.plot(v_4, label="f = 8/1")
plt.legend(loc='best')

plt.subplot(6,1,5)
plt.plot(v_5, label="f = 16/1")
plt.legend(loc='best')

plt.subplot(6,1,6)
plt.plot(v_6, label="f = 32/1")
plt.legend(loc='best')

plt.savefig("PeriodDoubling.png")
plt.show()




