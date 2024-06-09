class Pol:
    def __init__(self,P,n,q): # P =[1,2,4,0] pour P = 1 + 2x + 4x^2
        self.deg = n
        self.pol = P
        self.modulo=q
        for i in range(len(self.pol)):
            self.pol[i] = self.pol[i]%self.modulo # si coeffs pas <q, on met le reste de leur division euclidienne par q à la place



    def red(self): # réduction du polynôme dans l'ensemble

        if len(self.pol) < self.deg: #si pas d'éléments en x^n ou plus, pas de division euclidienne
            return self
        L= []
        e=1
        for i in range(self.deg,len(self.pol)):
            e=-e #signe change une fois sur deux
            L.append(e*self.pol[i]) # L: liste des coeffs à ajouter devant les bons x^k


        while len(L)> self.deg: # tant que L est plus grande que le degré n tq x^n=-1, on ajoute ses coefficients devant les bons x^k (k<=n)
            for i in range (self.deg):
                if i>len(self.pol):
                    self.pol.append(L[i])
                else:
                    self.pol[i]+=L[i]
            L = L[self.deg+1:]
        for i in range (len(L)): # on ajoute enfin les derniers éléments de L puis on recalcule les vrais coefficients modulo q
                if i>len(self.pol):
                    self.pol.append(L[i])
                else:
                    self.pol[i]+=L[i]
                self.pol[i] = self.pol[i]%self.modulo #on réadapte les coeffs modulo q
        self.pol = self.pol[:self.deg] # on enlève les coeffs de degré>n qui ont été ajoutés aux coeffs de degré<n

        return self

    def toString(self):
        return f"P={self.pol}"

    def add(self,Q):
        assert self.deg == Q.deg
        assert self.modulo==Q.modulo
        P= Pol.red(self).pol
        Q= Pol.red(Q).pol

        return Pol.red(Pol([P[i]+Q[i] for i in range(len(P))],self.deg,self.modulo))


    def mul(self,Q):

        assert self.deg == Q.deg
        assert self.modulo==Q.modulo
        P= Pol.red(self).pol
        Q= Pol.red(Q).pol
        n = self.deg
        R = [0 for i in range (2*n-1)]
        for i in range(n-1):
            for j in range(n-1):
                R[i+j] += P[i]*Q[j]

        return Pol.red(Pol(R,n,self.modulo))

    def scalar(self,c):
        for i in range (len(self.pol)):
            self.pol[i] = (c*self.pol[i])%self.modulo
        return self

    def rescale(self, r):
        for coeff in self.pol:
            coeff = coeff%r
        return self

    def fscalar(self,r,a):
        Q = []
        for coeff in self.pol:
            Q.append(round(coeff*a)%r)
        return Pol.red(Pol(Q,self.deg,self.modulo))


#test reduction
"""
H =Pol([1,4,7,2,7,8],5,3)
I = Pol.red(H)
print(Pol.toString(I))
"""

#test add
"""
Q=Pol.add(Pol([1,2,3],3,2),Pol([2,3,4],3,2))
print(Pol.toString(Q))
"""
#test mul
#print(Pol.toString(Pol.mul(Pol([1,2,3],3,2),Pol([2,3,4],3,2))))

#test scalar
#print(Pol.toString(Pol.scalar(Pol([1,2,3],3,2),5)))






