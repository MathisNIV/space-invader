# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:04:47 2021

@author: mathi
"""

import tkinter as tk

class Mafenetre(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width=1080, height=720, bg="ivory")
        canvas.pack(side = "bottom")
        score = tk.Label(self, text="score : 100")
        score.pack(side = "left")
        vie = tk.Label(self,text="Lives : 3")
        vie.pack(side = "right")
        reset = tk.Button(self, text = "New Game", command = Mafenetre.destroy)
        reset.pack(side = "right")
        quitter = tk.Button(self, text = "Quit" , command = Mafenetre.destroy)
        quitter.pack(side = "right")
        
    
    
    
    
    
root = tk.Tk()
root.title('space invader')
Mafenetre(root).pack()
root.mainloop()

        