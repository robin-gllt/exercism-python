from __future__ import division
import math

class Rational(object):
    def __init__(self, numer, denom):
        
        if denom < 0:
            numer, denom = -numer, -denom

        self.numer = numer
        self.denom = denom
        self._reduce()
        

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    #display the object in a nice str format
    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    #a1/b1 + a2/b2 = (a1 * b2 + a2 * b1) / (b1 * b2).
    def __add__(self, other):
        return Rational((self.numer * other.denom) + (self.denom * other.numer), self.denom * other.denom)

    #a1/b1 - a2/b2 = (a1 * b2 - a2 * b1) / (b1 * b2)
    def __sub__(self, other):
        return Rational((self.numer * other.denom) - (self.denom * other.numer), self.denom * other.denom)

    #r1 * r2 = (a1 * a2) / (b1 * b2
    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        try:
            return Rational(self.numer * other.denom, self.denom * other.numer)
        except:
            raise Exception("Can't divide by 0")

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** abs(power), self.denom ** abs(power))

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
        

    #reduce rational to lowest terms
    def _reduce(self):
        gcd = math.gcd(self.numer,self.denom)        
        self.numer = int(self.numer / gcd)
        self.denom = int(self.denom / gcd)

    
    

if __name__ == "__main__":
    n1 = Rational(4,8)
    print (3 ** n1)
    # n2 = Rational(0,3)
    # n3 = n1 / n2
    # print (n3)
    