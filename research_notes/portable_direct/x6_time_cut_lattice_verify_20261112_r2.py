#!/usr/bin/env python3
"""Exact finite check of the X6 native-time cut-count theorem.

No time metric or globally coupled physical-event permission is inferred.
Each independent component uses the declared V1R internal map, on disjoint
Cell-indexed components.  This verifies the finite product-domain theorem.
"""
from collections import defaultdict
from math import factorial, comb
import json

BASE = ((0,1,2),(1,1,1),"SHELL")

def next_local(s):
    axes, signs, mode = s
    if mode == "SHELL":
        return (axes, signs, "CLOSURE")
    return (axes[1:]+axes[:1], tuple(-x for x in signs), "SHELL")

def powers(n):
    p=[BASE]
    for _ in range(n):p.append(next_local(p[-1]))
    return p

def hist_by_polynomial(lengths):
    v=[1]
    for ell in lengths:
        w=[0]*(len(v)+ell)
        for i,a in enumerate(v):
            for j in range(ell+1):w[i+j]+=a
        v=w
    return v

def enumerate_interleavings(lengths):
    m=len(lengths)
    pending=list(lengths)
    word=[]
    def rec():
        if not any(pending):
            yield tuple(word)
            return
        for i in range(m):
            if pending[i]:
                pending[i]-=1;word.append(i)
                yield from rec()
                word.pop();pending[i]+=1
    yield from rec()

def verify(lengths):
    for ell in lengths: assert 0 <= ell <= 11
    local=[powers(ell) for ell in lengths]
    assert all(len(set(s))==len(s) for s in local)
    bins=[set() for _ in range(sum(lengths)+1)]
    parity_bins=[set() for _ in bins]
    orders=0
    endpoints=set()
    for word in enumerate_interleavings(lengths):
        orders+=1
        a=[0]*len(lengths)
        for k in range(len(word)+1):
            state=tuple(local[i][a[i]] for i in range(len(a)))
            bins[k].add(state)
            parity_bins[k].add(tuple(v%2 for v in a))
            if k<len(word):a[word[k]]+=1
        endpoints.add(state)
    expected=hist_by_polynomial(lengths)
    assert [len(b) for b in bins] == expected
    assert len(endpoints)==1
    expected_orders=factorial(sum(lengths))
    den=1
    for ell in lengths:den*=factorial(ell)
    expected_orders//=den
    assert orders==expected_orders
    return {"lengths":lengths,"serializations":orders,"cut_state_counts":expected,"parity_only_cut_counts":[len(s) for s in parity_bins],"distinct_endpoints":len(endpoints),"peak_labels":max(expected),"peak_bits":(max(expected)-1).bit_length(),"all_cut_states":sum(expected)}

def verify_period_alias():
    lengths=[12,12]
    local=[powers(x) for x in lengths]
    assert local[0][0] == local[0][12]
    k=12
    ideals=[(a,k-a) for a in range(13)]
    seen=defaultdict(list)
    for a,b in ideals:
        seen[(local[0][a],local[1][b])].append((a,b))
    assert len(ideals)==13 and len(seen)==12
    assert any(set(v)=={(0,12),(12,0)} for v in seen.values())
    return {"lengths":lengths,"cut_event_count":k,"distinguished_ideals":13,
            "distinct_V1R_phase_vectors":12,"collapsed_ideal_pair":[[0,12],[12,0]],
            "exact_per_component_event_count_recoverable_from_phase_and_k":False}

if __name__=="__main__":
    findings=[verify([1]*6),verify([2,3,4]),verify([3,3,3])]
    assert findings[0]["cut_state_counts"] == [comb(6,k) for k in range(7)]
    assert findings[1]["cut_state_counts"] == [1,3,6,9,11,11,9,6,3,1]
    print(json.dumps({"status":"PASS","domain":"disjoint V1R product; cut-state injectivity when all lengths <=11; C12 alias checked separately","cases":findings,"period_alias":verify_period_alias(),"native_inter_cell_permission_proven":False,"calibrated_duration_proven":False},ensure_ascii=False,indent=2))
