# -*- coding: utf-8 -*-
"""
Created on Thu Jul 04 10:22:42 2019

File Contents:

    * Quadtree nodes and axis-aligned bounding boxes (AABB)

~~~~~~~~~~INCOMPLETE~~~~~~~~~~

@author: Brandon Townsend
"""



import math
import numpy as np
class AABB:
    
    def _init_(self, center, halfdimension):
        
        self.center = center
        self.hd = halfdimension
        
    def contains(self, x, y):
        if self.center == (x, y):
            return True
        return False

class Node:   
  ##### Might be wrong approach, probably cant handle overlapping shapes. Might rewrite for image processing.  
    def _init_(self, radius, circcenter, center, dimension, root):
        self.root = root # True or False
        self.resolution = 1
        self.circleRes = 0.2
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None
        self.box = AABB(center, dimension/2)
        self.radius = radius
        self.circcenter = circcenter
    
    def calcPoints(circ):
        circlepoints = list()
        
        for i in range(len(circ): # for each circle
            temp = circ[i].center*2*math.pi/self.circleRes
            numPoints = int(temp)
            angleInterval = int(180/temp)
            points = list()
        
            for i in range(numPoints): #find all points on perimeter of circle within circle resolution
                points.append((circ[i].center[0]+circ[i].radius/math.cos(angleInterval), circ[i].center[1]+circ[i].radius/math.sin(angleInterval)))
                angleInterval += angleInterval
                
            circlepoints.append(points) # add points to total list of circle points
            
            # this should remove the points in the union of the current and previous circles
            if i>0:
                for j in range(len(circlepoints[i])): #see if points in this circle are in the prev circle
                    if (circlepoints[i][j][0] - circlepoints[i-1][j][0])**2 + (circlepoints[i][j][1] - circlepoints[i-1][j][1])**2 < circlepoints[i-1].radius**2:
                        circlepoints[i].remove(circlepoints[i][j])
                for j in range(len(circlepoints[i-1])): #and vice versa
                    if (circlepoints[i-1][j][0] - circlepoints[i][j][0])**2 + (circlepoints[i-1][j][1] - circlepoints[i][j][1])**2 < circlepoints[i].radius**2:
                        circlepoints[i-1].remove(circlepoints[i-1][j])
                
                    
        #______________in Progress______________
#    def contains():
#        if self.box.hd > 1 and self.radius < math.sqrt((circcenter[0]-center[0])**2+(circcenter[1]-center[1])**2):
#            if
    
#    def _call_(self, event):
        
        