"""
Auteur : Rodolphe Lajugie
    
Date de création : 14 décembre 2021
"""
    
class Vaisseau():
    """
    classe joueur
    """
    def __init__(self):
        self.taille_x = 100
        self.taille_y = 30
        self.max_vie = 90
        self.vie = 90
        self.position_x = 540
        self.position_y = 700
        self.vitesse = 5
        
    def get_taille(self):
        """
        getteur qui retourne la taille du vaisseau

        Returns:
            [liste]: retourne la taille en x [int] et en y [int]
        """
        return [self.taille_x,self.taille_y]

      
    def get_position(self):
        """
        getteur qui permet d'initialiser le vaisseau en bas et au milieu de la fenêtre

        Returns:
            [liste]: retourne les coordonnées x [int] et y [int]
        """
        return [self.position_x , self.position_y]
    
    def get_vie(self):
        return self.vie
    
    def deplacer_droite(self):
        
        '''
        Permet au vaisseau de se déplacer de sa vitesse si celui-ci n'est pas au bout de la fenêtre

        Returns:
            self.position_x [int]: retourne l'abscisse du vaisseau après le déplacement
        '''
        self.position_x += 10
        return self.position_x
    
    def deplacer_gauche(self):
        '''
        Permet au vaisseau de se déplacer de sa vitesse si celui-ci n'est pas au bout de la fenêtre
        Returns:
        self.position_x [int]: retourne l'abscisse du vaisseau après le déplacement
        '''
        self.position_x -= 10
        return self.position_x
    
    def perdre_vie(self):
        """
        Fonction permettant de rajouter différents dégats 

        Returns:
            self.vie [int]: retourne la santé du joueur, si celle-ci est nulle, la partie est terminée
        """
        
        if self.vie > 0:
            self.vie -= 30
        else:
            print("impossible, mort")
        return self.vie

