#!/usr/bin/env python3
"""Exact integer path multiplicities and residue-congruence certificates.

External scalar observer model following PREFIX-788; not a native X6 test.
Uses only the Python standard library. Raises on every failed assertion.
"""
from collections import Counter
from itertools import product
from random import Random
import json


def path_counts(layers):
    """Exact complete-path enumeration for a two-branch layered DAG."""
    return Counter(map(sum, product(*layers)))


def transfer_counts(layers):
    """N[Z] transfer recurrence, left to right; exact source-sum histogram."""
    counts = Counter({0: 1})
    for layer in layers:
        nxt = Counter()
        for current, multiplicity in counts.items():
            for w in layer:
                nxt[current + w] += multiplicity
        counts = nxt
    return counts


def transfer_residues(layers, m):
    """N[Z/m] path transfer; no signed cancellation is permitted."""
    assert m >= 1
    counts = Counter({0: 1})
    for layer in layers:
        nxt = Counter()
        for r, multiplicity in counts.items():
            for w in layer:
                nxt[(r + w) % m] += multiplicity
        counts = nxt
    return counts


def residue_lower_bound(residue_counts, m, target):
    """Minimum circular integer distance to an actually supported residue."""
    return min(min((target - r) % m, (r - target) % m)
               for r, c in residue_counts.items() if c > 0)


def exact_margin(counts, target):
    return min(abs(s - target) for s, c in counts.items() if c > 0)


def test():
    cases = 0
    modular_cases = 0
    assertions = 0
    rng = Random(78920261115)
    ms = (2, 3, 4, 5, 6, 7, 9, 11, 13)
    for _ in range(2048):
        n = rng.randint(1, 7)
        layers = [tuple(rng.randint(-9, 9) for _ in range(2)) for _ in range(n)]
        target = rng.randint(-30, 30)
        direct = path_counts(layers)
        dp = transfer_counts(layers)
        assert direct == dp
        assertions += 1
        margin = exact_margin(dp, target)
        lo = sum(min(layer) for layer in layers)
        hi = sum(max(layer) for layer in layers)
        for m in ms:
            by_residue = Counter()
            for s, c in dp.items():
                by_residue[s % m] += c
            observed = transfer_residues(layers, m)
            assert observed == by_residue
            lb = residue_lower_bound(observed, m, target)
            assert 0 <= lb <= margin
            if observed[target % m] == 0:
                assert margin >= 1
            if m > hi - lo:
                assert len({s % m for s in dp}) == len(dp)
            assertions += 4
            modular_cases += 1
        assert residue_lower_bound(transfer_residues(layers, 6), 6, target) >= max(
            residue_lower_bound(transfer_residues(layers, 2), 2, target),
            residue_lower_bound(transfer_residues(layers, 3), 3, target))
        assertions += 1
        cases += 1

    # Separate existential residues cannot be freely paired by CRT.
    layers = [(0, 5)]
    target = 2
    exact = transfer_counts(layers)
    assert exact == Counter({0: 1, 5: 1})
    assert exact_margin(exact, target) == 2
    assert transfer_residues(layers, 2)[target % 2] == 1
    assert transfer_residues(layers, 3)[target % 3] == 1
    assert transfer_residues(layers, 6)[target % 6] == 0
    assert residue_lower_bound(transfer_residues(layers, 2), 2, target) == 0
    assert residue_lower_bound(transfer_residues(layers, 3), 3, target) == 0
    assert residue_lower_bound(transfer_residues(layers, 6), 6, target) == 2
    assertions += 7

    # PREFIX-788 fixed no-instance, with true margin 1 and hull margin 0.
    layers = [(0, 3), (0, 5)]
    target = 4
    assert transfer_counts(layers) == Counter({0: 1, 3: 1, 5: 1, 8: 1})
    assert exact_margin(transfer_counts(layers), target) == 1
    assert residue_lower_bound(transfer_residues(layers, 3), 3, target) == 1
    assertions += 3
    out = {
        "name": "PREFIX789 path-residue BRC exact integer regression",
        "scope": "2048 seeded two-choice layered DAGs, 9 moduli each; integer weights [-9,9], 1-7 layers, target [-30,30]; deterministic witnesses",
        "seed": 78920261115,
        "random_layered_dags": cases,
        "modular_dp_comparisons": modular_cases,
        "assertions": assertions,
        "crt_mismatch": {"path_sums": [0, 5], "target": 2,
                         "mod_2_target_possible": True, "mod_3_target_possible": True,
                         "mod_6_target_possible": False, "exact_margin": 2,
                         "single_modulus_bounds": {"2": 0, "3": 0, "6": 2}},
        "prefix788_subset_sum": {"weights": [3, 5], "target": 4, "margin": 1},
        "status": "ALL_CHECKS_PASS PREFIX789 PROVENANCE_PRESERVING_MODULAR_TRANSFER"
    }
    print(json.dumps(out, ensure_ascii=False, sort_keys=True, indent=2))
    print(out['status'])
    return out


if __name__ == '__main__':
    test()
