#!/usr/bin/env python3
"""Independent exact checks for N31 auxiliary BRC single-pulse theorem.

Python stdlib only; finite tests do not replace the all-n analytical proof.
"""
from fractions import Fraction as Q
from math import comb

GOOD = {3, 6, 10, 12}

def zpoly(n,z):
    m=n-2
    return 4-2**m-2*(1-z)*(2+z)**m-(1+z)*(2-z)**m+(2-z)*(1+z)**m

def direct_coeff(m):
    a=[comb(m,j)*2**(m-j) for j in range(m+1)]
    b=[comb(m,j)*2**(m-j)*(-1)**j for j in range(m+1)]
    c=[comb(m,j) for j in range(m+1)]
    x=[0]*(m+2); x[0]=4-2**m
    for j in range(m+1):
        x[j]+=-2*a[j]-b[j]+2*c[j]
        x[j+1]+=2*a[j]-b[j]-c[j]
    return x

def theorem_coeff(m):
    x=[6-4*2**m]
    for j in range(1,m+1):
        h=(2+(-1)**j)*2**(m-j)
        x.append(h*(2*comb(m,j-1)-comb(m,j))+2*comb(m,j)-comb(m,j-1))
    x.append(1+(-1)**(m+1))
    return x

def pre(t,z):
    a,b,c=(1+z)/3,(1-z)/3,Q(1,3)
    return (a+b)**t+(a+c)**t+(b+c)**t-2*(a**t+b**t+c**t)

def post(t,z):
    a,b,c=(1+z)/3,(1-z)/3,Q(1,3)
    h=t-1
    return ((a+b)**h+2*(a+c)**h+(b+c)**h-a**h-2*c**h)/3

def dp(n,k,z):
    d={0:Q(1)}
    hist=[Q(0)]
    for t in range(1,n+1):
        q=[0,1+z,1-z,1] if t!=k else [1,1,0,1]
        e={}
        for mask,p in d.items():
            for i,m in enumerate(q):
                if m:
                    v=mask|(1<<i)
                    e[v]=e.get(v,Q(0))+p*m/3
        d=e
        assert sum(d.values())==1
        hist.append(sum(p for mask,p in d.items() if mask in GOOD))
    return hist

def residual(x):
    return sum(max(Q(0),x[i]-x[i-1]) for i in range(2,len(x)))-max(x)

def bracket(n,digits=45):
    b=10**digits
    lo,hi=0,b
    assert zpoly(n,Q(0))<0 and zpoly(n,Q(1))>0
    while hi-lo>1:
        mid=(lo+hi)//2
        v=zpoly(n,Q(mid,b))
        if v>0: hi=mid
        elif v<0: lo=mid
        else: return mid,mid,b
    assert zpoly(n,Q(lo,b))<0<zpoly(n,Q(hi,b))
    return lo,hi,b

def main():
    total=0
    for m in range(2,91):
        x=direct_coeff(m)
        assert x==theorem_coeff(m)
        assert x[0]<0 and sum(x)==2
        if m>=4:
            for j in range(1,m+1):
                assert (x[j]<0) if 3*j<m+1 else (x[j]>0)
            assert x[m+1] in (0,2)
        else:
            nz=[a for a in reversed(x) if a]
            assert sum((a>0)!=(b>0) for a,b in zip(nz,nz[1:]))==1
        total+=len(x)
    print("ALL_COEFFICIENT_CHECKS_PASS",total)
    cases=prefix=peak=increment=0
    for z in [Q(0),Q(1,7),Q(1,3),Q(1,2),Q(7,10),Q(9,10),Q(999,1000),Q(1)]:
        for n in range(4,19):
            for k in range(4,n+1):
                h=dp(n,k,z)
                assert h[3]==Q(2,3)
                oldmax=max(h[:k])
                for t in range(1,n+1):
                    assert h[t]==(pre(t,z) if t<k else post(t,z))
                    prefix+=1
                    if t>=k:
                        assert h[t]<=Q(2,3)-Q(1,3**t)
                        assert max(h[:t+1])==oldmax
                        peak+=1
                    if t>k:
                        assert h[t]-h[t-1]==zpoly(t,z)/3**t
                        assert residual(h[:t+1])-residual(h[:t])==max(Q(0),zpoly(t,z)/3**t)
                        increment+=1
                cases+=1
    print("INDEPENDENT_16_STATE_DP_PASS",cases,prefix,peak,increment)
    for n in (4,5,6,10,20,28,29,30,31,40,60,90):
        lo,hi,den=bracket(n)
        if n in (30,31):
            print("THETA_BRACKET",n,f"{lo//den}.{lo%den:045d}",f"{hi//den}.{hi%den:045d}")
    print("EXACT_RATIONAL_ROOT_BRACKETS_PASS 12")
    print("OVERALL_EXACT_REGRESSION_PASS")

if __name__=="__main__":
    main()
