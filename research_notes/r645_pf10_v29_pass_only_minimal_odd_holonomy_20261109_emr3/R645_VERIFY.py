#!/usr/bin/env python3
"""R645: exact complete bounded enumeration for V23/V27 score with V29 PASS-only ledgers.
All arithmetic integer; strict orbit stops on tie or first repeated triad (at most 20 steps).
"""
from itertools import combinations, combinations_with_replacement
import json

TRI = tuple(combinations(range(6),3))
MATCH = (((0,1),(2,3),(4,5)),
         ((0,2),(1,4),(3,5)),
         ((0,3),(1,5),(2,4)),
         ((0,4),(1,3),(2,5)))
PASS = tuple((a,b) for a in range(4) for b in range(4) if a!=b)
NEI = {s:tuple(t for t in TRI if len(set(t)&set(s))==2) for s in TRI}

def code(m,s):
    S=set(s)
    if any((a in S)+(b in S)!=1 for a,b in m): return 0
    return 1 if sum(b in S for a,b in m)%2==0 else -1
C={s:tuple(code(m,s) for m in MATCH) for s in TRI}
assert len(TRI)==20 and len(set(C.values()))==20 and sum(map(len,NEI.values()))==180

def ledger(edges):
    M=[[0]*4 for _ in range(4)]
    for a,b in edges:M[a][b]+=1
    I=[sum(row) for row in M]
    O=[sum(M[a][b] for a in range(4)) for b in range(4)]
    u=[I[i]-O[i] for i in range(4)]
    W=[[M[i][j]-M[j][i] for j in range(4)] for i in range(4)]
    assert sum(u)==0
    assert all(v>=0 for row in M for v in row)
    assert all(u[i]==sum(W[i]) for i in range(4))
    return M,I,O,u,W

def score(s,t,u,W):
    return sum(u[i]*C[t][i] for i in range(4)) + sum(
        C[s][i]*W[i][j]*C[t][j] for i in range(4) for j in range(4))

def successor(s,u,W):
    values={t:score(s,t,u,W) for t in NEI[s]}
    mx=max(values.values())
    winning=[t for t in NEI[s] if values[t]==mx]
    if len(winning)!=1:return None,0
    other=max(values[t] for t in NEI[s] if t!=winning[0])
    return winning[0],mx-other

def holonomy(cycle):
    assert cycle[0]==cycle[-1]
    s=cycle[0];slots={k:i for i,k in enumerate(s)}
    for t in cycle[1:]:
        common=set(s)&set(t)
        assert len(common)==2
        left=next(iter(set(s)-common));enter=next(iter(set(t)-common))
        slots={**{k:slots[k] for k in common},enter:slots[left]}
        s=t
    return tuple(slots[k] for k in cycle[0])

def is_odd(h):
    return sum(h[i]>h[j] for i in range(3) for j in range(i+1,3))%2==1

def trace(s,u,W):
    visited={s:0};history=[s];gaps=[]
    for _ in range(20):
        nxt,gap=successor(s,u,W)
        if nxt is None:return None
        gaps.append(gap);history.append(nxt)
        if nxt in visited:
            cycle=history[visited[nxt]:]
            return {'prefix_len':visited[nxt],'history':history,
                    'cycle':cycle,'holonomy':holonomy(cycle),'gaps':gaps}
        visited[nxt]=len(history)-1;s=nxt
    raise AssertionError('Finite graph must repeat a triad by step 20')

# Exhaust all unordered multisets of n non-diagonal PASS events.
# A diagonal PASS changes only M_aa, not u/Omega or any V27 score.
summary={}
for n in range(5):
    odd=even=allstrict=0;from012=immediate012=0
    for inds in combinations_with_replacement(range(12),n):
        edges=[PASS[i] for i in inds]
        M,I,O,u,W=ledger(edges)
        for s in TRI:
            result=trace(s,u,W)
            if result is None: continue
            allstrict+=1
            h=result['holonomy']
            if h!=(0,1,2):
                if is_odd(h):
                    odd+=1
                    if s==(0,1,2):
                        from012+=1
                        if result['prefix_len']==0: immediate012+=1
                else: even+=1
    summary[str(n)]={'distinct_multisets':len(tuple(combinations_with_replacement(range(12),n))),
                     'strict_orbits_over_20_starts':allstrict,
                     'odd_cycle_orbits':odd,'even_nontrivial_cycle_orbits':even,
                     'odd_from_012':from012,'immediate_odd_from_012':immediate012}
    if n<=3:assert odd==0
assert summary['4']['odd_cycle_orbits']==60
assert summary['4']['immediate_odd_from_012']==2

EDGES=((0,1),(2,0),(2,3),(3,0))
M,I,O,u,W=ledger(EDGES)
assert I==[1,0,2,1] and O==[2,1,0,1] and u==[-1,-1,2,0]
CYCLE=((0,1,2),(0,2,4),(1,2,4),(0,1,2))
res=trace(CYCLE[0],u,W)
assert res and res['prefix_len']==0 and tuple(res['cycle'])==CYCLE
assert res['holonomy']==(1,0,2) and res['gaps']==[1,1,3]

# The four PASS events are actual V29 primitive operations. Applying all
# four after each selector update is a PROPOSED packet scheduler.
for n in range(151):
    E=EDGES*(n+1)
    Mn,In,On,un,Wn=ledger(E)
    assert Mn==[[(n+1)*v for v in row] for row in M]
    assert un==[(n+1)*v for v in u]
    S=CYCLE[n%3]; T=CYCLE[(n+1)%3]
    win,gap=successor(S,un,Wn)
    assert win==T and gap==(n+1)*(1,1,3)[n%3]

out={'marker':'R645_V29_PASS_ONLY_FOUR_EVENT_ODD_HOLONOMY_EXACT_PASS',
     'scope':'V23 code + V27 unique-neighbor score + V29 PASS-only counts; proposed packet-boundary selector',
     'source_original':'b62110008321d9147212cb89f2627ff613c2550d',
     'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
     'number_of_active_triads':len(TRI),
     'directed_triad_neighbors':sum(map(len,NEI.values())),
     'primitive_PASS_port_types':12,
     'enumeration':summary,
     'witness':{'events':EDGES,'M':M,'Rin':[0]*4,'Rout':[0]*4,
                'I':I,'O':O,'u':u,'Omega':W,'Q':sum(u),
                'triad_cycle':CYCLE,'strict_gaps':res['gaps'],'holonomy':res['holonomy']},
     'closed_form':'M_n=(n+1)M, u_n=(n+1)u, Omega_n=(n+1)Omega, score_n=(n+1)score_0',
     'exact_packet_samples':151,'formal_task_claim':False,
     'independent_driver_review':False}
print(json.dumps(out,ensure_ascii=False,indent=2))