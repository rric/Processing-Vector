# Copyright 2021 Roland Richter
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

# Liste aller Positionen der Figur
posList = []

vecSign = +1
vecName = 'a'

vecLabelList = []


def setup():
    global posList
    
    size(800, 600)
    
    startPos = PVector(200, 300)
    posList = [startPos]


# Thanks, chris! https://stackoverflow.com/a/55115215
def nextLetter(s):
    return chr((ord(s.lower())+1 - 97) % 26 + 97)


def mousePressed():
    global posList, randomObject, vecSign, vecName
    
    # linke Maustaste: füge Maus-Position hinzu
    if mouseButton == LEFT:
        mouseVec = PVector(mouseX, mouseY) - posList[-1]
        posList.append(posList[-1] + vecSign * mouseVec)
        
        vecLabel = ("-" if vecSign == -1 else "") + vecName
        vecLabelList.append(vecLabel)
        
        vecSign = +1
        vecName = nextLetter(vecName)
    
    # rechte Maustaste: starte das Spiel von vorne
    elif mouseButton == RIGHT:
        randomObject = int(random(1,26))
        vecSign = +1
        vecName = 'a'
        startPos = PVector(200, 300)
        posList = [startPos]


# Mausrad: ändere Vorzeichen des momentanen Vektors
def mouseWheel(event): 
    global vecSign
    vecSign = +1 if event.getCount() < 0 else -1


def draw():
    background("#191970") # MidnightBlue

    # zeichne alle Positionen und die Vektoren zwischen ihnen
    showPositions(posList, "#4682B4", ["Start (200|300)"]) # SteelBlue
    showVectors(posList, vecLabelList)
    
    # die letzte Position ist das letzte Element in der Liste
    lastPos = posList[-1]
    
    targetPos = PVector(600, 300)
    showPosition(targetPos, "#FFD700", "Ziel (600|300)") # Gold
    
    textSize(16)
    stroke(255)
    fill(255)
    text("Verwende Vektoren, um die Figur ins Ziel zu bringen:", 10, 10)
    text("du musst mindestens drei Vektoren addieren;", 10, 36)
    text("der letzte Vektor muss negatives Vorzeichen haben.", 10, 62)
    
    d = PVector.dist(lastPos, targetPos)
    
    lastSign = +1
    if len(vecLabelList):
        lastSign = -1 if vecLabelList[-1].startswith("-") else +1

    if len(posList) >= 3 and d < 3.0 and lastSign == -1:
        textSize(28)
        fill(255)
        textAlign(CENTER)
        text("Ziel erreicht!", width/2, 2*height/3)
        return
    
    mousePos = PVector(mouseX, mouseY)

    # falls das Vorzeichen des Vektors + ist, 
    #   zeichne die Figur an der Maus-Position,
    #   und den Vektor von der letzten Position zur Maus-Position
    if vecSign == +1:
        drawSomething(randomObject, mousePos)
        showVector(lastPos, mousePos, vecName)
    # falls aber das Vorzeichen des Vektors - ist ("Gegenvektor"), 
    #   zeichne die Figur an der letzten Position,
    #   und drehe den Vektor um: also von der Maus-Position zur letzten Position 
    elif vecSign == -1:
        drawSomething(randomObject, lastPos)
        showVector(mousePos, lastPos, "-" + vecName)

    
