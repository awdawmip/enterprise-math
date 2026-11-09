#!/usr/bin/env python3
"""R681 exact V29 PASS port-symmetry and future-language checker (stdlib only).
This is a count/event semantics test, not a native physical propagator.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import factorial
import json

F=((0,1),(1,2),(2,0))
def sigma(i): return 2 if i==0 else 0 if i==2 else i
def rot(e): return (sigma(e[0]),sigma(e[1]))
B=tuple(map(rot,F))
E=F+B
assert len(set(E))==6 and not (set(F)&set(B))
assert set(map(rot,E))==set(E)
def ledger(word):
    m=[[0]*3 for _ in range(3)]
    for a,b in word: m[a][b]+=1
    u=tuple(sum(m[i][j]-m[j][i] for j in range(3)) for i in range(3))
    return m,u
def rotate(m):
    n=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3): n[sigma(i)][sigma(j)]=m[i][j]
    return n
def curvature(m):
    return sum(m[i][j]-m[j][i] for i,j in F)
words=tuple(w for k in range(7) for w in permutations(E,k))
subsets=tuple(frozenset(s) for k in range(7) for s in combinations(E,k))
assert len(words)==1957 and len(subsets)==64
mass=Counter(frozenset(w) for w in words)
assert all(mass[S]==factorial(len(S)) for S in subsets)
assert [sum(len(w)==k for w in words) for k in range(7)]==[1,6,30,120,360,720,720]
for w in words:
    m,u=ledger(w)
    mr,ur=ledger(tuple(map(rot,w)))
    assert mr==rotate(m) and ur==tuple(u[sigma(i)] for i in range(3))
    assert curvature(mr)==-curvature(m)
    assert sum(u)==0
    assert m==ledger(tuple(sorted(w)))[0]
assert len({frozenset(E)-S for S in subsets})==64
fixed=[S for S in subsets if S==frozenset(map(rot,S))]
orbits={frozenset((S,frozenset(map(rot,S)))) for S in subsets}
assert len(fixed)==8 and len(orbits)==36
assert F[0] in {F[0]} and F[0] not in {rot(F[0])}  # named-future counterexample
forward,_=ledger(F)
assert curvature(forward)==3
completion=[sum(ledger(F+choice)[0]==rotate(ledger(F+choice)[0])
                for choice in combinations(B,k)) for k in range(4)]
assert completion==[0,0,0,1]
complete,du=ledger(E)
assert complete==rotate(complete) and curvature(complete)==0 and du==(0,0,0)
assert all(ledger(w)==(complete,du) for w in permutations(E))
for values in product(range(3),repeat=6):
    m=[[0]*3 for _ in range(3)]
    for e,n in zip(E,values):m[e[0]][e[1]]=n
    assert curvature(rotate(m))==-curvature(m)
    if m==rotate(m): assert curvature(m)==0

# Exact R679 V23/V27 source-state and nine-neighbor static Ω=0 selector.
match=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),
       ((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
triads=tuple(combinations(range(6),3))
def c(s,m):
    if any((a in s)+(b in s)!=1 for a,b in m): return 0
    return 1 if sum(b in s for a,b in m)%2==0 else -1
C={s:tuple(c(s,m) for m in match) for s in triads}
neighbors={s:tuple(t for t in triads if len(set(s)&set(t))==2) for s in triads}
assert len(set(C.values()))==20 and all(len(v)==9 for v in neighbors.values())
biases=((-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),
        (2,4,3,-10),(3,2,4,-10),(4,3,2,-10))
cycles={}
for u in biases:
    p={s:sum(u[i]*C[s][i] for i in range(4)) for s in triads}
    f={}
    for s in triads:
        winners=[v for v in neighbors[s] if p[v]==max(p[w] for w in neighbors[s])]
        assert len(winners)==1
        f[s]=winners[0]
    found=[];visited=set()
    for v in triads:
        if v in visited: continue
        seq=[];seen={};x=v
        while x not in seen and x not in visited:
            seen[x]=len(seq);seq.append(x);x=f[x]
        if x in seen:found.append(seq[seen[x]:])
        visited.update(seq)
    assert all(len(z)==2 for z in found)
    cycles[str(u)]=['<->'.join(''.join(map(str,t)) for t in z) for z in found]
out={
 "schema":"R681_V29_PORT_ORIENTATION_SYMMETRY_EXACT_V1",
 "status":"AUTHOR_SIDE_FINITE_CHECK_UNREVIEWED",
 "frozen_science":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
 "forward":[list(x) for x in F],
 "reverse":[list(x) for x in B],
 "sigma_port":"0<->2,1 fixed,3 fixed",
 "minimal_sigma_closed_alphabet":6,
 "minimum_additional_reverse_pass":3,
 "unique_minimum_multiset":True,
 "completion_counts_by_k":completion,
 "forward_curvature":3,
 "reverse_curvature":-3,
 "symmetrized_curvature":0,
 "once_only_history_words":len(words),
 "labeled_future_states":len(subsets),
 "sigma_fixed_subsets":len(fixed),
 "sigma_subset_orbits":len(orbits),
 "positive_BRC_masses_by_length":[1,6,30,120,360,720,720],
 "full_six_event_orders_checked":factorial(6),
 "three_port_count_matrices_checked":3**6,
 "R679_zero_omega_V27_cycles":cycles,
 "note":"No per-PASS V17/V39 coupling or native physical attribution"
}
with open("R681_EVIDENCE.json","w",encoding="utf-8") as f:
    json.dump(out,f,indent=2,ensure_ascii=False);f.write("\n")
print(json.dumps({k:out[k] for k in ("labeled_future_states",
 "sigma_fixed_subsets","sigma_subset_orbits","completion_counts_by_k",
 "positive_BRC_masses_by_length")},ensure_ascii=False))
print("R681_V29_PORT_ORIENTATION_SYMMETRY_COMPLETION_EXACT_PASS")
