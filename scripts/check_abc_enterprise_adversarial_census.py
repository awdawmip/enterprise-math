#!/usr/bin/env python3
"""Exact adversarial census for RS-ABC-ENTERPRISE-ADVERSARIAL-CENSUS.

All theorem / counterexample decisions are integer or rational comparisons.
Floating logarithms are used only to order/display descriptive ranked tables.
"""
from __future__ import annotations

import argparse
import heapq
import json
import math
from fractions import Fraction
from pathlib import Path


def radical_sieve(n: int):
    rad = [1] * (n + 1)
    primes = []
    for p in range(2, n + 1):
        if rad[p] == 1:
            primes.append(p)
            for k in range(p, n + 1, p):
                rad[k] *= p
    return rad, primes


def unique_prime_factors(n: int, primes):
    out = []
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
        if x == 1:
            break
    if x > 1:
        out.append(x)
    return out


def vp(n: int, p: int) -> int:
    e = 0
    while n % p == 0 and n:
        n //= p
        e += 1
    return e


def vp_fact(n: int, p: int) -> int:
    s = 0
    while n:
        n //= p
        s += n
    return s


def vp_binom(n: int, k: int, p: int) -> int:
    return vp_fact(n, p) - vp_fact(k, p) - vp_fact(n - k, p)


def h_p(a: int, b: int, p: int, n: int) -> int:
    c = a + b
    return vp_binom(n * c, n * a, p) - vp(c, p)


def first_activation(a: int, b: int, p: int, limit: int):
    for n in range(1, limit + 1):
        if h_p(a, b, p, n) > 0:
            return n
    return None


def push_top(heap, key, item, keep=24):
    row = (key, item['c'], item['a'], item)
    if len(heap) < keep:
        heapq.heappush(heap, row)
    elif key > heap[0][0]:
        heapq.heapreplace(heap, row)


def exact_row(a: int, b: int, rad):
    c = a + b
    assert 1 <= a <= b and math.gcd(a, b) == 1
    ra, rb, rc = rad[a], rad[b], rad[c]
    rho = ra * rb * rc
    ua, ub, uc = a // ra, b // rb, c // rc
    m = a
    kcap = min(ua, m) * min(ub, m) * min(uc, m)
    tower = ua * ub * uc
    beta_arg = Fraction(c * c, 4 * a * b)

    coeff2_fails = kcap > rho * rho
    strong_boundary = tower * m * m <= kcap * c * c
    parent_boundary = tower * a * a * b * b <= kcap * c**4
    q_gt_1 = c > rho

    rlog = math.log(rho)
    q = math.log(c) / rlog
    h_over_r = math.log(tower) / rlog
    i_over_r = math.log(kcap) / rlog
    beta_over_r = math.log(float(beta_arg)) / rlog
    d_over_r = math.log(tower / kcap) / rlog

    return {
        "a": a,
        "b": b,
        "c": c,
        "rad_a": ra,
        "rad_b": rb,
        "rad_c": rc,
        "rho_rad_abc": rho,
        "tower_quotients": [ua, ub, uc],
        "tower_product": tower,
        "m_min_addend": m,
        "kcap_integer_proxy": kcap,
        "beta_argument": {
            "numerator": beta_arg.numerator,
            "denominator": beta_arg.denominator,
        },
        "exact_flags": {
            "q_gt_1": q_gt_1,
            "coefficient_2_Icap_bound_fails": coeff2_fails,
            "strong_boundary_bound_holds": strong_boundary,
            "parent_boundary_bound_holds": parent_boundary,
        },
        "descriptive_logs": {
            "q": q,
            "beta": math.log(float(beta_arg)),
            "H_over_R": h_over_r,
            "Icap_over_R": i_over_r,
            "beta_over_R": beta_over_r,
            "Dsup_over_R": d_over_r,
        },
    }


def carry_profile(a: int, b: int, primes, window: int):
    c = a + b
    support = sorted(
        set(unique_prime_factors(a, primes))
        | set(unique_prime_factors(b, primes))
        | set(unique_prime_factors(c, primes))
    )
    out = []
    for p in support:
        vals = [h_p(a, b, p, n) for n in range(1, window + 1)]
        tau = next((i + 1 for i, z in enumerate(vals) if z > 0), None)
        out.append(
            {
                "p": p,
                "vp_c": vp(c, p),
                "tau_within_window": tau,
                "energy_sum": sum(vals),
                "max_h": max(vals),
            }
        )
    return out


