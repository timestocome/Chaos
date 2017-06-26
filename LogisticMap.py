
# https://github.com/timestocome

# bifurcation diagram - logistic equation


import numpy as np 
import matplotlib.pyplot as plt

x_new = 0.01
x_old = 0.01



plt.figure(figsize=(14,14))
plt.title('Bifurcation diagram logistic equation')

for r in range(300):
    for x in range(100):

        A = r/100. + 1.0
        x_new = A * x_old * (1. - x_old)        
        plt.scatter(A, x_new, s=1.0)
        x_old = x_new





plt.ylabel='X'
plt.xlabel='R'
plt.savefig('LogisticMap.png')
plt.show()