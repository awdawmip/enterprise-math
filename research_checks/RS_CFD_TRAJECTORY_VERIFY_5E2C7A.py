#!/usr/bin/env python3
"""Exact finite dependence audit for the frozen 6D3A91 CFD A/B/C benchmark manifest.

This checker does not execute spectralDNS. It verifies that order balance alone does
not justify the frozen triplet-level Binomial(24, 1/2) sign-test calibration when
six triplets inside each of the four cycles may share a latent sign.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, ceil
import json

ORDERS = {"ABC", "BCA", "CAB", "ACB", "CBA", "BAC"}
CYCLES = [
    ["BAC", "ACB", "CAB", "ABC", "CBA", "BCA"],
    ["CBA", "BCA", "ABC", "CAB", "ACB", "BAC"],
    ["CAB", "ABC", "BAC", "ACB", "BCA", "CBA"],
    ["BAC", "CBA", "CAB", "ACB", "BCA", "ABC"],
]
ALPHA_GATE = Fraction(1, 40)  # 0.025

def tail(n: int, k: int) -> Fraction:
    return Fraction(sum(comb(n, i) for i in range(k, n + 1)), 2 ** n)

def verify_balance() -> tuple[dict[str, int], dict[str, int]]:
    assert all(set(c) == ORDERS and len(c) == 6 for c in CYCLES)
    positions = Counter()
    precedence = Counter()
    for cycle in CYCLES:
        for order in cycle:
            for pos, arm in enumerate(order, 1):
                positions[(arm, pos)] += 1
            for a in "ABC":
                for b in "ABC":
                    if a != b and order.index(a) < order.index(b):
                        precedence[(a, b)] += 1
    assert all(positions[(arm, pos)] == 8 for arm in "ABC" for pos in (1,2,3))
    assert all(precedence[(a,b)] == 12 for a in "ABC" for b in "ABC" if a != b)
    return (
        {f"{a}@{p}": positions[(a,p)] for a in "ABC" for p in (1,2,3)},
        {f"{a}>{b}": precedence[(a,b)] for a in "ABC" for b in "ABC" if a != b},
    )

def perfect_cycle_cluster_counterexample() -> dict[str, object]:
    # Four independent fair latent cycle signs; all six triplet signs inside a
    # cycle equal that cycle's latent sign. Each triplet is marginally fair.
    passes18 = 0
    veto17 = 0
    totals = Counter()
    for z in product((0,1), repeat=4):
        positives = 6 * sum(z)
        totals[positives] += 1
        passes18 += positives >= 18
        veto17 += positives >= 17
    assert passes18 == 5
    assert veto17 == 5
    p18 = Fraction(passes18, 16)
    p17 = Fraction(veto17, 16)
    assert p18 == Fraction(5,16)
    assert p17 == Fraction(5,16)
    return {
        "support": {str(k): v for k,v in sorted(totals.items())},
        "p_pass_18_of_24": str(p18),
        "p_veto_17_of_24": str(p17),
        "decimal": float(p18),
    }

def cluster_sensitivity() -> list[dict[str, object]]:
    out = []
    for block_size in (1,2,3,4,6,8,12,24):
        blocks = 24 // block_size
        threshold_blocks = ceil(18 / block_size)
        p = tail(blocks, threshold_blocks)
        out.append({
            "block_size": block_size,
            "independent_blocks": blocks,
            "threshold_blocks": threshold_blocks,
            "exact_tail": str(p),
            "decimal": float(p),
        })
    assert out[4]["exact_tail"] == "5/16"  # six triplets per frozen cycle
    return out

def exact_resolution_floor() -> dict[str, object]:
    # If only the four cycle signs are independent, the smallest nonzero
    # one-sided sign-test p-value is all four positive = 1/16.
    four = Fraction(1,16)
    five = Fraction(1,32)
    six = Fraction(1,64)
    assert four > ALPHA_GATE
    assert five > ALPHA_GATE
    assert six <= ALPHA_GATE
    return {
        "alpha_per_gate": str(ALPHA_GATE),
        "four_cycle_min_p": str(four),
        "five_block_min_p": str(five),
        "six_block_min_p": str(six),
        "minimum_independent_blocks_for_all_positive_p_le_0.025": 6,
    }

def main() -> None:
    positions, precedence = verify_balance()
    nominal18 = tail(24,18)
    nominal17 = tail(24,17)
    assert nominal18 == Fraction(190051, 16777216)
    assert nominal17 == Fraction(536155, 16777216)
    clustered = perfect_cycle_cluster_counterexample()
    resolution = exact_resolution_floor()
    cert = {
        "schema": "CFD_DEPENDENCE_AUDIT_CERTIFICATE_V1",
        "frozen_manifest_commit": "af956e55af72cedb44288bc8a6157da1670705a0",
        "frozen_manifest_blob_sha1": "0e903688ac6ffaba079f88449c3f170f33d2ffbc",
        "position_balance": positions,
        "pairwise_precedence_balance": precedence,
        "nominal_triplet_independent": {
            "p_ge_18_of_24": str(nominal18),
            "p_ge_17_of_24": str(nominal17),
        },
        "perfect_within_cycle_cluster": clustered,
        "cluster_sensitivity": cluster_sensitivity(),
        "resolution_floor": resolution,
        "decision": "FAIL_CLOSED_UNLESS_TRIPLET_LEVEL_SIGN_CALIBRATION_IS_JUSTIFIED",
    }
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("PASS")

if __name__ == "__main__":
    main()
