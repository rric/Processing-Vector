# Copyright 2021 Roland Richter
# Demonstration des "Daumenkino"-Effekts

def setup():
    size(600, 400)
    # frameRate(60)   # <- probier's aus


def draw():
    background("#87CEEB") # "Light sky blue"

    drawSunPlus(42, 84/2)
    drawSunPlus(width-42, mouseY)
    drawSunPlus(mouseX, mouseY)

    # Zeigt die momentane Bildanzahl und Bildrate an
    textSize(28)
    fill(0)
    text(str(frameCount) + " frames", 8, height-50)
    text(nf(frameRate, 1, 1) + " fps", 8, height-20)


# Malt eine orange Sonne mit einem "+"-Zeichen in der Mitte
def drawSunPlus(x, y):
    noStroke()
    fill("#FF4500") # "Orange-red"
    circle(x, y, 42)
    
    # Male ein schwarzes "+"-Zeichen an Position (x, y)
    stroke(0)
    line(x-8, y, x+8, y)
    line(x, y-8, x, y+8)
