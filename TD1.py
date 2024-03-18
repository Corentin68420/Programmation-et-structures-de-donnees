from copy import deepcopy
#camille.lanuel@loria.fr, lien github

f = open("frenchssaccent.dic",'r')
mots_possibles = []
for ligne in f:
    mots_possibles.append(ligne[0:len(ligne)-1])
f.close()


tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']

def rech(tirage, mots_possibles):

    n = len(tirage)
    p, M = mots_possibles[0], 0
    for mot in mots_possibles:
        l = 0

        ti = deepcopy(tirage)
        if len(mot) <=n:
            for lettre in mot:

                if lettre in ti:
                    l +=1
                    ti.pop(0)

                else:
                    l = l- 2*n

            if l >= M:
                M = l
                p = mot

    return p



dico = {1: ['a','e','i','l','n','o','r','s','t','u'], 2: ['d','g','m'], 3:['b','c','p'], 4:['f','h','v'], 8: ['j','q'], 10: ['k','w','x','y','z']}

def score(mot):
    sc=0
    for lettre in mot:
        for cle,valeur in dico.items():
            if lettre in valeur:
                sc += cle
    return sc

def max_score(liste):
    M = 0
    mo = liste[0]
    for mot in liste:
        if score(mot)>= M:
            M = score(mot)
            mo = mot
    return mo,M

## Exo 4

# il suffit de rajouter un test, si lettre="?", continuer de parcourir les autres lettres
# Dans dico, on peut également rajouter un item 0:["?"]





