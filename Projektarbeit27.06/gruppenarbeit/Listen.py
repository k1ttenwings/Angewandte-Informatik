# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:53:03 2022

@author: Franzi
"""

def addTuer(tliste,raum)

    for i in range (1,raum.Waende()+1):
        for j in range (1,len(raum.Waende[i].Oeffnungen())+1):
            if(type(raum.Waende[i].Oeffnungen[j]).__name__=="Tuer"):
                tliste.append(raum.Waende[i].Oeffnungen[i])
        return tliste
        
    
def addFester(fliste,raum):
    for i in range (1,raum.Waende()+1):
        for j in range (1,len(raum.Waende[i].Oeffnungen())+1):
            if(type(raum.Waende[i].Oeffnungen[j]).__name__=="Fenster"):
                fliste.append(raum.Waende[i].Oeffnungen[i])
        return fliste
    


# gibt gesamte Fensterliste (Aller Räume) zurück
def fausgeben(fliste):
    ausgabe="\nFensterliste:\n------------\n"
    for i in range (1,len(fliste)+1):
        ausgabe= ausgabe + str(i) + "-Fenster (Höhe: " + str(fliste[i].Hoehe)+"m, Breite: " + str(fliste[i].Breite)+ "m, Schallschutzklasse: " + str(fliste[i].Schallschutzklasse) + ", U-Wert: " + str(fliste[i].UWert) +", Hersteller: " + fliste[i].Hersteller + ", Brüstungshöhe: "+ str(fliste[i].Bruestungshoehe) + ")\n"
        
    return ausgabe

    
# gibt gesamte Türliste (aller Räume) zurück
def tausgeben(tliste):
    ausgabe="\nTürliste:\n------------\n"
    for i in range (1,len(tliste)+1):
        ausgabe= ausgabe + str(i) + "-Tür (Höhe: " + str(tliste[i].Hoehe)+"m, Breite: " + str(tliste[i].Breite)+ "m, Rauchschutz: " + str(tliste[i].Rauchschutz) + ", Notausgang: " + str(tliste[i].Notausgang) +", Hersteller: " + fliste[i].Hersteller +")\n"
        
    return ausgabe
 

# gibt alle Fenster eines Raumes als String zurück
def listFenster(raum):
    ausgabe=""
    k=0
    for i in range(1,len(raum.Waende())+1):
        for j in range(1,len(raum.Waende[i].Oeffnungen())+1)
            if(type(raum.Waende[i].Oeffnungen[j]).__name__=="Fenster"):
                k+=1
                ausgabe=ausgabe + str(k) + "-Fenster (Höhe: " + str(fliste[i].Hoehe)+"m, Breite: " + str(fliste[i].Breite)+ "m, Schallschutzklasse: " + str(fliste[i].Schallschutzklasse) + ", U-Wert: " + str(fliste[i].UWert) +", Hersteller: " + fliste[i].Hersteller + ", Brüstungshöhe: "+ str(fliste[i].Bruestungshoehe) + ")\n"
    return ausgabe




# gibt alle Türen eines Raumes als String zurück   
def listTueren(raum):
    
    
def berichtErzeugen(rliste):
    s=
    return s