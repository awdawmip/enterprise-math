"""Exact finite cross-check of R284ER's repetition-code torn-write formulas.
Uses the frozen R284CO *tag-storage channel*, not the numerical Port model.
"""
from itertools import combinations
from math import comb
import json


def masks(t, radius):
    return [sum(1 << j for j in J) for k in range(min(t, radius) + 1)
            for J in combinations(range(t), k)]


def weight(x):
    return x.bit_count()


unknown_cases = known_cases = directed_transitions = 0
for t in range(1, 9):
    whole = (1 << t) - 1
    for s in range(3):
        sphere = [x for x in range(1 << t) if weight(x) <= s]
        for b in range(3):
            tears = masks(t, b)
            possible_zero = {x ^ z for x in sphere for z in tears}
            possible_one = {x ^ whole for x in possible_zero}
            assert possible_zero.isdisjoint(possible_one) == (t > 2 * (s + b))
            unknown_cases += 1
            for J in combinations(range(t), min(t, b)):
                jmask = sum(1 << j for j in J)
                local_tears = [z for z in tears if z & ~jmask == 0]
                zero = {x ^ z for x in sphere for z in local_tears}
                one = {x ^ whole for x in zero}
                assert zero.isdisjoint(one) == (t > 2 * s + min(t, b))
                known_cases += 1

for t in range(1, 8):
    for s in range(3):
        for r in range(2):
            for w in range(1 << t):
                if weight(w) > s:
                    continue
                wrong = [j for j in range(t) if w >> j & 1]
                for k in range(len(wrong) + 1):
                    for J in combinations(wrong, k):
                        jmask = sum(1 << j for j in J)
                        for f in masks(t, r):
                            after_external = w ^ f
                            for old_or_new in masks(t, k):
                                if old_or_new & ~jmask:
                                    continue
                                after = (after_external & ~jmask) | old_or_new
                                assert weight(after) <= weight(w) + weight(f)
                                directed_transitions += 1


def bit_count_to_name_set(t, b):
    return (sum(comb(t, j) for j in range(b + 1)) - 1).bit_length()


ledger = []
for s in (0, 1, 2):
    for b in range(1, 9):
        known = 2 * s + b + 1
        unknown = 2 * (s + b) + 1
        address_bits = (comb(known, b) - 1).bit_length()
        ledger.append(dict(background=s, torn_addresses=b,
                           unknown_main_bits=unknown, known_main_bits=known,
                           exact_set_address_bits=address_bits,
                           known_total_bits=known + address_bits,
                           unknown_total_bits=unknown))

certificate = {
    'schema': 'R284ER_EXACT_FINITE_CROSSCHECK_V1',
    'scope': 'binary repetition tag-storage channel only',
    'unknown_torn_cases_checked': unknown_cases,
    'known_address_sets_checked': known_cases,
    'directed_page_transitions_checked': directed_transitions,
    'enumeration_range': {'length_t': [1, 8], 'background_s': [0, 2],
                          'blind_address_bound_b': [0, 2],
                          'directed_length_t': [1, 7], 'directed_external_r': [0, 1]},
    'formulas': {'unknown': 't>=2*(s+b)+1',
                 'known_set': 't>=2*s+b+1',
                 'directed_page': 't>=2*(e+r)+1'},
    'bit_cost_examples': ledger,
    'verified': True,
    'independent_review': False,
}
print(json.dumps(certificate, ensure_ascii=False, indent=2))
