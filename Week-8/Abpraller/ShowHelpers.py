# Copyright 2021 Roland Richter
# Helper functions to show positions, vectors, etc
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

from __future__ import division

# Draws a circle with a "+" mark, "Orange-red" by default,
# and places the given letter nearby the "+" mark
def showPosition(pos, col = "#FF4500", letter = ""):
    noStroke()
    fill(col)
    circle(pos.x, pos.y, 42)
    
    # draw a black "+" mark at position pos
    strokeWeight(1)
    stroke(0)
    fill(0)
    line(pos.x-8, pos.y, pos.x+8, pos.y)
    line(pos.x, pos.y-8, pos.x, pos.y+8)
    
    # if given, place the letter nearby the "+" mark
    if letter:
        textSize(14)
        textAlign(LEFT, TOP)
        text(letter, pos.x+2, pos.y)


# Draws a sequence of circles at the given positions, with colors
# lerped from gray to the given color
def showPositions(posList, col = "#FF4500", labelList = []):
    gray = color(64, 64, 64)
    n = len(posList)
    
    for k in range(n):
        lerpedCol = lerpColor(gray, col, (k+1)/n)
        showPosition(posList[k], lerpedCol, 
                     labelList[k] if k < len(labelList) else "")
        

# Draws a vector as an arrow --> from the begining point begPos to
# the end point endPos, and places a label at the middle of it
def showVector(begPos, endPos, label="", bright=255, weight=1):
    vec = endPos - begPos

    # the arrow head is drawn as a triangle; compute the coordinates
    # of its points here
    angle = PVector(vec.x, -vec.y).heading()
    leftEnd = endPos - 15 * PVector.fromAngle(-angle + 0.4)
    rightEnd = endPos - 15 * PVector.fromAngle(-angle - 0.4)

    strokeWeight(weight)
    stroke(bright)
    fill(bright)
    line(begPos.x, begPos.y, endPos.x, endPos.y)
    triangle(endPos.x, endPos.y, leftEnd.x, leftEnd.y, rightEnd.x, rightEnd.y)

    # translate, rotate, and center the label w.r.t. the arrow
    if label:
        pushMatrix()
        
        translate(lerp(begPos.x, endPos.x, 0.5), lerp(begPos.y, endPos.y, 0.5))
        if angle > -HALF_PI and angle < HALF_PI:
            rotate(-angle)
        else:
            rotate(PI-angle)
        
        textSize(14)
        textAlign(CENTER, CENTER)
        text(label, 0, -9)
        text("(" + nfp(int(vec.x), 0) + "," 
                 + nfp(int(vec.y), 0) + ")", 0, 9)
        popMatrix()
        
        
# Draws a sequence of vectors, from one position to the next
def showVectors(posList, labelList = []):
    n = len(posList)
    
    for k in range(n-1):
        lerpedBright = lerpColor(64, 255, (k+1)/n)
        showVector(posList[k], posList[k+1],
              labelList[k] if k < len(labelList) else "",
              lerpedBright)
        
    if n > 2:
        lbl = labelList[0] if 0 < len(labelList) else ""
        for k in range(1,n-1):
            lbl += " + " + labelList[k] if k < len(labelList) else ""

        showVector(posList[0], posList[-1], lbl, 255, 3)
        
