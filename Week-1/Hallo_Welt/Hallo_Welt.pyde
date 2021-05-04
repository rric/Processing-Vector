# Copyright 2021 Roland Richter
# Hallo Welt

# Erzeuge ein quadratisches Fenster
# mit Hintergrundfarbe RebeccaPurple
size(500, 500)
background("#663399")            

# Mache Text besser lesbar: 
# zentriert, größer und weiß
textAlign(CENTER)
textSize(24)
fill(255)
    
# Begrüße alle etwas über der Mitte:
# 50% Fensterbreite, 30% Fensterhöhe
text("Hallo, Khevis!", 
     0.5 * width, 0.3 * height)
