# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:30:00 2022

@author: muell
"""

class Mauerwerk:
    Steinsorte=""
    Sichtmauerwerk=False
    
    def __init__(self,Ss,Sm,Wl,Wh,Wd):
        super().__init__(Wl,Wh,Wd)
        self.Steinsorte=Ss
        self.Sichtmauerwerk=Sm
        #self.Sichtmauerwerk()=Sm