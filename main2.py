# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:17:28 2022

@author: mathi
"""

import tkinter as tk
from turtle import color
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
    
    vaisseauImg=Image.open('imges/vaisseau.png')
    vaisseauimg=vaisseauImg.resize((150,70))
    vaisseauPhoto=ImageTk.PhotoImage(vaisseauimg,master=frame1)
    
    taille = ship.get_taille()
    vaisseau = canvas.create_image(width/2+50 - taille[0]/2, height-taille[1]-20, image=vaisseauPhoto)
    canvas.sdfgsdfsdfdgf = vaisseauPhoto

    return vaisseau

'''ces deux fonctions recupèrent un objet de la class alien et l'initialisent dans la canvas'''
def crea_alien():
    alien = ca.Alien()
    return alien

def spawn_a(alien,marge_gauche,marge_haute): 
    #alienimage=Image.open('imges/alienfin.png')
    #alienIMG=alienimage.resize((30,30))
    #alienPhoto = ImageTk.PhotoImage(alienIMG)
    
    
    taille  = alien.get_taille()
    aliend = canvas.create_rectangle(marge_gauche,marge_haute,marge_gauche+taille[0], marge_haute + taille[1],fill = "white")
    #print(canvas.coords(aliend))
    #marge_gauche + taille[0]/2, marge_haute + taille[1]/2, image=alienPhoto
    #canvas.jesaispasquoiecrire = alienPhoto
    return aliend

def apocalypse(rep,dx,k):
    #condition droite
        j=0
        if (rep[-1][0][2] >= 1080)  or (rep[0][0][0] <= 0):
            dx = dx* (-1)
            k += 1 
        for i in rep:  
            #print(i)
            canvas.move(i[1],dx,0)
            rep[j][0][0] += dx
            rep[j][0][2] += dx
            j+=1
        if k%2 == 0 and k!=0:
            for h in rep:  
                canvas.move(h[1],0,400)
                h[0][1] += 400
                h[0][3] += 400
                k=0
    # if rep[-1][0][3]
#    for val in range(nb_alien):
#        print('ok')
#        if rep[val][0][1] >= 300:
#            print('fin')
        if rep[0][0][1] <= 670:
            root.after(50,apocalypse,rep,dx,k)
        else:
            frame1.destroy()
            window=tk.Frame(root)
            window.pack()
            
            PartieFin = tk.Label(window, text='Vous avez perdu, vous êtes vraiement nul !', fg='white', bg = 'black',font=('Helvetica', 24))
            PartieFin.pack()
            btnquit=tk.Button(window, text='abandonner', command=window.destroy)
            btnquit.pack()
            btngame=tk.Button(window, text='réessayer', command='')
            btngame.pack()    
      
    
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
        obj_alien = spawn_a(alien, 5+esp, 20)
        esp+=esp_par_alien
        pos_al.append([canvas.coords(obj_alien),obj_alien])
    return pos_al


'''ces deux fonctions recupèrent un objet de la classe projectile et l'initialisent dans la canvas'''
def crea_projectile(): 
    tir = proj.Projectile(0,0,0,0)
    return tir
def spawn_p(tir,ship):
    taille = tir.get_taille()
    tir.position_x1 = ship.get_position()[0]-taille[0]/2
    tir.position_y1 = ship.get_position()[1]-taille[1]-50
    tir.position_x2 = ship.get_position()[0]+taille[0]/2
    tir.position_y2 = ship.get_position()[1]-50
    projectiled = canvas.create_rectangle(tir.position_x1, tir.position_y1, tir.position_x2, tir.position_y2, fill = "white" )
    return projectiled

'''gère le mouvement du projectile une fois qu'on a appuyé sur la touche espace'''
def fire(projectile,projectiled,ship,pos_al):
    if canvas.coords(projectiled)[1]>=0:
        canvas.move(projectiled,0,-10)
        projectile.get_position()[1] -= 10
        root.after(10,fire,projectile,projectiled,ship,pos_al)
    # for i in pos_al:
    #     if canvas.coords(pos_al[i][1]) == canvas.coords(projectiled)[1]:
    #     #score +=10
    #         canvas.delete(pos_al[i][1])
    #         canvas.delete(projectiled)
    else:
        canvas.delete(projectiled)


'''fonction detection touche clavier qui apelle une focntion de mouvement du vaisseau'''
def mvmt_vaisseau_droite(event,vaisseau,ship):
    if canvas.coords(vaisseau)[0]<1020:
        canvas.move(vaisseau,10,0)
        ship.deplacer_droite()
    
def mvmt_vaisseau_gauche(event,vaisseau,ship):
    if canvas.coords(vaisseau)[0]>50:
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
taille = ship.get_taille()

nb_alien = 11
esp_tot_alien = width-2 * 20-nb_alien * crea_alien().get_taille()[0]
esp_par_alien = int(esp_tot_alien/nb_alien)+20
esp = 0

#initialisation mouvement alien
dx = 10
k = 0

# nb_block = 4
# esp_tot_block = width-2 * 20-nb_alien * crea_block().get_taille()[0]
# esp_par_block = int(esp_tot_block/nb_block)



'''fenètre tkinter et main programme'''
root = tk.Tk()
root.title('Projet Space Invader')

frame1 = tk.Frame(root)
frame1.pack(side = 'left')

'''importation de l'image de fond '''
backImg=Image.open("imges/bg3.jpeg")

bckPhoto=ImageTk.PhotoImage(backImg,master=frame1)
frame2 = tk.Frame(root)
frame2.pack(side = 'right')

''' importation de de l'image du vaisseau'''
'''vaisseauImg=Image.open('imges/vaisseau.png')
vaisseauimg=vaisseauImg.resize((100,30))
vaisseauPhoto=ImageTk.PhotoImage(vaisseauimg,master=frame1)

vaisImg=canvas.create_image(width/2+50 - taille[0]/2, height-taille[1], image=vaisseauPhoto)
'''
canvas = tk.Canvas(frame1, width = width, height = height, bg="ivory")
background=canvas.create_image(540,360,image=bckPhoto)


# objblock = spawn_b(block)

objvaisseau = spawn_v(ship,width,height)
pos_al = invasion(esp)
apocalypse(pos_al,dx,k)
 
canvas.pack()

root.bind("<Right>",lambda e : mvmt_vaisseau_droite(e, objvaisseau, ship))
root.bind("<Left>", lambda e : mvmt_vaisseau_gauche(e, objvaisseau, ship))
root.bind("<space>", lambda _ : fire(projectile,spawn_p(projectile,ship),ship,pos_al))


root.mainloop()
