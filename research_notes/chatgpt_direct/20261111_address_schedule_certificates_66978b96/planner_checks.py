"""Exact evidence for scheduled optimizers; outputs control counts and witnesses.

Ordered Bellman, slot-orbit Bellman, and latest-known-blocker Bellman use
different internal states.  The physical BRC runs are supplied in separate files.
"""
from __future__ import annotations
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path
from time import perf_counter
import argparse
import gc
import json

from schedule_planner import (LabelledSchedulePlanner, SchedulePlanner, LifetimePlanner,
                             key_weight, set_observation, replace_known, schedule_replay,
                             worst_static_witness, lifetime_capacity)


def small_case(r, schedule):
    t0=perf_counter()
    ref=LabelledSchedulePlanner(r,schedule)
    orbit=SchedulePlanner(r,schedule)
    life=LifetimePlanner(r,schedule)
    blank=((0,0),)*r
    cost=ref.value(blank,0)
    assert orbit.value(blank,0)==cost==life.value(blank,0)
    cold={n:p.metrics() for n,p in [('ordered',ref),('orbit',orbit),('lifetime',life)]}
    for (state,i),_ in tuple(ref.decisions.items()):
        assert ref.value(state,i)==orbit.value(state,i)==life.value(state,i)
    all_preps=0
    histograms={k:Counter() for k in ('orbit','lifetime')}
    for residues in product(range(ref.modulus),repeat=r):
        for key,p in [('orbit',orbit),('lifetime',life)]:
            ev=schedule_replay(p,residues)
            assert ev['cost']<=cost
            histograms[key][ev['cost']]+=1
        all_preps+=1
    for hist in histograms.values():assert max(hist)==cost
    return dict(slots=r,schedule=schedule,variable_value=cost,
                ordered_nonterminal_values_compared=len(ref.decisions),
                all_static_preparations_replayed_by_each=all_preps,
                cost_histograms={k:dict(sorted(h.items())) for k,h in histograms.items()},
                cold_metrics=cold,worst_static_lifetime=worst_static_witness(life),
                elapsed_seconds=perf_counter()-t0)


def image_check(r,schedule):
    """Check every abstract query/answer and safe write image against projection."""
    p=LifetimePlanner(r,schedule)
    o=SchedulePlanner(r,schedule)
    masks=tuple(p.domains)
    states=tuple(product(masks,repeat=r))
    rows=[]
    for i,(t,dest) in enumerate(schedule):
        images=set();orbits=set();qs=ks=0
        for state in states:
            u,l=p._represent(state,i)
            images.add((u,l));orbits.add(o._canonical(state,i))
            for slot,(m,v) in enumerate(state):
                if m==p.full:continue
                index=u.index((p.lifetimes[i][slot],m,v))
                for bit in range(p.width):
                    if m>>bit & 1:continue
                    for a in (0,1):
                        qs+=1
                        assert p._refine(u,l,index,bit,a)==p._represent(
                                set_observation(state,slot,bit,a),i)
            for k in p.keys[i]:
                z=k%p.modulus
                concrete=all(z&m!=v for m,v in state)
                abstract=l[z]<i and all(z&m!=v for e,m,v in u)
                assert concrete==abstract
                if not concrete:continue
                ks+=1
                if i+1<len(schedule):
                    assert p._write(u,l,i,z)==p._represent(
                            replace_known(state,dest,z,p.width),i+1)
        d=len(o.named[i]);a=r-d
        lc=lifetime_capacity(p.width,d,a)
        oc=3**(p.width*d)*comb(3**p.width+a-1,a)
        assert len(images)==lc and len(orbits)==oc
        rows.append(dict(position=i,named_count=d,ordered_patterns=len(states),
                         orbit_capacity=oc,lifetime_capacity=lc,physical_answer_edges=qs,
                         certified_creation_edges=ks))
    return rows


def full_prepared(r,schedule,residues):
    mask=(1<<r.bit_length())-1
    known=tuple((mask,z) for z in residues)
    planners=[cls(r,schedule) for cls in (LabelledSchedulePlanner,SchedulePlanner,LifetimePlanner)]
    value=planners[0].value(known,0)
    assert all(p.value(known,0)==value for p in planners)
    replay=schedule_replay(planners[-1],residues,known)
    assert replay['cost']==value and replay['vacancy_bit_reads']==0
    return dict(initial_residues=residues,variable_value=value,
                witness_keys=tuple(e['key'] for e in replay['events']),
                weights=tuple(e['key_weight'] for e in replay['events']),
                lifetime_certificate=planners[-1].certificate(known,0),
                slot_orbit=planners[1]._canonical(known,0))


