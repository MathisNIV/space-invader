#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:38:17 2021

@author: maximilienremillieux
"""
import time as t

class Alien():
    def __init__(self):
        self.taille_x = 30
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
                t.sleep(0.5)
                self.x1 = self.x1 + sens * self.dx
            while self.x1 > 0 :
                t.sleep(0.5)    
                self.x1 = self.x1 - sens * self.dx
            if self.x1 == 0:
                ar+=1
                self.y0 += 9*self.dy
        return ar 
    
    def pvAlien(self):
        self.pv = -1
        return self.pv
    
