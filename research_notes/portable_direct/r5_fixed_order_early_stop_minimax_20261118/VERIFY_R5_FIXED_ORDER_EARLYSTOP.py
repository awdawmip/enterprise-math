#!/usr/bin/env python3
"""Exact R5 scalar-input corroboration of the fixed-order early-stop theorem.
The general theorem is proved in RESEARCH.md; this checks the pinned corollaries.
Run: python3 VERIFY_R5_FIXED_ORDER_EARLYSTOP.py EXACT_R5_ALL_101_BUDGETS.json
"""
import hashlib
import json
import sys

SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L = 25845652773852463277015040000
U = 58182461585441404127941754880
T = 1876919155234970890319953920000
D = 1882951873548292168718745600000

def read(path):
    raw = open(path, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA
    src = json.loads(raw)
    assert src["mask_count"] == 256 and src["budget_range"] == [214, 314]
    return {int(k): [int(n) for n in src["counts_and_cohorts"][k]["counts"]]
            for k in map(str, range(214, 315))}

def test(centers, lower, upper, actions, witnesses):
    pairs = [(a, b) for a in range(256) for b in range(a+1, 256)]
    assert len(pairs) == 32640
    index = {pair: i for i, pair in enumerate(pairs)}
    sep = {}
    sep_lower = {}
    for k in actions:
        sep[k] = bytes(int(abs(centers[k][a]-centers[k][b]) > upper-1)
                       for a,b in pairs)
        sep_lower[k] = bytes(int(abs(centers[k][a]-centers[k][b]) > lower)
                             for a,b in pairs)
    # The cited alphabet must separate every pair at the hardest integer edge.
    assert all(any(sep[k][i] for k in actions) for i in range(32640))
    observations = []
    for a,b,k in witnesses:
        i=index[(a,b)]
        assert sep[k][i] == sep_lower[k][i] == 1
        assert sum(sep[j][i] for j in actions) == 1
        assert sum(sep_lower[j][i] for j in actions) == 1
        observations.append({"pair":[a,b],"only_selected_separator":k})
    runs=[]
    for f in (0,1,8):
        q=2*f+1
        schedule=actions*q
        d=[0]*32640
        penultimate=None
        first_complete=None
        for t,k in enumerate(schedule,1):
            d=[p+x for p,x in zip(d,sep[k])]
            ambiguous=next((i for i,v in enumerate(d) if v<q),None)
            if t == len(schedule)-1:
                assert ambiguous is not None
                penultimate={"pair":list(pairs[ambiguous]),"distance":d[ambiguous],"required":q}
            if ambiguous is None:
                first_complete=t
                break
        assert first_complete == len(schedule)
        runs.append({"f":f,"queries":len(schedule),"worst_case_cost":sum(schedule),
                     "first_globally_decodable_prefix":first_complete,
                     "penultimate_ambiguous":penultimate})
    return {"real_tau_chamber":[str(lower),str(upper)],"actions":actions,
            "witnesses":observations,"runs":runs}

def main():
    c=read(sys.argv[1])
    r={"pass":"R5_FIXED_ORDER_EARLYSTOP_MINIMAX_EQUAL_PREPAID",
       "input_sha256":SHA,"hypotheses":256,"budget_types":101,"pairs":32640,
       "fifth":test(c,L,U,[216,223,296],[(0,1,216),(0,64,223),(16,32,296)]),
       "critical":test(c,T,D,[217,218,224,298],
                       [(11,14,217),(4,10,218),(0,64,224),(16,32,298)])}
    print(json.dumps(r,indent=2))
    print("PASS_R5_FIXED_ORDER_EARLYSTOP_MINIMAX_EQUAL_PREPAID",file=sys.stderr)
if __name__ == "__main__":
    main()
