# Copyright 2020, 2021 Roland Richter
# Virtual spray can with simple graphical user interface
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

# This sketch uses a background image,
# 540px-David_by_Michelangelo_JBU06.JPG by Jörg Bittner Unna, 
# CC BY 3.0, https://commons.wikimedia.org/w/index.php?curid=38304749

# positions and colors of the color buttons
firstX, firstY = 470, 30
firstColor = color(255, 99, 71)   # Tomato

secondX, secondY = 510, 30
secondColor = color(0, 255, 0)    # Lime

# radius, color, and opacity of the brush
brushRadius = 19
brushColor = firstColor
opacity = 24


def setup():
    # use "David" as background; it is of size 540 x 720
    size(540, 720)
    david = loadImage("540px-David_by_Michelangelo_JBU06.JPG");
    background(david)

    # use cross cursor to indicate paint tool
    cursor(CROSS)
    
    # use the radius, not the extent, to draw circles
    ellipseMode(RADIUS)
    strokeWeight(2)

    drawButtons()


def draw():
    noStroke()

    # paint on background image, but NOT on buttons
    if mousePressed:
        if not (mouseX >= 440 and mouseY <= 70):
            fill(brushColor, opacity)
            circle(mouseX, mouseY, brushRadius)


def mouseClicked():
    global brushColor

    # if one of the color buttons was clicked,
    # select the brush color accordingly
    if dist(mouseX, mouseY, firstX, firstY) < brushRadius:
        brushColor = firstColor
    elif dist(mouseX, mouseY, secondX, secondY) < brushRadius:
        brushColor = secondColor

    drawButtons()


# Draws the buttons to select the brush color; the button which
# is selected is indicated with a white border
def drawButtons():
    stroke(255) if brushColor == firstColor else stroke(0)
    fill(firstColor)
    circle(firstX, firstY, brushRadius)

    stroke(255) if brushColor == secondColor else stroke(0)
    fill(secondColor)
    circle(secondX, secondY, brushRadius)
