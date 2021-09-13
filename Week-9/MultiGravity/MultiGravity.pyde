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

centerPos = PVector(0,0)
maxPosListLen = 25

class FlyingObject:
    def __init__(self, n = 0):
        self.num = int(random(1,26)) if n == 0 else n
        self.pos = PVector(0,0)
        self.posList = []
        self.speedVec = PVector(0,0)
        self.gravityVec = PVector(0,0)
        
    def startFlying(self, prevPos, startPos):
        self.pos = startPos
        self.posList = [copy.copy(self.pos)]
        self.speedVec = startPos - prevPos
        
    def updateFlying(self, sunPos, factor = 1./5.):
        # determine the gravity vector ...
        gravityFactor = 1./(PVector.dist(self.pos, sunPos)**2)
        gravityMag = 5000000. * gravityFactor
        self.gravityVec = (sunPos - self.pos).setMag(gravityMag)
        
        # ... and update the speed vector and position
        self.speedVec += factor * self.gravityVec
        self.pos += factor * self.speedVec
        
        # add (a copy of) the new position to the list, ...
        self.posList.append(copy.copy(self.pos))
        
        # .. but keep the list short
        while len(self.posList) > maxPosListLen:
            self.posList.pop(0)
        

flying = []

selection = [2,3,5,15,17,18,22]

# authors: 2 - Elisa Antelmann, 3 - Paula Maria Bauer, 
#          5 - Mithad Jan Bogner, 15 - Christian Kaukal,
#         17 - Luisa Mayr, 18 - Sina Mayr, 22 - Eliabeth Schimana

nextNum = selection[int(random(len(selection)))]
mousePressedPos = PVector(0,0)


def setup():
    global centerPos
    
    size(960, 720)
    centerPos = PVector(width/2, height/2)
    
    frameRate(5)


def mousePressed():
    global state, nextNum, mousePressedPos, flying
    
    # if left mouse button pressed: start to aim
    if mouseButton == LEFT and state == Ready:
        mousePressedPos = PVector(mouseX, mouseY)
        state = Aim
        
    # if right mouse button pressed: re-start game
    if mouseButton == RIGHT:
        nextNum = selection[int(random(len(selection)))]
        state = Ready
        
        
def mouseReleased():
    global state, flying
    
    # if left mouse button released: start to fly!
    if mouseButton == LEFT and state == Aim:
        flying.append(FlyingObject(nextNum))
        flying[-1].startFlying(PVector(mouseX, mouseY), mousePressedPos)
        state = Flying

        
def mouseWheel(event):
    global maxPosListLen
    e = event.getCount()
    maxPosListLen = max(0, maxPosListLen + event.getCount())


def draw():
    global flying
    
    background("#191970") # MidnightBlue

    txt = ""
    if state == Ready:
        txt = "Ready ..."
    elif state == Aim:
        txt = "Aim ... "
    elif state == Flying:
        txt = "Fly! "
        txt += " d = " + nf(PVector.dist(flying[-1].pos, centerPos), 1, 1) + " px,"
        txt += " v = " + nf(flying[-1].speedVec.mag(), 1, 1) + " px/s"
    
    textAlign(LEFT, CENTER)
    textSize(16)
    fill(255)
    text(txt, 8, height-20)

    showPosition(centerPos, "#FFFF00", letter = "S")
    
    if state == Ready:
        drawSomething(nextNum, PVector(mouseX, mouseY))
        
    elif state == Aim:
        drawSomething(nextNum, mousePressedPos)
        distVec = mousePressedPos - PVector(mouseX, mouseY)
        showVector(mousePressedPos, mousePressedPos + distVec)
        

    for f in flying:
        f.updateFlying(centerPos, 1./5.)
    
        showVector(centerPos - f.gravityVec, centerPos, "F", 0, 3)

        # ... and draw the complete list.
        showPositions(f.posList)
        showVectors(f.posList)
        drawSomething(f.num, f.pos)
        
