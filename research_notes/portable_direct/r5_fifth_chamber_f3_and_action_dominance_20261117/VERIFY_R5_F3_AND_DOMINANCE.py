#!/usr/bin/env python3
"""Exact R5 f=3 Bellman and 101-to-7 action-dominance certificate.

Usage: python VERIFY_R5_F3_AND_DOMINANCE.py EXACT_R5_ALL_101_BUDGETS.json
The complete 256-state f=3 minimax search can be resource intensive.
"""
import hashlib
import json
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
INPUT_SHA256 = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L = 25845652773852463277015040000
U = 58182461585441404127941754880
BUDGETS = range(214, 315)
FIVE = (18, 24, 82, 34, 17)
UPPER = (214, 215, 216, 223, 296)
SEVEN = (214, 215, 216, 217, 223, 295, 296)


def read_table(path):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == INPUT_SHA256
    data = json.loads(raw)["counts_and_cohorts"]
    rows = {int(k): tuple(map(int, item["counts"])) for k, item in data.items()}
    assert set(rows) == set(BUDGETS)
    assert all(len(row) == 256 for row in rows.values())
    return rows


def response_family(row, masks, tau):
    centers = {}
    for i, h in enumerate(masks):
        c = row[h]
        centers[c] = centers.get(c, 0) | (1 << i)
    candidates = set()
    for lo in centers:
        support = 0
        for c, group in centers.items():
            if lo <= c <= lo + tau:
                support |= group
        candidates.add(support)
    return tuple(sorted(x for x in candidates
                        if not any(x != y and x & y == x for y in candidates)))


def minimax_three(rows, masks, tau, budgets):
    masks = tuple(masks)
    full = (1 << len(masks)) - 1
    families = {}
    for k in budgets:
        families.setdefault(response_family(rows[k], masks, tau), k)
    actions = sorted(((k, family) for family, k in families.items()),
                     key=lambda p: (p[0] not in (216, 223, 296), p[0]))
    not_a = {a: full ^ a for _, fam in actions for a in fam}

    @lru_cache(None)
    def V(zero, one, two, three):
        if (zero | one | two | three).bit_count() <= 1:
            return 0
        best = 1 << 40
        for cost, family in actions:
            worst = 0
            valid = True
            for a in family:
                b = not_a[a]
                z = zero & a
                o = (one & a) | (zero & b)
                t = (two & a) | (one & b)
                h = (three & a) | (two & b)
                if (z, o, t, h) == (zero, one, two, three):
                    valid = False
                    break
                if (z | o | t | h).bit_count() > 1:
                    worst = max(worst, V(z, o, t, h))
                if cost + worst >= best:
                    valid = False
                    break
            if valid:
                best = min(best, cost + worst)
        assert best < (1 << 40)
        return best

    value = V(full, 0, 0, 0)
    return {"value": value, "memo_states": V.cache_info().currsize,
            "representative_actions": [k for k, _ in actions]}


def check_seven_dominance(rows):
    masks = tuple(range(256))
    fam = {k: response_family(rows[k], masks, U - 1) for k in BUDGETS}
    def dominates(j, k):
        return j <= k and all(any((a & b) == a for b in fam[k]) for a in fam[j])
    chosen = {}
    for k in BUDGETS:
        candidates = [j for j in SEVEN if dominates(j, k)]
        assert candidates, ("undominated k", k)
        chosen[k] = candidates[0]
    for j in SEVEN:
        assert chosen[j] == j
        assert not any(dominates(k, j) for k in range(214, j))
    return {"seven_budgets": list(SEVEN), "all_101_covered": True,
            "frequency": dict(sorted(Counter(chosen.values()).items())),
            "all_representatives": chosen}


def verify(path):
    rows = read_table(path)
    lower = minimax_three(rows, FIVE, L, BUDGETS)
    upper = minimax_three(rows, range(256), U - 1, UPPER)
    assert lower["value"] == upper["value"] == 3585, (lower, upper)
    action = check_seven_dominance(rows)
    result = {"status": "PASS_R5_FIFTH_CHAMBER_F3_AND_SEVEN_QUERY_DOMINANCE",
              "source_pin": PIN, "table_sha256": INPUT_SHA256,
              "tau_half_open": [str(L), str(U)], "f": 3,
              "exact_full_256_minimax": 3585, "five_state_lower": lower,
              "full_256_five_query_upper": upper,
              "seven_action_dominance_at_tau_U_minus_1": action,
              "independent_review": "NOT_REVIEWED"}
    return result


if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(json.dumps(verify(sys.argv[1]), indent=2))
