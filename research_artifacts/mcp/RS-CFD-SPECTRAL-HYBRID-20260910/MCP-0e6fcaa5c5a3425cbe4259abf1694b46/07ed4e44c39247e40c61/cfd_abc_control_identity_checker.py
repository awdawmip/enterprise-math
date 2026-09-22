from fractions import Fraction

q=Fraction(11,10)
h=Fraction(1,50)
af=Fraction(7,10)*Fraction(4,5)
m=1-Fraction(1,1)/q
g=h+m
w=g/af
A=Fraction(1,1)
C=A+h
B=C-g

assert m == Fraction(1,11)
assert g == Fraction(61,550)
assert w == Fraction(61,308)
assert B == Fraction(10,11) == A/q

def rho_threshold(k,n,w):
    return w*(n-k)/(k*(1-w))

assert rho_threshold(2,20,w) == Fraction(549,247)
assert rho_threshold(1,20,w) == Fraction(61,13)

for k,rho in [(2,Fraction(549,247)),(1,Fraction(61,13))]:
    ww=Fraction(k)*rho/(Fraction(k)*rho+(20-k))
    assert ww == w
    assert af*ww == g

print("PASS")
