#!/usr/bin/env python3
"""Independent exact Mobius audit of PREFIX-896; Python 3 standard library."""
import math
from collections import defaultdict
P=32
N=1<<P
M=N*(P+1)
A,B=262145,524287
Q=range(A,B+1,2)
S={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285}
AX={q for q in Q if any((2**h-1)%q==0 or (2**h+1)%q==0 for h in range(1,P))}
U=S|AX|{400011+2*j for j in range(256)}|{480011+2*j for j in range(256)}
assert len(U)==552 and len(AX)==24

def sf_divisors(a):
    t=a
    primes=[]
    d=3
    while d*d<=t:
        if t%d==0:
            primes.append(d)
            while t%d==0:t//=d
        d+=2
    if t>1:primes.append(t)
    out=[(1,1)]
    for p in primes:
        out += [(v*p,-sign) for v,sign in list(out)]
    return out

DIV={a:sf_divisors(a) for a in range(1,B//35+1,2)}
def coprime_odd_count(a,lo,hi):
    return sum(sign*((hi//d+1)//2-(((lo-1)//d)+1)//2) for d,sign in DIV[a])

Ug=defaultdict(list)
for u in U:
    for d in range(1,math.isqrt(u)+1,2):
        if u%d==0:
            if d>=35:Ug[d].append(u//d)
            g=u//d
            if g>=35 and g!=d and g%2==1:Ug[g].append(d)

zz_outside_P=0
zz_outside_PU=0
for g in range(35,B+1,2):
    amin=(A+g-1)//g
    amax=B//g
    amin+=amin%2==0
    amax-=amax%2==0
    rowU=Ug.get(g,())
    for a in range(amin,amax+1,2):
        lo=max(amin,(M+g*g*a-1)//(g*g*a))
        hi=min(amax,(N-1)//(g*a))
        lo+=lo%2==0
        hi-=hi%2==0
        if lo>hi:continue
        c=coprime_odd_count(a,lo,hi)
        zz_outside_P+=c
        if g*a not in U:
            zz_outside_PU+=c-sum(lo<=b<=hi and math.gcd(a,b)==1 for b in rowU)

assert zz_outside_P==95365328
assert zz_outside_PU==94314796
c=lambda q:max(0,(min(B,(M-1)//q)-A)//2+1)
pcount=sum(c(q) for q in Q)
cu=sum(c(u) for u in U)
cuu=sum(u*v<M for u in U for v in U)
hcount=2*len(U)*len(Q)-len(U)**2
total=pcount+hcount-(2*cu-cuu)+zz_outside_PU
assert (pcount,cu,cuu,total)==(7364142398,18312436,11996,7566243102)
checks=0
for p in range(2,8):
    n=1<<p
    pop=[(x,x) for x in range(n)]+[(x,x^(1<<i)) for x in range(n) for i in range(p)]
    for q1 in range(3,n+2,2):
        for q2 in range(3,n+2,2):
            if q1*q2<n*(p+1):
                seen=set()
                found=False
                for u,v in pop:
                    obs=(u%q1,v%q2)
                    if obs in seen:found=True;break
                    seen.add(obs)
                assert found
                checks+=1
print(dict(method="Mobius plus direct small-state regression",zz_outside_P=zz_outside_P,
           zz_outside_PU=zz_outside_PU,capacity=pcount,union=total,
           small_direct_capacity_checks=checks))
