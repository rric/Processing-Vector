# encoding: utf-8
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

# (Besare Abdulai)
def drawBesaresHouse(x, y): 
    rectMode(CORNER)
    fill("#E04444")
    rect(x, y, 300, 180)
    fill("#215879")
    triangle(x+300, y+0, x+0, y+0, x+160, y-100)
    fill("#69D374")
    ellipse(x+65, y+50, 50, 50)
    fill("#CEF063")
    rect(x+200, y+50, 50, 130)


# (Elisa Antelmann)
def drawLadyBird(x, y):
    noStroke()
    fill("#F71111") 
    circle(x, y, 60)
    
    stroke(0)
    fill("#030303")
    circle(x, y, 15)
    circle(x+10, y+19, 20)
    circle(x-19, y+10, 18)
    circle(x+19, y-10, 16)
    circle(x-22, y-10, 14)


# (Paula Bauer)
# Malt einen braunen Teddybären
def drawTeddyBear(x, y):
    noStroke()
    #male die Beine
    fill("#40280D")
    circle(x-17, y+40, 23)
    circle(x+17, y+40, 23)
    #male den Bauch
    fill("#4B2B0A")
    ellipse(x, y, 60, 80)
    fill("#816B3D")
    ellipse(x, y, 35, 60)
    #male die Ohren
    fill("#4B2B0A")
    circle(x-12, y-70, 20)
    circle(x+12, y-70, 20)
    fill("#816B3D")
    circle(x-10, y-66, 15)
    circle(x+10, y-66, 15)
    #male den Kopf
    fill("#40280D") 
    circle(x, y-50, 42)
    #male die Arme
    fill("#40280D")
    circle(x-30, y-10, 20)
    circle(x+30, y-10, 20)
    #male die Augen
    fill("#897B5F")
    circle(x-6, y-55, 5)
    circle(x+6, y-55, 5)
    #male die Schnauze
    fill("#EAD8C0")
    triangle(x-4, y-47.5, x, y-42, x+4, y-47.5)


# (Konstantin Bayerl)
def drawKonstantinsAlien(x, y):
#Alien
    drawKoerper(x, y)
    drawKopf(x, y)
    drawAuge1(x, y)
    drawAuge2(x, y)
    drawFuss1(x, y)
    drawFuss2(x,y)
    
#UFO
    drawBasis(x,110)
    drawKuppel(x,100)

#Alie_defenieren   

def drawKoerper(x, y):
    rectMode(CENTER)
    fill("#79FF79")
    rect(x, y, 20, 100)
        
def drawKopf(x, y):
    fill("#79FF79")
    ellipse(x, y-30,60,60)
        
def drawAuge1(x, y):
    fill("#000000")
    ellipse(x-19, y-30,16,32)
        
def drawAuge2(x, y):
    fill("#000000")
    ellipse(x+19, y-30,16,32)
        
def drawFuss1(x, y):
    line(x-10, y+50, x-20, y+60)
        
def drawFuss2(x,y):
    line(x+10, y+50, x+20, y+60)
    
#UFO_defienieren

def drawKuppel(x, y):
    fill("#4EE2EC")
    #ellipse(x, y, 70, 70)
    arc(x, y+10, 70, 30, 0, 3)
    arc(x, y+10, 70, 70, 3, 6.4)
    
def drawBasis(x, y):
    fill("#848482")
    ellipse(x, y,200,100)


# (Mithad Bogner)
def Zeichnung(x, y):
    strokeWeight(3)
    fill("#71FFEB")
    ellipse(x, y-25, 80, 130)
    fill("#8DF033") 
    circle(x, y, 42)
    
    # Male ein schwarzes "+"-Zeichen an Position (x, y)
    stroke(0)
    fill("#030302")
    circle(x-10, y-3, 12)
    circle(x+10, y-3, 12)
    circle(x, y+10, 6)
    line(x-30, y-40, x-10, y-20)
    line(x+30, y-40, x+10, y-20)
    fill("#5C5C5D")
    ellipse(x, y+30, 150, 30)      
    fill("#F01154")
    circle(x-45, y+30, 6)
    circle(x, y+30, 6)
    circle(x+45, y+30, 6)


# (Janine Davalos Herrera)
def drawanalien(x, y, color):
    fill("#20C9AB")
    rect(100,100,20,100)
    ellipse(100,70,60,60)
    ellipse(81,70,16,32) 
    ellipse(119,70,16,32) 
    line(90,150,80,160)
    line(110,150,120,160)


# (Niklas Dünser)
def drawIllusion(x, y):
    noStroke()
    fill("#F7FCF8")
    circle(x, y, 42)
    
    stroke(0)
    circle(x, y, 52)
    circle(x, y, 42)
    circle(x, y, 32)
    circle(x, y, 22)
    circle(x, y, 12)
    circle(x, y, 2)


# (Leonie Fehrer)
def drawLeoniesAlien(x,y):
    
    fill("#C185B9")
    rect (x-7, y+28, 20, 20)
    ellipse (x, y, 60, 60)
    ellipse(x+3,y+122, 60,150)
    
    fill("#55244F")
    ellipse (x-15,y,16,32) 
    ellipse (x+15, y, 16, 32) 
    ellipse(x, y+15, 10, 5)
    
    fill("#EA1123")
    ellipse(x-15, y, 5, 20)
    ellipse(x+15, y, 5, 20)
    

# (Sven Gruber)
# Malt das Auge
def drawEye(x, y):
    noStroke()
    fill("#FFFAFA") # white
    circle(x, y, 45)
    
    fill("#46B736")
    circle(x, y, 34)
    fill("#000000")
    circle(x, y, 20)


