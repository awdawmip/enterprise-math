#!/usr/bin/env python3
"""R642 exact finite triad histogram parity and one-trit residual."""
from collections import Counter, deque
from itertools import combinations, permutations
import json
from pathlib import Path

V=tuple(combinations(range(6),3))
ADJ={s:tuple(t for t in V if len(set(s)&set(t))==2) for s in V}
BASE=(0,1,2)
ID=(0,1,2)
def compose(p,q): return tuple(p[q[i]] for i in range(3))
def power(p,k):
    q=ID
    for _ in range(k): q=compose(q,p)
    return q
rho=(1,2,0); tau=(1,0,2)
normal={(q,e):compose(power(rho,q),power(tau,e)) for q in range(3) for e in range(2)}
inv_normal={p:key for key,p in normal.items()}
assert len(inv_normal)==6

def transport(s,sigma,t):
    assert t in ADJ[s]
    current=dict(zip(s,sigma))
    leave=next(iter(set(s)-set(t)))
    enter=next(iter(set(t)-set(s)))
    after={x:current[x] for x in (set(s)&set(t))}
    after[enter]=current[leave]
    return tuple(after[x] for x in t)

def edge_f(s,t): return transport(s,ID,t)
def edge_bit(s,t):
    leaving=next(iter(set(s)-set(t)))
    entering=next(iter(set(t)-set(s)))
    return (s.index(leaving)+t.index(entering))%2
def parity(p): return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
def hist(path): return Counter(zip(path,path[1:]))

def endpoint_from_hist(h, start=BASE):
    flow=Counter()
    for (s,t),m in h.items():
        flow[s]+=m
        flow[t]-=m
    nonzero={v:b for v,b in flow.items() if b}
    if not nonzero: return start
    assert len(nonzero)==2 and nonzero[start]==1
    return next(v for v,b in nonzero.items() if b==-1)

def run(path):
    sigma=ID
    assert path[0]==BASE
    for s,t in zip(path,path[1:]): sigma=transport(s,sigma,t)
    return sigma
def traced(path):
    s=BASE; q=e=0; h=Counter()
    for t in path[1:]:
        qe,ee=inv_normal[edge_f(s,t)]
        assert ee==edge_bit(s,t)
        q=(q+(-1 if e else 1)*qe)%3
        e=(e+ee)%2
        h[s,t]+=1; s=t
        assert e==sum(edge_bit(a,b)*n for (a,b),n in h.items())%2
    return normal[q,e],(q,e),h

assert len(V)==20 and all(len(ADJ[s])==9 for s in V)
all_edges=[(s,t) for s in V for t in ADJ[s]]
for s,t in all_edges: assert parity(edge_f(s,t))==edge_bit(s,t)
checks=0
for s in V:
    for sigma in permutations(range(3)):
        q,e=inv_normal[sigma]
        for t in ADJ[s]:
            qe,ee=inv_normal[edge_f(s,t)]
            nq=(q+(-1 if e else 1)*qe)%3
            ne=(e+ee)%2
            assert normal[nq,ne]==transport(s,sigma,t)
            checks+=1
assert checks==1080

A=(BASE,(0,1,3),(0,2,3),BASE)
B=(BASE,(0,1,3),(1,2,3),BASE)
assert run(A)==(0,2,1) and run(B)==(2,1,0)
paths={
"AABB":A+A[1:]+B[1:]+B[1:],
"ABAB":A+B[1:]+A[1:]+B[1:],
"BABA":B+A[1:]+B[1:]+A[1:],
}
h0=None
for name,path in paths.items():
    f,(q,e),hh=traced(path)
    assert f==run(path) and e==0
    if h0 is None: h0=hh
    else: assert hh==h0
assert {run(p) for p in paths.values()}=={ID,rho,power(rho,2)}
odd_paths={name:path+A[1:] for name,path in paths.items()}
ho=None
for name,path in odd_paths.items():
    f,(q,e),hh=traced(path)
    assert e==1 and parity(f)==1
    if ho is None: ho=hh
    else: assert hh==ho
assert len({run(p) for p in odd_paths.values()})==3

seen={(BASE,ID,0,0)}
queue=deque(seen)
while queue:
    s,p,q,e=queue.popleft()
    for t in ADJ[s]:
        qe,ee=inv_normal[edge_f(s,t)]
        nxt=(t,transport(s,p,t),(q+(-1 if e else 1)*qe)%3,(e+ee)%2)
        assert normal[nxt[2],nxt[3]]==nxt[1]
        if nxt not in seen:
            seen.add(nxt); queue.append(nxt)
assert len(seen)==120
# Check endpoint recovery from complete histogram on a shortest legal path
# to each of the 120 reachable states and all 1080 one-edge extensions.
paths_to_state={(BASE,ID):(BASE,)}
frontier=deque([(BASE,ID)])
endpoint_checks=0
while frontier:
    s,p=frontier.popleft()
    path=paths_to_state[(s,p)]
    assert endpoint_from_hist(hist(path))==s
    endpoint_checks+=1
    for t in ADJ[s]:
        next_path=path+(t,)
        assert endpoint_from_hist(hist(next_path))==t
        endpoint_checks+=1
        nxt=(t,transport(s,p,t))
        if nxt not in paths_to_state:
            paths_to_state[nxt]=next_path
            frontier.append(nxt)
assert len(paths_to_state)==120 and endpoint_checks==120+1080
result={
"marker":"R642_HISTOGRAM_PARITY_SHARP_TRIT_REPAIR_PASS",
"date":"2026-11-08","vertices":len(V),"directed_edges":len(all_edges),
"edge_parity_checks":len(all_edges),"slot_transition_checks":checks,
"reachable_states":len(seen),
"endpoint_recovery_checks":endpoint_checks,
"even_shared_histogram":{str(a)+"->"+str(b):n for (a,b),n in sorted(h0.items())},
"even_outcomes":{k:list(run(v)) for k,v in paths.items()},
"odd_outcomes":{k:list(run(v)) for k,v in odd_paths.items()},
"worst_case_same_histogram_fiber":3,
"added_residual":"q modulo3, parity epsilon from directed edge histogram",
"frozen_science":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
"V26_source_commit":"b62110008321d9147212cb89f2627ff613c2550d",
"proof_status":"author exact derivation, finite exact checker, unreviewed"
}
Path(__file__).with_name("R642_EVIDENCE.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
print(result["marker"],"edges",len(all_edges),"updates",checks,"states",len(seen))
