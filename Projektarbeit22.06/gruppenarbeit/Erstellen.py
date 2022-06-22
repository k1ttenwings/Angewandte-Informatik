# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:50:02 2022

@author: Franzi
"""
from Wand import Wand
from Raum import Raum
from Fenster import Fenster
from Tuer import Tuer



#Funktion: Bericht nach Eingabe erstellen


#Fenster erstellen
def fensterErstellen():
    f= Fenster(Ssk,U,Fh,BRH)
    return f

#Tür erstellen
def tuerErstellen():
    t= Tuer(Rs,Na,Th,Öh,Öb,Öd)
    return

#Oeffnung erstellen
def oeffnungErstellen():
    type = input("\n Fenster (f) oder Tür (t) hinzufügen? ")
    oe=None
    if(type=="f"):
        oe=fensterErstellen()
        return oe
    elif(type=="t"):
        oe=tuerErstellen()
        return oe
    else:
        print("\n ungültige Eingabe!")
        return oe

#Oeffnung erstellen
def oeffnungenErstellen(oe):
    oeList=oe
    bool= input("\n Wandöffnung hinzufügen? (j/n)")
    if(bool=="j"):
        oeList.append(oeffnungErstellen())
        oeffnungenErstellen(oeList)
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
        
    neueWand= Wand(stein,sicht,l,h,d,oe)
    return neueWand


def stahlbetonErstellen(l,h,d,oe):
    #Floats casten und exceptions handeln
    sd=float(input("\n Stahldchte: "))
    bd=float(input("\n Betondichte: "))
    bfk=float(input("\n Betonfestigkeitsklasse: "))
    bewG=float(input("\n Bewehrungsgehalt: "))
    
    neueWand= Wand(sd,bd,bfk,bewG,l,h,d,oe)
    return neueWand


#Wand erstellen
def wandErstellen():
    l= input("\n Länge: ")
    h= input("\n Höhe: ")
    d= input("\n Dicke: ")
    oe=[]
    oe= oeffnungenErstellen(oe)
    neueWand = None
    type= input("\nWandtyp:\n Mauerwerk (m)\n Stahlbeton (s)\n Undefiniert (u)\n")
    
    if(type=="m"):
        neueWand= mauerwerkErstellen(l,h,d,oe)
    
    elif(type=="s"):        
        neueWand= stahlbetonErstellen(l,h,d,oe)
    
    elif(type=="u"):
        neueWand= Wand(l,h,d,oe)
    
    else:
        print("\n ungültige Eingabe!")
        return
        
    return neueWand


#Raum erstellen
def raumErstellen():
    Eingabe = input("Raum erstellen? (j/n)\n")
        
    if (Eingabe == "y"): 
        h = float(input("\n Höhe: "))
        Rb = input("\n Raumbezeichnung: ")
        Rn = input("\n Raumnummer: ")
        
        wand1= wandErstellen()
        wand2= wandErstellen()
        wand3= wandErstellen()
        wand4= wandErstellen()
        
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


