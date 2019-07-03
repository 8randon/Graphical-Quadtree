# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:33:50 2019

Current Resources: 
        * https://matplotlib.org/3.1.0/users/event_handling.html
        * https://stackoverflow.com/questions/16527930/matplotlib-update-position-of-patches-or-set-xy-for-circles
        * https://stackoverflow.com/questions/47852102/drawing-circle-by-clicking-using-matplotlib

@author: Brandon Townsend
"""

from matplotlib import pyplot as plt
#from graphics import *

class CircleDrawer:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.cid = fig.canvas.mpl_connect('button_press_event', self)
    
    def __call__(self, event):
        print('click', event)
        circle = plt.Circle((event.xdata, event.ydata), 10, color='r', fill=False)
        self. ax.add_patch(circle)
        self.fig.canvas.draw()
    
def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % ('double' if event.dblclick else 'single', event.button, event.x, event.y, event.xdata, event.ydata))

fig, ax = plt.subplots()
ax.set_title('click to build line segments')
ax.set_xlim([-40, 40])
ax.set_ylim([-40, 40])
ax.set_aspect('equal')

#linebuilder = LineBuilder(line)
circledrawer = CircleDrawer(fig,ax)
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()