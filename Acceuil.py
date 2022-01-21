#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:44:00 2022

@author: maximilienremillieux
"""

import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()
root.title('Projet Space Invader')

width = 540
height = 360

backImg=Image.open("imges/background.jpeg")
vaisseauImg=Image.open("imges/vaisseau.png")

frame1 = tk.Frame(root)
frame1.pack()

label1 = tk.Label(frame1, text="BIENVENUE DANS SPACE INVADER",fg ='black')
label1.pack()

bckPhoto=ImageTk.PhotoImage(backImg,master=frame1)
vaisseauPhoto=ImageTk.PhotoImage(vaisseauImg,master=frame1)

canvas = tk.Canvas(frame1, width = width , height = height, bg="ivory")
canvas.pack()

background=canvas.create_image(270,180,image=bckPhoto)
vaisseau=canvas.create_image(270,50,image=vaisseauPhoto)


label2 = tk.Label(frame1, text="LANCER UNE PARTIE",fg ='black')
label2.pack()

def lancer_une_partie():
    import main2 as main2
    return main2

boutton1 = tk.Button(frame1, text = "JOUER",fg ='white',bg ='black', relief = 'raised', command=lancer_une_partie)
boutton1.pack()

boutton2 = tk.Button(frame1, text = "Quitter",fg ='white',bg ='black', relief = 'raised', command=root.destroy)
boutton2.pack()

root.mainloop()