#!/usr/bin/env python3
"""Stage358-B: exact two-objective domination of a nonzero r0 tube.

Reads/regenerates the Stage357-B 71-leaf witness library, verifies its
interval partition, then builds a new exact finite certificate over
|r0|<=1/20000 and b<=299/50000 in the outer x ranges.
All arithmetic establishing the continuum claim is Fraction-only.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import csv
import hashlib
import subprocess
import sys

W = (1, 3, 3, 1)
M = (61, 21, 9, 9)
O, Z = F(1), F(0)
N = 10**10
EPS = F(1, 20000)
CAP = F(299, 50000)
LEFT = F(229, 1000)
RIGHT = F(233, 1000)


def B(k, z): return z**k * (1-z)**(3-k)
def r(k, x, y): return (4*B(k, x)+B(k, y))/5 - F(M[k], 160)
def b(x, y): return F(5, 32)*sum(W[k]*abs(r(k, x, y)) for k in range(4))
def D(a, z): return F(1, 2)*sum(W[k]*abs(B(k, a)-B(k, z)) for k in range(4))
def c(x, y): return (63*D(F(1, 4), x)+D(F(3, 4), x)+9*D(F(1, 4), y)+7*D(F(3, 4), y))/256


def add(u,v): return u[0]+v[0],u[1]+v[1]
def neg(u): return -u[1],-u[0]
def mul(u,v):
    z=[a*d for a in u for d in v]
    return min(z),max(z)
def scale(u,t): return (u[0]*t,u[1]*t) if t>=0 else (u[1]*t,u[0]*t)
def bi(k,u): return mul((u[0]**k,u[1]**k),((1-u[1])**(3-k),(1-u[0])**(3-k)))
def abs_lower(u): return max(Z,u[0],-u[1])


def cube_enclosure(t):
    assert 0<=t<=1
    lo,hi=0,N
    while lo+1<hi:
        mid=(lo+hi)//2
        if F(mid,N)**3<=t:lo=mid
        else:hi=mid
    return F(lo,N),F(lo+1,N)


def cell_bounds(xl,xh,eps):
    # r0=(4(1-x)^3+(1-y)^3)/5-61/160.
    low=F(61,32)-4*(1-xl)**3-5*eps
    high=F(61,32)-4*(1-xh)**3+5*eps
    if high<0 or low>1:return None
    tl,_=cube_enclosure(max(Z,low))
    _,th=cube_enclosure(min(O,high))
    X,Y=(xl,xh),(1-th,1-tl)
    def residual(k):
        return add(add(scale(bi(k,X),F(4,5)),scale(bi(k,Y),F(1,5))),(-F(M[k],160),-F(M[k],160)))
    blo=F(5,32)*sum(W[k]*abs_lower(residual(k)) for k in range(4))
    def dlow(a,V):
        return F(1,2)*sum(W[k]*abs_lower(add((B(k,a),B(k,a)),neg(bi(k,V)))) for k in range(4))
    clo=(63*dlow(F(1,4),X)+dlow(F(3,4),X)+9*dlow(F(1,4),Y)+7*dlow(F(3,4),Y))/256
    return blo,clo


def parent_witnesses():
    base=Path(__file__).resolve().parents[1] / 'enterprise_math_stage357b_20261101'
    # In a checkout, the Stage357 and Stage358 research dirs have another naming layout.
    if not base.exists():
        base=Path(__file__).resolve().parents[1] / 'n12_aux_iid_stage357b_outer_r0_pareto_exclusion_20261101_RESEARCH2'
    src=base/'CERTIFICATE_STAGE357B_OUTER_R0.csv'
    if not src.exists():
        checker=base/'REPRO_STAGE357B.py'
        assert checker.is_file(), f'Missing ancestor checker: {checker}'
        subprocess.run([sys.executable,str(checker)],check=True,capture_output=True,text=True)
    with src.open(newline='',encoding='utf-8') as fp:
        rows=list(csv.DictReader(fp))
    assert len(rows)==71
    for first,last in ((F(0),LEFT),(RIGHT,F(1))):
        cells=sorted((F(t['x_lo']),F(t['x_hi'])) for t in rows if first<=F(t['x_lo'])<last)
        assert cells and cells[0][0]==first and cells[-1][1]==last
        assert all(lo<hi for lo,hi in cells)
        assert all(cells[i][1]==cells[i+1][0] for i in range(len(cells)-1))
    options=set()
    for row in rows:
        lo,hi=F(row['x_lo']),F(row['x_hi'])
        old=cell_bounds(lo,hi,Z)
        cls=row['leaf_class']
        if cls=='NO_R0':assert old is None
        elif cls=='B_EXCLUDED':assert old is not None and old[0]>CAP
        elif cls=='DOMINATED':
            q=(F(row['witness_x']),F(row['witness_y']))
            assert all(Z<=v<=O for v in q)
            assert old is not None and b(*q)<old[0] and c(*q)<old[1]
            options.add(q)
        else:raise AssertionError(cls)
    assert len(options)==31
    return sorted(options)


def main():
    witnesses=parent_witnesses()
    options=[(q,b(*q),c(*q)) for q in witnesses]
    leaves=[]
    def classify(lo,hi,depth):
        out=cell_bounds(lo,hi,EPS)
        if out is None:
            leaves.append((lo,hi,'NO_TUBE',None,None,None,depth));return
        blo,clo=out
        if blo>CAP:
            leaves.append((lo,hi,'B_EXCLUDED',None,blo,clo,depth));return
        good=[(q,bq,cq) for q,bq,cq in options if bq<blo and cq<clo]
        if good:
            q,bq,cq=min(good,key=lambda t:(t[2],t[1],t[0]))
            leaves.append((lo,hi,'DOMINATED',q,blo,clo,depth));return
        assert depth<22, (lo,hi,depth,blo,clo)
        mid=(lo+hi)/2
        classify(lo,mid,depth+1)
        classify(mid,hi,depth+1)
    classify(Z,LEFT,0)
    classify(RIGHT,O,0)
    counts=Counter(e[2] for e in leaves)
    assert sum(e[1]-e[0] for e in leaves)==F(996,1000)
    for first,last in ((Z,LEFT),(RIGHT,O)):
        pairs=sorted((e[0],e[1]) for e in leaves if first<=e[0]<last)
        assert pairs[0][0]==first and pairs[-1][1]==last
        assert all(pairs[i][1]==pairs[i+1][0] for i in range(len(pairs)-1))
    for lo,hi,typ,q,blo,clo,_ in leaves:
        if typ=='NO_TUBE':assert cell_bounds(lo,hi,EPS) is None
        elif typ=='B_EXCLUDED':assert blo>CAP
        else:
            assert typ=='DOMINATED' and q and b(*q)<blo and c(*q)<clo
    b_gaps=[blo-b(*q) for _,_,t,q,blo,clo,_ in leaves if t=='DOMINATED']
    c_gaps=[clo-c(*q) for _,_,t,q,blo,clo,_ in leaves if t=='DOMINATED']
    budget_gaps=[blo-CAP for _,_,t,q,blo,clo,_ in leaves if t=='B_EXCLUDED']
    assert min(b_gaps)>0 and min(c_gaps)>0 and min(budget_gaps)>0
    target=Path(__file__).with_name('CERTIFICATE_STAGE358B_R0_TUBE.csv')
    with target.open('w',newline='',encoding='utf-8') as fp:
        csvw=csv.writer(fp)
        csvw.writerow(['x_low','x_high','class','witness_x','witness_y','b_lower','c_lower','depth'])
        for lo,hi,t,q,blo,clo,depth in leaves:
            csvw.writerow([str(lo),str(hi),t,str(q[0]) if q else '',str(q[1]) if q else '',str(blo) if blo is not None else '',str(clo) if clo is not None else '',depth])
    digest=hashlib.sha256(target.read_bytes()).hexdigest()
    print('STAGE358B_OUTER_R0_NONZERO_TUBE_EXACT_PASS')
    print('scope','all real x,y in [0,1]; x<=229/1000 or x>=233/1000; abs(r0)<=1/20000; b<=299/50000')
    print('leaves',len(leaves),'counts',dict(sorted(counts.items())),'max_depth',max(e[-1] for e in leaves))
    print('ancestor_witnesses',len(witnesses),'source_leaves',71)
    print('strict_margins_lower_bounds','min_b>',str(min(b_gaps)),'min_c>',str(min(c_gaps)),'min_b_exclusion>',str(min(budget_gaps)))
    print('certificate',target.name,'bytes',target.stat().st_size,'sha256',digest)
    print('status','PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED')
if __name__=='__main__':main()
