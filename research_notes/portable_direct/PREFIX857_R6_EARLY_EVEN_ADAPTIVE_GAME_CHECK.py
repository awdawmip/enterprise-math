#!/usr/bin/env python3
"""PREFIX-857: complete exact time-dependent feedback game for 5 named binary BRC sources.
No-op/one named bit flip per heartbeat; all raw moduli 1..16; no X6 attribution.
"""
import json
from math import gcd
P=5; STATES=range(1<<P); FULL=(1<<len(STATES))-1; MMAX=16
MOVES=tuple(tuple([x]+[x^(1<<i) for i in range(P)]) for x in STATES)
RES_MASK={q:tuple(sum(1<<x for x in STATES if x%q==r) for r in range(q)) for q in range(1,MMAX+1)}
def qm(t):
    c=1<<(t//2)
    return tuple(sorted({m//gcd(m,c) for m in range(1,MMAX+1)}))
def next_states(mask):
    out=0
    while mask:
        bit=mask&-mask; mask-=bit; x=bit.bit_length()-1
        for y in MOVES[x]:out |=1<<y
    return out
def children(mask,q):
    post=next_states(mask)
    return tuple(z for R in RES_MASK[q] if (z:=post&R))
assert qm(8)==(1,3,5,7,9,11,13,15)
reachable={0:{FULL}}
for t in range(1,9):
    reachable[t]={child for b in reachable[t-1] for q in qm(t) for child in children(b,q)}
# Close all heartbeat-8 beliefs under the stationary late observer family.
late=list(sorted(reachable[8]));seen=set(late);edges=[]
for b in late:
    row=[]
    for q in qm(8):
        cs=children(b,q);row.append(cs)
        for child in cs:
            if child not in seen:seen.add(child);late.append(child)
    edges.append(tuple(row))
assert FULL in seen
winning={b for b in late if b.bit_count()==1};late_layers=[len(winning)]
while True:
    new={b for b,row in zip(late,edges) if b not in winning and any(all(c in winning for c in cs) for cs in row)}
    if not new:break
    winning|=new;late_layers.append(len(winning))
assert len(late)==8796 and late_layers==[32,56]
losing=set(late)-winning
assert all(any(c in losing for c in cs) for b,row in zip(late,edges) if b in losing for cs in row)
# Backward induction on early time, ending at exact infinite-horizon odd stage.
W={8:reachable[8]&winning}
for t in range(7,0,-1):
    W[t]={b for b in reachable[t] if b.bit_count()==1 or any(all(c in W[t+1] for c in children(b,q)) for q in qm(t+1))}
initial_winning_moduli=[q for q in qm(1) if all(c in W[1] for c in children(FULL,q))]
assert not initial_winning_moduli
assert [len(reachable[t]) for t in range(1,9)]==[136,1525,5164,9219,11528,12330,12496,8796]
assert [len(W[t]) for t in range(1,9)]==[4,69,94,96,96,96,96,56]
for t in range(1,32):
    assert set(qm(t+1)).issubset(qm(t))
def collisions(q0,q1):
    n=0
    for x in STATES:
        for y in STATES:
            if x%q0!=y%q0:continue
            for u in MOVES[x]:
                for v in MOVES[y]:
                    if u%q1==v%q1 and u!=v:n+=1
    return n
assert collisions(17,31)==0
result={
 'schema':'PREFIX857_R6_TEMPORAL_ADAPTIVE_GAME_V1',
 'status':'ALL_EXACT_ASSERTIONS_PASSED',
 'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'model':'Five named binary source positions, no-op/one-bit-flip each heartbeat, raw m<=16, c_t=2^floor(t/2), t>=1, arbitrary feedback/history',
 'effective_moduli_per_t':{str(t):list(qm(t)) for t in range(1,9)},
 'reachable_posterior_counts_per_t':{str(t):len(reachable[t]) for t in range(1,9)},
 'infinite_late_graph':{'states':len(late),'action_rows':len(late)*len(qm(8)),'winning_layers_cumulative':late_layers,'losing_states':len(losing),'all_losing_actions_have_losing_successor':True},
 'backward_winning_posterior_counts_per_t':{str(t):len(W[t]) for t in range(1,9)},
 'initial_four_bit_winning_moduli':initial_winning_moduli,
 'four_bit_adaptive_cold_start_from_t1':False,
 'four_bit_adaptive_cold_start_from_any_t_ge1':False,
 'action_set_temporal_nesting_checked_to_t':32,
 'five_bit_positive_schedule':[17,31],
 'five_bit_terminal_off_diagonal_collisions':collisions(17,31),
 'next_question':'derive a short invariant/certificate for the 1,896 and 8,740 losing-state regions; arbitrary p and multi-source flips; native observer bridge'
}
with open('PREFIX857_R6_EARLY_EVEN_ADAPTIVE_GAME_RESULTS.json','w') as f:
    f.write(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
