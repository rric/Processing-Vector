# Copyright 2021 Paula Bauer, Leonie Fehrer, Christian Kaukal, Lena Lorenz,
#   Luisa Mayr, Nina Müllner, Eliabeth Schimana, Roland Richter
# und -- hoffentlich -- bald noch vielen, vielen anderen!

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

from collection import *

def setup():
    size(1000, 700)


def draw():
    background("#87CEEB") # "Light sky blue"

    offsetX, offsetY = -120, -40
    drawTeddyBear(mouseX + offsetX, mouseY + offsetY)

    offsetX, offsetY = -80, +90
    draw_duck(mouseX + offsetX, mouseY + offsetY, 1.0)

    offsetX, offsetY = 120, +70
    drawHouse(mouseX + offsetX, mouseY + offsetY, "#E92DED")

    offsetX, offsetY = 60, -50
    drawLadybug(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = -350, +40
    drawLeoniesAlien(mouseX + offsetX, mouseY + offsetY)    
    
    offsetX, offsetY = -200, +50
    drawNinasAlien(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = 280, +60
    drawMyCactus(mouseX + offsetX, mouseY + offsetY)
    
