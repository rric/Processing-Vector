# encoding: utf-8
# Copyright 2021 
#   Elisa Antelmann, Paula Maria Bauer, Konstantin Bayerl, 
#   Mithad Jan Bogner, Janine Davalos Herrera, Leonie Fehrer, 
#   Tim Friedrich, Sven Gruber, Jakob Hinterkörner,
#   Emilia Hochreiter, Christian Kaukal, Lena Lorenz, Luisa Mayr,
#   Sina Mayr, Nina Eva Müllner, Anton Pargfrieder, 
#   Eliabeth Schimana, Leon Szepe, Sophie Zehetner and Roland Richter
# 
# Sammlung aller abgegebenen und GPL-lizenzierten "drawSomething()"
# Funktionen, die PVector pos als Argument übernehmen
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


def drawSomething(number, pos):
    if number == 1:
        drawBesaresHouse(pos)
    elif number == 2:
        drawLadyBird(pos)
    elif number == 3:
        drawTeddyBear(pos)
    elif number == 4:
        drawStrahl(pos)
        drawKsAlien(pos)
        drawUFO(pos)
    elif number == 5:
        drawMithadsAlien(pos)
    elif number == 7:
        drawJaninesAlien(pos)
    elif number == 8:
        drawIllusion(pos)
    elif number == 9:
        drawLeoniesAlien(pos)
    elif number == 10:
        drawTimsAlien(pos)
    elif number == 11:
        drawEye(pos)
    elif number == 12:
        drawJakobsAlien(pos)
    elif number == 13:
        drawEmiliasAlien(pos)
    elif number == 15:
        draw_duck(pos, 1)
    elif number == 16:
        drawLenasHouse(pos)
    elif number == 17:
        drawLadybug(pos)
    elif number == 18:
        drawSinasAlien(pos, "#9932CC")
    elif number == 19:
        drawNinasAlien(pos)
    elif number == 21:
        drawAntonsAlien(pos)
    elif number == 22:
        drawMyCactus(pos)
    elif number == 23:
        drawShamrock(pos)
    elif number == 24:
        drawFisch(pos)
    elif number == 25:
        drawSophiesAlien(pos)


# (Besare Abdulai)
def drawBesaresHouse(pos): 
    pass
    

# (Elisa Antelmann)
def drawLadyBird(pos):
    # male den Kopf
    strokeWeight(2)
    stroke(0)
    fill("#F71111")
    circle(pos.x, pos.y, 42)
    
    # male beide Augen
    fill("#FFFFFF")
    circle(pos.x-10, pos.y-10, 10)
    circle(pos.x+10, pos.y-10, 10)
           
    # male Fühler
    line(pos.x-30, pos.y-30, pos.x-15, pos.y-15)
    line(pos.x+30, pos.y-30, pos.x+15, pos.y-15)
    strokeWeight(1)
    
    # male Punkte
    fill("#030303")
    circle(pos.x+2, pos.y+19, 9)
    circle(pos.x-9, pos.y+10, 10)
    circle(pos.x+1, pos.y-10, 8)
    circle(pos.x-1, pos.y-10, 6) 
    
    
# (Paula Maria Bauer)
# Male einen braunen Teddybären
def drawTeddyBear(pos):
    noStroke()
    
    #male die Beine
    fill("#40280D")
    circle(pos.x-17, pos.y+40, 23)
    circle(pos.x+17, pos.y+40, 23)
    
    #male den Bauch
    fill("#4B2B0A")
    ellipse(pos.x, pos.y, 60, 80)
    fill("#816B3D")
    ellipse(pos.x, pos.y, 35, 60)
    
    #male die Ohren
    fill("#4B2B0A")
    circle(pos.x-12, pos.y-70, 20)
    circle(pos.x+12, pos.y-70, 20)
    fill("#816B3D")
    circle(pos.x-10, pos.y-66, 15)
    circle(pos.x+10, pos.y-66, 15)
    
    #male den Kopf
    fill("#40280D") 
    circle(pos.x, pos.y-50, 42)
    
    #male die Arme
    fill("#40280D")
    circle(pos.x-30, pos.y-10, 20)
    circle(pos.x+30, pos.y-10, 20)
    
    #male die Augen
    fill("#897B5F")
    circle(pos.x-6, pos.y-55, 5)
    circle(pos.x+6, pos.y-55, 5)
    
    #male die Schnauze
    fill("#EAD8C0")
    triangle(pos.x-4, pos.y-47.5, pos.x, pos.y-42, pos.x+4, pos.y-47.5)


