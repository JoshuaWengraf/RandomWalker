# -*- coding: utf-8 -*-
"""
Created on 01/06/2021

@author: Joshua

Plots the path of a random walker. Simulation finishes once the walker 
reaches the edge of the grid 


"""

import random
import numpy as np
import matplotlib.pyplot as plt

class randomWalker:
     def __init__(self, x, y):
         self.x = x
         self.y = y
         
     def moveWalker(self, amount_x, amount_y):
         self.x = self.x + amount_x
         self.y = self.y + amount_y

gridSize = 200

dx = np.array([1, 0])
dy = np.array([0, 1])
steps = [dx, -dx, dy, -dy]

grid = np.zeros([gridSize+1, gridSize+1])

ctr = 0
walking = True

walker = randomWalker(int(gridSize/2), int(gridSize/2))

while(walking == True):
    amount_x, amount_y = random.choice(steps)
    walker.moveWalker(amount_x, 0)
    walker.moveWalker(0, amount_y)

    if walker.x > gridSize or walker.y > gridSize or walker.y < 0 or walker.x < 0:
        walking == False
        break

    grid[walker.x, walker.y] = 1

    ctr = ctr + 1

    if ctr % 100 == 0:
        print(ctr)
        plt.imsave('randomWalk_' + str(int(ctr/2)) + '.png', grid)

plt.figure()
plt.imshow(grid)

plt.xticks([]) #remove plot axis lines
plt.yticks([])