def carry_family_regression(primes):
    checks = []
    for p in (2, 3, 5, 7, 11):
        for k in range(1, 5):
            P = p**k
            a, b = 1, P - 1
            zeros = all(h_p(a, b, p, n) == 0 for n in range(1, P + 1))
            first = h_p(a, b, p, P + 1)
            checks.append(
                {
                    "p": p,
                    "k": k,
                    "P": P,
                    "all_h_zero_for_1_to_P": zeros,
                    "h_at_P_plus_1": first,
                    "tau_exact": (P + 1) if zeros and first > 0 else None,
                }
            )
            assert zeros and first > 0
    return checks


def run(max_c: int, carry_window: int):
    rad, primes = radical_sieve(max_c)
    heaps = {k: [] for k in ("q", "Icap_over_R", "H_over_R", "interior_stress")}
    counterexamples = []
    primitive_count = 0
    strong_boundary_failures = []
    parent_boundary_failures = []

    for c in range(3, max_c + 1):
        for a in range(1, c // 2 + 1):
            if math.gcd(a, c) != 1:
                continue
            b = c - a
            primitive_count += 1
            row = exact_row(a, b, rad)
            logs = row["descriptive_logs"]
            if row["exact_flags"]["coefficient_2_Icap_bound_fails"]:
                counterexamples.append(row)
            if not row["exact_flags"]["strong_boundary_bound_holds"]:
                strong_boundary_failures.append(row)
            if not row["exact_flags"]["parent_boundary_bound_holds"]:
                parent_boundary_failures.append(row)
            push_top(heaps["q"], logs["q"], row)
            push_top(heaps["Icap_over_R"], logs["Icap_over_R"], row)
            push_top(heaps["H_over_R"], logs["H_over_R"], row)
            push_top(
                heaps["interior_stress"],
                logs["q"] / (1.0 + logs["beta"]),
                row,
            )

    counterexamples.sort(key=lambda r: (r["c"], r["a"]))
    rankings = {}
    for name, hp in heaps.items():
        rankings[name] = [row for _, _, _, row in sorted(hp, reverse=True)[:10]]

    carry_examples = [(32, 49), (1024, 1377), (625, 2048), (1, 80), (1, 2400)]
    carry = []
    for a, b in carry_examples:
        if a + b <= max_c:
            carry.append(
                {
                    "triple": [a, b, a + b],
                    "window": carry_window,
                    "profile": carry_profile(a, b, primes, carry_window),
                }
            )

    family = carry_family_regression(primes)

    assert primitive_count > 0
    assert not strong_boundary_failures
    assert not parent_boundary_failures
    assert counterexamples
    first = counterexamples[0]
    assert (first["a"], first["b"], first["c"]) == (32, 49, 81)
    assert first["kcap_integer_proxy"] == 3024
    assert first["rho_rad_abc"] == 42
    assert first["tower_product"] == 3024

    return {
        "schema": "ABC_ENTERPRISE_ADVERSARIAL_CENSUS_V1",
        "max_c": max_c,
        "primitive_triples_scanned": primitive_count,
        "theorem_decisions_use_exact_integer_or_rational_arithmetic": True,
        "descriptive_log_rankings_are_not_global_proofs": True,
        "definitions": {
            "rho": "rad(a) rad(b) rad(c) = rad(abc)",
            "R": "log(rho)",
            "u_x": "x / rad(x)",
            "H": "log(u_a u_b u_c)",
            "m": "min(a,b)",
            "K_cap": "prod_x min(u_x,m)",
            "I_cap": "log(K_cap)",
            "D_sup": "H-I_cap",
            "beta": "log(c^2/(4ab))",
            "q": "log(c)/R",
            "h_p(n)": "v_p(binomial(nc,na))-v_p(c)",
            "tau_p": "min n>=1 with h_p(n)>0",
        },
        "exact_identities": [
            "R+H = 3 log(c) - beta - log(4)",
            "3(q-1)R = H+beta+log(4)-2R",
            "H = I_cap + D_sup",
        ],
        "global_elementary_boundary_theorem": {
            "strong_form": "D_sup <= 2 log(c/m)",
            "parent_form": "D_sup <= 2 beta + log(16)",
            "finite_regression_failures_strong": len(strong_boundary_failures),
            "finite_regression_failures_parent": len(parent_boundary_failures),
        },
        "coefficient_2_counterexamples": counterexamples,
        "coefficient_2_counterexample_count": len(counterexamples),
        "minimal_counterexample": counterexamples[0],
        "rankings": rankings,
        "carry_profiles": carry,
        "carry_infinite_family_regression": family,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-c", type=int, default=4000)
    ap.add_argument("--carry-window", type=int, default=64)
    ap.add_argument("--output", type=Path)
    ns = ap.parse_args()
    data = run(ns.max_c, ns.carry_window)
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if ns.output:
        ns.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
