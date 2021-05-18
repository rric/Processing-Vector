# encoding: utf-8
# Copyright 2021 Paula Bauer, Leonie Fehrer, Christian Kaukal, Lena Lorenz,
#   Luisa Mayr, Nina Müllner, Eliabeth Schimana, Roland Richter
# und -- hoffentlich -- bald noch vielen, vielen anderen!
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
def drawNothingYet01(x, y):
    pass

# (Elisa Antelmann)
def drawNothingYet02(x, y):
    pass

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
def drawNothingYet04(x, y):
    pass

# (Mithad Bogner)
def drawNothingYet05(x, y):
    pass
    
# (Elena Carcamo)
def drawNothingYet06(x, y):
    pass
    
# (Janine Davalos Herrera)
def drawNothingYet07(x, y):
    pass
    
# (Niklas Dünser)
def drawNothingYet08(x, y):
    pass

# (Leonie Fehrer)
def drawLeoniesAlien(x,y):
    
    rect (x-7, y+28, 20, 100)
    ellipse (x, y, 60, 60)
    
    fill("#55244F")
    ellipse (x-15,y,16,32) 
    ellipse (x+15, y, 16, 32) 
    

# (Tim Friedrich)
def drawNothingYet10(x, y):
    pass

# (Sven Gruber)
def drawNothingYet11(x, y):
    pass
    
# (Jakob Hinterkörner)
def drawNothingYet12(x, y):
    pass
    
# (Emil Hochradner)
def drawNothingYet13(x, y):
    pass
    
# (Emilia Hochreiter)
def drawNothingYet14(x, y):
    pass
    
# (Florian Kabelka)
def drawNothingYet15(x, y):
    pass

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

# (Samuel Kubik)
def drawNothingYet17(x, y):
    pass

# (Lena Lorenz)
def drawHouse(x,y,color):
    fill(color)
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
def drawNothingYet20(x, y):
    pass
    
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
    
# (Andrei Negru)
def drawNothingYet22(x, y):
    pass
    
# (Anton Pargfrieder)
def drawNothingYet23(x, y):
    pass

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
def drawNothingYet25(x, y):
    pass
    
# (Leon Szepe)
def drawNothingYet26(x, y):
    pass
    
# (Sophie Zehetner)
def drawNothingYet27(x, y):
    pass
    
