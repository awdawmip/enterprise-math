#!/usr/bin/env python3
"""Exact finite checks of the D-probe Newton bound and its sharpness.

Author-only auxiliary Z/p^L six-coordinate observer model; never a native X6 run.
"""
from __future__ import annotations

import collections
import json
from pathlib import Path


def polynomial(x: int, coefficients: tuple[int, ...]) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def falling(x: int, degree: int, step: int) -> int:
    value = 1
    for j in range(degree):
        value *= x - j * step
    return value


def next_prime_above(value: int) -> int:
    n = max(3, value + 1)
    while any(n % t == 0 for t in range(2, int(n**0.5) + 1)):
        n += 1
    return n


def check_sharp_witness(degree: int, s: int) -> dict:
    p = next_prime_above(degree)
    e = 1
    n = s * degree + 1
    L = n + e
    mod_obs = p ** n
    step = p ** s
    a, b = 0, step
    differences = [
        (falling(a + j * step, degree, step)
         - falling(b + j * step, degree, step)) % mod_obs
        for j in range(degree)
    ]
    assert all(v == 0 for v in differences[:-1]), (degree, s, differences)
    assert differences[-1] != 0, (degree, s, differences)
    expected = (-__import__('math').factorial(degree) * p ** (s * degree)) % mod_obs
    assert differences[-1] == expected
    return {"degree": degree, "p": p, "s": s, "e": e,
            "L": L, "observation_modulus": mod_obs,
            "first_distinguishing_probe_j": degree - 1,
            "last_difference_mod": differences[-1]}


def check_general_model(p: int, L: int, e: int, s: int,
                        coefficients: tuple[int, ...]) -> dict:
    assert L > e and s < L
    mod_state = p ** L
    mod_obs = p ** (L - e)
    step = p ** s
    D = len(coefficients) - 1
    assert D >= 1 and coefficients[-1] != 0
    period = p ** (L - s)
    seen: dict[tuple[int, ...], tuple[int, ...]] = {}
    all_futures: dict[tuple[int, ...], int] = collections.Counter()
    for height in range(mod_state):
        short = tuple(polynomial(height + j * step, coefficients) % mod_obs
                      for j in range(D))
        long = tuple(polynomial(height + j * step, coefficients) % mod_obs
                     for j in range(period))
        if short in seen:
            assert seen[short] == long, (p, L, e, s, coefficients, height)
        else:
            seen[short] = long
        all_futures[long] += 1
        # Explicit six-chart source and legal candidate T/U probe semantics.
        q = (1, 2, 3, 4, 0)
        z = tuple((height + q[i]) % mod_state for i in range(5)) + (height,)
        assert tuple((z[i] - z[5]) % mod_state for i in range(5)) == q
        for j in range(D):
            shifted = tuple((coordinate + j * step) % mod_state for coordinate in z)
            updated = list(shifted)
            updated[0] = (updated[0] + p**e * polynomial(shifted[5], coefficients)) % mod_state
            read = tuple((updated[i] - updated[5]) % mod_state for i in range(5))
            assert read[0] == (q[0] + p**e * short[j]) % mod_state
            assert read[1:] == q[1:]
    # Exact BRC multiplicities and conservation.
    spectrum = dict(sorted(collections.Counter(all_futures.values()).items()))
    assert sum(size * count for size, count in spectrum.items()) == mod_state
    assert len(seen) == len(all_futures)
    return {"p": p, "L": L, "e": e, "s": s,
            "degree": D, "coefficients": list(coefficients),
            "source_heights": mod_state, "translation_period": period,
            "future_fiber_count": len(seen),
            "fiber_size_histogram": {str(k): v for k, v in spectrum.items()}}


def main() -> None:
    witnesses = [check_sharp_witness(D, s)
                 for D in range(2, 8) for s in (0, 1, 2)]
    configurations = []
    for p in (3, 5):
        for L, e, s in ((2, 1, 0), (3, 1, 1), (3, 2, 0)):
            for coefficients in ((0, 1), (1, 2, 3), (0, -1, 1),
                                 (2, 0, 1, 1), (0, 2, -1, 0, 1)):
                configurations.append(check_general_model(p, L, e, s, coefficients))
    # The small sharp example: f(x)=x(x-1)(x-2), p=5,L=2,e=1,s=0.
    p, L, e, s = 5, 2, 1, 0
    f = lambda x: x * (x - 1) * (x - 2)
    short_to_long = {}
    long_fibers = collections.Counter()
    for h in range(p**L):
        short = tuple(f(h+j) % p for j in range(2))
        long = tuple(f(h+j) % p for j in range(3))
        short_to_long.setdefault(short, set()).add(long)
        long_fibers[long] += 1
    assert any(len(v) > 1 for v in short_to_long.values())
    assert len(long_fibers) == 5
    assert dict(collections.Counter(long_fibers.values())) == {5: 5}
    assert tuple(f(j) % 5 for j in range(2)) == tuple(f(j+1) % 5 for j in range(2))
    assert f(2) % 5 != f(3) % 5
    out = {
        "status": "PASS",
        "scope": "author-only exact integer auxiliary candidate, not native X6 or independent review",
        "theorem": "D consecutive resettable T_f after U_s^j probes suffice for degree D; D is uniformly sharp",
        "universal_derivation_method": "Newton forward differences with integral binomial coefficients; not inferred from enumeration",
        "sharp_witness_slices": len(witnesses),
        "sharp_witnesses": witnesses,
        "complete_height_translation_model_slices": len(configurations),
        "complete_height_translation_models": configurations,
        "total_labeled_heights_across_configs": sum(x["source_heights"] for x in configurations),
        "total_full_future_evaluations": sum(x["source_heights"]*x["translation_period"] for x in configurations),
        "representative_sharp_BRC": {"p": 5, "L": 2, "e": 1, "s": 0,
                                     "degree": 3, "initial_equal_source_heights": [0, 1],
                                     "two_probe_equal": True,
                                     "third_probe_separates": True,
                                     "complete_future_fibers": {"5": 5},
                                     "labeled_heights": 25}
    }
    path = Path(__file__).with_name('d25_polynomial_translation_finite_probe_author_check_20261030.json')
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('sharp_witnesses','complete_height_translation_models')}, indent=2))

if __name__ == '__main__':
    main()
