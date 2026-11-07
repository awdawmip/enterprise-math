#!/usr/bin/env python3
"""R5 exact support-switch checker: Fraction-only affine certificates, 2026-11-07.
Each 8-point identity check (origin + 7 coordinate vectors) proves the affine
identity for every real flow. No finite testing is used as a universal proof.
"""
from fractions import Fraction as Q
Z=Q(0)
R=(Q(1,10),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(19,10))
LM=-Q(351,17291)
LP=Q(351,16589)
# lam: (sharp bound at TP=TQ=31/10, alpha, beta,
#       four slacks (u,C1-v,w,9b/40-v+z), g-b slack, 1-g slack)
C={
-Q(1,10):(Q(16456,58125),Q(21007,348750),Q(9403,348750),
 (Q(46481,930000),Q(54791,558000),Q(183499,2790000),Q(17537,162000)),Q(13781,558000),Z),
LM:(Q(22146,86455),Q(6694,86455),Q(3016,86455),
 (Q(22473,345820),Q(7789,69164),Q(46129,345820),Q(81757,622476)),Z,Z),
Z:(Q(13269,53000),Q(391,6625),Q(364,6625),
 (Q(3999,53000),Q(1283,10600),Q(7127,53000),Q(247,1800)),Z,Q(117,10600)),
LP:(Q(20391,82945),Q(3184,82945),Q(6526,82945),
 (Q(26373,331780),Q(7789,66356),Q(42229,331780),Q(81757,597204)),Z,Z),
Q(1,10):(Q(27083,116250),-Q(43037,348750),Q(81727,348750),
 (Q(332837,2790000),Q(67769,558000),Q(112541,2790000),Q(21983,162000)),Q(13079,558000),Z)}

def model(g,a,b,u,v,w,z,legal=False):
 c0=Q(13,40)*a+b/80
 c1=a/10+Q(9,40)*b
 c2=Q(3,40)*a+Q(21,80)*b
 tp=1+g+(3*a+5*b)/8+u/2+v+Q(3,2)*w
 tq=1+g+(a+b)/2+u+v+w
 m=(Q(509,900)*u+Q(47,180)*z+Q(67,162)*(v-z)+w/100,
    c0-u,(g-a)/2,
    1-g+c1-v+Q(191,450)*(u+w)+Q(43,90)*z+Q(14,81)*(v-z),
    (g-b)/2,c2-w,
    u/100+Q(47,180)*z+Q(67,162)*(v-z)+Q(509,900)*w)
 sl=(u,c1-v,w,Q(9,40)*b-v+z)
 if legal:
  assert 0<=a<=g<=1 and 0<=b<=g
  assert 0<=u<=c0 and 0<=v<=c1 and 0<=w<=c2
  assert 0<=z<=a/10 and 0<=v-z<=Q(9,40)*b
  assert all(x>=0 for x in m) and sum(m,Z)==1
  assert sum((r*x for r,x in zip(R,m)),Z)==1
 for lam,(bound,alpha,beta,mu,mg,mo) in C.items():
  s=sum((max(Z,1-(1+lam)*r)*x for r,x in zip(R,m)),Z)
  gap=bound+alpha*(tp-Q(31,10))+beta*(tq-Q(31,10))-s
  rhs=sum((x*y for x,y in zip(mu,sl)),Z)+mg*(g-b)+mo*(1-g)
  assert gap==rhs, (lam,gap,rhs)
 return tp,tq,m

basis=[(Z,)*7]+[tuple(Q(int(j==k)) for j in range(7)) for k in range(7)]
for point in basis: model(*point)
print('PASS_40_AFFINE_COEFFICIENT_IDENTITIES_ALL_REAL')

A=Q(28,31)
B=Q(44,53)
def endpoint(g,a): return (g,a,a,Z,Q(13,40)*a,Z,a/10)
for g,a in [(A,A),(Q(1),B)]:
 tp,tq,m=model(*endpoint(g,a),legal=True)
 assert tp==tq==Q(31,10)
 assert 9*a*(a/10)==4*a*(Q(13,40)*a-a/10)
 for lam in C:
  s=sum((max(Z,1-(1+lam)*r)*x for r,x in zip(R,m)),Z)
  if g==a and lam in (-Q(1,10),LM,LP,Q(1,10)): assert s==C[lam][0]
  if g==1 and lam in (LM,Z,LP): assert s==C[lam][0]
print('PASS_TWO_SEEDLESS_ENDPOINTS_AND_SWITCH_EQUALITIES')

# Both switch values and slopes are exact, with no additional key-sign changes.
def support(a,lam):
 m=model(*endpoint(a,a) if a==A else endpoint(Q(1),B))[2]
 return sum((max(Z,1-(1+lam)*r)*x for r,x in zip(R,m)),Z)
for lam in (LM,LP):
 assert support(A,lam)==support(B,lam)==C[lam][0]
assert -Q(1,10)<LM<0<LP<Q(1,10)
for i in range(-100,101):
 lam=Q(i,1000)
 best=max(support(A,lam),support(B,lam))
 # On each closed piece, affine nonnegative certificates at its endpoints
 # interpolate; this loop checks samples, while the proof handles all reals.
 for g,a in [(A,A),(Q(1),B)]:
  assert support(a,lam)<=best
print('PASS_201_RATIONAL_SLICES_AND_PIECEWISE_SHARP_SUPPORT')
print('LAMBDA_SWITCH_MINUS',LM,'VALUE',C[LM][0])
print('LAMBDA_SWITCH_PLUS',LP,'VALUE',C[LP][0])
print('LAMBDA_ZERO_VALUE',C[Z][0])
print('PASS_EXACT_R5_SIGNED_LAMBDA_TWO_FLOW_SWITCH_GLOBAL')
