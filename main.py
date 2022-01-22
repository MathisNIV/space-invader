# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:17:28 2022

@author: mathi
"""


from curses import window
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
    """

    Args:
        ship (objet): objet de la classe vaisseau
        width (int): largeur de laaa fenêtre
        height (int): hauteur de la fenêtre

    Returns:
        [image]: image du vaissseau sur le canvas
    """
    vaisseauImg=Image.open('imges/vaisseau.png')
    vaisseauimg=vaisseauImg.resize((150,70))
    vaisseauPhoto=ImageTk.PhotoImage(vaisseauimg,master=frame1)
    
    taille = ship.get_taille()
    vaisseau = canvas.create_image(width/2+50 - taille[0]/2, height-taille[1]-20, image=vaisseauPhoto)
    canvas.sdfgsdfsdfdgf = vaisseauPhoto

    return vaisseau

'''ces deux fonctions recupèrent un objet de la class alien et l'initialisent dans la canvas'''
def crea_alien(pv, taillex, tailley):
    alien = ca.Alien(pv, taillex,tailley)
    return alien

def spawn_a(alien,marge_gauche,marge_haute, color): 
    #alienimage=Image.open('imges/alienfin.png')
    #alienIMG=alienimage.resize((30,30))
    #alienPhoto = ImageTk.PhotoImage(alienIMG)
    taille  = alien.get_taille()
    aliend = canvas.create_rectangle(marge_gauche,marge_haute,marge_gauche+taille[0], marge_haute + taille[1],fill = color)
    #marge_gauche + taille[0]/2, marge_haute + taille[1]/2, image=alienPhoto (parametre de la fonction create_image si nous avions eu le temps de l'appliquer proprerment sur les aliens )
    #canvas.jesaispasquoiecrire = alienPhoto
    return aliend

def lancer_une_partie2():
    root.destroy()
    import Acceuil as acc
    return acc


def apocalypse(rep,dx,k):
    """
    fonction qui régit le déplacement des aliens, ils descendent s'ils ont effectués un allé retour

    Args:
        rep (liste): contient les coordonnées de chaque alien
        dx (int): correspond au pas de chaque alien
        k (int): correspond au nb d'aller-retour de chaque alien
    """
    #condition droite
    j=0
    if (rep[-1][0][2] >= 1080)  or (rep[0][0][0] <= 0):
        dx = dx* (-1)
        k += 1 
    for i in rep:  
        canvas.move(i[1],dx,0)
        rep[j][0][0] += dx
        rep[j][0][2] += dx
        j+=1
    if k%2 == 0 and k!=0:
        for h in rep:  
            canvas.move(h[1],0,dx)
            h[0][1] += dx
            h[0][3] += dx 
            k=0
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
        btngame=tk.Button(window, text='réessayer', command=lancer_une_partie2)
        btngame.pack()    
      

    
# def crea_block():
#     block = bl.Block(540, 600)
#     return block

# def spawn_b(block):
#     taille = block.get_taille()
#     position = block.get_position()
#     blockd = canvas.create_rectangle(position[0], position[1], position[0] + taille [0], position[1] + taille[1])
#     return blockd

def op():
    ap=open('apropos.txt')
    text=ap.readlines()
    window=tk.Tk()
    window.title('A propos')
    window.geometry(('1600x300'))
    Label1=tk.Label(window, text=text[0], font=('Calibri', 16))
    Label1.pack(expand='yes')
    ap.close()

'''placement de plusieurs alien dans la canva'''

def invasion(esp, color, esp_par,alien,nalien):
    """
    fonction qui permet de faire apparaitre plusieurs aliens

    Args:
        esp (int): espace pris par tous les alien
        color (str): couleur des aliens
        esp_par (int): espace par alien
        alien (objet): objet de la classe alien
        nalien (int): nombre d'alien

    Returns:
        [list]: contient les coordonnées de chaque alien
    """
    
    pos_al = []
    for i in range(nalien):
        obj_alien = spawn_a(alien, 5+esp, 20,color)
        esp+=esp_par
        pos_al.append([canvas.coords(obj_alien),obj_alien])
    return pos_al


'''ces deux fonctions recupèrent un objet de la classe projectile et l'initialisent dans la canvas'''
def crea_projectile(): 
    tir = proj.Projectile(0,0,0,0)
    return tir

def spawn_p(tir,ship):
    """
    fonction qui permet d'afficher le projectile

    Args:
        tir (objet): objet de la classe projectile
        ship (objet): objet de la classe vaisseau

    Returns:
        [image]: un rectangle créé sur le canvas
    """
    taille = tir.get_taille()
    tir.position_x1 = ship.get_position()[0]-taille[0]/2
    tir.position_y1 = ship.get_position()[1]-taille[1]-50
    tir.position_x2 = ship.get_position()[0]+taille[0]/2
    tir.position_y2 = ship.get_position()[1]-50
    projectiled = canvas.create_rectangle(tir.position_x1, tir.position_y1, tir.position_x2, tir.position_y2, fill = "green" )
    return projectiled 


def fire(projectile,projectiled,ship):
    """
    gère le mouvement du projectile une fois qu'on a appuyé sur la touche espace
    """
    
    if canvas.coords(projectiled)[1]>=0:
        canvas.move(projectiled,0,-10)
        projectile.get_position()[1] -= 10
        extermination(projectiled)
        root.after(10,fire,projectile,projectiled,ship)
    else:
        canvas.delete(projectiled)
        
#def fire2(projectile,projectiled,ship):
#    """
#    gère le mouvement du projectile une fois qu'on a appuyé sur la touche espace
#    """
#    
#    if canvas.coords(projectiled)[1]>=0:
#        canvas.move(projectiled,0,-10)
#        projectile.get_position()[1] -= 10
#        extermination(projectiled)
#        root.after(10,fire,projectile,projectiled,ship)
#    else:
#        canvas.delete(projectiled)

        
def extermination(projectiled):
    """
    fonction qui permettra de détruire les aliens et le projectile si ceux si se rencontrent

    Args:
        projectiled (objet): objet de la classe projectile
        pos_al (liste): liste contenant les coordonnées des aliens 
    """
    global score, var, pos_al , pos_al2
    for i in range(len(pos_al)):        
        if canvas.coords(pos_al[i][1])[3] == canvas.coords(projectiled)[1] and canvas.coords(pos_al[i][1])[0]<canvas.coords(projectiled)[0]<canvas.coords(pos_al[i][1])[2]:
            canvas.delete(pos_al[i][1])
            pos_al.pop(i)
            canvas.delete(projectiled)
            score+=10
            var.set(score)
    
    for i in range(len(pos_al2)):        
        if canvas.coords(pos_al2[i][1])[3] == canvas.coords(projectiled)[1] and canvas.coords(pos_al2[i][1])[0]<canvas.coords(projectiled)[0]<canvas.coords(pos_al2[i][1])[2]:
            alien2.pvAlien()
            print('vie de lalien', alien2.pvAlien())
            score +=10
            var.set(score)
            if alien2.getVie() == 0:
                canvas.delete(pos_al2[i][1])
                pos_al2.pop(i)
                canvas.delete(projectiled)
                score+=20
                var.set(score)
            
    if len(pos_al) == 0 and len(pos_al2)==0:
        root.destroy()
        window=tk.Tk()
        window.title('Partie Gagnée')
        txt= tk.Label(window, text="Vous avez survécu à l'invasion")
        txt.pack(expand='yes')
        Lscore1 = tk.Label(window,text = 'Score : ')
        Lscore1.pack()
        var = tk.StringVar()
        var.set(score)
        Lscore2 = tk.Label(window,textvariable = var)
        Lscore2.pack()
        btquitter=tk.Button(window, text='Quitter', command = window.destroy)
        btquitter.pack(expand='yes')
        

 
