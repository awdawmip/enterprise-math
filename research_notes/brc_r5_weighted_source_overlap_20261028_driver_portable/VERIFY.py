#!/usr/bin/env python3
"""Exact rational checks of the nonblind R5 weighted source-overlap theorem."""
from fractions import Fraction as F
from random import Random

def interp(s, i, j, mass, moment):
    if i == j:
        assert moment == s[i]*mass
        z = [F(0) for _ in s]
        z[i] = mass
        return z
    assert s[i] < s[j]
    xi = (s[j]*mass-moment)/(s[j]-s[i])
    xj = (moment-s[i]*mass)/(s[j]-s[i])
    assert xi >= 0 and xj >= 0
    z = [F(0) for _ in s]
    z[i],z[j] = xi,xj
    return z

def stats(s,r,q,qp):
    assert len(s)==len(q)==len(qp) and sum(q)==sum(qp)==1
    assert sum(x*y for x,y in zip(s,q))==r
    assert sum(x*y for x,y in zip(s,qp))==r
    u = sum(abs(x-y) for x,y in zip(q,qp))/2
    v = sum(si*abs(x-y) for si,x,y in zip(s,q,qp))/(2*r)
    return u,v

def max_coordinate(s,mass,moment,k):
    values=[mass]
    if k>0:
        values.append((moment-s[0]*mass)/(s[k]-s[0]))
    if k<len(s)-1:
        values.append((s[-1]*mass-moment)/(s[-1]-s[k]))
    G=min(values)
    assert 0<=G<=mass
    return G

def construct(s,r,u,v,w1,w2,k):
    assert len(s)>=3 and all(0<s[i]<s[i+1] for i in range(len(s)-1))
    assert s[0]<r<s[-1] and w1>0 and w2>0
    assert 0<=u<=1 and s[1]*u<=r*v<=s[-2]*u
    M,C=1-u,r*(1-v)
    assert s[0]*M<=C<=s[-1]*M
    G=max_coordinate(s,M,C,k)
    U=max_coordinate(s,u,r*v,k)
    wl,wh=sorted((w1,w2))
    c=[F(0) for _ in s]
    c[k]=G
    others=[i for i in range(len(s)) if i!=k]
    extra=interp(s,others[0],others[-1],M-G,C-s[k]*G) if M>G else [F(0) for _ in s]
    c=[x+y for x,y in zip(c,extra)]
    moment=r*v
    if not u:
        a=b=[F(0) for _ in s]
    else:
        m=moment/u
        if m>s[k]:
            a=interp(s,k,len(s)-1,u,moment)
            b=interp(s,1 if k==0 else 0,len(s)-2,u,moment)
        elif m<s[k]:
            a=interp(s,0,k,u,moment)
            b=interp(s,1,len(s)-2 if k==len(s)-1 else len(s)-1,u,moment)
        else:
            a=[F(0) for _ in s]
            a[k]=u
            b=interp(s,0,len(s)-1,u,moment)
    assert all(x*y==0 for x,y in zip(a,b))
    assert a[k]==U and b[k]==0
    q=[c[i]+a[i] for i in range(len(s))]
    qp=[c[i]+b[i] for i in range(len(s))]
    assert stats(s,r,q,qp)==(u,v)
    assert min(q[k],qp[k])==G
    cap=min(wl*(G+U),wh*G)
    assert min(wl*q[k],wh*qp[k])==cap
    return cap,G,U,q,qp

def mean_kernel(s,r,rng):
    q=[F(rng.randint(1,8),10000) for _ in s]
    total=1-sum(q)
    rest=r-sum(si*qi for si,qi in zip(s,q))
    z=interp(s,0,len(s)-1,total,rest)
    return [x+y for x,y in zip(q,z)]

def main():
    s=[F(1,2),F(1),F(2),F(3)]
    r=F(3,2)
    u=v=F(3,5)
    equal=construct(s,r,u,v,F(1,4),F(1,4),3)
    unequal=construct(s,r,u,v,F(1,6),F(1,3),3)
    assert equal[:3]==(F(1,25),F(4,25),F(6,25))
    assert unequal[:3]==(F(4,75),F(4,25),F(6,25))
    q=[F(147,250),F(1,100),F(1,100),F(49,125)]
    qp=[F(57,250),F(31,100),F(31,100),F(19,125)]
    assert all(x>0 for x in q+qp) and stats(s,r,q,qp)==(u,v)
    assert min(F(1,6)*q[-1],F(1,3)*qp[-1])==F(19,375)>F(1,20)>F(1,25)
    print('EQUAL_WEIGHT_TOP_CAP=1/25; UNEQUAL_WEIGHT_TOP_SUP=4/75')
    print('STRICT_POSITIVE_UNEQUAL_WEIGHT_TOP_OVERLAP=19/375>1/20')
    rng=Random(202610282000)
    cases=0
    for n in (3,4,5,6,7):
        t=[F((j+1)**2,j+2) for j in range(n)]
        r0=(t[0]+t[-1])/2
        for _ in range(65):
            qa=mean_kernel(t,r0,rng)
            qb=mean_kernel(t,r0,rng)
            u0,v0=stats(t,r0,qa,qb)
            for k in range(n):
                for wa,wb in ((F(1,7),F(3,7)),(F(1,4),F(1,4)),(F(2,9),F(7,9))):
                    cap,G,U,x,y=construct(t,r0,u0,v0,wa,wb,k)
                    assert min(wa*qa[k],wb*qb[k])<=cap
                    assert min(wa*qb[k],wb*qa[k])<=cap
                    assert min(x[k],y[k])==G
                    cases+=1
    assert cases==4875
    print('EXACT_RATIONAL_WITNESS_AND_UPPER_BOUND_CASES',cases)
    print('ALL CHECKS PASSED')

if __name__=="__main__":
    main()
