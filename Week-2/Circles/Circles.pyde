# Create a quadratic display window
size(500, 500)
# Use SkyBlue and OrangeRed
background("#87CEEB")
fill("#FF4500")       

# Draw a circle with diameter 42
circle(40, 25, 42)    # where is it?
circle(400, 25, 42)   # ...and now?
circle(40, 250, 42)   # ...and now?
circle(40, 2500, 42)  # ...and now?
circle(width-40, 25, 42) # ... now?
circle(40, height-25, 42) # ...now?
circle(0.5*width, 0.3*height, 42) # ?
