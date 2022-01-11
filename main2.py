# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:17:28 2022

@author: mathi
"""

import tkinter as tk
import classVaisseau as cv 
import classAlien as ca
import classProjectile as proj
import block as bl
from PIL import Image, ImageTk


'''ces deux fonctions recupèrent un objet de la classe vaisseau et l'initialisent dans la canvas'''
def crea_vaisseau():
    ship = cv.Vaisseau()
    return ship

def spawn_v(ship,width,height):
    taille = ship.get_taille()
    vaisseau = canvas.create_rectangle(width/2 - taille[0]/2, height-taille[1], width/2 + taille[0]/2, height, fill = "pink" )
    return vaisseau

'''ces deux fonctions recupèrent un objet de la class alien et l'initialisent dans la canvas'''
def crea_alien():
    alien = ca.Alien()
    return alien

def spawn_a(alien,marge_gauche,marge_haute):
    taille  = alien.get_taille()
    aliend = canvas.create_rectangle(marge_gauche,marge_haute,marge_gauche+taille[0], marge_haute + taille[1])
    return aliend


def crea_block():
    block = bl.Block(540, 600)
    return block

def spawn_b(block):
    taille = block.get_taille()
    position = block.get_position()
    blockd = canvas.create_rectangle(position[0], position[1], position[0] + taille [0], position[1] + taille[1])
    return blockd


'''placement de plusieurs alien dans la canva'''

def invasion(esp):
    for i in range(nb_alien):
        objalien = spawn_a(alien, 20+esp, 20)
        esp+=esp_par_alien+ca.Alien().get_taille()[0]
        if i == 0:
            x1=20
            y1=20
        if i == nb_alien-1:
            x2=x1+esp-esp_par_alien
            y2=20+ca.Alien().get_taille()[1]
    return x1,y1,x2,y2


'''ces deux fonctions recupèrent un objet de la classe projectile et l'initialisent dans la canvas'''
def crea_projectile(): 
    tir = proj.Projectile(0,0,0,0)
    return tir
def spawn_p(tir):
    taille = tir.get_taille()
    tir.position_x1 = width/2 - taille[0]/2
    tir.position_y1 = height-taille[1]-cv.Vaisseau().get_taille()[1]
    tir.position_x2 = width/2 + taille[0]/2
    tir.position_y2 =height-cv.Vaisseau().get_taille()[1]
    projectiled = canvas.create_rectangle(tir.position_x1, tir.position_y1, tir.position_x2, tir.position_y2, fill = "black" )
    return projectiled

'''gère le mouvement du projectile une fois qu'on a appuyé sur la touche espace'''
def fire(projectile,projectiled,ship):
    if projectile.get_position()[1]>0:
        canvas.coords(projectiled,photo-2,projectile.get_position()[1],photo+2,projectile.get_position()[3])
        projectile.deplacement()
        root.after(50,fire,projectile,projectiled,ship,photo)
    


'''fonction detection touche clavier qui apelle une focntion de mouvement du vaisseau'''
def mvmt_vaisseau_droite(event,vaisseau,ship):
    canvas.move(vaisseau,10,0)
    ship.deplacer_droite()
    
def mvmt_vaisseau_gauche(event,vaisseau,ship):
    canvas.move(vaisseau,-10,0)
    ship.deplacer_gauche()
    

'''variables'''
#élements
ship = crea_vaisseau()
alien = crea_alien() 
projectile = crea_projectile()
block = crea_block()

#taille écran
width = 1080
height = 720

nb_alien = 11
esp_tot_alien = width-2 * 20-nb_alien * crea_alien().get_taille()[0]
esp_par_alien = int(esp_tot_alien/nb_alien)
esp = 0


nb_block = 4
esp_tot_block = width-2 * 20-nb_alien * crea_block().get_taille()[0]
esp_par_block = int(esp_tot_block/nb_block)



'''fenètre tkinter et main programme'''
root = tk.Tk()
root.title('Projet Space Invader')

frame1 = tk.Frame(root)
frame1.pack(side = 'left')

'''importation des photos a utiliser dans le programme'''
backImg=Image.open("imges/bg3.jpeg")

bckPhoto=ImageTk.PhotoImage(backImg,master=frame1)
frame2 = tk.Frame(root)
frame2.pack(side = 'right')

canvas = tk.Canvas(frame1, width = width, height = height, bg="ivory")
background=canvas.create_image(540,360,image=bckPhoto)

objblock = spawn_b(block)

objvaisseau = spawn_v(ship,width,height)
rec = canvas.create_rectangle(invasion(esp))

canvas.pack()

root.bind("<Right>",lambda e : mvmt_vaisseau_droite(e, objvaisseau, ship))
root.bind("<Left>", lambda e : mvmt_vaisseau_gauche(e, objvaisseau, ship))
root.bind("<space>", lambda _ : fire(projectile,spawn_p(projectile),ship,photo))

root.mainloop()
