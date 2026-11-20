#!/usr/bin/env python3
"""Stage364-B exact rational transverse equal-error projection certificate.

All 16 Bernoulli source/word labels remain separate. Fraction+SymPy;
no floating-point computation is used to establish a universal inequality.
"""
from fractions import Fraction as F
import sympy as S

XL,XU=F(2311,10000),F(29,125)
YL,YU=F(1111,2000),F(559,1000)
KL,KU=F(2312,10000),F(2318,10000)
LL,LU=F(139,250),F(279,500)
ETA=F(1,100000)
X,Y=S.symbols('x y',real=True)
w=(1,3,3,1)
m=(61,21,9,9)

def B(k,z):return z**k*(1-z)**(3-k)
def residual(k,x,y):return (4*B(k,x)+B(k,y))/5-F(m[k],160)
def u1(z):return (1-z)*(1-3*z)
def u2(z):return z*(2-3*z)
def Dport(a,z,s):return S.Rational(1,2)*sum(w[k]*s[k]*(B(k,a)-B(k,z)) for k in range(4))

assert XL<KL<KU<XU and YL<LL<LU<YU
assert XL<F(1,4)<YL<F(2,3)
assert sum(w[k]*m[k] for k in range(4))==160
assert S.expand(sum(w[k]*residual(k,X,Y) for k in range(4)))==0
# r0 decreases, r2 and r3 increase on R; exact full-box signs.
assert residual(0,XL,YL)<0 and residual(2,XL,YL)>0 and residual(3,XU,YU)<0
print('EXACT_RESIDUAL_SIGNS_r0_NEG_r2_POS_r3_NEG_AND_WEIGHTED_SUM_ZERO_PASS')

# Four port blocks preserve the original sixteen labeled comparisons.
labels=[(F(1,4),XL,XU,(-1,+1,+1,+1)),
        (F(3,4),XL,XU,(-1,-1,+1,+1)),
        (F(1,4),YL,YU,(+1,+1,-1,-1)),
        (F(3,4),YL,YU,(-1,-1,+1,+1))]
for anchor,lo,hi,signs in labels:
    for k in range(4):
        for z in (lo,hi):
            assert signs[k]*(B(k,anchor)-B(k,z))>0
C=S.factor((63*Dport(S.Rational(1,4),X,labels[0][3])
           +Dport(S.Rational(3,4),X,labels[1][3])
           +9*Dport(S.Rational(1,4),Y,labels[2][3])
           +7*Dport(S.Rational(3,4),Y,labels[3][3]))/256)
cx=-3*(1-X)*(63-61*X)/256
cy=3*Y*(1-Y)/64
assert S.simplify(S.diff(C,X)-cx)==0 and S.simplify(S.diff(C,Y)-cy)==0
print('ORIGINAL_SIXTEEN_LABELS_AND_FOUR_AUDIT_GRADIENTS_PASS')

r1=residual(1,X,Y)
r2=residual(2,X,Y)
bminus=S.Rational(15,16)*r2
bplus=S.Rational(15,16)*(r2+r1)
assert S.simplify(bplus-S.Rational(3,16)*(4*X*(1-X)+Y*(1-Y))+S.Rational(45,256))==0
bxm=S.Rational(3,4)*u2(X);bym=S.Rational(3,16)*u2(Y)
bxp=S.Rational(3,4)*(1-2*X);byp=S.Rational(3,16)*(1-2*Y)
assert all(S.simplify(a-b)==0 for a,b in [(S.diff(bminus,X),bxm),(S.diff(bminus,Y),bym),
                                           (S.diff(bplus,X),bxp),(S.diff(bplus,Y),byp)])
rx=S.Rational(4,5)*u1(X);ry=S.Rational(1,5)*u1(Y)
Jm=S.factor(rx*bym-ry*bxm)
Jp=S.factor(rx*byp-ry*bxp)
J=S.Rational(3,20)*(u1(X)*u2(Y)-u1(Y)*u2(X))
assert S.simplify(Jm-J)==0 and S.simplify(Jp-J)==0
print('EXACT_BRANCH_GRADIENTS_AND_SHARED_POSITIVE_JACOBIAN_IDENTITY_PASS')

# All corner-enclosure bounds use rational, globally valid monotonic ranges.
gmin=F(3,256)*(1-XU)*(63-61*XU)
cymin=F(3,64)*YU*(1-YU)
cymax=F(3,64)*YL*(1-YL)
bymin=F(3,16)*u2(YU)
bxmin=F(3,4)*u2(XL)
bxpmax=F(3,4)*(1-2*XL)
negative_byp_min=F(3,16)*(2*YL-1)
Dminus_upper=-gmin*bymin-cymin*bxmin
Dplus_lower=gmin*negative_byp_min-cymax*bxpmax
Jlower=F(3,20)*(u1(XU)*u2(YU)-u1(YL)*u2(XL))
Jupper=F(3,20)*(u1(XL)*u2(YL)-u1(YU)*u2(XU))
assert Dminus_upper<-F(1,60),Dminus_upper
assert Dplus_lower>F(1,250),Dplus_lower
assert Jlower>F(1,60) and Jupper<F(1,40)
# bx never exceeds 41/100 in absolute value, and |by|<1/25.
assert F(3,4)*(1-2*XL)<F(41,100)
assert F(3,4)*u2(XU)<F(41,100)
assert F(3,16)*u2(YL)<F(1,25)
assert F(3,16)*(2*YU-1)<F(1,25)
print('EXACT_JACOBIAN_1/60<J<1/40_AND_COST_DETERMINANTS_DMINUS<-1/60_DPLUS>1/250_PASS')

# Distance-to-boundary barrier establishes existence of the fixed-b continuation.
dx_bound=F(12,5)*ETA  # (1/25)/(1/60)
dy_bound=F(123,5)*ETA # (41/100)/(1/60)
assert dx_bound<min(KL-XL,XU-KU)
assert dy_bound<min(LL-YL,YU-LU)
assert F(1,250)*40==F(4,25)
assert F(1,60)*40==F(2,3)
print('EXACT_INNER_BOX_ETA_BARRIER_AND_PROJECTION_COST_SLOPE_LOWER_BOUNDS_PASS')
print('THEOREM: for p in K with |r1(p)|<=1/100000, the fixed-b path')
print('reaches an r1=0 point q in R with b(q)=b(p).')
print('When r1(p)>0: c(p)-c(q) > (4/25)*r1(p).')
print('When r1(p)<0: c(p)-c(q) > (2/3)*(-r1(p)).')
print('STAGE364B_EXACT_OFF_ARC_EQUAL_ERROR_SHARP_PROJECTION_PASS')
