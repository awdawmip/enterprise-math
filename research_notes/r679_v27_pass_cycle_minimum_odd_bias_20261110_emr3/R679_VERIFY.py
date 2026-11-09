#!/usr/bin/env python3
"""R679: exact V23/V27/V29 PASS-cycle odd-holonomy bias certificate.
All arithmetic is integer and combinatorial. No external packages are required.
Usage: python R679_VERIFY.py > R679_EVIDENCE_and_pass.txt
"""
import json
from collections import Counter
from itertools import combinations, permutations, product
from math import comb

AXES=range(6)
TRIADS=tuple(combinations(AXES,3))
MATCHINGS=(
 ((0,1),(2,3),(4,5)),
 ((0,2),(1,4),(3,5)),
 ((0,3),(1,5),(2,4)),
 ((0,4),(1,3),(2,5)),
)
def field_eval(matching,triad):
    s=set(triad); bits=[]
    for a,b in matching:
        if int(a in s)+int(b in s)!=1:return 0
        bits.append(int(b in s))
    return 1 if sum(bits)%2==0 else -1
C={s:tuple(field_eval(m,s) for m in MATCHINGS) for s in TRIADS}
N={s:tuple(t for t in TRIADS if len(set(t)&set(s))==2) for s in TRIADS}
assert len(TRIADS)==20 and len(set(C.values()))==20
assert all(len(N[s])==9 for s in TRIADS) and C[(0,1,2)]==(0,0,1,1)

PASS=((0,1),(1,2),(2,0))
ZERO=[[0]*4 for _ in range(4)]
def after_pass(du,om,a,b):
    du=list(du);om=[list(row) for row in om]
    du[a]+=1;du[b]-=1
    om[a][b]+=1;om[b][a]-=1
    return tuple(du),om
STAGES=[((0,0,0,0),ZERO)]
for a,b in PASS: STAGES.append(after_pass(*STAGES[-1],a,b))
assert STAGES[-1][0]==(0,0,0,0)
assert STAGES[-1][1]==[[0,1,-1,0],[-1,0,1,0],[1,-1,0,0],[0,0,0,0]]

def phi(u,om,s,t):
    cs,ct=C[s],C[t]
    return sum(u[i]*ct[i] for i in range(4))+sum(cs[i]*om[i][j]*ct[j] for i in range(4) for j in range(4))

def winner_map(u,om):
    out={}; ties=0;gap=None
    for s in TRIADS:
        scores=[(phi(u,om,s,t),t) for t in N[s]]
        top=max(score for score,_ in scores)
        maximizers=[t for score,t in scores if score==top]
        if len(maximizers)>1:
            ties+=1
        else:
            out[s]=maximizers[0]
            second=max(score for score,t in scores if t!=maximizers[0])
            delta=top-second
            gap=delta if gap is None else min(gap,delta)
    return out,ties,gap

def cycles_of(f):
    visited=set(); cycles=[]
    for s in TRIADS:
        if s in visited: continue
        seen={}; trace=[]; x=s
        while x not in visited and x not in seen:
            seen[x]=len(trace); trace.append(x); x=f[x]
        if x in seen: cycles.append(tuple(trace[seen[x]:]))
        visited.update(trace)
    return cycles

def holonomy(cycle):
    if len(cycle)<2:return None
    start=cycle[0]; slot={a:i for i,a in enumerate(start)}
    for idx,s in enumerate(cycle):
        t=cycle[(idx+1)%len(cycle)]; common=set(s)&set(t)
        assert len(common)==2
        left=next(iter(set(s)-common)); enter=next(iter(set(t)-common))
        slot={a:slot[a] for a in common}|{enter:slot[left]}
    return tuple(slot[a] for a in start)

def inspect(u,om):
    f,ties,gap=winner_map(u,om)
    if ties:return None
    cyc=cycles_of(f)
    hol=tuple(holonomy(c) for c in cyc)
    return {'gap':gap,'cycles':cyc,'holonomies':hol,'odd':any(h!=(0,1,2) for h in hol)}

