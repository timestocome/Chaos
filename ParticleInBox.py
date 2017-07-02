

# https://github.com/timestocome

# simple example of a particle in a box



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation




# create data
n_frames = 1000
box_size = 30
radius = 2

left = -box_size + radius
right = box_size - radius
top = box_size - radius
bottom = -box_size + radius


x = 0.0
y = 0.0
x_speed = 1.5
y_speed = 2.3

xp = []
yp = []
for z in range(n_frames):

    if x <= left: x_speed *= -1
    if x >= right: x_speed *= -1
    if y <= bottom: y_speed *= -1
    if y >= top: y_speed *= -1

    x += x_speed
    y += y_speed

    xp.append(x)
    yp.append(y)





# set up graphics

figure = plt.figure(figsize=(12,12))
ax = figure.add_subplot(111)
plt.title("Particle in a box")
ax.set_xlim(-box_size, box_size)
ax.set_ylim(-box_size, box_size)

patch = patches.Circle((0.0, 0.0), radius, fc=[0.0, 0.5, 0.5, 1.0])


# run animation

def init():
    ax.add_patch(patch)
    return patch


def animate(i):
    
    patch.center = ([xp[i], yp[i]])
    return patch,


anim = animation.FuncAnimation(figure, animate, init_func=init, frames=len(xp), interval=60, blit=False)
                               
plt.show()

