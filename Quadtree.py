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
    
    def __init__(self, center, halfdimension):
        
        self.center = center
        self.hd = halfdimension
        
    def contains(self, x, y):
        if self.center == (x, y):
            return True
        return False

class Node:   
  ##### Might be wrong approach, probably cant handle overlapping shapes. Might rewrite for image processing.  
    def __init__(self, radius=None, circcenter=None, center=None, dimension=None, root=None, resolution=None, circleres=None):
        
    # _________DEFAULTS_________
        if radius == None:
            self.radius = 0
        else:
            self.radius = radius
        if circcenter == None:
            self.circcenter = (0,0)
        else:
            self.circcenter = circcenter
        if center == None:
            self.center = (0,0)
        else:
            self.center = center
        if dimension == None:
            self.dimension = 0
        else:
            self.dimension = dimension
        if root == None: # True or False
            self.root = False
        else:
            self.root = root
        if resolution == None:
            self.resolution = 1
        else:
            self.resolution = resolution
        if circleres == None:
            self.circleres = 0.2
        else:
            self.circleres = circleres
        
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None
        self.box = AABB(self.center, (self.dimension/2))
    
    # This method will only be called by the root node at the beginning of mapping
    def calcPoints(self, circ):
        cp = list() #circle points
        val = list()
        xy = list()
        print circ[0].center
 
        for i in range(len(circ)): # For each circle...
            temp = circ[i].radius*2*math.pi/self.circleres
            numPoints = int(temp) # The number of points in the circle
            angleInterval = 360/temp # Angular interval between points
            curAngle = 0.0000001 # Counter to keep track of current angle
            points = list() # A temporary list of points
            val =  range(len(circ))
            print val
            
            for j in range(numPoints): # Find all points on perimeter of circle within circle resolution
                points.append((circ[i].center[0]+circ[i].radius*math.cos(2*math.pi/numPoints*j), 
                               circ[i].center[1]+circ[i].radius*math.sin(2*math.pi/numPoints*j)))
                curAngle += angleInterval
                
            print angleInterval
            cp.append(points) # Add points to total list of circle points; each circle has its own list
            
            # This should remove the points in the union of the current and previous circles.
            # I am doing this to prevent looking at points that are not on the perimeter of a compound shape
            
            toRemove = list() #list of points to remove
            tempPointList = list()
#            if i>0: # If this is not the first circle...
#                
#                for f in range(len(cp[i])-1): # for each point in this circle...
#                    print f, len(cp[i])
#                
#                for f in range(len(cp[i])-1): # for each point in this circle...
#                    print f, range(len(cp[i]))[f]
#                    
#                    if f > len(cp[i])-1:
#                        print range(len(cp[i-1])), i-1
#                        print range(len(cp[i])-1), i, len(cp[i])-1
#                        print 'hold'
#                        
#                    for p in range(len(cp[i-1])): # check to see if it is in the prev circle
#                        if (cp[i][f][0] - cp[i-1][p][0])**2 + (cp[i][f][1] - cp[i-1][p][1])**2 < circ[i-1].radius**2:
#                            toRemoveCur.append(cp[i][f]) # Add point to removal list 
#                
#                for k in range(len(cp[i-1])-1): # and vice versa
#                    for p in range(len(cp[i])): # Other has to check each point in the current circle
#                        if (cp[i-1][k][0] - cp[i][p][0])**2 + (cp[i-1][k][1] - cp[i][p][1])**2 < circ[i].radius**2:
#                            toRemovePrev.append(cp[i-1][k]) # Add point to removal list
##                if len(toRemove) != 0:
##                    cp[i-1].remove(toRemove) # remove points
#                
#                cp[i] = [x for x in cp[i] if x not in toRemoveCur] # remove points from current circle
#                cp[i-1] = [x for x in cp[i-1] if x not in toRemovePrev] # remove points from previous circle
        for i in range(len(cp)): # Now that we have all the points; i is the index of the current circle...
            tempPointList = list()        
            for f in range(len(cp[i])): # For each point in this circle; f is the index of the current point...
                print f, range(len(cp[i]))[f]
                            
                for c in range(len(cp)): # Check to see if it's points lie in other circles; c is the index of another circle
                    
                    if c!=i and (cp[i][f][0] - circ[c].center[0])**2 + (cp[i][f][1] - circ[c].center[1])**2 < circ[c].radius**2:
#                        a = toRemove[c]
#                        a = cp[i]
#                        a = cp[i][f]
                       tempPointList.append(cp[i][f]) # Add point to removal list
                       
            # Now we should have a list of points in this circle that are in other circles...
            
            toRemove.append(tempPointList)        
#                for k in range(len(cp[i-1])-1):
#                    for c in range(len(cp)): # See if points in other circles 
#                        if (cp[c][k][0] - cp[c].center[0])**2 + (cp[i-1][k][1] - cp[c].center[1])**2 < circ[c].radius**2:
#                            toRemovePrev.append(cp[i-1][k]) # Add point to removal list
    #                if len(toRemove) != 0:
    #                    cp[i-1].remove(toRemove) # remove points
        # Now we can go through the the list of points to remove
        for remove in range(len(toRemove)):# remove is the index of the list of points we want to remove; should be the same index as the corresponding circle    
                temp = [x for x in cp[remove] if x not in toRemove[remove]] # remove points from current circle
                cp[remove] = temp
#                cp[i-1] = [x for x in cp[i-1] if x not in toRemovePrev] # remove points from previous circle
                
        for circle in cp:
            xy.append(np.array(zip(*circle)))
        
        return xy       
        #______________in Progress______________
#    def contains():
#        if self.box.hd > 1 and self.radius < math.sqrt((circcenter[0]-center[0])**2+(circcenter[1]-center[1])**2):
#            if
    
#    def _call_(self, event):
        
        