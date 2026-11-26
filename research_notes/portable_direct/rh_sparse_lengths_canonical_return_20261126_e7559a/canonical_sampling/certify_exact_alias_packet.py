#!/usr/bin/env python3
"""Exact rational checks of the canonical alias-packet contraction.

The proof applies to the dyadic lattice.  To make a finite demonstration
entirely rational, this script takes log(base)=2*pi, so the frequency
spacing is 1, beta and the residue class gamma mod 1 are rational, and
every coefficient 1/[rho(1-rho)] is an exact rational complex number.
This is an abstract spectrum, not a zeta-zero computation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from math import isqrt
from pathlib import Path


K = 32
Q = F(1, 2) + F(4, K * K)


def rat(x: F) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def read_rat(x: dict) -> F:
    return F(int(x["numerator"]), int(x["denominator"]))


def canonical(beta: F, gamma: F) -> tuple[F, F]:
    aa = gamma * gamma + beta * (1 - beta)
    bb = (2 * beta - 1) * gamma
    dd = aa * aa + bb * bb
    return aa / dd, bb / dd


def choose_heights(u: F, phase: F) -> tuple[F, F]:
    g_squared = F(K * K) / u
    initial = isqrt(g_squared.numerator // g_squared.denominator)
    kp = max(0, initial - 1)
    while (F(kp) + phase) ** 2 * u < K * K:
        kp += 1
    km = max(1, initial - 1)
    while (F(km) - phase) ** 2 * u < K * K:
        km += 1
    return F(kp) + phase, phase - F(km)


def certified_round_down(x: F) -> tuple[int, F, F]:
    # An intentionally conservative interval of width 1/4.  It permits
    # a leftover greater than 1, including when the exact value is integral.
    floor_eighth = (8 * x.numerator) // x.denominator
    lo = F(floor_eighth - 1, 8)
    hi = lo + F(1, 4)
    assert lo <= x <= hi
    multiplicity = max(0, lo.numerator // lo.denominator)
    assert 0 <= x - multiplicity < 2
    return multiplicity, lo, hi


def run_packet(beta: F, phase: F, target: F, steps: int) -> dict:
    delta = 2 * beta - 1
    assert F(1, 2) < beta < 1 and 0 <= phase < 1 and 0 < target <= 1
    u, v = target, F(0)
    total_real, total_imag = F(0), F(0)
    records = []
    for index in range(steps):
        assert (16 * K) ** 2 * v * v <= delta * delta * u**3
        gp, gm = choose_heights(u, phase)
        rp, ip = canonical(beta, gp)
        rm, im_signed = canonical(beta, gm)
        im = -im_signed
        determinant = rp * im + rm * ip
        xx = (u * im / 2 + v * rm) / determinant
        yy = (u * ip / 2 - v * rp) / determinant
        assert xx > 0 and yy > 0 and xx + yy <= 6 * K * K
        mp, lox, hix = certified_round_down(xx)
        mm, loy, hiy = certified_round_down(yy)
        next_u = u - mp * rp - mm * rm
        next_v = v - mp * ip + mm * im
        assert u / 2 <= next_u <= Q * u
        assert (16 * K) ** 2 * next_v**2 <= delta**2 * next_u**3
        assert 0 < mp + mm <= 6 * K * K
        for gamma, real, imag in [(gp, rp, ip), (gm, rm, im_signed)]:
            assert K * K <= gamma**2 * u <= 4 * K * K
            assert (gamma - phase).denominator == 1
            # Verify the defining inverse kernel directly in rational complex arithmetic.
            dreal = gamma**2 + beta * (1 - beta)
            dimag = gamma * (1 - 2 * beta)
            assert real * dreal - imag * dimag == 1
            assert real * dimag + imag * dreal == 0
        total_real += mp * rp + mm * rm
        total_imag += mp * ip - mm * im
        assert total_real + next_u == target and total_imag + next_v == 0
        records.append({
            "step": index,
            "u_before": rat(u), "v_before": rat(v),
            "gamma_positive": rat(gp), "gamma_negative": rat(gm),
            "multiplicity_positive": mp, "multiplicity_negative": mm,
            "positive_real_weight_solution": rat(xx),
            "negative_real_weight_solution": rat(yy),
            "positive_solution_interval": [rat(lox), rat(hix)],
            "negative_solution_interval": [rat(loy), rat(hiy)],
            "u_after": rat(next_u), "v_after": rat(next_v),
        })
        u, v = next_u, next_v
    # Independent recomputation from the saved heights and integer multiplicities.
    encoded = json.loads(json.dumps(records))
    sr, si = F(0), F(0)
    for row in encoded:
        for name in ["positive", "negative"]:
            gamma = read_rat(row[f"gamma_{name}"])
            real, imag = canonical(beta, gamma)
            multiplicity = row[f"multiplicity_{name}"]
            sr += multiplicity * real
            si += multiplicity * imag
    assert sr + u == target and si + v == 0
    return {
        "beta": rat(beta), "gamma_residue_mod_one": rat(phase), "target": rat(target),
        "steps": records,
        "final_residual_real": rat(u), "final_residual_imag": rat(v),
        "absolute_remaining_series_bound": rat(2 * u),
        "geometric_real_residual_bound": rat(target * Q**steps),
        "total_integer_multiplicity": sum(r["multiplicity_positive"] + r["multiplicity_negative"] for r in records),
        "final_residual_orientation_only": [float(u), float(v)],
        "saved_sum_plus_residual_is_exact_target": True,
    }


def main() -> None:
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=24)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("exact_alias_packet_certificate.json"))
    args = parser.parse_args()
    if not 1 <= args.steps <= 64:
        raise SystemExit("The exact demonstration allows 1 to 64 steps.")
    inputs = [(F(3, 4), F(1, 3), F(1, 8)), (F(3, 4), F(0), F(1, 10)), (F(17, 32), F(2, 5), F(1, 16))]
    packets = [run_packet(beta, phase, target, args.steps) for beta, phase, target in inputs]
    result = {
        "status": "AUTHOR_EXACT_RATIONAL_CANONICAL_ALIAS_PACKET_NOT_ZETA",
        "author": "EM-DIRECT-E7559A", "activity": "RA-D2F111EA1C0D4B1DBEFBC1B4",
        "sample_base": "exp(2*pi)", "frequency_lattice_spacing": rat(F(1)),
        "proof_also_covers_dyadic_lattice": True,
        "K": K, "contraction_q": rat(Q), "packets": packets,
        "infinite_exactness_basis": "The accompanying cusp-contraction theorem, not finite truncation.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "cases": len(packets), "steps_each": args.steps,
        "all_exact_checks_passed": True,
        "multiplicities": [p["total_integer_multiplicity"] for p in packets],
        "residuals_orientation_only": [p["final_residual_orientation_only"] for p in packets],
        "output": str(args.output),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
