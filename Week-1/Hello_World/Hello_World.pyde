# Copyright 2021 Roland Richter
# Hello World

# Create a quadratic display window
# with RebeccaPurple background
size(500, 500)
background("#663399")            

# Make text more readable: 
# centered, large and white
textAlign(CENTER)
textSize(24)
fill(255)
    
# Say hello to everyone at
# 50 % width and 30 % height
text("Hello, class!", 
     0.5 * width, 0.3 * height)
