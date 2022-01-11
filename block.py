"""
Auteur : Rodolphe Lajugie
    
Date de création : 14 décembre 2021
"""

class Block():
    
    def __init__(self,pX,pY):
        self.vie=3
        self.taille_x=30
        self.taille_y=30
        self.position_x=pX
        self.position_y=pY
        
    def perdre_vie(self):
        self.vie=0
        return self.vie
    
    def get_position(self):
        return [self.position_x,self.position_y]
    
    def get_taille(self):
        return [self.taille_x,self.taille_y]