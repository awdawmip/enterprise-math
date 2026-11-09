#!/usr/bin/env python3
"""R679: exact V23/V27/V29 and labeled positive BRC event-word certificate.
Exhausts all integer four-field u with L1 norm <= 19.
"""
import json
from itertools import combinations, permutations
from collections import Counter
from math import prod

TRIADS = tuple(combinations(range(6), 3))
MATCH = (((0,1),(2,3),(4,5)), ((0,2),(1,4),(3,5)),
         ((0,3),(1,5),(2,4)), ((0,4),(1,3),(2,5)))
PASS = ((0,1),(1,2),(2,0))

def code(s, matching):
    if any((a in s)+(b in s)!=1 for a,b in matching):
        return 0
    return 1 if sum(b in s for a,b in matching)%2==0 else -1

C = {s:tuple(code(s,m) for m in MATCH) for s in TRIADS}
N = {s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
assert len(set(C.values()))==20
assert all(len(N[s])==9 for s in TRIADS)

def ledger(u, order):
    u=list(u); M=[[0]*4 for _ in range(4)]
    yield tuple(u),tuple(tuple(row) for row in M)
    for x in order:
        a,b=PASS[x]; M[a][b]+=1;u[a]+=1;u[b]-=1
        yield tuple(u),tuple(tuple(row) for row in M)

def skew(M):
    return tuple(tuple(M[i][j]-M[j][i] for j in range(4)) for i in range(4))

def winners(u,M):
    O=skew(M)
    p={t:sum(u[i]*C[t][i] for i in range(4)) for t in TRIADS}
    out={}
    for s in TRIADS:
        z={t:p[t]+sum(C[s][i]*O[i][j]*C[t][j] for i in range(4) for j in range(4)) for t in N[s]}
        mx=max(z.values())
        out[s]=tuple(t for t in N[s] if z[t]==mx)
    return out

def frames(cycle):
    slots={a:i for i,a in enumerate(cycle[0])}
    for s,t in zip(cycle,cycle[1:]+cycle[:1]):
        common=set(s)&set(t)
        old=next(iter(set(s)-common))
        new=next(iter(set(t)-common))
        slots={a:slots[a] for a in common}|{new:slots[old]}
    return tuple(slots[a] for a in cycle[0])

def shell(k):
    def rec(i,rem,values):
        if i==4:
            if rem==0: yield tuple(values)
            return
        for magnitude in range(rem+1):
            for v in ((0,) if magnitude==0 else (-magnitude,magnitude)):
                yield from rec(i+1,rem-magnitude,values+[v])
    yield from rec(0,k,[])

M=tuple(tuple(int((i,j) in PASS) for j in range(4)) for i in range(4))
O=skew(M)
K={s:{t:sum(C[s][i]*O[i][j]*C[t][j] for i in range(4) for j in range(4)) for t in N[s]} for s in TRIADS}

def final_cycles(u):
    p={t:sum(u[i]*C[t][i] for i in range(4)) for t in TRIADS}
    f={}
    for s in TRIADS:
        vals=[(p[t]+K[s][t],t) for t in N[s]]
        mx=max(x for x,t in vals)
        winners_here=[t for x,t in vals if x==mx]
        if len(winners_here)!=1: return None
        f[s]=winners_here[0]
    seen=set();cycles=[]
    for x in TRIADS:
        if x in seen:continue
        chain=[];pos={}
        while x not in pos and x not in seen:
            pos[x]=len(chain);chain.append(x);x=f[x]
        if x in pos:cycles.append(tuple(chain[pos[x]:]))
        seen.update(chain)
    return tuple((cyc,frames(list(cyc))) for cyc in cycles)

hist=[];witness=[]
for k in range(20):
    tested=strict=curved=0
    for u in shell(k):
        tested+=1
        cycles=final_cycles(u)
        if cycles is None:continue
        strict+=1
        if any(h!=(0,1,2) for cyc,h in cycles):
            curved+=1
            if k==19:witness.append((u,cycles))
    hist.append((k,tested,strict,curved))

assert sum(row[1] for row in hist)==97281
assert all(row[3]==0 for row in hist[:19])
assert hist[-1][3]==6
assert {u for u,cyc in witness}=={
    (-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),
    (2,4,3,-10),(3,2,4,-10),(4,3,2,-10)}

branches={}
for u,cycles in witness:
    details={}
    for word in permutations(range(3)):
        stages=[]
        for current_u,current_M in ledger(u,word):
            w=winners(current_u,current_M)
            stages.append({
                'ties':dict(sorted(Counter(map(len,w.values())).items())),
                'choice_sections':prod(map(len,w.values()))
            })
        assert [s['ties'].get(1,0)==20 for s in stages]==[True,False,False,True]
        details[''.join('ABC'[a] for a in word)]=stages
    branches[str(u)]=details

out={
 'schema':'R679_EXACT_FINITE_V23_V27_V29_BRC_V1',
 'status':'AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE',
 'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'domain':'integer u four-vector L1 <=19, fixed V29 nonnegative PASS 01,12,20',
 'total_tested':97281,
 'L1_shells':[{'norm':k,'tested':n,'globally_strict':s,'nonflat':c} for k,n,s,c in hist],
 'minimum_nonflat_L1_norm':19,
 'minimizers':[list(u) for u,cyc in witness],
 'minimizer_cycles':{str(u):[{'cycle':[''.join(map(str,x)) for x in cyc],'holonomy':list(h)} for cyc,h in cycles] for u,cycles in witness},
 'labeled_positive_BRC_prefix_branches':branches,
 'boundary_TRANSFER_unit_min_in_separated_class':19,
 'triadic_PASS_unit_events':3,
 'total_event_min_in_separated_class':22
}
print(json.dumps(out,ensure_ascii=False,indent=2))
print('R679_THREE_PASS_MINIMAL_CURVATURE_BRC_EXACT_PASS')
