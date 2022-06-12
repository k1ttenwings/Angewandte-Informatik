# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:32:49 2022

@author: muell
"""

class Oeffnung:
    Hoehe=0.0
    Breite=0.0
    Durchmesser=0.0
    Wand=Wand()
    Fenster=Fenster()
    
    def __init__(self,Öh,Öb,Öd,Wnd):
        self.Hoehe=Öh
        self.Breite=Öb
        self.Durchmesser=Öd
        self.Wand=Wnd