#!/usr/bin/env python3
"""Exact 12-hypothesis f=8 minimal query-type checker for R5.

Supply SHA-pinned EXACT_R5_ALL_101_BUDGETS.json and compile
VERIFY_EXACT_SMALL_MINIMAX.cpp to ./exact_small.
"""
from pathlib import Path
from itertools import combinations
import hashlib, json, subprocess

P=Path(__file__).resolve().parent
FROZEN_SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L=25845652773852463277015040000
U=58182461585441404127941754880
H=(18,24,82,34,17,0,1,2,3,144,208,255)
F=8

def family(values, tau):
    by={}
    for j,value in enumerate(values):
        by[value]=by.get(value,0)|(1<<j)
    supports={sum(mask for value,mask in by.items()
                  if lo<=value<=lo+tau) for lo in by}
    return tuple(sorted(x for x in supports if not any(
        x!=y and x&y==x for y in supports)))

def cheapest_families(table,tau):
    classes={}
    for k in range(214,315):
        vals=tuple(int(table[str(k)]["counts"][h]) for h in H)
        classes.setdefault(family(vals,tau),k)
    return {k:s for s,k in classes.items()}

def solve(actions,costs):
    lines=[f"{len(H)} {len(costs)}"]
    lines += [f"{k} {len(actions[k])} "+" ".join(map(str,actions[k]))
              for k in costs]
    path=P/"_r5_h12_exact.actions"
    path.write_text("\n".join(lines)+"\n",encoding="utf-8")
    try:
        proc=subprocess.run([str(P/"exact_small"),str(path),str(F)],
            text=True,capture_output=True,check=True,timeout=120)
    finally:
        path.unlink(missing_ok=True)
    fields=dict(s.split("=",1) for s in proc.stdout.split() if "=" in s)
    assert int(fields["n"])==len(H) and int(fields["f"])==F
    return {"query_budgets":list(costs),"optimal_cost":int(fields["V"]),
            "bellman_states":int(fields["states"]),"stdout":proc.stdout.strip()}

def main():
    raw=(P/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest()==FROZEN_SHA
    T=json.loads(raw)["counts_and_cohorts"]
    assert set(map(int,T))==set(range(214,315))
    assert all(len(v["counts"])==256 for v in T.values())

    fl=cheapest_families(T,L)
    full=(1<<len(H))-1
    info={k:s for k,s in fl.items() if s!=(full,)}
    assert len(fl)==10
    assert sorted(info)==[214,215,216,221,222,223,294,295,296]
    pairs={(i,j) for i in range(len(H)) for j in range(i+1,len(H))}
    distinguish={k:{(i,j) for i,j in pairs if abs(
        int(T[str(k)]["counts"][H[i]])-int(T[str(k)]["counts"][H[j]]))>L}
        for k in info}
    for k,supports in info.items():
        assert distinguish[k]=={(i,j) for i,j in pairs if all(
            not ((s>>i)&1 and (s>>j)&1) for s in supports)}

    finite=[]; impossible=0
    for costs in combinations(sorted(info),4):
        if set.union(*(distinguish[k] for k in costs))!=pairs:
            impossible+=1
        else:
            finite.append(solve(info,costs))
    assert impossible==117 and len(finite)==9
    assert {tuple(x["query_budgets"]):x["optimal_cost"] for x in finite}=={
        (214,215,223,296):10244,
        (214,216,223,296):8343,
        (214,221,223,296):8444,
        (215,216,223,296):8343,
        (215,221,223,296):8444,
        (216,221,223,296):8343,
        (216,222,223,296):8343,
        (216,223,294,296):8343,
        (216,223,295,296):8343
    }
    fr=cheapest_families(T,U-1)
    five=(214,215,216,223,296)
    assert len(fr)==10 and all(k in fr for k in five)
    right=solve(fr,five)
    assert right["optimal_cost"]==8335 and right["bellman_states"]==3539792
    out={
        "schema":"R5_H12_F8_FIVE_ACTION_MINIMALITY_CERT_V1",
        "source_commit":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
        "frozen_table_sha256":FROZEN_SHA,
        "H12":list(H),"f":F,"noise_left":str(L),
        "noise_right_exclusive":str(U),
        "physical_costs":{"min":214,"max":314,"count":101},
        "left_family_representatives":sorted(fl),
        "left_informative_representatives":sorted(info),
        "four_subsets_total":len(finite)+impossible,
        "four_pairwise_impossible":impossible,
        "four_finite_exact_results":finite,
        "four_minimum_at_left":min(x["optimal_cost"] for x in finite),
        "right_five_action_result":right,
        "conclusion":"Exactly five distinct query-budget values needed and sufficient for cost 8335 on H12 throughout chamber.",
        "scope":"Named scalar observer only; not native X6 state equivalence.",
        "review":"AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED"
    }
    (P/"RESULTS_MINIMAL_FIVE.json").write_text(
        json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("PASS_R5_H12_F8_MINIMAL_FIVE_QUERY_BUDGET_TYPES",
          "left_four_subsets=126","pairwise_impossible=117",
          "four_finite=9","left_four_min=8343",
          "right_five=8335","right_five_Bellman_states=3539792")

if __name__=="__main__":
    main()
