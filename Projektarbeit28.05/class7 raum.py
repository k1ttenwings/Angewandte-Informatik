# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:35:08 2022

@author: muell
"""


class Raum:
    Raumhoehe=0.0
    Waende=[Wand(),Wand(),Wand(),Wand()]
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
        for i in range (1,len(self.Waende())+1):
                        Umfang = Umfang + self.Waende[i].Laenge
        return Umfang  
    
    
    
    """ Bei der Berechnung des Volumens wird von ausschließlich quaderförmigen Räumen ausgegangen """
    def Volumen(self):
        Laenge=0.0
        Breite=0.0
        Hoehe=self.Waende[1].Hoehe
        
        if (self.Waende[1].Laenge == self.Waende[2].Laenge==self.Waende[3].Laenge==self.Waende[4].Laenge):
            Laenge=self.Waende[1].Laenge
            Breite=self.Waende[1].Laenge          
        elif (self.Waende[1].Laenge != self.Waende[2].Laenge):
            Laenge=self.Waende[1].Laenge
            Breite=self.Waende[2].Laenge        
        else:
            Laenge=self.Waende[1].Laenge
            Breite=self.Waende[3].Laenge
        return Laenge*Breite*Hoehe
    
    
    """Berechnung Raumseitenfläche ohne Berücksichtigung der Öffnungen"""
    def SeitenflächenGesamt(self):
        Flaeche=0.0
        for i in range (1,len(self.Waende())+1):
            Flaeche+=self.Waende[i].Laenge*self.Waende[i].Hoehe
        return Flaeche
    
    """Berechnung Raumseitenfläche mit Berücksichtigung der Öffnungen.
    ---> VOB??
    """
    def SeitenflächenMinusÖffnungen(self):
        Flaeche=0.0
        Oeffnungen=0.0
        for i in range (1, len(self.Waende())+1):
            Flaeche +=self.Waende[i].Lange*self.Waende[i].Hoehe
            for j in range (1, len(self.Waende[i].Oeffnung())+1):
                Oeffnungen=self.Waende[i].Oeffnung[j].Hoehe*self.Waende[i].Oeffnung[j]
            Flaeche -= Oeffnungen
        return Flaeche