def counterexamples():
    sched=((0,0),(0,1),(0,0))
    rows=[full_prepared(3,sched,rs) for rs in ((0,1,2),(0,2,1))]
    assert [r['variable_value'] for r in rows]==[16,12]
    assert rows[0]['witness_keys']==(3,4,1) and rows[1]['witness_keys']==(3,4,2)
    s2=((0,0),(0,1))
    shadow=[full_prepared(3,s2,rs) for rs in ((1,1,2),(2,1,2))]
    assert [r['variable_value'] for r in shadow]==[10,10]
    assert shadow[0]['lifetime_certificate']==shadow[1]['lifetime_certificate']
    assert shadow[0]['slot_orbit']!=shadow[1]['slot_orbit']
    latest=[full_prepared(2,s2,rs) for rs in ((1,2),(2,1))]
    assert [r['variable_value'] for r in latest]==[10,6]
    return dict(next_destination_only=dict(schedule=sched,rows=rows,
                minimality='With at most 2 slots fixing the next bind destination leaves no two other addresses to permute. At most 2 rounds have at most one effective bind destination.'),
                strict_known_shadow=dict(schedule=s2,rows=shadow),
                current_support_only=dict(schedule=s2,rows=latest))


def large_case():
    r=4;schedule=((0,0),(1,1),(0,3));blank=((0,0),)*r
    # Single sequential allocation at a time: no need to retain two large caches.
    results={}
    for cls in (SchedulePlanner,LifetimePlanner):
        ts=perf_counter()
        p=cls(r,schedule);val=p.value(blank,0);tm=perf_counter()-ts
        metrics=p.metrics().copy();wit=worst_static_witness(p)
        hist=Counter()
        for initial in product(range(p.modulus),repeat=r):
            replay=schedule_replay(p,initial)
            assert replay['cost']<=val
            hist[replay['cost']]+=1
        assert max(hist)==val==wit['cost']
        results[cls.__name__]=dict(value=val,planning_seconds=tm,cold_metrics=metrics,
                                   static_preparations=sum(hist.values()),
                                   cost_histogram=dict(sorted(hist.items())),worst_static=wit)
        del p;gc.collect()
    assert results['SchedulePlanner']['value']==results['LifetimePlanner']['value']==72
    return dict(slots=r,schedule=schedule,implementations=results)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('planner_results.json'))
    args=parser.parse_args()
    started=perf_counter()
    schedules=[(2,((0,0),(1,1),(0,0))), (3,((0,0),(0,1),(0,0))),
               (3,((0,0),(1,1),(2,2),(0,0))), (3,((0,0),(1,0),(2,0),(0,1))),
               (3,((0,0),(1,1),(2,0),(0,2)))]
    checks=[small_case(r,seq) for r,seq in schedules]
    images=[dict(slots=r,schedule=seq,positions=image_check(r,seq))
            for r,seq in [schedules[0],schedules[2],schedules[-1]]]
    cex=counterexamples()
    larger=large_case()
    L=LifetimePlanner(2,())
    assert L.value(((0,0),(0,0)),0)==0
    result=dict(status='PASS',unit='One fresh residue-bit query costs 8; weights use complete positive keys; fixed BRC words are separate.',
                scope='Exact control decision games and static replays. No original BRC run is counted by this script.',
                small_cases=checks,all_preparations_per_policy_small=sum(c['all_static_preparations_replayed_by_each'] for c in checks),
                ordered_nonterminal_states_compared_small=sum(c['ordered_nonterminal_values_compared'] for c in checks),
                full_image_transition_checks=images,counterexamples=cex,
                larger_four_slot_case=larger,
                last_round_b3_r6_capacity=dict(ordered=27**6,orbit=comb(32,6),
                                                lifetime=lifetime_capacity(3,0,6)),
                elapsed_seconds=perf_counter()-started)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',small_values=[x['variable_value'] for x in checks],
                          small_nonterminal=result['ordered_nonterminal_states_compared_small'],
                          small_preps=result['all_preparations_per_policy_small'],
                          larger_values={name:x['value'] for name,x in larger['implementations'].items()},
                          larger_states={name:x['cold_metrics']['nonterminal_states'] for name,x in larger['implementations'].items()},
                          elapsed_seconds=result['elapsed_seconds']),ensure_ascii=False))


if __name__=='__main__':main()