# (Konstantin Bayerl)
def drawKsAlien(pos):
    rectMode(CENTER)
    fill("#79FF79")
    stroke(12);
    rect(pos.x, pos.y, 20, 100)
    
    fill("#79FF79")
    ellipse(pos.x, pos.y-30,60,60)    

    fill("#000000")
    ellipse(pos.x-19, pos.y-30,16,32) 

    fill("#000000")
    ellipse(pos.x+19, pos.y-30,16,32)   

    line(pos.x-10, pos.y+50, pos.x-20, pos.y+60)

    line(pos.x+10, pos.y+50, pos.x+20, pos.y+60)
    
def drawUFO(pos):
    
    fill("#848482")
    stroke(12)
    ellipse(pos.x, 100,200,100)
    
    fill("#4EE2EC")
    arc(pos.x, 100, 70, 30, 0, 3)
    arc(pos.x, 100, 70, 70, 3, 6.4)
    
    
def drawStrahl(pos):
    fill("#90CBA5")
    noStroke();
    triangle(pos.x+100, 500, pos.x, 90, pos.x-100, 500)
    
    
# (Mithad Bogner)
# Malt Ellen, den Alien, an der Position pos
def drawMithadsAlien(pos):
    stroke(0)
    fill("#99FF7E")
    circle(pos.x, pos.y, 42)
    fill("#000000")
    circle(pos.x-10, pos.y-3, 12)
    circle(pos.x+10, pos.y-3, 12)
    circle(pos.x, pos.y+10, 6)
    line(pos.x-30, pos.y-40, pos.x-10, pos.y-20)
    line(pos.x+30, pos.y-40, pos.x+10, pos.y-20)
    strokeWeight(1)


# (Janine Davalos Herrera)
# Malt Ellen, den Alien, an der Position pos
def drawJaninesAlien(pos):
    stroke(0)
    rectMode(CENTER)
    rect(pos.x,pos.y,14,100)
    ellipse(pos.x,pos.y-30,60,60)
    fill("#FF0505")
    ellipse(pos.x-19,pos.y-30,16,32) 
    ellipse(pos.x+19,pos.y-30,16,32) 
    line(pos.x-10,pos.y+50,pos.x-20,pos.y+60)
    line(pos.x+10,pos.y+50,pos.x+20,pos.y+60)
    line(pos.x-10,pos.y+10,pos.x-20,pos.y+30)
    line(pos.x+10,pos.y+10,pos.x+20,pos.y+30)


# (Niklas Dünser)
def drawIllusion(pos):
    pass
    
    
# (Leonie Fehrer)
# Male Alien an der Position pos
def drawLeoniesAlien(pos):    
    fill("#D39CCC")

    fill("#C185B9")
    rect (pos.x-7, pos.y+28, 20, 20)
    ellipse (pos.x, pos.y, 60, 60)
    ellipse(pos.x+3, pos.y+122, 60, 150)
    
    fill("#55244F")
    ellipse (pos.x-15,pos.y, 16, 32) 
    ellipse (pos.x+15, pos.y, 16, 32) 
    ellipse(pos.x, pos.y+15, 10, 5)
    
    fill("#EA1123")
    ellipse(pos.x-15, pos.y, 5, 20)
    ellipse(pos.x+15, pos.y, 5, 20)
    
    
# (Tim Friedrich)
def drawTimsAlien(pos):
    drawKoerper(pos.x, pos.y)
    drawKopf(pos.x, pos.y)
    drawAuge1(pos.x, pos.y)
    drawAuge2(pos.x, pos.y)
    drawFuss1(pos.x, pos.y)
    drawFuss2(pos.x,pos.y)
    drawWaffe1(pos.x,pos.y)
    drawWaffe2(pos.x,pos.y)
    
def drawKoerper(x, y):
    rectMode(CENTER)
    fill("#288083")
    rect(x, y, 20, 100)
    
def drawWaffe1(x, y):
    fill("#241C1C")
    rect(x+15, y+30,5,30)
    
