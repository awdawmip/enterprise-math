"""Exact Fraction certificate for finite two-merger source-route-sensitive model."""
from fractions import Fraction as F
from itertools import product

ZERO=F(0);ONE=F(1)
R=(F(1,2),ONE,F(3,2))
ROUTES={'L':(F(1,2),F(1,3)),'R':(F(3,2),F(5,3))}
U={('A','L'):F(1,32),('A','R'):F(3,32),('B','L'):F(13,32),('B','R'):F(15,32)}
N=(ONE,ONE,-F(1,16),ZERO)
def obs(q,r,t,a):
    return (q*r if a=='Q' else ZERO,q if a=='P' else ZERO,t*q*r,t*q)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def dot(n,v):return sum((a*b for a,b in zip(n,v)),ZERO)
def path_weights():
    for s,route in product(('A','B'),('L','R')):
        rr,side=ROUTES[route]
        qr=F(1,4)
        yield s,route,'M',qr*F(1,4),ONE
        yield s,route,'S',qr*F(3,4),side

for u in U.values():
    Q=(u,ONE-2*u,u)
    assert all(q>0 for q in Q)
    assert sum(Q,ZERO)==ONE
    assert sum((p*r for p,r in zip(Q,R)),ZERO)==ONE
for route,(rr,side) in ROUTES.items():
    assert F(1,4)*ONE+F(3,4)*side==rr
assert sum((q for s,route,node,q,r in path_weights()),ZERO)==ONE

def run(root,side,merge,term):
    out=(ZERO,)*4
    for s in ('A','B'):
        if root[s]!='C':
            out=add(out,obs(F(1,2),ONE,1,root[s]))
    for s,route,node,q,r in path_weights():
        if root[s]!='C':continue
        if node=='S':
            out=add(out,obs(q,r,3,side[(s,route)]))
        else:
            a=merge[(s,route)]
            if a!='C':out=add(out,obs(q,ONE,3,a))
            else:
                u=U[(s,route)]
                for rr,p in zip(R,(u,ONE-2*u,u)):
                    out=add(out,obs(q*p,rr,4,term[(s,route,rr)]))
    return out

ROOT={s:'C' for s in ('A','B')}
SIDE={(s,route):('P' if route=='L' else 'Q') for s,route in product(('A','B'),('L','R'))}
MERGE={(s,route):('P' if s=='A' else 'C') for s,route in product(('A','B'),('L','R'))}
TERM={(s,route,r):('Q' if r>ONE else 'P') for s,route,r in product(('A','B'),('L','R'),R)}
W=run(ROOT,SIDE,MERGE,TERM)
assert W==(F(181,256),F(73,128),F(25,8),F(25,8))

scores=[]
for t1,l,r,m,decisions in product(('P','Q','C'),('P','Q'),('P','Q'),('P','Q','C'),product(('P','Q'),repeat=3)):
    a={s:t1 for s in ('A','B')}
    b={(s,route):(l if route=='L' else r) for s,route in product(('A','B'),('L','R'))}
    c={(s,route):m for s,route in product(('A','B'),('L','R'))}
    d={(s,route,rr):decisions[i] for s,route in product(('A','B'),('L','R')) for i,rr in enumerate(R)}
    scores.append((dot(N,run(a,b,c,d)),(t1,l,r,m,decisions)))
assert len(scores)==288
hlr,policy=max(scores,key=lambda e:e[0])
assert hlr==F(69,64)
assert dot(N,W)==F(277,256)

stop=F(13,16)
cont=lambda u:F(3,4)+u/2
side=F(55,64)
hfull=side+sum((F(1,16)*max(stop,cont(u)) for u in U.values()),ZERO)
hseed=side+F(1,4)*max(stop,sum((cont(u) for u in U.values()),ZERO)/4)
jensen=(sum((max(ZERO,u-F(1,8)) for u in U.values()),ZERO)-max(ZERO,sum(U.values(),ZERO)-F(1,2)))/32
gap=dot(N,W)-hlr
assert hfull==dot(N,W) and hseed==hlr and gap==jensen==F(1,256)
dist=gap/sum((abs(x) for x in N),ZERO)
assert dist==F(1,528)
print('N=',N)
print('U=',U)
print('W=',W)
print('FULL_EXACT_SUPPORT=',hfull)
print('LR_DETERMINISTIC_POLICIES=',len(scores))
print('LR_EXACT_SUPPORT=',hseed)
print('LR_MAX_POLICY=',policy)
print('EXACT_GAP=',gap)
print('JENSEN_FORMULA=',jensen)
print('LINF_DISTANCE_LOWER_BOUND=',dist)
print('PASS_EXACT_R5_SOURCE_ROUTE_TWO_MERGER_JENSEN_SEPARATOR')
