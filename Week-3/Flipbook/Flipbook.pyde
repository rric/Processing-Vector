# Copyright 2021 Roland Richter
# Demonstration of the "flip book" effect
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

def setup():
    size(800, 600)
    # frameRate(60)   # <- try out and change it


def draw():
    background("#87CEEB") # "Light sky blue"

    drawSunPlus(42, 84/2)
    drawSunPlus(width-42, mouseY)
    drawSunPlus(mouseX, mouseY)

    # Displays current frame rate and count
    textSize(28)
    fill(0)
    text(str(frameCount) + " frames", 8, height-50)
    text(nf(frameRate, 1, 1) + " fps", 8, height-20)


# Draws an orange sun with a "+" mark at the center
def drawSunPlus(x, y):
    noStroke()
    fill("#FF4500") # "Orange-red"
    circle(x, y, 42)
    
    # Draw a black "+" mark at position (x, y)
    stroke(0)
    line(x-8, y, x+8, y)
    line(x, y-8, x, y+8)
