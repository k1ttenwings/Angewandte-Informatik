
"""
Created on Sat May 28 18:33:56 2022
@author: muell
"""
from Oeffnung import Oeffnung

class Fenster(Oeffnung):
    Schallschutzklasse=""
    UWert=0.0
    Hersteller=""
    Bruestungshoehe=0.0
    
    def __init__(self,Ssk,U,Fh,BRH,Öh,Öb,Öd,Wnd):
        super().__init__(Öh, Öb, Öd, Wnd)
        self.Schallschutzklasse=Ssk
        self.U_Wert=U
        self.Hersteller=Fh
        self.Brüstungshöhe=BRH