#!/usr/bin/env python3
"""Exact adversarial census for RS-ABC-ENTERPRISE-ADVERSARIAL-CENSUS.

All acceptance / counterexample decisions use integer cross-products. Floating
logs are emitted only as ranked readouts.
"""
from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import math
from pathlib import Path

LN4 = math.log(4.0)
CAP_KS = (0, 1, 2, 4, 8)


def sieve_spf(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factor_tables(n: int, spf: list[int]):
    factors = [()] * (n + 1)
    rad = [1] * (n + 1)
    rep = [1] * (n + 1)
    lograd = [0.0] * (n + 1)
    logrep = [0.0] * (n + 1)
    logn = [0.0] * (n + 1)
    for x in range(2, n + 1):
        y = x
        rows = []
        r = 1
        h = 1
        while y > 1:
            p = spf[y]
            e = 0
            while y % p == 0:
                y //= p
                e += 1
            rows.append((p, e))
            r *= p
            h *= p ** (e - 1)
        factors[x] = tuple(rows)
        rad[x] = r
        rep[x] = h
        lograd[x] = math.log(r)
        logrep[x] = math.log(h) if h > 1 else 0.0
        logn[x] = math.log(x)
    return factors, rad, rep, lograd, logrep, logn


def vp_fact(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def vp_int(n: int, p: int) -> int:
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def carry_h(a: int, b: int, p: int, n: int) -> int:
    c = a + b
    return (
        vp_fact(n * c, p)
        - vp_fact(n * a, p)
        - vp_fact(n * b, p)
        - vp_int(c, p)
    )


def first_activation(a: int, b: int, p: int, limit: int) -> int | None:
    for n in range(1, limit + 1):
        if carry_h(a, b, p, n) > 0:
            return n
    return None


def push_top(heap, key, tie1, tie2, payload, limit=20):
    row = (key, tie1, tie2, payload)
    if len(heap) < limit:
        heapq.heappush(heap, row)
    elif row[:3] > heap[0][:3]:
        heapq.heapreplace(heap, row)


def primitive_totient_count(cmax: int, spf: list[int]) -> int:
    total = 0
    for c in range(3, cmax + 1):
        x = c
        phi = c
        last = 0
        while x > 1:
            p = spf[x]
            if p != last:
                phi -= phi // p
                last = p
            while x % p == 0:
                x //= p
        total += phi // 2
    return total


def pack_metrics(a, b, c, r, rep_all, icap_product, R, H, I, beta, q):
    return {
        "a": a,
        "b": b,
        "c": c,
        "rad_abc": r,
        "repeated_product": rep_all,
        "icap_product_operational": icap_product,
        "q": q,
        "R": R,
        "H": H,
        "beta": beta,
        "I_cap_operational": I,
        "D_sup_operational": H - I,
        "beta_over_R": beta / R,
        "H_over_R": H / R,
        "I_cap_over_R": I / R,
    }


def prime_list(n: int, spf: list[int]) -> list[int]:
    return [p for p in range(2, n + 1) if spf[p] == p]


def run(cmax: int = 5000, carry_prime_max: int = 997) -> dict:
    spf = sieve_spf(max(cmax, carry_prime_max + 1))
    factors, rad, rep, lograd, logrep, logn = factor_tables(cmax, spf)

    total = 0
    q_gt_1 = 0
    top_q = []
    top_interior = []
    top_icap = []
    min_counterexamples = {}
    boundary_violation = None

    for c in range(3, cmax + 1):
        lc = logn[c]
        for a in range(1, c // 2 + 1):
            b = c - a
            if math.gcd(a, b) != 1:
                continue
            total += 1

            # Primitive a+b=c implies pairwise coprimality, so products concatenate.
            r = rad[a] * rad[b] * rad[c]
            rep_all = rep[a] * rep[b] * rep[c]
            R = lograd[a] + lograd[b] + lograd[c]
            H = logrep[a] + logrep[b] + logrep[c]
            beta = 2.0 * lc - LN4 - logn[a] - logn[b]
            q = lc / R
            if q > 1.0:
                q_gt_1 += 1

            icap_product = 1
            I = 0.0
            all_factors = factors[a] + factors[b] + factors[c]
            for p, e in all_factors:
                tower = p ** (e - 1)
                capped = min(tower, r)
                icap_product *= capped
                I += min((e - 1) * math.log(p), R)

            payload = pack_metrics(
                a, b, c, r, rep_all, icap_product, R, H, I, beta, q
            )
            push_top(top_q, q, -c, -a, payload)
            if beta <= 0.1:
                push_top(top_interior, q, -c, -a, payload)
            push_top(top_icap, I / R, -c, -a, payload)

            # Candidate C_k: I_cap <= 2 R + k beta.
            # Exact multiplicative form:
            # icap * (4ab)^k <= r^2 * c^(2k).
            for k in CAP_KS:
                if k in min_counterexamples:
                    continue
                lhs = icap_product * (4 * a * b) ** k
                rhs = r * r * c ** (2 * k)
                if lhs > rhs:
                    min_counterexamples[k] = {
                        "a": a,
                        "b": b,
                        "c": c,
                        "lhs": str(lhs),
                        "rhs": str(rhs),
                        "ratio_float": lhs / rhs,
                        "rad_abc": r,
                        "repeated_product": rep_all,
                        "icap_product_operational": icap_product,
                    }

            # Parent-shaped boundary payment check under the operational cap:
            # D_sup <= 2 beta + log 16
            # iff (rep/icap) <= c^4/(a^2 b^2).
            if (
                boundary_violation is None
                and rep_all * a * a * b * b > icap_product * c**4
            ):
                boundary_violation = {
                    "a": a,
                    "b": b,
                    "c": c,
                    "left": str(rep_all * a * a * b * b),
                    "right": str(icap_product * c**4),
                }

    expected = primitive_totient_count(cmax, spf)
    if expected != total:
        raise AssertionError((expected, total))

    # Exact infinite-family regression for (1,p-1,p): tau_p = p+1.
    carry_primes = prime_list(carry_prime_max, spf)
    carry_failures = []
    for p in carry_primes:
        # Exact direct replay up through p+1; theorem is proved separately in return.
        for n in range(1, p + 1):
            if carry_h(1, p - 1, p, n) != 0:
                carry_failures.append({"p": p, "n": n, "kind": "early_activation"})
                break
        else:
            if carry_h(1, p - 1, p, p + 1) != 1:
                carry_failures.append(
                    {
                        "p": p,
                        "n": p + 1,
                        "kind": "wrong_first_value",
                        "value": carry_h(1, p - 1, p, p + 1),
                    }
                )

    witness_profiles = []
    for a, b in [(32, 49), (169, 343), (1024, 1377), (625, 2048)]:
        c = a + b
        rows = []
        for p, _e in factors[a] + factors[b] + factors[c]:
            t = first_activation(a, b, p, 4 * p + 500)
            rows.append({"p": p, "tau": t})
        witness_profiles.append({"a": a, "b": b, "c": c, "carry": rows})

    def descending(heap):
        return [row[3] for row in sorted(heap, reverse=True)]

    summary = {
        "schema": "ABC_ENTERPRISE_ADVERSARIAL_CENSUS_V1",
        "task_id": "RS-ABC-ENTERPRISE-ADVERSARIAL-CENSUS",
        "parameters": {
            "c_max": cmax,
            "unordered_convention": "1 <= a <= b, a+b=c, gcd(a,b)=1",
            "carry_family_prime_max": carry_prime_max,
            "candidate_beta_coefficients": list(CAP_KS),
        },
        "operational_definitions": {
            "rad_abc": "rad(a*b*c)",
            "R": "log(rad_abc)",
            "H": "log(a*b*c/rad_abc)",
            "beta": "log(c^2/(4*a*b))",
            "q": "log(c)/R",
            "repeat_tower_p": "(v_p(a*b*c)-1)*log(p)",
            "I_cap": "sum_p min(repeat_tower_p,R)",
            "D_sup": "H-I_cap",
            "carry_h_p_n": "v_p(binomial(n*c,n*a))-v_p(c)",
            "tau_p": "min n>=1 with carry_h_p_n>0",
        },
        "scope_guard": (
            "The taskbook names beta/I_cap/D_sup but does not durably restate their "
            "formulas. beta and the R-cap I_cap/D_sup are frozen here as operational "
            "audit readouts; Driver must map or reject them against the parent source."
        ),
        "exact_identity": "3*log(c)=R+H+beta+log(4)",
        "enumeration": {
            "primitive_unordered_triples": total,
            "totient_formula_crosscheck": expected,
            "q_gt_1_count": q_gt_1,
        },
        "candidate_inequalities": {
            "C_k": "I_cap <= 2*R + k*beta",
            "minimum_counterexamples": {
                str(k): min_counterexamples.get(k) for k in CAP_KS
            },
            "boundary_payment_operational": "D_sup <= 2*beta+log(16)",
            "boundary_payment_first_violation": boundary_violation,
            "boundary_payment_status": (
                "NO_COUNTEREXAMPLE_IN_RANGE"
                if boundary_violation is None
                else "COUNTEREXAMPLE"
            ),
        },
        "carry_exact_family": {
            "family": "(a,b,c)=(1,p-1,p), p prime",
            "theorem": "h_p(n)=0 for 1<=n<=p and h_p(p+1)=1; hence tau_p=p+1",
            "regression_prime_count": len(carry_primes),
            "regression_max_prime": carry_prime_max,
            "regression_failures": carry_failures,
        },
        "top_quality": descending(top_q),
        "top_quality_beta_le_0_1": descending(top_interior),
        "top_I_cap_over_R": descending(top_icap),
        "selected_carry_profiles": witness_profiles,
    }
    canonical = json.dumps(summary, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    summary["canonical_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--c-max", type=int, default=5000)
    parser.add_argument("--carry-prime-max", type=int, default=997)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    if args.c_max < 3:
        raise SystemExit("--c-max must be >=3")
    value = run(args.c_max, args.carry_prime_max)
    text = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
