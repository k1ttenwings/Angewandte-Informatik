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
from Autor import Autor





Raumliste = []
Tuerliste = []
Fensterliste = []




autor1=Autor("Thorben","Müller","348238")
autor2=Autor("Franziska","Köhler","297224")
autor3=Autor("Moritz","Fluch","342373")
autoren=[autor1,autor2,autor3]

auswahl = mainMenu()



while(auswahl!="x"):

    if(auswahl=="n"):
        neuerRaum=raumErstellen()
        Raumliste.append(neuerRaum)
        Tuerliste= addTuer(Tuerliste,neuerRaum)
        Fensterliste= addFenster(Fensterliste,neuerRaum)
        bericht=open("Bericht.txt","a")
        bertxt= berichtErzeugen(neuerRaum,autoren)
        print(bertxt)
        bericht.write(bertxt)
        bericht.close()
        auswahl=mainMenu()
        
    elif(auswahl=="f"):
        print(fausgeben(Fensterliste))
        auswahl=mainMenu()
    
    elif(auswahl=="t"):
        print(tausgeben(Tuerliste))
        auswahl=mainMenu()
    elif(auswahl=="r"):
        listRaeume(Raumliste)
        if(Raumliste==[]):
            print(" keine Räume vorhanden\n\n")
        auswahl=mainMenu()
    
    else:
        print("ungültige Eingabe")
        auswahl=mainMenu()

sys.exit()        







    
