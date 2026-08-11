#!/usr/bin/env python3
"""R022 pass-7 finite distributive join-frontier and macro-basis checks."""
from itertools import combinations
import json


def powerset(xs):
    xs = list(xs)
    for r in range(len(xs) + 1):
        for c in combinations(xs, r):
            yield frozenset(c)


def transitive_closure(n, edges):
    rel = [[False] * n for _ in range(n)]
    for i in range(n):
        rel[i][i] = True
    for i, j in edges:
        rel[i][j] = True
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]:
                        rel[i][j] = True
    return rel


def natural_order_posets(n=4):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    seen = {}
    for mask in range(1 << len(pairs)):
        edges = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
        rel = transitive_closure(n, edges)
        key = tuple(tuple(row) for row in rel)
        seen[key] = rel
    return list(seen.values())


def ideals(rel):
    n = len(rel)
    out = []
    for s in powerset(range(n)):
        ok = True
        for x in s:
            for y in range(n):
                if rel[y][x] and y not in s:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(s)
    return out


def maximal_elements(ideal, rel):
    return frozenset(
        x for x in ideal
        if not any(x != y and y in ideal and rel[x][y] for y in ideal)
    )


def verify_frontier_cover_equivalence(rel, target):
    dictionary = [d for d in ideals(rel) if d and d <= target]
    frontier = maximal_elements(target, rel)
    for idxs in powerset(range(len(dictionary))):
        chosen = [dictionary[i] for i in idxs]
        join = frozenset().union(*chosen) if chosen else frozenset()
        covered = (
            frozenset().union(*(frontier & d for d in chosen))
            if chosen else frozenset()
        )
        if (join == target) != (covered == frontier):
            return False, {
                "frontier": sorted(frontier),
                "chosen": [sorted(x) for x in chosen],
                "join": sorted(join),
                "covered_frontier": sorted(covered),
            }
    return True, None


def exhaustive_distributive_model():
    posets = natural_order_posets(4)
    targets = 0
    for rel in posets:
        for target in ideals(rel):
            if not target:
                continue
            targets += 1
            ok, witness = verify_frontier_cover_equivalence(rel, target)
            if not ok:
                return {
                    "natural_order_posets": len(posets),
                    "target_ideals_checked": targets,
                    "counterexample": True,
                    "witness": witness,
                }
    return {
        "natural_order_posets": len(posets),
        "target_ideals_checked": targets,
        "counterexample": False,
    }


def minimum_existing_basis(signatures):
    signatures = list(dict.fromkeys(signatures))
    target = frozenset().union(*signatures) if signatures else frozenset()
    for k in range(len(signatures) + 1):
        for chosen in combinations(signatures, k):
            if (frozenset().union(*chosen) if chosen else frozenset()) == target:
                return list(chosen)
    return []


def boolean_macro_cover_model():
    dictionary = [
        frozenset({1, 2, 3, 4}),
        frozenset({1, 2, 5}),
        frozenset({3, 4, 6}),
        frozenset({5}),
        frozenset({6}),
    ]
    target = frozenset().union(*dictionary)
    optimum = minimum_existing_basis(dictionary)
    frontier = [frozenset({a}) for a in sorted(target)]
    return {
        "target_atom_count": len(target),
        "canonical_join_frontier_width": len(frontier),
        "existing_dictionary_optimum_width": len(optimum),
        "existing_dictionary_optimum": [sorted(x) for x in optimum],
        "free_target_macro_width_if_admissible": 1,
        "lesson": "semantic frontier is canonical; executable width is macro-dictionary relative",
    }


def m3_nondistributive_kill():
    # M3 has three incomparable atoms a,b,c with pairwise join = top.
    frontier = {"a", "b", "c"}
    chosen = {"a", "b"}
    join_is_top = True
    frontier_covered = frontier <= chosen
    return {
        "lattice": "M3",
        "chosen_atoms": sorted(chosen),
        "join_is_target_top": join_is_top,
        "canonical_frontier_fully_covered": frontier_covered,
        "kill": join_is_top and not frontier_covered,
        "lesson": "frontier-cover equivalence needs join-prime frontier elements; distributivity supplies this",
    }


def explicit_rjc_verifier(before, after):
    old = frozenset().union(*before) if before else frozenset()
    new = frozenset().union(*after) if after else frozenset()
    return old == new


def proof_carrying_model():
    before = [
        frozenset({1, 2, 3, 4}),
        frozenset({1, 2, 5}),
        frozenset({3, 4, 6}),
        frozenset({5}),
        frozenset({6}),
    ]
    exact_suboptimal = [
        frozenset({1, 2, 3, 4}),
        frozenset({5}),
        frozenset({6}),
    ]
    optimum = [
        frozenset({1, 2, 5}),
        frozenset({3, 4, 6}),
    ]
    unsafe = exact_suboptimal[:2]
    return {
        "suboptimal_candidate_verified": explicit_rjc_verifier(before, exact_suboptimal),
        "optimal_candidate_verified": explicit_rjc_verifier(before, optimum),
        "unsafe_truncation_rejected": not explicit_rjc_verifier(before, unsafe),
        "semantic_safety_independent_of_optimality": True,
    }


def run_all():
    return {
        "distributive_join_frontier": exhaustive_distributive_model(),
        "boolean_macro_cover": boolean_macro_cover_model(),
        "nondistributive_kill": m3_nondistributive_kill(),
        "proof_carrying_verifier": proof_carrying_model(),
    }


def self_test():
    out = run_all()
    d = out["distributive_join_frontier"]
    assert d["natural_order_posets"] == 40
    assert d["target_ideals_checked"] == 317
    assert not d["counterexample"]
    b = out["boolean_macro_cover"]
    assert b["canonical_join_frontier_width"] == 6
    assert b["existing_dictionary_optimum_width"] == 2
    assert out["nondistributive_kill"]["kill"]
    p = out["proof_carrying_verifier"]
    assert p["suboptimal_candidate_verified"]
    assert p["optimal_candidate_verified"]
    assert p["unsafe_truncation_rejected"]


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
