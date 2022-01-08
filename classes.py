#/usr/bin/python3

class Fraction:

    # initialize variables
    def __init__(self, num, den):
        self.num = num
        self.dem = den

    def toDecimal(self):
        return self.num/self.den
    
    def gcd(m,n):
        while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

    def __add__(self, f2):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

x = Fraction(2,3)

print(x.toDecimal())