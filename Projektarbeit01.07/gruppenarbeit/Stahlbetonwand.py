# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:32:15 2022

@author: fluch
"""
from Wand import Wand

class Stahlbetonwand(Wand):
    Stahldichte=0.0
    Betondichte=0.0
    Betonfestigkeitsklassen=0.0
    Bewehrungsgehalt=0.0
    
    def __init__(self,Sd,Bd,Bfk,Bg,Wl,Wh,Wd,Oe):
        super().__init__(Wl,Wh,Wd,Oe)
        self.Stahldichte=Sd
        self.Betondichte=Bd
        self.Betonfestigkeitsklassen=Bfk
        self.Bewehrungsgehalt=Bg