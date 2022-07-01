# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:30:00 2022

@author: fluch
"""
from Wand import Wand 

class Mauerwerk(Wand):
    Steinsorte=""
    Sichtmauerwerk=False
    
    def __init__(self,Ss,Sm,Wl,Wh,Wd,Of):
        super().__init__(Wl,Wh,Wd,Of)
        self.Steinsorte=Ss
        self.Sichtmauerwerk=Sm