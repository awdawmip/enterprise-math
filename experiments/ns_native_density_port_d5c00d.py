#!/usr/bin/env python3
"""Exact density-port test dynamics on the full signed X6 lattice.

This is a constitutive CANDIDATE, not a P000 force law or a Navier--Stokes solver.
The finite dictionary holds deviations from a homogeneous channel background.
All omitted spatial cells retain that background; no periodic/projection boundary
is used. Run next to the exact parent checker, whose helpers are reused unchanged.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations_with_replacement, permutations, product
import json
from pathlib import Path
from typing import Mapping, Sequence
from ns_native_ternary_coherence_d5c00d import (
    D, DIRS, ZERO, C, slot_data, unit, add, act_vec,
)

Counts = tuple[int, ...]
Vec = tuple[int, ...]
Field = dict[Vec, Counts]
NCH = 2*D
EMPTY: Counts = (0,)*NCH

def config_counts(c: Sequence[int]) -> Counts:
    count = Counter(c)
    return tuple(count.get(v, 0) for v in range(NCH))

BACKGROUND: Counts = config_counts(C(0, 1, 1))

def actual(field: Mapping[Vec, Counts], z: Vec, bg: Counts) -> Counts:
    delta = field.get(z, EMPTY)
    return tuple(a+b for a,b in zip(bg, delta))

def validate(field: Mapping[Vec, Counts], bg: Counts) -> None:
    if len(bg)!=NCH or any(type(a) is not int or a<0 for a in bg):
        raise ValueError('Background must have 12 nonnegative integer counts')
    for z, delta in field.items():
        if len(z)!=D or any(type(a) is not int for a in z):
            raise ValueError('Coordinates must be six signed integers')
        if len(delta)!=NCH or any(type(a) is not int for a in delta):
            raise ValueError('Deviations must have 12 integer entries')
        if any(a+b<0 for a,b in zip(bg,delta)):
            raise ValueError('Negative actual occupation')
        if not any(delta):
            raise ValueError('Sparse representation contains a zero entry')

def local_collision(counts: Counts, scores: Sequence[int]) -> tuple[Counts, tuple | None]:
    """Pure synchronous collision. Scores are axis-indexed neighboring totals."""
    if len(counts)!=NCH or any(type(a) is not int or a<0 for a in counts):
        raise ValueError('Invalid actual channel counts')
    if len(scores)!=D or any(type(a) is not int or a<0 for a in scores):
        raise ValueError('Invalid density scores')
    if sum(counts)!=3:
        return counts, None
    config = tuple(v for v, count in enumerate(counts) for _ in range(count))
    data = slot_data(config)
    if data is None:
        return counts, None
    j, sign, old = data
    if j==old:
        return counts, None
    eligible = tuple(i for i in range(D) if i not in (j,old))
    high = max(scores[i] for i in eligible)
    winners = tuple(i for i in eligible if scores[i]==high)
    if len(winners)!=1:
        return counts, None  # Explicit wait-on-tie constitutive choice.
    new = winners[0]
    out = list(counts)
    out[2*old]-=1; out[2*old+1]-=1
    out[2*new]+=1; out[2*new+1]+=1
    return tuple(out), (j,sign,old,new)

def collision(field: Mapping[Vec, Counts], bg: Counts=BACKGROUND) -> tuple[Field, list]:
    validate(field,bg)
    # Every uniform background is fixed by collision: all axis scores tie.
    totals = {z:sum(d) for z,d in field.items() if sum(d)}
    sites = set(field)
    for z in totals:
        for v in DIRS:
            sites.add(add(z,v))
    out = dict(field)
    events=[]
    base_total=2*sum(bg)
    for z in sorted(sites):
        scores=tuple(base_total+totals.get(add(z,unit(i)),0)
                     +totals.get(add(z,unit(i,-1)),0) for i in range(D))
        old=actual(field,z,bg)
        new,event=local_collision(old,scores)
        delta=tuple(a-b for a,b in zip(new,bg))
        if any(delta): out[z]=delta
        else: out.pop(z,None)
        if event is not None:
            events.append((z,event,scores))
    validate(out,bg)
    return out,events

def stream(field: Mapping[Vec, Counts]) -> Field:
    out={}
    for z,delta in field.items():
        for v,value in enumerate(delta):
            if value:
                target=add(z,DIRS[v])
                if target not in out: out[target]=[0]*NCH
                out[target][v]+=value
    return {z:tuple(d) for z,d in out.items() if any(d)}

def step(field: Mapping[Vec, Counts], bg: Counts=BACKGROUND) -> tuple[Field, list]:
    mid,events=collision(field,bg)
    result=stream(mid)
    validate(result,bg)
    return result,events

def norm(field: Mapping[Vec, Counts]) -> int:
    return sum(abs(a) for d in field.values() for a in d)

def invariants(field: Mapping[Vec, Counts]) -> tuple[int, Vec]:
    population=sum(sum(d) for d in field.values())
    moment=tuple(sum((d[2*i+1]-d[2*i]) for d in field.values()) for i in range(D))
    return population,moment

def transformed_counts(p: tuple[int,...], c: Counts) -> Counts:
    out=[0]*NCH
    for i in range(D):
        out[2*p[i]]=c[2*i];out[2*p[i]+1]=c[2*i+1]
    return tuple(out)

def transformed_field(p: tuple[int,...], field: Mapping[Vec, Counts]) -> Field:
    return {act_vec(p,z):transformed_counts(p,c) for z,c in field.items()}

def seed() -> Field:
    plus=[0]*NCH;plus[1]=1
    minus=[0]*NCH;minus[1]=-1
    # Move one +e_0 packet from e_0 to the anchor; relative mass/moment stay zero.
    return {ZERO:tuple(plus),unit(0):tuple(minus)}

def frontier_check(wake: Mapping[Vec, Counts], age: int) -> int:
    if age<1: raise ValueError('Wake age must be positive')
    holes=0
    for m in range(2,D):
        for epsilon in (-1,1):
            for sign in (-1,1):
                z=add(unit(m,epsilon),tuple(sign*age if i==1 else 0 for i in range(D)))
                v=2+(sign==1)
                assert actual(wake,z,BACKGROUND)[v]==0, (age,z,v)
                holes+=1
    for z,d in wake.items():
        assert z[0]==0
        assert abs(z[1])<=age
        assert d[0]==d[1]==0
        if z[1]==age:
            assert all(a==0 for v,a in enumerate(d) if v!=3)
            assert d[3]==-1
        if z[1]==-age:
            assert all(a==0 for v,a in enumerate(d) if v!=2)
            assert d[2]==-1
    assert invariants(wake)==(0,ZERO)
    assert norm(wake)>=32
    return holes

def run_checks(max_age: int=7, full_steps: int=5) -> dict:
    if max_age<1 or full_steps<1 or full_steps>max_age:
        raise ValueError('Require 1 <= full_steps <= max_age')
    # Exhaust the inherited 364 ternary channel states under all binary score
    # patterns (64). Conservation is independently recomputed from counts.
    ncases=0;changed=0
    for config in combinations_with_replacement(range(NCH),3):
        c=config_counts(config)
        p=tuple(c[2*i+1]-c[2*i] for i in range(D))
        for scores in product(range(2),repeat=D):
            q,event=local_collision(c,scores)
            assert sum(q)==3 and min(q)>=0
            assert tuple(q[2*i+1]-q[2*i] for i in range(D))==p
            if event is not None:
                j,s,old,new=event
                assert len({j,old,new})==3
                assert all(a<=1 for a in q)
                changed+=1
            ncases+=1
    initial=seed(); assert invariants(initial)==(0,ZERO) and norm(initial)==2
    first,ev=step(initial)
    assert len(ev)==8 and norm(first)==34
    assert {(z,e[3]) for z,e,_ in ev}=={
        (unit(m,s),m) for m in range(2,D) for s in (-1,1)}
    wake={z:d for z,d in first.items() if z[0]==0}
    wakes=[wake]; ages=[]; hole_checks=0
    for age in range(1,max_age+1):
        if age>1:
            wake,wake_events=step(wake)
            wakes.append(wake)
        else: wake_events=ev
        hole_checks+=frontier_check(wake,age)
        assert max(max(actual(wake,z,BACKGROUND)) for z in wake)<=2
        ages.append({'age':age,'l1':norm(wake),'changed_cells':len(wake),
                     'collisions_creating_this_age':len(wake_events),
                     'certified_distinguished_holes':16})
    # Check exact independent-plane decomposition against generic six-axis run.
    full=initial; full_records=[]
    for t in range(1,full_steps+1):
        full,events=step(full)
        expected={}
        for age in range(1,t+1):
            for z,d in wakes[age-1].items():
                target=(t-age,)+z[1:]
                assert target not in expected
                expected[target]=d
        p=[0]*NCH;p[1]=1
        h=[0]*NCH;h[1]=-1
        expected[(t,0,0,0,0,0)]=tuple(p)
        expected[(t+1,0,0,0,0,0)]=tuple(h)
        assert full==expected
        assert invariants(full)==(0,ZERO)
        assert norm(full)==2+sum(x['l1'] for x in ages[:t])
        assert norm(full)>=32*t+2
        full_records.append({'tick':t,'l1':norm(full),'changed_cells':len(full),
                             'collisions':len(events),'proved_lower_bound':32*t+2})
    # All 720 axis permutations on a full-system, first-step witness.
    symmetry=0
    for p in permutations(range(D)):
        lhs,_=step(transformed_field(p,initial),transformed_counts(p,BACKGROUND))
        rhs=transformed_field(p,first)
        assert lhs==rhs
        symmetry+=1
    shifts=((5,-2,0,3,1,-4),ZERO,(-1,0,7,0,-2,1))
    for shift in shifts:
        lhs,_=step({add(z,shift):d for z,d in initial.items()})
        assert lhs=={add(z,shift):d for z,d in first.items()}
    # The stream-only control is isometric and does not proliferate the defect.
    control=initial
    for _ in range(max_age):
        control=stream(control)
        assert norm(control)==2 and invariants(control)==(0,ZERO)
    # Finite-mass, zero-background sanity check of the identical update law.
    sparse={ZERO:BACKGROUND,unit(2):config_counts((1,))}
    finite_initial=invariants(sparse)
    finite=[]
    for tick in range(1,9):
        sparse,events=step(sparse,EMPTY)
        assert invariants(sparse)==finite_initial
        assert all(0<=a<=2 for c in sparse.values() for a in c)
        finite.append({'tick':tick,'mass':finite_initial[0],'occupied_cells':len(sparse),'collisions':len(events)})
    # An independent finite-population realization, same law, no background
    # reservoir supplied at runtime. Boundary effects are allowed and evolved.
    box={tuple(z):BACKGROUND for z in product(range(-2,3),repeat=D)}
    pert=dict(box)
    pert[ZERO]=actual(initial,ZERO,BACKGROUND)
    pert[unit(0)]=actual(initial,unit(0),BACKGROUND)
    box_mass=3*5**D
    assert invariants(box)==invariants(pert)
    box_next,_=step(box,EMPTY)
    pert_next,_=step(pert,EMPTY)
    finite_difference={}
    for z in set(box_next)|set(pert_next):
        d=tuple(a-b for a,b in zip(pert_next.get(z,EMPTY),box_next.get(z,EMPTY)))
        if any(d): finite_difference[z]=d
    assert norm(finite_difference)==34
    assert invariants(finite_difference)==(0,ZERO)
    assert invariants(box_next)==invariants(box)
    assert invariants(pert_next)==invariants(pert)
    return {'schema':'EM_X6_DENSITY_PORT_RESULTS_V1',
        'event_id':'NS-NATIVE-DENSITY-PORT-20260909-D5C00D-10',
        'status':'CANDIDATE_LAW_ORDINARY_PROOFS_EXACT_CHECKS_NOT_INDEPENDENTLY_REVIEWED',
        'law_id':'X6-DENSITY-PORT-1',
        'ternary_score_cases':ncases,'nontrivial_local_cases':changed,
        'initial_l1':2,'first_tick_l1':34,'first_tick_collision_count':8,
        'wake_ages':ages,'frontier_hole_checks':hole_checks,
        'generic_full_x6_runs':full_records,
        'all_S6_first_step_covariance_checks':symmetry,'translation_checks':len(shifts),
        'stream_only_control_ticks':max_age,'finite_mass_zero_background_checks':finite,
        'proved_for_all_t':'D_t = 2 + sum_{a=1}^t D(w_a) >= 32*t+2',
        'finite_population_family':'For every T, background restricted to [-R,R]^6, R=3*T+3, gives D_T>=32*T+2 by radius-two dependency locality.',
        'pointwise_channel_bound':2,
        'finite_box_check':{'radius':2,'initial_occupied_cells':5**D,'particles_in_each_run':box_mass,'initial_l1_difference':2,'one_tick_l1_difference':34,'same_zero_background_law':True},
        'nonclaims':['not a TRIADIC_CLOSURE_E or physical force-law certificate',
                    'no viscosity or Navier-Stokes bridge','no finite-time blowup',
                    'no fixed-finite-state Lyapunov instability claim',
                    'no independent review or Lean build','no historical novelty claim']}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-age',type=int,default=7)
    parser.add_argument('--full-steps',type=int,default=5)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run_checks(args.max_age,args.full_steps)
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.output: args.output.write_text(text,encoding='utf-8')
    print(text)
