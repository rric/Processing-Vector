# Copyright 2021 Roland Richter
# Demonstration des "Daumenkino"-Effekts
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
    # frameRate(60)   # <- probier's aus


def draw():
    background("#87CEEB") # "Light sky blue"

    drawAlien(42, 84/2)
    drawAlien(width-42, mouseY)
    drawAlien(mouseX, mouseY)

    # Zeigt die momentane Bildanzahl und Bildrate an
    textSize(28)
    fill(0)
    text(str(frameCount) + " frames", 8, height-50)
    text(nf(frameRate, 1, 1) + " fps", 8, height-20)


# HAUSÜBUNG Erstelle eine Funktion drawSomeThing(x, y), um an der
#   Position (x, y) ein anderes Objekt (statt der "Sonne") zu malen: 
#   einen Fußball, einen Alien, einen Marienkäfer, ... Ein Beispiel 
#   ist ganz unten auf https://py.processing.org/tutorials/drawing/ 
#
#   Das Objekt soll an der Mausposition (und evtl. an anderen
#   Positionen) angezeigt werden.

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