''''''
def mvmt_vaisseau_droite(event,vaisseau,ship):
    
    """
    fonction detection touche clavier qui apelle une focntion de mouvement du vaisseau
    """
    
    if canvas.coords(vaisseau)[0]<1020:
        canvas.move(vaisseau,10,0)
        ship.deplacer_droite()
    
def mvmt_vaisseau_gauche(event,vaisseau,ship):
    if canvas.coords(vaisseau)[0]>50:
        canvas.move(vaisseau,-10,0)
        ship.deplacer_gauche()
    

'''variables élements'''
ship = crea_vaisseau()
alien = crea_alien(1,30,30) 
projectile = crea_projectile()
alien2=crea_alien(2, 20,20)

#blockd = crea_block()
# block = crea_block()

'''taille de la fenêtre'''
width = 1080
height = 720 
taille = ship.get_taille()

nb_alien = 10
nb_alien2 = 1
esp_tot_alien = width-2 * 20-nb_alien * alien.get_taille()[0]
esp_tot_alien2 = width-2 * 20-nb_alien2 * alien2.get_taille()[0]

esp_par_alien = int(esp_tot_alien/nb_alien)+20
esp_par_alien2 = int(esp_tot_alien2/nb_alien2)-20
esp = 0
esp2=0

'''initialisation mouvement alien'''
dx1 = 10
dx2 = 12
k = 0
score = 0

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

Lscore = tk.Label(frame2,text = 'score : ')
Lscore.pack()
var = tk.StringVar()
L2score = tk.Label(frame2,textvariable = var)
L2score.pack()

ng = tk.Button(frame2, text = 'Nouvelle Partie', command = lancer_une_partie2)
ng.pack()

quitter = tk.Button(frame2, text = 'Quitter', command = root.destroy)
quitter.pack()


''' importation de de l'image du vaisseau'''
vaisseauImg=Image.open('imges/vaisseau.png')
vaisseauimg=vaisseauImg.resize((100,30))
vaisseauPhoto=ImageTk.PhotoImage(vaisseauimg,master=frame1)



canvas = tk.Canvas(frame1, width = width, height = height, bg="ivory")
vaisImg=canvas.create_image(width/2+50 - taille[0]/2, height-taille[1], image=vaisseauPhoto)
background=canvas.create_image(540,360,image=bckPhoto)

#objblock = spawn_b(blockd)
# objblock = spawn_b(block)


objvaisseau = spawn_v(ship,width,height)
pos_al = invasion(esp, 'white',esp_par_alien, alien, nb_alien)
apocalypse(pos_al,dx1,k)
pos_al2=invasion(esp2, 'red',esp_par_alien2,alien2, nb_alien2)
apocalypse(pos_al2, dx2, k)
canvas.pack()

root.bind("<Right>",lambda e : mvmt_vaisseau_droite(e, objvaisseau, ship))
root.bind("<Left>", lambda e : mvmt_vaisseau_gauche(e, objvaisseau, ship))
root.bind("<space>", lambda _ : fire(projectile,spawn_p(projectile,ship),ship))

'''création du menu'''
menu=tk.Menu(root)


file=tk.Menu(menu, tearoff='0')
file.add_command(label='Nouveau', command=lancer_une_partie2)
file.add_command(label='quitter', command=root.destroy)
file.add_command(label = 'à propos', command = op)
menu.add_cascade(label='fichier', menu=file)

'''configurer notre fenêtre'''
root.config(menu=menu)
root.mainloop()
