# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:33:50 2019

Current Resources: 
        * https://matplotlib.org/3.1.0/users/event_handling.html
        * https://stackoverflow.com/questions/16527930/matplotlib-update-position-of-patches-or-set-xy-for-circles
        * https://stackoverflow.com/questions/47852102/drawing-circle-by-clicking-using-matplotlib
        * https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib

Current state: adds circles

@author: Brandon Townsend
"""

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from Quadtree import Node
#import numpy as np
#from graphics import *

class CircleDrawer:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.cid = fig.canvas.mpl_connect('button_press_event', self)
        self.circles = list()
        self.points = list()
    
    def __call__(self, event):
        
        print('click', event)
        circle = plt.Circle((event.xdata, event.ydata), 10, color='r', fill=False)
        self.circles.append(circle)
        n = Node(root=True)
        
        self.points.append(n.calcPoints(self.circles))
        
        for points in self.points:
            plt.plot(points[0], points[1], 'bo')
            
        self. ax.add_patch(circle)
        self.fig.canvas.draw()
        
    def Circles(self):
        return self.circles
    
    def Add(self, circle):
        self.circles.append(circle)
    
def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % ('double' if event.dblclick else 'single', event.button, event.x, event.y, event.xdata, event.ydata))


fig, ax = plt.subplots()
ax.set_title('click to make circles')
ax.set_xlim([-40, 40])
ax.set_ylim([-40, 40])
ax.set_aspect('equal')
plt.grid()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
#linebuilder = LineBuilder(line)
circledrawer = CircleDrawer(fig,ax)
cid = fig.canvas.mpl_connect('button_press_event', onclick)

#n = Node(root=True)
#
#circledrawer.Add(plt.Circle((20, 20), 20, color='r', fill=False))
#circledrawer.Add(plt.Circle((10, 10), 20, color='b', fill=False))
#
#if len(circledrawer.Circles()) > 0:
#    a = n.calcPoints(circledrawer.Circles())
#    
#    for points in a:
#        plt.plot(points[0], points[1], 'bo')
#_______________TEST_______________
#print('click test')
#circles = list()
#circles.append(plt.Circle((20, 20), 5, color='r', fill=False))
#circles.append(plt.Circle((10, 10), 5, color='b', fill=False))
#
#n = Node(circleres = 1, root=True)
#
#for cir in circles:
#    ax.add_patch(cir)
#    
#fig.canvas.draw()
#a = n.calcPoints(circles)
#for points in a:
#    plt.plot(points[0], points[1], 'ro')
#_______________^^^^_______________

plt.show()