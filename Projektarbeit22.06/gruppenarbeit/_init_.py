# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:31:27 2022

@author: muell
"""
from Wand import Wand
from Oeffnung import Oeffnung
from Tuer import Tuer
from Stahlbtonwand import Stahlbetonwand
from Mauerwerk import Mauerwerk
from Raum import Raum
from Fenster import Fenster

from Erstellen import *
from MainMenu import *



#Speicherdatei bei öffnen des programms lesen und bei schließen des programms überspeichern --> MainMenu
# Raumliste = open("Raumliste.txt", "r")
# Raumliste.close() 
#

# Nach Beenden der Eingabe bericht als txt erstellen. systemzeit als name? (aufg.5)

# docstring erstellen

Raumliste = []
Tuerlisten = []
Fensterliste = []



auswahl = mainMenu()

if(auswahl=="n"):
    neuerRaum=raumErstellen()
    Raumliste.append(neuerRaum)
        
# if t
# if f
# if x









    
