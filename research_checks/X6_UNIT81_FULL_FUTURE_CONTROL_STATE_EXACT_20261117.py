#!/usr/bin/env python3
"""Exact Unit81: all-root future suffix and control-state counts for P000 signed X6 C12."""
from itertools import combinations, product
from collections import defaultdict, Counter
from math import ceil, log2
import json

N=6
ZERO=(0,)*N

def e(i,s=1): return tuple(s if j==i else 0 for j in range(N))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def phases(i,j,k,eps):
    if eps==1: return (e(i),e(j,-1),e(k),e(i,-1),e(j),e(k,-1))
    return (e(i),e(k,-1),e(j),e(i,-1),e(k),e(j,-1))
def build(frame,eps,bits):
    pp=phases(*frame,eps)
    states=[]
    for r in range(6):
        a,b=pp[r],pp[(r+1)%6]
        mid=add(a,b) if bits[r] else ZERO
        if sum(abs(x-y) for x,y in zip(a,mid)) != 1 or sum(abs(x-y) for x,y in zip(b,mid))!=1:raise ValueError('invalid BRC primitive pair')
        states.extend((a,mid))
    return tuple(states)

def run():
    by_root=defaultdict(list)
    for frame in combinations(range(N),3):
        for eps in (-1,1):
            for bits in product((0,1),repeat=6):
                s=build(frame,eps,bits)
                if s[3] !=ZERO:
                    if bits[1]!=1:raise ValueError('invalid root branch')
                    by_root[s[3]].append((frame,eps,bits,s))
    if len(by_root)!=20 or sum(map(len,by_root.values()))!=1280:raise ValueError('population')
    root_counts=[]
    histogram=Counter()
    total_distinct_suffix=0
    total_distinct_histories=0
    total_future_control=0
    sum_m_log=0.0
    for root,records in sorted(by_root.items()):
        fs={f for f,eps,b,s in records};m=len(fs)
        suffix=defaultdict(list)
        full=defaultdict(list)
        for frame,eps,bits,states in records:
            suffix[states[4:12]].append((frame,eps,bits))
            full[states].append((frame,eps,bits))
        if len(suffix)!=16*m or len(full)!=32*m:raise ValueError(('census',root,m,len(suffix),len(full)))
        if {len(v) for v in suffix.values()}!={2} or {len(v) for v in full.values()}!={1}:
            raise ValueError(('fibers',root))
        for witness in suffix.values():
            (f1,ep1,b1),(f2,ep2,b2)=witness
            if (f1,ep1,b1[1:])!=(f2,ep2,b2[1:]) or b1[0]==b2[0]:
                raise ValueError(('wrong forgotten history bit',root))
        for bits in product((0,1),repeat=4):
            outputs={build(f,eps0,(0,1)+bits)[4:12] for f,eps0,b0,s in records}
            if len(outputs)!=m:raise ValueError(('state+controls not injective',root,bits))
            total_future_control+=1
        total_distinct_suffix+=len(suffix)
        total_distinct_histories+=len(full)
        histogram[m]+=1
        sum_m_log+=len(records)*log2(m)
        root_counts.append({'root':list(root),'source_frames_m':m,'root_histories':len(records),'future_suffixes':len(suffix),'root_to_future_bits':4+ceil(log2(m)),'root_to_full_history_bits':5+ceil(log2(m)),'known_future_control_prior_state_bits':ceil(log2(m))})
    return {'schema':'EM_X6_UNIT81_FULL_FUTURE_OPERATION_INPUT_EXACT_V1','scientific_pin':'59538f585d037d09ef687b28715c4bc1a3f9fe03','case_count':1280,'distinct_signed_roots':len(by_root),'frame_fiber_histogram':dict(sorted(histogram.items())),'total_root_conditional_distinct_future_suffixes':total_distinct_suffix,'total_root_conditional_full_histories':total_distinct_histories,'fixed_future_control_crosschecks':total_future_control,'max_root_future_suffix_size':64,'max_root_history_size':128,'max_root_conditional_future_bits':6,'max_root_conditional_full_history_bits':7,'max_prior_state_bits_with_named_future_controls':2,'uniform_labeled_history_conditional_future_entropy_bits':4+sum_m_log/1280,'root_classes':root_counts,'failed_checks':0,'caveat':'All-branch suffix coding is retrospective/precommitted. With future INNER/OUTER operations supplied at each step, only prior source frame i is additional state at nonzero root; the branch inputs are not pre-existing state.'}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
