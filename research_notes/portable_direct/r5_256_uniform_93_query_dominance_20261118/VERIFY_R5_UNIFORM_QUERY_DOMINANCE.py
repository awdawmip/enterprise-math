#!/usr/bin/env python3
"""Exact all-256 state, all-f fifth-chamber dominance certificate.
python3 VERIFY_R5_UNIFORM_QUERY_DOMINANCE.py EXACT_R5_ALL_101_BUDGETS.json
"""
import sys, json, hashlib
from functools import lru_cache
from pathlib import Path

EXPECTED='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
L=25845652773852463277015040000
U=58182461585441404127941754880
A=tuple(range(214,315))

def maximal(items):
    d=set(items)
    return tuple(sorted(x for x in d if not any(x!=y and x&y==x for y in d)))

def sorted_windows(v,t):
    order=sorted(range(256),key=lambda h:(v[h],h))
    out=[];r=0
    for l in range(256):
        r=max(l,r)
        while r<256 and v[order[r]]-v[order[l]]<=t:r+=1
        out.append(sum(1<<order[i] for i in range(l,r)))
    return maximal(out)

def endpoint_sweep(v,t):
    events={}
    for h,n in enumerate(v):
        events.setdefault(2*n-t,[0,0])[0]|=1<<h
        events.setdefault(2*n+t,[0,0])[1]|=1<<h
    out=[];active=0
    for z in sorted(events):
        starts,ends=events[z]
        active|=starts
        out.append(active)          # closed endpoint: start before end
        active &= ~ends
        out.append(active)          # open interval until next endpoint
    return maximal(out)

def main():
    raw=Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==EXPECTED
    data=json.loads(raw);assert data['budget_range']==[214,314]
    N={k:tuple(int(y) for y in data['counts_and_cohorts'][str(k)]['counts']) for k in A}
    assert all(len(v)==256 for v in N.values())
    cuts={L}
    for k in A:
        values=sorted(set(N[k]))
        for i,n in enumerate(values):
            for m in values[i+1:]:
                g=m-n
                if L<g<U:cuts.add(g)
    cuts=sorted(cuts)
    assert len(cuts)==18
    C={}
    for t in cuts:
        for k in A:
            w=sorted_windows(N[k],t)
            assert w==endpoint_sweep(N[k],t),(k,t)
            C[t,k]=w
    def dominates(j,k):
        return all(all(any((s&v)==s for v in C[t,k]) for s in C[t,j]) for t in cuts)
    core=[k for k in A if not any(dominates(j,k) for j in range(214,k))]
    assert core==[214,215,216,217,223,294,295,296]
    replacement={}
    for k in A:
        if k not in core:
            valid=[j for j in core if j<k and dominates(j,k)]
            assert valid, k
            replacement[k]=valid[0]
    assert len(replacement)==93
    bands=[(218,222,217),(224,290,223),(291,293,214),
           (297,312,296),(313,314,295)]
    for a,z,j in bands:
        assert all(replacement[k]==j for k in range(a,z+1))
    assert len(replacement)==sum(z-a+1 for a,z,j in bands)
    # Every core member resists any one cheaper action at some exact signature.
    witnesses=0
    for k in core:
        for j in range(214,k):
            assert any(any(not any(s&v==s for v in C[t,k]) for s in C[t,j]) for t in cuts)
            witnesses+=1
    result={
        'status':'PASS_R5_FULL256_UNIFORM_93_ACTION_DOMINANCE_ALL_F',
        'input_sha256':EXPECTED,'science_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'noise_diameter_range':{'inclusive_left':str(L),'exclusive_right':str(U)},
        'named_hypotheses':256,'physical_budgets':101,
        'internal_gap_count':len(cuts)-1,
        'critical_representatives':[str(t) for t in cuts],
        'independently_checked_response_families':len(cuts)*len(A),
        'safe_core':core,'discarded_actions':len(replacement),
        'uniform_dominance_bands':[{'from':a,'to':z,'replace_with':j} for a,z,j in bands],
        'core_nondominance_witness_count':witnesses,
        'review':'NOT_REVIEWED'}
    print(json.dumps(result,sort_keys=True,indent=2))
    print(result['status'],file=sys.stderr)

if __name__=='__main__':main()
