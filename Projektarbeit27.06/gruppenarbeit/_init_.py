# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:31:27 2022

@author: muell
"""
from Wand import Wand
from Oeffnung import Oeffnung
from Tuer import Tuer
from Stahlbetonwand import Stahlbetonwand
from Mauerwerk import Mauerwerk
from Raum import Raum
from Fenster import Fenster

from Erstellen import *
from MainMenu import *
from Listen import *



#Speicherdatei bei öffnen des programms lesen und bei schließen des programms überspeichern --> MainMenu
# Raumliste = open("Raumliste.txt", "r")
# Raumliste.close() 
#

# Nach Beenden der Eingabe bericht als txt erstellen. systemzeit als name? (aufg.5)

# docstring erstellen

Raumliste = []
Tuerliste = []
Fensterliste = []

"""
Großbuchstabe.
"""

auswahl = mainMenu()

if(auswahl=="n"):
    neuerRaum=raumErstellen()
    Raumliste.append(neuerRaum)
    Tuerliste= addTuer(Tuerliste,neuerRaum)
    Fensterliste= addFenster(Fensterliste,neuerRaum)
    bericht=open(Bericht.txt,"w")
    bertxt= berichtErzeugen(Raumliste)
    #hier schreiben
    bericht.close()
    
elif(auswahl=="f"):
    print(fausgeben(Fensterliste))

elif(auswahl=="t"):
    print(tausgeben(Tuerliste))
        
# if t
# if f
# if x









    
