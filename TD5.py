from tkinter import *
from tkinter import ttk
import random

total_cercles=6

root = Tk()
root.geometry("400x400")
window = Frame(root)
window.grid()


## Construction de la cible

can = Canvas(root, width=400,height=400,bg='red')
can.grid()


for i in range (total_cercles):
    circle_color = "ivory"
    text_color = "red"
    if i == total_cercles -2:
        circle_color ="red"
        text_color='ivory'
    oval = can.create_oval(30*(i+1), 30*(i+1), 400 - 30*(i+1), 400 -30*(i+1), outline='red', fill=circle_color)
    text = can.create_text(200,30*(i+1) + 15,text=i+1 , font=('Times','20','bold'),fill= text_color)



ligne1 = can.create_line(0,200,400,200, fill='red')
ligne2= can.create_line(200,0,200,400, fill='red')


## Action si "f" est pressé

Nb_tirs = 0  # variable globale
total = 0

def score(a,b):
    global total
    total = 0
    x = a + 15/2 -200
    y = b + 15/2 -200
    R = (370 - 30)/2
    for i in range (6):
        R = (370 - 30 )/2 - 30*i
        if x*x +y*y <= R*R:
            total += 1
    return total
# points basés sur le centre de l'impact

def feu():
    global Nb_tirs
    global total
    if Nb_tirs>=5:
        Feu["state"]= DISABLED
        return None

    a = random.random()*400
    b = random.random()*400
    oval = can.create_oval(a, b, a+15,b+15, fill='black', outline = "black")
    total += score(a,b)
    Nb_tirs +=1
    Score = ttk.Label(window, text=f"Score de {total} points").grid(row = 1, column = 302)
    return total
root.bind("f", lambda x: feu())

## Boutons de tir




def tir():
    global Nb_tirs
    global total
    for i in range(5 - Nb_tirs):
        a = random.random()*400
        b = random.random()*400
        oval = can.create_oval(a, b, a+15,b+15, fill='black', outline = "black")
        total += score(a,b)
        Nb_tirs = 5

    Score = ttk.Label(window, text=f"Score de {total} points").grid(row = 1, column = 302)
    Feu["state"]= DISABLED
    return total

Feu = ttk.Button(window, text="Feu!", command = tir)
Feu.grid(row = 1, column = 300)
Quitter = ttk.Button(window, text="Quitter", command=root.destroy).grid(row = 1, column = 0)
# je n'arrive pas à placer en bas les boutons



root.mainloop()
