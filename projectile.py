"""
Auteur: Rodolphe Lajugie
    
date de création: 20 décembre 2021
"""
    
class Projectile():
    
    def __init__(self,pX,pY):
        self.vitesse=40
        self.puissance=30
        self.position_x=pX
        self.position_y=pY
        self.taille_x=3
        self.taille_y=3
    
    def get_taille(self):
        return [self.taille_x, self.taille_y]
        
    def bolPos(self):
        bol=False
        if (self.position_y) >= 720 :
            bol = True
        return bol
    
    def getPos(self):
        return self.position_y
    
    def deplacement(self):
        blo=False
        while blo != True:
            b = Projectile(self.position_x, self.position_y)
            blo = b.bolPos()
            self.position_y -= self.vitesse
            blo = b.bolPos()
            print(blo, '\npos y ', self.position_y)
        
        return self.position_y

        #le détruire
