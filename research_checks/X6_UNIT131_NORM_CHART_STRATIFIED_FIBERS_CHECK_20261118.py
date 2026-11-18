#!/usr/bin/env python3
"""Unit131 signed-Xd two-axis charts vs full X6 G-shell; independent exact check."""
from itertools import combinations,product
from math import comb,factorial,isqrt
import json

def require(v):
    if not v: raise AssertionError('unit131 exact invariant')

def roots(N):
    return [(a,isqrt(N-a*a)) for a in range(isqrt(N)+1)
            if isqrt(N-a*a)**2==N-a*a]

def brc(z):
    v=factorial(sum(abs(x) for x in z))
    for x in z: v//=factorial(abs(x))
    return v

def chart(d,N):
    counts={}
    for i,j in combinations(range(d),2):
        for s,t in product((-1,1),repeat=2):
            for a,b in roots(N):
                z=[0]*d;z[i]=s*a;z[j]=t*b;z=tuple(z)
                counts[z]=counts.get(z,0)+1
    labelled=4*comb(d,2)*len(roots(N))
    labelled_mass=4*comb(d,2)*sum(comb(a+b,a) for a,b in roots(N))
    require(sum(counts.values())==labelled)
    require(sum(m*brc(z) for z,m in counts.items())==labelled_mass)
    unique_mass=sum(brc(z) for z in counts)
    if N:
        axial=2*(d-1)
        over=2*d*(axial-1) if isqrt(N)**2==N else 0
        require(labelled-len(counts)==labelled_mass-unique_mass==over)
        require(all(m==(axial if sum(x!=0 for x in z)==1 else 1)
                    for z,m in counts.items()))
    else:
        require(counts=={(0,)*d:4*comb(d,2)})
        require((len(counts),unique_mass)==(1,1))
    return [len(counts),unique_mass,labelled,labelled_mass]

def native_shell(d,Nmax):
    # (squared norm, shortest length) -> (number of endpoints, summed N-BRC)
    states={(0,0):(1,1)}
    for _ in range(d):
        nxt={}
        for (G,L),(count,mass) in states.items():
            for k in range(isqrt(Nmax-G)+1):
                key=(G+k*k,L+k); c,w=nxt.get(key,(0,0)); t=2 if k else 1
                nxt[key]=(c+t*count,w+t*mass*comb(L+k,k))
        states=nxt
    totals=[[0,0] for _ in range(Nmax+1)]
    for (G,_), (c,w) in states.items():
        totals[G][0]+=c;totals[G][1]+=w
    return totals

def exhaustive(d,N):
    r=isqrt(N); result=[0,0]
    for z in product(range(-r,r+1),repeat=d):
        if sum(x*x for x in z)==N:
            result[0]+=1;result[1]+=brc(z)
    return result

def main():
    for d in range(2,9):
        for G in range(201): chart(d,G)
    full=native_shell(6,200)
    for G in (*range(10),25): require(full[G]==exhaustive(6,G))
    require(full[0:4]==[[1,1],[12,12],[60,120],[160,960]])
    samples={}
    for G in range(201):
        a,b,c,w=chart(6,G)
        require(full[G][0]>=a and full[G][1]>=b)
        if G in (0,1,2,3,5,25,50,100,200):
            samples[str(G)]={'unique_endpoints':a,'unique_brc':b,
                             'labeled_endpoints':c,'labeled_brc':w,
                             'full_native_endpoints':full[G][0],
                             'full_native_brc':full[G][1],
                             'missing_native_endpoints':full[G][0]-a,
                             'missing_native_brc':full[G][1]-b}
    print(json.dumps({'schema':'X6_UNIT131_EXACT_INTEGER_CHECK_V1',
                      'dimensions':[2,3,4,5,6,7,8],'norm_range':[0,200],
                      'chart_cases':1407,'native_shell_dp_cases':201,
                      'full_native_direct_shells':list(range(10))+[25],
                      'samples':samples,'review':'UNREVIEWED_NOT_ADMITTED',
                      'original_R063_benchmark_executed':False},sort_keys=True,indent=2))
if __name__=='__main__': main()
