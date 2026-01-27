from PIL import Image
import numpy as np
from time import perf_counter
from pathlib import Path

#Generates a x by x grid based on sidelength input.
def GenerateGrid(sideLength):
    
    #Grid default value is " . " - small placeholder
    gridSide = [0 for x in range(sideLength)] 
    grid = [gridSide.copy() for x in range(sideLength)]
    return grid

#Calculates where the circle should go onto the grid
def CircleOverlay(grid, sideLength):

    #Tolerance required as array integer may not line up exactly with calculated distance
    tolerance = (sideLength-1)/2
    radius = (sideLength-1)/2

    #Iterates through the grid and calculates if point is a radius' distance away from the centre of the circle
    for yCoord in range(0,len(grid)):
        for xCoord in range(0,len(grid)):

            #If the grid coordinate is within the tolerance of the radius, change the grid value from 0 to 255
            if (yCoord-radius)**2 - tolerance + (xCoord-radius)**2 - tolerance > (radius)**2 or (yCoord-radius)**2 + tolerance + (xCoord-radius)**2 + tolerance < (radius)**2:
                grid[yCoord][xCoord] = 255
    return grid

#Formats the final grid into an image
def CircleFormat(circle):
    array = np.array(circle, dtype=np.uint8)
    newImage = Image.fromarray(array)
    newImage.save(Path(__file__).parent.joinpath("testImage.png"))


#User input
sideLength = int(input("Enter a side length of the square grid you wish to find a circle of: "))

#Stuff
startTime = perf_counter()
grid = GenerateGrid(sideLength)
circle = CircleOverlay(grid, sideLength)
CircleFormat(circle)
finTime = perf_counter()-startTime
print(finTime)