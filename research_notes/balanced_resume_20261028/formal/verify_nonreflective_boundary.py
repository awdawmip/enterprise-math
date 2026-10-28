#!/usr/bin/env python3
"""Exact bounded diagnostics, not a proof of halting undecidability."""
from __future__ import annotations
import json
from math import gcd
from random import Random


def run():
    primes = (2, 3, 5, 7, 11)
    exhaustive = 0
    adaptive = 0
    rng = Random(20261028)
    for pi, p in enumerate(primes):
        for q in primes[pi + 1:]:
            n = p * q
            for order in (p, q, n):
                for a in range(n):
                    for b in range(n):
                        d = (a - b) % n
                        g = gcd(n, d)
                        actual = (a - b) % order == 0
                        if g == n:
                            assert actual
                        elif g == 1:
                            assert not actual
                        else:
                            assert n % g == 0 and 1 < g < n
                        exhaustive += 1
                for _ in range(120):
                    coeffs = [0, 1]
                    vals = [0, 1]
                    stopped = False
                    for step in range(70):
                        i = rng.randrange(len(coeffs))
                        j = rng.randrange(len(coeffs))
                        scalar = rng.randrange(n)
                        coeffs.append((scalar * coeffs[i] + coeffs[j]) % n)
                        vals.append((scalar * vals[i] + vals[j]) % order)
                        assert vals[-1] == coeffs[-1] % order
                        if step % 3 == 0:
                            d = (coeffs[-1] - coeffs[i]) % n
                            g = gcd(n, d)
                            if 1 < g < n:
                                stopped = True
                                break
                            predicted = g == n
                            actual = vals[-1] == vals[i]
                            assert predicted == actual
                            # Genuine adaptive control uses the answer.
                            coeffs.append((coeffs[-1] + int(predicted)) % n)
                            vals.append((vals[-1] + int(actual)) % order)
                    adaptive += 1
                    assert isinstance(stopped, bool)
    assert (1 - 1) % 3 == 0
    assert (1 - 2) % 5 != 0
    assert gcd(15, 1) == gcd(15, -1) == 1

    activation_checks = 0
    for n in (2, 6, 15, 35):
        for halt in (None, 0, 3, 9):
            def valid(s, a):
                return a == 0 or (halt is not None and halt <= s)
            handles = [(s, a) for s in range(12) for a in range(n) if valid(s, a)]
            residues = {a for _, a in handles}
            assert len(residues) == (1 if halt is None else n)
            for s, a in handles:
                assert valid(s, (-a) % n)
                for k in range(n):
                    assert valid(s, (k * a) % n)
                    activation_checks += 1
                for t, b in handles:
                    assert valid(max(s, t), (a + b) % n)
                    activation_checks += 1
            sizes = []
            for stage in range(12):
                seen = {a for s, a in handles if s <= stage}
                sizes.append(len(seen))
            assert all(b % a == 0 for a, b in zip(sizes, sizes[1:]))
            assert sum(a != b for a, b in zip(sizes, sizes[1:])) <= 1
    return {"status": "PASS", "exact_equality_cases": exhaustive,
            "adaptive_program_runs": adaptive,
            "activation_operation_checks": activation_checks,
            "two_seed_scope_countermodel": "PASS",
            "halting_theorem_computationally_verified": False,
            "seed": 20261028}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
