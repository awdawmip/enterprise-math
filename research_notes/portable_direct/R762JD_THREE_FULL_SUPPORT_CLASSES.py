#!/usr/bin/env python3
"""Exact finite verification for three additional 46->44 full-support Port-Euler histograms.

Run in the same directory as R762JC_SEVEN_TRIPLE_46_44.py; requires NumPy and
SciPy/HiGHS for constructing integer edge allocations. Checks are integer-only.
"""
from itertools import combinations
from collections import Counter
from R762JC_SEVEN_TRIPLE_46_44 import (
    P, T, M, perms, triangle_components, solve, verify_exact
)

def essential_reps(triple_count):
    essential=[]
    for t in combinations(range(20),triple_count):
        c=triangle_components(t)
        if all(triangle_components(t[:i]+t[i+1:])>c for i in range(triple_count)):
            essential.append(sum(1<<s for s in t))
    left=set(essential); full=set(essential); out=[]
    while left:
        m=min(left)
        orbit={sum(1<<q[s] for s in range(20) if (m>>s)&1) for q in perms}
        assert orbit<=full
        out.append((m,len(orbit)))
        left-=orbit
    assert sum(sz for _,sz in out)==len(essential)
    return len(essential),out

def run_class(triple_count,single_count,expected):
    assert 3*triple_count+single_count+2*(20-triple_count-single_count)==46
    essential,reps=essential_reps(triple_count)
    cases=labelled=0;inact=Counter();cuts=Counter()
    for mask,orbit_size in reps:
        triple=[s for s in range(20) if (mask>>s)&1]
        covered={u for s in triple for u in T[s]}
        other=[s for s in range(20) if s not in triple]
        for missing in M:
            if not set(missing).isdisjoint(covered):continue
            for singles in combinations(other,single_count):
                singleton_set=set(singles)
                counts=[3 if s in triple else 1 if s in singleton_set else 2 for s in range(20)]
                counts[triple[0]]=1
                allocation,rounds=solve(counts,missing)
                verify_exact(allocation,counts,missing)
                cases+=1;labelled+=orbit_size
                inact[len(missing)]+=1;cuts[rounds]+=1
    observed=(essential,len(reps),cases,labelled,dict(inact),dict(cuts))
    assert observed==expected,(triple_count,observed,expected)
    print(f'PASS ({triple_count},{20-triple_count-single_count},{single_count},0): '
          f'essential={essential} orbits={len(reps)} '
          f'certificates={cases} labelled={labelled} inactive={dict(sorted(inact.items()))} '
          f'cut-rounds={dict(sorted(cuts.items()))}',flush=True)

def main():
    expected={
        (8,2):(4920,16,1650,455400,{0:1056,1:528,2:66},{0:1639,1:11}),
        (9,3):(240,2,495,49500,{0:330,1:165},{0:494,1:1}),
        (10,4):(6,1,210,1260,{0:210},{0:210}),
    }
    for (triples,singles),counts in expected.items():
        run_class(triples,singles,counts)
    print('PASS R762JD ALL THREE CLASSES: 2355/2355 EXACT CONNECTED EULER WITNESSES')

if __name__=='__main__':main()
