#!/usr/bin/env python3
from fractions import Fraction
from math import comb
import json

N = 23
R = 16
ALPHA = Fraction(1, 20)

def success_intersection_bound(k: int) -> Fraction:
    vals = [Fraction(1, 1)]
    vals.extend(
        Fraction(comb(N, j), (2 ** j) * comb(R, j))
        for j in range(1, min(k, R) + 1)
    )
    return min(vals)

def verify_success_intersection_envelope():
    rows = []
    for k in range(1, N + 1):
        p = success_intersection_bound(k)
        # Primal witness: with probability p choose a uniform R-subset of [N]
        # as the success set; otherwise choose the empty set.
        for j in range(1, k + 1):
            q = (
                p * Fraction(comb(R, j), comb(N, j))
                if j <= R else Fraction(0, 1)
            )
            assert q <= Fraction(1, 2 ** j)
        # Dual certificate: choose an order j attaining the minimum.
        candidates = [
            (j, Fraction(comb(N, j), (2 ** j) * comb(R, j)))
            for j in range(1, min(k, R) + 1)
        ]
        j_star, dual_value = min(candidates, key=lambda x: x[1])
        assert dual_value == p
        # Pointwise majorant of 1{S>=R} by C(S,j*)/C(R,j*).
        for s in range(N + 1):
            lhs = Fraction(1 if s >= R else 0, 1)
            rhs = Fraction(comb(s, j_star), comb(R, j_star)) if s >= j_star else Fraction(0, 1)
            assert lhs <= rhs
        rows.append({
            "k": k,
            "j_star": j_star,
            "bound": f"{p.numerator}/{p.denominator}",
            "decimal": float(p),
        })
    return rows

def verify_22wise_independence_witness():
    # Binomial baseline under full 23-way independence.
    baseline = [Fraction(comb(N, s), 2 ** N) for s in range(N + 1)]
    baseline_tail = sum(baseline[R:], Fraction(0, 1))

    # A null-vector for moments through order 22 is (-1)^s C(23,s).
    alternating_tail = sum(((-1) ** s) * comb(N, s) for s in range(R, N + 1))
    sign = 1 if alternating_tail >= 0 else -1

    # Endpoint perturbation: even-parity binomial law for this sign.
    p = [
        Fraction(comb(N, s), 2 ** N) * (1 + sign * ((-1) ** s))
        for s in range(N + 1)
    ]
    assert sum(p, Fraction(0, 1)) == 1
    assert all(x >= 0 for x in p)

    # Exact all-success intersection moments through order 22.
    # Exchangeability plus inclusion-exclusion implies full 22-wise
    # Bernoulli(1/2) independence for every 0/1 pattern on <=22 coordinates.
    for j in range(0, 23):
        lhs = sum((p[s] * comb(s, j) for s in range(N + 1)), Fraction(0, 1))
        rhs = Fraction(comb(N, j), 2 ** j)
        assert lhs == rhs, (j, lhs, rhs)

    # Explicit pattern check by inclusion-exclusion.
    for m in range(0, 23):
        for a in range(0, m + 1):
            prob = sum(
                Fraction(((-1) ** t) * comb(m - a, t), 2 ** (a + t))
                for t in range(0, m - a + 1)
            )
            assert prob == Fraction(1, 2 ** m)

    tail = sum(p[R:], Fraction(0, 1))
    delta = Fraction(abs(alternating_tail), 2 ** N)
    assert tail == baseline_tail + delta
    assert baseline_tail == Fraction(763, 16384)
    assert tail == Fraction(35075, 524288)
    assert tail > ALPHA
    assert baseline_tail < ALPHA
    return {
        "baseline_23wise_tail": f"{baseline_tail.numerator}/{baseline_tail.denominator}",
        "baseline_23wise_decimal": float(baseline_tail),
        "max_22wise_witness_tail": f"{tail.numerator}/{tail.denominator}",
        "max_22wise_witness_decimal": float(tail),
        "alternating_tail_sum": alternating_tail,
        "tail_delta": f"{delta.numerator}/{delta.denominator}",
        "alpha": f"{ALPHA.numerator}/{ALPHA.denominator}",
    }

def main():
    rows = verify_success_intersection_envelope()
    full = verify_22wise_independence_witness()
    plateau = min(Fraction(row["bound"]) for row in rows)
    assert plateau == Fraction(7429, 53248)
    assert plateau > ALPHA
    out = {
        "schema": "CFD_KWISE_TAIL_CERTIFICATE_V1",
        "n": N,
        "r": R,
        "success_intersection_envelope": rows,
        "all_order_success_intersection_floor": f"{plateau.numerator}/{plateau.denominator}",
        "all_order_success_intersection_floor_decimal": float(plateau),
        "full_kwise_independence_contrast": full,
        "conclusion": (
            "No k<=23 of one-sided all-success intersection upper bounds restores alpha<=0.05; "
            "even exact full 22-wise Bernoulli(1/2) independence is insufficient, while exact "
            "23-wise independence gives the binomial tail below 0.05."
        ),
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
