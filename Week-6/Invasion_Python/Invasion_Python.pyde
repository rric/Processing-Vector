# Invasion_Python
# Copyright 2021 Roland Richter
# Demonstrates the usage of lists and loops
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


# no need to import anything

# List of positions of all objects
posList = []

# the minimal distance objects must have from each other
MinimalDistance = 50

# short for "show indices for n further frames"
showIndicesFnFF = 0


def setup():
    global posList, showIndicesFnFF
    
    size(800, 600)
    
    posList.append(PVector(width/2, height/2))
    showIndicesFnFF = 180


def mousePressed():
    global posList, showIndicesFnFF
    
    if mouseButton == LEFT:
        newPos = PVector(mouseX, mouseY)
        
        # The new position newPos is added to the list only
        # if it is not too close to any other position in the list.
        # - compute the distance of newPos to all other positions
        # - only if all other positions are "far away", the new
        #    position can be added to the list
        
        # List comprehesion makes code much shorter in Python:
        # is it more readable as well?
        distList = [PVector.dist(it, newPos) for it in posList]
        
        print("Distances to new position: ")
        println(distList)
        
        allAreFarAway = (min(distList) > MinimalDistance)
        if (allAreFarAway):
            posList.append(newPos)

        showIndicesFnFF = 180

    elif mouseButton == RIGHT:
        pass


def keyPressed():
    global posList, showIndicesFnFF
    
    if (key == 'c' or key == 'C'):
        posList = []

    if (key == 'r' or key == 'R'):
        posList.append(PVector(random(0,width), random(0,height)))
        showIndicesFnFF = 180
        
    # TODO Think of some other keys to add or remove aliens 
    #      to the list here, etc.
    # See https://www.w3schools.com/python/python_lists.asp


def draw():
    global posList, showIndicesFnFF
    
    background("#191970") # "MidnightBlue"
            
    # draw all objects in the list
    if showIndicesFnFF <= 0:
        for pos in posList:
            drawAlien(pos)
    else:
        for i in range(len(posList)):
            drawAlien(posList[i])
            textSize(16)
            fill(255)
            text(str(i), posList[i].x+20, posList[i].y+20)

    showIndicesFnFF -= 1
    
    # display the list's length
    textSize(28)
    fill(255)
    text(str(len(posList)) + " element(s)", 8, height-20)


# Draws Ellen, the alien, at the given position pos
def drawAlien(pos):
    # draw the head
    strokeWeight(2)
    stroke(0)
    fill("#32CD32")
    circle(pos.x, pos.y, 42)
    
    # draws both eyes
    fill("#FFD700")
    circle(pos.x-10, pos.y-10, 12)
    circle(pos.x+10, pos.y-10, 12)
    
    # draws mouth and tentacles
    line(pos.x-6, pos.y+10, pos.x+6, pos.y+10)
    line(pos.x-30, pos.y-30, pos.x-15, pos.y-15)
    line(pos.x+30, pos.y-30, pos.x+15, pos.y-15)
    strokeWeight(1)
