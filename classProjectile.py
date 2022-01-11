"""
Auteur: Rodolphe Lajugie
    
date de création: 20 décembre 2021
"""
    
class Projectile(): 
    def __init__(self,x1,y1,x2,y2):
        self.dy = 15
        self.position_x1=x1
        self.position_y1=y1
        self.position_x2=x2
        self.position_y2=y2
        self.taille_x=4
        self.taille_y=20
    
    def get_taille(self):
        return [self.taille_x, self.taille_y]
    def get_position(self):
        return [self.position_x1,self.position_y1,self.position_x2,self.position_y2]

    
    def deplacement(self):
        self.position_y1 = self.position_y1 - self.dy
        self.position_y2 = self.position_y2 - self.dy
        return [self.position_x1,self.position_y1,self.position_x2,self.position_y2]

