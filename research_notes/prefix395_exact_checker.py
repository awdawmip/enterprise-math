#!/usr/bin/env python3
"""Exact self-contained author checker for PREFIX-395's public research note."""
import sympy as S
z, r, k, s4, s5 = S.symbols('z r k s4 s5', real=True)
R = 1 + z*z


def eliminate(rr, kk, t4, t5):
    A, B = rr*(1-z*z), 2*rr*z
    l4, m4 = 56*A+24*B+72*R, -24*A+56*B-40*R
    n4 = 78*A-8*B+(32*kk+29*rr**2+53-2*t4)*R
    l5, m5 = 980*A+492*B+980*R, -492*A+980*B-492*R
    n5 = 1418*A+(424*kk+709*rr**2+709-64*t5)*R
    D = S.expand(l4*m5-m4*l5)
    C = S.expand(m4*n5-m5*n4)
    T = S.expand(l5*n4-l4*n5)
    H = S.expand(C*C+T*T-kk*D*D)
    return D,C,T,H

D,C,T,H = eliminate(r,k,s4,s5)
assert S.rem(H,R,z) == 0
G=S.div(H,R,z)[0]
assert S.degree(G,z) <= 6
D2=(3776-4032*r*r)*R-256*r*(1-z*z)+47104*r*z
assert S.expand(D-R*D2) == 0
assert S.expand(S.rem(C,R,z)+3872*r*r*z+13984*r*r) == 0
assert S.expand(S.rem(T,R,z)+13984*r*r*z-3872*r*r) == 0

Q=S.Rational
I=S.I
MAT=S.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
              [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
w=S.Matrix([1,Q(11,26)-I*Q(66,65),-Q(4,3)+I*Q(1,2)])
y=MAT[:3,:].inv()*w
intensities=[S.expand_complex(v*S.conjugate(v)).simplify() for v in MAT*y]
assert intensities == [1,Q(121,100),Q(73,36),Q(532313,23400),Q(11531293,748800)]
assert all(v>0 for v in intensities)
d,c,t,h=eliminate(Q(11,10),Q(73,36),intensities[3],intensities[4])
exact_g=S.Poly(-741820491*z**6+135702895008*z**5-2066435198845*z**4-
               6015285648440*z**3-2513495362034*z**2+
               383703712072*z+16724861960,z)
G0=S.Poly(S.div(h,R,z)[0],z)
assert G0.degree() == 6
assert G0.clear_denoms(convert=True)[1].primitive()[1] in (exact_g,-exact_g)
assert S.gcd(exact_g,S.Poly(S.div(d,R,z)[0],z)).degree() == 0
assert S.gcd(exact_g,exact_g.diff()).degree() == 0
intervals=[(-2,-Q(19,10)),(-Q(7,10),-Q(3,5)),(-Q(1,20),-Q(1,50)),
           (Q(1,10),Q(1,5)),(S.Integer(19),S.Integer(20)),
           (S.Integer(160),S.Integer(170))]
for lo,hi in intervals:
    assert lo<hi and exact_g.eval(lo)*exact_g.eval(hi)<0
assert all(intervals[i][1]<intervals[i+1][0] for i in range(5))
abs_bins=[(Q(1,50),Q(1,20)),(Q(1,10),Q(1,5)),
          (Q(3,5),Q(7,10)),(Q(19,10),S.Integer(2)),
          (S.Integer(19),S.Integer(20)),(S.Integer(160),S.Integer(170))]
def Cu(t): return 1+Q(121,100)+Q(11,5)*(1-t*t)/(1+t*t)
gaps=[S.factor(Cu(abs_bins[j][1])-Cu(abs_bins[j+1][0])) for j in range(5)]
assert gaps == [Q(1320,40501),Q(220,221),Q(137280,68689),
                Q(3927,4525),Q(110880,10266001)]
assert min(gaps)>Q(1,100)
print('PASS_PREFIX395_REPOSITORY_EXACT_WITNESS_AND_UNIVERSAL_SEXTIC')
print('SIX_PHASE_INEQUIVALENT_REGULAR_FIVE_PORT_SOURCES')
print('SINGLE_OBSERVER_MIN_GAP',min(gaps))
print('DETERMINISTIC_OBSERVER_ERROR_AT_MOST_1_OVER_200')
