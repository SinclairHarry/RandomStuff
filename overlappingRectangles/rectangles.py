import random
import numpy as np
import tkinter as tk
from time import perf_counter



class Rectangle:
    def __init__(self, maxSideLength, gridSide):
        #Declaring variables
        self.sideX = random.randint(80,maxSideLength)
        self.sideY = random.randint(80,maxSideLength)
        self.angle = random.randint(0,89)*np.pi/180
        self.colour = '#'
        self.ColourPicker()

        #Trig calculations to find direction of line after rotation
        xAfterRotation = [self.sideX * np.cos(self.angle), -self.sideX * np.sin(self.angle)]
        yAfterRotation = [self.sideY * np.sin(self.angle), self.sideY * np.cos(self.angle)]
        xlimit = int(np.floor(np.abs(yAfterRotation[0]) + np.abs(xAfterRotation[0])))

        #Finding where to place one corner so that the rectangle is not drawn outside of the scene
        self.centre = [random.randint(5, gridSide - xlimit), random.randint(max(0, 4-int(np.ceil(xAfterRotation[1]))), min(gridSide, gridSide - int(np.floor(yAfterRotation[1]))))]
        self.points = [self.centre,
                       [self.centre[0] + xAfterRotation[0], self.centre[1] + xAfterRotation[1]],
                       [self.centre[0] + xAfterRotation[0] + yAfterRotation[0], self.centre[1] + xAfterRotation[1] + yAfterRotation[1]],
                       [self.centre[0] + yAfterRotation[0], self.centre[1] + yAfterRotation[1]],
                       [self.centre]         
        ]
    
    #Randomly picks 6 hex values to get a random colour
    def ColourPicker(self):
        for i in range(6):
            self.colour += COLOURS[0][random.randint(0,15)]
    
    #Prints out all the details about the Rect when printing the object out
    def __str__(self):
        return(f"Side X: {self.sideX}\nSide Y: {self.sideY}\nAngle: {self.angle*180/np.pi}\nCentre: {self.centre}\nColour: {self.colour}")

class Grid:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=GRIDSIZE, height=GRIDSIZE)
        self.canvas.pack()

    #Creates a rectangle, prints out the randomized info, draws to grid.
    def AddRectToGrid(self, statsArray):
        rect = Rectangle(MAXSIDELENGTH, GRIDSIZE)
        statsArray.append(GradientSolver(rect.points))
        self.canvas.create_line(rect.points,fill=rect.colour)
        return statsArray

def GradientSolver(pointArray):
    horizGradient = (pointArray[1][0]-pointArray[0][0])/(pointArray[1][1]-pointArray[0][1])
    vertGradient = -1/horizGradient
    horizC = pointArray[1][1]-horizGradient*pointArray[1][0]
    vertC = pointArray[1][1]-vertGradient*pointArray[1][0]
    return [[horizGradient,horizC],[vertGradient,vertC]]

#Hex values 
COLOURS = ["0123456789abcdef"]
GRIDSIZE = 800
RECTNUM = 2

#This allows for a maximum sized square where the sides are 1/sqrt(2) of the screen length. This makes the furthest corner to corner distance == gridsize.
MAXSIDELENGTH = int(np.floor(GRIDSIZE/np.sqrt(2))-5)

statsArray = []

#Setup Tkinter root
root = tk.Tk()
grid = Grid(root)

#Rectangle spawn
startTime = perf_counter()
for i in range(RECTNUM):
    grid.AddRectToGrid(statsArray)
finTime = perf_counter()-startTime
print(finTime)


print(statsArray)

#Start
root.mainloop()


