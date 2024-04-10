import matplotlib.pyplot as plt


class Hashtable:

    def __init__(self,h,n):
        self.size = n
        self.hash = h
        self.table = [[] for i in range (n)]


    def put(self, key, value):
        v = self.hash(key,self.size)
        l = self.table[v]
        for i in range (len(l)):
            if l[i][0]==key:
                l[i] = (key,value)
        if (key, value) not in l:
            l.append((key,value))
        return self


    def toString(self):
        return f" {self.table}"

    def get(self, key):
        v = self.hash(key,self.size)
        l = self.table[v]
        for tup in l:
            if tup[0] ==key:
                return tup[1]
        print("clé non présente")
        return None

    def resize(self):
        new_size = self.size * 2
        new_tables = [[] for _ in range(new_size)]
        for table in self.table:
            for key, value in table:
                new_index = self.hash(key, new_size)
                new_tables[new_index].append((key, value))
        self.size = new_size
        self.table = new_tables





def hnaif(ch,n):
    h = 0
    for l in ch:
        h += ord(l)%n
    return h

H = Hashtable(hnaif,5).put('a',2)
H = H.put('a',3)
print(H.toString())


