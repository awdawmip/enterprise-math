#!/usr/bin/env python3
"""Stage373-B: exact rational interval certificate for right-source y centrality.

External 16 provenance-labelled Bernoulli/BRC auxiliary observer only.
Frozen scientific pins: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419.
Run: python REPRO_STAGE373B.py [--emit <certificate.csv>]
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from pathlib import Path
from hashlib import sha256
import sys

W=(1,3,3,1); M=(61,21,9,9)
LAM=F(6,5)
CUT=F(469,2000)
CORE_X=(F(577,2500),F(239,1000))
CORE_Y=(F(27,50),F(59,100))
LEFT=(CORE_X[0],CUT,*CORE_Y)
Q_LOW=(CUT,CORE_X[1],CORE_Y[0],F(57,100))
Q_HIGH=(CUT,CORE_X[1],F(29,50),CORE_Y[1])
FLOOR_LEFT=F(1873,50000)
FLOOR_Q_LOW=F(37443,1000000)
FLOOR_Q_HIGH=F(37445,1000000)
BUDGET_UP=F(61,6250)
CREF_UP=F(6319,100000)

@lru_cache(None)
def B(k,z):
    return z**k*(1-z)**(3-k)

def r(k,x,y):
    return (4*B(k,x)+B(k,y))/5-F(M[k],160)

def b(x,y):
    return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))

def d(a,z):
    return sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))/2

def c(x,y):
    return (63*d(F(1,4),x)+d(F(3,4),x)+9*d(F(1,4),y)+7*d(F(3,4),y))/256

@lru_cache(None)
def cubic_range(k,lo,hi):
    # The only possible interior critical point of B_k is k/3.
    v=[B(k,lo),B(k,hi)]
    if lo<F(k,3)<hi:
        v.append(B(k,F(k,3)))
    return min(v),max(v)

def distance_lower(target,lo,hi):
    if lo<=target<=hi:
        return F(0)
    return min(abs(target-lo),abs(target-hi))

def lower_bounds(x0,x1,y0,y1):
    X=[cubic_range(k,x0,x1) for k in range(4)]
    Y=[cubic_range(k,y0,y1) for k in range(4)]
    eb=F(5,32)*sum(W[k]*distance_lower(
        F(M[k],160), (4*X[k][0]+Y[k][0])/5,
        (4*X[k][1]+Y[k][1])/5) for k in range(4))
    # Four physical audit ports, retaining all 16 provenance labels.
    ports=[sum(W[k]*distance_lower(B(k,a),q[k][0],q[k][1])
               for k in range(4))/2
           for a,q in ((F(1,4),X),(F(3,4),X),
                       (F(1,4),Y),(F(3,4),Y))]
    ec=sum(weight*port for weight,port in zip((63,1,9,7),ports))/256
    return eb,ec

def cover(tag,rectangle,threshold):
    stack=[(*rectangle,0)]
    rows=[];splits=0
    while stack:
        x0,x1,y0,y1,depth=stack.pop()
        eb,ec=lower_bounds(x0,x1,y0,y1)
        bound=ec+LAM*eb
        if bound>threshold:
            rows.append((tag,depth,x0,x1,y0,y1,eb,ec,bound))
            continue
        assert depth<40, (tag,depth,x0,x1,y0,y1,bound)
        splits+=1
        if 5*(x1-x0)>=y1-y0:
            mid=(x0+x1)/2
            stack.extend(((x0,mid,y0,y1,depth+1),
                          (mid,x1,y0,y1,depth+1)))
        else:
            mid=(y0+y1)/2
            stack.extend(((x0,x1,y0,mid,depth+1),
                          (x0,x1,mid,y1,depth+1)))
    assert len(rows)==splits+1
    assert all(row[8]>threshold for row in rows)
    assert sum(((row[3]-row[2])*(row[5]-row[4]) for row in rows),F(0)) == (rectangle[1]-rectangle[0])*(rectangle[3]-rectangle[2])
    return rows,splits

def frac(x):
    return f'{x.numerator}/{x.denominator}'

# q* bracket and exact rational feasible comparison from Stage372-B.
xl,xu=F(2310839,10**7),F(2310840,10**7)
yl,yu=F(5555086,10**7),F(5555091,10**7)
assert r(0,xl,yu)>0>r(0,xu,yl)
assert r(1,xl,yl)>0>r(1,xl,yu)
assert r(1,xu,yl)>0>r(1,xu,yu)
assert r(2,xl,yl)>0 and r(3,xu,yu)<0
beta_lower=F(15,16)*r(2,xl,yl)
beta_upper=F(15,16)*r(2,xu,yu)
assert 2*beta_upper+F(11,5000)<BUDGET_UP
P0=(F(231138,10**6),F(555681,10**6))
Q0=(F(237807,10**6),F(575694,10**6))
assert P0[0]<CUT<Q0[0]
assert b(*P0)+b(*Q0)<2*beta_lower+F(11,5000)
assert c(*P0)+c(*Q0)==F(16174439790495832521,256000000000000000000)
assert c(*P0)+c(*Q0)<CREF_UP

margin_low=FLOOR_LEFT+FLOOR_Q_LOW-LAM*BUDGET_UP-CREF_UP
margin_high=FLOOR_LEFT+FLOOR_Q_HIGH-LAM*BUDGET_UP-CREF_UP
assert margin_low==F(1,1000000)
assert margin_high==F(3,1000000)

lhs,ns_left=cover('LEFT_X',LEFT,FLOOR_LEFT)
low,ns_low=cover('RIGHT_Y_LE_57_100',Q_LOW,FLOOR_Q_LOW)
high,ns_high=cover('RIGHT_Y_GE_29_50',Q_HIGH,FLOOR_Q_HIGH)
assert (len(lhs),len(low),len(high))==(4200,4258,86)
assert (ns_left,ns_low,ns_high)==(4199,4257,85)
rows=lhs+low+high
lines=['region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower']
for row in rows:
    region,depth,*nums=row
    lines.append(','.join([region,str(depth),*(frac(q) for q in nums)]))
raw=('\n'.join(lines)+'\n').encode('utf-8')
if len(sys.argv)==3 and sys.argv[1]=='--emit':
    Path(sys.argv[2]).write_bytes(raw)
else:
    assert len(sys.argv)==1
print('STAGE373B_EXACT_RIGHT_Y_CENTRAL_BAND_PASS')
print('left_leaves=',len(lhs),'low_leaves=',len(low),'high_leaves=',len(high),'total_leaves=',len(rows))
print('left_max_depth=',max(z[1] for z in lhs),'low_max_depth=',max(z[1] for z in low),'high_max_depth=',max(z[1] for z in high))
print('exact_strict_cost_gaps=',frac(margin_low),frac(margin_high))
print('right_y_necessary=57/100<y_Q<29/50')
print('certificate_bytes=',len(raw),'certificate_sha256=',sha256(raw).hexdigest())