def drawWaffe2(x, y):
    fill("#241C1C")
    rect(x+12, y+10,10,10)
        
def drawKopf(x, y):
    fill("#62C6E3")
    ellipse(x, y-30,60,60)
        
def drawAuge1(x, y):
    fill("#1EF5D6")
    ellipse(x-19, y-30,16,32)
        
def drawAuge2(x, y):
    fill("#1EF5D6")
    ellipse(x+19, y-30,16,32)
        
def drawFuss1(x, y):
    line(x-10, y+50, x-20, y+60)
        
def drawFuss2(x,y):
    line(x+10, y+50, x+20, y+60)


# (Sven Gruber)
# Malt das Auge
def drawEye(pos):
    # male den Kopf
    noStroke()
    fill("#FFFAFA") # white
    circle(pos.x, pos.y, 45)
    
    fill("#46B736")
    circle(pos.x, pos.y, 34)
    fill("#000000")
    circle(pos.x, pos.y, 20)


# (Jakob Hinterkörner)
def drawJakobsAlien(pos):
    stroke ("#00000")
    fill("#ffd700") 
    rectMode(CENTER)
    rect(pos.x,pos.y,20,100)
    ellipse(pos.x,pos.y-30,60,60)
    ellipse(pos.x-19,pos.y-30,16,32) 
    ellipse(pos.x+19,pos.y-30,16,32)
    line(pos.x-10,pos.y+50,pos.x-20,pos.y+60)
    line(pos.x+10,pos.y+50,pos.x+20,pos.y+60)
    strokeWeight(1)
    

# (Emilia Hochreiter)
def drawEmiliasAlien(pos):
    # male den Kopf
    strokeWeight(2)
    noStroke()
    fill("#400808") # "Orange-red"
    rect(pos.x-10,pos.y+20,20,100)
    ellipse(pos.x,pos.y,60,60)
    
    # male beide Augen
    fill("#FF4500")
    ellipse(pos.x-12,pos.y,16,32) 
    ellipse(pos.x+12,pos.y,16,32)
    
    # male Mund und Fühler
    fill("#030303")
    strokeWeight(1)
    line(pos.x-10,pos.y-50,pos.x-10,pos.y-50)
    line(pos.x+10,pos.y-50,pos.x+10,pos.y-50)  
    line(pos.x-6,pos.y+10,pos.x+6,pos.y+10)


# (Christian Kaukal)
# definiert wie eine Ente gemalt werden soll; "s" steht für "size" (= Größe)
def draw_duck(pos, s):
    noStroke()
    fill("#ffec3d")
    ellipse(pos.x+75*s,pos.y-45*s,30*s,10*s)
    fill("#ffffff")
    ellipse(pos.x+0*s,pos.y+0*s,100*s,50*s)
    ellipse(pos.x+50*s,pos.y-40*s,60*s,35*s)
    ellipse(pos.x+28*s,pos.y-20*s,20*s,60*s)
    fill("#111111")
    ellipse(pos.x+60*s,pos.y-45*s,5*s,5*s)


# (Lena Lorenz)
def drawLenasHouse(pos):
    rectMode(CORNER)  # TODO looks wrong otherwise?
    fill("#EA45D7")
    noStroke()
    square(pos.x, pos.y, 90)
    fill("#FF3B3B")
    triangle(pos.x+45, pos.y-45, pos.x, pos.y, pos.x+90, pos.y)
    fill("#C4FEFF")
    square(pos.x+5, pos.y+5,35)
    square(pos.x+50, pos.y+5,35)
    square(pos.x+5, pos.y+50,35)
    square(pos.x+50, pos.y+50,35)
    

# (Luisa Mayr)
def drawLadybug(pos):
    stroke(0)
    line(pos.x-18.5, pos.y-18.5, pos.x+18.5, pos.y+18.5)
    line(pos.x+25, pos.y, pos.x-25, pos.y)
    line(pos.x-18.5, pos.y+18.5, pos.x+18.5, pos.y-18.5)
    line(pos.x+1, pos.y, pos.x+6, pos.y-40)
    line(pos.x, pos.y, pos.x-9, pos.y-40)
    fill("#F22C4A")
    circle(pos.x, pos.y, 42)
    fill("#080001")
    circle(pos.x, pos.y, 10)
    circle(pos.x-10, pos.y-10, 10)
    circle(pos.x+10, pos.y-10, 10)
    circle(pos.x-10, pos.y+10, 10)
    circle(pos.x+10, pos.y+10, 10)
    line(pos.x, pos.y-20, pos.x, pos.y+20)
    circle(pos.x-8, pos.y-38, 3)
    circle(pos.x+6, pos.y-38, 3)


