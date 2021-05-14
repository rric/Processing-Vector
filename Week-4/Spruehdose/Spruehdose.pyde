# Copyright 2020, 2021 Roland Richter
# Virtuelle Sprühdose mit einfacher graphischer Benutzeroberfläche
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

# Dieser Sketch verwendet als Hintergrund das Bild
# 540px-David_by_Michelangelo_JBU06.JPG von Jörg Bittner Unna, 
# CC BY 3.0, https://commons.wikimedia.org/w/index.php?curid=38304749

# Positionen, Farben und Buchstaben der Schalter
firstX, firstY = 410, 30
firstColor = color(255, 99, 71)   # Tomato
firstLetter = 'R'

secondX, secondY = 460, 30
secondColor = color(0, 255, 0)    # Lime
secondLetter = 'G'

buttonRadius = 21

# Radius, Farbe und Deckkraft des Pinsels
brushRadius = 19
brushColor = firstColor
opacity = 24


def setup():
    # Verwende "David" (540 x 720 groß) als Hintergrund
    size(540, 720) 
    david = loadImage("540px-David_by_Michelangelo_JBU06.JPG");
    background(david)

    # Verwende "+"-Mauszeiger für den Pinsel
    cursor(CROSS)
    
    # Verwende Radius, nicht Durchmesser, zum Zeichnen der Kreise
    ellipseMode(RADIUS)
    strokeWeight(2)

    drawButtons()


def draw():
    noStroke()

    # Male auf Hintergrundbild, aber NICHT auf die Tasten
    if mousePressed:
        if not (mouseX >= 380 and mouseY <= 70):
            fill(brushColor, opacity)
            circle(mouseX, mouseY, brushRadius)


def mouseClicked():
    global brushColor
        
    # Falls einer der Schalter angeklickt wird, dann ändere die
    # Pinsel-Farbe entsprechend
    if dist(mouseX, mouseY, firstX, firstY) < buttonRadius:
        brushColor = firstColor
    elif dist(mouseX, mouseY, secondX, secondY) < buttonRadius:
        brushColor = secondColor

    drawButtons()


# Zeichnet die Schalter zum Auswählen der Pinsel-Farbe;
# der ausgewählte Schalter wird durch einen weißen Rand angezeigt.
def drawButtons():
    textSize(24)
    textAlign(CENTER, CENTER)
    stroke(255) if brushColor == firstColor else stroke(0)
    fill(firstColor)
    circle(firstX, firstY, buttonRadius)
    fill(255) if brushColor == firstColor else fill(0)
    text(firstLetter, firstX+1, firstY-4)

    stroke(255) if brushColor == secondColor else stroke(0)
    fill(secondColor)
    circle(secondX, secondY, buttonRadius)
    fill(255) if brushColor == secondColor else fill(0)
    text(secondLetter, secondX+1, secondY-4)
