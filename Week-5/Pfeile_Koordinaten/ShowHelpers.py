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


# Draws a circle with a "+" mark, "Orange-red" by default,
# and places a letter nearby the "+" mark
def showPosition(x, y, col = "#FF4500", letter = ""):
    noStroke()
    fill(col)
    circle(x, y, 42)
    
    # draw a black "+" mark at position (x, y)
    stroke(0)
    fill(0)
    line(x-8, y, x+8, y)
    line(x, y-8, x, y+8)
    
    # if given, place the letter nearby the "+" mark
    if letter:
        textSize(14)
        textAlign(LEFT, TOP)
        text(letter, x+2, y)


# Draws the vector (vx, vy) as an arrow -->, from the begining point 
# (bx, by) to the end point, and places a label to the middle of it
def showVector(bx, by, vx, vy, label=""):
    ex, ey = bx + vx, by + vy

    # the arrow head is drawn as a triangle; compute the coordinates
    # of its points here
    angle = PVector(vx, -vy).heading()
    leftend = PVector(ex, ey) - 15 * PVector.fromAngle(-angle + 0.4)
    rightend = PVector(ex, ey) - 15 * PVector.fromAngle(-angle - 0.4)

    stroke(255)
    fill(255)
    line(bx, by, ex, ey)
    triangle(ex, ey, leftend.x, leftend.y, rightend.x, rightend.y)

    # translate, rotate, and center the label w.r.t. the arrow
    if label:
        pushMatrix()
        
        translate(lerp(bx, ex, 0.5), lerp(by, ey, 0.5))
        if angle > -HALF_PI and angle < HALF_PI:
            rotate(-angle)
        else:
            rotate(PI-angle)
        
        textSize(14)
        textAlign(CENTER, CENTER)
        text(label, 0, -9)
        text("(" + nfp(int(vx), 0) + "," 
                 + nfp(int(vy), 0) + ")", 0, 9)
        popMatrix()
