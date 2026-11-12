#!/usr/bin/env python3
"""Exact V29 count-ledger PASS and matched TRANSFER event-cut witness.
This models declared V29 primitive *ledger* updates, not TRIADIC_CLOSURE_E
or a coupled V1R active-triad physical event law.
"""
from itertools import permutations
from math import comb
from collections import defaultdict
import json

class Ledger:
    def __init__(self):
        self.M=defaultdict(int)
        self.Rin=defaultdict(int)
        self.Rout=defaultdict(int)
    def PASS(self,x,a,b):self.M[(x,a,b)]+=1
    def TRANSFER(self,x,a,y,b,allowed_edges):
        assert (x,a,y,b) in allowed_edges
        self.Rout[(x,a)]+=1
        self.Rin[(y,b)]+=1
    def snapshot(self):
        return (tuple(sorted(self.M.items())),tuple(sorted(self.Rin.items())),tuple(sorted(self.Rout.items())))
    def Q(self):
        return sum(self.Rin.values())-sum(self.Rout.values())
    def contrasts(self):
        u=defaultdict(int)
        for (x,a,b),n in self.M.items():u[x,a]+=n;u[x,b]-=n
        for (x,a),n in self.Rin.items():u[x,a]+=n
        for (x,a),n in self.Rout.items():u[x,a]-=n
        assert sum(u.values())==self.Q()
        return tuple(sorted(u.items()))

def check_pass(n=6):
    cuts=[set() for k in range(n+1)]
    finals=set()
    words=0
    for w in permutations(range(n)):
        L=Ledger();cuts[0].add(L.snapshot())
        for k,x in enumerate(w,1):
            L.PASS(x,0,1)
            assert L.Q()==0 and sum(v for (_,_,_),v in L.M.items())==k
            L.contrasts()
            cuts[k].add(L.snapshot())
        words+=1;finals.add(L.snapshot())
    assert words==720 and len(finals)==1
    assert [len(s) for s in cuts]==[comb(n,k) for k in range(n+1)]
    return {'cells':n,'event_kind':'PASS','serializations':words,'cut_state_counts':[len(s) for s in cuts],
            'distinct_endpoints':len(finals),'network_scalar_Q':0,'peak_cut_bits':(max(map(len,cuts))-1).bit_length()}

def check_transfer():
    edges={(0,0,1,1),(2,0,3,1)}
    cuts=[set() for k in range(3)];finals=set()
    for order in [(0,1),(1,0)]:
        L=Ledger();cuts[0].add(L.snapshot())
        for k,i in enumerate(order,1):
            e=sorted(edges)[i]
            L.TRANSFER(*e,allowed_edges=edges)
            assert L.Q()==0
            L.contrasts()
            cuts[k].add(L.snapshot())
        finals.add(L.snapshot())
    assert [len(s) for s in cuts]==[1,2,1] and len(finals)==1
    return {'cells':4,'allowed_connections':sorted(list(edges)),'event_kind':'TRANSFER',
            'serializations':2,'cut_state_counts':[1,2,1], 'distinct_endpoints':1,'network_scalar_Q':0}

if __name__=='__main__':
    print(json.dumps({'status':'PASS','count_ledger_law_source':'X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906',
                      'pass_witness':check_pass(),'transfer_witness':check_transfer(),
                      'proven':'EXACT_V29_LEDGER_LEVEL_AND_COUNT_ONLY_FUTURE',
                      'not_proven':['TRIADIC_CLOSURE_E','V1R_INTERNAL_FRAME_COUPLING','PHYSICAL_TIME_DURATION']},indent=2))
