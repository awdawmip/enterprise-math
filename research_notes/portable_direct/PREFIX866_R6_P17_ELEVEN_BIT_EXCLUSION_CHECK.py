#!/usr/bin/env python3
"""Exact p=17 fixed-odd two-read complete-transition impossibility at B=11.
All pairs of odd moduli 3..2047 are covered; pruning uses proven necessary
conditions. The residue test uses only old-state fiber r=0, not sampled states.
"""
import json
from math import gcd

P, N, B = 17, 1 << 17, 11
CAP, TRANSITIONS = (1 << B) - 1, N * (P + 1)

def half_period(q):
    x = 2 % q
    for d in range(1, q + 1):
        if x == 1 or x == q - 1:
            return d
        x = 2 * x % q
    raise AssertionError("invalid modular order")

def fiber_zero(q1):
    return [v for u in range(0, N, q1)
            for v in [u] + [u ^ (1 << i) for i in range(P)]]

def injective_fiber(q1, q2):
    residues = set()
    for v in fiber_zero(q1):
        r = v % q2
        if r in residues:
            return False
        residues.add(r)
    return True

def main():
    q_safe = [q for q in range(3, CAP + 1, 2) if half_period(q) >= P]
    tested_q1 = 0
    candidates = 0
    fiber_pass = []
    for q1 in q_safe:
        first_bucket_size = ((N + q1 - 1) // q1) * (P + 1)
        if TRANSITIONS > q1 * CAP or first_bucket_size > CAP:
            continue
        qs = [q2 for q2 in q_safe
              if q1 * q2 >= TRANSITIONS
              and q1 * q2 // gcd(q1, q2) >= N
              and q2 >= first_bucket_size]
        if not qs:
            continue
        tested_q1 += 1
        candidates += len(qs)
        # Generate once per q1, test every possible q2 with exact integer residue comparisons.
        vals = fiber_zero(q1)
        for q2 in qs:
            seen = set()
            for v in vals:
                r = v % q2
                if r in seen:
                    break
                seen.add(r)
            else:
                fiber_pass.append([q1, q2])
    # Independently verify the published upper witness using the exact CRT lemma.
    g, a, b = 37, 33, 109
    assert half_period(g) == 18 >= P
    assert gcd(a, b) == 1
    assert g * a * b >= N
    assert max((g * a).bit_length(), (g * b).bit_length()) == 12
    assert len(q_safe) == 958
    assert tested_q1 == 441 and candidates == 113884
    assert not fiber_pass
    cert = {
      "schema": "PREFIX866_P17_EXACT_ELEVEN_BIT_NO_GO_V1",
      "status": "ALL_EXACT_ASSERTIONS_PASSED",
      "model": "complete ordered no-op-or-one-bit-flip transition; fixed ordered odd moduli",
      "p": P, "peak_width_excluded": B,
      "total_ordered_candidate_pairs": ((CAP - 1) // 2)**2,
      "half_period_safe_moduli": len(q_safe),
      "eligible_first_moduli_after_necessary_bounds": tested_q1,
      "candidate_pairs_after_necessary_bounds": candidates,
      "pairs_surviving_exact_full_zero_fiber": len(fiber_pass),
      "exact_optimal_peak_width": 12,
      "constructive_upper_witness": {"q1": g*a, "q2": g*b,
                                     "g": g, "a": a, "b": b,
                                     "h_g": half_period(g), "lcm": g*a*b},
    }
    print(json.dumps(cert, ensure_ascii=False, separators=(',', ':')))

if __name__ == '__main__':
    main()
