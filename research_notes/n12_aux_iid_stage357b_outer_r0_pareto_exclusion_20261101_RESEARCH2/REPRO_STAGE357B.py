#!/usr/bin/env python3
"""Exact rational interval certificate for outer r0=0 Pareto exclusion.
Reproduces 71 certified dyadic cells, no numerical sampling or float logic.
This is an external labeled Bernoulli observer, not native X6/BRC–Shor.
"""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import csv

W = (1, 3, 3, 1)
M = (61, 21, 9, 9)
O, Z = F(1), F(0)
N = 10**10

def B(k, z): return z**k * (1-z)**(3-k)
def r(k, x, y): return (4*B(k,x)+B(k,y))/5 - F(M[k],160)
def b(x, y): return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def D(a, z): return sum(F(W[k],2)*abs(B(k,a)-B(k,z)) for k in range(4))
def c(x, y): return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256

def crfloor(v):
    assert 0 <= v <= 1
    lo, hi = 0, N
    while lo+1 < hi:
        m = (lo+hi)//2
        if F(m,N)**3 <= v: lo = m
        else: hi = m
    return F(lo,N), F(lo+1,N)

def add(a,v): return (a[0]+v[0],a[1]+v[1])
def neg(a): return (-a[1],-a[0])
def mul(a,v):
    q = [u*w for u in a for w in v]
    return min(q),max(q)
def scale(a,k):return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def powi(a,k):
    assert a[0]>=0
    return (a[0]**k,a[1]**k)
def bi(k,z): return mul(powi(z,k),powi(add((O,O),neg(z)),3-k))
def abslo(a):return max(Z,a[0],-a[1])

def cell_bounds(xl,xh):
    t3lo = F(61,32)-4*(1-xl)**3
    t3hi = F(61,32)-4*(1-xh)**3
    if t3hi<0 or t3lo>1: return None
    tl,_=crfloor(max(Z,t3lo))
    _,th=crfloor(min(O,t3hi))
    X,Y=(xl,xh),(1-th,1-tl)
    def residue(k):
        return add(add(scale(bi(k,X),F(4,5)),scale(bi(k,Y),F(1,5))),(-F(M[k],160),-F(M[k],160)))
    blo=F(5,32)*sum(W[k]*abslo(residue(k)) for k in range(4))
    def dlow(a,V):
        return F(1,2)*sum(W[k]*abslo(add((B(k,a),B(k,a)),neg(bi(k,V)))) for k in range(4))
    clo=(63*dlow(F(1,4),X)+dlow(F(3,4),X)+9*dlow(F(1,4),Y)+7*dlow(F(3,4),Y))/256
    return blo,clo,Y

def near_r1_zero_y(x):
    l,h=F(1,2),F(3,4)
    assert r(1,x,l)>0>r(1,x,h)
    for _ in range(38):
        mid=(l+h)/2
        if r(1,x,mid)>0:l=mid
        else:h=mid
    return (l+h)/2

LEFT=(F('0.2310839408555'),F('0.555508857277'))
CAND=[]
for i in range(232000,245001,50):
    x=F(i,10**6)
    y=near_r1_zero_y(x)
    CAND.append((x,y,b(x,y),c(x,y)))
LEAVES=[]

def certify(lo,hi,depth=0):
    bounds=cell_bounds(lo,hi)
    if bounds is None:
        LEAVES.append((lo,hi,'NO_R0',None,None,None,depth));return
    blo,clo,_=bounds
    if blo>F(299,50000):
        LEAVES.append((lo,hi,'B_EXCLUDED',None,blo,clo,depth));return
    if hi<=F(229,1000):
        if blo>b(*LEFT) and clo>c(*LEFT):
            LEAVES.append((lo,hi,'DOMINATED',LEFT,blo,clo,depth));return
    else:
        matches=[q for q in CAND if q[2]<blo and q[3]<clo]
        if matches:
            q=min(matches,key=lambda z:z[3])
            LEAVES.append((lo,hi,'DOMINATED',q[:2],blo,clo,depth));return
    assert depth<23, ('failed cell',lo,hi,blo,clo)
    mid=(lo+hi)/2
    certify(lo,mid,depth+1)
    certify(mid,hi,depth+1)

def main():
    certify(F(0),F(229,1000))
    certify(F(233,1000),F(1))
    counts=Counter((('LEFT' if e[0]<F(229,1000) else 'RIGHT')+'_'+e[2]) for e in LEAVES)
    assert len(LEAVES)==71 and max(e[-1] for e in LEAVES)==13
    assert counts=={'LEFT_NO_R0':4,'LEFT_B_EXCLUDED':1,'LEFT_DOMINATED':15,'RIGHT_NO_R0':2,'RIGHT_B_EXCLUDED':18,'RIGHT_DOMINATED':31},counts
    # End-to-end exact interval partition, strictness, all 16 signed-subset labels:
    assert sum(e[1]-e[0] for e in LEAVES)==F(996,1000)
    assert all(blo>b(*q) and clo>c(*q) for _,_,status,q,blo,clo,_ in LEAVES if status=='DOMINATED')
    assert all(blo>F(299,50000) for _,_,status,_,blo,_,_ in LEAVES if status=='B_EXCLUDED')
    output=Path(__file__).with_name('CERTIFICATE_STAGE357B_OUTER_R0.csv')
    with output.open('w',newline='',encoding='utf-8') as fh:
        writer=csv.writer(fh)
        writer.writerow(['x_lo','x_hi','leaf_class','witness_x','witness_y','b_lower','c_lower','depth'])
        for lo,hi,status,q,blo,clo,depth in LEAVES:
            writer.writerow([str(lo),str(hi),status,str(q[0]) if q else '',str(q[1]) if q else '',str(blo) if blo is not None else '',str(clo) if clo is not None else '',depth])
    print('STAGE357B_OUTER_R0_EXACT_INTERVAL_PARETO_EXCLUSION_PASS')
    print('n_leaves',len(LEAVES),'counts',dict(sorted(counts.items())),'max_depth',max(e[-1] for e in LEAVES))
    print('witness_grid',len(CAND),'candidate_x_range',CAND[0][0],CAND[-1][0])
    print('coverage', '[0,229/1000] union [233/1000,1] ; r0=0; b<=299/50000')
    print('strict_outcome', 'each outer point replaced by rational Q with both b(Q)<b and c(Q)<c')
    print('certificate',output.name,'nonempty_bytes',output.stat().st_size)
    print('scope', '16 labeled TV-subset comparisons, four original audit channels; no P000/X6 mapping')
    print('status','PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED')

if __name__=='__main__':main()
