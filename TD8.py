import struct

##Exo 1


def lecture(file):

    f = open(file, "rb")
    data = f.read()
    nb_channels=struct.unpack_from("h",data,22)
    taille_data = struct.unpack_from("I",data,40)
    nb_echantillons = int(taille_data[0]/4)

#    on récupère les échantillons qu'on met dans les voies de gauche et de droite

    right_channel=[]
    left_channel=[]

    for i in range(nb_echantillons):
        right_channel.append((struct.unpack_from("hh",data,44+4*i))[0])
        left_channel.append((struct.unpack_from("hh",data,44+4*i))[1])
    return right_channel,left_channel

droite,gauche = lecture ("the_wall.wav")

##Exo 2

def autre_sens(droite, gauche, file):
    g = open(file,"wb")
    g.write(b"RIFF")
    g.write(struct.pack("I", 44-8 +len(droite)*4))
    g.write(b"WAVE")
    g.write(b"fmt ") #ne pas oublier l'espace
    g.write(struct.pack("IHHIIHH",16,1,2,44100,176400,4,16))
    g.write(b"data")
    g.write(struct.pack("I",len(droite)*4))

    for i in range(len(droite)):
        g.write(struct.pack("hh",gauche[i],droite[i]))
    g.close()
    return file


autre_sens(droite,gauche,"new.wav")

##Exo 3

def unsurdeux(d,g):
    return d[::2],g[::2]

d,g = unsurdeux(droite,gauche)
autre_sens(d,g,"demi.wav")





