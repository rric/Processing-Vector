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
    drawCircle(beginPos, "#4682B4", "B")
    drawCircle(endPos,   "#87CEEB", "E")
    
    # the vector from beginning point B to end point E is the
    # difference of "end point" minus "beginning point"
    vecBtoE = endPos - beginPos      # vector subtraction
    arrow(beginPos, vecBtoE, "vector B->E")

    # draw objects both at original and at moved positions
    drawAlien(firstPos)
    drawAlien(firstPos + vecBtoE)    # vector addition
    arrow(firstPos, vecBtoE, "vector B->E")

    drawAlien(secondPos)
    drawAlien(secondPos + vecBtoE)   # vector addition
    arrow(secondPos, vecBtoE, "vector B->E")

    drawAlien(thirdPos)
    drawAlien(thirdPos + vecBtoE)    # vector addition
    arrow(thirdPos, vecBtoE, "vector B->E")


# Draws a circle with a "+" mark, "Orange-red" by default,
# and places a letter nearby the "+" mark
def drawCircle(pos, col = "#FF4500", letter = ""):
    noStroke()
    fill(col)
    circle(pos.x, pos.y, 42)
    
    # draw a black "+" mark at position (x, y)
    stroke(0)
    fill(0)
    line(pos.x-8, pos.y, pos.x+8, pos.y)
    line(pos.x, pos.y-8, pos.x, pos.y+8)
    
    # if given, place the letter nearby the "+" mark
    if letter:
        textSize(14)
        textAlign(LEFT, TOP)
        text(letter, pos.x+2, pos.y)


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
    
    
# Draws the vector (vx, vy) as an arrow -->, from the begining point 
# (bx, by) to the end point, and places a label to the middle of it
def arrow(begP, vec, label=""):
    endP = begP + vec

    # the arrow head is drawn as a triangle; compute the coordinates
    # of its points here
    angle = PVector(vec.x, -vec.y).heading()
    leftEnd = endP - 15 * PVector.fromAngle(-angle + 0.4)
    rightEnd = endP - 15 * PVector.fromAngle(-angle - 0.4)

    stroke(255)
    fill(255)
    line(begP.x, begP.y, endP.x, endP.y)
    triangle(endP.x, endP.y, leftEnd.x, leftEnd.y, rightEnd.x, rightEnd.y)

    # translate, rotate, and center the label w.r.t. the arrow
    if label:
        pushMatrix()
        
        translate(lerp(begP.x, endP.x, 0.5), lerp(begP.y, endP.y, 0.5))
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
