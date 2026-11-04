#!/usr/bin/env python3
"""O(p) finite-field operations, O(1) memory: source-labelled signed first-jet Sun transport."""
from math import isqrt
def primes(N):
    for p in range(5,N+1):
        if all(p%d for d in range(2,isqrt(p)+1)): yield p
def jet(p,d):
    inv=lambda z:pow(z%p,-1,p)
    add=lambda a,b:((a[0]+b[0])%p,(a[1]+b[1])%p)
    mul=lambda a,b:((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    scl=lambda a,z:(a[0]*z%p,a[1]*z%p)
    n=p//d;C=(d-1)*inv(d*d)%p
    J=(n-1 if p%3==1 else n) if d==3 else (2*n-1 if p%4==1 else 2*n+1)
    x=scl((2,1),inv(4)) if d==3 else scl((3,2),inv(6))
    t=(1,0);c=1;qm=0;q=0;V=(0,0);D=(0,0)
    for j in range(J):
        f=(2-6*C*inv(j+1))*c%p
        z=f+(2*j+1)*(j*(j+1)+2*C)*q-j*(j*j-1+4*C)*qm
        qnext=z*inv((j+1)**3)%p
        D=add(D,scl(t,(j+1)*qnext))
        t=mul(t,x);V=add(V,scl(t,qnext))
        qm,q=q,qnext
        c=c*(j*(j+1)+C)*inv((j+1)**2)%p
    cxp=scl(add((1,0),scl(x,-1)),C)
    return mul(cxp,V),mul(cxp,D)
def main():
    anchors={
        13:((6,0),(11,5),(1,0),(12,4),(12,3)),
        19:((18,0),(4,2),(17,0),(5,7),(6,18)),
        139:((138,0),(3,53),(122,0),(50,73),(16,75)),
        373:((132,0),(287,249),(137,0),(371,268),(227,371))}
    cases=0
    for p in primes(5000):
        if p%24 not in (13,19):continue
        e3,ed3=jet(p,3);e4,ed4=jet(p,4)
        assert e3[1]==e4[1]==0
        if p in anchors:
            def smul(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
            v=smul((0,1),tuple(k*3*pow(4,-1,p)%p for k in ed3))
            w=smul((0,1),tuple(k*pow(6,-1,p)%p for k in ed4))
            signed=tuple((-e3[i]+e4[i]+v[i]-w[i])%p for i in (0,1))
            assert (e3,ed3,e4,ed4,signed)==anchors[p],(p,signed)
            print(p,'E3',e3,'E3prime',ed3,'E4',e4,'E4prime',ed4,'S_def',signed)
        cases+=2
    print('model_cases=',cases,'failures=0')
if __name__=='__main__':main()
