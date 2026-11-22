#!/usr/bin/env python3
"""PREFIX-1004: exact BRC Z2 phase-cover and marked-collision scalarization.
Frozen P000 V5@f42f2906; Stage46 C(h,d)=1/6-[h=d].
All six native X6 coordinates and the last incoming-neighbour port are retained.
The only blocked Link is {anchor, anchor+e1}, without renormalization.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import factorial
import json

D = 6
O = (0,) * D
E1 = (1,) + (0,) * (D - 1)


def shifted(x, i, delta):
    y = list(x)
    y[i] += delta
    return tuple(y)


@lru_cache(None)
def multinomial(m, k):
    if m < 0 or any(v < 0 for v in k) or sum(k) != m:
        return 0
    den = 1
    for v in k:
        den *= factorial(v)
    return factorial(m) // den


def compositions(m, d):
    if d == 1:
        yield (m,)
        return
    for j in range(m + 1):
        for rest in compositions(m - j, d - 1):
            yield (j,) + rest


def endpoints(n):
    return {shifted(v, i, -1) for v in compositions(n - 1, D)
            for i in range(D)}


def phase_cover(n, masked):
    # Positive integral coefficients in N[Z2], with full branch/phase state.
    states = {(O, D, 0, 0): 1}  # chosen anchor, initial -e1 port
    for _ in range(n):
        nxt = defaultdict(int)
        for (x, h, negatives, phase), weight in states.items():
            for d in range(2 * D):
                count = negatives + int(d >= D)
                if count > 1:
                    continue
                if masked and ((x == O and d == 0)
                               or (x == E1 and d == D)):
                    continue
                reversal = h == d
                y = shifted(x, d % D, 1 if d < D else -1)
                nxt[y, (d + D) % (2 * D), count,
                    phase ^ int(reversal)] += weight * (5 if reversal else 1)
        states = nxt
    fibres = defaultdict(int)
    for (x, h, negatives, phase), weight in states.items():
        if negatives == 1:
            fibres[x, h] += (-1 if phase else 1) * weight
    return {key: weight for key, weight in fibres.items() if weight}


def free_numerator(n, x, port):
    # port >= D: the last move was +e_j; port < D: it was -e_r.
    if port < D:
        r = port
        return (multinomial(n - 1, shifted(x, r, 1))
                - 6 * multinomial(n - 2, x))
    j = port - D
    v = shifted(x, j, -1)
    return ((n - 1) * sum(multinomial(n - 2, shifted(v, r, 1))
                          for r in range(D))
            - 36 * (n - 3) * multinomial(n - 3, v)
            - 6 * multinomial(n - 2, shifted(v, 0, 1))
            - 6 * multinomial(n - 2, x))


def masked_numerator(n, x, port):
    v = free_numerator(n, x, port)
    v -= free_numerator(n - 1, shifted(x, 0, -1), port)
    if port >= D:
        y = shifted(shifted(x, 0, -1), port - D, -1)
        v += 25 * multinomial(n - 4, y)
    return v


def exact_masses(n, compare_direct):
    raw_sq = masked_sq = 0
    computed = 0
    raw = phase_cover(n, False) if compare_direct else None
    masked = phase_cover(n, True) if compare_direct else None
    for x in endpoints(n):
        for port in range(2 * D):
            a = free_numerator(n, x, port)
            b = masked_numerator(n, x, port)
            if compare_direct:
                assert a == raw.get((x, port), 0), (n, x, port, 'raw')
                assert b == masked.get((x, port), 0), (n, x, port, 'masked')
            raw_sq += a * a
            masked_sq += b * b
            computed += 1
    return {
        'n': n, 'full_joint_fibres_examined': computed,
        'phase_cover_checked': compare_direct,
        'free_mass': str(Fraction(raw_sq, 36 ** n)),
        'masked_mass': str(Fraction(masked_sq, 36 ** n)),
        'masked_to_free_ratio': str(Fraction(masked_sq, raw_sq)),
        'masked_to_free_ratio_decimal': round(masked_sq / raw_sq, 12),
    }


def main():
    result = {
        'schema': 'PREFIX1004_NATIVE_X6_MARKED_COLLISION_BRC_V1',
        'source_pin': 'p000@f42f2906 / Stage46 candidate / PREFIX-1003@d9c53f6a',
        'native_carrier': 'Z6 affine torsor, signed primitive axes, last incoming-neighbour port',
        'BRC': 'N-weighted Z2 phase cover with terminal joint-fibre signed character',
        'blocked_link': 'undirected {anchor, anchor+e1}, absorption, no renormalization',
        'verification': [exact_masses(n, n <= 9)
                         for n in [5, 6, 7, 8, 9, 10, 12, 14, 16, 20]],
        'asymptotic': {
            'free_first_interior_over_outer': '35/4 (reused PREFIX-998)',
            'masked_first_interior_over_free_first_interior': '7475/11664',
            'masked_first_interior_over_free_outer': '261625/46656',
            'masked_mass_coefficient_over_pi_power_5_over_2': '261625/41472',
            'proof': 'formal Laurent coefficient and five-relative-coordinate Gaussian saddle',
            'independent_review': False,
        },
    }
    assert result['verification'][3]['masked_mass'] == '259181485/78364164096'
    with open('PREFIX1004_R6_EXACT_RESULTS.json', 'w', encoding='utf-8') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(json.dumps({'status': 'PASS',
                      'phase_check_n': [5, 9],
                      'scalar_n': [5, 20],
                      'ratio_at_n20': result['verification'][-1]['masked_to_free_ratio_decimal'],
                      'predicted_ratio': '7475/11664'}))


if __name__ == '__main__':
    main()
