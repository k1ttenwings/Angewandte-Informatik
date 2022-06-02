# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:33:56 2022

@author: muell
"""

class Fenster:
    Schallschutzklasse=""
    U_Wert=0.0
    FHersteller=""
    Büstungshöhe=0.0
    
    def __init__(self,Ssk,U,Fh,BRH):
        self.Schallschutzklasse=Ssk
        self.U_Wert=U
        self.FHersteller=Fh
        self.Brüstungshöhe=BRH