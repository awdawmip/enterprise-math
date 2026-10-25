#!/usr/bin/env python3
"""Exact positive BRC path counts and independent Laurent rational recurrence.
Author-side mathematical evidence; this does not run the P000 native model.
Python 3 stdlib only. Usage: python R283_verify_runner_up.py
"""
from collections import defaultdict
from decimal import Decimal, localcontext
from hashlib import sha256
from json import dumps
from pathlib import Path

MAX_N = 450
GF_CHECK_MAX_N = 150
TRANSITIONS = {
    (0, 0): (2, -1, -1), (0, 1): (2, +1, -1),
    (1, 0): (0, -1, -1), (1, 1): (0, +1, -1),
    (2, 0): (1, +1, +1), (2, 1): (2, +1, -1),
}

def iterate(dp):
    output = defaultdict(int)
    for (q, previous, sign, k), multiplicity in dp.items():
        for bit in (0, 1):
            if previous == 0 and bit == 0:
                continue
            next_q, eta, b = TRANSITIONS[q, bit]
            output[next_q, bit, sign * eta, eta * k + b] += multiplicity
    return output

def laurent_next(coeff, n, numerator):
    """H=1-xS+x^2-x^3S+2x^4+x^6-x^8, S=z+z^-1."""
    out = defaultdict(int)
    def add_shift(source_n, scalar=1, offsets=(0,)):
        if source_n < 0:
            return
        for k, v in coeff[source_n].items():
            for shift in offsets:
                out[k + shift] += scalar * v
    add_shift(n - 1, 1, (-1, 1))
    add_shift(n - 2, -1)
    add_shift(n - 3, 1, (-1, 1))
    add_shift(n - 4, -2)
    add_shift(n - 6, -1)
    add_shift(n - 8, 1)
    for k, v in numerator.get(n, {}).items():
        out[k] += v
    return {k: v for k, v in out.items() if v}

NPLUS = {0: {0: 1}, 1: {-1: -1, 1: -1},
         2: {0: 1}, 3: {1: -1}, 4: {0: 1}}
NMINUS = {4: {-2: 1}, 5: {-1: -1}}

