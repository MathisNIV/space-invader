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
        self.taille = self.x1 - self.x0
        
    def deplacement(self):
        
        sens = 2

        while self.x0 <= 400 : # 400 = taille fenetre
            while self.x0 >= 0 :
                self.x0 = self.x0 + sens * self.dx
                if self.x1 <= 0:
                    print( 'oK2')
            if self.x0 >= 400:
                print( 'oK1')
            self.x0 = self.x0 + sens * self.dx
        sens = -1

        return 
    
    def pvAlien(self):
        self.pv = -1
        return self.pv
    
    
a = Alien()
a.deplacement()