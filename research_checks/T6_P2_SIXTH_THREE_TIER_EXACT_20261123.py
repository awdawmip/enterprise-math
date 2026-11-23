#!/usr/bin/env python3
"""Exact integer certificate: T6 2-adic v6/v5/v4 three-tier elimination.

Full reciprocal moments S_1..S_6 equal; each exponent sum <=2331.
Uses prior proof of universal cancellation at exact v2>=7.
No componentwise rational-moment equality is presumed.
"""
from collections import defaultdict
from heapq import heappush, heappop

CAP = 2331
K = range(1, 7)
MOD = tuple(1 << k for k in K)

def enumerate_profiles(weights, cap):
    current = [0] * len(weights)
    def rec(i, remaining, mass):
        if i == len(weights):
            yield tuple(current), mass
            return
        w = weights[i]
        for n in range(remaining // w + 1):
            current[i] = n
            yield from rec(i + 1, remaining - n*w, mass + n*w)
        current[i] = 0
    yield from rec(0, cap, 0)

def signature(profile, js, scale=1):
    return tuple(sum(n * pow(j, -k, scale * (1 << k))
                     for n,j in zip(profile,js)) % (scale * (1 << k))
                 for k in K)

def add(s,t,sign=1):
    return tuple((s[i] + sign*t[i]) % MOD[i] for i in range(6))

def minimal_signature_cost(v,cap):
    js = tuple(range(1,(cap+1)//(1<<v)+1,2))
    weights = [(1<<v)*j-1 for j in js]
    generators = [signature((1,),(j,)) for j in js]
    best = {(0,)*6:0}
    q = [(0,(0,)*6)]
    while q:
        cost,s = heappop(q)
        if cost != best[s]: continue
        for generator,w in zip(generators,weights):
            nc = cost+w
            if nc>cap: continue
            t = add(s,generator)
            if nc < best.get(t,CAP*2):
                best[t] = nc
                heappush(q,(nc,t))
    return best

def odd_signature_group():
    generators = [signature((1,),(j,)) for j in range(1,64,2)]
    seen = {(0,)*6}
    queue = [(0,)*6]
    for s in queue:
        for g in generators:
            t = add(s,g)
            if t not in seen:
                seen.add(t)
                queue.append(t)
    return seen

def main():
    js6 = tuple(range(1,36,2))
    w6 = tuple(64*j-1 for j in js6)
    groups = defaultdict(list)
    for p,m in enumerate_profiles(w6,CAP):
        groups[signature(p,js6)].append((p,m))
    pairs = [(a,ma,b,mb) for group in groups.values()
             for i,(a,ma) in enumerate(group)
             for b,mb in group[i+1:]]
    assert (sum(map(len,groups.values())),len(groups),len(pairs)) == (4979,1529,11353)
    max_pair_remainder = max(CAP-min(ma,mb) for a,ma,b,mb in pairs)
    assert max_pair_remainder == 2268
    m5 = minimal_signature_cost(5,max_pair_remainder)
    assert len(m5) == 2048
    candidates = []
    for a,ma,b,mb in pairs:
        ra,rb = CAP-ma,CAP-mb
        d6low = tuple(sum((x-y)*pow(j,-k,1<<(2*k))
                          for x,y,j in zip(a,b,js6)) % (1<<(2*k))
                      for k in K)
        assert all(d6low[k-1] % (1<<k) == 0 for k in K)
        shift5 = tuple(d6low[k-1]//(1<<k) for k in K)
        if any(cost<=ra and m5.get(add(s,shift5),CAP*2)<=rb
               for s,cost in m5.items()):
            candidates.append((a,ma,b,mb,ra,rb))
    assert len(candidates) == 26

    maximum = max(max(ra,rb) for a,ma,b,mb,ra,rb in candidates)
    assert maximum == 1376
    js5 = tuple(range(1,(maximum+1)//32+1,2))
    w5 = tuple(32*j-1 for j in js5)
    profiles5 = [(p,m,signature(p,js5),signature(p,js5,64))
                 for p,m in enumerate_profiles(w5,maximum)]
    assert len(profiles5) == 13023
    G = odd_signature_group()
    assert len(G) == 2048

    counts = []
    for a,ma,b,mb,ra,rb in candidates:
        by_b = defaultdict(list)
        for p,cost,low,high in profiles5:
            if cost<=rb:
                by_b[low].append((cost,high))
        d6low = tuple(sum((x-y)*pow(j,-k,1<<(2*k))
                          for x,y,j in zip(a,b,js6)) % (1<<(2*k))
                      for k in K)
        shift5 = tuple(d6low[k-1]//(1<<k) for k in K)
        compatible = 0
        compatible_v4 = 0
        for _,ca,sa,ahigh in profiles5:
            if ca>ra: continue
            target = add(sa,shift5)
            for cb,bhigh in by_b.get(target,()):
                compatible += 1
                T = []
                for k in K:
                    modulus = 1<<(3*k)
                    d6 = sum((x-y)*pow(j,-k,modulus)
                             for x,y,j in zip(a,b,js6)) % modulus
                    d5 = (ahigh[k-1]-bhigh[k-1]) % (1<<(2*k))
                    delta = (d6+(1<<k)*d5) % modulus
                    assert delta % (1<<(2*k)) == 0
                    T.append(delta//(1<<(2*k)))
                need = tuple((-T[k-1]) % (1<<k) for k in K)
                if need in G:
                    compatible_v4 += 1
        counts.append((compatible,compatible_v4))
    expected = [1,151,34,14,168,2,11,46,2,6,23,1,70,4,20,4,11,4,396,14,5,62,10,4,14,1]
    assert [n for n,_ in counts] == expected
    assert sum(n for n,_ in counts)==1078
    assert all(v4==0 for _,v4 in counts)
    print('PASS 4979 v6; 1529 signatures; 11353 ambiguous pairs')
    print('PASS 2048 v5 min-cost states; 26 two-tier candidate pairs')
    print('PASS 13023 v5 profiles; |G|=2048')
    print('PASS 1078 v5-compatible pairs; zero v4-completable cases')
    print('THEOREM exact v2(d)=6 multiplicities universally equal')

if __name__ == '__main__':
    main()
