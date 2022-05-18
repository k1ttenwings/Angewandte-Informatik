# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:25:13 2022

@author: fluch
"""


class Raum:
    Raumhoehe=0.0
    RBezeichnung=""
    Raumnummer=""
    
    def __init__(self,h,Rb,Rn):
        self.Raumhoehe=0.0
        self.RBezeichnung=""
        self.Raumnummer=""
    
class Wand:
    #Waende = [None,None,None,None]
    WLaenge=0.0
    WHoehe=0.0
    WDicke=0.0
    
    #Haus=Raum()

    #NordWand = Wand()
    #Ostwand = Wand()
    #Südwand = Wand()
    #Westwand = Wand()
    
    #Haus.Waende [0]= NordWand
    #Haus.Waende [1]= Ostwand
    #Haus.Waende [2]= Südwand
    #Haus.Waende [3]= Westwand
    
    def __init__(self,Wl,Wh,Wd):
        self.WLaenge=Wl
        self.WHoehe=Wh
        self.WDicke=Wd
        
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
    ÖHoehe=0.0
    ÖBreite=0.0
    ÖDurchmesser:0.0
    
    def __init__(self,Öh,Öb,Öd):
        self.ÖHoehe=Öh
        self.ÖBreite=Öb
        self.ÖDurchmesser=Öd
        
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
        
