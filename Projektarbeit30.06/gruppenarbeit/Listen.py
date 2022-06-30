# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:53:03 2022

@author: Franzi
"""
# from Raum import Raum
# from Wand import Wand
# from Oeffnung import Oeffnung
# from Fenster import Fenster
# from Tuer import Tuer

#erstellt raumübergreifende Liste aller Türen
def addTuer(tliste,raum):
    for i in range (0,len(raum.Waende)-1):
        for j in range (0,len(raum.Waende[i].Oeffnungen)-1):
            if(type(raum.Waende[i].Oeffnungen[j]).__name__=="Tuer"):
                tliste.append(raum.Waende[i].Oeffnungen[i])
        return tliste
        
    
#erstelt raumübergreifende Liste aller Fenster    
def addFenster(fliste,raum):
    for i in range (0,len(raum.Waende)-1):
        for j in range (0,len(raum.Waende[i].Oeffnungen)-1):
            if(type(raum.Waende[i].Oeffnungen[j]).__name__=="Fenster"):
                fliste.append(raum.Waende[i].Oeffnungen[i])
        return fliste
    






# gibt gesamte Fensterliste (Aller Räume) als String zurück
def fausgeben(fliste):
    ausgabe="\nFensterliste:\n------------\n"
    for i in range (0,len(fliste)-1):
        ausgabe= ausgabe + str(i) + "-Fenster (Höhe: " + str(fliste[i].Hoehe)+"m, Breite: " + str(fliste[i].Breite)+ "m, Schallschutzklasse: " + str(fliste[i].Schallschutzklasse) + ", U-Wert: " + str(fliste[i].UWert) +", Hersteller: " + fliste[i].Hersteller + ", Brüstungshöhe: "+ str(fliste[i].Bruestungshoehe) + ")\n"
        
    return ausgabe

    
# gibt gesamte Türliste (aller Räume) als String zurück
def tausgeben(tliste):
    ausgabe="\nTürliste:\n------------\n"
    for i in range (0,len(tliste)-1):
        ausgabe= ausgabe + str(i) + "-Tür (Höhe: " + str(tliste[i].Hoehe)+"m, Breite: " + str(tliste[i].Breite)+ "m, Rauchschutz: " + str(tliste[i].Rauchschutz) + ", Notausgang: " + str(tliste[i].Notausgang) +", Hersteller: " + tliste[i].Hersteller +")\n"
        
    return ausgabe
 
    
 

# gibt alle Fenster eines Raumes als String zurück
def listFenster(raum):
    ausgabe="\nFensterliste:\n------------\n"
    k=0
    for i in range(0,len(raum.Waende)-1):
        for j in range(0,len(raum.Waende[i].Oeffnungen)-1):
            if(type(raum.Waende[i].Oeffnungen[j]).__name__=="Fenster"):
                k+=1
                ausgabe=ausgabe + str(k) + "-Fenster (Höhe: " + str(raum.Waende[i].Oeffnungen[j].Hoehe)+"m, Breite: " + str(raum.Waende[i].Oeffnungen[j].Breite)+ "m, Schallschutzklasse: " + str(raum.Waende[i].Oeffnungen[j].Schallschutzklasse) + ", U-Wert: " + str(raum.Waende[i].Oeffnungen[j].UWert) +", Hersteller: " + raum.Waende[i].Oeffnungen[j].Hersteller + ", Brüstungshöhe: "+ str(raum.Waende[i].Oeffnungen[j].Bruestungshoehe) + ")\n"
    return ausgabe


# gibt alle Türen eines Raumes als String zurück   
def listTueren(raum):
    ausgabe="\nTürliste:\n------------\n"
    k=0
    for i in range(0,len(raum.Waende())-1):
        for j in range(0,len(raum.Waende[i].Oeffnungen)-1):
            if(type(raum.Waende[i].Oeffnungen[j]).__name__=="Tuer"):
                k+=1
                ausgabe=ausgabe + str(k) + "-Tür (Höhe: " + str(raum.Waende[i].Oeffnungen[j].Hoehe)+"m, Breite: " + str(raum.Waende[i].Oeffnungen[j].Breite)+ "m, Rauchschutz: " + str(raum.Waende[i].Oeffnungen[j].Rauchschutz) + ", Notausgang: " + str(raum.Waende[i].Oeffnungen[j].Notausgang) +", Hersteller: " + raum.Waende[i].Oeffnungen[j].Hersteller +")\n"
    return ausgabe


#gibt alle Räume einer Liste als String zurück, Funktion wird nicht genutzt
def listRaeume(rliste):
    s="Raumbuch\n-----------\n"
    for i in range(0,len(rliste)-1):
        s+=str(i+1)+"-Raum (Raumbezechnung:"+rliste[i].RBezeichnung+", Raumnummer:"+rliste[i].Raumnummer+"\n"
        
        v="        Raumvolumen:"+str(rliste[i].Volumen())+"m³\n"
        u="        Raumumfang:"+str(rliste[i].Umfang())+"m\n\n"
        fb="        Raumseitenfläche Brutto:"+str(rliste[i].SeitenflächenGesamt())+"m²\n"
        fn="        Raumseitenfläche Netto:"+str(rliste[i].SeitenflächenMinusOeffnungen())+ "m²\n"
        
        s+=v+u+fb+fn
    return s

#gibt einen Raum als String zurück
def raumToString(raum):
    s="1-Raum (Raumbezechnung:"+raum.RBezeichnung+", Raumnummer:"+raum.Raumnummer+"\n"
    
    v="        Raumvolumen:"+str(raum.Volumen())+"m³\n"
    u="        Raumumfang:"+str(raum.Umfang())+"m\n\n"
    fb="        Raumseitenfläche Brutto:"+str(raum.SeitenflächenGesamt())+"m²\n"
    fn="        Raumseitenfläche Netto:"+str(raum.SeitenflächenMinusOeffnungen())+ "m²\n"
    
    s+=v+u+fb+fn
    return s

    

def autorenToString(aliste):
    s=""
    for i in range(0,len(aliste)-1):
        s+=aliste[i].Nachname+", "+aliste[i].Vorname+"                                                        "+aliste[i].Matrikelnr
    s+="-------------------------------------------------------------------------------------------------\n"
    return s


def berichtErzeugen(raum,aliste):
    
    s=autorenToString(aliste)+raumToString(raum)+listTueren(raum)+listFenster(raum)
    s+="\n-------------------------------------------------------------------------------------------------\nEnde des Berichts"
    return s