# (Sina Mayr)
def drawSinasAlien(pos, color):
    stroke("#000000")
    fill(color)
    rectMode(CENTER)
    rect(pos.x, pos.y, 20, 100)
    ellipse(pos.x, pos.y-30, 60, 60)
    line(pos.x-10, pos.y+50, pos.x-20, pos.y+60)
    line(pos.x+10, pos.y+50, pos.x+20, pos.y+60)
    
    fill("#000000")
    ellipse(pos.x-19, pos.y-30, 16, 32)
    ellipse(pos.x+19, pos.y-30, 16, 32)

    fill("#FFFFFF")
    circle(pos.x-20, pos.y-40, 8)
    circle(pos.x+20, pos.y-40, 8)
    

# (Nina Eva Müllner)
def drawNinasAlien(pos): 
    stroke(0)
    fill("#25E844")
    rect(pos.x-13,pos.y+47,30,125)
    fill("#E8D225")
    ellipse(pos.x,pos.y,100,100)
    fill("#2595E8")
    ellipse(pos.x-20,pos.y,30,50) 
    ellipse(pos.x+20,pos.y,30,50)


# (Anton Pargfrieder)
def drawAntonsAlien(pos):
    stroke("#000000")
    fill("#FF4500")
# Male eine Figur
    rectMode(CENTER)
#Arme
    stroke("#f00000")
    line(pos.x+20,pos.y,pos.x-10,pos.y-40)
    line(pos.x+20,pos.y-50,pos.x-20,pos.y) 
    stroke("#000000")

#Körper
    rect(pos.x,pos.y,20,100)
#Kopf und Augen
    ellipse(pos.x,pos.y-60,60,60)
    #Change Color
    fill("#0000ff")
    ellipse(pos.x-18,pos.y-60,16,32) 
    ellipse(pos.x+18,pos.y-60,16,32) 
#Füße
    stroke("#000000")
    line(pos.x,pos.y+50,pos.x,pos.y+20)
    
    
# (Eliabeth Schimana)
def drawMyCactus(pos):
    stroke(0)
    fill("#1FCB10") # "Grün"
    ellipse(pos.x, pos.y, 60, 175)
    ellipse(pos.x-40, pos.y-25, 30, 70)
    ellipse(pos.x+40, pos.y, 35, 80)
    
    fill("#F00AC6") # "Pink"
    circle(pos.x+35, pos.y-85, 20)
    circle(pos.x+35, pos.y-65, 20)
    circle(pos.x+15, pos.y-85, 20)
    circle(pos.x+15, pos.y-65, 20)
   
    fill("#FFEB03") # "Gelb"
    circle(pos.x+25, pos.y-75, 15)


# (Felix Steiner)
#Kleeblatt mit farbe wird gezeichnet
def drawShamrock(pos):
    pass
    
            
# (Leon Szepe)
def drawFisch(pos):
    noStroke()
    fill("#FA8F1C")    
    triangle(pos.x,pos.y, pos.x+70, pos.y-30, pos.x+70, pos.y+30)
    ellipseMode(CENTER)
    ellipse(pos.x, pos.y, 100, 50)
    fill("#000000")
    circle(pos.x-25, pos.y-8, 10)

    
# (Sophie Zehetner)
def drawSophiesAlien(pos):
    rectMode(CORNER)  # TODO looks wrong otherwise?
    noStroke()
    fill("#FF4500")
    fill("#030101")

    rect(pos.x-10,pos.y,20,100)
    ellipse(pos.x,pos.y,60,60)
    
    fill("#23FAE6")
    ellipse(pos.x-15,pos.y,16,32)     
    ellipse(pos.x+15,pos.y,16,32) 
    
    fill("#030101")
    line(pos.x-90,pos.y-150,pos.x-80,pos.y-160)
    line(pos.x-110,pos.y-150,pos.x-120,pos.y-160)
    
