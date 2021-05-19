# Copyright 2021 Besare Abdulai, Elisa Antelmann, Paula Bauer, Konstantin Bayerl, 
# Mithad Bogner, Janine Davalos Herrera, Niklas Dünser, Leonie Fehrer, Sven Gruber,
# Jakob Hinterkörner, Emilia Hochreiter, Christian Kaukal, Lena Lorenz, Luisa Mayr, 
# Sina Mayr, Nina Müllner, Anton Pargfrieder, Eliabeth Schimana, Felix Steiner, 
# Sophie Zehetner, Roland Richter
# 
# Sammlung aller abgegebenen und GPL-lizenzierten "drawSomething()"-Funktionen
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

from collection import *

def setup():
    size(1000, 700)


def draw():
    background("#87CEEB") # "Light sky blue"

    offsetX, offsetY = +120, -50
    drawLadyBird(mouseX + offsetX, mouseY + offsetY)

    offsetX, offsetY = -120, -40
    drawTeddyBear(mouseX + offsetX, mouseY + offsetY)

    offsetX, offsetY = -80, +90
    draw_duck(mouseX + offsetX, mouseY + offsetY, 1.0)

    offsetX, offsetY = +170, +90
    drawBesaresHouse(mouseX + offsetX, mouseY + offsetY)

    offsetX, offsetY = -370, +90
    drawLenasHouse(mouseX + offsetX, mouseY + offsetY, "#8120A7")

    offsetX, offsetY = +60, -50
    drawLadybug(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = -300, -170
    drawEmiliasAlien(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = -300, +80
    drawLeoniesAlien(mouseX + offsetX, mouseY + offsetY) 
    
    offsetX, offsetY = -350, +40
    drawJakobsAlien(mouseX + offsetX, mouseY + offsetY)    
    
    offsetX, offsetY = -200, +50
    drawNinasAlien(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = -230, -220
    Zeichnung(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = +280, +60
    drawMyCactus(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = +320, +70
    shamrock(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = +300, -170
    drawEye(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = +370, -140
    drawIllusion(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = +0, -240
    drawSunPlus(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = +50, -220
    drawKonstantinsAlien(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = -50, -220
    drawAntonsAlien(mouseX + offsetX, mouseY + offsetY)
    
    offsetX, offsetY = -150, -220
    drawSinasAlien(mouseX + offsetX, mouseY + offsetY, "#00BB00")
    
    offsetX, offsetY = -200, -220
    drawanalien(mouseX + offsetX, mouseY + offsetY, "#AAAA00")
    
# HAUSÜBUNG Verwende einige Funktionen aus der Sammlung, um ein Bild zu erstellen,
#   wie beispielsweise Gruppenbild mit Aliens, Haus mit Garten, oder ähnliches
