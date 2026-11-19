#!/usr/bin/env python3
"""Exact BRC query-tree check for identifying local X6 update laws.

Nine available scalar coordinates are (axis j, shell time t), j,t in {0,1,2}.
The decision-tree optimizer even allows noncausal query order; its lower bound
therefore applies to causal experiments. Native event permission is not inferred.
"""

from collections import defaultdict
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
import sys

from check_streaming_state import (
    SOURCE_REVISION, KERNEL_SHA256, LAWS, advance, changes,
    import_kernel, kernel_path, key, relation,
)


def create_leaves(kernel):
    leaves = []
    for law, s, a in product(LAWS, kernel.SIGNS, kernel.TWISTS):
        carrier = kernel.NamedTriadBRC.lift(s)
        r = relation(key(carrier, a))
        if r == (-1, -1, -1):
            continue
        c1, a1 = advance(carrier, a, law)
        c2, a2 = advance(c1, a1, law)
        snapshots = (carrier.read_signs(), c1.read_signs(), c2.read_signs())
        assert c2.sources == carrier.sources and len(c2.history) == 2
        assert all(len(event.joint_branches) == 3 for event in c2.history)
        leaves.append({"law": law, "s": s, "a": a, "r": r,
                       "r_after_one": relation(key(c1, a1)),
                       "query_values": tuple(sign for frame in snapshots for sign in frame),
                       "generator_word": tuple(event.generator for event in c2.history),
                       "source_word": tuple(tuple(branch.source for branch in event.joint_branches)
                                            for event in c2.history)})
    assert len(leaves) == 96
    return leaves


def identify_five(row):
    values = row["query_values"]
    r = [0] * 3
    r[2] = values[0] * values[3]
    r[0] = values[1] * values[4]
    r[1] = -r[0] * r[2]
    axis = 0 if r[2] == 1 else 1
    assert r[(axis - 1) % 3] == 1
    next_relation_bit = values[3 + axis] * values[6 + axis]
    fixed_bit = r[(axis - 2) % 3]
    ingress_bit = r[axis]
    assert fixed_bit != ingress_bit
    law = "persistent" if next_relation_bit == fixed_bit else "ingress"
    return tuple(r), law, (0, 1, 3, 4, 6 + axis)


def identify_six(row):
    values = row["query_values"]
    r = [0] * 3
    r1 = [0] * 3
    r[2], r[0] = values[0] * values[3], values[1] * values[4]
    r1[2], r1[0] = values[3] * values[6], values[4] * values[7]
    r[1], r1[1] = -r[0] * r[2], -r1[0] * r1[2]
    possible = {}
    for law in LAWS:
        d = changes(tuple(r), law)
        image = tuple(d[i] * r[(i - 1) % 3] for i in range(3))
        assert image not in possible
        possible[image] = law
    return tuple(r), possible[tuple(r1)], (0, 1, 3, 4, 6, 7)


def optimum(leaves, family):
    leaves = [row for row in leaves if row["law"] in family]
    all_mask = (1 << len(leaves)) - 1
    plus_masks = tuple(sum(1 << i for i, row in enumerate(leaves)
                           if row["query_values"][coordinate] == 1)
                       for coordinate in range(9))
    target_masks = defaultdict(int)
    for i, row in enumerate(leaves):
        target_masks[(row["r"], row["law"])] |= 1 << i
    target_for_row = [target_masks[(row["r"], row["law"])] for row in leaves]
    chosen = {}

    @lru_cache(None)
    def solve(mask):
        first = (mask & -mask).bit_length() - 1
        if mask & ~target_for_row[first] == 0:
            return 0
        best, best_query = 10, None
        for coordinate, plus_mask in enumerate(plus_masks):
            yes, no = mask & plus_mask, mask & ~plus_mask
            if not yes or not no:
                continue
            depth = 1 + max(solve(yes), solve(no))
            if depth < best:
                best, best_query = depth, coordinate
        chosen[mask] = best_query
        return best

    depth = solve(all_mask)
    assert depth < 10
    # Read out one actual optimal tree and check every original BRC leaf.
    lengths = []
    for index, row in enumerate(leaves):
        mask, length = all_mask, 0
        while solve(mask):
            query = chosen[mask]
            positive = row["query_values"][query] == 1
            mask &= plus_masks[query] if positive else ~plus_masks[query]
            assert mask & (1 << index)
            length += 1
        assert mask & ~target_for_row[index] == 0
        lengths.append(length)
    single_axis = []
    for axis in range(3):
        fibers = defaultdict(set)
        for row in leaves:
            word = tuple(row["query_values"][3 * t + axis] for t in range(3))
            fibers[word].add((row["r"], row["law"]))
        assert min(map(len, fibers.values())) >= 2
        single_axis.append({"axis": axis, "read_words": len(fibers),
                            "target_counts_per_fiber": sorted(set(map(len, fibers.values())))})
    return {"family": list(family), "input_leaves": len(leaves),
            "distinct_targets": len(target_masks),
            "optimal_worst_case_queries": depth,
            "dp_subproblems": solve.cache_info().currsize,
            "maximum_checked_tree_leaf_depth": max(lengths),
            "query_model": "Any adaptive ordering of the nine raw sign coordinates, including noncausal order",
            "one_axis_fibers": single_axis}


