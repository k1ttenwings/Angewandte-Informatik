# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:50:02 2022

@author: Franzi
"""
from Wand import Wand
from Raum import Raum
from Fenster import Fenster
from Tuer import Tuer
from Mauerwerk import Mauerwerk
from Stahlbetonwand import Stahlbetonwand






# Enthält die Funktionen zum Erstellen von Raumobjekten






#erstellt Eigenschaften eines Fensters
def fensterErstellen(h,b,d,w):
    u=0.0
    brh=0.0
    ssk=input("\n Schallschutzklasse: ")
    u=float(input("\n U-Wert: "))
    fh=input("\n Hersteller: ")
    brh=float(input("\n Brüstunghöhe: "))
    f= Fenster(ssk,u,fh,brh,h,b,d,w)
    return f

#Erstellt Eigenschaften einer Tür
def tuerErstellen(h,b,d,w):
    rs= bool(input("\n Rauchschutz vorhanden? (j/n)"))
    na= bool(input("\n Ist diese Tür ein Notausgang? (j/n)"))
    th= input("\n Hersteller: ")
    t= Tuer(rs,na,th,h,b,d,w)
    return t


#Erstellt allgemeine Eigenschaften einer Öffnung, ruft entweder fensterErstellen oder tuerErstellen auf
def oeffnungErstellen(wnd):
    oe=None
    w=wnd
    
    h=0.0
    b=0.0
    d=0.0
    form=input("\n runde (r) oder eckige (e) Öffnung?")
    typ=""
    typ = input("\n Fenster (f) oder Tür (t) hinzufügen? ")

    if(form=="r"):
        d=input("\n Durchmesser: ")
    elif(form=="e"):    
        h=input("\n Höhe:")
        b=input("\n Breite: ")
    else:
        print("\n ungültige Eingabe")
        oeffnungErstellen(wnd)
    
    if(typ=="f"):
        oe=fensterErstellen(h,b,d,w)
        return oe
    elif(typ=="t"):
        oe=tuerErstellen(h,b,d,w)
        return oe
    else:
        print("\n ungültige Eingabe")
        return oe
    
    

#Fragt ab, ob Öffnungen erstellt werden sollen und ruft ggf mehrfach oeffnungErstellen auf
def oeffnungenErstellen(wnd,oe):
    oeList=oe
    bool= input("\n Wandöffnung hinzufügen? (j/n)")
    if(bool=="j"):
        oeList.append(oeffnungErstellen(wnd))
        oeffnungenErstellen(wnd,oeList)
    elif(bool=="n"):
        return oeList
    else:
        print("\n ungültige Eingabe!")
        return oeList
    
#Erstellt Eigenschaften einer gemauerten Wand
def mauerwerkErstellen(l,h,d,oe):
    sicht=False
    stein= input("\n Steinsorte: ")
    sichtString= input("\n Sichtmauererk? (j/n)")

    if (sichtString=="j"):
        sicht=True
    elif(sichtString=="n"):
        sicht=False
    else:
        print("ungültige Eingabe!")
        return
        
    neueWand= Mauerwerk(stein,sicht,l,h,d,oe)
    return neueWand

#Erstellt Eigenschaften einer Wand aus Stahlbeton
def stahlbetonErstellen(l,h,d,oe):
    sd=float(input("\n Stahldichte: "))
    bd=float(input("\n Betondichte: "))
    bfk=float(input("\n Betonfestigkeitsklasse: "))
    bewG=float(input("\n Bewehrungsgehalt: "))
    
    neueWand= Stahlbetonwand(sd,bd,bfk,bewG,l,h,d,oe)
    return neueWand


#Erstellt allgemeine Eigenschaften einer Wand
#ruft entweder stahlbetonErstellen oder mauerwerkErstellen auf

def wandErstellen(n):
    print("\nWand "+ str(n) +":")
    l= input("\n Länge: ")
    h= input("\n Höhe: ")
    d= input("\n Dicke: ")
    oe=[]
    neueWand = None
    typ= input("\nWandtyp:\n Mauerwerk (m)\n Stahlbeton (s)\n Undefiniert (u)\n ")
    
    if(typ=="m"):
        neueWand= mauerwerkErstellen(l,h,d,oe)
    
    elif(typ=="s"):        
        neueWand= stahlbetonErstellen(l,h,d,oe)
    
    elif(typ=="u"):
        neueWand= Wand(l,h,d,oe)
    
    else:
        print("\n ungültige Eingabe!")
        return
    oe= oeffnungenErstellen(neueWand,oe)    
    return neueWand


#Erstellt einen Raum, ruft Funktion zum Erstellen von Wänden auf
def raumErstellen():
    h = float(input("\n Höhe: "))
    Rb = input("\n Raumbezeichnung: ")
    Rn = input("\n Raumnummer: ")
    
    wand1= wandErstellen(1)
    wand2= wandErstellen(2)
    wand3= wandErstellen(3)
    wand4= wandErstellen(4)
    
    Wnde=[wand1,wand2,wand3,wand4]
    
    neuerRaum = Raum(h,Wnde,Rb,Rn)
    return neuerRaum

    
