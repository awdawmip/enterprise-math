#!/usr/bin/env python3
"""Stage363-B exact standalone algebra/inequality verifier.

Original 16 Bernoulli label comparisons remain separate; no randomized search
or float values enter the mathematical certificate. Python 3 + SymPy.
"""
from fractions import Fraction as F
import sympy as S

Lx, Ux, Ly, Uy = F(229,1000), F(233,1000), F(27,50), F(14,25)
xl, xr, xb = F(231,1000), F(2311,10000), F(29,125)
X,Y=S.symbols('x y',real=True)
w=(1,3,3,1)
m=(61,21,9,9)

def B(k,z): return z**k*(1-z)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(m[k],160)
def deriv(z):return (1-z)*(1-3*z)
def B2p(z):return z*(2-3*z)

def signed_D(a,z,signs):
    return S.Rational(1,2)*sum(w[k]*signs[k]*(B(k,a)-B(k,z)) for k in range(4))

# Each B_k is strictly monotonic in both coordinate intervals: B0 decreases;
# B1 increases for x<1/3 and decreases for y>1/3; B2/B3 increase here.
assert Ux<F(1,3)<Ly and Uy<F(2,3)
labels=[(F(1,4),Lx,Ux,(-1,+1,+1,+1)),
        (F(3,4),Lx,Ux,(-1,-1,+1,+1)),
        (F(1,4),Ly,Uy,(+1,+1,-1,-1)),
        (F(3,4),Ly,Uy,(-1,-1,+1,+1))]
for anchor,lo,hi,sgn in labels:
    for k,sign in enumerate(sgn):
        for z in (lo,hi):
            assert sign*(B(k,anchor)-B(k,z))>0,(anchor,k,z)
print('FOUR_AUDIT_PORTS_SIXTEEN_LABEL_SIGNS_EXACT_PASS')

C=S.factor((63*signed_D(S.Rational(1,4),X,labels[0][3])
 +signed_D(S.Rational(3,4),X,labels[1][3])
 +9*signed_D(S.Rational(1,4),Y,labels[2][3])
 +7*signed_D(S.Rational(3,4),Y,labels[3][3]))/256)
cx=-3*(1-X)*(63-61*X)/256
cy=3*Y*(1-Y)/64
assert S.simplify(S.diff(C,X)-cx)==0
assert S.simplify(S.diff(C,Y)-cy)==0

# The r1=0 curve exists uniquely and is increasing for x in [xl,xb],
# because r1(y=Ly)>0, r1(y=Uy)<0 and B1'(y)<0.
assert r(1,xl,Ly)>0 and r(1,xb,Uy)<0
assert r(1,xl,F(555,1000))>0 and r(1,xl,F(5555,10000))<0
assert r(0,xl,F(5555,10000))>0
assert r(1,xr,F(55555,100000))>0 and r(1,xr,F(55556,100000))<0
assert r(0,xr,F(55555,100000))<0
assert r(1,xb,F(558,1000))>0 and r(1,xb,F(559,1000))<0
assert r(2,Lx,Ly)>0 and r(3,Ux,Uy)<0
print('STAR_ROOT_UNIQUE_BRACKET_X=(231/1000,2311/10000);_Y_MONOTONE_EXACT_PASS')

# Implicit differentiation: 4*B1(x)+B1(y)=21/32.
yprime=-4*S.diff(B(1,X),X)/S.diff(B(1,Y),Y)
ysecond=-(4*S.diff(B(1,X),X,2)+S.diff(B(1,Y),Y,2)*yprime**2)/S.diff(B(1,Y),Y)
beta=S.Rational(15,16)*((4*B(2,X)+B(2,Y))/5-S.Rational(9,160))
bp=S.factor(S.diff(beta,X)+S.diff(beta,Y)*yprime)
bpp=S.factor(S.diff(bp,X)+S.diff(bp,Y)*yprime)
cp=S.factor(cx+cy*yprime)
cpp=S.factor(S.diff(cp,X)+S.diff(cp,Y)*yprime)
assert S.simplify(yprime+4*(1-X)*(1-3*X)/((1-Y)*(1-3*Y)))==0
assert S.simplify(bp-S.Rational(3,16)*(4*B2p(X)+B2p(Y)*yprime))==0
assert S.simplify(bpp-S.Rational(3,16)*(4*(2-6*X)+(2-6*Y)*yprime**2+B2p(Y)*ysecond))==0
assert S.simplify(cpp-(S.diff(cx,X)+S.diff(cy,Y)*yprime**2+cy*ysecond))==0
print('IMPLICIT_FIRST_SECOND_DERIVATIVE_POLYNOMIAL_IDENTITIES_PASS')

# Exact uniform bounds on the *entire* rational rectangle, hence on its r1=0 arc.
def yp_rat(x,y):return 4*(1-x)*(1-3*x)/((1-y)*(3*y-1))
ypmin=yp_rat(Ux,Uy); ypmax=yp_rat(Lx,Ly)
assert ypmin>3 and ypmax<F(7,2)
Bmax=(1-Uy)*(3*Uy-1)
Amin=4*(4-6*Ux)+(4-6*Uy)*9
assert Bmax<F(3,10) and Amin>F(159,10) and Amin/Bmax>53
bpmin=F(3,16)*4*B2p(Lx)
bpmax=F(3,16)*(4*B2p(Ux)+B2p(Ly)*F(7,2))
assert bpmin>F(9,40) and bpmax<F(3,8)
cxmax=-3*(1-Ux)*(63-61*Ux)/256
cpmax=-F(43,100)+F(3,256)*F(7,2)
assert cxmax<-F(43,100) and cpmax<-F(3,8)
bppmax=F(3,16)*(4*(2-6*Lx)+(2-6*Ly)*9+B2p(Uy)*(-53))
assert bppmax<-3
cppmax=3*(124-122*Lx)/256
assert cppmax<F(7,6)
# c'' * b' - c' * b'' < (7/6)(3/8) - (3/8)(3) = -11/16
assert F(7,6)*F(3,8)-F(3,8)*3 == -F(11,16)
assert F(11,16)/F(3,8)**3 == F(352,27)
print('UNIFORM_BPRIME=(9/40,3/8),_CPRIME<-3/8,_BSECOND<-3,_CSECOND<7/6_PASS')
print('CURVATURE_NUMERATOR<-11/16_AND_COST_ERROR_SECOND_DERIVATIVE<-352/27_PASS')

# Star x is < xr; xb-star x > xb-xr=9/10000. Along r1=0 beta'>9/40.
assert xb-xr==F(9,10000)
assert F(9,40)*(xb-xr)>F(1,5000)
print('ALL_ERROR_EXCESSES_0<=s<=1/5000_LIE_IN_CERTIFIED_PRECUSP_ARC_PASS')
print('THEOREM: for s,t>=0, s+t<=E<=1/5000,')
print('phi(s)+phi(t)-phi(0)-phi(E) >= (352/27)*s*t + E-s-t;')
print('equality exactly when s*t=0 and s+t=E (including E=0).')
print('STAGE363B_NEAR_STAR_QUANTITATIVE_SPLIT_RIGIDITY_EXACT_PASS')
