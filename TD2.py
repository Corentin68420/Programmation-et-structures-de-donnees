from math import gcd
##Exo 1
class Fraction:
    def __init__(self,n,d):
        self._num = n
        self._den = d

    def toString(self):
        return f" {self._num}/{self._den}"

    def add(self,other):
        n1 =self._num
        n2 =other._num
        d1= self._den
        d2 = other._den
        return Fraction(d1*n2 +d2*n1,d1*d2)

    def mult(self,n1,d1,n2,d2):
        n1 =self._num
        n2 =other._num
        d1= self._den
        d2 = other._den
        return Fraction(n1*n2,d1*d2)


    def simplify(self):
        n = self._num
        d = self._den
        return Fraction(n/gcd(n,d),d/gcd(n,d))



if __name__ == '__main__':

    fract = Fraction(3,4)
    #assert add(1,4,1,4)== Fraction(1,2)?

    print(fract.toString())


##Exo 3

def H(n):
    s = Fraction(0,1)
    for i in range(1,n+1):
        s = s.add(Fraction(1,i))
    return s.toString()


##Exo 4

def Leibniz(n):
    s = Fraction(0,1)
    for i in range(1,n+1):
        s = s.add(Fraction((-1)**i,2*i+1))
    return s.toString()





