def vectors_of_norm(k):
    if k==0:
        yield (0,0,0,0);return
    # Every vector of L1 norm k has a unique nonzero support, a composition
    # of k into positive magnitudes on the support, and independent signs.
    for j in range(1,min(4,k)+1):
        for supp in combinations(range(4),j):
            for cuts in combinations(range(1,k),j-1):
                sizes=tuple(b-a for a,b in zip((0,)+cuts,cuts+(k,)))
                for signs in product((-1,1),repeat=j):
                    u=[0]*4
                    for i,size,sign in zip(supp,sizes,signs):u[i]=size*sign
                    yield tuple(u)

def count_formula(k):
    if not k:return 1
    return sum(comb(4,j)*comb(k-1,j-1)*2**j for j in range(1,min(4,k)+1))

results=[]; minimizers=[]; searched=0
for norm in range(20):
    total=strict=odd=0
    for u in vectors_of_norm(norm):
        total+=1;searched+=1
        result=inspect(u,STAGES[-1][1])
        if result is None: continue
        strict+=1
        if result['odd']:
            odd+=1
            if norm==19:minimizers.append(u)
    assert total==count_formula(norm)
    results.append({'l1_norm':norm,'tested':total,'globally_strict':strict,'odd_holonomy':odd})
assert all(x['odd_holonomy']==0 for x in results[:19])
assert results[19]['odd_holonomy']==6
expected={(-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),(2,4,3,-10),(3,2,4,-10),(4,3,2,-10)}
assert set(minimizers)==expected

# For each minimizer, every possible FIRST primitive PASS causes at least one
# tied active triad; the three PASS events can be ordered arbitrarily.
first_step_tie_counts=[]
for u in sorted(minimizers):
    orig=inspect(u,STAGES[0][1])
    assert orig is not None and not orig['odd']
    fin=inspect(u,STAGES[3][1])
    assert fin is not None and fin['odd']
    ties={}
    for a,b in PASS:
        du,om=after_pass((0,0,0,0),ZERO,a,b)
        v=tuple(u[i]+du[i] for i in range(4))
        _,n_ties,_=winner_map(v,om)
        assert n_ties>=1
        ties[f'{a}->{b}']=n_ties
    first_step_tie_counts.append({'u':u,'first_PASS_tied_triads':ties,
      'final_min_gap':fin['gap'],
      'final_nontrivial_cycles':['->'.join(''.join(map(str,t)) for t in c)
        for c,h in zip(fin['cycles'],fin['holonomies']) if h!=(0,1,2)]})

v27=(-2,-4,-3,10)
assert v27 in minimizers
info=inspect(v27,STAGES[-1][1]); assert info['gap']==1
assert any(len(c)==6 and h!=(0,1,2) for c,h in zip(info['cycles'],info['holonomies']))
assert sum(e['tested'] for e in results)==searched
assert searched==sum(count_formula(k) for k in range(20))

output={
 'schema':'R679_PASS_CYCLE_MIN_ODD_BIAS_EXACT_V1',
 'date':'2026-11-10',
 'method':'Complete integer L1 spheres 0..19, 20 V23 triads each with 9 exact V27 neighbors, V17 slot transport',
 'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'pass_sequence':['0->1','1->2','2->0'],
 'final_omega':STAGES[-1][1],
 'final_du':STAGES[-1][0],
 'search':results,'total_bias_vectors':searched,
 'minimal_odd_l1':19,
 'number_of_minimizers':len(minimizers),
 'minimizers':first_step_tie_counts,
 'network_realization':{
    'example_field_u':v27,'bridge':(0,2,1,3),
    'port_u':(v27[0],v27[2],v27[1],v27[3]),
    'transfer_event_count':19,'internal_PASS_count':3,
    'total_primitive_event_count':22,
    'global_scalar_Q':'exactly zero at all stages for zero initial ledger'
 },
 'status':'AUTHOR_SIDE_EXACT_INTEGER_COMPUTATION_AND_FINITE_EXHAUSTIVE_PROOF'
}
print(json.dumps(output,ensure_ascii=False,indent=2))
print('R679_PASS_CYCLE_MIN_ODD_BIAS_EXACT_PASS')
