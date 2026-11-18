#!/usr/bin/env python3
"""Full exact-input corroboration for the R5 f=8 conditional corruption profile.
Run: python3 VERIFY_R5_CONDITIONAL_ERROR_PROFILE.py EXACT_R5_ALL_101_BUDGETS.json
"""
import hashlib
import json
import sys

SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L = 25845652773852463277015040000
U = 58182461585441404127941754880
T = 1876919155234970890319953920000
D = 1882951873548292168718745600000

def load(path):
    raw = open(path,"rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA
    o = json.loads(raw)
    assert o["mask_count"] == 256 and o["budget_range"] == [214,314]
    return {k:[int(v) for v in o["counts_and_cohorts"][str(k)]["counts"]]
            for k in (216,223,296,217,218,224,298)}

def test(centers,low,high,actions,witnesses):
    pairs = [(a,b) for a in range(256) for b in range(a+1,256)]
    assert len(pairs) == 32640
    sep = {k:bytearray(abs(centers[k][a]-centers[k][b])>high-1
                     for a,b in pairs) for k in actions}
    sep_low = {k:bytearray(abs(centers[k][a]-centers[k][b])>low
                         for a,b in pairs) for k in actions}
    assert all(any(sep[k][i] for k in actions) for i in range(32640))
    for a,b,k in witnesses:
        j = pairs.index((a,b))
        assert sep[k][j]==sep_low[k][j]==1
        assert sum(sep[x][j] for x in actions)==1
        assert sum(sep_low[x][j] for x in actions)==1
    profiles = []
    f=8
    for r in range(f+1):
        q=f+r+1
        schedule=actions*q
        distances=bytearray(32640)
        first_complete=None
        penultimate=None
        for t,k in enumerate(schedule,1):
            mask=sep[k]
            for j in range(32640):
                distances[j]+=mask[j]
            ambiguous=next((j for j,d in enumerate(distances) if d<q),None)
            if t==len(schedule)-1:
                assert ambiguous is not None
                penultimate={"pair":list(pairs[ambiguous]),
                             "separation_count":distances[ambiguous],
                             "needed":q}
            if ambiguous is None:
                first_complete=t
                break
        assert first_complete==len(schedule)
        profiles.append({"f":8,"r":r,"q":q,"first_complete_prefix":first_complete,
                         "exact_cost":sum(schedule),"penultimate_ambiguity":penultimate})
    return {"tau_real_interval":[str(low),str(high)],"budgets":actions,"profiles":profiles}

def main():
    c=load(sys.argv[1])
    result={
       "pass":"R5_CONDITIONAL_ADAPTIVE_STOP_PROFILE_F8_ALL_R",
       "input_sha256":SHA,"hypothesis_pairs":32640,
       "fifth":test(c,L,U,[216,223,296],
                    [(0,1,216),(0,64,223),(16,32,296)]),
       "critical":test(c,T,D,[217,218,224,298],
                       [(11,14,217),(4,10,218),(0,64,224),(16,32,298)])}
    print(json.dumps(result,indent=2))
    print(result["pass"],file=sys.stderr)

if __name__=="__main__":
    main()
