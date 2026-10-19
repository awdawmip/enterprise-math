#!/usr/bin/env python3
"""Exhaustive local verifier for the explicit constant-width ternary decoder.

Researcher: EM-DIRECT-66DE45
No RSA factor is used or produced.
"""
from collections import defaultdict


def canonical_pair(a,b,M):
    return tuple(sorted((a%M,b%M)))


def ramanujan_3e(e,t):
    m=3**e
    n=m//3
    t%=m
    if t==0:
        return 2*n
    if t%n==0:
        return -n
    return 0


def tau(e,r):
    m=3**e
    rr=r%(2*m)
    assert rr%2==1
    return ((rr+m)//2)%m


def z_trace(e,p,q,r):
    tp=tau(e,p)
    tq=tau(e,q)
    return (
        ramanujan_3e(e,tp-r)-ramanujan_3e(e,-tp-r)
       +ramanujan_3e(e,tq-r)-ramanujan_3e(e,-tq-r)
    )


def probes_from_prev(prev,e):
    n=3**(e-1)
    fibers=[]
    for rr in prev:
        t=tau(e-1,rr)%n
        if t not in fibers:
            fibers.append(t)
    probes=[]
    for t in fibers:
        probes.extend([t,t+n])
    assert len(probes) in (2,4)
    return probes


def code_digit(i,n):
    return ((2*n,-n),(-n,2*n),(-n,-n))[i]


def check_symbolic_tables():
    n=7  # arbitrary positive scale
    codes=[code_digit(i,n) for i in range(3)]
    assert len(set(codes))==3
    pair_codes={}
    for i in range(3):
        for j in range(i,3):
            v=(codes[i][0]+codes[j][0],codes[i][1]+codes[j][1])
            assert v not in pair_codes.values()
            pair_codes[(i,j)]=v
    expected={
        (0,0):(4*n,-2*n),
        (0,1):(n,n),
        (0,2):(n,-2*n),
        (1,1):(-2*n,4*n),
        (1,2):(-2*n,n),
        (2,2):(-2*n,-2*n),
    }
    assert pair_codes==expected
    print("symbolic ternary code tables: PASS")


def h2_residues(e):
    M=2*3**e
    return [r for r in range(1,M,2) if r%3==2]


def check_all_local_groups(e):
    """Group all level-e H2 pairs by (previous pair, product mod current M).

    Each group is exactly the set of product-compatible lifts visible from that
    previous residue pair. The predetermined probes must be injective on it.
    """
    M=2*3**e
    M0=2*3**(e-1)
    groups=defaultdict(list)
    R=h2_residues(e)
    for i,p in enumerate(R):
        for q in R[i:]:
            pair=(p,q)
            prev=canonical_pair(p,q,M0)
            key=(prev,(p*q)%M)
            groups[key].append(pair)

    max_group=0
    for (prev,_),candidates in groups.items():
        max_group=max(max_group,len(candidates))
        assert len(candidates)<=3
        probes=probes_from_prev(prev,e)
        values=[]
        for p,q in candidates:
            values.append(tuple(z_trace(e,p,q,r) for r in probes))
        assert len(set(values))==len(values),(e,prev,candidates,probes,values)
    print(f"e={e}: exhaustive local groups PASS; groups={len(groups)}, max candidates={max_group}")


def check_negative_sector_vanishes():
    for e in range(2,7):
        m=3**e
        n=m//3
        for rr in h2_residues(e):
            t=tau(e,rr)
            assert t%3==1
            for r in (t%n,(t%n)+n):
                # negative exponent is mod3=2 while r is mod3=1, so trace zero.
                assert ramanujan_3e(e,-t-r)==0
    print("H2 positive/negative sector separation: PASS")


if __name__=="__main__":
    check_symbolic_tables()
    check_negative_sector_vanishes()
    for e in range(2,6):
        check_all_local_groups(e)
    print("ALL CHECKS PASS")
