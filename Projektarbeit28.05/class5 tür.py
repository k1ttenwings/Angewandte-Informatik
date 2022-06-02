# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:33:22 2022

@author: muell
"""

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