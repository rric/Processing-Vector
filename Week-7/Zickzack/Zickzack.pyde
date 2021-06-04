# Copyright 2021 Roland Richter
# Ein Vektor ist ein Pfeil: er hat eine Richtung und eine Länge
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
from Collection import *

randomObject = int(random(1,26))

posList = []
vecName = 'a'
scalar = 1.0
labelsList = []


def setup():
    size(800, 600)
    centerPos = PVector(width/2, height/2)
    posList.append(centerPos)

# Thanks, chris! https://stackoverflow.com/a/55115215
def nextLetter(s):
    return chr((ord(s.lower())+1 - 97) % 26 + 97)


def mousePressed():
    global randomObject, scalar, vecName
    
    if mouseButton == LEFT:
        mouseVec = PVector(mouseX, mouseY) - posList[-1]
        posList.append(posList[-1] + scalar * mouseVec)
        labelsList.append(nf(scalar) + "*" + vecName)
        
        scalar = 1.0
        vecName = nextLetter(vecName)
        
    elif mouseButton == RIGHT:
        randomObject = int(random(1,26))


def mouseWheel(event): 
    global scalar
    # e = -event.getCount()
    # scalar += 0.05 * e
    scalar = +1 if event.getCount() < 0 else -1


def draw():
    background("#191970") # "MidnightBlue"

    # zeichne die Anfangs-Position in der Mitte des Bildes
    showPositions(posList, "#4682B4")
    showVectors(posList, labelsList)
    
    currentPos = posList[-1]
    mouseVec = PVector(mouseX, mouseY) - currentPos
    scaledVec = scalar * mouseVec   # Multiplikation Skalar mal Vektor
    
    drawSomething(randomObject, currentPos + scaledVec)
    currentLabel = nf(scalar) + "*" + vecName
    showVector(currentPos, scaledVec, currentLabel)
