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
firstPos  = PVector(42, 420)
secondPos = PVector(420, 420)
thirdPos  = PVector(420, 42)

def setup():
    size(800, 600)


def draw():
    background("#191970") # "MidnightBlue"

    # draw the beginning point (center of frame) and the end
    # point (at mouse position) in shades of blue
    beginPos = PVector(width/2, height/2)
    endPos   = PVector(mouseX, mouseY)
    showPosition(beginPos, "#4682B4", "B")
    showPosition(endPos,   "#87CEEB", "E")
    
    # the vector from beginning point B to end point E is the
    # difference of "end point" minus "beginning point"
    vecBtoE = endPos - beginPos      # vector subtraction
    showVector(beginPos, vecBtoE, "vector B->E")

    # draw objects both at original and at moved positions
    drawAlien(firstPos)
    drawAlien(firstPos + vecBtoE)    # vector addition
    showVector(firstPos, vecBtoE, "vector B->E")

    drawAlien(secondPos)
    drawAlien(secondPos + vecBtoE)   # vector addition
    showVector(secondPos, vecBtoE, "vector B->E")

    drawAlien(thirdPos)
    drawAlien(thirdPos + vecBtoE)    # vector addition
    showVector(thirdPos, vecBtoE, "vector B->E")


# Draws Ellen, the Alien, at the given position (x, y)
def drawAlien(pos):
    # draw the head
    strokeWeight(2)
    stroke(0)
    fill("#32CD32")
    circle(pos.x, pos.y, 42)
    
    # draw both eyes
    fill("#FFD700")
    circle(pos.x-10, pos.y-10, 12)
    circle(pos.x+10, pos.y-10, 12)
    
    # draw mouth and antennas
    line(pos.x-6, pos.y+10, pos.x+6, pos.y+10)
    line(pos.x-30, pos.y-30, pos.x-15, pos.y-15)
    line(pos.x+30, pos.y-30, pos.x+15, pos.y-15)
    strokeWeight(1)

