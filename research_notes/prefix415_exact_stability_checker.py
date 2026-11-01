#!/usr/bin/env python3
"""PREFIX-415: exact rational inequalities, not a substitute for continuous proof."""
from fractions import Fraction as F
B=F(37577,64);E=F(53,8);beta=F(1,10**6)
eps=F(1,10**6);a=F(7,4000);b=F(187,100000)
C=a-E*beta;Slo=F(2416,100000);Shi=F(2417,100000)
assert Slo*Slo<B*beta-C*C<Shi*Shi
assert 1-eps-eps*eps>F(999999,1000000)**2
assert (eps+eps**2)/(1+F(999999,1000000))<F(3,5)*eps
assert F(709,64)<F(10,3)**2
assert E<F(13,5)**2
assert F(709,32)<F(471,100)**2
assert F(471,100)+F(13,5000)<F(19,4)
assert 2*F(19,4)*F(10,3)*F(6,5)+(F(10,3)*F(6,5))**2*eps<40
assert F(29,2)<F(381,100)**2
assert 2*F(27,4)*F(381,100)*F(6,5)+F(381,100)**2*F(6,5)**2*eps<64
xlo=(23*C+F(61,8)*Slo)/B;xhi=(23*C+F(61,8)*Shi)/B
assert xlo>0 and 2*xhi+beta<a
qplus=(1165*C+182*Slo)/B+16*beta
qminus=(141*a+48*40*eps+43*beta)/23+64*eps
assert qplus-qminus>F(1,12000)
assert F(301,10)**2>905
qplusright=2*(b+40*eps)+F(301,40000)+F(11,4)*beta+64*eps
assert F(141,23)*b-qplusright==F(4799,92000000)>F(1,20000)
def f(z,t):return (z+t)**2/4+F(45,368)**2*(t-z)**2-t
assert f(b,0)>0 and f(b,beta)<0
assert 40*eps+E*beta<a
m=F(141,23)-F(1165)/B
assert m==F(3583477,864271)>4
assert F(344)/m<86 and F(144)/m<36
print("PASS_PREFIX415_UNIFORM_CROSSING_STABILITY_EXACT_RATIONAL_CERTIFICATE")
