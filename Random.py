

# https://github.com/timestocome

# simple example of a random walk animation


import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


fig = plt.figure(figsize=(16, 16))

ax1 = fig.add_subplot(1,1,1)
ax1.set_ylim([-30, 30])
ax1.set_xlim([-30, 30])
plt.title("Random Walk")



# returns int of value: -1, 0, 1
def randomWalk():
    s = np.random.randint(low=-1, high=2)
    return s
    



counter = 1
location_x = [0]
location_y = [0]

def animate(i):

    global location_x, location_y, counter

    location_x.append(location_x[counter-1] + randomWalk())
    location_y.append(location_y[counter-1] + randomWalk())

    plt.plot(location_x[counter], location_y[counter], marker='*', color="b", alpha=0.3)

    counter += 1




ani = animation.FuncAnimation(fig, animate, interval=10, frames=1000, repeat=False)
plt.show()


fig = plt.figure(figsize=(12,12))
plt.subplot(2,1,1)
plt.hist(location_x)
plt.title('X')

plt.subplot(2,1,2)
plt.hist(location_y)
plt.title('Y')
plt.hist(location_y)

plt.savefig('random_histogram.png')
plt.show()