#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:38:17 2021

@author: maximilienremillieux
"""
import time as t

class Alien():
    """
    classe régissant le fonctionnement de chaque alien
    """
    def __init__(self,pv,taillex, tailley):
        self.taille_x = taillex
        self.taille_y = tailley
        self.pv =pv
        self.x0 = 0
        self.y0 = 0 
        self.x1 = self.x0 + 20
        self.y1 = self.y0 + 20
        self.dx = 20
        self.dy = 20
        self.taille = self.x1 - self.x0

    def get_taille(self):
        """
        getteur qui permet d'accéder à la taille de chaque alien

        Returns:
            [liste]: [description]
        """
        return [self.taille_x,self.taille_y]

    # def deplacement(self):
    #     if 
    
    def pvAlien(self):
        self.pv -= 1
        return self.pv
    
    def getVie(self):
        return self.pv
