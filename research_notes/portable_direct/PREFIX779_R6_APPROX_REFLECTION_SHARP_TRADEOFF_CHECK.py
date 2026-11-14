"""PREFIX-779: rational and symbolic verifier for the sharp two-noise Gamma witness.
This checks the universal algebraic reduction of the inherited PREFIX-778
four-cell certificate. It does not rerun the frozen 189-layer BRC kernel.
"""
from fractions import Fraction as F
from sympy import symbols, simplify

b1,b2,a1,a2,eps,d = symbols('b1 b2 a1 a2 eps d', positive=True)
D = a2*b1-a1*b2
K = 2*b1+4*b2
q = (a1+4*eps)/b1
x1 = a1-b1*q
x2 = a2-b2*q
assert simplify(x1+4*eps)==0
assert simplify(x2-(2*eps+d) - (D-K*eps-b1*d)/b1)==0
# The seven base corners split into one common corner and six private corners.
# L1(e)=+4 eps, L1(f)=+4 eps-d;
# L2(e)=-2 eps, L2(f)=-2 eps-d.
Y1=x1+4*eps
Y2=x2-2*eps
Z1=-x1-4*eps+d
Z2=-x2+2*eps+d
assert simplify(Y1)==0
assert simplify(Z2-(K*eps+b1*d-D)/b1)==0
assert simplify(Y2-(D-K*eps)/b1)==0
# At the threshold D=K*eps+b1*d, the four increments become (0,d,d,0).
for val,target in [(Y1,0),(Y2,d),(Z1,d),(Z2,0)]:
    assert simplify(val.subs(a2,(a1*b2+K*eps+b1*d)/b1)-target)==0
# Bounds: B2 L1(e)-B1 L2(f) <= K eps + B1 min(delta,2eps).
# The coefficient upper bound is attained with c=+eps, c'=eps-d,
# private R1 base signs +eps and private R2 reflected signs -eps.
assert simplify(b2*4*eps-b1*(-2*eps-d) - (K*eps+b1*d))==0

# exact rational examples, with q>0 and 0<=d<=2eps
cases=[(F(1),F(2),F(1,100),F(1,25)),
       (F(7,6),F(13,10),F(1,50),F(7,250)),
       (F(19,20),F(1),F(1,40),F(7,250))]
for B1,B2,A1,A2 in cases:
    DD=A2*B1-A1*B2
    assert B2>B1>0 and DD>0
    CC=DD/(B1+B2); KK=2*B1+4*B2
    eps_equiv=DD/KK; eps_free=CC/4; pivot=CC/2
    assert eps_equiv>eps_free>0
    for delta in (F(0),pivot/3,pivot,pivot*2):
        threshold=(DD-B1*delta)/KK if delta<=pivot else eps_free
        d0=min(delta,2*threshold)
        assert DD==KK*threshold+B1*d0
        q0=(A1+4*threshold)/B1
        assert q0>0
        x1=A1-q0*B1; x2=A2-q0*B2
        y1=x1+4*threshold
        y2=x2-2*threshold
        z1=-x1-4*threshold+d0
        z2=-x2+2*threshold+d0
        assert (y1,y2,z1,z2)==(F(0),d0,d0,F(0))
        for fraction in (F(0),F(1,3),F(9,10)):
            e=threshold*fraction
            actual_d=min(delta,2*e)
            gap=DD-KK*e-B1*actual_d
            assert gap>0
            # For every q>0 and every admissible perturbation, the
            # positive/negative weighted certificates have gap 'gap'.
        print('PASS',B1,B2,'delta=',delta,'threshold=',threshold,
              'q_boundary=',q0,'pivot=',pivot)
print('ALL_CHECKS_PASS PREFIX779 SHARP_TWO_NOISE_TRADEOFF')