def run(kernel):
    leaves = create_leaves(kernel)
    pair = ("persistent", "ingress")
    five_count = six_count = gauge_count = shared_count = 0
    for row in leaves:
        if row["law"] in pair:
            decoded_r, decoded_law, queries = identify_five(row)
            assert (decoded_r, decoded_law) == (row["r"], row["law"])
            assert len(set(queries)) == 5
            five_count += 1
        decoded_r, decoded_law, queries = identify_six(row)
        assert (decoded_r, decoded_law) == (row["r"], row["law"])
        assert len(set(queries)) == 6
        six_count += 1
        # Check the exact covariance used in sequential first-read normalization.
        for epsilon in kernel.SIGNS:
            s = tuple(epsilon[i] * row["s"][i] for i in range(3))
            a = kernel.edge_gauge(row["a"], epsilon)
            c = kernel.NamedTriadBRC.lift(s)
            assert relation(key(c, a)) == row["r"]
            signs = [c.read_signs()]
            for _ in range(2):
                c, a = advance(c, a, row["law"])
                signs.append(c.read_signs())
            transformed = tuple(signs[t][j] for t in range(3) for j in range(3))
            assert transformed == tuple(epsilon[j] * row["query_values"][3 * t + j]
                                        for t in range(3) for j in range(3))
            gauge_count += 1

    for s, a in product(kernel.SIGNS, kernel.TWISTS):
        c = kernel.NamedTriadBRC.lift(s)
        if relation(key(c, a)) != (-1, -1, -1):
            continue
        histories = []
        for law in LAWS:
            current, twist = c, a
            states = []
            for _ in range(7):
                states.append(key(current, twist))
                current, twist = advance(current, twist, law)
            histories.append((states, current.history))
        assert all(history == histories[0] for history in histories)
        shared_count += 1

    pair_result, all_result = optimum(leaves, pair), optimum(leaves, LAWS)
    assert pair_result["optimal_worst_case_queries"] == 5
    assert all_result["optimal_worst_case_queries"] == 6
    return {
        "schema": "X6_LOCAL_LAW_IDENTIFICATION_CHECK_V1", "status": "PASS",
        "source_revision": SOURCE_REVISION,
        "baseline_package_commit": "5806c80973d881009a755e8b5c922dab758a1032",
        "brc_kernel_sha256": KERNEL_SHA256,
        "entrypoint": "check_law_identification.py:run -> NamedTriadBRC.apply",
        "input_carrier": "96 labelled hypotheses: four local laws, 24 sign/twist states with r != (---), fixed three source names and cyclic support",
        "operation_semantics": "Two actual source-preserving III BRC scatterings using the chosen law; exact observation-fiber decision tree on their nine scalar signs",
        "observer_and_future_scope": "Recover (initial r, fixed law) by adaptive queries of three fixed axes at shell times 0,1,2",
        "residual_certificate": "Sharp 5/6 query values; structural gauge-normalization lower bound and exhaustive finite decision-tree optimum agree; shared sector unidentifiable because maps agree",
        "counts": {"five_query_protocol_inputs": five_count, "six_query_protocol_inputs": six_count,
                   "static_gauge_covariance_cases": gauge_count, "shared_sector_complete_histories": shared_count},
        "two_reversible_laws": pair_result, "all_four_laws": all_result,
        "coordinate_order": [[t, j] for t in range(3) for j in range(3)],
        "exact_observation_leaves": leaves,
    }


if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_law_identification.py [BASELINE_PACKAGE_OR_REPO_OR_KERNEL]")
    result = run(import_kernel(kernel_path(sys.argv[1] if len(sys.argv) == 2 else None)))
    destination = Path(__file__).with_name("law_identification_results.json")
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "counts": result["counts"],
                      "two_law_depth": result["two_reversible_laws"]["optimal_worst_case_queries"],
                      "four_law_depth": result["all_four_laws"]["optimal_worst_case_queries"],
                      "dp_states": [result[k]["dp_subproblems"]
                                    for k in ("two_reversible_laws", "all_four_laws")]}, ensure_ascii=False))
