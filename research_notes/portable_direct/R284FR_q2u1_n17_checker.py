#!/usr/bin/env python3
"""R284FR: q=2,u=1 reset-free four-phase code has sharp minimum n=18.

This exact finite lower-bound checker extends the already published
R284FQ_q2u1_n16_checker.py. Run from the same folder at the pinned Git commit.
All 17-bit column permutations reduce to 100,947 seven-pattern histograms.
Check all six last-update flow cuts, exact stable/noisy forced read labels,
then all possible first bits, then a necessary locally safe prefix lattice
for every changed pattern type. Every remaining case fails on a publication edge.
"""
import json
from collections import deque
from math import comb
from itertools import combinations
import R284FQ_q2u1_n16_checker as base

assert (base.Q,base.U)==(2,1)
base.N=17

def has_safe_order(words,pp,stable_states,forced,phase):
    nxt=(phase+1)%4
    old,new=1<<phase,1<<nxt
    allowed=old|new
    groups=tuple(tuple(k for k,p in enumerate(pp) if p==kind)
                 for kind in sorted(set(pp))
                 if base.PAT[kind][0][phase]!=base.PAT[kind][0][nxt])
    lengths=tuple(map(len,groups))
    assert sum(lengths)==(words[phase]^words[nxt]).bit_count()
    zero=(0,)*len(groups)
    queue=deque([zero])
    seen={zero}
    checked=0
    safe=0
    while queue:
        current=queue.popleft()
        if current==lengths:
            return True,checked,safe
        for k in range(len(groups)):
            if current[k]>=lengths[k]:continue
            attempt=list(current)
            attempt[k]+=1
            attempt=tuple(attempt)
            if attempt in seen:continue
            seen.add(attempt)
            checked+=1
            attempted=tuple(pos for group,count in zip(groups,attempt)
                            for pos in group[:count])
            mask=sum(1<<pos for pos in attempted)
            omissions=[0]+[sum(1<<pos for pos in subset)
                      for r in range(1,min(2,len(attempted))+1)
                      for subset in combinations(attempted,r)]
            valid=True
            for source in stable_states[phase]:
                baseline=(source&~mask)|(words[nxt]&mask)
                for omitted in omissions:
                    physical=baseline ^ ((source^words[nxt])&omitted)
                    labels=forced[physical]
                    if labels&~allowed or (labels&allowed)==allowed:
                        valid=False
                        break
                if not valid:break
            if valid:
                queue.append(attempt)
                safe+=1
    return False,checked,safe

def main():
    candidates=[h for h in base.compositions(base.N) if base.necessary(h)]
    assert len(candidates)==208
    first_survivors=0
    lattice_excluded=0
    edge_exclusion_counts=[0]*4
    examples=[]
    for hist in candidates:
        words,types=base.words_and_types(hist)
        stable=[base.stable(words,i) for i in range(4)]
        forced=base.observed_masks(stable)
        first=[base.first_bit_choices(words,stable,forced,i) for i in range(4)]
        if not all(first):
            continue
        first_survivors+=1
        for phase in range(4):
            path,checked,safe=has_safe_order(words,types,stable,forced,phase)
            if not path:
                lattice_excluded+=1
                edge_exclusion_counts[phase]+=1
                if len(examples)<12:
                    examples.append({"histogram":hist,"blocked_edge":phase,
                                     "lattice_nodes_checked":checked,
                                     "locally_safe_nodes":safe})
                break
        else:
            raise AssertionError(("17-bit scheme survives necessary prefix lattice",hist))
    assert first_survivors==108 and lattice_excluded==108
    report={"result":"n_min(2,1)=18 using previously proved 18-bit Gray upper construction",
            "model":{"q":2,"u":1,"n_excluded":17},
            "histogram_classes":comb(base.N+6,6),
            "six_flow_cut_survivors":len(candidates),
            "histograms_passing_first_bit_each_edge":first_survivors,
            "no_locally_safe_order_on_some_edge":lattice_excluded,
            "remaining_candidates":0,
            "first_blocking_edge_counts":edge_exclusion_counts,
            "sample_lattice_obstructions":examples,
            "repro_dependency":"R284FQ_q2u1_n16_checker.py",
            "proof_scope":"exact finite obstruction, four fixed words, persistent q omissions, one noisy read flip, stateless no-rollback observer",
            "independent_math_review":"NOT_REVIEWED"}
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
