# Copyright 2021 Roland Richter
# A vector is, basically, an arrow: it has direction and length
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

from ShowHelpers import *

# positions of the objects which will be moved
firstX, firstY   = 42, 420
secondX, secondY = 420, 420
thirdX, thirdY   = 420, 42

def setup():
    size(800, 600)


def draw():
    background("#191970") # "MidnightBlue"

    # draw the beginning point (center of frame) and the end
    # point (at mouse position) in shades of blue
    beginX, beginY = width/2, height/2
    endX, endY = mouseX, mouseY
    showPosition(beginX, beginY, "#4682B4", "B")
    showPosition(endX,   endY,   "#87CEEB", "E")
    
    # the vector from beginning point B to end point E is the
    # difference of "end point" minus "beginning point"
    beX, beY = endX - beginX, endY - beginY
    showVector(beginX, beginY, beX, beY, "vector B->E")

    # draw objects both at original and at moved positions
    drawAlien(firstX, firstY)
    drawAlien(firstX + beX, firstY + beY)
    showVector(firstX, firstY, beX, beY, "vector B->E")
    
    drawAlien(secondX, secondY)
    drawAlien(secondX + beX, secondY + beY)
    showVector(secondX, secondY, beX, beY, "vector B->E")

    drawAlien(thirdX, thirdY)
    drawAlien(thirdX + beX, thirdY + beY)
    showVector(thirdX, thirdY, beX, beY, "vector B->E")


# Draws Ellen, the Alien, at the given position (x, y)
def drawAlien(x, y):
    # draw the head
    strokeWeight(2)
    stroke(0)
    fill("#32CD32")
    circle(x, y, 42)
    
    # draw both eyes
    fill("#FFD700")
    circle(x-10, y-10, 12)
    circle(x+10, y-10, 12)
    
    # draw mouth and antennas
    line(x-6, y+10, x+6, y+10)
    line(x-30, y-30, x-15, y-15)
    line(x+30, y-30, x+15, y-15)
    strokeWeight(1)
    
    
