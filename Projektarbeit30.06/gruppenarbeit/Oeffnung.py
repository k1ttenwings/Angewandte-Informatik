# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:32:49 2022

@author: muell
"""
from Wand import Wand


class Oeffnung:
    Hoehe=0.0
    Breite=0.0
    Durchmesser=0.0
    Wand=None
    
    def __init__(self,Öh,Öb,Wnd):
        self.Hoehe=Öh
        self.Breite=Öb
        self.Wand=Wnd
    