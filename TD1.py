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

print(rech(tirage, mots_possibles))

def score(mot):
    score = 0
    D = { 1 : "aeilnostu", 2:"dgm", 3: "bcp", 4: "fhv", 8: "jq", 10: "kwxyz"}
    for lettre in mot:
        for (value,key) in D.items:
            if lettre in value:
                score = key
    return score