with localcontext() as ctx:
    ctx.prec = 65
    sqrt5 = Decimal(5).sqrt()
    phi = (Decimal(1) + sqrt5) / 2
    variance = Decimal(3) / 2 + Decimal(7) * sqrt5 / 10
    delta_even = (5 * sqrt5 - 11) / 2
    delta_odd = (25 - 11 * sqrt5) / 2
    # pi needed only for diagnostics, not mathematical proof or positivity.
    pi = Decimal('3.14159265358979323846264338327950288419716939937510')
    gap_const_even = delta_even / (10 * variance * (2 * pi * variance).sqrt())
    gap_const_odd = delta_odd / (10 * variance * (2 * pi * variance).sqrt())
    assert delta_even > 0 and delta_odd > 0

    dp = {(0, 2, 1, 0): 1}  # 'previous=2' is only a start sentinel
    plus, minus = [], []
    unique_first_second = []
    fails = []
    nonpositive_pair = {"even": [], "odd": []}
    samples = {}
    coeffs_checked = 0
    counts_checked = 0
    for n in range(MAX_N + 1):
        fibre = defaultdict(int)
        for (q, last, sign, k), val in dp.items():
            if q == 0:
                fibre[(sign, k)] += val
        if n <= GF_CHECK_MAX_N:
            plus.append(laurent_next(plus, n, NPLUS))
            minus.append(laurent_next(minus, n, NMINUS))
            fibre_plus = {k: v for (sign, k), v in fibre.items() if sign == +1}
            fibre_minus = {k: v for (sign, k), v in fibre.items() if sign == -1}
            assert plus[n] == fibre_plus, f'Laurent mismatch + at n={n}'
            assert minus[n] == fibre_minus, f'Laurent mismatch - at n={n}'
            coeffs_checked += len(plus[n]) + len(minus[n])
            counts_checked += 1
        if n >= 12:
            if n % 2:
                xdiff = fibre.get((-1, -3), 0) - fibre.get((+1, -5), 0)
                if xdiff <= 0:
                    nonpositive_pair['odd'].append(n)
            else:
                xdiff = fibre.get((+1, -4), 0) - fibre.get((-1, -4), 0)
                if xdiff <= 0:
                    nonpositive_pair['even'].append(n)
        # Ranking effects, not distinct numerical values.
        ranked = sorted(fibre.items(), key=lambda kv: (-kv[1], kv[0]))
        if len(ranked) >= 4:
            expected = (((-1, -3), (+1, -5), (+1, -3)) if n % 2
                        else ((+1, -4), (-1, -4), (-1, -2)))
            holds = (tuple(effect for effect, count in ranked[:3]) == expected
                     and ranked[0][1] > ranked[1][1] > ranked[2][1] > ranked[3][1])
            if n >= 12 and not holds:
                fails.append(n)
            if n >= 81:
                assert holds, f'top-three pattern fails at n={n}'
                unique_first_second.append(n)
            if n in (40, 79, 80, 81, 82, 100, 101, 150, 151,
                     200, 201, 300, 301, 400, 401, 450):
                gap = ranked[0][1] - ranked[1][1]
                ratio = Decimal(gap) * (Decimal(n) ** Decimal('1.5')) / (phi ** n)
                samples[str(n)] = {
                    'first_effect': [ranked[0][0][0], ranked[0][0][1]],
                    'second_effect': [ranked[1][0][0], ranked[1][0][1]],
                    'third_effect': [ranked[2][0][0], ranked[2][0][1]],
                    'first_count': str(ranked[0][1]),
                    'second_count': str(ranked[1][1]),
                    'gap': str(gap),
                    'gap_over_phi_n_per_n_3over2': str(ratio),
                }
        dp = iterate(dp)
    assert fails and max(fails) == 80
    assert len(unique_first_second) == MAX_N - 80
    report = {
        'schema': 'EM_R283_AUTHOR_EXACT_EVIDENCE_V1',
        'status': 'PASS',
        'mathematical_scope': 'formal positive ordered six-edge BRC auxiliary clean reset, not P000 native dynamics',
        'source_algorithm': 'separate six-edge provenance-preserving DP, independently compared with H Laurent recurrence',
        'max_length_checked': MAX_N,
        'gf_crosscheck_max_length': GF_CHECK_MAX_N,
        'gf_nonzero_effect_coefficients_compared': coeffs_checked,
        'gf_levels_compared': counts_checked,
        'last_failure_in_12_to_450_top_two_pattern': max(fails),
        'verified_top_three_range': [81, MAX_N],
        'verified_top_three_levels': len(unique_first_second),
        'last_nonpositive_pair_even_in_12_to_450': max(nonpositive_pair['even']) if nonpositive_pair['even'] else None,
        'last_nonpositive_pair_odd_in_12_to_450': max(nonpositive_pair['odd']) if nonpositive_pair['odd'] else None,
        'exact_gap_distance_square_even': '(5*sqrt(5)-11)/2',
        'exact_gap_distance_square_odd': '(25-11*sqrt(5))/2',
        'predicted_gap_constant_even_approx': str(gap_const_even),
        'predicted_gap_constant_odd_approx': str(gap_const_odd),
        'samples': samples,
        'limit_of_finite_check': 'no effective proof that threshold 81 suffices for all n',
        'native_software_benchmark': 'NOT_RUN',
        'independent_driver_review': 'NOT_DONE',
    }
    output = Path(__file__).with_name('EXACT_EVIDENCE.json')
    output.write_text(dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f'PASS: DP 0..{MAX_N}; Laurent checks 0..{GF_CHECK_MAX_N}; '
          f'{coeffs_checked} coefficients; 81..{MAX_N} first/second/third unique')
    print('last failed top-three layer:', max(fails))
    print('last nonpositive pair even/odd:', max(nonpositive_pair['even']), max(nonpositive_pair['odd']))
    print('gap constants:', str(gap_const_even), str(gap_const_odd))
    print('evidence path:', output)
