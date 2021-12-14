#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:38:17 2021

@author: maximilienremillieux
"""

class Alien():
    def __init__(self):
        self.pv = 5
        self.x0 = 0
        self.y0 = 0 
        self.x1 = self.x0 + 20
        self.y1 = self.y0 + 20
        self.dx = 20
        self.dy = 20
        self.taille_x = self.x1 - self.x0
        self.taille_y = self.y1 - self.y0
        
    def deplacement(self):
        
        sens = 1
        
        while self.y0 < 720:
            while self.x1 < 400 : # 400 = taille fenetre
                self.x1 = self.x1 + sens * self.dx
                if self.x1 >= 400:

            while self.x1 > 0 :
                self.x1 = self.x1 - sens * self.dx
            if self.x1 == 0:

        return 
    
    def perde_pvAlien(self):
        if self.pv > 0:
            self.pv = -1
        return self.pv
    
    def get_position(self):
        return [self.x0, self.y0]
    
    def get_taille(self):
        return [self.taille_x, self.taille_y]
    
    def get_pvAlien(self):
        return self.pv
    
    
a = Alien()
a.deplacement()