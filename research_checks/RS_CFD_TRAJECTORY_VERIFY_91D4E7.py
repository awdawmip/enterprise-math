#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE.parent / "research_artifacts" / "RS-CFD-TRAJECTORY-VERIFY-20260910_91D4E7" / "cycle_block_manifest.json"

def binom_tail_half(n: int, k: int) -> Fraction:
    return Fraction(sum(math.comb(n, i) for i in range(k, n + 1)), 2**n)

def binom_tail(n: int, k: int, p: Fraction) -> Fraction:
    q = 1 - p
    return sum((Fraction(math.comb(n, i)) * p**i * q**(n-i) for i in range(k, n+1)), Fraction(0))

def block_success(signs) -> bool:
    return sum(x > 0 for x in signs) >= 4

def verify_sign_reversal():
    patterns = 0
    for v in itertools.product((-1, 0, 1), repeat=6):
        patterns += 1
        neg = tuple(-x for x in v)
        assert not (block_success(v) and block_success(neg))
    assert patterns == 729
    return patterns

def verify_schedule(m):
    s = m["sampling"]
    literal = ["ABC","BCA","CAB","ACB","CBA","BAC"]
    assert s["cycles"] == 23
    assert s["orders_per_cycle"] == 6
    assert s["scheduled_triplets"] == 138
    assert s["arm_executions"] == 414
    assert len(s["cycle_orders"]) == 23
    seed = s["seed_material"]
    for c, got in enumerate(s["cycle_orders"], start=1):
        expected = sorted(literal, key=lambda o: hashlib.sha256(f"{seed}|cycle={c}|order={o}".encode()).hexdigest())
        assert got == expected
        assert sorted(got) == sorted(literal)
    position = {(a,p): 0 for a in "ABC" for p in range(3)}
    precedence = {(a,b): 0 for a in "ABC" for b in "ABC" if a != b}
    idx = 0
    for cycle in s["cycle_orders"]:
        for order in cycle:
            idx += 1
            for p,a in enumerate(order):
                position[(a,p)] += 1
            for a,b in precedence:
                if order.index(a) < order.index(b):
                    precedence[(a,b)] += 1
    assert idx == 138
    assert all(v == 46 for v in position.values())
    assert all(v == 69 for v in precedence.values())
    return position, precedence

def verify_statistics(m):
    st = m["statistics"]
    assert st["global_alpha"] == 0.05
    assert st["per_component_alpha"] == 0.05
    assert st["n_cycles_fixed"] == 23
    assert st["cycle_positive_required"] == 16
    t16 = binom_tail_half(23,16)
    t15 = binom_tail_half(23,15)
    assert t16 == Fraction(763,16384) and t16 <= Fraction(1,20)
    assert t15 == Fraction(440485,4194304) and t15 > Fraction(1,20)
    t17 = binom_tail_half(23,17)
    assert t17 == Fraction(145499,8388608) and t17 <= Fraction(1,40)
    assert t16 > Fraction(1,40)
    power = binom_tail(23,16,Fraction(4,5))
    assert power == Fraction(11068512973881344,11920928955078125)
    frechet = 2*power - 1
    assert frechet == Fraction(10216096992684563,11920928955078125)
    assert power > Fraction(9,10) and frechet > Fraction(4,5)
    return t16, t15, t17, power, frechet

def decision(cycles, independence_ok, correctness_ok=True, route_ok=True, horizon_ok=True):
    if not (independence_ok and correctness_ok and route_ok and horizon_ok):
        return False
    assert len(cycles) == 23
    def wins(g):
        return sum(sum(x > 0 for x in c[g]) >= 4 for c in cycles)
    ab, cb, ac = wins("AB"), wins("CB"), wins("AC")
    return ab >= 16 and cb >= 16 and ac < 16

def synthetic_fail_closed():
    pos=[1,1,1,1,-1,-1]; neg=[-1,-1,-1,-1,1,1]; acsafe=[-1]*6
    good=[{"AB":pos,"CB":pos,"AC":acsafe} for _ in range(16)]+[{"AB":neg,"CB":neg,"AC":acsafe} for _ in range(7)]
    assert decision(good, True) and not decision(good, False)
    fail_ab=[{"AB":pos,"CB":pos,"AC":acsafe} for _ in range(15)]+[{"AB":neg,"CB":pos,"AC":acsafe} for _ in range(8)]
    assert not decision(fail_ab, True)
    veto=[{"AB":pos,"CB":pos,"AC":pos} for _ in range(16)]+[{"AB":pos,"CB":pos,"AC":acsafe} for _ in range(7)]
    assert not decision(veto, True)
    assert not block_success([0]*6)
    return 4

def main():
    m=json.loads(MANIFEST.read_text())
    patterns=verify_sign_reversal(); verify_schedule(m)
    t16,t15,t17,power,frechet=verify_statistics(m); synthetics=synthetic_fail_closed()
    out={"status":"PASS","sign_patterns_checked":patterns,"cycles":23,"triplets":138,"arm_executions":414,"position_balance_per_arm_per_slot":46,"directed_pair_precedence_each":69,"iut_component_critical":"16/23","iut_component_null_tail":f"{t16.numerator}/{t16.denominator}","15_of_23_tail":f"{t15.numerator}/{t15.denominator}","separate_claim_bonferroni_critical":"17/23","separate_claim_null_tail":f"{t17.numerator}/{t17.denominator}","power_at_p_block_4_5":f"{power.numerator}/{power.denominator}","frechet_joint_lower_bound":f"{frechet.numerator}/{frechet.denominator}","synthetic_fail_closed_cases":synthetics,"cross_cycle_independence_certified":False,"native_host_run":False}
    print(json.dumps(out, indent=2, sort_keys=True)); return 0

if __name__ == "__main__":
    raise SystemExit(main())
