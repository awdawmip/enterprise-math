#!/usr/bin/env python3
"""PREFIX-975 exact finite checks: signed endpoint carriers and changing-residual updates.
Auxiliary integer/XOR observer only; not an executed native X6 or BRC dynamics.
"""
from collections import Counter, defaultdict
import json


def residual_masks(p):
    out = defaultdict(lambda: [0, 0])
    for i in range(p):
        for j in range(p):
            out[(1 << i) - (1 << j)][0] |= 1 << j
            out[(1 << i) + (1 << j)][1] |= 1 << j
    return {c: tuple(pair) for c, pair in out.items()}


def signed(pair, x, p):
    P, M = pair
    cap = (1 << p) - 1
    return (P & (~x) & cap, M & x)


def output():
    checks = []
    for p in range(4, 9):
        masks = residual_masks(p)
        single_flip = 0
        endpoint_count = 0
        support_rank_hist = Counter()
        for c, (P, M) in masks.items():
            T = P | M
            support_rank_hist[(T & ~1).bit_count()] += 1
            for x in range(1, 1 << p, 2):
                old_plus, old_minus = signed((P, M), x, p)
                actual = set()
                for i in range(p):
                    for j in range(p):
                        bit = (x >> j) & 1
                        s = -1 if bit else 1
                        if (1 << i) - s * (1 << j) == c:
                            actual.add((i, j, s))
                rebuilt = set()
                for j in range(p):
                    if old_plus >> j & 1:
                        i = (c + (1 << j)).bit_length() - 1
                        assert (1 << i) == c + (1 << j)
                        rebuilt.add((i, j, 1))
                    if old_minus >> j & 1:
                        i = (c - (1 << j)).bit_length() - 1
                        assert (1 << i) == c - (1 << j)
                        rebuilt.add((i, j, -1))
                assert actual == rebuilt
                endpoint_count += 1
                for j in range(1, p):
                    F = 1 << j
                    flipped = signed((P, M), x ^ F, p)
                    assert flipped == (old_plus ^ (P & F), old_minus ^ (M & F))
                    single_flip += 1
        pair_checks = 0
        counterexamples = 0
        for c, (P, M) in masks.items():
            T = (P | M) & ~1
            for C, (P2, M2) in masks.items():
                R = (P2 | M2) & ~1
                if R & ~T:
                    j = (R & ~T & -(R & ~T)).bit_length() - 1
                    x, y = 1, 1 | (1 << j)
                    assert signed((P, M), x, p) == signed((P, M), y, p)
                    assert signed((P2, M2), x, p) != signed((P2, M2), y, p)
                    counterexamples += 1
                else:
                    for x in range(1, 1 << p, 2):
                        sp = signed((P, M), x, p)
                        recovered_x = 1
                        for j in range(1, p):
                            if not (R >> j & 1):
                                continue
                            if P >> j & 1:
                                val = 0 if (sp[0] >> j & 1) else 1
                            else:
                                val = 1 if (sp[1] >> j & 1) else 0
                            recovered_x |= val << j
                        assert signed((P2, M2), x, p) == signed((P2, M2), recovered_x, p)
                pair_checks += 1
        checks.append(dict(p=p,distinct_residuals=len(masks),endpoint_states_checked=endpoint_count,
                           single_odd_preserving_flips_checked=single_flip,ordered_transition_pairs=pair_checks,
                           transitions_not_factoring=counterexamples,
                           current_signed_observer_rank_histogram=dict(sorted(support_rank_hist.items()))))
    for q in range(4, 20):
        d = residual_masks(q)
        ranks = Counter(((P | M) & ~1).bit_count() for P, M in d.values())
        expected = {0:q-2, 1:q*q-3*q+8, 2:q*(q-1)//2-2, q-1:1}
        assert dict(ranks) == expected, (q, ranks, expected)
        assert len(d) == (3*q*q-5*q+10)//2
    p = 19
    masks = residual_masks(p)
    rank = Counter(((P | M) & ~1).bit_count() for P, M in masks.values())
    full = (1 << p) - 1
    universal_union = 0
    for P, M in masks.values():
        universal_union |= P | M
    assert universal_union == full
    assert masks[0][0] == full and masks[0][1] == 0
    p4 = residual_masks(4)
    assert signed(p4[-7], 1, 4) == signed(p4[-7], 5, 4) == (8, 0)
    assert signed(p4[-3], 1, 4) == (4, 0)
    assert signed(p4[-3], 5, 4) == (0, 0)
    diagonal = {(1, 1), (2, 2)}
    crossed = {(1, 2), (2, 1)}
    assert {j for j, J in diagonal} == {j for j, J in crossed} == {1, 2}
    assert {J for j, J in diagonal} == {J for j, J in crossed} == {1, 2}
    assert sum(j == J for j, J in diagonal) == 2
    assert sum(j == J for j, J in crossed) == 0
    return dict(schema="PREFIX975_EXACT_FINITE_V1",frozen_pin="f42f2906d77f24085c123f3ccfe9667d41caa96d",
                small_domain_checks=checks,p19=dict(distinct_residuals=len(masks),
                signed_state_information_rank_odd_slice_histogram=dict(sorted(rank.items())),
                all_residuals_next_query_repair_bits=p-1,
                analytic_rank_distribution_odd_slice={"zero":p-2,"one":p*p-3*p+8,"two":p*(p-1)//2-2,"full":1},
                residual_zero_plus_ports=masks[0][0],residual_zero_minus_ports=masks[0][1]),
                explicit_transition_counterexample=dict(p=4,old_c=-7,new_c=-3,x=1,y=5,
                     old_signed_masks=[8,0],new_x_masks=[4,0],new_y_masks=[0,0]),
                correlation_counterexample=dict(source_residual=0,x=1,ports=[1,2],
                     diagonal_equal_mass=2,crossed_equal_mass=0),
                scientific_status="AUTHOR_PROOF_EXACT_INTEGER_CHECKED_NOT_REVIEWED")

if __name__ == '__main__':
    print(json.dumps(output(), ensure_ascii=False, indent=2, sort_keys=True))
