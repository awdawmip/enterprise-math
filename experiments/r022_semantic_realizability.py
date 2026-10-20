#!/usr/bin/env python3
"""R022 fifth-pass finite support-signature normalization experiments."""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product
import json


def join_sets(sets):
    out = frozenset()
    for s in sets:
        out |= frozenset(s)
    return out


def verify_rjc(old_sets, new_sets):
    """Exact explicit-signature RJC verifier."""
    return join_sets(old_sets) == join_sets(new_sets)


def dedup_sets(sets):
    return list(dict.fromkeys(frozenset(s) for s in sets if s))


def brute_min_basis(sets):
    sets = dedup_sets(sets)
    target = join_sets(sets)
    for k in range(len(sets) + 1):
        for ids in combinations(range(len(sets)), k):
            basis = [sets[i] for i in ids]
            if join_sets(basis) == target:
                return basis
    return []


def greedy_uncovered_basis(sets):
    """Set-cover style proposer. Exactness is checked separately by verify_rjc."""
    sets = dedup_sets(sets)
    target = set(join_sets(sets))
    uncovered = set(target)
    out = []
    while uncovered:
        best = max(sets, key=lambda s: len(uncovered & set(s)))
        gain = uncovered & set(best)
        if not gain:
            raise RuntimeError("dictionary does not cover target")
        out.append(best)
        uncovered -= gain
        sets.remove(best)
    return out


def proof_carrying_greedy_witness():
    dictionary = [
        frozenset({1, 2, 3, 4}),
        frozenset({1, 2, 5}),
        frozenset({3, 4, 6}),
        frozenset({5}),
        frozenset({6}),
    ]
    greedy = greedy_uncovered_basis(dictionary)
    optimum = brute_min_basis(dictionary)
    unsafe_cap = greedy[:2]
    return {
        "greedy_width": len(greedy),
        "optimum_width": len(optimum),
        "greedy_exact": verify_rjc(dictionary, greedy),
        "unsafe_cap_exact": verify_rjc(dictionary, unsafe_cap),
        "lesson": "heuristic proposer may be suboptimal while an independent RJC verifier preserves exactness",
    }


def representation_relative_width_witness():
    a, b, c = "a", "b", "c"
    dictionary = [frozenset({a, b}), frozenset({b, c})]
    target = join_sets(dictionary)
    semantic_atoms = [frozenset({x}) for x in sorted(target)]
    free_synthetic = [target]
    return {
        "target_atoms": sorted(target),
        "free_synthetic_width": len(free_synthetic),
        "existing_dictionary_width": len(brute_min_basis(dictionary)),
        "semantic_singleton_width": len(semantic_atoms),
        "all_exact": (
            verify_rjc(dictionary, free_synthetic)
            and verify_rjc(dictionary, brute_min_basis(dictionary))
            and verify_rjc(dictionary, semantic_atoms)
        ),
        "lesson": "branch width is representation-class relative; carrier grammar and cost must be explicit",
    }


def is_laminar(family):
    fam = dedup_sets(family)
    for i, a in enumerate(fam):
        for b in fam[i + 1 :]:
            if not (a <= b or b <= a or a.isdisjoint(b)):
                return False
    return True


def weighted_laminar_basis(tokens):
    """Minimum-cost exact basis for a laminar signature dictionary."""
    best_cost = {}
    for s, cost in tokens:
        s = frozenset(s)
        if not s:
            continue
        if cost < 0:
            raise ValueError("costs must be nonnegative")
        best_cost[s] = min(best_cost.get(s, float("inf")), cost)

    sets = list(best_cost)
    if not is_laminar(sets):
        raise ValueError("signature family is not laminar")

    children = {}
    for s in sets:
        proper = [t for t in sets if t < s]
        children[s] = [t for t in proper if not any(t < u < s for u in proper)]
    roots = [s for s in sets if not any(s < t for t in sets)]

    @lru_cache(None)
    def dp(s):
        kids = children[s]
        own = (best_cost[s], (s,))
        if not kids:
            return own
        if join_sets(kids) != s:
            return own
        sub_cost = sum(dp(k)[0] for k in kids)
        sub_basis = tuple(x for k in kids for x in dp(k)[1])
        return own if own[0] <= sub_cost else (sub_cost, sub_basis)

    total_cost = sum(dp(r)[0] for r in roots)
    basis = tuple(x for r in roots for x in dp(r)[1])
    return total_cost, basis


def brute_min_cost(tokens):
    best_cost = {}
    for s, cost in tokens:
        s = frozenset(s)
        if s:
            best_cost[s] = min(best_cost.get(s, float("inf")), cost)
    sets = list(best_cost)
    target = join_sets(sets)
    best = (float("inf"), ())
    for k in range(len(sets) + 1):
        for ids in combinations(range(len(sets)), k):
            basis = tuple(sets[i] for i in ids)
            if join_sets(basis) != target:
                continue
            cost = sum(best_cost[s] for s in basis)
            if cost < best[0]:
                best = (cost, basis)
    return best


def powerset_nonempty(n):
    return [
        frozenset(i for i in range(n) if (mask >> i) & 1)
        for mask in range(1, 1 << n)
    ]


