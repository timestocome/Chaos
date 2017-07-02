

# https://github.com/timestocome

# create random numbers with different distributions


import numpy as np 
import matplotlib.pyplot as plt 


n_samples = 10000
x = np.arange(0, n_samples)
n_bins = n_samples//100

# default numpy
default = np.random.rand(n_samples)

p = np.random.rand(n_samples)           # array of floats
n = np.random.randint(n_samples)        # array of ints

exponential = np.random.exponential(1, n_samples)


zipf = np.random.zipf(2., n_samples)
zipf = np.delete(zipf, np.where(zipf > 50))

logistic = np.random.logistic(p, 1., n_samples)

poisson = np.random.poisson(p, n_samples)


fig = plt.figure(figsize=(12,12))
plt.subplot(6,1,1)
plt.hist(logistic, bins=n_bins, normed=True)
plt.title('Logistic')

plt.subplot(6,1,2)
plt.hist(poisson, bins=n_bins, normed=True)
plt.title('Poisson')

plt.subplot(6,1,3)
plt.hist(default, bins=n_bins, normed=True)
plt.title('Default')

plt.subplot(6,1,4)
plt.hist(exponential, bins=n_bins, normed=True)
plt.title('Exponetial')


plt.subplot(6,1,5)
plt.hist(zipf, bins=n_bins, normed=True)
plt.title('Zipf')





plt.savefig('distributions.png')
plt.show()




