"""Exact transcript quotient on the distinct-one-hole scheduled subfamily."""
from __future__ import annotations
import argparse
from itertools import permutations
from math import factorial, perm
from pathlib import Path
import json

def run(slots,schedule):
    M=slots+1
    b=slots.bit_length()
    B=1<<b
    windows=[tuple(range(1+t*M,1+(t+1)*M)) for t,d in schedule]
    common=tuple(sorted(k%B for k in windows[0]))
    assert all(set(k%B for k in w)==set(common) for w in windows)
    first={}
    for i,(_,d) in enumerate(schedule[:-1]):first.setdefault(d,i)
    named=tuple(sorted(first))
    by_projection={};by_output={}
    first_example=None
    all_count=0
    for permuted in permutations(common):
        initial_hole=permuted[0]
        initial_slots=permuted[1:]
        # Independent literal selection: inspect every legal candidate at every round.
        actual=list(initial_slots);literal=[]
        for keys,(_,dst) in zip(windows,schedule):
            available=[k for k in keys if k%B not in actual]
            assert len(available)==1
            key=available[0];literal.append(key)
            actual[dst]=key%B
        # Projection only: initial hole plus values of the effectively addressed slots.
        records={dst:initial_slots[dst] for dst in named}
        hole=initial_hole;trace=[]
        for i,((target,dst),keys) in enumerate(zip(schedule,windows)):
            key=keys[0]+((hole-keys[0])%B)
            assert key<=keys[-1]
            trace.append(key)
            if i+1<len(schedule):hole,records[dst]=records[dst],hole
        assert literal==trace
        output=tuple(trace)
        projection=tuple([initial_hole]+[initial_slots[d] for d in named])
        recovered=tuple([trace[0]%B]+[trace[first[d]+1]%B for d in named])
        assert recovered==projection
        old=by_projection.setdefault(projection,output)
        assert old==output
        old=by_output.setdefault(output,projection)
        assert old==projection
        all_count+=1
        if first_example is None:
            weights=[2*k.bit_count()+4*(1-((k>>(b-1))&1)) for k in trace]
            first_example=dict(initial_slot_residues=initial_slots,initial_hole=initial_hole,
                               projected_state=projection,full_key_trace=trace,
                               weight_sum=sum(weights))
    classes=perm(M,len(named)+1)
    assert len(by_projection)==len(by_output)==classes and all_count==factorial(M)
    return dict(slots=slots,colors=M,modulus=B,schedule=schedule,
                common_legal_residues=common,named_nonterminal_slots=named,
                initial_permutations=all_count,distinct_output_traces=len(by_output),
                projected_classes=classes,configurations_per_class=factorial(slots-len(named)),
                key_events_checked=all_count*len(schedule),example=first_example)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('saturated_results.json'));a=p.parse_args()
    cases=[run(3,((0,0),(0,1),(0,0))),
           run(6,((0,0),(0,1),(0,0),(0,5))),
           run(6,tuple((0,d) for d in (0,1,2,3,4,5,0,2))),
           run(7,((0,0),(1,1),(2,0),(1,2),(0,6)))]
    data=dict(status='PASS',scope='Exact independent literal and projection-only finite control; initial saturated label configuration is supplied as evidence. No BRC execution charged here.',
              cases=cases,total_configuration_schedule_pairs=sum(x['initial_permutations'] for x in cases),
              total_key_events_checked=sum(x['key_events_checked'] for x in cases))
    a.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print([(c['slots'],len(c['named_nonterminal_slots']),c['initial_permutations'],c['projected_classes']) for c in cases])
