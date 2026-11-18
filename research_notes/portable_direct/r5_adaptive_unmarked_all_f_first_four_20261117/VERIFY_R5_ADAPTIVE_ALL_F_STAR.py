#!/usr/bin/env python3
"""R5 all-f symbolic-star witness: exact verifier of four noise chambers.

Usage: python VERIFY_R5_ADAPTIVE_ALL_F_STAR.py EXACT_R5_ALL_101_BUDGETS.json
The symbolic minimax argument is in RESEARCH.md; this verifies its finite premises.
"""
import hashlib
import json
import sys
from pathlib import Path

FROZEN_SHA256="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
SCIENCE_PIN="435e77af0d180eac32bd1f9c4c464bc4010b7551"
CHAMBERS=(
    (0,76289178155959966960189440,(214,223,294),(16,17,80,32)),
    (76289178155959966960189440,3133722521542003559403356160,(214,223,295),(16,17,80,32)),
    (3133722521542003559403356160,13883516118328421520506880000,(214,223,296),(16,17,80,32)),
    (13883516118328421520506880000,25845652773852463277015040000,(215,223,296),(18,24,82,34)),
)

def verify(path):
    blob=Path(path).read_bytes()
    assert hashlib.sha256(blob).hexdigest()==FROZEN_SHA256,"unexpected frozen input"
    data=json.loads(blob)
    N={int(k):tuple(map(int,record["counts"]))
       for k,record in data["counts_and_cohorts"].items()}
    assert set(N)==set(range(214,315))
    assert all(len(v)==256 for v in N.values())
    outcome={"schema":"R5_FIRST_FOUR_ALL_F_CERT_V1","frozen_science_pin":SCIENCE_PIN,
             "source_sha256":FROZEN_SHA256,"count_entries":25856,
             "chambers":[]}
    for number,(L,U,Q,W) in enumerate(CHAMBERS,1):
        base=W[0]
        supports=[]
        for h in W[1:]:
            s={k for k,v in N.items() if abs(v[h]-v[base])>L}
            supports.append(s)
        assert all(supports)
        assert all(not(supports[i]&supports[j]) for i in range(3)
                   for j in range(i+1,3))
        assert [min(s) for s in supports]==list(Q)
        max_zero_diameter=0
        for k in N:
            targeted=[j+1 for j,s in enumerate(supports) if k in s]
            assert len(targeted)<=1
            non_target=[N[k][W[i]] for i in range(4) if i not in targeted]
            diameter=max(non_target)-min(non_target)
            max_zero_diameter=max(max_zero_diameter,diameter)
            assert diameter<=L,(number,k,"no common zero interval",diameter,L)
        signature_gap=min(max(abs(N[k][a]-N[k][b]) for k in Q)
                          for a in range(256) for b in range(a+1,256))
        assert signature_gap>=U
        # Query in descending order. Verify centers only within each already
        # identified fiber: global minimum gap can be smaller in chamber 4.
        fibers=[list(range(256))]
        conditional={}
        for k in reversed(Q):
            gaps=[];new=[]
            for group in fibers:
                centers=sorted({N[k][h] for h in group})
                gaps.extend(v-u for u,v in zip(centers,centers[1:]))
                for value in centers:
                    new.append([h for h in group if N[k][h]==value])
            assert gaps and min(gaps)>=U,(number,k,min(gaps) if gaps else None,U)
            conditional[str(k)]=str(min(gaps))
            fibers=new
        assert len(fibers)==256 and all(len(g)==1 for g in fibers)
        S=sum(Q)
        assert Q[1]<=2*Q[0] and Q[2]<=Q[1]+2*Q[0]
        outcome["chambers"].append({
            "number":number,"noise_tau":[str(L),str(U)],
            "four_state_witness":list(W),"optimal_budgets":list(Q),
            "support_sizes":[len(s) for s in supports],
            "maximum_non_target_diameter":str(max_zero_diameter),
            "descending_conditional_center_gaps":conditional,
            "joint_signature_margin":str(signature_gap),
            "exact_all_f_optimal_cost":f"{S}+{S+Q[0]}f",
            "full_pair_comparisons":32640,"window_checks":101
        })
    outcome["status"]="PASS_R5_FIRST_FOUR_CHAMBERS_UNIVERSAL_F_STAR_CERT"
    return outcome

if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("Usage: python VERIFY_R5_ADAPTIVE_ALL_F_STAR.py EXACT_R5_ALL_101_BUDGETS.json")
    result=verify(sys.argv[1])
    print(result["status"])
    for v in result["chambers"]:
        print(v["number"],v["exact_all_f_optimal_cost"],v["four_state_witness"])
    Path(__file__).with_name("RESULTS_EXACT.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n")
