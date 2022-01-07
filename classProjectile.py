"""
Auteur: Rodolphe Lajugie
    
date de création: 20 décembre 2021
"""
    
class Projectile():
    
    def __init__(self,dx1,dy1,dx2,dy2):
        self.dy = 0
        self.position_x1=dx1
        self.position_y1=dy1
        self.position_x2=dx2
        self.position_y2=dy2
        self.taille_x=3
        self.taille_y=20
    
    def get_taille(self):
        return [self.taille_x, self.taille_y]
    def get_position(self):
        return [self.position_x1,self.position_y1,self.position_x2,self.position_y2]

    
    def deplacement(self):
        while True:
            self.dy = -20
            return self.position_y1-self.dy
        self.dy = 0
        return self.position_y1