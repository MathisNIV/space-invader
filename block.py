"""
Auteur : Rodolphe Lajugie
    
Date de création : 14 décembre 2021
"""

class block():
    
    def __init__(self,pX,pY):
        self.vie=1
        self.taille_x=1
        self.taille_y=1
        self.postionx=pX
        self.position_y=pY
        
    def destruction(self):
        self.vie=0
        