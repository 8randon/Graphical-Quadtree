# -*- coding: utf-8 -*-
"""
Created on Sat Jul 06 13:15:47 2019

@author: Brandon Townsend
"""
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
import math
import numpy as np

def PointsInCircum(r,n=100):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]

fig, ax = plt.subplots()
ax.set_title('click to make circles')
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_aspect('equal')
plt.grid()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))


#_______________TEST_______________
print('click test')
circles = list()
circle = plt.Circle((5, 5), 5, color='r', fill=False)
circles.append(circle)
ax.add_patch(circle)
fig.canvas.draw()
#_______________^^^^_______________

print np.array(zip(*PointsInCircum(10,100)))

a = np.array(zip(*PointsInCircum(10,100)))
b = a[0]
c = a[1]

plt.plot(b,c, 'ro')
plt.show()

plt.plot(a, 'ro')
plt.axis([0, 6, 0, 20])
plt.show()