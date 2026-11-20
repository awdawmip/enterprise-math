"""R762GR exact orientation quotient and rational moments for the constructed
moving named-Port K4-STAR candidate (not a native force event law).
Python 3 with sympy for exact rational linear systems.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from fractions import Fraction
from sympy import Matrix
import json

E = tuple(combinations(range(4),2))
S = [tuple(E.index(tuple(sorted((v,u)))) for u in range(4) if u != v)
     for v in range(4)]
I = tuple(range(6))
P = [p for p in permutations(I)
     if sum(p[a]>p[b] for a in I for b in range(a+1,6))%2 == 0]
PI = {p:i for i,p in enumerate(P)}
def mul(p,q): return tuple(p[q[i]] for i in I)
def cycle(star):
    q=list(I); a,b,c=star; q[a],q[b],q[c]=b,c,a
    return tuple(q)
G=[cycle(s) for s in S]
N=[tuple(g.index(i) for i in I) for g in G]
arcs=[[PI[mul(p,G[v] if sign==1 else N[v])]
       for v in E[p[0]] for sign in (-1,1)] for p in P]
absorbing={i for i,p in enumerate(P) if p[0]==5}
assert len(P)==360 and len(absorbing)==60
assert all(set(arcs[i])<=absorbing for i in absorbing)
initial=PI[I]
reachable={initial};queue=deque([initial])
while queue:
    i=queue.popleft()
    for j in arcs[i]:
        if j not in reachable:
            reachable.add(j);queue.append(j)
transient=reachable-absorbing
assert len(reachable)==350 and len(transient)==290

# Edge-induced vertex relabelings fixing initial unordered edge 01.
H=[]
for b in permutations(range(4)):
    if set((b[0],b[1]))=={0,1}:
        q=tuple(E.index(tuple(sorted((b[u],b[v])))) for u,v in E)
        H.append(q)
assert len(H)==4
def conjugation_orbit(i):
    p=P[i]; out=set()
    for q in H:
        inv=[q.index(x) for x in I]
        out.add(PI[tuple(q[p[inv[x]]] for x in I)])
    return frozenset(out)
orbits=sorted({conjugation_orbit(i) for i in transient},key=min)
assert len(orbits)==74
assert Counter(map(len,orbits))==Counter({4:72,1:2})
index={i:k for k,O in enumerate(orbits) for i in O}
assert len(index)==290
Q=[[0]*74 for _ in range(74)]
for k,O in enumerate(orbits):
    for i in sorted(O):
        cnt=Counter(index[j] for j in arcs[i] if j in transient)
        if i==min(O):
            for j,value in cnt.items():Q[k][j]=value
        else:
            assert all(Q[k][j]==cnt[j] for j in range(74))
assert sum(bool(v) for row in Q for v in row)==256
assert Counter(4-sum(row) for row in Q)==Counter({0:40,1:34})

# Coarsest absorption-respecting Markov equitable partition.
blocks={i:int(i in absorbing) for i in reachable}
steps=0
while True:
    sig={i:(int(i in absorbing),tuple(sorted(Counter(blocks[j]
         for j in arcs[i]).items()))) for i in reachable}
    keys={key:k for k,key in enumerate(sorted(set(sig.values()))}
    nxt={i:keys[sig[i]] for i in reachable}
    steps+=1
    if len(set(nxt.values()))==len(set(blocks.values())):
        assert all((blocks[i]==blocks[j])==(nxt[i]==nxt[j])
                   for i in reachable for j in reachable)
        break
    blocks=nxt
assert len(set(nxt.values()))==75
assert len({nxt[i] for i in absorbing})==1
for O in orbits:
    assert len({nxt[i] for i in O})==1
    assert sum(nxt[i]==nxt[min(O)] for i in transient)==len(O)

# The 8-step contraction of R762GO/GQ proves M=4I-Q invertible.
M=Matrix(74,74,lambda i,j:(4 if i==j else 0)-Q[i][j])
ones=Matrix([4]*74)
mean=M.inv()*ones
rhs_second=ones+2*Matrix([sum(Q[i][j]*mean[j] for j in range(74)) for i in range(74)])
second=M.inv()*rhs_second
m=mean[index[initial]];s=second[index[initial]];variance=s-m**2
assert Fraction('12.93946845281426419721')<m<Fraction('12.93946845281426419722')
assert Fraction('263.58902488422540237226')<s<Fraction('263.58902488422540237227')
assert Fraction('96.15918104284983428470')<variance<Fraction('96.15918104284983428471')

# Full unquotiented transient-state BRC source count cross-check.
source={initial:1};counts={}
for t in range(17):
    counts[t]=sum(source.values())
    nxt=Counter()
    for i,c in source.items():
        for j in arcs[i]:
            if j in transient:nxt[j]+=c
    source=nxt
assert counts[12]==6534252 and counts[16]==1118196052
assert counts[0]==1 and counts[1]==4 and counts[2]==16

out={"schema":"R762GR_CERTIFICATE_V1","candidate":"MOVING_NAMED_PORT_K4_STAR",
     "frozen_p000_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
     "orientation_states":360,"reachable":350,"transient":290,"absorbing":60,
     "symmetry_group_order":4,"transient_orbits":74,"transient_orbit_sizes":{"4":72,"1":2},
     "coarsest_absorption_respecting_lump_classes":75,
     "quotient_nonzero_entries":256,"quotient_equitability":"PASS",
     "partition_refinement_rounds":steps,
     "mean_tau":{"numerator":str(m.p),"denominator":str(m.q)},
     "second_tau":{"numerator":str(s.p),"denominator":str(s.q)},
     "variance_tau":{"numerator":str(variance.p),"denominator":str(variance.q)},
     "source_survivors":{"12":counts[12],"16":counts[16]},
     "author_check":"PASS","independent_review":"NOT_REVIEWED"}
print(json.dumps(out,indent=2,ensure_ascii=False))
