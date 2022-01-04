# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:38:01 2021

@author: mathis Niveau
"""

import tkinter as tk
import classVaisseau as cv
import classAlien as ca




'''ces deux fonctions recupèrent un objet de la classe vaisseau et l'initialisent dans la canvas'''
def crea_vaisseau():
    ship = cv.Vaisseau()
    return ship

def spawn_v(ship,width,height):
    taille = ship.get_taille()
    vaisseau = canvas.create_rectangle(width/2 - taille[0]/2, height-taille[1], width/2 + taille[0]/2, height, fill = "pink" )
    return vaisseau


def crea_alien():
    alien = ca.Alien()
    return alien

def spawn_a(alien):
    taille  = alien.get_taille()
    aliend = canvas.create_rectangle(20,20,20+taille[0],20 + taille[1])
    return aliend




'''fonction detection touche clavier qui apelle une focntion de mouvement du vaisseau'''
def mvmt_vaisseau_droite(event,vaisseau):
    canvas.move(vaisseau,10,0)
def mvmt_vaisseau_gauche(event,vaisseau):
    canvas.move(vaisseau,-10,0)
def mvmt_vaisseau_tire(event):
    print('espace')



    
'''variables'''
#taille écran
width = 1080
height = 720





'''Création de la fenerte tkinter'''
root = tk.Tk()
root.title("Space Invader")



frame1 = tk.Frame(root)
frame1.pack(side = 'left')

frame2 = tk.Frame(root)
frame2.pack(side = 'right')

canvas = tk.Canvas(frame1, width = width, height = height, bg="ivory")
objvaisseau = spawn_v(crea_vaisseau(),width,height)
canvas.pack()

score_label = tk.Label(frame2, text = "score : 100")
score_label.pack()


vie_label = tk.Label(frame2, text = "vie = 3")
vie_label.pack()


ng = tk.Button(frame2, text = "New Game", command = lambda : print("oui"))
ng.pack()


quitter = tk.Button(frame2, text = "Quit", command = lambda : root.destroy())
quitter.pack()

root.bind("<Right>",lambda e : mvmt_vaisseau_droite(e, objvaisseau))
root.bind("<Left>", lambda e : mvmt_vaisseau_gauche(e, objvaisseau))
root.bind("<space>",mvmt_vaisseau_tire)

root.mainloop()
