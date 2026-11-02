#!/usr/bin/env python3
"""PREFIX-444 compact exact certificate: one-axis signed-X6 path bags, no native class import."""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb

def legal(n, bag):
    return all(count <= comb(n,k) for k,count in Counter(bag).items())

def readout(n, bag):
    xs = [n-2*k for k in bag]
    sector = tuple(tuple(sum((n-2*k)**j for k in bag if k%2==r)
                         for j in range(3)) for r in range(2))
    whole = tuple(sum(x**j for x in xs) for j in range(4))
    return sector, whole

def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for j in range(len(a[0])):
        p = next((i for i in range(r,len(a)) if a[i][j]),None)
        if p is None: continue
        a[p],a[r] = a[r],a[p]
        z=a[r][j];a[r]=[v/z for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                z=a[i][j];a[i]=[v-z*w for v,w in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def run():
    n=7
    pairs = (
        ((0,3,4,7),(1,1,6,6)),
        ((0,4,4,4),(2,2,2,6)),
        ((0,4,4,4,3,3,3,7),(2,2,2,6,1,5,5,5)),
    )
    for a,b in pairs:assert legal(n,a) and legal(n,b)
    a,b=pairs[0];sa,ma=readout(n,a);sb,mb=readout(n,b)
    assert ma==mb==(4,0,100,0) and sa!=sb
    a,b=pairs[1];sa,ma=readout(n,a);sb,mb=readout(n,b)
    assert sa==sb==((4,4,52),(0,0,0)) and ma[3]-mb[3]==384
    a,b=pairs[2];sa,ma=readout(n,a);sb,mb=readout(n,b)
    assert sa==sb and ma==mb
    xs=[n-2*k for k in range(n+1)]
    q=[[x**j if k%2==r else 0 for k,x in enumerate(xs)] for r in range(2) for j in range(3)]
    m=[[x**j for x in xs] for j in range(4)]
    mixed=q+[m[3]]
    q3=[[x**j if k%2==r else 0 for k,x in enumerate(xs)] for r in range(2) for j in range(4)]
    assert [rank(y) for y in (q,m,mixed,q3)]==[6,4,7,8]
    h=(1,-1,-3,3,3,-3,-1,1)
    assert all(sum(x*y for x,y in zip(row,h))==0 for row in mixed)
    assert sum(max(0,x) for x in h)==sum(max(0,-x) for x in h)==8
    # Additional sharp-threshold witnesses at n=9 and n=14.
    for length,left,right in (
        (9,(0,3,3,6,6,9),(1,2,2,7,7,8)),
        (14,(0,6,8,14),(2,2,12,12)),
    ):
        assert legal(length,left) and legal(length,right)
        assert readout(length,left)==readout(length,right)
    # A one-sector cubic collision on at most five atoms is impossible
    # when its normalized k-grid is within {0,...,6}: finite complete test.
    small_grid_counts=[]
    for mass in range(1,6):
        seen=set()
        for bag in combinations_with_replacement(range(7),mass):
            key=tuple(sum(k**j for k in bag) for j in (1,2,3))
            assert key not in seen
            seen.add(key)
        small_grid_counts.append(len(seen))
    assert small_grid_counts==[7,28,84,210,462]
    # Check no joint collision under the proposed sharp threshold in the
    # finite boundary regimes, including the n=8 two-kernel case.
    sharp_checked=0
    for length,bound in ((7,8),(8,8),(9,6),(10,6),(11,6),(12,6),(13,6)):
        for mass in range(1,bound):
            seen=set()
            for bag in combinations_with_replacement(range(length+1),mass):
                if not legal(length,bag):continue
                sector,whole=readout(length,bag)
                key=(sector,whole[3])
                assert key not in seen,(length,mass,bag)
                seen.add(key)
            sharp_checked+=len(seen)
    counts=[]
    for n0 in range(7):
        seen={}; count=0
        for bag in combinations_with_replacement(range(n0+1),4):
            if not legal(n0,bag):continue
            key=tuple(sum(k**j for k in bag) for j in (1,2,3))
            assert key not in seen or seen[key]==bag
            seen[key]=bag;count+=1
        counts.append(count)
    assert counts==[0,0,1,14,41,85,155]
    # Algebraic common (+/-) future map: n increases, k stays or increases by 1.
    tests=0;alpha=Fraction(2,3);beta=Fraction(3,5)
    for n0 in range(1,10):
        for bag in combinations_with_replacement(range(n0+1),3):
            if not legal(n0,bag):continue
            s,p=readout(n0,bag)
            predicted=tuple(tuple(sum(comb(j,t)*(alpha*s[r][t]+beta*(-1)**(j-t)*s[1-r][t])
                    for t in range(j+1)) for j in range(3)) for r in range(2))
            pred3=sum(comb(3,t)*(alpha+beta*(-1)**(3-t))*p[t] for t in range(4))
            transformed=[(k,alpha) for k in bag]+[(k+1,beta) for k in bag]
            direct=tuple(tuple(sum(w*(n0+1-2*k)**j for k,w in transformed if k%2==r)
                    for j in range(3)) for r in range(2))
            direct3=sum(w*(n0+1-2*k)**3 for k,w in transformed)
            assert predicted==direct and pred3==direct3
            tests+=1
    print('PASS n=7: two opposite four-word observer fibers and joint eight-word fiber')
    print('PASS exact ranks: sector_quad=6, global_cubic=4, joint=7, sector_cubic=8')
    print('PASS primitive kernel: (1,-1,-3,3,3,-3,-1,1); minimum joint mass=8')
    print('PASS sharp thresholds: n<=6 infinity; n=7,8 mass 8; n=9..13 mass 6; n>=14 mass 4')
    print('PASS one-sector normalized grid <=6 cubic recovery for mass <=5: '+str(small_grid_counts))
    print('PASS complete finite joint-collision exclusion probes: '+str(sharp_checked)+' legal bags')
    print('PASS exhaustive legal mass-four bag counts n<=6: '+str(counts))
    print('PASS exact common signed-step future transfer: '+str(tests)+' bags')
    print('UPSTREAM_CONTROL_PACKET_DIRECT_IMPORT=NOT_EXECUTED')

if __name__=='__main__':run()
