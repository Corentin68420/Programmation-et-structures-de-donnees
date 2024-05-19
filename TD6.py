from tkinter import *
from tkinter import ttk
import numpy as np
from random import random


graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0],
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

WIDTH = 400
HEIGHT =400

root = Tk()
root.geometry("400x400")
window = Frame(root)
window.grid()
can = Canvas(root, width=400,height=400,bg='white')
can.grid()

pos = np.array([(random()*WIDTH, random()*HEIGHT)
       for i in range(len(graph))])
vit = np.array([((random()-0.5)*10, (random()-0.5)*10)
       for i in range(len(graph))])



for i in range (len(graph)):
    circle = can.create_oval(pos[i][0]-15,pos[i][1]-15,pos[i][0]+15,pos[i][1]+15,outline= "black")
    text = can.create_text(pos[i][0],pos[i][1],text= i , font=('Times','20','bold'),fill= "black")
    for j in graph[i]:
        can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1], fill="black")

##Exo 2





def move():
    F = []
    tau=0.1
    k=1
    global pos
    global vit
    for i in range(len(graph)):
        x,y = 0,0
        for j in graph[i]:
            x = x -k*abs(pos[i][0]-pos[j][0])
            y = y -k*abs(pos[i][1]-pos[j][1])
        F.append([x,y])

    for i in range(len(F)):
        for j in range(len(F[i])):
            F[i][j] = F[i][j]*tau
    vit = vit + F
    for i in range(len(vit)):
        for j in range(len(vit[i])):
            vit[i][j] = vit[i][j]*tau
    pos = pos + vit
    can.delete('all')
    for i in range (len(graph)):
        circle = can.create_oval(pos[i][0]-15,pos[i][1]-15,pos[i][0]+15,pos[i][1]+15,outline= "black")
        text = can.create_text(pos[i][0],pos[i][1],text= i , font=('Times','20','bold'),fill= "black")
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1], fill="black")
    return pos


root.bind("f", lambda x: move())


root.mainloop()