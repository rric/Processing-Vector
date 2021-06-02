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

def setup():
    size(800, 600)

northNum, eastNum, southNum, westNum = 1, 2, 3, 4

def mousePressed():
    global northNum, eastNum, southNum, westNum
    if mouseButton == LEFT:
        northNum = int(random(1,26))
        eastNum = int(random(1,26))
        southNum = int(random(1,26))
        westNum = int(random(1,26))


def draw():
    background("#191970") # "MidnightBlue"

    # zeichne die Anfangs-Position in der Mitte des Bildes
    centerPos = PVector(width/2, height/2)
    showPosition(centerPos, "#4682B4")

    # der Vektor von Anfangs-Position zu End-Position ist die
    # Differenz: "End-Position minus Anfangs-Position"
    northVec = PVector(mouseX, mouseY) - centerPos
    
    drawSomething(northNum, centerPos + northVec)
    showVector(centerPos, northVec, "Vektor N")

    # HAUSÜBUNG Beschreibe, was hier berechnet wird
    eastVec = PVector(-northVec.y, northVec.x)
    
    drawSomething(eastNum, centerPos + eastVec)
    showVector(centerPos, eastVec, "Vektor E")    
    
    # HAUSÜBUNG Beschreibe, was hier berechnet wird
    southVec = PVector(-northVec.x, -northVec.y)
    
    drawSomething(southNum, centerPos + southVec)
    showVector(centerPos, southVec, "Vektor S")

    # HAUSÜBUNG Beschreibe, was hier berechnet wird
    westVec = PVector(northVec.y, -northVec.x)
    
    drawSomething(westNum, centerPos + westVec)
    showVector(centerPos, westVec, "Vektor W") 
