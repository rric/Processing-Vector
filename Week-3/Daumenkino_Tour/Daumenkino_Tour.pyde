# Copyright 2021 Roland Richter
# Demonstration des "Daumenkino"-Effekts

# TOUR-1 Die meisten Processing-Programme definieren zwei Funktionen:
#   - setup(), das genau einmal beim Programmstart aufgerufen wird
#   - draw(), das standardmäßig ca. 60 mal pro Sekunde aufgerufen wird;
#     bei jedem Aufruf wird die Anzeige neu gemalt; dies führt zu einem 
#     "Daumenkino"-Effekt.
#
#   Hier wird setup() definiert: das Schlüsselwort `def` bedeutet
#   'define a function'; am Zeilenende muss ein Doppelpunkt ':' stehen.
def setup():
    size(800, 600)
    # frameRate(60)   # <- Probier's aus und ändere die Bildrate

# TOUR-2 Hier wird draw() definiert. Die Funktionen setup() und draw()
#   haben keine Parameter, daher ist ihre Parameterliste `()` leer.
def draw():
    background("#87CEEB") # <- Was ist, wenn du diese Zeile kommentierst?

    # TOUR-4 Hier wird die Funktion `drawSunPlus` mehrmals verwendet, 
    #   um einige Sonnen zu zeichnen. Jedes Mal muss man (genau) zwei
    #   Argumente an die Funktion übergeben: Das können einfach Zahlen
    #   sein, aber auch aritmethische Ausdrücke mit Variablen.
    drawSunPlus(42, 84/2)
    drawSunPlus(width-42, mouseY)
    drawSunPlus(mouseX, mouseY)

    # Zeigt die momentane Bildanzahl und Bildrate an
    textSize(28)
    fill(0)
    
    # TOUR-5 Um Zahlen in Text zu verwandeln, gibt es in Processing 
    #   einige Funktionen, zum Beispiel `str()` und `nf()`.
    text(str(frameCount) + " frames", 8, height-50)
    text(nf(frameRate, 1, 1) + " fps", 8, height-20)


# TOUR-3 Hier wird eine Funktion namens `drawSunWithPlus` definiert.
#   Diese Funktion erwartet zwei Parameter, `x` und `y`, das ist die 
#   Position, an der die Sonne gezeichnet werden soll.

# Malt eine orange Sonne mit einem "+"-Zeichen in der Mitte
def drawSunPlus(x, y):
    noStroke()
    fill("#FF4500") # "Orange-red"
    circle(x, y, 42)
    
    # Male ein schwarzes "+"-Zeichen an Position (x, y)
    stroke(0)
    line(x-8, y, x+8, y)
    line(x, y-8, x, y+8)
    
# AUFGABE-1 Ändere drawSunPlus so, dass es ein "x"-Zeichen statt 
#   eines "+"-Zeichens malt.

# AUFGABE-2 Erweitere drawSunPlus so, dass es einen dritten Parameter
#   hat: nämlich die Farbe, mit der der Kreis gemalt wird.

# HAUSÜBUNG Erstelle eine Funktion drawSomeThing(x, y), um an der
#   Position (x, y) ein anderes Objekt (statt der "Sonne") zu malen: 
#   einen Fußball, einen Alien, einen Marienkäfer, ... Ein Beispiel 
#   ist ganz unten auf https://py.processing.org/tutorials/drawing/ 
#
#   Das Objekt soll an der Mausposition (und evtl. an anderen
#   Positionen) angezeigt werden.
