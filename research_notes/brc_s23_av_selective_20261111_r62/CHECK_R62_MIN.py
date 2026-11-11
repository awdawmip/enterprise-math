"""R62 independently executed exact miniature checker: Fraction/integer only."""
from fractions import Fraction as Q
from bisect import bisect_right
P=262204504569236716045286
D=10**24

def vector(theta,m,ages):
    boundaries=sorted((((h*theta)%1),h) for h in range(m))
    out=[None]*m
    for r in sorted(ages):
        u=(-r*theta)%1
        i=bisect_right(boundaries,(u,m))-1
        label=boundaries[i][1]
        if out[label] is None:out[label]=r
    return out

def strict(p,q,d):
    if d==0:return False
    x=d*p;y=d*(p+1)
    return x%q!=0 and y%q!=0 and x//q==y//q

def certify(p,q,m,ages,label):
    if not all(min((d*p)%q,q-(d*p)%q)>d for d in range(1,m)):
        return None
    theta=Q(2*p+1,2*q)
    order=sorted((((h*theta)%1),h) for h in range(m))
    j=next(i for i,(_,h) in enumerate(order) if h==label)
    nxt=order[(j+1)%m][1]
    youngest=vector(theta,m,ages)[label]
    checked=[r for r in ages if youngest is None or r<=youngest]
    if all(strict(p,q,-r-h) for r in checked for h in (label,nxt)):
        return (youngest,len(checked))
    return None

if __name__=='__main__':
    age=D
    t1=Q(4*P+1,4*D);t2=Q(4*P+3,4*D)
    assert vector(t1,2,[1,age])==[None,1]
    assert vector(t2,2,[1,age])==[age,1]
    assert certify(P,D,2,[1,age],1)==(1,1)
    assert certify(P,D,2,[1,age],0) is None
    data=[certify(P,D,128,list(range(1,226)),z) for z in (0,31,127)]
    assert data==[(61,61),(30,30),(98,98)],data
    E=set(range(-225,0))|set(range(128))
    diffs={u-v for u in E for v in E if u!=v}
    assert len(diffs)==704
    margin=min(min((d*P)%D,D-((d*P)%D))-abs(d) for d in diffs)
    assert margin==1538749354821431426740
    print({'witness_vectors':([None,1],[age,1]),'sparse':data,
           'interval_differences':len(diffs),'margin':margin})
