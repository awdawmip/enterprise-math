#!/usr/bin/env python3
"""Exact census of seven-label extensions of the pinned R5 sextet.

Usage: python3 VERIFY_R5_SINGLE_AUGMENTATION.py EXACT_R5_ALL_101_BUDGETS.json stages_18.json ./r5solve
Compile first: g++ -O3 -std=c++17 SOLVE_R5_SINGLE_AUGMENTATION.cpp -o r5solve
Output: RESULT_R5_SINGLE_AUGMENTATION.json.
"""
import collections, hashlib, json, subprocess, sys
from pathlib import Path
PIN = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
SCIENCE_COMMIT = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
H = (0,16,32,48,1,64)
BASE_F0_TO_F8 = (732,1678,2624,3570,4516,5462,6408,7354,8300)

def maximal(masks):
    return tuple(sorted(s for s in masks if not any(s!=q and (s&q)==s for q in masks)))

def family_window(centers, labels, tau):
    a=[centers[u] for u in labels]
    return maximal({sum(1<<i for i,y in enumerate(a) if x<=y<=x+tau) for x in a})

def family_endpoint(centers, labels, tau):
    a=[centers[u] for u in labels]
    left=sorted({2*x-tau for x in a})
    return maximal({sum(1<<i for i,x in enumerate(a) if 2*x-tau<=z<=2*x+tau) for z in left})

def main():
    ip,sp,exe=map(Path,sys.argv[1:4])
    raw=ip.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==PIN,"frozen input SHA-256 mismatch"
    j=json.loads(raw)
    centers={k:tuple(map(int,j["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)}
    assert len(centers)==101 and all(len(v)==256 for v in centers.values())
    stages=json.loads(sp.read_text())
    tau=int(stages["U"])-1
    assert int(stages["L"])<=tau
    rows=[]; signatures=collections.defaultdict(list); crosschecks=0
    for u in range(256):
        if u in H:continue
        labels=H+(u,);classes=collections.defaultdict(list)
        for k,c in centers.items():
            x=family_window(c,labels,tau)
            y=family_endpoint(c,labels,tau)
            assert x==y,(u,k,x,y)
            crosschecks+=1
            classes[x].append(k)
        representatives=tuple(sorted((min(ks),s) for s,ks in classes.items() if s!=(127,)))
        signatures[representatives].append(u)
        inp=("7\n"+str(len(representatives))+"\n"+
             "".join(f"{k} {len(ss)} "+" ".join(map(str,ss))+"\n" for k,ss in representatives))
        values=[]; root=None
        for f in range(9):
            r=subprocess.run([str(exe.resolve()),str(f)],input=inp,text=True,
                             stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
            fields=r.stdout.splitlines()[0].split()
            assert fields[0]=="RESULT" and fields[2]=="n=7" and fields[3]==f"f={f}"
            values.append(int(fields[1]))
            if f==8:root=[line for line in r.stdout.splitlines() if line.startswith("ROOT ")]
        expected0=733 if 16<=u%64<=47 else 732
        assert values[0]==expected0 and tuple(values[1:])==BASE_F0_TO_F8[1:],(u,values)
        rows.append({"added_label":u,"values_f0_to_f8":values,
                     "observer_signature_sha256":hashlib.sha256(repr(representatives).encode()).hexdigest(),
                     "cheapest_action_representatives":[k for k,_ in representatives],
                     "f8_root_actions":root})
    assert len(rows)==250 and len(signatures)==42 and crosschecks==25250
    result={
        "schema":"R5_SINGLE_AUGMENTATION_EXACT_CENSUS_V1",
        "status":"AUTHOR_COMPUTED_EXACT_FINITE_NOT_REVIEWED",
        "frozen_science_commit":SCIENCE_COMMIT,
        "frozen_input_sha256":PIN,
        "robust_noise_endpoint_tau":str(tau),
        "base_hypotheses":list(H),
        "test_domain":"u in 0..255 excluding H; f in 0..8",
        "number_of_augmented_subproblems":250,
        "number_of_exact_dp_roots":2250,
        "support_family_cross_checks":crosschecks,
        "distinct_price_aware_observer_signatures":len(signatures),
        "zero_error_value_distribution":{"732":124,"733":126},
        "f1_to_f8_value_formula":"732+946*f, for 1<=f<=8",
        "f8_value_for_every_u":8300,
        "rows":rows,
        "signature_classes":[
            {"representative_label":us[0],"members":us,
             "cheapest_actions":[k for k,_ in signature]}
            for signature,us in sorted(signatures.items(),key=lambda item:item[1][0])
        ],
        "scope":"finite scalar observer only; no full-256 or native Port equivalence claim"
    }
    Path("RESULT_R5_SINGLE_AUGMENTATION.json").write_text(
        json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    print("PASS_R5_SINGLE_AUGMENTATION added= 250 error_budgets= 9 exact_dps= 2250 support_cross_checks= 25250 signature_classes= 42 all_f8= 8300")

if __name__=="__main__":
    main()
