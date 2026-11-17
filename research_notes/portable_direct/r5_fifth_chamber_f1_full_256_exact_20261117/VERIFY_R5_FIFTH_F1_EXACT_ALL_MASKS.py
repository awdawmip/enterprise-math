#!/usr/bin/env python3
"""Exact fifth-chamber f=1 minimax certificate (R5 frozen scalar observer).
Run: python VERIFY_R5_FIFTH_F1_EXACT_ALL_MASKS.py EXACT_R5_ALL_101_BUDGETS.json
No third-party dependencies or floating-point arithmetic.
"""
import hashlib
import json
import sys
from functools import lru_cache
from pathlib import Path

INPUT_SHA = '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
L = 25845652773852463277015040000
U = 58182461585441404127941754880
FIVE = (18, 24, 82, 34, 17)

def get_table(filename):
    raw = Path(filename).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == INPUT_SHA
    data = json.loads(raw)
    table = {int(k): tuple(map(int, row['counts']))
             for k, row in data['counts_and_cohorts'].items()}
    assert set(table) == set(range(214, 315))
    assert all(len(row) == 256 for row in table.values())
    return table

def answer_families(row, masks, tau):
    values = {}
    for i, h in enumerate(masks):
        v = row[h]
        values[v] = values.get(v, 0) | (1 << i)
    ordered = sorted(values)
    windows = set()
    for v in ordered:
        windows.add(sum((values[w] for w in ordered if v <= w <= v + tau), 0))
    # The sum is a bitwise union because each state has exactly one center.
    return tuple(sorted(a for a in windows
                        if not any(a != b and a & b == a for b in windows)))

def minimax(table, masks, tau):
    all_states = (1 << len(masks)) - 1
    by_family = {}
    for k in range(214, 315):
        family = answer_families(table[k], masks, tau)
        by_family.setdefault(family, k)  # cheapest equivalent query
    actions = sorted(((k, f) for f, k in by_family.items()),
                     key=lambda x: (x[0] not in (216, 223, 296), x[0]))
    complements = {a: all_states ^ a for _, fam in actions for a in fam}

    @lru_cache(None)
    def V(zero, one):
        if (zero | one).bit_count() <= 1:
            return 0
        best = 1 << 40
        for k, family in actions:
            worst = 0
            admissible = True
            for a in family:
                z2 = zero & a
                o2 = (one & a) | (zero & complements[a])
                if z2 == zero and o2 == one:
                    admissible = False  # repeating answer never reduces uncertainty
                    break
                if (z2 | o2).bit_count() > 1:
                    worst = max(worst, V(z2, o2))
                if k + worst >= best:
                    admissible = False
                    break
            if admissible:
                best = min(best, k + worst)
        assert best < (1 << 40)
        return best

    value = V(all_states, 0)
    return {'minimum_cost': value, 'bellman_states': V.cache_info().currsize,
            'distinct_action_families': len(actions),
            'cheapest_query_budgets': sorted(k for k, _ in actions)}

def verify(filename):
    table = get_table(filename)
    lower = minimax(table, FIVE, L)
    upper = minimax(table, tuple(range(256)), U - 1)
    assert lower['minimum_cost'] == upper['minimum_cost'] == 1685
    result = {
        'status': 'PASS_R5_FIFTH_CHAMBER_F1_FULL_256_EXACT_1685',
        'science_pin': PIN,
        'input_sha256': INPUT_SHA,
        'scope': 'all 256 masks; one unmarked arbitrary corrupted reading; integer budgets 214..314',
        'tau_interval_left_inclusive': str(L),
        'tau_interval_right_exclusive': str(U),
        'exact_worst_case_budget': 1685,
        'lower_five_mask_at_L': lower,
        'upper_full_256_at_U_minus_1': upper,
        'monotone_sandwich': 'C_5(L)<=C_256(tau)<=C_256(U-1), for every real L<=tau<U',
        'independent_review': 'NOT_REVIEWED',
    }
    return result

if __name__ == '__main__':
    assert len(sys.argv) == 2
    result = verify(sys.argv[1])
    print(result['status'])
    print(json.dumps(result, indent=2, ensure_ascii=False))
