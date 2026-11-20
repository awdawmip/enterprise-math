#!/usr/bin/env python3
"""Stage370-B: full-real, continuous two-sided y-strip elimination, exact rational boxes.

Scientific frozen inputs: Stage369-B, 16 provenance-distinct original labels, 4 audit channels.
No floating-point arithmetic or interval rounding; all bounds use fractions.
"""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from collections import Counter
import sys

w=(1,3,3,1)
m=(61,21,9,9)
lam=F(6,5)
R=(F(219,1000),F(239,1000),F(51,100),F(16,25))
LO=(R[0],R[1],R[2],F(27,50))      # y <= 0.54
HI=(R[0],R[1],F(59,100),R[3])     # y >= 0.59
THR_LO=F(3767,100000)             # 0.03767
THR_HI=F(3795,100000)             # 0.03795
R_BOUND=F(373,10000)              # Stage369-B exact 1191-leaf global lower bound
BUDGET_UP=F(61,6250)              # Stage369-B strict source-relative budget upper bound
CREF_UP=F(6319,100000)            # Stage369-B rational feasible reference upper bound

@lru_cache(None)
def B(k,z): return z**k*(1-z)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(m[k],160)
def b(x,y):return F(5,32)*sum(w[k]*abs(r(k,x,y)) for k in range(4))
def d(a,z):return sum(w[k]*abs(B(k,a)-B(k,z)) for k in range(4))/2
def c(x,y):return (63*d(F(1,4),x)+d(F(3,4),x)+9*d(F(1,4),y)+7*d(F(3,4),y))/256

@lru_cache(None)
def band(k,a,z):
    values=[B(k,a),B(k,z)]
    if a<F(k,3)<z:values.append(B(k,F(k,3)))
    return min(values),max(values)
def gap(v,lo,hi):return F(0) if lo<=v<=hi else min(abs(v-lo),abs(v-hi))
def lb(x0,x1,y0,y1):
    X=[band(k,x0,x1) for k in range(4)]
    Y=[band(k,y0,y1) for k in range(4)]
    eb=F(5,32)*sum(w[k]*gap(F(m[k],160),(4*X[k][0]+Y[k][0])/5,(4*X[k][1]+Y[k][1])/5) for k in range(4))
    port=[sum(w[k]*gap(B(k,a),q[k][0],q[k][1]) for k in range(4))/2 for a,q in ((F(1,4),X),(F(3,4),X),(F(1,4),Y),(F(3,4),Y))]
    ec=sum(i*j for i,j in zip((63,1,9,7),port))/256
    return eb,ec

def cover(tag,rect,target):
    stack=[(*rect,0)];out=[];splits=0
    while stack:
        x0,x1,y0,y1,depth=stack.pop()
        eb,ec=lb(x0,x1,y0,y1);v=ec+lam*eb
        if v>target:
            out.append((tag,depth,x0,x1,y0,y1,eb,ec,v));continue
        if depth>=40: raise AssertionError(f'Unclosed {tag} depth {depth}: {x0,x1,y0,y1,v}')
        splits+=1
        if 5*(x1-x0)>=y1-y0:
            mid=(x0+x1)/2
            stack.extend([(x0,mid,y0,y1,depth+1),(mid,x1,y0,y1,depth+1)])
        else:
            mid=(y0+y1)/2
            stack.extend([(x0,x1,y0,mid,depth+1),(x0,x1,mid,y1,depth+1)])
    assert len(out)==splits+1
    assert all(row[-1]>target for row in out)
    return out,splits

# Revalidate exact reference and the strict budget bound used with Stage369-B.
xl,xu=F(2310839,10**7),F(2310840,10**7)
yl,yu=F(5555086,10**7),F(5555091,10**7)
assert r(0,xl,yu)>0>r(0,xu,yl)
assert r(1,xl,yl)>0>r(1,xl,yu)
assert r(1,xu,yl)>0>r(1,xu,yu)
assert r(2,xl,yl)>0 and r(3,xu,yu)<0
bl=F(15,16)*r(2,xl,yl);bu=F(15,16)*r(2,xu,yu)
assert 2*bu+F(11,5000)<BUDGET_UP
P=(F(231138,10**6),F(555681,10**6));Q=(F(237807,10**6),F(575694,10**6))
assert b(*P)+b(*Q)<2*bl+F(11,5000)
assert c(*P)+c(*Q)==F(16174439790495832521,256000000000000000000)
assert c(*P)+c(*Q)<CREF_UP
assert R_BOUND + THR_LO - lam*BUDGET_UP - CREF_UP==F(17,250000)  # .000068
assert R_BOUND + THR_HI - lam*BUDGET_UP - CREF_UP==F(87,250000)  # .000348

BASE,NBASE=cover('R_GLOBAL',R,R_BOUND)
assert (NBASE,len(BASE),max(z[1] for z in BASE))==(1190,1191,16)
LOW,NLOW=cover('LOW_Y',LO,THR_LO)
HIGH,NHIGH=cover('HIGH_Y',HI,THR_HI)
fr=lambda x:f'{x.numerator}/{x.denominator}'
rows=['region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower']
for tag,depth,x0,x1,y0,y1,eb,ec,L in LOW+HIGH:
    rows.append(','.join((tag,str(depth),fr(x0),fr(x1),fr(y0),fr(y1),fr(eb),fr(ec),fr(L))))
csv='\n'.join(rows)+'\n'
sha=sha256(csv.encode('utf-8')).hexdigest()
if len(sys.argv)==3 and sys.argv[1]=='--emit':Path(sys.argv[2]).write_bytes(csv.encode('utf-8'))
else:assert len(sys.argv)==1
assert (NLOW,len(LOW),max(z[1] for z in LOW))==(1661,1662,17)
assert (NHIGH,len(HIGH),max(z[1] for z in HIGH))==(94,95,15)
assert sha=='b21fe204b5baa2485dfb08d529cd9a003f2491caf83d2e27012cb83b8dab58a0'
assert len(csv.encode('utf-8'))==257043
print('STAGE370B_EXACT_TWO_SIDED_Y_STRIP_EXCLUSION_PASS')
print('R_GLOBAL_splits=',NBASE,'R_GLOBAL_leaves=',len(BASE),'R_GLOBAL_depth=',max(row[1] for row in BASE))
print('LOW_Y_splits=',NLOW,'LOW_Y_leaves=',len(LOW),'LOW_Y_depth=',max(row[1] for row in LOW))
print('HIGH_Y_splits=',NHIGH,'HIGH_Y_leaves=',len(HIGH),'HIGH_Y_depth=',max(row[1] for row in HIGH))
print('minimum_strict_cost_gaps=17/250000,87/250000')
print('certificate_bytes=',len(csv.encode('utf-8')),'certificate_sha256=',sha)
