"""
Auteur : Rodolphe Lajugie
    
Date de création : 14 décembre 2021
"""
    
class Vaisseau():
    
    def __init__(self):
        self.taille_x = 100
        self.taille_y = 30
        self.max_vie = 90
        self.vie = 90
        self.position_x = 540
        self.position_y = 700
        self.vitesse = 5
        
    def get_taille(self):
        return [self.taille_x,self.taille_y]

      
    def get_position(self):
        "fonction get qui permet d'initialiser le vaisseau en bas et au milieu de la fenêtre"
        return [self.position_x , self.position_y]
    
    def get_vie(self):
        return self.vie
    
    def deplacer_droite(self):
        "Permet au vaisseau de se déplacer de sa vitesse si celui-ci n'est pas au bout de la fenêtre"
        self.position_x += 10
        return self.position_x
    
    def deplacer_gauche(self):
        "Permet au vaisseau de se déplacer de sa vitesse si celui-ci n'est pas au début de la fenêtre"
        self.position_x -= 10
        return self.position_x
    
    def perdre_vie(self):
        """
        rajouter différents dégats en paramètre si besoin
        """
        if self.vie > 0:
            self.vie -= 30
        else:
            print("impossible, mort")
        return self.vie

