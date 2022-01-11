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
    aliend = canvas.create_rectangle(marge_gauche,marge_haute,marge_gauche+taille[0], marge_haute + taille[1],fill = "white")
    return aliend

def apocalypse(rep):
    #condition gauche
    if rep[-1][0][3]<1000:
        for i in rep:  
            canvas.move(i[1],10,0)
            rep[-1][0][3] += 10
        root.after(500,apocalypse,rep)
    elif rep[0][0][0]>10:
        for i in rep:  
            canvas.move(i[1],-10,0)
            rep[0][0][0] -= 10
        root.after(500,apocalypse,rep)
# def crea_block():
#     block = bl.Block(540, 600)
#     return block

# def spawn_b(block):
#     taille = block.get_taille()
#     position = block.get_position()
#     blockd = canvas.create_rectangle(position[0], position[1], position[0] + taille [0], position[1] + taille[1])
#     return blockd


'''placement de plusieurs alien dans la canva'''

def invasion(esp):
    pos_al = []
    for i in range(nb_alien):
        obj_alien = spawn_a(alien, 20+esp, 20)
        esp+=esp_par_alien+ca.Alien().get_taille()[0]
        pos_al.append([canvas.coords(obj_alien),obj_alien])
    print(pos_al)
    return pos_al


'''ces deux fonctions recupèrent un objet de la classe projectile et l'initialisent dans la canvas'''
def crea_projectile(): 
    tir = proj.Projectile(0,0,0,0)
    return tir
def spawn_p(tir,ship):
    taille = tir.get_taille()
    tir.position_x1 = ship.get_position()[0]-taille[0]/2
    tir.position_y1 = ship.get_position()[1]-taille[1]
    tir.position_x2 = ship.get_position()[0]+taille[0]/2
    tir.position_y2 = ship.get_position()[1]
    projectiled = canvas.create_rectangle(tir.position_x1, tir.position_y1, tir.position_x2, tir.position_y2, fill = "white" )
    return projectiled

'''gère le mouvement du projectile une fois qu'on a appuyé sur la touche espace'''
def fire(projectile,projectiled,ship):  
    if projectile.get_position()[1]>100:
        canvas.move(projectiled,0,-10)
        root.after(10,fire,projectile,projectiled,ship)
     


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
# block = crea_block()

#taille écran
width = 1080
height = 720

nb_alien = 11
esp_tot_alien = width-2 * 20-nb_alien * crea_alien().get_taille()[0]
esp_par_alien = int(esp_tot_alien/nb_alien)
esp = 0


# nb_block = 4
# esp_tot_block = width-2 * 20-nb_alien * crea_block().get_taille()[0]
# esp_par_block = int(esp_tot_block/nb_block)



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

# objblock = spawn_b(block)

objvaisseau = spawn_v(ship,width,height)

apocalypse(invasion(esp))
 
canvas.pack()

root.bind("<Right>",lambda e : mvmt_vaisseau_droite(e, objvaisseau, ship))
root.bind("<Left>", lambda e : mvmt_vaisseau_gauche(e, objvaisseau, ship))
root.bind("<space>", lambda _ : fire(projectile,spawn_p(projectile,ship),ship))

root.mainloop()
