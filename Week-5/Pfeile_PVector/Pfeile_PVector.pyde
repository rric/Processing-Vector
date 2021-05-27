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
firstPos   = PVector(42, 420)
secondPos  = PVector(420, 420)
thirdPos   = PVector(420, 42)

def setup():
    size(800, 600)


def draw():
    background("#191970") # "MidnightBlue"

    # zeichne die Anfangs-Position in der Mitte des Bildes
    # und die End-Position beim Maus-Zeiger in zwei Blautönen
    anfPos = PVector(width/2, height/2)
    endPos = PVector(mouseX, mouseY)
    showPosition(anfPos, "#4682B4", "A")
    showPosition(endPos, "#87CEEB", "E")
    
    # der Vektor von Anfangs-Position zu End-Position ist die
    # Differenz: "End-Position minus Anfangs-Position"
    aeVec = endPos - anfPos           # Vektor-Subtraktion
    showVector(anfPos, aeVec, "Vektor A->E")

    # male Objekte an der ursprünglichen Position sowie
    # um den Vektor aeX, aeY verschoben
    drawAlien(firstPos)
    drawAlien(firstPos + aeVec)       # Vektor-Addition
    showVector(firstPos, aeVec, "Vektor A->E")
    
    drawAlien(secondPos)
    drawAlien(secondPos + aeVec)      # Vektor-Addition
    showVector(secondPos, aeVec, "Vektor A->E")

    drawAlien(thirdPos)
    drawAlien(thirdPos + aeVec)       # Vektor-Addition
    showVector(thirdPos, aeVec, "Vektor A->E")


# HAUSÜBUNG Ändere deine Funktion `drawSomething(x, y)` in
#   `drawSomething(pos)` ab und verwende sie an dieser Stelle 
#   statt `drawAlien(pos)`.

# Malt Ellen, den Alien, an der Position pos
def drawAlien(pos):
    # male den Kopf
    strokeWeight(2)
    stroke(0)
    fill("#32CD32")
    circle(pos.x, pos.y, 42)
    
    # male beide Augen
    fill("#FFD700")
    circle(pos.x-10, pos.y-10, 12)
    circle(pos.x+10, pos.y-10, 12)
    
    # male Mund und Fühler
    line(pos.x-6, pos.y+10, pos.x+6, pos.y+10)
    line(pos.x-30, pos.y-30, pos.x-15, pos.y-15)
    line(pos.x+30, pos.y-30, pos.x+15, pos.y-15)
    strokeWeight(1)
