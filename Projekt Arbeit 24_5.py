# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:25:13 2022

@author: fluch
"""

        
    
class Wand:
    Raum=Raum()
    Laenge=0.0
    Hoehe=0.0
    Dicke=0.0
    Oeffnung  = []
        
    def __init__(self,Wl,Wh,Wd,Ofng):
        self.Laenge=Wl
        self.Hoehe=Wh
        self.Dicke=Wd
        self.Oeffnung=Ofng
        
class Mauerwerk:
    Steinsorte=""
    Sichtmauerwerk=False
    
    def __init__(self,Ss,Sm,Wl,Wh,Wd):
        super().__init__(Wl,Wh,Wd)
        self.Steinsorte=Ss
        self.Sichtmauerwerk=Sm
        #self.Sichtmauerwerk()=Sm
        
class Stahlbetonwand:
    Stahldichte=0.0
    Betondichte=0.0
    Bertonfertigkeitsklassen=0.0
    Bewehrungsgehlat=0.0
    
    def __init__(self,Sd,Bd,Bfk,Bg,Wl,Wh,Wd):
        super().__init__(Wl,Wh,Wd)
        self.Stahldichte=Sd
        self.Betondichte=Bd
        self.Bertonfertigkeitsklassen=Bfk
        self.Bewehrungsgehlat=Bg
        
        
class Oeffnung:
    Hoehe=0.0
    Breite=0.0
    Durchmesser=0.0
    Wand=Wand()
    
    def __init__(self,Öh,Öb,Öd,Wnd):
        self.Hoehe=Öh
        self.Breite=Öb
        self.Durchmesser=Öd
        self.Wand=Wnd
        
class Tuer(Oeffnung):
    Rauchschutz=False
    Notausgang=False
    Hersteller=""
    
    def __init__(self,Rs,Na,Th,Öh,Öb,Öd):
        super().__init__(Öh, Öb, Öd)
        self.Rauchschutz=Rs
        #self.Rauchschutz()=Rs
        self.Notausgang=Na
        #self.Notausgang()=Na
        self.Hersteller=Th
        
class Fenster:
    Schallschutzklasse=""
    U_Wert=0.0
    FHersteller=""
    Büstingshöhe=0.0
    
    def __init__(self,Ssk,U,Fh,BRH):
        self.Schallschutzklasse=Ssk
        self.U_Wert=U
        self.FHersteller=Fh
        self.Brüstungshöhe=BRH







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

























        