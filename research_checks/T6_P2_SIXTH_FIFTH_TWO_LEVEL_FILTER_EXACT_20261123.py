#!/usr/bin/env python3
"""Exact T6 v2(d)=6 / v2(d)=5 necessary two-tier profile sieve.

Assumes proven cancellation at v2>=7; no isolated rational-prime moments.
Enumerates v6 signature collision pairs; tests each against minimal attainable
v5-side signature costs under separate exponent-mass budget <=2331.
"""
from collections import Counter, defaultdict
from heapq import heappush, heappop

CAP = 2331
MOD = tuple(1 << k for k in range(1,7))
J6 = tuple(range(1, (CAP+1)//64+1, 2))
W6 = tuple(64*u-1 for u in J6)


def profiles(weights, cap):
    current = [0]*len(weights)
    def visit(i, r):
        if i==len(weights):
            yield tuple(current)
            return
        for n in range(r//weights[i]+1):
            current[i]=n
            yield from visit(i+1, r-n*weights[i])
        current[i]=0
    yield from visit(0,cap)


def sig5(a, js):
    return tuple(sum(n*pow(j,-k,MOD[k-1]) for n,j in zip(a,js))%MOD[k-1]
                 for k in range(1,7))


def signature_costs_dijkstra(cap):
    js=tuple(range(1, (cap+1)//32+1, 2))
    W=tuple(32*j-1 for j in js)
    c=tuple(tuple(pow(j,-k,MOD[k-1]) for k in range(1,7)) for j in js)
    zero=(0,)*6
    best={zero:0}
    pq=[(0,zero)]
    while pq:
        cost,s=heappop(pq)
        if best[s]!=cost: continue
        for w,v in zip(W,c):
            nc=cost+w
            if nc>cap: continue
            t=tuple((s[k]+v[k])%MOD[k] for k in range(6))
            if nc<best.get(t, 10**9):
                best[t]=nc
                heappush(pq,(nc,t))
    return js,best


def independent_recursive_costs(cap, js):
    w=tuple(32*j-1 for j in js)
    best={}
    count=0
    for a in profiles(w,cap):
        count+=1
        s=sig5(a,js)
        mass=sum(n*v for n,v in zip(a,w))
        if mass<best.get(s,10**9): best[s]=mass
    return count,best


def main():
    assert len(J6)==18
    P=list(profiles(W6,CAP))
    assert len(P)==4979
    groups=defaultdict(list)
    for a in P:
        groups[sig5(a,J6)].append(a)
    assert len(groups)==1529
    pairs=[(a,b) for g in groups.values() for i,a in enumerate(g)
           for b in g[i+1:]]
    assert len(pairs)==11353
    rmax=max(max(CAP-sum(x*w for x,w in zip(a,W6)),
                 CAP-sum(y*w for y,w in zip(b,W6))) for a,b in pairs)
    assert rmax==2268
    js,M=signature_costs_dijkstra(rmax)
    assert len(js)==35 and len(M)==2048
    count,other=independent_recursive_costs(rmax,js)
    assert count==335438 and other==M
    remaining=[]
    for a,b in pairs:
        Ra=CAP-sum(x*w for x,w in zip(a,W6))
        Rb=CAP-sum(x*w for x,w in zip(b,W6))
        shift=tuple(
            (sum((x-y)*pow(j,-k,1<<(2*k)) for x,y,j in zip(a,b,J6))
             %(1<<(2*k)))//(1<<k)
            for k in range(1,7)
        )
        possible=False
        for s,c in M.items():
            if c>Ra:continue
            t=tuple((s[k]+shift[k])%MOD[k] for k in range(6))
            if M.get(t,10**9)<=Rb:
                possible=True
                break
        if possible:
            remaining.append((a,b,Ra,Rb))
    assert len(remaining)==26
    rclasses=Counter(min(Ra,Rb) for a,b,Ra,Rb in remaining)
    assert rclasses==Counter({33:3,35:2,96:1,98:3,100:1,161:3,163:1,
                             224:2,226:1,287:1,289:1,350:1,352:1,
                             415:1,417:1,480:1,543:1,606:1})
    print('PASS: 4979 v6 profiles, 1529 signatures, 11353 candidate pairs')
    print('PASS: v5 minimum cost states = 2048; recursive profiles = 335438')
    print('PASS: 11327 v6 ambiguity pairs excluded, 26 necessary survivors')
    for i,(a,b,Ra,Rb) in enumerate(remaining,1):
        aa=[64*j for j,n in zip(J6,a) for _ in range(n)]
        bb=[64*j for j,n in zip(J6,b) for _ in range(n)]
        print(f'{i:02d}: residual budgets=({Ra},{Rb}), v6 sides={aa} | {bb}')


if __name__=='__main__':
    main()
