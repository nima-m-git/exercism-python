from __future__ import division



class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    
    def __eq__(self, other):
        return self.numer == numer and self.denom == denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)  

    def __add__(self, other):
        return self.lcd(n=(self.numer*self.denom + other.numer*self.denom), d=(self.denom*other.denom))

    def __sub__(self, other):
        return self.lcd(n=(self.numer*other.denom - other.numer*self.denom), d=(self.denom*other.denom))

    def __mul__(self, other):
        return self.lcd(n=(self.numer*other.numer), d=(self.denom*other.denom))

    def __truediv__(self, other):
        if (other.numer*self.denom) != 0:
            return self.lcd(n=(self.numer*other.denom), d=(other.numer*self.denom))

    def __abs__(self):
        return self.lcd(n=abs(self.numer), d=abs(self.denom))

    def __pow__(self, p):
        if p > 0:
            return self.lcd(n=(self.numer**p), d=(self.denom**p))
        if p < 0:
            m = abs(p)
            return self.lcd(n=(self.denom**m), d=(self.numer**m))

    def __rpow__(self, b):
        return self.lcd((b**self.numer)**(1/self.denom))
    
    def lcd(self, n, d):
        d_a = [i for i in range(1,abs(n)+1) if n%i==0]
        d_b = [i for i in range(1,abs(d)+1) if d%i==0]
        #make a list that only has common values in a and b, find lowest
        lcd = max([denom for denom in d_a if denom in d_b])
        numer, denom = int(n/lcd), int(d/lcd)
        return numer, denom  

print(Rational(-1,2) == Rational(1,2))
