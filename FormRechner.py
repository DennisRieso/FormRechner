import math
# Rechteck
class Rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def flaeche_berechnen(self):
        return round(self.laenge * self.breite, 2)

    def umfang_berechnen(self):
        return round(2 * (self.laenge + self.breite), 2)
# Kreis
class Kreis:
    def __init__(self, radius):
        self.radius = radius

    def flaeche_berechnen(self):
        return round(math.pi * self.radius**2, 2)

    def umfang_berechnen(self):
        return round(2 * math.pi * self.radius, 2)
# Diagonale
class Diagonale:
    def __init__(self, seite):
        self.seite = seite

    def laenge_berechnen(self):
        return round(math.sqrt(2) * self.seite, 2)
# Rechtwinkliges Dreieck
class Dreieck:
    def __init__(self, h, s):
        self.h = h
        self.s = s
        
    def flaeche_berechnen(self):
        ergebnis = (self.h * self.s / 2)
        return round(ergebnis, 2)
    
    def umfang_berechnen(self):
        p = (self.h * self.h + self.s * self.s)
        r = (math.sqrt(p))
        return round(self.h + self.s + r)


# Funktion, um die Eingabe des Benutzers abzufragen
def eingabe_abfragen():
    form = input("Welche Form möchten Sie berechnen? (Rechteck/Kreis/Diagonale/Dreieck): ").lower()

    if form == 'rechteck':
        laenge = float(input("Geben Sie die Länge des Rechtecks in cm ein: "))
        breite = float(input("Geben Sie die Breite des Rechtecks in cm ein: "))
        return Rechteck(laenge, breite)
    elif form == 'kreis':
        radius = float(input("Geben Sie den Radius des Kreises in cm ein: "))
        return Kreis(radius)
    elif form == 'diagonale':
        seite = float(input("Geben Sie die Länge der Seite des Quadrats für die Diagonale in cm ein: "))
        return Diagonale(seite)
    elif form == 'dreieck':
        h = float(input("Gib die Höhe des Dreiecks in cm ein: "))
        s = float(input("Gib die zu dieser Höhe gehörige Grunseite in cm ein: "))
        return Dreieck(h, s)
    else:
        print("Ungültige Eingabe. Bitte wählen Sie zwischen Rechteck, Kreis, Diagonale oder Dreieck.")
        return eingabe_abfragen()






# Abfrage der Eingabe des Benutzers
form_objekt = eingabe_abfragen()

# Berechnung und Anzeige der Ergebnisse
if isinstance(form_objekt, Rechteck) or isinstance(form_objekt, Kreis):
    flaeche = form_objekt.flaeche_berechnen()
    umfang = form_objekt.umfang_berechnen()
    print(f"Fläche: {flaeche} cm², Umfang: {umfang} cm")
elif isinstance(form_objekt, Diagonale):
    laenge = form_objekt.laenge_berechnen()
    print(f"Diagonale - Länge: {laenge} cm")
elif isinstance(form_objekt, Dreieck):
    umfang = form_objekt.umfang_berechnen()
    flaeche = form_objekt.flaeche_berechnen()
    print(f"Umfang: {umfang} cm, Fläche: {flaeche} cm²")





