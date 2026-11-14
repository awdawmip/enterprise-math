#!/usr/bin/env python3
"""Radius-2 frontier support lemma: exact finite tests and frozen R5 instances.

Pure geometric tail-support bound applies to any strictly increasing integer
sample (regardless of cost/optimality); this script checks all admissible
consecutive-center arcs on fixed radius 2 over 3**9 small sequences with coordinate gaps 1..3 and
32 effective R5 masks. The gap<=3 premise justifies the arc-distance cutoff
7 for this checker. It is *not* an independent full recourse proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
BITS=(3,8,9,10,27)

def frozen():
    p={3:set(),12:set(),15:set()};n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t;i=bit.bit_length()-1;mask^=bit
        sgn=1 if mask&bit else -1
        n+=sgn*W[i];k+=sgn*K0[i]
        if n>=3 and k%36==0 and k//36 in p:p[k//36].add(n)
    e=Counter(Fraction(v,q) for q,vals in p.items() for v in vals)
    x=[0]
    for v in sorted(e):x.append(x[-1]+e[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert len(x)==954 and len(cuts)==28
    return x,cuts

def close(x,cuts,selected):
    active={cuts[i] for i in selected}; shift=0;z=[]
    for i,v in enumerate(x):
        z.append(v-shift)
        if i in active:shift+=1
    return z

def arc_tails(z,radius=2):
    n=len(z)
    # Each observed event between consecutive centers must be covered by one.
    # With each adjacent coordinate gap <=3, every radius-2 feasible
    # consecutive-center arc has total coordinate span <=7.
    active=[set() for _ in z]
    for i in range(n-1):
        for q in range(i+1,n):
            d=z[q]-z[i]
            # If there is an event strictly inside the uncovered middle, any
            # further q beyond it remains invalid until such event is covered
            # by the right center again; for frozen gaps<=3, d>7 never valid.
            if d>7:break
            if all(min(z[t]-z[i],z[q]-z[t])<=radius for t in range(i+1,q)):
                for j in range(i,q):active[j].add(i)
    return active

def band(z,j,radius=2):
    # Last event strictly more than radius to the left of event j.
    t=next((k for k in range(j-1,-1,-1) if z[k]<z[j]-radius),None)
    A={i for i in range(j+1) if z[i]>=z[j]-radius}
    if t is not None:
        A.update(i for i in range(t+1) if z[i]>=z[t]-radius)
    return A

def check(z):
    act=arc_tails(z)
    tailmax=0;bandmax=0
    for j,A in enumerate(act):
        B=band(z,j)
        if not A<=B:raise AssertionError(('band',j,z,sorted(A-B)))
        if len(A)>5:raise AssertionError(('five',j,z,sorted(A)))
        tailmax=max(tailmax,len(A));bandmax=max(bandmax,len(B))
    return tailmax,bandmax

def main():
    hist=Counter();counter=0
    for ds in product((1,2,3),repeat=9):
        z=[0]
        for d in ds:z.append(z[-1]+d)
        max_tail,_=check(z)
        hist[max_tail]+=1;counter+=1
    x,cuts=frozen();frozen_rows=[]
    for mask in range(32):
        active=[b for idx,b in enumerate(BITS) if mask>>idx&1]
        z=close(x,cuts,active)
        max_tail,max_band=check(z)
        frozen_rows.append(dict(mask=mask,max_crossing_tail_indices=max_tail,
                                max_two_band_candidates=max_band))
    # Equality witness: full integer event line z=0,...,9, j=4 has 5 tails.
    equal=arc_tails(list(range(10)))[4]
    assert equal==set(range(5)),equal
    assert max(r['max_crossing_tail_indices'] for r in frozen_rows)<=5
    print(json.dumps(dict(status='PASS_R5_FRONTIER_SPATIAL_SUPPORT',
         frozen_scientific_input='435e77af0d180eac32bd1f9c4c464bc4010b7551',
         model='derived indexed-center 1D integer radius-2',
         universal_proof_bound=5,
         exhaustive_small_gap_sequences=counter,
         small_sequence_max_tail_histogram=dict(sorted(hist.items())),
         effective_masks_checked=len(frozen_rows),
         frozen_max_tail_indices=max(r['max_crossing_tail_indices'] for r in frozen_rows),
         frozen_max_two_band_candidates=max(r['max_two_band_candidates'] for r in frozen_rows),
         tightness_witness=dict(events=list(range(10)),cut_index=4,tails=sorted(equal)),
         frozen_per_mask=frozen_rows),indent=2,sort_keys=True))
if __name__=='__main__':main()
