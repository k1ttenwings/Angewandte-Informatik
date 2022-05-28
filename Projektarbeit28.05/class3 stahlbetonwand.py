# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:32:15 2022

@author: muell
"""

class Stahlbetonwand:
    Stahldichte=0.0
    Betondichte=0.0
    Bertonfestigkeitsklassen=0.0
    Bewehrungsgehalt=0.0
    
    def __init__(self,Sd,Bd,Bfk,Bg,Wl,Wh,Wd):
        super().__init__(Wl,Wh,Wd)
        self.Stahldichte=Sd
        self.Betondichte=Bd
        self.Bertonfestigkeitsklassen=Bfk
        self.Bewehrungsgehalt=Bg