def verify_weighted_laminar_exhaustive():
    subsets = powerset_nonempty(3)
    family_count = 0
    cost_trials = 0
    for family_mask in range(1, 1 << len(subsets)):
        family = [
            subsets[i] for i in range(len(subsets)) if (family_mask >> i) & 1
        ]
        if not is_laminar(family):
            continue
        family_count += 1
        for costs in product((1, 2, 3), repeat=len(family)):
            tokens = list(zip(family, costs))
            brute_cost, _ = brute_min_cost(tokens)
            dp_cost, _ = weighted_laminar_basis(tokens)
            cost_trials += 1
            if brute_cost != dp_cost:
                return {
                    "families": family_count,
                    "cost_trials": cost_trials,
                    "counterexample": True,
                }
    return {
        "families": family_count,
        "cost_trials": cost_trials,
        "counterexample": False,
    }


def interval_set(interval):
    lo, hi = interval
    return frozenset(range(lo, hi + 1))


def interval_greedy_basis(intervals):
    intervals = list(dict.fromkeys(intervals))
    target = set()
    for iv in intervals:
        target |= set(interval_set(iv))
    uncovered = set(target)
    chosen = []
    while uncovered:
        leftmost = min(uncovered)
        candidates = [iv for iv in intervals if iv[0] <= leftmost <= iv[1]]
        if not candidates:
            raise RuntimeError("uncoverable target")
        best = max(candidates, key=lambda iv: (iv[1], -iv[0]))
        chosen.append(best)
        uncovered -= set(interval_set(best))
    return chosen


def verify_interval_greedy_exhaustive(n=5):
    intervals = [(lo, hi) for lo in range(n) for hi in range(lo, n)]
    tested = 0
    for mask in range(1, 1 << len(intervals)):
        family = [
            intervals[i] for i in range(len(intervals)) if (mask >> i) & 1
        ]
        greedy = interval_greedy_basis(family)
        optimum = brute_min_basis(interval_set(iv) for iv in family)
        tested += 1
        if len(greedy) != len(optimum):
            return {"families": tested, "counterexample": True}
    crossing = [(0, 1), (1, 2)]
    return {
        "families": tested,
        "counterexample": False,
        "crossing_nonlaminar_example": {
            "intervals": crossing,
            "laminar": is_laminar(interval_set(iv) for iv in crossing),
            "greedy_width": len(interval_greedy_basis(crossing)),
        },
    }


def overlap_components(family):
    sets = dedup_sets(family)
    n = len(sets)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if sets[i] & sets[j]:
                adj[i].add(j)
                adj[j].add(i)

    seen = set()
    out = []
    for i in range(n):
        if i in seen:
            continue
        stack = [i]
        seen.add(i)
        comp = []
        while stack:
            x = stack.pop()
            comp.append(sets[x])
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        out.append(comp)
    return out


def min_cover_dp_small_universe(family, n):
    masks = []
    target = 0
    for s in family:
        mask = 0
        for x in s:
            mask |= 1 << x
        masks.append(mask)
        target |= mask
    inf = 10 ** 9
    dp = [inf] * (1 << n)
    dp[0] = 0
    for mask in masks:
        nxt = dp[:]
        for state, value in enumerate(dp):
            if value < inf:
                nxt[state | mask] = min(nxt[state | mask], value + 1)
        dp = nxt
    return dp[target]


def verify_overlap_component_factorization_exhaustive():
    subsets = powerset_nonempty(4)
    tested = 0
    for family_mask in range(1, 1 << len(subsets)):
        family = [
            subsets[i] for i in range(len(subsets)) if (family_mask >> i) & 1
        ]
        direct = min_cover_dp_small_universe(family, 4)
        factorized = sum(
            min_cover_dp_small_universe(comp, 4)
            for comp in overlap_components(family)
        )
        tested += 1
        if direct != factorized:
            return {"families": tested, "counterexample": True}
    return {"families": tested, "counterexample": False}


def run_all():
    return {
        "proof_carrying_normalization": proof_carrying_greedy_witness(),
        "representation_relative_width": representation_relative_width_witness(),
        "weighted_laminar": verify_weighted_laminar_exhaustive(),
        "interval_fast_path": verify_interval_greedy_exhaustive(),
        "overlap_component_factorization": verify_overlap_component_factorization_exhaustive(),
        "semantic_realization_boundary": {
            "explicit_signature_exactness_check": "one materialized join equality",
            "optimal_existing_token_basis": "Set-Cover-hard from R022 pass 3",
            "implicit_signature_warning": (
                "cheap verification claim is scoped to explicit finite signatures; "
                "symbolic/implicit future signatures may require separate proofs"
            ),
        },
    }


def self_test():
    out = run_all()
    p = out["proof_carrying_normalization"]
    assert p["greedy_width"] == 3
    assert p["optimum_width"] == 2
    assert p["greedy_exact"] is True
    assert p["unsafe_cap_exact"] is False

    r = out["representation_relative_width"]
    assert r["free_synthetic_width"] == 1
    assert r["existing_dictionary_width"] == 2
    assert r["semantic_singleton_width"] == 3
    assert r["all_exact"] is True

    w = out["weighted_laminar"]
    assert w["families"] == 63
    assert w["cost_trials"] == 2559
    assert w["counterexample"] is False

    i = out["interval_fast_path"]
    assert i["families"] == 32767
    assert i["counterexample"] is False
    assert i["crossing_nonlaminar_example"]["laminar"] is False

    c = out["overlap_component_factorization"]
    assert c["families"] == 32767
    assert c["counterexample"] is False


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
