#!/usr/bin/env python3
"""R749SOG exact rational checks of the analytic transverse positive collar.
All-real theorem is proved in the companion note. Only standard library.
"""
from fractions import Fraction as Q
from itertools import combinations
import json

MASKS = (3,12,15,1,2,4,8)
SIGNS = tuple(tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16))
A = tuple(row[0] for row in SIGNS)
B = tuple(row[1] for row in SIGNS)

def law(t,s,h,u,v,w,z):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,c)),Q(0)))/16 for row in SIGNS)

def center(t,s): return law(t,s,min(t,s),Q(0),Q(0),Q(0),Q(0))
def tv(x,y): return sum((abs(a-b) for a,b in zip(x,y)),Q(0))/2

def G(t):
    if Q(1,2)<=t<=Q(9,16):return Q(7,220)-t/22
    if t<=Q(3,5):return (2*t-1)/20
    if t<Q(2,3):return (2-3*t)/20
    if t==Q(2,3):return Q(0)
    raise ValueError(t)

def width(t):return (1-t)*G(t)/4

def primitive(a,b,t):
    return a*t+(b-a)*t*t/2-b*t*t*t/3

def exact_area():
    pieces=((Q(1,2),Q(9,16),Q(7,220),-Q(1,22)),
            (Q(9,16),Q(3,5),-Q(1,20),Q(1,10)),
            (Q(3,5),Q(2,3),Q(1,10),-Q(3,20)))
    return sum((primitive(a,b,hi)-primitive(a,b,lo) for lo,hi,a,b in pieces),Q(0))/2

def transport(mu,t,s,t2,s2):
    d=abs(t2-t)+abs(s2-s)
    assert Q(0)<=t<=1 and Q(0)<=s<=1 and d<=1-max(t,s)
    alpha=d/(1-max(t,s))
    rr=center(t,s)
    out=tuple((1-alpha)*x+alpha*y+((t2-t)*a+(s2-s)*b)/16
              for x,y,a,b in zip(mu,rr,A,B))
    assert min(out)>=0 and sum(out)==1
    for idx,new_moment in ((0,t2),(1,s2)):
        assert sum((out[k]*SIGNS[k][idx] for k in range(16)),Q(0))==new_moment
    for idx in range(3,7):
        assert sum((out[k]*SIGNS[k][idx] for k in range(16)),Q(0)) == \
           (1-alpha)*sum((mu[k]*SIGNS[k][idx] for k in range(16)),Q(0))
    error=tv(mu,out)
    assert error<=alpha+max(abs(t2-t),abs(s2-s))/2
    return error

def linear5(matrix,rhs):
    a=[[Q(v) for v in row]+[Q(y)] for row,y in zip(matrix,rhs)]
    for j in range(5):
        pivot=next((i for i in range(j,5) if a[i][j]),None)
        if pivot is None:return None
        if pivot!=j:a[pivot],a[j]=a[j],a[pivot]
        v=a[j][j]
        for k in range(j,6):a[j][k]/=v
        for i in range(j+1,5):
            v=a[i][j]
            for k in range(j,6):a[i][k]-=v*a[j][k]
    ans=[Q(0)]*5
    for j in range(4,-1,-1):
        ans[j]=a[j][5]-sum((a[j][k]*ans[k] for k in range(j+1,5)),Q(0))
    return tuple(ans)

def vertices(t,s):
    seen=set()
    for ids in combinations(range(16),5):
        z=linear5([SIGNS[k][2:] for k in ids],[-1-t*A[k]-s*B[k] for k in ids])
        if z is not None and min(law(t,s,*z))>=0:seen.add(z)
    return tuple(sorted(seen))

def main():
    assert exact_area()==Q(18199,76032000)
    assert [G(x) for x in (Q(1,2),Q(9,16),Q(3,5),Q(2,3))] == \
           [Q(1,110),Q(1,160),Q(1,100),Q(0)]
    assert 1-Q(100,133)-Q(3,16)==Q(129,2128)
    samples=[]
    for t in (Q(1,2),Q(3,5),Q(13,20),Q(199,300)):
        d=width(t);g=G(t)
        assert d>0 and d<(1-t)/2
        assert g-3*(d/(1-t-d)+d/2)>=Q(129,2128)*g
        for sign in (-1,1):
            s=Q(1,2)+sign*d
            aa=vertices(t,Q(1,2));bb=vertices(t,s)
            err1=max(transport(law(t,Q(1,2),*v),t,Q(1,2),t,s) for v in aa)
            err2=max(transport(law(t,s,*v),t,s,t,Q(1,2)) for v in bb)
            samples.append(dict(t=str(t),s=str(s),source_vertices=len(aa),
                 target_vertices=len(bb),direct_tv_max=str(err1),
                 reverse_tv_max=str(err2),gap_lower=str(Q(129,2128)*g)))
    return dict(status="PASS",exact_area="18199/76032000",
       frozen_science_pin="a72226e2430ffa4786321ac86e7f0c599d5f0389",
       proof_dependency="R749SOF author-side exact transverse theorem, NOT_REVIEWED",
       bound="g(t,s)>=(129/2128)*G(t)>0 on 1/2<=t<2/3, abs(s-1/2)<=(1-t)*G(t)/4",
       samples=samples)

if __name__=="__main__":
    print(json.dumps(main(),sort_keys=True,indent=2))
