#!/usr/bin/env python3
"""Exact k=6, s=2, J={0} source-labelled dynamic and inert-controller certificate.
Standard library only; integer bitsets and exhaustive branch-and-bound cover search.
Frozen source pin 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
from functools import reduce
import json

K, S, J = 6, 2, 1
RAW = 1 << K
CENTERS = [23, 29, 43, 46, 47, 53, 58, 59, 62, 63]
TRANS = [(0, 0), (1, 1), (2, 2), (3, 4), (3, 4),
         (5, 5), (6, 7), (6, 7), (8, 9), (8, 9)]
INERT_CENTERS = [23, 27, 31, 39, 43, 45, 47, 51, 53, 55, 59, 61, 63]


def q(x):
    return sum((x >> i & 1) * (x >> ((i + 1) % K) & 1)
               for i in range(K))


def delta(r, u):
    d = r & ~u
    e = r | (J & ~d)
    return q(e) - q(e & ~d)


def candidates(r):
    return [u for u in range(RAW) if u & ~r == 0 and delta(r, u) <= S]


def static_cover(r):
    return sum(1 << u for u in range(RAW)
               if u & ~r == 0 and q(r) - q(u) <= S)


def inert_cover(r):
    result = 0
    for t in range(RAW // 2):
        lo = 2 * t
        hi = lo + 1
        if lo & ~r == 0 and hi & ~r == 0 \
           and q(r) - q(lo) <= S and q(r) - q(hi) <= S:
            result |= 1 << t
    return result


def exact_no_cover(covers, domain_bits, budget):
    """Exact: every <=budget cover is ruled out by an exhaustive recurrence."""
    # Strictly dominated centres are dispensable for minimum set cover.
    surviving = [v for v in covers if not any(
        covers[v] != covers[w] and covers[v] & covers[w] == covers[v]
        for w in covers)]
    options = [[v for v in surviving if covers[v] >> u & 1]
               for u in range(domain_bits)]
    full = (1 << domain_bits) - 1
    visited = set()
    nodes = 0

    def search(uncovered, slots):
        nonlocal nodes
        nodes += 1
        if uncovered == 0:
            return ()
        if slots == 0:
            return None
        maximum = max((covers[v] & uncovered).bit_count() for v in surviving)
        if uncovered.bit_count() > slots * maximum:
            return None
        state = (uncovered, slots)
        if state in visited:
            return None
        # Every covering selection must choose some centre covering this u.
        u = min((u for u in range(domain_bits) if uncovered >> u & 1),
                key=lambda u: len(options[u]))
        order = sorted(options[u], key=lambda v: (covers[v] & uncovered).bit_count(),
                       reverse=True)
        for v in order:
            result = search(uncovered & ~covers[v], slots - 1)
            if result is not None:
                return (v,) + result
        visited.add(state)
        return None

    found = search(full, budget)
    assert found is None, found
    return {"budget_ruled_out": budget, "dominance_reduced_centres": len(surviving),
            "recursion_nodes": nodes, "failed_states_memoized": len(visited)}


def main():
    states = [candidates(r) for r in CENTERS]
    assert all(states)
    assert set().union(*map(set, states)) == set(range(RAW))
    cert = []
    for i, (r, members) in enumerate(zip(CENTERS, states)):
        assert all(u & ~r == 0 and q(r) - q(u) <= S for u in members)
        assert all(delta(r, u) <= S for u in members)
        destinations = []
        for b in (0, 1):
            images = {(u & ~1) | b for u in members}
            choices = [j for j, B in enumerate(states) if images <= set(B)]
            assert choices, (r, b)
            destinations.append(choices[0])
        assert tuple(destinations) == TRANS[i], (i, destinations)
        cert.append({"state": i, "source_center": r, "source_cost": 5 * K + q(r),
                     "belief_masks": members, "max_current_slack": max(q(r)-q(u) for u in members),
                     "Set0": destinations[0], "Set1": destinations[1]})

    source_lower = exact_no_cover({r: static_cover(r) for r in range(RAW)}, RAW, 9)
    source_upper = 0
    for r in CENTERS:
        source_upper |= static_cover(r)
    assert source_upper == (1 << RAW) - 1

    inert_lower = exact_no_cover({r: inert_cover(r) for r in range(1, RAW, 2)},
                                 RAW // 2, 12)
    inert_upper = 0
    for r in INERT_CENTERS:
        inert_upper |= inert_cover(r)
    assert inert_upper == (1 << (RAW // 2)) - 1

    result = {"status": "PASS_R5_K6_SINGLE_CONTROL_EXACT_10_VS_INERT_13",
              "frozen_science_pin": "435e77af0d180eac32bd1f9c4c464bc4010b7551",
              "model": {"k": K, "slack": S, "named_commands": ["Set_0(0)", "Set_0(1)"],
                        "source_cost": "5k+q(u)"},
              "exact": {"static_minimum": 10, "dynamic_minimum": 10,
                        "self_loop_minimum": 13,
                        "static_lower_certificate": source_lower,
                        "self_loop_lower_certificate": inert_lower},
              "source_centers": CENTERS, "states": cert,
              "self_loop_source_centers": INERT_CENTERS,
              "proof_status": "FINITE_EXHAUSTIVE_CERTIFICATE_AND_EXPLICIT_CONSTRUCTION",
              "independent_review": "NOT_REVIEWED"}
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
