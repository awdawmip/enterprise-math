#!/usr/bin/env python3
"""EC49FHF: exact native signed-prefix H9-pair lower bounds, frozen BRC observer.

This is an author-side, finite, exhaustively reproducible calculation. No
inference about canonical theorem admission is made by this script.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
SOURCE = PARENT / "EC49FGW_RADIUS5_EXACT_SCREENS_20261110"
TRIE = PARENT / "EC49FHD_PREFIX_TRIE_RADIUS5_20261110"
sys.path.insert(0, str(SOURCE))
sys.path.insert(0, str(TRIE))
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, pref, raw_key, validate_profile

def solve_group_tree(options, fixed_prefixes):
    """Exact rooted-prefix-tree group-Steiner DP for 1..5 terminal groups."""
    n = len(options)
    assert 1 <= n <= 5
    nodes = {b"": 0}
    parent = [-1]
    ends = [0]
    edges = [b""]
    children = [[]]
    for group, words in enumerate(options):
        assert words
        for word in words:
            v = 0
            for i in range(1, len(word) + 1):
                p = word[:i]
                u = nodes.get(p)
                if u is None:
                    u = len(parent)
                    nodes[p] = u
                    parent.append(v)
                    ends.append(0)
                    edges.append(p)
                    children.append([])
                    children[v].append(u)
                v = u
            ends[v] |= 1 << group
    full = (1 << n) - 1
    INF = 10 ** 6
    dp = [None] * len(parent)
    visited = 0
    for v in range(len(parent) - 1, -1, -1):
        terminal = ends[v]
        if not terminal and not children[v]:
            continue
        cur = [0 if mask & ~terminal == 0 else INF for mask in range(full + 1)]
        for u in children[v]:
            sub = dp[u]
            if sub is None:
                continue
            added = int(edges[u] not in fixed_prefixes)
            if terminal == 0 and cur[0] == 0 and all(
                    cost == INF for cost in cur[1:]):
                cur = [0] + [cost + added if cost < INF else INF
                             for cost in sub[1:]]
                continue
            merged = [INF] * (full + 1)
            for mask in range(full + 1):
                choice = mask
                best = cur[mask]
                while choice:
                    left = cur[mask ^ choice]
                    right = sub[choice]
                    if left < INF and right < INF:
                        best = min(best, left + right + added)
                    choice = (choice - 1) & mask
                merged[mask] = best
            cur = merged
        dp[v] = cur
        visited += 1
    best = dp[0][full]
    assert best < INF
    return best, {"trie_nodes": len(nodes), "computed_nodes": visited}


H9_LABELS = ((9, 16), (9, 32))
catalog = collections.defaultdict(list)
total = 0
for label, word in all_words():
    total += 1
    if label in H9_LABELS:
        catalog[label].append(pref(word)[-1])
assert total == 178850
assert all(len(catalog[x]) == 11440 for x in H9_LABELS)

def calculate(profile):
    rows, paths = validate_profile(profile)
    labels = [(r["window"], r["signature"]) for r in rows]
    assert tuple(labels[22:]) == H9_LABELS
    prefix_support = collections.defaultdict(int)
    key_support = collections.defaultdict(int)
    for i, (row, words) in enumerate(zip(rows, paths)):
        key_support[raw_key(row["word"])] |= (1 << i)
        for prefix in words:
            prefix_support[prefix] |= (1 << i)
    assert len(prefix_support) == 94 and len(key_support) == 7
    grouped = collections.defaultdict(list)
    one_h9 = []
    for Q in itertools.combinations(range(24), 5):
        mask = sum(1 << i for i in Q)
        released = sum((support & mask) == support for support in key_support.values())
        if not released:
            continue
        B = sum((support & mask) == support for support in prefix_support.values()) - 1
        if B <= 15:
            continue
        item = {"Q": list(Q), "B": B, "released_original_keys": released}
        if 22 in Q and 23 in Q:
            fixed = frozenset(
                p for p, support in prefix_support.items()
                if (support & mask) != support
            )
            assert len(fixed) == 93 - B
            grouped[fixed].append(item)
        else:
            one_h9.append(item)
    results = []
    for fixed, cases in grouped.items():
        pair_min, stats = solve_group_tree(
            [catalog[x] for x in H9_LABELS], set(fixed)
        )
        for item in cases:
            item["H9_pair_min_added_prefixes"] = pair_min
            item["excluded_by_H9_pair"] = (pair_min > item["B"])
        results.extend(cases)
    hist = collections.Counter(
        (c["B"], c["H9_pair_min_added_prefixes"], c["excluded_by_H9_pair"])
        for c in results
    )
    excluded = sum(c["excluded_by_H9_pair"] for c in results)
    assert len(grouped) == 25
    assert len(results) == 210
    assert len(one_h9) == 16
    assert excluded == 62
    assert hist[(18, 19, True)] == 60
    assert hist[(21, 22, True)] == 2
    assert hist[(17, 16, False)] == 112
    assert hist[(19, 16, False)] == 20
    assert hist[(20, 19, False)] == 16
    return {
        "profile": profile["profile_id"],
        "high_budget_positions": 226,
        "distinct_H9_pair_backgrounds": len(grouped),
        "both_H9_positions": 210,
        "new_exclusions": excluded,
        "remaining": 226 - excluded,
        "pair_histogram": [
            {"budget": b, "pair_min": m, "excluded": feasible,
             "count": n}
            for (b, m, feasible), n in sorted(hist.items())
        ],
        "cases": sorted(results, key=lambda c: c["Q"]),
        "one_H9_cases": one_h9,
    }

if __name__ == "__main__":
    report = {
        "schema": "EC49FHF_H9_PAIR_EXACT_V1",
        "frozen_scientific_pin": PIN,
        "catalog_words": total,
        "legal_H9_words_per_signature": 11440,
        "scope": "A/B witness radius-five with original key release, B>15; H9/16 and H9/32 included together",
        "profiles": [calculate(profile) for profile in W["profiles"]],
    }
    (HERE / "EXACT_REPORT_EC49FHF.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print("EC49FHF_EXACT_PASS", [
        (p["profile"], p["new_exclusions"], p["remaining"])
        for p in report["profiles"]
    ])
