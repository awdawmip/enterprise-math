"""PREFIX-719: exact frozen Gamma maximum, diagonal stationary interval.
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json,hashlib
from pathlib import Path
N,D,W=189,768,1<<18
@lru_cache(None)
def inside(m,k,x):
    return 40*(m+1)*comb(m,k)*x**k*(W-x)**(m-k)>W**m
@lru_cache(None)
def wide(m,k):
    if k>m//2:return wide(m,m-k)
    mid=k*W//m
    assert inside(m,k,mid)
    if k==0: l0=l1=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(m,k,x):hi=x
            else:lo=x
        l0,l1=lo,hi
    lo,hi=mid,W
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(m,k,x):lo=x
        else:hi=x
    if 4*(lo-l1)>W:return True
    if 4*(hi-l0)<W:return False
    raise ValueError('ambiguous frozen width predicate')
rows=[{0:1}]
for m in range(1,N+1):
    new=defaultdict(int)
    for k,v in rows[-1].items():new[k]+=v;new[k+1]+=v
    rows.append({k:v for k,v in new.items() if wide(m,k)})
assert not rows[-1] and sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}
L,Z=D**(N-1),2**(2*N-1)
R=L*L*Z
@lru_cache(None)
def tail(i):
    a,b=i,D-i; pa=[1];pb=[1]
    for _ in range(N):pa.append(pa[-1]*a);pb.append(pb[-1]*b)
    return tuple(sum(v*pa[k]*pb[n-k] for k,v in row.items())*D**(N-1-n)
                 for n,row in enumerate(rows[:N]))
@lru_cache(None)
def dtail(i):
    a,b=i,D-i;pa=[1];pb=[1]
    for _ in range(N):pa.append(pa[-1]*a);pb.append(pb[-1]*b)
    return tuple(sum(v*((k*pa[k-1]*pb[n-k] if k else 0)-
                        ((n-k)*pa[k]*pb[n-k-1] if n>k else 0))
                     for k,v in row.items())*D**(N-n)
                 for n,row in enumerate(rows[:N]))
@lru_cache(None)
def influence(j):
    terms=[(m,v) for m,v in enumerate(tail(j)) if v]
    a=[];h=[]
    for n in range(N):
        cs=[(m,v,comb(n+m,n)*2**(2*N-2-n-m)) for m,v in terms]
        a.append(L*Z-sum(v*c for m,v,c in cs))
        h.append(2*(n+1)*L*Z-sum((n+m+1)*v*c for m,v,c in cs))
    assert min(a)>0 and min(h)>0
    return a,h
@lru_cache(None)
def mu(i,j):
    ai,_=influence(j)
    return F(sum(tail(i))+sum(tail(j)),L)-F(sum(x*(L*Z-y) for x,y in zip(tail(i),ai)),R)
@lru_cache(None)
def ratio(i,j):
    a,h=influence(j);s=dtail(i)
    den=sum(x*y for x,y in zip(s,a))
    num=sum(x*y for x,y in zip(s,h))
    assert den>0
    return F(num,den)
def run():
    lo,hi=86,91
    tl=ratio(lo,lo)-2*mu(lo,lo)
    tr=ratio(hi,hi)-2*mu(hi,hi)
    assert F(566,1000)<tl<F(567,1000)
    assert -F(109,1000)<tr<-F(108,1000)
    assert tl>F(1,2) and tr<0
    pts=[1,20,50,75,100,125,150,175,200,225,250,275,300,325,350,380]
    pairs=list(combinations(pts,2))
    assert len(pairs)==120 and all(ratio(i,j)<ratio(j,i) for i,j in pairs)
    result={'schema':'PREFIX719_R6_GAMMA_DIAGONAL_STATIONARY_V1',
      'date':'2026-11-12','frozen_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'model':'original 189-level stopping-survivor plus independent Gamma maximum',
      'diagonal_stationary_maximum_open_interval':['43/384','91/768'],
      'scope':'every real q>=2, restriction p->V_q(p,p); existence not uniqueness nor global square optimality',
      'Theta_left_exact_enclosure':['566/1000','567/1000'],
      'Theta_right_exact_enclosure':['-109/1000','-108/1000'],
      'exact_nonzero_survivor_coefficients':9529,
      'ordered_offdiagonal_pairs_exact_tested':120,
      'offdiagonal_result':'r_p<r_z at all predeclared i<j, hence J=mu_p*M2_z-mu_z*M2_p>0 at sampled pairs only',
      'sample_indices':pts,
      'sample_pairs_sha256':hashlib.sha256(json.dumps(pairs,separators=(',',':')).encode()).hexdigest(),
      'status':'AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED',
      'checker':'ALL_CHECKS_PASS PREFIX719-R6',
      'remaining':'Prove uniqueness or counterexample; off-diagonal J sign across continuous square; full 2D optimum'}
    Path(__file__).with_name('PREFIX719_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ALL_CHECKS_PASS PREFIX719-R6',result['diagonal_stationary_maximum_open_interval'],len(pairs))
if __name__=='__main__':run()
