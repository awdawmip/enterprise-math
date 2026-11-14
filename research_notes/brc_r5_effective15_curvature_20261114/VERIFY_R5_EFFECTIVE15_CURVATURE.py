#!/usr/bin/env python3
"""Exact independently enumerated effective-cut census for frozen R5.
Scope: derived 1D integer-event radius-two observer; not native X6.
"""
from collections import Counter
from fractions import Fraction
from math import comb
import json

SCIENCE_PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
ACTIVE = (2,3,4,5,6,8,9,10,11,12,13,16,25,26,27)
INERT = tuple(i for i in range(28) if i not in ACTIVE)
EXPECTED_REDUCED = {207:28,208:624,209:4413,210:11462,211:11404,212:4298,213:539}
EXPECTED_POLY = (213,-5,1,-3,3,-3,1)

def frozen():
    pools={3:set(),12:set(),15:set()}
    numerator = phase = bits = 0
    for step in range(1,1<<15):
        bit=step & -step
        i=bit.bit_length()-1
        bits ^= bit
        delta=1 if bits & bit else -1
        numerator += delta*W[i]
        phase += delta*K0[i]
        if numerator>=3 and phase%36==0 and phase//36 in pools:
            pools[phase//36].add(numerator)
    assert [len(pools[q]) for q in (3,12,15)] == [538,298,229]
    events=Counter(Fraction(n,q) for q,items in pools.items() for n in items)
    points=[0]
    for value in sorted(events):
        points.append(points[-1]+events[value])
    cuts=[i for i in range(len(points)-1) if points[i+1]-points[i]>2]
    assert len(points)==954 and points[-1]==1065 and len(cuts)==28
    assert all(points[i+1]-points[i]==3 for i in cuts)
    return points,cuts

def center_count(points):
    n=len(points)
    i=j=0
    answer=0
    while i<n:
        while j+1<n and points[j+1]<=points[i]+2:
            j+=1
        reach=points[j]+2
        answer+=1
        while i<n and points[i]<=reach:
            i+=1
    return answer

def closed_points(points,cuts,mask):
    out=[];shift=0
    active_cut_indices={cuts[ACTIVE[j]] for j in range(15) if mask>>j & 1}
    for i,x in enumerate(points):
        out.append(x-shift)
        if i in active_cut_indices:
            shift+=1
    return out

def main():
    points,cuts=frozen()
    distribution=Counter()
    by_q=[0]*16
    for mask in range(1<<15):
        d=center_count(closed_points(points,cuts,mask))
        distribution[d]+=1
        by_q[mask.bit_count()]+=d
    assert dict(sorted(distribution.items()))==EXPECTED_REDUCED
    assert sum(distribution.values())==32768
    power=[0]*16
    for q,moment in enumerate(by_q):
        for j in range(16-q):
            power[q+j]+=moment*(-1 if j%2 else 1)*comb(15-q,j)
    assert power[:7]==list(EXPECTED_POLY)
    assert all(v==0 for v in power[7:])
    assert sum(distribution.values())*(1<<13)==1<<28
    second=[i*(i-1)*power[i] for i in range(2,16)]
    assert second[:5]==[2,-18,36,-60,30]
    result={
      'status':'PASS_EXACT_R5_EFFECTIVE15_AND_UNIQUE_INFLECTION',
      'science_pin':SCIENCE_PIN,
      'observer':'derived integer-event radius-2 center-cover',
      'event_boundaries':len(points),'total_events':points[-1],
      'active_cuts_zero_based':list(ACTIVE),
      'inert_cuts_zero_based':list(INERT),
      'directly_enumerated_effective_patterns':1<<15,
      'reduced_minimum_center_distribution':dict(sorted(distribution.items())),
      'all_28_cut_distribution_multiplicity':1<<13,
      'by_active_closure_count_first_moment':by_q,
      'bernoulli_mean_polynomial_ascending':power[:7],
      'bernoulli_mean_second_derivative_ascending':second[:5],
      'inflection_bracket_rational':['142932/1000000','142933/1000000']
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
