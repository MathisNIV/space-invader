"""
Auteur: Rodolphe Lajugie
    
date de création: 20 décembre 2021
"""
    
class Projectile():
    
    def __init__(self,pX,pY):
        self.puissance=1
        self.dy = 0.2
        self.position_x=pX
        self.position_y=pY
        self.taille_x=3
        self.taille_y=3
    
    def get_taille(self):
        return [self.taille_x, self.taille_y]
        
    def bolPos(self):
        blo=False
        if self.position_y < 0 :
            blo = True
        return blo
    
    def getPuissance(self):
        return self.puissance
    
    def deplacement(self):
        blo=self.bolPos()
        while blo != True:
            self.position_y = self.position_y - self.vitesse
            blo = self.bolPos()
            print(blo, self.position_y)
        
        return self.position_y