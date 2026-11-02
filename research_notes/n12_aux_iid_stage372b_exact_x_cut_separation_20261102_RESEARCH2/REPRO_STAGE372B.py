#!/usr/bin/env python3
"""Stage372-B: Exact two-source X-cut separation certificate.

Bernoulli/BRC four audit-port auxiliary model: preserve all sixteen
provenance-distinct label differences; Fraction arithmetic only.
Science source pins: global main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419.

Optional: python REPRO_STAGE372B.py --emit CERTIFICATE_STAGE372B_X_CUT.csv
"""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import sys

W=(1,3,3,1); M=(61,21,9,9)
LAMBDA=F(6,5)
CUT=F(469,2000)
XLO=F(577,2500); XHI=F(239,1000)
YLO=F(27,50); YHI=F(59,100)
LEFT=(XLO,CUT,YLO,YHI)
RIGHT=(CUT,XHI,YLO,YHI)
LEFT_L_FLOOR=F(1873,50000)  # .03746
RIGHT_B_FLOOR=F(49,10000) # .0049
BUDGET_UP=F(61,6250)     # strict Stage369-B/370-B upper bound
CREF_UP=F(6319,100000)   # strict Stage369-B/370-B rational reference cost upper bound

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
def band(k,u,v):
    assert F(0)<=u<=v<=F(1)
    values=[B(k,u),B(k,v)]
    if u<F(k,3)<v:
        values.append(B(k,F(k,3)))
    return min(values),max(values)
def gap(v,lo,hi):
    return F(0) if lo<=v<=hi else min(abs(v-lo),abs(v-hi))
def bounds(x0,x1,y0,y1):
    X=[band(k,x0,x1) for k in range(4)]
    Y=[band(k,y0,y1) for k in range(4)]
    error_lower=F(5,32)*sum(W[k]*gap(F(M[k],160),
          (4*X[k][0]+Y[k][0])/5,
          (4*X[k][1]+Y[k][1])/5) for k in range(4))
    # Every port and outcome label remains distinct in this sum.
    ports=[]
    for a,q in ((F(1,4),X),(F(3,4),X),(F(1,4),Y),(F(3,4),Y)):
        ports.append(sum(W[k]*gap(B(k,a),q[k][0],q[k][1])
                         for k in range(4))/2)
    cost_lower=sum(coef*val for coef,val in zip((63,1,9,7),ports))/256
    return error_lower,cost_lower

def cover(tag,root,threshold,mode):
    stack=[(*root,0)]; rows=[]; splits=0
    while stack:
        x0,x1,y0,y1,depth=stack.pop()
        eb,ec=bounds(x0,x1,y0,y1)
        lower=ec+LAMBDA*eb if mode=='L' else eb
        if lower>threshold:
            rows.append((tag,depth,x0,x1,y0,y1,eb,ec,lower));continue
        assert depth<40,(tag,depth,x0,x1,y0,y1,lower)
        splits+=1
        if 5*(x1-x0)>=y1-y0:
            mid=(x0+x1)/2
            stack.extend(((x0,mid,y0,y1,depth+1),(mid,x1,y0,y1,depth+1)))
        else:
            mid=(y0+y1)/2
            stack.extend(((x0,x1,y0,mid,depth+1),(x0,x1,mid,y1,depth+1)))
    assert len(rows)==splits+1
    assert all(row[-1]>threshold for row in rows)
    assert sum((x1-x0)*(y1-y0) for _,_,x0,x1,y0,y1,*_ in rows)==(root[1]-root[0])*(root[3]-root[2])
    return rows,splits

# Reproduce the exact reference feasibility and source-independent budgets.
xl,xu=F(2310839,10**7),F(2310840,10**7)
yl,yu=F(5555086,10**7),F(5555091,10**7)
assert r(0,xl,yu)>0>r(0,xu,yl)
assert r(1,xl,yl)>0>r(1,xl,yu)
assert r(1,xu,yl)>0>r(1,xu,yu)
assert r(2,xl,yl)>0 and r(3,xu,yu)<0
bl=F(15,16)*r(2,xl,yl);bu=F(15,16)*r(2,xu,yu)
assert 2*bu+F(11,5000)<BUDGET_UP
P=(F(231138,10**6),F(555681,10**6))
Q=(F(237807,10**6),F(575694,10**6))
assert P[0]<CUT<Q[0]
assert b(*P)+b(*Q)<2*bl+F(11,5000)
assert c(*P)+c(*Q)==F(16174439790495832521,256000000000000000000)
assert c(*P)+c(*Q)<CREF_UP

# Explicit separation gaps: positive for every possible common-side pair.
GAP_LEFT=2*LEFT_L_FLOOR-LAMBDA*BUDGET_UP-CREF_UP
GAP_RIGHT=2*RIGHT_B_FLOOR-BUDGET_UP
assert GAP_LEFT==F(9,500000)
assert GAP_RIGHT==F(1,25000)
LEFT_ROWS,LEFT_SPLITS=cover('LEFT_X',LEFT,LEFT_L_FLOOR,'L')
RIGHT_ROWS,RIGHT_SPLITS=cover('RIGHT_X',RIGHT,RIGHT_B_FLOOR,'b')
assert (LEFT_SPLITS,len(LEFT_ROWS),max(row[1] for row in LEFT_ROWS))==(4199,4200,20)
assert (RIGHT_SPLITS,len(RIGHT_ROWS),max(row[1] for row in RIGHT_ROWS))==(50,51,14)

fr=lambda a: f'{a.numerator}/{a.denominator}'
columns='region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,target_lower'
lines=[columns]
for tag,depth,x0,x1,y0,y1,eb,ec,v in LEFT_ROWS+RIGHT_ROWS:
    lines.append(','.join((tag,str(depth),fr(x0),fr(x1),fr(y0),fr(y1),fr(eb),fr(ec),fr(v))))
certificate='\n'.join(lines)+'\n'
cert_bytes=certificate.encode('utf-8')
cert_sha=sha256(cert_bytes).hexdigest()
if len(sys.argv)==3 and sys.argv[1]=='--emit':
    Path(sys.argv[2]).write_bytes(cert_bytes)
else:
    assert len(sys.argv)==1
print('STAGE372B_EXACT_X_CUT_SEPARATION_PASS')
print('cut_x=',fr(CUT))
print('left_L_floor=',fr(LEFT_L_FLOOR),'right_b_floor=',fr(RIGHT_B_FLOOR))
print('left_splits=',LEFT_SPLITS,'left_leaves=',len(LEFT_ROWS),'left_max_depth=',max(row[1] for row in LEFT_ROWS))
print('right_splits=',RIGHT_SPLITS,'right_leaves=',len(RIGHT_ROWS),'right_max_depth=',max(row[1] for row in RIGHT_ROWS))
print('strict_left_two_source_cost_gap=',fr(GAP_LEFT))
print('strict_right_two_source_budget_deficit=',fr(GAP_RIGHT))
print('certificate_bytes=',len(cert_bytes),'certificate_sha256=',cert_sha)
