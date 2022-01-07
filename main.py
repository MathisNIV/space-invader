# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:38:01 2021

@author: mathis Niveau
"""

import tkinter as tk
import classVaisseau as cv
import classAlien as al



'''ces deux fonctions recupèrent un objet de la classe vaisseau et l'initialisent dans la canvas'''
def crea_vaisseau():
    ship = cv.Vaisseau()
    return ship

def spawn_vaisseau(ship,width,height):
    taille = ship.get_taille()
    vaisseau = canvas.create_rectangle(width/2 - taille[0]/2, height-taille[1], width/2 + taille[0]/2, height, fill = "pink" )
    return vaisseau

'''fonction pour les aliens'''
def crea_alien():
    alien = al.Alien()
    return alien
def spawn_alien(alien,nombre_alien,width,height):
    taille = al.get_taille()
    alien = canvas.create_rectangle(width/3 - taille[0]/2, height-taille[1], width/2 + taille[0]/2, height, fill = "blue" )
    return alien
        


'''fonction detection touche clavier qui apelle une focntion de mouvement du vaisseau'''
def mvmt_vaisseau_droite(event,vaisseau):
    canvas.move(vaisseau,10,0)
def mvmt_vaisseau_gauche(event,vaisseau):
    canvas.move(vaisseau,-10,0)
def mvmt_vaisseau_tire(event):
    print('espace')



    
'''variables'''
width = 1080
height = 720
nombre_alien = 5





'''Création de la fenerte tkinter'''
root = tk.Tk()
root.title("Space Invader")



frame1 = tk.Frame(root)
frame1.pack(side = 'left')

frame2 = tk.Frame(root)
frame2.pack(side = 'right')

canvas = tk.Canvas(frame1, width = width, height = height, bg="ivory")
objvaisseau = spawn_vaisseau(crea_vaisseau(),width,height)
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
