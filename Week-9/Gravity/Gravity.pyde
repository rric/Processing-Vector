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

# User interaction depends on three states:
# - Ready: the shape is displayed at the current mouse position
# - Aim: when the left mouse button is pressed, the shape is 
#        fixed at the current mouse position; one can now aim
#        in any direction, indicated by a vector
# - Flying: when the left mouse button is released, the shape
#        starts to fly in the direction of the vector; every
#        0.2 sec, the new position is computed; all previous
#        positions are also displayed.
Ready, Aim, Flying = range(3)
state = Ready
maxPosListLen = 25

objectNum = int(random(1,26))
objectPos = PVector(0,0)
objectPosList = []
speedVec = PVector(0,0)
gravityVec = PVector(0,50)
SunPos = PVector(0,0)


def setup():
    global SunPos
    size(960, 720)
    SunPos = PVector(width/2, height/2)
    
    # Ready and Aim: frame rate 60; Flying: frame rate 5
    frameRate(60)


def mousePressed():
    global state, objectNum, objectPos
    
    # if left mouse button pressed: start to aim
    if mouseButton == LEFT and state == Ready:
        objectPos = PVector(mouseX, mouseY)
        state = Aim
        
    # if right mouse button pressed: re-start game
    if mouseButton == RIGHT:
        frameRate(60)
        objectNum = int(random(1,26))
        state = Ready
        
        
def mouseReleased():
    global state, maxPosListLen, objectPosList, speedVec 
    
    # if left mouse button released: start to fly!
    if mouseButton == LEFT and state == Aim:
        
        objectPosList = [copy.copy(objectPos)]
        speedVec = objectPos - PVector(mouseX, mouseY)
        
        state = Flying
        maxPosListLen = 25
        
        # Ready and Aim: frame rate 60; Flying: frame rate 5
        frameRate(5)
        
        
def mouseWheel(event):
    global maxPosListLen
    e = event.getCount()
    maxPosListLen = max(0, maxPosListLen + event.getCount())


def draw():
    global objectPos, objectPosList, gravityVec, speedVec
    
    background("#191970") # MidnightBlue

    txt = ""
    if state == Ready:
        txt = "Ready ..."
    elif state == Aim:
        txt = "Aim ... v = " + nf(speedVec.mag(), 1, 1) + " px/s"
    elif state == Flying:
        txt = "Fly! "
        txt += " d = " + nf(PVector.dist(objectPos, SunPos), 1, 1) + " px,"
        txt += " v = " + nf(speedVec.mag(), 1, 1) + " px/s"
    
    textAlign(LEFT, CENTER)
    textSize(16)
    fill(255)
    text(txt, 8, height-20)

    showPosition(SunPos, "#FFFF00", letter = "S")
    
    if state == Ready:
        drawSomething(objectNum, PVector(mouseX, mouseY))
        
    elif state == Aim:
        drawSomething(objectNum, objectPos)
        speedVec = objectPos - PVector(mouseX, mouseY)
        showVector(objectPos, objectPos + speedVec)
        
    elif state == Flying:
        # cannot use frameRate here, as it is *averaged* over several frames
        factor = 1./5.
        
        # Calculate the new position
        gravityFactor = 1./(PVector.dist(objectPos, SunPos)**2)
        gravityMag = 5000000. * gravityFactor
        gravityVec = (SunPos - objectPos).setMag(gravityMag)
    
        # print(" gravity factor: " + nf(gravityFactor, 1, 10) + 
        #       " => magnitude: " + nf(gravityMag, 1, 1))
        # print(gravityVec)
        
        showVector(SunPos - gravityVec, SunPos, "F", 0, 3)
        
        speedVec += factor * gravityVec
        objectPos += factor * speedVec
        
        # Add (a copy of the) new position to the list ...
        objectPosList.append(copy.copy(objectPos))
        
        while len(objectPosList) > maxPosListLen:
            objectPosList.pop(0)

        # ... and draw the complete list.
        showPositions(objectPosList)
        showVectors(objectPosList)
        drawSomething(objectNum, objectPos)
        
