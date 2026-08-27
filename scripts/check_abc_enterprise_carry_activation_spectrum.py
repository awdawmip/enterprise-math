#!/usr/bin/env python3
"""Exact regression checker for RS-ABC-ENTERPRISE-CARRY-ACTIVATION-SPECTRUM.

The global theorem is proved in the research return.  This script only replays
integer-valued p-adic identities on deterministic finite cases; it is not used
as a substitute for the proof.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def vp_int(n: int, p: int) -> int:
    e = 0
    while n and n % p == 0:
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
    if not 0 <= k <= n:
        raise ValueError("binomial index out of range")
    return vp_fact(n, p) - vp_fact(k, p) - vp_fact(n - k, p)


def h_p(a: int, b: int, p: int, n: int) -> int:
    """h_p(n)=v_p(binomial(nc,na))-v_p(c), c=a+b."""
    c = a + b
    return vp_binom(n * c, n * a, p) - vp_int(c, p)


def first_activation(a: int, b: int, p: int, limit: int):
    for n in range(1, limit + 1):
        if h_p(a, b, p, n) > 0:
            return n
    return None


def energy(a: int, b: int, p: int, window: int) -> int:
    return sum(h_p(a, b, p, n) for n in range(1, window + 1))


def family_case(p: int, k: int):
    P = p**k
    a, b, c = 1, P - 1, P
    zero_prefix = all(h_p(a, b, p, n) == 0 for n in range(1, P + 1))
    first = h_p(a, b, p, P + 1)
    tau = first_activation(a, b, p, P + 1)
    assert zero_prefix
    assert first == k
    assert tau == P + 1
    assert energy(a, b, p, P) == 0
    return {
        "p": p,
        "k": k,
        "P": P,
        "triple": [a, b, c],
        "all_h_zero_for_1_to_P": zero_prefix,
        "h_at_P_plus_1": first,
        "tau_p": tau,
        "energy_through_P": 0,
    }


def run():
    primes = (2, 3, 5, 7, 11)
    cases = [family_case(p, k) for p in primes for k in range(1, 5)]

    # A few non-family sanity profiles, all evaluated by Legendre valuations.
    probes = []
    for a, b in ((32, 49), (1024, 1377), (625, 2048)):
        c = a + b
        support = []
        x = a * b * c
        p = 2
        while p * p <= x:
            if x % p == 0:
                support.append(p)
                while x % p == 0:
                    x //= p
            p += 1
        if x > 1:
            support.append(x)
        probes.append({
            "triple": [a, b, c],
            "window": 64,
            "channels": [
                {
                    "p": p,
                    "tau_within_64": first_activation(a, b, p, 64),
                    "energy_64": energy(a, b, p, 64),
                    "max_h_64": max(h_p(a, b, p, n) for n in range(1, 65)),
                }
                for p in support
            ],
        })

    return {
        "schema": "ABC_ENTERPRISE_CARRY_ACTIVATION_SPECTRUM_CHECK_V1",
        "decisions_are_exact_integer_valuations": True,
        "theorem": "for (a,b,c)=(1,p^k-1,p^k), tau_p=p^k+1 and h_p(p^k+1)=k",
        "controlled_window_consequence": "E_p(W)=0 for every W<=p^k",
        "family_regression_cases": cases,
        "family_regression_count": len(cases),
        "sanity_profiles": probes,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ns = ap.parse_args()
    data = run()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if ns.output:
        ns.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
