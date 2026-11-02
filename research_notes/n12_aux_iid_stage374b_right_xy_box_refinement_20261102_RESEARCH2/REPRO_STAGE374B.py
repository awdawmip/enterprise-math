#!/usr/bin/env python3
"""Stage374-B exact rational continuous-domain y-band refinement.

Scientific source pins (unchanged):
GLOBAL main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53
Enterprise Math main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419
P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488

16 original provenance-labelled comparisons via four independent audit ports.
All bounds and comparisons use fractions; the generated CSV is a closed-box
certificate for the entire indicated real rectangle, not a point sample.
"""
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import argparse
from pathlib import Path

w=(1,3,3,1); m=(61,21,9,9)
lam=F(6,5)
A=F(37464,10**6)
BMIN=F(37431,10**6)
BUDGET_UP=F(61,6250)
CREF_UP=F(63182,10**6)
# Stage373-B ordered domain; Stage374-B new thin excluded slices.
LEFT=(F(577,2500),F(469,2000),F(27,50),F(59,100))
RIGHT_LO=(F(469,2000),F(239,1000),F(57,100),F(143,250))     # y in [0.57,0.572]
RIGHT_HI=(F(469,2000),F(239,1000),F(2897,5000),F(29,50))   # y in [0.5794,0.58]
RIGHT_X_LO=(F(469,2000),F(473,2000),F(143,250),F(2897,5000)) # x in [0.2345,0.2365]

@lru_cache(None)
def B(k,z): return z**k*(1-z)**(3-k)
def r(k,x,y): return (4*B(k,x)+B(k,y))/5-F(m[k],160)
def b(x,y):return F(5,32)*sum(w[k]*abs(r(k,x,y)) for k in range(4))
def d(a,z):return sum(w[k]*abs(B(k,a)-B(k,z)) for k in range(4))/2
def c(x,y):return (63*d(F(1,4),x)+d(F(3,4),x)+9*d(F(1,4),y)+7*d(F(3,4),y))/256

@lru_cache(None)
def band(k,a,z):
    values=[B(k,a),B(k,z)]
    critical=F(k,3)
    if a<critical<z: values.append(B(k,critical))
    return min(values),max(values)
def gap(target,lo,hi):return F(0) if lo<=target<=hi else min(abs(target-lo),abs(target-hi))

def lb(x0,x1,y0,y1):
    X=[band(k,x0,x1) for k in range(4)]
    Y=[band(k,y0,y1) for k in range(4)]
    eb=F(5,32)*sum(w[k]*gap(F(m[k],160),(4*X[k][0]+Y[k][0])/5,(4*X[k][1]+Y[k][1])/5) for k in range(4))
    ports=[]
    for anchor,rrange in ((F(1,4),X),(F(3,4),X),(F(1,4),Y),(F(3,4),Y)):
        ports.append(sum(w[k]*gap(B(k,anchor),rrange[k][0],rrange[k][1]) for k in range(4))/2)
    ec=sum(h*port for h,port in zip((63,1,9,7),ports))/256
    return eb,ec

def cover(tag,rect,target,leaves):
    stack=[(*rect,0)]; nsplit=0; nleaf=0; maxdep=0; min_margin=None; area=F(0)
    while stack:
        x0,x1,y0,y1,depth=stack.pop()
        eb,ec=lb(x0,x1,y0,y1); L=ec+lam*eb
        if L>target:
            nleaf+=1; maxdep=max(maxdep,depth)
            margin=L-target
            if min_margin is None or margin<min_margin: min_margin=margin
            area+=(x1-x0)*(y1-y0)
            leaves.append((tag,depth,x0,x1,y0,y1,eb,ec,L))
            continue
        assert depth<40, ('UNRESOLVED',tag,depth,x0,x1,y0,y1,L)
        nsplit+=1
        if 5*(x1-x0)>=y1-y0:
            mid=(x0+x1)/2
            stack.extend([(x0,mid,y0,y1,depth+1),(mid,x1,y0,y1,depth+1)])
        else:
            mid=(y0+y1)/2
            stack.extend([(x0,x1,y0,mid,depth+1),(x0,x1,mid,y1,depth+1)])
    assert nleaf==nsplit+1
    assert area==(rect[1]-rect[0])*(rect[3]-rect[2])
    return dict(tag=tag,splits=nsplit,leaves=nleaf,maxdepth=maxdep,strict_margin=min_margin)

def check_root_and_reference():
    # The P000/external model frozen pin and original Stage370 verification
    # identify the unique beta* = b(q*) by a rational monotonic root isolator.
    xl,xu=F(2310839,10**7),F(2310840,10**7)
    yl,yu=F(5555086,10**7),F(5555091,10**7)
    assert r(0,xl,yu)>0>r(0,xu,yl)
    assert r(1,xl,yl)>0>r(1,xl,yu)
    assert r(1,xu,yl)>0>r(1,xu,yu)
    assert r(2,xl,yl)>0 and r(3,xu,yu)<0
    # At simultaneous r0=r1=0, sum_k w_k r_k=0; with r2>0,r3<0,
    # b(q*)=(15/16)r2(q*). r2 is increasing in both x,y here.
    bstarlo=F(15,16)*r(2,xl,yl)
    bstarhi=F(15,16)*r(2,xu,yu)
    assert 2*bstarhi+F(11,5000)<BUDGET_UP
    P=(F(231138,10**6),F(555681,10**6))
    Q=(F(237807,10**6),F(575694,10**6))
    assert b(*P)+b(*Q)<2*bstarlo+F(11,5000)
    assert c(*P)+c(*Q)==F(16174439790495832521,256000000000000000000)
    assert c(*P)+c(*Q)<CREF_UP
    assert A+BMIN-lam*BUDGET_UP-CREF_UP==F(1,10**6)
    # The 16 comparisons have been handled as four independently signed
    # per-port sums, not collapsed into an unlabeled aggregate. Exact b,c
    # on the reference and interval distance in lb enforce that.
    return P,Q

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--emit',type=Path,help='write complete certificate CSV')
    a=ap.parse_args()
    P,Q=check_root_and_reference()
    leaves=[]
    stats=[cover('LEFT',LEFT,A,leaves),cover('RIGHT_LO',RIGHT_LO,BMIN,leaves),cover('RIGHT_HI',RIGHT_HI,BMIN,leaves),cover('RIGHT_X_LO',RIGHT_X_LO,BMIN,leaves)]
    fr=lambda x:f'{x.numerator}/{x.denominator}'
    header='region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower\n'
    csv=header+''.join(','.join([tag,str(depth),*(fr(z) for z in (x0,x1,y0,y1,eb,ec,L))])+'\n' for tag,depth,x0,x1,y0,y1,eb,ec,L in leaves)
    digest=sha256(csv.encode()).hexdigest()
    if a.emit:
        a.emit.write_bytes(csv.encode('utf-8'))
        assert a.emit.read_bytes()==csv.encode()
    print('STAGE374B_EXACT_RIGHT_XY_BOX_REFINEMENT_PASS')
    print('budget_E=11/5000;_R2_candidate=(231138/1000000,555681/1000000),(237807/1000000,575694/1000000)')
    print('L_LEFT>37464/1000000; L_RIGHT_SLICES>37431/1000000')
    print('strict_cost_gap_over_rational_feasible_comparator>1/1000000')
    for s in stats:print('region',s['tag'],'splits',s['splits'],'leaves',s['leaves'],'maxdepth',s['maxdepth'],'min_strict_margin',fr(s['strict_margin']))
    print('total_leaves',len(leaves),'csv_bytes',len(csv.encode()),'csv_sha256',digest)
