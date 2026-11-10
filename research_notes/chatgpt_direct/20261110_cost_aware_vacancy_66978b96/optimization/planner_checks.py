"""Exact finite control replays of the masked-observation Bellman planner.

These are control-model executions. The fixed business words, complete matching
and physical output register are executed by the separate original-BRC harness.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import itertools
import json
from pathlib import Path
import time

from bellman_planner import Planner, control_replay, key_cost


def verify_events(planner, initial, knowledge, replay):
    """Check the returned path against its actual table and stated observations."""
    actual=list(initial)
    patterns=list(knowledge)
    position=cost=queries=0
    full=planner.modulus-1
    for event in replay['events']:
        assert event['round']==position
        unknown_before=sum(planner.width-mask.bit_count() for mask,_ in patterns)
        rank_before=(planner.slots*planner.width+1)*(len(planner.targets)-position)+unknown_before
        if event['kind']=='read':
            slot,bit=event['slot'],event['bit']
            mask,value=patterns[slot]
            assert 0<=slot<planner.slots and 0<=bit<planner.width
            assert not mask&(1<<bit), 'Every scheduled query observes a new bit'
            answer=(actual[slot]>>bit)&1
            assert answer==event['answer']
            patterns[slot]=(mask|(1<<bit),value|(answer<<bit))
            queries+=1;cost+=8
        else:
            assert event['kind']=='create'
            key=event['key'];target=planner.targets[position]
            assert event['target']==target
            assert 1+target*planner.colors<=key<1+(target+1)*planner.colors
            residue=key%planner.modulus
            assert residue not in actual
            for mask,value in patterns:
                compatible_values={x for x in range(planner.modulus) if x&mask==value}
                assert residue not in compatible_values, 'Chosen key is certified for every compatible input'
            expected_weight=2*key.bit_count()+4*(1-((key>>(planner.width-1))&1))
            assert event['key_weight']==expected_weight
            cost+=expected_weight
            actual[0]=residue
            patterns[0]=(full,residue)
            position+=1
        unknown_after=sum(planner.width-mask.bit_count() for mask,_ in patterns)
        rank_after=(planner.slots*planner.width+1)*(len(planner.targets)-position)+unknown_after
        assert rank_after<rank_before
    assert position==len(planner.targets)
    assert cost==replay['cost'] and queries==replay['vacancy_bit_reads']
    assert queries<=planner.slots*planner.width
    assert tuple(patterns)==replay['final_knowledge']
    assert actual==replay['final_residues']


def check_case(slots,targets,*,initial_knowledge=None):
    started=time.perf_counter()
    planner=Planner(slots,targets)
    knowledge=initial_knowledge or ((0,0),)*slots
    value=planner.value(knowledge,0)
    planning_seconds=time.perf_counter()-started
    after_solve=planner.metrics()
    per_slot=[tuple(x for x in range(planner.modulus) if x&mask==known)
              for mask,known in knowledge]
    hist=Counter();read_hist=Counter();table_count=worst_count=0
    worst=None
    replay_started=time.perf_counter()
    selected_schedules=set()
    for initial in itertools.product(*per_slot):
        replay=control_replay(planner,initial,knowledge)
        verify_events(planner,initial,knowledge,replay)
        table_count+=1
        assert replay['cost']<=value
        hist[replay['cost']]+=1
        read_hist[replay['vacancy_bit_reads']]+=1
        selected_schedules.add(tuple(event['key'] for event in replay['events'] if event['kind']=='create'))
        if replay['cost']==value:
            worst_count+=1
            if worst is None:
                worst=dict(initial_residues=initial,**replay)
    assert table_count==planner.modulus**slots if initial_knowledge is None else table_count==4
    assert max(hist)==value and worst is not None
    elapsed_replay=time.perf_counter()-replay_started
    after_replay=planner.metrics()
    assert after_solve['states']==after_replay['states'], 'Replays use the solved policy state set'
    return dict(slots=slots,colors=planner.colors,width=planner.width,
                target_sequence=targets,initial_knowledge=knowledge,
                actual_initial_residue_domains=per_slot,
                initial_tables_exhausted=table_count,
                minimax_variable_commands=value,actual_maximum=max(hist),
                cost_histogram=dict(sorted(hist.items())),
                read_histogram=dict(sorted(read_hist.items())),
                worst_input_count=worst_count,worst_witness=worst,
                selected_key_schedules=sorted(selected_schedules),
                planner_metrics=after_solve,replay_final_metrics=after_replay,
                elapsed_seconds=dict(planning=planning_seconds,replays=elapsed_replay,
                                     total=time.perf_counter()-started))


def run():
    started=time.perf_counter()
    cases=[check_case(slots,targets) for slots,targets in (
        (2,(0,)),(2,(0,1)),(2,(0,0,0,0)),(3,(0,1,2,0)))]
    seed=check_case(2,(0,1),initial_knowledge=((2,0),(2,0)))
    assert seed['minimax_variable_commands']==8
    assert seed['selected_key_schedules']==[(3,6)]
    assert seed['read_histogram']=={0:4}
    assert key_cost(3,2)==4 and key_cost(6,2)==4
    assert key_cost(2,2)==2, 'Full key 6 and its low residue 2 have different actual write weights'
    return dict(status='PASS',model='FINITE_MASKED_OBSERVATION_CONTROL_ONLY',
                generated_at_utc=datetime.now(timezone.utc).isoformat(),
                checked_implementation='bellman_planner.py',
                value_units='Eight commands per added bit read plus full-key-dependent creation/binding weight; fixed business words are separate',
                scope='All initial residue tables in each of four stated sequence domains, plus all four completions of the observed-high-bit seed',
                total_initial_tables=sum(x['initial_tables_exhausted'] for x in cases)+seed['initial_tables_exhausted'],
                cases=cases,observed_high_bit_seed=seed,
                elapsed_seconds=time.perf_counter()-started)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('planner_results.json'))
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],model=result['model'],
                         total_initial_tables=result['total_initial_tables'],
                         values=[x['minimax_variable_commands'] for x in result['cases']],
                         seed_value=result['observed_high_bit_seed']['minimax_variable_commands'],
                         elapsed_seconds=result['elapsed_seconds'])))
