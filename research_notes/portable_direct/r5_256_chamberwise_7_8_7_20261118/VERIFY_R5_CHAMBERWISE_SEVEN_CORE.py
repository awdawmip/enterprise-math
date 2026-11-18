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

P=42621568083499305947627520000
Q=45392032647559604256815185920
CORE1=(214,215,216,223,294,295,296)
CORE2=(214,215,216,217,223,294,295,296)
CORE3=(214,215,216,217,223,295,296)
def phase_main():
    raw=Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==EXPECTED
    data=json.loads(raw)
    assert data["budget_range"]==[214,314]
    N={k:tuple(map(int,data["counts_and_cohorts"][str(k)]["counts"])) for k in A}
    assert all(len(N[k])==256 for k in A)
    cuts={L}
    for k in A:
        vals=sorted(set(N[k]))
        for i,v in enumerate(vals):
            for w in vals[i+1:]:
                if L<w-v<U:cuts.add(w-v)
    cuts=sorted(cuts)
    assert len(cuts)==18 and P in cuts and Q in cuts
    out=[]
    for tau in cuts:
        C={}
        for k in A:
            C[k]=sorted_windows(N[k],tau)
            assert C[k]==endpoint_sweep(N[k],tau),(tau,k)
        def dom(j,k):
            return all(any((s&t)==s for t in C[k]) for s in C[j])
        core=tuple(k for k in A if not any(dom(j,k) for j in range(214,k)))
        expected=CORE1 if tau<P else CORE2 if tau<Q else CORE3
        assert core==expected,(tau,core)
        repl={}
        for k in A:
            if k not in core:
                choices=[j for j in core if j<k and dom(j,k)]
                assert choices,(tau,k)
                repl[str(k)]=choices[0]
        counter={}
        for k in core:
            for j in range(214,k):
                s=next((s for s in C[j] if not any(s&t==s for t in C[k])),None)
                assert s is not None,(tau,j,k)
                counter[f"{j}->{k}"]=hex(s)
        out.append({"tau_from_inclusive":str(tau),"core":core,
                    "replacement_map":repl,"witness_count":len(counter),
                    "witness_digest":hashlib.sha256(json.dumps(counter,sort_keys=True).encode()).hexdigest()})
    assert max(N[294])-min(N[294])==Q
    assert sorted_windows(N[294],Q)==((1<<256)-1,)
    w216=sorted_windows(N[216],P); w217=sorted_windows(N[217],P)
    bad=next(s for s in w216 if not any(s&t==s for t in w217))
    hs=[h for h in range(256) if bad>>h&1]
    assert hs==[2+16*i for i in range(8)]+[128+16*i for i in range(8)]
    result={"status":"PASS_R5_256_CHAMBERWISE_7_8_7_ACTION_CORES_ALL_F",
            "science_commit":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
            "input_sha256":EXPECTED,"L":str(L),"U_exclusive":str(U),
            "first_217_needed":str(P),"first_294_uninformative":str(Q),
            "cores":{"initial":CORE1,"middle":CORE2,"final":CORE3},
            "center_range_294":str(Q),"witness_states_216_not_refining_217_at_P":hs,
            "support_family_checks":len(cuts)*len(A),
            "per_chamber_detailed_certificates":out,"review":"NOT_REVIEWED"}
    print(json.dumps(result,sort_keys=True,indent=2))
    print(result["status"],file=sys.stderr)
if __name__=="__main__":phase_main()
