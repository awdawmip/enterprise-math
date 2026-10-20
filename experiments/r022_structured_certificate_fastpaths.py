#!/usr/bin/env python3
"""R022 fourth-pass structured exact fast paths for residual certificates."""
from itertools import combinations
import json


def is_laminar_sets(sets):
    sets = list(sets)
    for i, a in enumerate(sets):
        for b in sets[i + 1:]:
            if a & b and not (a <= b or b <= a):
                return False
    return True


def minimum_cover_size(sets):
    sets = list(sets)
    target = set().union(*sets) if sets else set()
    for k in range(len(sets) + 1):
        for idxs in combinations(range(len(sets)), k):
            out = set()
            for i in idxs:
                out |= sets[i]
            if out == target:
                return k
    return None


def maximal_signature_basis(family):
    rep_by_sig = {}
    for name in sorted(family):
        sig = frozenset(family[name])
        if sig:
            rep_by_sig.setdefault(sig, name)
    unique = {name: set(sig) for sig, name in rep_by_sig.items()}
    if not is_laminar_sets(unique.values()):
        raise ValueError("family is not laminar")
    maxima = []
    for name, sig in unique.items():
        if not any(sig < other for other_name, other in unique.items() if other_name != name):
            maxima.append(name)
    return tuple(sorted(maxima))


def exhaustive_laminar_theorem(universe_size=4):
    universe = tuple(range(universe_size))
    subsets = [set(c) for r in range(1, universe_size + 1) for c in combinations(universe, r)]
    tested = 0
    failures = []
    for mask in range(1, 1 << len(subsets)):
        family = [subsets[i] for i in range(len(subsets)) if (mask >> i) & 1]
        if not is_laminar_sets(family):
            continue
        tested += 1
        brute = minimum_cover_size(family)
        maxima = sum(not any(s < t for t in family) for s in family)
        if brute != maxima:
            failures.append({"family": [sorted(x) for x in family], "brute": brute, "maxima": maxima})
            break
    return {
        "universe_size": universe_size,
        "laminar_families_tested": tested,
        "failures": failures,
        "theorem_holds_in_exhaustive_model": not failures,
    }


def laminar_examples():
    chain = {"small": {1}, "mid": {1, 2}, "large": {1, 2, 3}}
    forest = {
        "a": {1, 2}, "a1": {1}, "a2": {2},
        "b": {3, 4}, "b1": {3}, "b2": {4},
    }
    return {
        "chain_basis": list(maximal_signature_basis(chain)),
        "chain_width": len(maximal_signature_basis(chain)),
        "forest_basis": list(maximal_signature_basis(forest)),
        "forest_width": len(maximal_signature_basis(forest)),
    }


def certificate_reuse_depth(old_context, new_context):
    depth = 0
    for a, b in zip(old_context, new_context):
        if a != b:
            break
        depth += 1
    return depth


def prefix_certificate_cache_model():
    old_context = (0, 1, 1, 0, 1, 0)
    new_context = (0, 1, 1, 1, 1, 0)
    depth = certificate_reuse_depth(old_context, new_context)
    certificate_depths = (1, 3, 4, 5)
    return {
        "old_context": old_context,
        "new_context": new_context,
        "certificate_reuse_depth": depth,
        "certificate_validity": {str(b): b <= depth for b in certificate_depths},
        "interpretation": "cumulative-prefix certificates through the common footprint remain reusable; deeper certificates are invalidated",
    }


def partition_from_mask(contexts, mask):
    groups = {}
    for c in contexts:
        key = tuple(c[i] for i in mask)
        groups.setdefault(key, set()).add(c)
    return list(groups.values())


def partition_refines(fine, coarse):
    return all(any(cell <= parent for parent in coarse) for cell in fine)


def noncumulative_footprint_kill():
    contexts = [(0, 0), (0, 1), (1, 0), (1, 1)]
    depth1 = partition_from_mask(contexts, (0,))
    depth2 = partition_from_mask(contexts, (1,))
    return {
        "depth1_partition": [sorted(map(list, cell)) for cell in depth1],
        "depth2_partition": [sorted(map(list, cell)) for cell in depth2],
        "depth2_refines_depth1": partition_refines(depth2, depth1),
        "kill": "without cumulative/refining dependency footprints, certificate validity regions do not form a refinement tree",
    }


def run_all():
    return {
        "laminar_exhaustive": exhaustive_laminar_theorem(),
        "laminar_examples": laminar_examples(),
        "prefix_certificate_cache": prefix_certificate_cache_model(),
        "noncumulative_footprint_kill": noncumulative_footprint_kill(),
    }


def self_test():
    out = run_all()
    l = out["laminar_exhaustive"]
    assert l["laminar_families_tested"] == 831
    assert l["theorem_holds_in_exhaustive_model"] and not l["failures"]
    e = out["laminar_examples"]
    assert e["chain_basis"] == ["large"] and e["chain_width"] == 1
    assert e["forest_basis"] == ["a", "b"] and e["forest_width"] == 2
    p = out["prefix_certificate_cache"]
    assert p["certificate_reuse_depth"] == 3
    assert p["certificate_validity"] == {"1": True, "3": True, "4": False, "5": False}
    assert not out["noncumulative_footprint_kill"]["depth2_refines_depth1"]


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
