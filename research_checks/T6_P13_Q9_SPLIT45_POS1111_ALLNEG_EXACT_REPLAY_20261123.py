#!/usr/bin/env python3
"""Exact author-level replay for T6 maximal-p13 qorder9 split(4,5).

Canonical positive q-pattern (1,1,1,1) index [start,end) of 1365,
against every named negative q-order5 roster (10,908). The upstream
q9 checker implements the same saturated q0 lattice, rational
Gram-Schmidt recursion and exact mixed 13-adic congruences. The
published check is NOT an independently executed review.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

BASE = Path(__file__).with_name("T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py")
spec = importlib.util.spec_from_file_location("t6_p13_q9_replay", BASE)
assert spec is not None and spec.loader is not None
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)

def partitions(total: int, lower: int = 1):
    if total == 0:
        yield ()
    for q in range(lower, total + 1):
        for tail in partitions(total - q, q):
            yield (q,) + tail

def negative_rosters():
    return sorted(
        tuple(ros)
        for pattern in partitions(5)
        for ros in prior.all_rosters(pattern)
    )

def run(start: int, end: int):
    plus_all = [
        tuple((1, r) for r in rs)
        for rs in itertools.combinations_with_replacement(range(1, 13), 4)
    ]
    minus_all = negative_rosters()
    assert len(plus_all) == 1365 and len(minus_all) == 10908
    assert 48 <= start < end <= 1365
    stats = {"raw_pairs": 0, "common_cancelled": 0, "vertical_overbudget": 0,
             "gs_evaluated": 0, "gs_nodes": 0, "ball_leaves": 0, "budget_valid": 0}
    h_plus, h_pairs = hashlib.sha256(), hashlib.sha256()
    leaves = []
    for idx in range(start, end):
        plus = plus_all[idx]
        h_plus.update((repr(plus) + "\n").encode("ascii"))
        positive_set = set(plus)
        for minus in minus_all:
            stats["raw_pairs"] += 1
            h_pairs.update((str((plus, minus)) + "\n").encode("ascii"))
            if not positive_set.isdisjoint(minus):
                stats["common_cancelled"] += 1
                continue
            skipped, nodes, found = prior.pair_search(plus, minus)
            stats["vertical_overbudget"] += int(skipped)
            if skipped:
                continue
            stats["gs_evaluated"] += 1
            stats["gs_nodes"] += nodes
            stats["ball_leaves"] += len(found)
            for x in found:
                valid = max(x["masses"]) <= prior.CAP
                stats["budget_valid"] += int(valid)
                leaves.append(dict(pos_index=idx, plus=plus, minus=minus,
                                   u=x["u"], masses=x["masses"],
                                   radius_sq=x["radius_sq"], valid=valid))
    assert stats["raw_pairs"] == (end-start)*10908
    assert stats["raw_pairs"] == (stats["common_cancelled"] +
                                  stats["vertical_overbudget"] + stats["gs_evaluated"])
    return dict(schema="EM_T6_P13_Q9_POS1111_SLICE_REPLAY_V1",
                scientific_pin="d84bd940cfb093cdc60e569f15cad58772a51dca",
                positive_index_interval=[start, end],
                negative_roster_count=len(minus_all), stats=stats,
                positive_sha256=h_plus.hexdigest(),
                ordered_pairs_sha256=h_pairs.hexdigest(),
                relaxed_witnesses=leaves,
                strength="AUTHOR_EXACT_FINITE_UNREVIEWED_NOT_ADMITTED")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("start", type=int)
    p.add_argument("end", type=int)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    result = run(a.start, a.end)
    Path(a.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["stats"], sort_keys=True))
