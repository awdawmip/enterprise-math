#!/usr/bin/env python3
"""EC49FRV exact native-BRC two-observation discount verifier.

Usage:
  python EC49FRV_JOINT_DISCOUNT_EXACT_CERTIFIER.py <extracted_FRU_bundle_root> [output.json] [anchor_index]
An anchor_index from 0..6 permits bounded individual exact checks.
The bundle is the frozen self-contained EC49FRU evidence from PR #2655.
"""
import sys
import json
from pathlib import Path
from fractions import Fraction
from functools import cache
from collections import Counter

ROOT = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "code"))
from EC49FQI_NATIVE_DATA import V, keys, PIN
from EC49FRQ_INDEPENDENT_ALL228 import PARTS, OBS, subset_keys, ALL

assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(V) == len(OBS) == len(PARTS) == 228 and len(V[0]) == 141
assert ALL == (1 << 141) - 1

native = lambda i: i if i < 144 else 144 + keys.index(subset_keys[i - 144])
assert all(tuple(OBS[i]) == tuple(V[native(i)]) for i in range(228))
original_parts = []
for response_vector in V:
    fibers = {}
    for i, ans in enumerate(response_vector):
        fibers[ans] = fibers.get(ans, 0) | (1 << i)
    original_parts.append(tuple(fibers.values()))
for i in range(228):
    assert sorted(PARTS[i]) == sorted(original_parts[native(i)])

def solve(parts, index_map, s):
    p, q = s.numerator, s.denominator
    names = [index_map(i) for i in range(228)]
    prices = [q - p if n in (32, 34) else q for n in names]
    assert min(prices) > 0

    @cache
    def bell(mask):
        if mask.bit_count() == 1:
            return 0, 0, -1
        best = 10**18
        best_k = -1
        best_q = -1
        n = mask.bit_count()
        for obs, partition in enumerate(parts):
            child_masks = [mask & fiber for fiber in partition if mask & fiber]
            if len(child_masks) < 2:
                continue
            val = n * prices[obs]
            k = n if names[obs] in (32, 34) else 0
            for child in child_masks:
                if child.bit_count() > 1:
                    child_val, child_k, _ = bell(child)
                    val += child_val
                    k += child_k
                if val > best:
                    break
            if val < best or (val == best and k > best_k):
                best, best_k, best_q = val, k, obs
        assert best_q >= 0
        return best, best_k, best_q

    value, k, first = bell(ALL)
    assert (value + p * k) % q == 0
    u = (value + p * k) // q
    return {"value": value, "U": u, "K": k, "root": names[first],
            "reached_subsets": bell.cache_info().currsize}, bell

def extract_tree(mask, bell):
    if mask.bit_count() == 1:
        return {"leaf": mask.bit_length() - 1}
    obs = bell(mask)[2]
    children = {}
    for fiber in original_parts[obs]:
        sub = mask & fiber
        if sub:
            i = (sub & -sub).bit_length() - 1
            children[str(V[obs][i])] = extract_tree(sub, bell)
    assert len(children) > 1
    return {"q": obs, "children": children}

def replay(tree):
    visits = Counter()
    depth_max = 0
    for i in range(141):
        node = tree
        depth = 0
        seen = set()
        while "q" in node:
            q = node["q"]
            assert q not in seen and 0 <= q < 228
            seen.add(q)
            visits[q] += 1
            depth += 1
            node = node["children"][str(V[q][i])]
        assert node["leaf"] == i
        depth_max = max(depth_max, depth)
    return {"U": sum(visits.values()), "K": visits[32] + visits[34],
            "uses_32": visits[32], "uses_34": visits[34],
            "max_depth": depth_max, "root": tree["q"]}

ANCHORS = [
    (0, 1, 296, 152), (1, 4, 297, 156), (1, 3, 304, 177),
    (2, 5, 306, 182), (1, 2, 310, 190), (5, 9, 315, 199),
    (3, 5, 321, 209),
]
indices = [int(sys.argv[3])] if len(sys.argv) >= 4 else range(7)
results = []
for ix in indices:
    p, q, u_expected, k_expected = ANCHORS[ix]
    s = Fraction(p, q)
    a, bell = solve(original_parts, lambda x: x, s)
    b, _ = solve(PARTS, native, s)
    assert a["value"] == b["value"] == q * u_expected - p * k_expected
    assert (a["U"], a["K"]) == (u_expected, k_expected)
    assert (b["U"], b["K"]) == (u_expected, k_expected)
    tree = extract_tree(ALL, bell)
    observed = replay(tree)
    assert (observed["U"], observed["K"]) == (u_expected, k_expected)
    results.append({"s": str(s), "integer_cost": a["value"],
                    "primary": a, "independent_raw_rebuild": b,
                    "141_path_replay": observed, "full_tree": tree})
    print("PASS", str(s), "value", a["value"],
          "U", u_expected, "K", k_expected, flush=True)

# Analytic lifting: on each adjacent anchor interval the left witness
# is exact at both endpoints. Concavity of the all-tree Bellman envelope
# and the witnessed affine upper bound establish continuum equality.
for ix in range(6):
    p0, q0, u0, k0 = ANCHORS[ix]
    p1, q1, u1, k1 = ANCHORS[ix + 1]
    assert Fraction(u0) - Fraction(p1, q1)*k0 == (
        Fraction(u1) - Fraction(p1, q1)*k1
    )
out = {
    "schema": "EC49FRV_NATIVE_JOINT_DISCOUNT_FINITE_CERTIFICATE_V1",
    "frozen_science_pin": PIN, "named_states": 141, "named_observations": 228,
    "model": "lambda=0, x=1, p32=p34=(1-s)t, others=t, 0<=s<=3/5",
    "all_anchor_U_K": [[u, k] for _, _, u, k in ANCHORS],
    "exact_breakpoints": ["1/4", "1/3", "2/5", "1/2", "5/9", "3/5"],
    "results": results,
    "status": "AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED"
}
target = Path(sys.argv[2]) if len(sys.argv) >= 3 else ROOT / "evidence/EC49FRV_CERT.json"
target.parent.mkdir(exist_ok=True, parents=True)
target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print("COMPLETE", target, flush=True)
