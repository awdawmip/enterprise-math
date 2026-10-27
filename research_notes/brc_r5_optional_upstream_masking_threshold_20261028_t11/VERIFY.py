from fractions import Fraction as F
from itertools import product, combinations
from math import lcm, gcd
Y=(F(1,2),F(1),F(3,2))
a,b=F(1,4),F(1,8)
K=((a,1-2*a,a),(b,1-2*b,b))
W=(F(1,2),F(1,2))
M=tuple((K[0][j]+K[1][j])/2 for j in range(3))
assert all(min(k)>0 and sum(k)==1 and sum(Y[j]*k[j] for j in range(3))==1 for k in K)
qleaf=[W[i]*K[i][j] for i in range(2) for j in range(3)]
pleaf=[Y[j]*W[i]*K[i][j] for i in range(2) for j in range(3)]
assert min(qleaf)>0 and min(pleaf)>0 and sum(qleaf)==sum(pleaf)==1

def action(w,k,act):
    kind,bits=act
    if kind=='P':return (F(0),w,2*w)
    if kind=='Q':return (w,F(0),2*w)
    return (w*sum(k[j]*Y[j]*bits[j] for j in range(3)),
            w*sum(k[j]*(1-bits[j]) for j in range(3)),3*w)

def plus(u,v):return tuple(x+y for x,y in zip(u,v))
ACTIONS=[('P',None),('Q',None)]+[('C',bits) for bits in product((0,1),repeat=3)]
root={(F(0),F(1),F(1)),(F(1),F(0),F(1))}
FULL=root | {plus(action(W[0],K[0],u),action(W[1],K[1],v)) for u,v in product(ACTIONS,repeat=2)}
LR=root | {action(F(1),M,u) for u in ACTIONS}
assert len(FULL)==77 and len(LR)==12 and LR<=FULL

def sub(u,v):return tuple(x-y for x,y in zip(u,v))
def cross(u,v):return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def dot(u,v):return sum((x*y for x,y in zip(u,v)),F(0))

def faces(points):
    pts=sorted(points); answer=set()
    for u,v,w in combinations(pts,3):
        n=cross(sub(v,u),sub(w,u))
        if n==(0,0,0):continue
        d=lcm(*(x.denominator for x in n))
        n=tuple(int(x*d) for x in n)
        g=gcd(*n);n=tuple(x//g for x in n)
        rhs=dot(n,u); signs=[dot(n,p)-rhs for p in pts]
        if max(signs)<=0:answer.add((*n,rhs))
        elif min(signs)>=0:answer.add((*(-x for x in n),-rhs))
    return sorted(answer)

FACETS=faces(LR)
assert len(FACETS)==7
assert all(sum(n[i]*p[i] for i in range(3))<=rhs for n0,n1,n2,rhs in FACETS for p in FULL for n in [(n0,n1,n2)])
expected={(-64,-64,-3,F(-67)),(-2,-3,0,F(-2)),(-2,-1,0,F(-1)),(0,0,1,F(3)),(2,1,0,F(2)),(2,3,0,F(3)),(64,64,-3,F(61))}
assert set(FACETS)==expected

f=lambda al,be,y:min(al*y,be)
for al,be,c in product((F(-3),F(-1),F(0),F(1,2),F(1),F(2),F(4)),repeat=3):
    d=2*f(al,be,1)-f(al,be,F(1,2))-f(al,be,F(3,2))
    assert d>=0
    ga,gb=a*d,b*d
    aa=(max(F(0),ga-c)+max(F(0),gb-c))/2
    bb=max(F(0),(ga+gb)/2-c)
    assert max(F(0),aa-c)==max(F(0),bb-c)

full=plus(action(F(1,2),K[0],('C',(1,0,0))),action(F(1,2),K[1],('P',None)))
x,q=F(3,4),F(8,9)
lr=(x*M[0]*Y[0]*q,(1-x)+x*(1-M[0]*q),(1-x)+3*x)
assert full==lr==(F(1,16),F(7,8),F(5,2))
assert F(1,2)*M[0]*F(1,2)==F(3,64)<F(1,16)
hi,lo,c=F(3,16),F(1,64),F(1,32)
AA=(max(F(0),hi-c)+max(F(0),lo-c))/2
BB=max(F(0),(hi+lo)/2-c)
assert max(F(0),AA-c)-max(F(0),BB-c)==F(1,128)
print('FULL_UNIQUE=77 LR_UNIQUE=12 FACES=7')
print('ALL_FULL_VERTICES_INSIDE_EXACT_LR_HULL=TRUE')
print('SIGNED_GRID=343 EXACT CASES PASSED')
print('FULL_TO_LR_WITNESS=(1/16,7/8,5/2,5/2)')
print('DIFFERENT_TIME_LAW=TRUE')
print('BELOW_THRESHOLD_GAP=1/128')
print('ALL EXACT CHECKS PASSED')
