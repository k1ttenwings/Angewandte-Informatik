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



#Funktion: Bericht nach Eingabe erstellen


#Fenster erstellen
def fensterErstellen(h,b,d,w):
    ssk=input("\n Schallschutzklasse: ")
    u=input("\n U-Wert: ")
    fh=input("\n Hersteller: ")
    brh=input("Brüstunghöhe: ")
    f= Fenster(ssk,u,fh,brh,h,b,d,w)
    return f

#Tür erstellen
def tuerErstellen(h,b,d,w):
    rs= bool(input("\n Rauchschutz vorhanden? (j/n)"))
    na= bool(input("\n Ist diese Tür ein Notausgang? (j/n)"))
    th= input("\n Hersteller: ")
    t= Tuer(rs,na,th,h,b,d)
    return


"""
Ich bin ein Kommentar :) .
"""
def oeffnungErstellen(wnd):
    oe=None
    w=wnd
    #abfrage rausnehmen
    eingabe=input("\n Öffnung erstellen? (j/n)")
    if(eingabe=="j"):
        h=0.0
        b=0.0
        d=0.0
        form=input("\n runde (r) oder eckige (e) Öffnung?")
        typ = input("\n Fenster (f) oder Tür (t) hinzufügen? ")
    
        if(form=="r"):
            d=float(input("\n Durchmesser: "))
        elif(form=="e"):    
            h=float(input("\n Höhe:"))
            b=float(input("\n Breite: "))
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
            print("\n ungültige Eingabe!")
            return oe
    else:
        print("\n dann nicht...")
        return oe    
    

#Oeffnung erstellen
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


def stahlbetonErstellen(l,h,d,oe):
    #Floats casten und exceptions handeln
    sd=float(input("\n Stahldchte: "))
    bd=float(input("\n Betondichte: "))
    bfk=float(input("\n Betonfestigkeitsklasse: "))
    bewG=float(input("\n Bewehrungsgehalt: "))
    
    neueWand= Stahlbetonwand(sd,bd,bfk,bewG,l,h,d,oe)
    return neueWand


"""
Hallo.
"""
def wandErstellen(n):
    print("\nWand "+ str(n) +":")
    l= input("\n Länge: ")
    h= input("\n Höhe: ")
    d= input("\n Dicke: ")
    oe=[]
    neueWand = None
    typ= input("\nWandtyp:\n Mauerwerk (m)\n Stahlbeton (s)\n Undefiniert (u)\n")
    
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


#Raum erstellen
def raumErstellen():
    Eingabe = input("Raum erstellen? (j/n)\n")
        
    if (Eingabe == "j"): 
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

    elif (Eingabe == "n"):
        print("Dann nicht...")
        return
    else:
        print("Ungültige Eingabe")
        return
    return

#Hauptmenu
def mainMenu():
    return


