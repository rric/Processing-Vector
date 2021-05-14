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

# TOUR-1 Dieser Sketch verwendet als Hintergrund das Bild
#   540px-David_by_Michelangelo_JBU06.JPG von Jörg Bittner Unna, 
#   CC BY 3.0, https://commons.wikimedia.org/w/index.php?curid=38304749
#
#   Das Bild wird hier unter der "Creative Commons"-Lizenz verwendet.
#   Bilder und Audiodateien, die in Processing geladen werden, müssen
#   im `data`-Unterverzeichnis liegen.

# TOUR-2 Es ist nützlich, zu Beginn einige Einstellungen als 
#   "globale Variablen" zu deklarieren. Diese Variablen können
#   in allen Funktionen verwendet werden; möchte man sie aber
#   verändern, muss man das Schlüsselwort `global` verwenden:
#   siehe https://py.processing.org/reference/globals.html

# Positionen, Farben und Buchstaben der Schalter
firstX, firstY = 410, 30
firstColor = color(255, 99, 71)   # Tomato
firstLetter = 'R'

secondX, secondY = 460, 30
secondColor = color(0, 255, 0)    # Lime
secondLetter = 'G'

buttonRadius = 21

# Radius, Farbe und Deckkraft des Pinsels
brushRadius = 15
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

    # TOUR-3 Male auf Hintergrundbild, aber NICHT auf die Tasten.
    #   Hier wird die `if`-Anweisung gleich zwei Mal verwendet:
    #   - falls eine Maustaste gedrückt ist, dann ...
    #   - ... wird überprüft, ob sich die Maus im rechten oberen
    #     Eck befindet, wo ja auch die Tasten sind: 
    #     nur falls das NICHT der Fall ist, wird ins Bild gemalt
    if mousePressed:
        if not (mouseX >= 370 and mouseY <= 70):
            fill(brushColor, opacity)
            circle(mouseX, mouseY, brushRadius)


def mouseClicked():
    global brushColor
        
    # TOUR-4 Falls einer der Schalter angeklickt wird, dann wird die
    #   Pinsel-Farbe entsprechend geändert.
    #   Der Befehl dist(x1, y1, x2, y2) berechnet die Distanz zwischen 
    #   den Punkten (x1, y1) und (x2, y2). Wie wird das gemacht?
    #   Tipp: Satz des Pythagoras
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
    
    # TOUR-5 Der ausgewählte Schalter soll durch einen weißen Rand
    #   angezeigt werden; der nicht ausgewählte durch einen schwarzen.
    #
    #   Der Unterschied zwischen `=` und `==` ist wichtig:
    #   mit `=` wird einer Variablen ein Wert zugewiesen;
    #   mit `==` werden zwei Werte verglichen. Die Zeile
    #
    #   stroke(255) if brushColor == firstColor else stroke(0)
    #
    #   ist eine kurze Schreibweise für
    #
    #   if brushColor == firstColor:
    #       stroke(255) 
    #   else:
    #       stroke(0)
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
    
# HAUSÜBUNG Erweitere drawButtons() um einen dritten Schalter
#   mit einer weiteren Farbe.
#   Such dir ein anderes Hintergrundbild aus und erstelle eine
#   "Übermalung" davon.
