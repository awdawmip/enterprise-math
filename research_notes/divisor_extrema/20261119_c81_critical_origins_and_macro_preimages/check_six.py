"""Exact endpoint certificate for an open set with six macroscopic preimages."""
from fractions import Fraction as F

def h(a,d):
    m=F(7,16)*a**4*d
    return 1/(a-1)+5-4*m/(1+m)-5*m*a/(1+m*a)

one=F(1)
half=F(1,2)
small=F(1,100)
target=F(1,10000)
assert h(F(4),small)==F(-18896,21783)
assert 4**4*3*small**4<target
l,r=F(3,4),F(4,5)
L,R=F(5,3),F(7,4)
assert h(l,half)>0>h(r,half)
assert h(L,half)>0>h(R,half)
assert l**4*(1-r)/(64*(1+F(7,32))**2)>target
assert (L-1)/(64*(1+F(7,32)*R**4)*(1+F(7,32)*R**5))>target
assert F(1,10)**3*F(11,10)**8>F(3,11)**3*F(8,11)**8
assert h(F(6,7),F(11,10))<F(-11,3)
assert h(F(29,25),F(4))>4
assert h(F(6,5),one)>h(F(4),F(0))==F(16,3)
print('Six-preimage and explicit sector rational endpoints verified.')
