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

import copy

from ShowHelpers import *
from Collection import *

# Das Programm läuft in drei Phasen ab:
# - Ready: die Figur wird nur an der Maus-Position angezeigt
# - Aim: sobald der Benutzer die linke Maustaste gedrückt hat,
#        wird die Figur an der Maus-Position beim Drücken angezeigt; 
#        mit einem Vektor kann in alle Richtungen gezielt werden
# - Flying: sobald der Benutzer die linke Maustaste wieder los
#        gelassen hat, fliegt das Objekt in die gewählte Richtung 
#        davon; alle 0.2 sec wird die aktuelle Position neu 
#        berechnet; alle bisherigen Positionen werden angezeigt.
Ready, Aim, Flying = range(3)
state = Ready

objectNum = int(random(1,26))
objectPos = PVector(0,0)
objectPosList = []
speedVec = PVector(0,0)


def setup():
    size(800, 600)
    frameRate(5)


def mousePressed():
    global state, objectNum, objectPos
    
    # linke Maustaste gedrückt: beginne zu zielen
    if mouseButton == LEFT and state == Ready:
        objectPos = PVector(mouseX, mouseY)
        state = Aim
        
    # rechte Maustaste gedrückt: beginne neuen Durchgang
    if mouseButton == RIGHT:
        objectNum = int(random(1,26))
        state = Ready
        
        
def mouseReleased():
    global state, objectPosList, speedVec 
    
    # linke Maustaste losgelassen: fliege los!
    if mouseButton == LEFT and state == Aim:
        objectPosList = [copy.copy(objectPos)]
        speedVec = objectPos - PVector(mouseX, mouseY)
        state = Flying
        
        
def draw():
    global objectPos, objectPosList, speedVec
    
    background("#191970") # MidnightBlue

    txt = ""
    if state == Ready:
        txt = "Bereit ..."
    elif state == Aim:
        txt = "Zielen ... v = " + nf(speedVec.mag(), 1, 1) + " px/s"
    elif state == Flying:
        txt = "Fliegen! v = " + nf(speedVec.mag(), 1, 1) + " px/s"
        
    textSize(16)
    fill(255)
    text(txt, 8, height-20)

    if state == Ready:
        drawSomething(objectNum, PVector(mouseX, mouseY))
        
    elif state == Aim:
        drawSomething(objectNum, objectPos)
        speedVec = objectPos - PVector(mouseX, mouseY)
        showVector(objectPos, objectPos + speedVec)
        
    elif state == Flying:
        # Berechne die neue Position der Figur
        # TODO Beschreibe mit eigenen Worten, wie die neue Position
        #   hier berechnet wird.
        factor = 1./frameRate
        objectPos += factor * speedVec
        
        # Füge (eine Kopie der neuen) Position zur Liste hinzu ...
        objectPosList.append(copy.copy(objectPos))

        # ... und zeichne die gesamte Liste.
        showPositions(objectPosList)
        showVectors(objectPosList)
        drawSomething(objectNum, objectPos)
        
        # Pralle vom unteren Rand des Fensters ab
        if objectPos.y > height:
            speedVec.y = -speedVec.y
        
        # TODO Die Figur prallt derzeit nur vom unteren Rand ab.
        #   Erweitere das Programm so, dass die Figur von *allen*
        #   Rändern abprallt.
