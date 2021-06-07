# Copyright 2021 Roland Richter
# Zeichnet viele, viele Aliens mit Listen und Schleifen
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


# Liste der Positionen aller Objekte
posList = []

# Die minimale Distanz, die Objekte voneinander haben müssen
MinimalDistance = 50

# kurz für "show indices for n further frames"
showIndicesFnFF = 0


def setup():
    global posList, showIndicesFnFF
    
    size(800, 600)
    
    posList = [PVector(width/2, height/2)]
    showIndicesFnFF = 180


def mousePressed():
    global posList, showIndicesFnFF
    
    if mouseButton == LEFT:
        newPos = PVector(mouseX, mouseY)
        
        # Die neue Position newPos wird nur dann zur Liste hinzugefügt,
        # wenn sie nicht zu nahe an einer anderen Position ist.
        # - bestimme die Distanzen von newPos zu allen anderen Positionen
        # - nur wenn alle anderen Positionen "weit weg" sind, darf die neue
        #     Position zur Liste hinzugefügt werden
        
        distList = [PVector.dist(pos, newPos) for pos in posList]
        print("Distanzen zur neuen Position: ")
        println(distList)
        
        isFarAwayList = [d > MinimalDistance for d in distList]
        # oder:
        # isFarAwayList = [PVector.dist(pos, newPos) > MinimalDistance
        #                  for pos in posList]
        print("Neue Position ist weit weg?: ")
        println(isFarAwayList)        
        
        if all(isFarAwayList):
            posList.append(newPos)

        showIndicesFnFF = 180

    elif mouseButton == RIGHT:
        pass


def keyPressed():
    global posList
    
    if key == 'c' or key == 'C':
        # posList.clear() 
        posList = []

    if key == 'r' or key == 'R':
        posList.append(PVector(random(0,width), random(0,height)))
        showIndicesFnFF = 180
        

def draw():
    global showIndicesFnFF
    
    background("#191970") # "MidnightBlue"
            
    # male alle Objekte in der Liste
    if showIndicesFnFF <= 0:
        for pos in posList:
            drawAlien(pos)
    else:
        for i in range(len(posList)):
            drawAlien(posList[i])
            textSize(16)
            fill(255)
            text(str(i), posList[i].x+20, posList[i].y+20)
        
    showIndicesFnFF -= 1
    
    # zeige die Länge der Liste an
    textSize(28)
    fill(255)
    text(str(len(posList)) + " Element(e)", 8, height-20)


# HAUSÜBUNG
# Füge statt Ellen dem Alien deine Figur hier ein.
# Ändere auch die minimale Distanz entsprechend.

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
