"""
Auteur : Rodolphe Lajugie
    
Date de création : 14 décembre 2021
"""


class Block():
    """
    class régissant les block de protection du joueur
    
    """
    
    def __init__(self,pX,pY):
        """
        Fonction d'initialisation de la classe block

        Args:
            pX (int): coordonnées x (abscisse) du block
            pY (int): coordonnées y (ordonnée) du block
        """
        self.vie=3
        self.taille_x=30
        self.taille_y=30
        self.position_x=pX
        self.position_y=pY
        
    def perdre_vie(self):
        """
        fonction permettant de détruire un block si celui-ci est touché par un projectile  

        Returns:
            self.vie [int]: retourne 0 si la fonction est appelée 
        """
        self.vie=0
        return self.vie
    
    def get_position(self):
        
        """
        getteur qui retourne une liste contenant les coordonnées du block

        Returns:
        liste contenant:
            self.position_x [int]: abscisse du block
            self.position_y [int]: ordonnée du bllock
        """
        return [self.position_x,self.position_y]
    
    def get_taille(self):
        """
        getteur qui retourne une liste contenant la taille en x et en y du block

        Returns:
        liste contenant:
            self.taille_x [int]: taille en x du block
            self.taille_y [int]: taille en y du block
        """
        return [self.taille_x,self.taille_y]