#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:38:17 2021

@author: maximilienremillieux
"""

class Alien():
    def __init__(self):
        self.taille_x = 100
        self.taille_y = 30
        self.pv = 5
        self.x0 = 0
        self.y0 = 0 
        self.x1 = self.x0 + 20
        self.y1 = self.y0 + 20
        self.dx = 20
        self.dy = 20
        self.taille = self.x1 - self.x0
        
    def get_taille(self):
        return [self.taille_x,self.taille_y]
        
    def deplacement(self):
        sens = 1
        ar=0
        while self.y0 < 720:
            while self.x1 < 400 : # 400 = taille fenetre
                self.x1 = self.x1 + sens * self.dx
                if self.x1 >= 400:
                    print( 'OK')
                    print('a droite', self.x1)
            while self.x1 > 0 :
                
                self.x1 = self.x1 - sens * self.dx
            print('a gauche', self.x1)
            if self.x1 == 0:
                ar=1
                self.y0 += self.dy
                print('ok')
                print('y0',self.y0)
        return 
    
    def pvAlien(self):
        self.pv = -1
        return self.pv
    
    
a = Alien()
a.deplacement()