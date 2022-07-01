# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:33:22 2022

@author: fluch
"""

from Oeffnung import Oeffnung


class Tuer(Oeffnung):
    Rauchschutz=False
    Notausgang=False
    Hersteller=""
    
    def __init__(self,Rs,Na,Th,Öh,Öb,Öd,w):
        super().__init__(Öh,Öb,Öd,w)
        self.Rauchschutz=Rs
        self.Notausgang=Na
        self.Hersteller=Th