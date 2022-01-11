"""
Auteur: Rodolphe Lajugie
    
date de création: 20 décembre 2021
"""
    
class Projectile():
    """
    classe régissant le fonctionnement de tous les projectiles
    """
    def __init__(self,dx1,dy1,dx2,dy2):
        """
        Args:
            dx1 ([int]): abscisse du point en haut a gauche du projectile
            dy1 ([int]): ordonnée du point en haut à gauche du projectile 
            dx2 ([int]): abscisse du point en haut a gauche du projectile
            dy2 ([int]): ordonnée du point en haut à gauche du projectile
        """
        self.dy = 0
        self.position_x1=dx1
        self.position_y1=dy1
        self.position_x2=dx2
        self.position_y2=dy2
        self.taille_x=3
        self.taille_y=20
    
    def get_taille(self):
        """
        getteur qui permet d'obtenir la taille en x et y du projectile

        Returns:
            [liste]: contenant: 
                - taille en x et taille en y
        """
        return [self.taille_x, self.taille_y]
    
    def get_position(self):
        """
        getteur permettant d'obtenir la position en x et en y des deux points définis dans la fonction __init__ 

        Returns:
            [liste]: contenant:
                - coordonnée du point du point en haut à gauche (x1,y1)
                - coordonnée du point du point en bas à droite (x2,y2)
        """
        return [self.position_x1,self.position_y1,self.position_x2,self.position_y2]

    
    def deplacement(self):
        self.position_y1 = self.position_y1 - self.dy
        self.position_y2 = self.position_y2 - self.dy
        return [self.position_x1,self.position_y1,self.position_x2,self.position_y2]


