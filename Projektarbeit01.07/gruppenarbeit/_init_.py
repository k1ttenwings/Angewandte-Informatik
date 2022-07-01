# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:31:27 2022

@author: Franzi
"""

import os
import sys
from Erstellen import *
from MainMenu import *
from Listen import *
from Autor import Autor



#Autorenobjekte zur Erstellung des berichts
autor1=Autor("Thorben  ","Müller","348238")
autor2=Autor("Franziska","Köhler","297224")
autor3=Autor("Moritz    ","Fluch","342373")
autoren=[autor1,autor2,autor3]



#Raumübergreifende Listen
Raumliste = []
Tuerliste = []
Fensterliste = []

#Aufrufen des Hauptmenüs und von Funktionen je nach Nutzereingabe 
auswahl = mainMenu()

while(auswahl!="x"):

    if(auswahl=="n"):
        neuerRaum=raumErstellen()
        Raumliste.append(neuerRaum)
        Tuerliste= addTuer(Tuerliste,neuerRaum)
        Fensterliste= addFenster(Fensterliste,neuerRaum)
        path=os.path.join(os.getcwd(),'Berichte','Bericht.txt')
        bericht=open(path,"a")
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
        s=listRaeume(Raumliste)
        print(s)
        if(Raumliste==[]):
            print(" keine Räume vorhanden\n\n")
        auswahl=mainMenu()
    elif(auswahl=="cwd"):
        print(os.getcwd())
        auswahl=mainMenu()
    # elif(auswahl=="txt"):
    #     p=os.path.join(os.getcwd(),'Berichte','Bericht.txt')
    #     print(p+"\n")
    #     bericht=open(p,"a")
    #     bericht.close()
    #     auwahl=mainMenu()
    
    else:
        print("ungültige Eingabe")
        auswahl=mainMenu()

# Quelle: https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
sys.exit("Nutzereingabe: Programm beenden")


    
