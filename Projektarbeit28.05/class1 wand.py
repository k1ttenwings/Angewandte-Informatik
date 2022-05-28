# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:28:32 2022

@author: muell
"""

class Wand:
    Laenge=0.0
    Hoehe=0.0
    Dicke=0.0
    Oeffnung  = []
        
    def __init__(self,Wl,Wh,Wd,Ofng):
        self.Laenge=Wl
        self.Hoehe=Wh
        self.Dicke=Wd
        self.Oeffnung=Ofng