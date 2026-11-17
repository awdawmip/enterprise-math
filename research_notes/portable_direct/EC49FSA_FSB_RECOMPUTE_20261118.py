#!/usr/bin/env python3
"""EC49FSA/FSB exact Bellman verifier: native original class 16943, 228 physical observations.

Usage:
  python EC49FSA_FSB_RECOMPUTE.py /path/to/EC49FRZ2_COMPLETE_BRC_TWO_PRICE_SQUARE

The frozen root must contain source/frozen_original_master.txt,
source/EC49FPG_PROFILE.csv and code/EC49FRQ_INDEPENDENT_ALL228.py
as provided by EC49FRZ2 / PR #2669 and this turn's self-contained archive.
Run from any path. Standard-library Python 3. No network, credentials or hidden services.
"""
from __future__ import annotations
import sys, json, math, time
from pathlib import Path
from fractions import Fraction
from functools import lru_cache

if len(sys.argv) != 2:
    raise SystemExit("Usage: python EC49FSA_FSB_RECOMPUTE.py FROZEN_ARCHIVE_ROOT")
FROZEN = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(FROZEN / "code"))

# This separately reconstructs every original physical observer from the
# SHA256-checked 94-family raw master and profile CSV.
from EC49FRQ_INDEPENDENT_ALL228 import OBS

assert len(OBS) == 228
assert all(len(v) == 141 for v in OBS)
ALL = (1 << 141) - 1
fibers = []
for vec in OBS:
    partition = {}
    for i, response in enumerate(vec):
        partition[response] = partition.get(response, 0) | (1 << i)
    fibers.append(tuple(partition.values()))

def oracle(discounts, want_witness=True):
    """Return exact global Bellman value and a full original-name decision tree."""
    discounts = {int(q): Fraction(z) for q, z in discounts.items()}
    assert all(0 <= q < 228 and 0 <= z <= 1 for q, z in discounts.items())
    denom = math.lcm(*(z.denominator for z in discounts.values())) if discounts else 1
    price = [denom] * 228
    for q, z in discounts.items():
        price[q] = int(denom * (1 - z))

    @lru_cache(None)
    def D(mask):
        if mask.bit_count() == 1:
            return (0, None)
        n = mask.bit_count()
        best, optimal_q = 10**35, None
        for q, blocks in enumerate(fibers):
            children = [mask & block for block in blocks if mask & block]
            if len(children) < 2:
                continue
            candidate = n * price[q]
            for child in children:
                if child.bit_count() > 1:
                    candidate += D(child)[0]
                if candidate >= best:
                    break  # nonnegative prices justify pruning
            if candidate < best:
                best, optimal_q = candidate, q
        assert optimal_q is not None
        return best, optimal_q

    score, root = D(ALL)
    if not want_witness:
        return score, denom, {"root": root, "states": D.cache_info().currsize}

    def build(mask):
        if mask.bit_count() == 1:
            return {"leaf": mask.bit_length() - 1}
        q = D(mask)[1]
        out = {"q": q, "responses": {}}
        for block in fibers[q]:
            child = mask & block
            if child:
                state = (child & -child).bit_length() - 1
                out["responses"][str(OBS[q][state])] = build(child)
        return out

    tree = build(ALL)
    calls = [0] * 228
    max_depth = 0
    for state in range(141):
        node = tree
        seen = set()
        depth = 0
        while "q" in node:
            q = node["q"]
            assert q not in seen, ("repeat", state, q)
            seen.add(q)
            calls[q] += 1
            depth += 1
            node = node["responses"][str(OBS[q][state])]
        assert node["leaf"] == state, ("misidentified", state)
        max_depth = max(max_depth, depth)
    U = sum(calls)
    assert score == denom * U - sum(int(denom * z) * calls[q] for q, z in discounts.items())
    return score, denom, {
        "root": root,
        "states": D.cache_info().currsize,
        "max_depth": max_depth,
        "U": U,
        "N32": calls[32],
        "N34": calls[34],
        "N140": calls[140],
        "tree": tree
    }

theorem_A = [
    ("0", "296"),
    ("1/57", "5615/19"),
    ("1", "157"),
]
theorem_B = [
    ("0", "155"),
    ("1/6", "155"),
    ("1/3", "154"),
    ("1/2", "152"),
    ("2/3", "149"),
    ("4/5", "721/5"),
    ("13/15", "704/5"),
    ("1", "132"),
]
results = []
for slice_id, anchor_table, q32_discount in [
    ("A", theorem_A, Fraction(0)),
    ("B", theorem_B, Fraction(1)),
]:
    for z_text, expected_text in anchor_table:
        z = Fraction(z_text)
        score, denom, audit = oracle({32: q32_discount, 34: Fraction(0), 140: z})
        assert Fraction(score, denom) == Fraction(expected_text), (
            slice_id, z_text, score, denom, expected_text
        )
        result = {
            "slice": slice_id, "z": z_text, "optimal_cost": str(Fraction(score, denom)),
            "root": audit["root"], "states": audit["states"],
            "U": audit["U"], "N32": audit["N32"],
            "N140": audit["N140"], "max_depth": audit["max_depth"],
            "replay_verified": True
        }
        results.append(result)
        print(json.dumps(result, ensure_ascii=False))
print(json.dumps({
    "frozen_pin": "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
    "all_physical_observations": 228,
    "named_profiles": 141,
    "exact_full_Bellman_endpoint_checks": len(results),
    "status": "PASS"
}, ensure_ascii=False))
