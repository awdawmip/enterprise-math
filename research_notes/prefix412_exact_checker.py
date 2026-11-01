#!/usr/bin/env python3
"""PREFIX-412 author-side exact certificates; Python 3 / SymPy.
The all-eta interval theorem uses the separate analytic continuity proof.
"""
from fractions import Fraction as F
from sympy import I, Matrix, Rational as R, sqrt, simplify, expand, conjugate

# Original 5x3 static complex Port matrix: no native typed BRC claim.
A=Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
T=simplify(A*A[:3,:].inv())
a=(5+9*I)/2; b=(3+7*I)/2; d=(22+15*I)/8; e=(5+9*I)/4
assert T[3,:]==Matrix([[a,b,4*I]])
assert T[4,:]==Matrix([[d,d,e]])
x,y=__import__('sympy').symbols('x y',real=True)
v=x+I*y; t=x*x+y*y
E=R(53,8); beta=R(1,10**6)

for sig,P,Q,jbase,cx,cy in [(1,R(23),R(61,8),37,48,8),(-1,R(61,8),-R(23),45,24,-48)]:
    u=sig*I
    J4=expand((a+b*u+4*I*v)*conjugate(a+b*u+4*I*v))
    J5=expand((d*(1+u)+e*v)*conjugate(d*(1+u)+e*v))
    h=2*x+t
    k=P*x+Q*y+E*t
    assert simplify(J4-(jbase+cx*x+cy*y+16*t))==0
    assert simplify(J5-(R(709,32)+k))==0
    if sig==1:
        assert simplify(J4-(37+(728*h+64*k-176*t)/61))==0
    else:
        assert simplify(J4-(45+(93*h+48*k-43*t)/23))==0

eta_lo=R(1,10000); eta_pos=R(3,4000); eta_hi=R(23,1000)
# Exact uniform positive-branch witness v_eta=(2/5-5i/4)eta.
eta=__import__('sympy').symbols('eta',real=True,nonnegative=True)
xw=R(2,5)*eta; yw=-R(5,4)*eta
tw=simplify(xw*xw+yw*yw)
hw=simplify(2*xw+tw); kw=simplify(23*xw+R(61,8)*yw+E*tw)
assert tw==R(689,400)*eta**2
assert simplify(kw+R(53,160)*eta-E*tw)==0
assert simplify((48*xw+8*yw+16*tw)-(R(46,5)*eta+R(689,25)*eta**2))==0
assert tw.subs(eta,eta_pos)<beta
assert 0<hw.subs(eta,eta_pos)<eta_pos
assert abs(kw.subs(eta,eta_pos))<eta_pos
assert (R(353,115)*eta_lo+R(689,25)*eta_lo**2-R(43,23)*beta)>0

# Exact negative-branch witness at eta_hi.
xn=-R(3,5000); yn=R(4,5000)
tn=xn*xn+yn*yn
hn=2*xn+tn
kn=R(61,8)*xn-23*yn+E*tn
J4n=45+24*xn-48*yn+16*tn
assert tn==beta
assert hn==-R(1199,10**6)
assert kn==-R(183747,8000000)
assert abs(hn)<eta_hi and abs(kn)<eta_hi
assert J4n-41==R(246701,62500)
assert R(6083,1000)**2>37
# All positive sources have kappa_+ > 493915/125000 > the negative witness.
assert (4-R(6083,1000)/125-R(1,62500))==R(493915,125000)
assert R(493915,125000)>J4n-41

# For eta>=1/40 the h,k constraints hold throughout each disk |v|<=sqrt(beta).
assert R(194)**2>R(37577)
assert R(194,8000)+E*beta<R(1,40)
assert R(2,1000)+beta<R(1,40)
kap_plus=41-(sqrt(37)+R(1,250))**2
kap_minus=(sqrt(45)-R(1,250))**2-41
assert (sqrt(45)-sqrt(37))>R(1,250)
assert simplify(kap_plus-kap_minus)>0
print('PASS_PREFIX412_EXACT_PORT_IDENTITIES_WITNESSES_AND_EVENTUAL_BRANCH_INVERSION')
print('lower_eta_positive_dominance_to',eta_pos,'; upper_eta_negative_witness_at',eta_hi)
print('eta_hi_negative_witness_h=',hn,'k=',kn,'t=',tn,'kappa=',J4n-41)
print('full_disk_unconstrained_eta_ge=',R(1,40))
print('saturation_kappa=',kap_minus,'approx=',kap_minus.evalf(18))
print('eta_critical_in_open_interval=',(eta_pos,eta_hi),'existence_from_continuity')
