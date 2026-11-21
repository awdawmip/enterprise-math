"""Canonical fixed-class skeletons for the three moving orbits of a C3-invariant twelve-label partition."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations

def enumerate_fixed(rows, gen, linear, translations, cap):
    cycles=[]; index={}
    for i in range(125):
        if i in index:continue
        g=[i]
        while gen[g[-1]]!=i:g.append(gen[g[-1]])
        index.update(dict.fromkeys(g,len(cycles)));cycles.append(g)
    eye=sum(1<<j for j,g in enumerate(cycles) if len(g)==1)
    mins=(0,0,12,36,72,120,201,292,419,557,744,936,1104,1296)
    @lru_cache(None)
    def remaining(n,k):
        if not k:return 0 if n==0 else 10**8
        return min([3*mins[s]+remaining(n-s,k-1) for s in range(8,14) if n>=s] or [10**8])
    lookup=defaultdict(list)
    for idx,(q,c) in enumerate(rows):lookup[q&eye].append((idx,q,c))
    minima={}
    for a in sorted(lookup):
      for b in sorted(lookup):
        if a&b or b<a:continue
        e=eye^(a|b)
        if e<b or e not in lookup:continue
        for i,x,c in lookup[a]:
          for j,y,d in lookup[b]:
            if (a==b and i>=j) or x&y:continue
            for k,z,f in lookup[e]:
                if (b==e and j>=k) or (x|y)&z:continue
                u=x|y|z;n=45-u.bit_count();cost=c+d+f
                if cost+remaining(n,3)>cap:continue
                if u not in minima or cost<minima[u][0]:
                    minima[u]=(cost,x,y,z)
    norm=set()
    for l in linear:
        for t in translations:
            phi=bytes(t[i] for i in l)
            if all(len({index[phi[p]] for p in g})==1 for g in cycles):
                norm.add(tuple(index[phi[g[0]]] for g in cycles))
    blocks=defaultdict(list)
    for u,(cost,x,y,z) in minima.items():
        bits=[p for p in range(45) if u>>p&1]
        orbit={sum(1<<f[p] for p in bits) for f in norm}
        if min(orbit)!=u:continue
        assert all(minima[v][0]==cost for v in orbit)
        blocks[u]=[cost,x,y,z,len(orbit)]
    return sorted([(u,*rs) for u,rs in blocks.items()],key=lambda r:r[1]+remaining(45-r[0].bit_count(),3)),len(minima)

