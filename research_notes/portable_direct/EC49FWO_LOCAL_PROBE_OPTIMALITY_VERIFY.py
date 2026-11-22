#!/usr/bin/env python3
"""Exact finite verification of n/2 fixed local probes for even-n CRT products."""
import itertools, json
from collections import defaultdict


def support(k, mask):
    return tuple(i for i in range(k) if mask & (1 << i))


def conv(A,k):
    out=[0]*k
    for a in A:
        for b in A:
            out[(a+b)%k]+=1
    return tuple(out)


def defects(U,V,n,q):
    a,b=conv(U,n),conv(V,q)
    N=len(U)*len(V)
    return tuple(2*(N-a[x]*b[y]) for x in range(n) for y in range(q))


def check(n,q):
    m=n//2;assert n>=4 and n%2==0 and q%2
    groups=defaultdict(list)
    for ua in range(1,1<<n):
        U=support(n,ua)
        for vb in range(1,1<<q):
            V=support(q,vb)
            key=defects(U,V,n,q)
            mass=len(U)*len(V)
            bitmap=sum(1<<(x*q+y) for x in U for y in V)
            groups[key].append((mass,bitmap))
    masks=set()
    for members in groups.values():
        for i in range(len(members)):
            for j in range(i):
                if members[i][0] != members[j][0]:
                    masks.add(members[i][1]^members[j][1])
    P=tuple(x*q for x in range(m))
    pmask=sum(1<<x for x in P)
    assert all(pmask & diff for diff in masks)
    for Q in itertools.combinations(range(n*q),m-1):
        qmask=sum(1<<x for x in Q)
        assert any(not(qmask & diff) for diff in masks), (n,q,Q)
    return dict(n=n,q=q,total_products=((1<<n)-1)*((1<<q)-1),
                distinct_defect_signatures=len(groups),distinct_cross_mass_discrepancies=len(masks),
                minimum_fixed_probe_count=m, example_probe_positions=list(P),
                all_smaller_probe_sets_rejected=True)


def check_odd(n,q):
    assert n % 2 == 1 and q % 2 == 1
    groups=defaultdict(list)
    for ua in range(1,1<<n):
        U=support(n,ua)
        for vb in range(1,1<<q):
            V=support(q,vb)
            key=defects(U,V,n,q)
            mass=len(U)*len(V)
            bit=int(0 in U and 0 in V)
            groups[key].append((mass,bit))
    cross=0
    for g in groups.values():
        for i in range(len(g)):
            for j in range(i):
                if g[i][0] != g[j][0]:
                    cross+=1
                    assert g[i][1] != g[j][1]
    assert cross>0
    return dict(n=n,q=q,cross_mass_pairs=cross,one_fixed_probe_suffices=True)


def symbolic_family_witness(n,q,missing_pair=0):
    m=n//2
    U=frozenset((missing_pair+j)%n for j in range(1,m))
    U2=U|frozenset({missing_pair,(missing_pair+m)%n})
    V=tuple(range(q))
    assert defects(U,V,n,q)==defects(U2,V,n,q)
    assert len(U2)-len(U)==2
    assert U2-U==frozenset({missing_pair,(missing_pair+m)%n})
    return dict(n=n,q=q,lower_mass=q*(m-1),upper_mass=q*(m+1),different_coordinates=sorted(U2-U))


if __name__=='__main__':
    records=[check(4,5),check(6,5),check(8,3),check(10,3)]
    print(json.dumps(dict(status='ALL PASS',exact_finite_cases=records,
       odd_cases=[check_odd(n,q) for n,q in [(1,5),(3,5),(5,3)]],
       structured_lower_witness=[symbolic_family_witness(n,q) for n,q in [(4,5),(6,5),(8,3),(10,11)]],
       scope='fully indexed spectra, unknown nonempty product factors, fixed local physical bits'),
       indent=2,ensure_ascii=False,sort_keys=True))
