from tkinter import *
from tkinter import ttk
import random


root = Tk()
root.geometry("1000x1000")
window = Frame(root)
window.grid()
can = Canvas(root, width= 1000, height = 1000, bg = "white")
can.grid()


graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]

pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])



COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']

##Ex 1
def draw(can, graph, pos, col_index):
    can.delete(all)
    N = len(graph)
    for e in can.find_all():
        can.delete(e)
    for i in range(N):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1],fill= "black" )
    for i in range(N):
        x, y = pos[i]
        can.create_oval(x-6, y-6, x+6, y+6, fill=col_index[i])
        can.create_text(x-12,y,text=f"{i}", font=('Times','15','bold'),fill= "black")

#draw(can, graph, pos, COLORS)
#root.mainloop()

##Ex2

def min_local(i, graph, colors):
    m = i
    if len(graph[i]) !=0:
        mm = min (graph[i])
        m = min(m,mm)

    index_voisins = [i]
    for j in range(len(graph)):
        if i in graph[j]:

            m = min(m,j)
            index_voisins.append(j)
    col=colors[m]
    for index in graph[i]:
        index_voisins.append(index)

    for j in index_voisins:
        colors[j] = col
    return colors

"""
COLORS_new =min_local(1, graph, COLORS)
draw(can, graph, pos, COLORS_new)
root.mainloop()
"""

##Ex3

for j in range(len(graph)):
    COLORS = min_local(j,graph,COLORS)

dicolors={}
for j in range(len(graph)):
    if COLORS[j] in dicolors.keys():
        dicolors[COLORS[j]].append(j)
    else:
        dicolors[COLORS[j]] = [j]

print("il y a",len(dicolors),"parties connexes")
for value in dicolors.values():
    print("->",value)
draw(can, graph, pos, COLORS)
root.mainloop()

