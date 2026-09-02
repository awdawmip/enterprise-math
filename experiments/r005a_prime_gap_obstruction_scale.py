#!/usr/bin/env python3
"""R005-A least-basis failure -> prime-gap obstruction scale verifier."""

from __future__ import annotations

from fractions import Fraction
import json


def obstruction_lambda(p: int) -> Fraction:
    return Fraction(1, 1) - Fraction(3, 2 * p)


def exact_constant(p: int, k: int) -> float:
    A = k**p
    U = (k + 1) ** p - 1
    W = U - A
    return W * (k ** (1.5 - p)) / (U ** (1 / (2 * p)))


def verify_bound(p: int, k: int, q: int) -> tuple[float, float]:
    A = k**p
    U = (k + 1) ** p - 1
    W = U - A
    lam = float(obstruction_lambda(p))
    x = A / q
    lhs = W / q
    rhs = exact_constant(p, k) * (x ** lam)
    return lhs, rhs


def main() -> None:
    bounded_checks = 0
    min_margin = None

    for p in range(2, 9):
        for k in range(2, 500):
            U = (k + 1) ** p - 1
            c3 = int(round(U ** (1 / 3)))
            while (c3 + 1) ** 3 <= U:
                c3 += 1
            while c3**3 > U:
                c3 -= 1

            samples = {2, 3, c3, max(2, c3 - 1), max(2, c3 // 2)}
            samples.update(
                max(2, (c3 * j) // 11)
                for j in range(1, 11)
            )

            for q in sorted(q for q in samples if 2 <= q <= c3):
                lhs, rhs = verify_bound(p, k, q)
                margin = lhs - rhs
                assert margin > -1e-8 * max(1.0, lhs)
                bounded_checks += 1
                if min_margin is None or margin < min_margin:
                    min_margin = margin

    rows = []
    for p in range(2, 9):
        lam = obstruction_lambda(p)
        rows.append(
            {
                "p": p,
                "lambda": f"{lam.numerator}/{lam.denominator}",
                "lambda_decimal": float(lam),
                "asymptotic_gap_constant": p,
                "established_BHP_0_525_rules_out_infinite_failure": float(lam) > 0.525,
                "Li_preprint_0_52_rules_out_infinite_failure_if_accepted": float(lam) > 0.52,
            }
        )

    assert [r["p"] for r in rows if r["established_BHP_0_525_rules_out_infinite_failure"]] == [4,5,6,7,8]
    assert [r["p"] for r in rows if r["Li_preprint_0_52_rules_out_infinite_failure_if_accepted"]] == [4,5,6,7,8]

    result = {
        "status": "R005-A LEAST-BASIS PRIME-GAP OBSTRUCTION SCALE CHECK",
        "bounded_algebra_checks": bounded_checks,
        "minimum_floating_margin_in_sample": min_margin,
        "theorem": (
            "If a p-power basin at k has no least divisor-witness basis, "
            "then some consecutive prime gap p0<r containing x=k^p/q "
            "satisfies gap > c_{p,k} * p0^lambda, where "
            "lambda=1-3/(2p), c_{p,k}=W*k^(3/2-p)/U^(1/(2p)), "
            "and c_{p,k}->p."
        ),
        "infinite_failure_consequence": (
            "Infinitely many no-least p-power basins imply "
            "limsup gap_n / prime_n^lambda >= p."
        ),
        "p2_specialization": (
            "Infinitely many no-least square basins imply "
            "limsup gap_n / prime_n^(1/4) >= 2."
        ),
        "rows": rows,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
