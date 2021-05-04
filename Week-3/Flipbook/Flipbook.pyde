# Copyright 2021 Roland Richter
# Demonstration of the "flip book" effect

# TOUR-1 Here, the setup() function is defined. setup() is called only
#   once, at program start-up. The keyword `def` is short for 'define
#   a function'. Note the colon ':' at the end of the line is necessary.
def setup():
    size(600, 400)
    # frameRate(60)   # <- try out and change it

# TOUR-2 Here, draw() is defined. It is called about 60 times per sec
#   by default, resulting in a "flip book" effect. Note you can change
#   the frame rate in setup().
#   Both the setup() and draw() functions do not have any parameters,
#   hence their argument list `()` is empty.
def draw():
    background("#87CEEB") # "Light sky blue"

    # TOUR-4 Here, function `drawSunPlus` is used several times to
    #   draw some suns. In each case, one has to pass (exactly) two
    #   arguments to the function: This can be simple numbers, but
    #    also aritmethic expressions with variables.
    drawSunPlus(42, 84/2)
    drawSunPlus(width-42, mouseY)
    drawSunPlus(mouseX, mouseY)

    # Displays current frame rate and count
    textSize(28)
    fill(0)
    text(str(frameCount) + " frames", 8, height-50)
    text(nf(frameRate, 1, 1) + " fps", 8, height-20)


# TOUR-3 Another function is defined here, called `drawSunWithPlus`.  
#   This function takes two parameters, `x` and `y`, i.e. the 
#   position where to draw the sun to.

# Draws an orange sun with a "+" mark at the center
def drawSunPlus(x, y):
    noStroke()
    fill("#FF4500") # "Orange-red"
    circle(x, y, 42)
    
    # Draw a black "+" mark at position (x, y)
    stroke(0)
    line(x-8, y, x+8, y)
    line(x, y-8, x, y+8)
    
# EXERCISE-1 Change drawSunPlus such that it draws a "x" mark
#   instead of the "+" mark

# EXERCISE-2 Extend drawSunPlus such that it takes a third parameter,
#   namely the color to draw the circle with

# HOMEWORK Create a function drawSomeThing() to draw anything you 
#   like: a football, an alien face, a ladybug ...
