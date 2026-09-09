#!/usr/bin/env python3
"""Actual autonomous native microstep executor for the capacity router.

Frozen incidence/anchor are configuration, ordered frame/phase/labelled positions
are state. Each call reads only that current state. This is routing, NOT force
admissibility, viscosity, mechanical momentum conservation, or Navier--Stokes.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import permutations
from collections import Counter
from pathlib import Path
import argparse
import json
import ns_native_event_capacity_d5c00d as core

@dataclass(frozen=True)
class State:
    frame: tuple[int, int, int, int]
    phase: int
    positions: tuple[tuple[int, ...], ...]  # indexed by immutable token identity

class Router:
    def __init__(self, anchor=core.ZERO, template=core.STARS):
        if len(anchor)!=6 or any(type(x) is not int for x in anchor):
            raise ValueError('anchor must be six integers')
        self.anchor=tuple(anchor)
        self.template=tuple(tuple(e) for e in template)
        self.maps={}
        cells=tuple(core.add(self.anchor,core.unit(i)) for i in range(6))
        for h in permutations(range(4)):
            axes=core.frame_axes(h,self.template)
            first={z:z for z in cells};second={}
            for k,i in enumerate(axes):
                j=axes[(k+1)%3]
                middle=core.add(cells[i],core.unit(j))
                first[cells[i]]=middle
                second[middle]=cells[j]
            for i in set(range(6))-set(axes):
                second[cells[i]]=cells[i]
            if len(set(first.values()))!=6 or set(first.values())!=set(second):
                raise ValueError('colliding or incomplete routing template')
            self.maps[(h,0)]=first;self.maps[(h,1)]=second

    def initial(self, tokens=tuple(range(6)), frame=(0,1,2,3)):
        if sorted(tokens)!=list(range(6)) or sorted(frame)!=list(range(4)):
            raise ValueError('token/frame permutations required')
        positions=[None]*6
        for i,token in enumerate(tokens):
            positions[token]=core.add(self.anchor,core.unit(i))
        return State(tuple(frame),0,tuple(positions))

    def step(self,state):
        if state.phase not in (0,1) or (state.frame,state.phase) not in self.maps:
            raise ValueError('illegal frame or phase')
        mapping=self.maps[(state.frame,state.phase)]
        if len(state.positions)!=6 or len(set(state.positions))!=6 or set(state.positions)!=set(mapping):
            raise ValueError('positions outside the declared router state family')
        positions=tuple(mapping[z] for z in state.positions)
        h=state.frame if state.phase==0 else state.frame[1:]+state.frame[:1]
        return State(h,1-state.phase,positions)

def l1_counts(left,right):
    a=Counter(left);b=Counter(right)
    return sum(abs(a[z]-b[z]) for z in set(a)|set(b))

def run():
    router=Router();tests=0;edges=0
    for h in permutations(range(4)):
        for tokens in permutations(range(6)):
            s=router.initial(tokens,h);mid=router.step(s);end=router.step(mid)
            expected,frame=core.macro_step(tokens,h)
            assert end==router.initial(expected,frame)
            assert l1_counts(s.positions,end.positions)==0
            for x,y in ((s,mid),(mid,end)):
                for a,b in zip(x.positions,y.positions):
                    assert sum(abs(v) for v in core.sub(b,a)) in (0,1)
                    edges+=1
            tests+=2
    for h in permutations(range(4)):
        initial=router.initial(frame=h);s=initial
        for t in range(1,41):
            s=router.step(s)
            assert s!=initial or t==40
        assert s==initial
    a=router.initial(frame=(0,1,2,3));b=router.initial(frame=(1,0,2,3))
    assert a.positions==b.positions
    counter=l1_counts(router.step(a).positions,router.step(b).positions)
    assert counter==10
    # Guards alone do not guarantee commuting disjoint writes.
    # U(a,b)=(b,b), V(a,b)=(a,1-b): both guards True, writes disjoint.
    U=lambda s:(s[1],s[1]);V=lambda s:(s[0],1-s[1])
    assert U(V((0,0)))!=V(U((0,0)))
    return {'schema':'EM_NATIVE_ROUTER_MICROSTEP_RESULTS_V1',
       'event_id':core.EVENT,'current_state_only_executor':True,
       'valid_microstates_exhausted':tests,'individual_edge_checks':edges,
       'frames_with_exact_40_tick_period':24,
       'same_boundary_count_next_microstep_count_distance':counter,
       'guard_only_commutation_counterexample':{'input':[0,0],'UV':[1,1],'VU':[0,1]},
       'scope':'Packet routing test interface, not force dynamics; no independent review.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=Path('microstep_results_13.json'))
    a=p.parse_args();text=json.dumps(run(),indent=2)+'\n';a.output.write_text(text);print(text)
