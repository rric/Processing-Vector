# Copyright 2021 Roland Richter
# Ein Vektor ist ein Pfeil: er hat eine Richtung und eine Länge
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

from ShowHelpers import *

# Ursprüngliche Positionen der gezeigten Objekte
firstX, firstY   = 42, 420
secondX, secondY = 420, 420
thirdX, thirdY   = 420, 42

def setup():
    size(800, 600)


def draw():
    background("#191970") # "MidnightBlue"

    # zeichne die Anfangs-Position in der Mitte des Bildes
    # und die End-Position beim Maus-Zeiger in zwei Blautönen
    anfX, anfY = width/2, height/2
    endX, endY = mouseX, mouseY
    showPosition(anfX, anfY, "#4682B4", "B")
    showPosition(endX, endY, "#87CEEB", "E")
    
    # der Vektor von Anfangs-Position zu End-Position ist die
    # Differenz: "End-Position minus Anfangs-Position"
    aeX, aeY = endX - anfX, endY - anfY
    showVector(anfX, anfY, aeX, aeY, "Vektor A->E")

    # male Objekte an der ursprünglichen Position sowie
    # um den Vektor aeX, aeY verschoben
    drawAlien(firstX, firstY)
    drawAlien(firstX + aeX, firstY + aeY)
    showVector(firstX, firstY, aeX, aeY, "Vektor A->E")
    
    drawAlien(secondX, secondY)
    drawAlien(secondX + aeX, secondY + aeY)
    showVector(secondX, secondY, aeX, aeY, "Vektor A->E")

    drawAlien(thirdX, thirdY)
    drawAlien(thirdX + aeX, thirdY + aeY)
    showVector(thirdX, thirdY, aeX, aeY, "Vektor A->E")


# Malt Ellen, den Alien, an der Position (x, y)
def drawAlien(x, y):
    # male den Kopf
    strokeWeight(2)
    stroke(0)
    fill("#32CD32")
    circle(x, y, 42)
    
    # male beide Augen
    fill("#FFD700")
    circle(x-10, y-10, 12)
    circle(x+10, y-10, 12)
    
    # male Mund und Fühler
    line(x-6, y+10, x+6, y+10)
    line(x-30, y-30, x-15, y-15)
    line(x+30, y-30, x+15, y-15)
    strokeWeight(1)
    
