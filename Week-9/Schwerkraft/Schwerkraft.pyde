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

objectN = int(random(1,26))

Ready, Aim, Flying = range(3)
state = Ready

pos = PVector(0,0)
posList = []

speedVec = PVector(0,0)
gravityVec = PVector(0,50)


def setup():
    size(800, 600)
    frameRate(5)


def mousePressed():
    global objectN, state, pos
    
    # linke Maustaste gedrückt: beginne zu zielen
    if mouseButton == LEFT and state == Ready:
        state = Aim
        pos = PVector(mouseX, mouseY)
        
    # rechte Maustaste gedrückt: beginne neuen Durchgang
    if mouseButton == RIGHT:
        objectN = int(random(1,26))
        state = Ready
        
        
def mouseReleased():
    global state, pos, posList, speedVec 
    
    # linke Maustaste losgelassen: fliege los!
    if mouseButton == LEFT and state == Aim:
        posList = [copy.copy(pos)]
        speedVec = pos - PVector(mouseX, mouseY)
        state = Flying
        
        
def draw():
    global pos, posList, speedVec
    
    background("#191970") # MidnightBlue

    if state == Ready:
        drawSomething(objectN, PVector(mouseX, mouseY))
        
    elif state == Aim:
        drawSomething(objectN, pos)
        aimVec = pos - PVector(mouseX, mouseY)
        showVector(pos, pos + aimVec)
        
    elif state == Flying:
        factor = 1./frameRate
        speedVec += factor * gravityVec
        pos += factor * speedVec
        
        posList.append(copy.copy(pos))
        # println(posList)

        showPositions(posList)
        showVectors(posList)
        drawSomething(objectN, pos)
        
        if pos.y > height:
            speedVec.y = -speedVec.y
            
        if pos.y < 0:
            speedVec.y = -speedVec.y
            
        if pos.x < 0:
            speedVec.x = -speedVec.x
            
        if pos.x > width:
            speedVec.x = -speedVec.x            
            
            
