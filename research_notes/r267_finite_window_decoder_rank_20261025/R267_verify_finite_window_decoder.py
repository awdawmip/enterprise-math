"""Exact, dependency-free checks for R267 bounded effect decoders.

Finite checks validate implementation inputs; the all-H statements require
the companion analytical Toeplitz-rank and permutation proofs.
"""
import json
from pathlib import Path


def then(g, h, n=None):
    e, k = g
    eta, b = h
    value = eta * k + b
    return eta * e, value if n is None else value % n


def inv(g, n=None):
    e, k = g
    value = -e * k
    return e, value if n is None else value % n


def residue(g, n):
    return g[0], g[1] % n


def perm_translation(g, n):
    e, k = g
    return tuple((e * x + k) % n for x in range(n))


def perm_regular(g, n):
    states = [(e, k) for e in (1, -1) for k in range(n)]
    lookup = {x: i for i, x in enumerate(states)}
    return tuple(lookup[then(x, g, n)] for x in states)


def compose_perms(first, second):
    return tuple(second[first[i]] for i in range(len(first)))


def check_all(max_h=12):
    counters = {
        "translation_zero_coefficients": 0,
        "full_identity_coefficients": 0,
        "translation_toeplitz_identity_entries": 0,
        "full_effect_toeplitz_identity_entries": 0,
        "translation_representation_anti_hom_checks": 0,
        "full_representation_anti_hom_checks": 0,
        "checked_horizons": max_h + 1,
    }
    for h in range(max_h + 1):
        n = h + 1
        effects = [(e, k) for e in (1, -1) for k in range(-h, h + 1)]
        for g in effects:
            assert (perm_translation(g, n)[0] == 0) == (g[1] == 0)
            counters["translation_zero_coefficients"] += 1
            assert (perm_regular(residue(g, n), n)[0] == 0) == (g == (1, 0))
            counters["full_identity_coefficients"] += 1
        for i in range(n):
            for j in range(n):
                assert (perm_translation((1, i-j), n)[0] == 0) == (i == j)
                counters["translation_toeplitz_identity_entries"] += 1
        s = [(e, i) for e in (1, -1) for i in range(n)]
        for i, g in enumerate(s):
            for j, z in enumerate(s):
                w = then(g, inv(z))
                assert abs(w[1]) <= h
                assert (perm_regular(residue(w, n), n)[0] == 0) == (i == j)
                counters["full_effect_toeplitz_identity_entries"] += 1
        if n <= 7:
            finite = [(e, k) for e in (1, -1) for k in range(n)]
            for g in finite:
                for z in finite:
                    target = then(g, z, n)
                    assert perm_translation(target, n) == compose_perms(perm_translation(g, n), perm_translation(z, n))
                    counters["translation_representation_anti_hom_checks"] += 1
                    assert perm_regular(target, n) == compose_perms(perm_regular(g, n), perm_regular(z, n))
                    counters["full_representation_anti_hom_checks"] += 1
    return {
        "claim": "Finite checks agree with exact H+1 and 2(H+1) bounded decoder dimensions; universal theorem requires proof",
        "algorithm": "integer permutation representation of affine group quotient and Toeplitz identity witnesses",
        "arithmetic": "exact Python integers, no floating point",
        "max_h": max_h,
        "counts": counters,
        "status": "PASS",
    }


if __name__ == "__main__":
    result = check_all()
    path = Path(__file__).with_name("EXACT_EVIDENCE.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
