# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:35:08 2022

@author: muell
"""
from Wand import *
from Mauerwerk import *
from Stahlbetonwand import *
from Oeffnung import *
from Tuer import *
from Fenster import *
import math

class Raum:
    Raumhoehe=0.0
    Waende=[None,None,None,None]
    RBezeichnung=""
    Raumnummer=""
    

    
    def __init__(self,h,Wnde,Rb,Rn):
        self.Raumhoehe=0.0
        self.Waende = Wnde
        self.RBezeichnung=""
        self.Raumnummer=""
    
    """Berechnung Umfang """
    def Umfang(self):
        Umfang = 0.0
        for i in range (0,len(self.Waende)):
                        Umfang = float(Umfang) + float(self.Waende[i].Laenge)
        return Umfang  
    
    
    
    """ Bei der Berechnung des Volumens wird von ausschließlich quaderförmigen Räumen ausgegangen """
    def Volumen(self):
        Laenge=0.0
        Breite=0.0
        Hoehe=self.Waende[0].Hoehe
        
        if (self.Waende[0].Laenge == self.Waende[1].Laenge==self.Waende[2].Laenge==self.Waende[3].Laenge):
            Laenge=self.Waende[0].Laenge
            Breite=self.Waende[0].Laenge          
        elif (self.Waende[0].Laenge != self.Waende[1].Laenge):
            Laenge=self.Waende[0].Laenge
            Breite=self.Waende[1].Laenge        
        else:
            Laenge=self.Waende[0].Laenge
            Breite=self.Waende[2].Laenge
        
        ergebnis= float(Laenge)*float(Breite)*float(Hoehe)
        return ergebnis
    
    
    """Berechnung Raumseitenfläche ohne Berücksichtigung der Öffnungen"""
    def SeitenflächenGesamt(self):
        Flaeche=0.0
        for i in range (0,len(self.Waende)):
            Flaeche+=float(self.Waende[i].Laenge)*float(self.Waende[i].Hoehe)
        return Flaeche
    
    """Berechnung Raumseitenfläche mit Berücksichtigung der Öffnungen.
    ---> VOB??
    """
    def SeitenflächenMinusOeffnungen(self):
        Flaeche=0.0
        Oeffnungenen=0.0
        for i in range (0, len(self.Waende)):
            Flaeche +=float(self.Waende[i].Laenge)*float(self.Waende[i].Hoehe)
            for j in range (0, len(self.Waende[i].Oeffnungen)):
                print("Öffnung:"+str(j))
                if(self.Waende[i].Oeffnungen[j].Durchmesser==0.0):
                    Oeffnungenen+=float(self.Waende[i].Oeffnungen[j].Hoehe)*float(self.Waende[i].Oeffnungen[j].Breite)
                    print("Größe:"+str(Oeffnungenen))
                else:
                    r=float(self.Waende[i].Oeffnungen[j].Durchmesser)/2
                    Oeffnungenen+=math.pow(r,2.0)*math.pi
            Flaeche -= float(Oeffnungenen)
        return Flaeche

