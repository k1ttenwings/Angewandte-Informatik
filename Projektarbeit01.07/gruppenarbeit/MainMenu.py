# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:47:56 2022

@author: Franzi
"""
import time

#Erzeugt die Optionen des Hauptmenüs, gibt die vom Nutzer gewählte Option als String zurück
def mainMenu():
    print("\n\n---Hauptmenü---\n")
    #Quelle sleep: https://realpython.com/python-sleep/
    #Hinzugefügt, weil "neuen Raum erstellen (n) sonst vor "---Hauptmenü---" ausgegeben wurde
    time.sleep(1)
    eingabe=input(" neuen Raum erstellen (n)\n Raumliste ausgeben (r)\n Türliste ausgeben (t)\n Fensterliste ausgeben (f)\n Programm beenden (x)\n ")
    #raumliste? raum auswählen? wand auswählen? umfang, volumen, fläche durch nutzer abfragen?
    
    
    
    return eingabe