# (Jakob Hinterkörner)
def drawJakobsAlien(x, y):
    stroke ("#0000000000")
    fill("#FF4500") 
    rectMode(CENTER)
    rect(x,y,20,100)
    ellipse(x,y-30,60,60)
    ellipse(x-19,y-30,16,32) 
    ellipse(x+19,y-30,16,32)
    line(x-10,y+50,x-20,y+60)
    line(x+10,y+50,x+20,y+60)

    
# (Emilia Hochreiter)
def drawEmiliasAlien(x, y):
    noStroke()
    fill("#FF4500")
    fill("#400808") # "Orange-red"
    rect(x-10,y+20,20,100)
    ellipse(x,y,60,60)

    fill("#FF4500")
    ellipse(x-12,y,16,32) 
    ellipse(x+12,y,16,32)
    
    fill("#030303")
    line(x-10,y+50,80,160)
    line(x+10,y+50,120,60)


# (Christian Kaukal)
# definiert wie eine Ente gemalt werden soll; "s" steht für "size" (= Größe)
def draw_duck(x, y, s):
    noStroke()
    fill("#ffec3d")
    ellipse(x+75*s,y-45*s,30*s,10*s)
    fill("#ffffff")
    ellipse(x+0*s,y+0*s,100*s,50*s)
    ellipse(x+50*s,y-40*s,60*s,35*s)
    ellipse(x+28*s,y-20*s,20*s,60*s)
    fill("#111111")
    ellipse(x+60*s,y-45*s,5*s,5*s)


# (Lena Lorenz)
def drawLenasHouse(x,y,col):
    rectMode(CORNER)
    fill(col)
    noStroke()
    square(x,y,90)
    fill("#FF3B3B")
    triangle(x+45,y-45,x,y,x+90,y)
    fill("#C4FEFF")
    square(x+5,y+5,35)
    square(x+50,y+5,35)
    square(x+5,y+50,35)
    square(x+50,y+50,35)
    

# (Luisa Mayr)
def drawLadybug(x, y):
    stroke(0)
    line(x-18.5, y-18.5, x+18.5, y+18.5)
    line(x+25, y, x-25, y)
    line(x-18.5, y+18.5, x+18.5, y-18.5)
    line(x+1, y, x+6, y-40)
    line(x, y, x-9, y-40)
    fill("#F22C4A")
    circle(x, y, 42)
    fill("#080001")
    circle(x, y, 10)
    circle(x-10, y-10, 10)
    circle(x+10, y-10, 10)
    circle(x-10, y+10, 10)
    circle(x+10, y+10, 10)
    line(x, y-20, x, y+20)
    circle(x-8, y-38, 3)
    circle(x+6, y-38, 3)


# (Sina Mayr)
def drawSinasAlien(x, y, col):
    stroke("#000000")
    fill(col)
    rectMode(CENTER)
    rect(x, y, 20, 100)
    ellipse(x, y-30, 60, 60)
    line(x-10, y+50, x-20, y+60)
    line(x+10, y+50, x+20, y+60)
    
    fill("#000000")
    ellipse(x-19, y-30, 16, 32)
    ellipse(x+19, y-30, 16, 32)

    fill("#FFFFFF")
    circle(x-20, y-40, 8)
    circle(x+20, y-40, 8)
    

# (Nina Müllner)
def drawNinasAlien(x, y ): 
    stroke(0)
    fill("#25E844")
    rect(x-13,y+47,30,125)
    fill("#E8D225")
    ellipse(x,y,100,100)
    fill("#2595E8")
    ellipse(x-20,y,30,50) 
    ellipse(x+20,y,30,50) 

    
# (Anton Pargfrieder)
def drawAntonsAlien(x, y):
    stroke("#000000")
    fill("#FF4500")
# Male eine Figur
    rectMode(CENTER)
#Arme
    stroke("#f00000")
    line(x+20,y,x-10,y-40)
    line(x+20,y-50,x-20,y) 
    stroke("#000000")

#Körper
    rect(x,y,20,100)
#Kopf und Augen
    ellipse(x,y-60,60,60)
    #Change Color
    fill("#0000ff")
    ellipse(x-18,y-60,16,32) 
    ellipse(x+18,y-60,16,32) 
#Füße
    stroke("#000000")
    line(x,y+50,x,y+20)


# (Eliabeth Schimana)
def drawMyCactus(x, y):
    stroke(0)
    fill("#1FCB10") # "Grün"
    ellipse(x, y, 60, 175)
    ellipse(x-40, y-25, 30, 70)
    ellipse(x+40, y, 35, 80)
    
    fill("#F00AC6") # "Pink"
    circle(x+35, y-85, 20)
    circle(x+35, y-65, 20)
    circle(x+15, y-85, 20)
    circle(x+15, y-65, 20)
   
    fill("#FFEB03") # "Gelb"
    circle(x+25, y-75, 15)
    

# (Felix Steiner)
#Kleeblatt mit farbe wird gezeichnet
def shamrock(x, y):
    noStroke()
    fill("#53EA4C") # grün
    circle(x, y, 42)
    circle(x, y, 42)
    circle(x, y-34, 42)
    circle(x, y+34, 42)
    circle(x-34, y, 42)
    circle(x+34, y, 42)

    
# (Sophie Zehetner)
# Malt eine orange Sonne mit einem "+"-Zeichen in der Mitte
def drawSunPlus(x, y):
    noStroke()
    fill("#FF4500")
    fill("#FA1919") # "Orange-red"

    rect(x-10,y,20,100)
    ellipse(x,y,60,60)
    
    fill("#344FE0")
    ellipse(x-15,y,16,32)     
    ellipse(x+15,y,16,32) 
    
    fill("#FA1919")
    line(x-90,y-150,x-80,y-160)
    line(x-110,y-150,x-120,y-160)
    
