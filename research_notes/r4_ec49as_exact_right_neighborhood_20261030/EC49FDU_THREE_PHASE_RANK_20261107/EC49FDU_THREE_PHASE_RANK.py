#!/usr/bin/env python3
"""EC49FDU finite rank-only three-phase theorem; run with Python stdlib.
Frozen science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Source EC49FDT at 7ca6e255a07f27b26971d9918f520c9851d35de3.
The theorem is about observer-rank support, NOT native prefix optimization.
"""
from collections import Counter,defaultdict
from itertools import combinations, permutations
import json
from pathlib import Path

TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
CLAUSES=(18,20,33,40)
rank9=lambda m: all(m&c for c in CLAUSES)
states={(0,0,0,0,0,0,0):1}
horizon={};counts=[]
for h in range(1,10):
    next_states=defaultdict(int)
    for old,n in states.items():
        for step in range(6):
            new=list(old[:6]);new[step]+=1;new.append(TRANS[old[6]][step]);next_states[tuple(new)]+=n
    states=next_states
    masks=defaultdict(int);valid=accepted=0
    for s,n in states.items():
        na,nc,nd,ne,nf,ng,q=s
        if ne!=na+1: continue
        valid+=n
        if not SIG[q]:continue
        accepted+=n;z=ne;r=nc+nd
        masks[(2*z+r+nf,r+ng,z)]|=SIG[q]
    horizon[h]=dict(masks)
    counts.append((h,valid,accepted,len(masks),sum(map(rank9,masks.values()))))
assert counts[1:9]==[(2,8,6,3,1),(3,51,38,6,4),(4,304,206,13,9),
(5,1770,1062,21,17),(6,10224,5352,34,28),(7,58947,26644,49,43),
(8,340064,131686,70,62),(9,1964862,647930,94,86)]
keys=sorted(set().union(*(horizon[h] for h in range(4,10))))
assert len(keys)==155
individual={k:tuple(h for h in range(4,10) if rank9(horizon[h].get(k,0))) for k in keys}
assert all(not v or v==tuple(range(v[0],v[-1]+1)) for v in individual.values())
fullpairs={p for p in combinations(keys,2) if all(rank9(horizon[h].get(p[0],0)|horizon[h].get(p[1],0)) for h in range(4,10))}
assert len(fullpairs)==124
triples_good=withpair=threeonly=0
exceptions=[];switchpair_counter=Counter();schedule_multiplicity=Counter();threephase=0
certificate=[]
for t in combinations(keys,3):
    if any(not rank9(horizon[h].get(t[0],0)|horizon[h].get(t[1],0)|horizon[h].get(t[2],0)) for h in range(4,10)):continue
    triples_good+=1
    if any(p in fullpairs for p in combinations(t,2)):
        withpair+=1;continue
    threeonly+=1
    isolated=[h for h in range(4,10) if not any(rank9(horizon[h].get(k,0)) for k in t)]
    # Every rank-supporting triple has a 2-key subfamily for each local horizon.
    assert all(any(rank9(horizon[h].get(p[0],0)|horizon[h].get(p[1],0)) for p in combinations(t,2)) for h in range(4,10))
    if isolated:
        exceptions.append({'keys':t,'windows':isolated,
            'masks_at_h4':[horizon[4].get(k,0) for k in t],
            'individual_rank_windows':[individual[k] for k in t]})
        certificate.append({'keys':t,'schedule':[[0,1],[2],[2],[2],[2],[2]]})
        continue
    valid=[]
    for p,q in combinations(range(1,6),2):
        for order in permutations(range(3)):
            sched=([order[0]]*p+[order[1]]*(q-p)+[order[2]]*(6-q))
            if all(rank9(horizon[h].get(t[sched[h-4]],0)) for h in range(4,10)):
                valid.append((p,q,order,sched))
                switchpair_counter[(p+3,q+3)]+=1
    assert valid
    threephase+=1;schedule_multiplicity[len(valid)]+=1
    p,q,order,sched=min(valid)
    certificate.append({'keys':t,'schedule':sched,'switch_after':[p+3,q+3]})
assert (triples_good,withpair,threeonly,threephase,len(exceptions))==(23728,16994,6734,6730,4)
assert sum(v for v in schedule_multiplicity.values())==6730
assert sum(k*v for k,v in schedule_multiplicity.items())==14628
expected=[((2,3,1),(5,0,1),(6,4,1)),((2,3,1),(5,0,2),(6,4,1)),
((4,1,2),(5,0,1),(6,4,1)),((4,1,2),(5,0,2),(6,4,1))]
assert [tuple(map(tuple,x['keys'])) for x in exceptions]==expected
report={'schema':'EC49FDU_THREE_PHASE_RANK_V1',
'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
'ec49fdt_parent':'7ca6e255a07f27b26971d9918f520c9851d35de3',
'allowed_keys':len(keys),'rank_feasible_pairs':len(fullpairs),
'feasible_triples':triples_good,'with_feasible_pair':withpair,'genuinely_three':threeonly,
'standalone_rank_interval_lengths':dict(sorted(Counter(map(len,individual.values())).items())),
'one_key_per_window_three_contiguous_blocks':threephase,
'exceptional_h4_two_key_triples':exceptions,
'valid_three_block_schedules_per_triple':dict(sorted(schedule_multiplicity.items())),
'valid_schedule_switchpoint_occurrences':{str(k):v for k,v in sorted(switchpair_counter.items())},
'complete_schedule_certificate_count':len(certificate),
'certificate_scope':'Rank-nine only, H4..H9. Individual keys in schedules witness rank support; per-window quotas, legal paths, total cache count with early paths and signed-native-prefix cost remain to be optimized.'}
if __name__=='__main__':
    Path('EC49FDU_THREE_PHASE_RANK_RESULT.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    Path('EC49FDU_THREE_PHASE_RANK_CERTIFICATE.json').write_text(json.dumps(certificate,separators=(',',':'))+'\n',encoding='utf8')
    print(json.dumps(report,indent=2))
