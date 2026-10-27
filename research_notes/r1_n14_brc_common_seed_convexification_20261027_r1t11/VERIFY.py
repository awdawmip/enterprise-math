#!/usr/bin/env python3
"""Exact Fraction checks for two-law shared-seed observer convexification.
No network, randomness, or floating point. Computes two finite examples;
universal theorem in PROOF.md is proved mathematically, not by this program.
"""
from fractions import Fraction as F
from itertools import product
import json


def frac(x):
    return f"{x.numerator}/{x.denominator}"


def joint_binary_model():
    # t=1 symbol i in {0,1}; t=2 symbol is ignored. Both laws IID.
    initial = {"P": (F(3, 4), F(1, 4)), "Q": (F(1, 4), F(3, 4))}
    # A: stop i=1 at t1,D0; continue i=0, decide D1 at t2.
    # B: stop i=0 at t1,D0; continue i=1, decide D0 at t2.
    output = {}
    for name, continue_symbol, final_d in [("A", 0, 1), ("B", 1, 0)]:
        distribution = {}
        for law, probs in initial.items():
            distribution[law] = {
                "T1D0": sum((probs[i] for i in (0, 1) if i != continue_symbol), F(0)),
                "T2D0": probs[continue_symbol] if final_d == 0 else F(0),
                "T2D1": probs[continue_symbol] if final_d == 1 else F(0),
            }
            assert sum(distribution[law].values()) == 1
        output[name] = distribution
    midpoint = {law: {event:(output["A"][law][event]+output["B"][law][event])/2
                     for event in ("T1D0", "T2D0", "T2D1")}
                for law in ("P", "Q")}
    det = midpoint["P"]["T2D1"]*midpoint["Q"]["T2D0"] - midpoint["Q"]["T2D1"]*midpoint["P"]["T2D0"]
    assert det == F(1, 8)
    # For every local fresh coin policy at terminal compressed t2 state *,
    # each law uses the same Bernoulli terminal D1 probability d,
    # so determinant must vanish identically.
    return {"strategies": {name: {law:{e:frac(v) for e,v in output[name][law].items()}
                                 for law in ("P", "Q")} for name in ("A", "B")},
            "half_lottery":{law:{e:frac(v) for e,v in midpoint[law].items()}
                             for law in ("P", "Q")},
            "fresh_coin_determinant":frac(det),
            "lottery_support_size":2}


def ternary_no_go():
    p_rows = [(F(1, 4), F(1, 4), F(1, 2)),
              (F(1, 12), F(3, 4), F(1, 6)),
              (F(1, 6), F(1, 2), F(1, 3))]
    ratios = (F(2), F(1), F(1, 2))
    q_rows = [tuple(ratios[j]*row[j] for j in range(3)) for row in p_rows]
    for rows in (p_rows, q_rows):
        assert all(all(v > 0 for v in row) and sum(row) == 1 for row in rows)
    masses = {"P":{}, "Q":{}}
    for i,j in product(range(3),repeat=2):
        masses["P"][(i,j)] = p_rows[i][j] / 3
        masses["Q"][(i,j)] = q_rows[i][j] / 3
        assert masses["Q"][(i,j)] == ratios[j]*masses["P"][(i,j)]
    assert sum(masses["P"].values()) == sum(masses["Q"].values()) == 1

    # Full policy: continue only i=0; at t2 D1 iff j=0.
    full = {}
    for law in ("P", "Q"):
        full[law] = {
            "T2":sum((masses[law][(0,j)] for j in range(3)),F(0)),
            "T2D1":masses[law][(0,0)],
        }
    gap = full["Q"]["T2D1"] - full["P"]["T2D1"] - F(1,6)*full["P"]["T2"]
    assert gap == F(1,36)

    # All deterministic state-local tables for z1=constant, z2=j:
    # at z1 choose STOP_D0, STOP_D1, or CONTINUE;
    # at z2 choose D0/D1 for each j. The linear witness holds
    # on the convex hull (hence for ANY persistent initial seed).
    tested=0
    max_functional=None
    for action in ("STOP_D0", "STOP_D1", "CONTINUE"):
        for dtuple in product((0,1),repeat=3):
            tested+=1
            vals={}
            for law in ("P", "Q"):
                if action=="CONTINUE":
                    vals[law]={"T2":F(1),
                               "T2D1":sum((masses[law][(i,j)] for i,j in product(range(3),repeat=2) if dtuple[j]==1),F(0))}
                else:
                    vals[law]={"T2":F(0),"T2D1":F(0)}
            val=vals["Q"]["T2D1"] - vals["P"]["T2D1"] - F(1,6)*vals["P"]["T2"]
            if max_functional is None or val>max_functional:
                max_functional=val
            assert val <= 0
    assert tested == 24 and max_functional == 0
    return {"prefix_count": 13,"deterministic_compressed_tables_checked":tested,
            "max_compressed_linear_witness":frac(max_functional),
            "full_witness": {law:{k:frac(v) for k,v in full[law].items()} for law in ("P", "Q")},
            "strict_full_minus_convexified_quotient_gap":frac(gap),
            "q_over_p_terminal_j": [frac(r) for r in ratios]}


def main():
    result={"schema":"ENTERPRISE_MATH_TWO_LAW_CONVEXIFICATION_CERT_V1",
            "arithmetic":"python fractions.Fraction exact rational",
            "scope":"two concrete N=2 finite-law examples; universal statements proved in PROOF.md",
            "nonconvex_midpoint":joint_binary_model(),
            "persistent_seed_still_insufficient":ternary_no_go(),
            "result":"PASS_EXACT_FRACTION"}
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True))

if __name__ == "__main__":
    main()
