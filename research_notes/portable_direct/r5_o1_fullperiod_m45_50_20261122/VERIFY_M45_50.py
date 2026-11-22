#!/usr/bin/env python3
"""Exact finite-field recheck of all 84 new R5 period witnesses, m=45..50.
Run from any working directory: python3 VERIFY_M45_50.py.
Reuses the exact pinned parent verifier on the same immutable branch;
does not require Python packages beyond the standard library.
"""
import importlib.util
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / "r5_o1_first_contraction_m37_20261122" / "VERIFY_MODULAR.py"
spec = importlib.util.spec_from_file_location("frozen_r5_modular", PARENT)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

W = [7,9,11,13,17,19,23,25,27,29,31,32,37,43]
L = 229746052653717600
# Exact values from six independent completed invocation groups;
# each tuple is (R_m(w_d), (q*d/dq)R_m(w_d)) mod the declared prime.
EXPECTED = {
 45: [(0,7715),(0,7158),(8841,6213),(6638,2880),(1448,3905),(9524,4976),(0,4299),(1034,7242),(0,6261),(372,4951),(0,8589),(3165,7088),(7510,1651),(8782,116)],
 46: [(0,5911),(0,2837),(7458,9374),(8934,8768),(3492,3515),(5187,9825),(0,4811),(0,8772),(0,6789),(7845,6938),(0,1466),(6139,2623),(3911,7002),(8662,3303)],
 47: [(0,4736),(0,4148),(7597,3486),(7518,9281),(0,464),(4570,973),(7856,6840),(0,733),(0,1647),(8431,6805),(0,4922),(7207,8595),(5236,3808),(8239,9245)],
 48: [(0,5980),(0,2132),(9431,4570),(0,6108),(0,7302),(4673,7760),(2301,9562),(0,3430),(0,2926),(7925,4273),(0,1942),(1552,4969),(1287,505),(7185,4416)],
 49: [(0,3588),(0,7917),(3294,9255),(0,9615),(0,3750),(7504,9978),(9038,2231),(0,5968),(0,3019),(5220,5527),(0,4135),(4986,7706),(3978,3471),(8459,7040)],
 50: [(0,563),(0,249),(3786,6329),(0,9919),(0,2493),(8307,6710),(1462,5600),(0,110),(0,6446),(7288,4059),(0,7511),(4012,4097),(7544,7087),(843,9504)],
}

def singleton_root43(m, prime, root):
    # Distinct derivation: at primitive 43rd roots only E1 survives.
    ps = base.S[1]
    h = [1] + [0] * (m-1)
    for price in ps:
        t = pow(root, price, prime)
        for n in range(1, m):
            h[n] = (h[n] + t * h[n-1]) % prime
    product = 1
    for price in ps:
        product = product * (1-pow(root, price, prime)) % prime
    return product * sum(h) % prime

def main():
    assert math.lcm(*W) == L
    candidates = [d for d in range(1,315)
                  if sum(p % d == 0 for p in range(214,315)) >= 3]
    assert len(candidates) == 40 and math.lcm(*candidates) == L
    assert [d for d in candidates if d % 43 == 0] == [43]
    rows = []
    for m in range(45,51):
        observed = [base.calc(m,d) for d in W]
        assert all(r["witness"] for r in observed), m
        pairs = [(r["R0"], r["DR0"]) for r in observed]
        assert pairs == EXPECTED[m], (m, pairs)
        r43 = observed[-1]
        assert r43["R0"] == singleton_root43(m,r43["p"],r43["root"]), m
        # Independently recover the zero-order 43-phase from earlier thresholds.
        assert r43["R0"] == base.calc(m-43,43)["R0"], m
        rows.extend(observed)
        print("PASS",m,"14/14; root43",r43["R0"],flush=True)
    report = {
        "schema": "R5_O1_M45_50_EXACT_MODULAR_CERT_V1",
        "scientific_pin": "enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15",
        "parent": "enterprise-math@9d2acb53a59a2790c499f6890424feb335a33de6",
        "thresholds": list(range(45,51)), "candidate_count": len(candidates),
        "witness_orders": W, "universal_period_upper": L, "rows": rows,
        "scope": "finite exact m=45..50; author checked, not independently reviewed"
    }
    dest = HERE / "GENERATED_FULL_CERTIFICATE.json"
    dest.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("ALL CHECKS PASS; 84 verified witnesses")

if __name__ == "__main__":
    main()
