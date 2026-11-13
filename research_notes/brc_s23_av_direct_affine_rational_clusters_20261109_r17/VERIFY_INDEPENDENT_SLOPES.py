#!/usr/bin/env python3
"""Independent exact finite experiments with a non-S23 irrational and near-rational slope."""
import math, csv, io, sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import VERIFY_DIRECT_AFFINE as r

Q=10**24
x=math.isqrt(2*Q*Q)
assert x*x<2*Q*Q<(x+1)**2


def exact_risk_by_sort(t,m,n):
    order=sorted(range(n),key=lambda i:(i*t)%1)
    ph=[(i*t)%1 for i in order]
    old=sorted(range(m),key=lambda i:(i*t)%1)
    points=[(i*t)%1 for i in old]
    mx=[F(0)]*m
    from bisect import bisect_right
    for j in range(n):
        p=ph[j];nextp=ph[(j+1)%n]
        gap=(nextp-p)%1
        k=bisect_right(points,p)-1
        if gap>mx[k]:mx[k]=gap
    return 1-sum(mx)


def verify_case(label,lo,hi,m,N,expected_single=False):
    r.LO,r.HI,r.M,r.N=lo,hi,m,N
    arr=r.history_members(m,N)
    n=m;epoch=r.farey_at_n(m)
    stream=io.StringIO()
    out=csv.writer(stream,delimiter='\t',lineterminator='\n')
    z=r.AffineEmitter(out,m,(0,0)); es=0; seg=0
    while n<=N:
        es+=1;a,b,c,d=epoch
        end=min(N,b+d);changes={n}
        for row in arr:
            t=b+row[0]+1
            if n<t<=end:changes.add(t)
            k=r.bisect.bisect_left(row,d)
            if k<len(row):
                t=row[k]+1
                if n<t<=end:changes.add(t)
            if k:
                t=b+row[k-1]+1
                if n<t<=end:changes.add(t)
        pts=sorted(changes)
        for j,p in enumerate(pts):
            q=pts[j+1]-1 if j+1<len(pts) else end
            z.take_constant_segment(p,q,r.risk_at(p,epoch,arr));seg+=1
        n=end+1
        if n<=N:epoch=r.advance(*epoch)
    z.finish()
    rows=[tuple(map(int,line.split('\t'))) for line in stream.getvalue().splitlines()]
    assert z.last_n==N
    for t in (lo,hi):
        for idx in sorted(set([m,m+1,m+2,m+8,m+31,m+71,m+127,N//2,N-1,N])):
            if idx<m or idx>N:continue
            row=next(x for x in rows if x[0]<=idx<=x[1]);n0,n1,a,b,da,db=row
            got=F(a+da*(idx-n0))+(b+db*(idx-n0))*t
            assert got==exact_risk_by_sort(t,m,idx),(label,idx,got,exact_risk_by_sort(t,m,idx))
    if expected_single:
        assert len(rows)==1,rows[:10]
        assert rows[0][:4]==(m,N,0,0)
        assert rows[0][4:]==(-1,2)
    print(label,'interval',str(lo),str(hi),'m',m,'nmax',N,'farey_epochs',es,'candidates',seg,'runs',len(rows),'checks',20,'final',z.last_v)
    return rows


if __name__=='__main__':
    a,b=F(x-Q,Q),F(x-Q+1,Q)
    verify_case('SQRT2_MINUS_1',a,b,17,3017)
    a,b=F(1,2)+F(x,Q*10**8), F(1,2)+F(x+1,Q*10**8)
    verify_case('NEAR_HALF_SQRT2',a,b,128,5128,expected_single=True)
    print('PASS_NON_S23_TWO_SLOPES_EXACT_TWO_ENDPOINT_BRUTE')
