from fractions import Fraction as F
from itertools import product
from math import comb
P=tuple(F(x,36) for x in (455,-295,-25,185,-25,-295))
h=[(-F(1,81) if a%3==0 else F(1,162))-F((-1)**a,192) for a in range(6)]
alpha=[-4320**2*x for x in h]
D4=(1,-4,6,-4,1)
def stencil(U):
    return [sum(w*U[(a+j)%6] for j,w in enumerate(D4)) for a in range(6)]
sig=stencil(P)
v=[518400+x for x in stencil(alpha)]
print('h=',h,'alpha=',alpha,'G=',sig,'V=',v)
def enc(a,x):return [x[(a+j)%6] for j in range(3)]
def ray(a,b,sgn):
    A,B,V=enc(a,sig),enc(b,sig),[sgn*x for x in enc(a,v)]
    H=max(abs(x) for x in V)
    crit=F(0)
    for da,u in zip((x-y for x,y in zip(A,B)),V):
        for s in (1,-1):
            num=s*da; denom=H-s*u
            if num>0 and denom==0: return None
            if denom>0:crit=max(crit,F(num,denom))
    return crit
for d in (1,-1):
    values=sorted((x,a,b) for a,b in product(range(6),repeat=2) if a!=b for x in [ray(a,b,d)] if x is not None)
    print(d,values[:10])
    first,a,b=values[0]; V=enc(a,v); A=enc(a,sig);B=enc(b,sig)
    for x in (first,first+F(1,10**12)):
        dt=max(abs(z*d*x) for z in V);dr=max(abs(i-j+z*d*x) for z,i,j in zip(V,A,B)); print(x,dt,dr,dt-dr)
