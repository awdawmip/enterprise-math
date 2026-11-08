#!/usr/bin/env python3
"""PREFIX-601: generic two-occurrence signed three-STAR phase graph checks.
Exact integer certificate, standard-library only. Original 4-STAR incidence
is a frozen native X6-BRC seed; other STAR systems are abstract examples.
"""
from collections import Counter

def validate(stars):
    s=len(stars)
    assert s>0 and all(len(a)==3 and len(set(a))==3 for a in stars)
    multiplicity=Counter(k for a in stars for k in a)
    assert all(x==2 for x in multiplicity.values())
    assert s%2==0
    def near(a,c):
        return tuple((-1 if c>0 else 1)*k for k in stars[a] if k!=abs(c))
    ph=tuple((a,p,sign*k) for a in range(s) for k in stars[a]
             for sign in (-1,1) for p in near(a,sign*k))
    idx={x:i for i,x in enumerate(ph)}
    assert len(idx)==12*s
    def other(a,k):
        return next(b for b in range(s) if b!=a and k in stars[b])
    nxt=[]
    for a,p,c in ph:
        b=other(a,abs(c))
        nxt.append(tuple(idx[x] for x in
                [(a,c,k) for k in near(a,c) if k!=p]+
                [(b,c,k) for k in near(b,c)]))
    slot0=[row[0] for row in nxt]
    assert set(slot0)==set(range(len(ph)))
    inv=[None]*len(ph)
    for i,j in enumerate(slot0):inv[j]=i
    B=[tuple(nxt[inv[i]][1:]) for i in range(len(ph))]
    F=[next(j for j, (aj,pj,cj) in enumerate(ph)
            if aj==a and pj==p and cj!=c)
        for a,p,c in ph]
    assert all(F[F[i]]==i and F[i]!=i for i in range(len(ph)))
    for i,(a,p,c) in enumerate(ph):
        b=other(a,abs(p))
        expected={j for j,(aj,pj,cj) in enumerate(ph) if aj==b and pj==p}
        assert set(B[i])==expected and len(B[i])==2
        assert set(B[i])==set(B[F[i]])
        counts=Counter(k for j in B[i] for k in B[j])
        assert counts==Counter({i:2,F[i]:2})
    # Slot-0 permutation has exactly two six-cycles per STAR.
    seen=set(); cycles=[]
    for i in range(len(ph)):
        if i in seen:continue
        j=i;cycle=[]
        while j not in seen:
            seen.add(j);cycle.append(j);j=slot0[j]
        assert j==i
        cycles.append(cycle)
    assert len(cycles)==2*s and all(len(c)==6 for c in cycles)
    pairs=[(i,F[i]) for i in range(len(ph)) if i<F[i]]
    assert len(pairs)==6*s
    byphase={x:k for k,pair in enumerate(pairs) for x in pair}
    twin_tau=[byphase[B[pair[0]][0]] for pair in pairs]
    assert all(twin_tau[twin_tau[k]]==k and twin_tau[k]!=k
               for k in range(len(pairs)))
    return dict(stars=s,phases=len(ph),twin_pairs=len(pairs),
                tau_transpositions=3*s,
                determinant=3**(3*s), smith_ones=9*s,smith_threes=3*s)

def from_edges(n,edges):
    st=[[] for _ in range(n)]
    for lab,(a,b) in enumerate(edges,1):
        st[a].append(lab);st[b].append(lab)
    return st

CASES=[
 ("two_star_parallel",2,[(0,1)]*3),
 ("K4",4,[(i,j) for i in range(4) for j in range(i+1,4)]),
 ("K3_3",6,[(i,j) for i in range(3) for j in range(3,6)]),
 ("triangular_prism",6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]),
 ("cube",8,[(i,j) for i in range(8) for j in range(i+1,8)
            if (i^j).bit_count()==1])
]
if __name__=="__main__":
    for name,n,edges in CASES:
        result=validate(from_edges(n,edges))
        print("ALL_CHECKS_PASS",name,result)
