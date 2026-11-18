#!/usr/bin/env python3
"""Check R5 global scalar identifiability threshold; no floating-point arithmetic.
Usage: python3 VERIFY_R5_IDENTIFIABILITY_THRESHOLD.py EXACT_R5_ALL_101_BUDGETS.json
"""
import hashlib, itertools, json, pathlib, sys

SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
D = 1882951873548292168718745600000
T = 1876919155234970890319953920000
CRITICAL = [(11+16*i,14+16*i) for i in range(8)]
OPT = (217,218,224,298)

def main(fname):
    raw = pathlib.Path(fname).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA, "frozen input changed"
    data = json.loads(raw)
    assert data["mask_count"] == 256
    budgets = list(range(214,315))
    N = {k: tuple(map(int,data["counts_and_cohorts"][str(k)]["counts"])) for k in budgets}
    assert all(len(N[k]) == 256 for k in budgets)
    pairs = [(a,b) for a in range(256) for b in range(a+1,256)]
    assert len(pairs)==32640
    full=(1<<len(pairs))-1
    sep={}
    previous=0
    for k in budgets:
        bits=0
        for i,(a,b) in enumerate(pairs):
            gap=abs(N[k][a]-N[k][b])
            if gap>=D:
                bits |= 1<<i
            elif gap>previous:
                previous=gap
        sep[k]=bits
    assert previous==T
    critical=[]
    for a,b in pairs:
        maximum=max(abs(N[k][a]-N[k][b]) for k in budgets)
        assert maximum>=D, (a,b,maximum)
        if maximum==D:
            critical.append((a,b))
    assert critical==CRITICAL,critical
    assert all([k for k in budgets if abs(N[k][a]-N[k][b])>=D]==[217] for a,b in critical)
    others=[k for k in budgets if k!=217]
    assert all(sep[217]|sep[a]|sep[b] != full for a,b in itertools.combinations(others,2))
    covers=[]
    for a,b,c in itertools.combinations(others,3):
        if (sep[217]|sep[a]|sep[b]|sep[c])==full:
            covers.append((217,a,b,c))
    assert len(covers)==1876
    cheapest=min(sum(x) for x in covers)
    winners=[x for x in covers if sum(x)==cheapest]
    assert (cheapest,winners)==(957,[OPT])
    assert 5*min(budgets)>cheapest
    result={
        "science_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
        "frozen_counts_sha256":SHA,"pair_count":len(pairs),"budget_count":len(budgets),
        "critical_D":str(D),"previous_gap_T":str(T),"critical_pairs":critical,
        "critical_only_budget":217,"triples_containing_217_covering_all_pairs":0,
        "four_budget_covers":len(covers),"unique_min_cost_batch":list(OPT),
        "unique_min_cost":cheapest,"valid_noise_chamber":"T<=tau<D",
        "finite_identification_iff":"tau<D for all f>=0",
        "review":"NOT_REVIEWED",
    }
    print(json.dumps(result,indent=2,sort_keys=True))
    print("PASS_R5_SHARP_IDENTIFIABILITY_THRESHOLD_AND_NEAR_CHAMBER",file=sys.stderr)

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Supply EXACT_R5_ALL_101_BUDGETS.json")
    main(sys.argv[1])
