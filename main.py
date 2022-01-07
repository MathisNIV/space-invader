# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:38:01 2021

@author: mathis Niveau
"""

import tkinter as tk
import classVaisseau as cv
import classAlien as ca
import projectile as proj



'''ces deux fonctions recupèrent un objet de la classe vaisseau et l'initialisent dans la canvas'''
def crea_vaisseau():
    ship = cv.Vaisseau()
    return ship

def spawn_vaisseau(ship,width,height):
    taille = ship.get_taille()
    vaisseau = canvas.create_rectangle(width/2 - taille[0]/2, height-taille[1], width/2 + taille[0]/2, height, fill = "pink" )
    return vaisseau

'''fonction pour les aliens'''
def spawn_alien(alien,nombre_alien,width,height):
    taille = ca.get_taille()
    alien = canvas.create_rectangle(width/3 - taille[0]/2, height-taille[1], width/2 + taille[0]/2, height, fill = "blue" )
    return alien
        

def crea_alien():
    alien = ca.Alien()
    return alien

def spawn_a(alien,marge_gauche,marge_haute):
    taille  = alien.get_taille()
    aliend = canvas.create_rectangle(marge_gauche,marge_haute,marge_gauche+taille[0], marge_haute + taille[1])
    return aliend

def crea_projectile():
    tir = proj.Projectile(540,700)
    return tir
def spawn_p(tir):
    taille = tir.get_taille()
    projectile = canvas.create_rectangle(width/2 - taille[0]/2 , height-taille[1]-cv.Vaisseau().get_taille()[1], width/2 + taille[0]/2 , height-cv.Vaisseau().get_taille()[1], fill = "black" )
    if True:
        root.after(15,canvas.move(projectile,0,-20))
        #a finir
    return projectile

'''fonction detection touche clavier qui apelle une focntion de mouvement du vaisseau'''
def mvmt_vaisseau_droite(event,vaisseau):
    canvas.move(vaisseau,10,0)
def mvmt_vaisseau_gauche(event,vaisseau):
    canvas.move(vaisseau,-10,0)
def mvmt_vaisseau_tire():
    print('espace')



def projectile():
    spawn_p(crea_projectile())
    mvmt_vaisseau_tire()


    
'''variables'''
#taille écran
width = 1080
height = 720
nb_alien=11
esp_tot_alien=width-2*20-nb_alien*crea_alien().get_taille()[0]
esp_par_alien=int(esp_tot_alien/nb_alien)




'''Création de la fenerte tkinter'''
root = tk.Tk()
root.title("Space Invader")


frame1 = tk.Frame(root)
frame1.pack(side = 'left')

frame2 = tk.Frame(root)
frame2.pack(side = 'right')

canvas = tk.Canvas(frame1, width = width, height = height, bg="ivory")
objvaisseau = spawn_vaisseau(crea_vaisseau(),width,height)
esp=0
for i in range(nb_alien):
    objalien = spawn_a(crea_alien(), 20+esp, 20)
    esp+=esp_par_alien+ca.Alien().get_taille()[0]
    if i == 0:
        x1=20
        y1=20
    if i == nb_alien-1:
        x2=x1+esp-esp_par_alien
        y2=20+ca.Alien().get_taille()[1]

objvaisseau = spawn_vaisseau(crea_vaisseau(),width,height)
rec = canvas.create_rectangle(x1,y1,x2,y2)
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
root.bind("<space>", lambda _ : projectile())

root.mainloop()