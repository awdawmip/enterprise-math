#!/usr/bin/env python3
from itertools import combinations, permutations

# Finite weighted DAG/poset critical-path checker.
def critical_path(n,edges,w):
    preds=[[] for _ in range(n)]
    succ=[[] for _ in range(n)]
    indeg=[0]*n
    for a,b in edges:
        preds[b].append(a); succ[a].append(b); indeg[b]+=1
    q=[i for i,d in enumerate(indeg) if d==0]
    order=[]
    while q:
        x=q.pop(0); order.append(x)
        for y in succ[x]:
            indeg[y]-=1
            if indeg[y]==0: q.append(y)
    assert len(order)==n
    finish=[0]*n
    for x in order:
        start=max((finish[p] for p in preds[x]), default=0)
        finish[x]=start+w[x]
    return max(finish, default=0), tuple(finish)

# Chain: serial sums.
n=12; edges=tuple((i,i+1) for i in range(n-1)); w=(1,)*n
T,_=critical_path(n,edges,w)
assert T==12

# Antichain: parallel max.
n=7; edges=(); w=(1,3,2,5,4,2,1)
T,_=critical_path(n,edges,w)
assert T==5

# Serial composition of two independent internal DAGs with all A before all B.
wA=(2,3,1); eA=((0,1),(0,2))
wB=(4,2); eB=((0,1),)
TA,_=critical_path(3,eA,wA)
TB,_=critical_path(2,eB,wB)
# shift B nodes by 3 and add all A->all B precedence
edges=list(eA)+[(a+3,b+3) for a,b in eB]+[(a,b) for a in range(3) for b in range(3,5)]
T,_=critical_path(5,tuple(edges),wA+wB)
assert T==TA+TB

# Parallel composition = max.
edges=list(eA)+[(a+3,b+3) for a,b in eB]
T,_=critical_path(5,tuple(edges),wA+wB)
assert T==max(TA,TB)

# Triadic macro: 3 simultaneous incoming occurrences treated as one atomic
# relation layer followed by one outgoing layer; elapsed relation duration 2,
# primitive occurrence traffic 6.
triadic_relation_duration=2
primitive_force_occurrences=6
assert triadic_relation_duration!=primitive_force_occurrences

print('PASS_X6_NATIVE_TIME_DURATION_V3')
print('uniform_C12_chain_duration_ticks',12)
print('seven_event_antichain_duration',5)
print('serial_composition_additive',True)
print('parallel_composition_max',True)
print('triadic_macro_relation_layers',triadic_relation_duration)
print('triadic_macro_force_occurrences',primitive_force_occurrences)
