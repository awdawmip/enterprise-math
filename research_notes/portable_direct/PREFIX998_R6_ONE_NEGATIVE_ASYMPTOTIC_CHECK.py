"""PREFIX-998: exact Stage46 BRC first-interior boundary/port amplitude.

Frozen source: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Native typed local rule: C[incoming,outgoing]=(1-6*(incoming==outgoing))/6,
on 12 signed X6 ports. Everything below uses its exact integer numerator.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial, prod
import json

D = 6


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in weak_compositions(total - first, parts - 1):
                yield (first,) + rest


@lru_cache(maxsize=None)
def multinomial(counts):
    return factorial(sum(counts)) // prod(factorial(c) for c in counts)


def closed_amplitudes(n, initial_axis=0):
    """Coherently group every exactly-one-negative n-word by Cell and final port.

    Plus key (k,j) means final step +e_j (incoming-neighbour port -j).
    Minus key (k,r) means final step -e_r (incoming-neighbour port +r).
    Values are integer amplitude numerators; the common denominator is 6**n.
    """
    assert n >= 1 and 0 <= initial_axis < D
    positive = defaultdict(int)
    negative = defaultdict(int)
    m = n - 1
    if m == 0:
        for r in range(D):
            k = tuple(-int(a == r) for a in range(D))
            negative[(k, r)] = 1 - 6 * int(initial_axis == r)
        return dict(positive), dict(negative)

    for h in weak_compositions(m, D):
        n_all = multinomial(h)
        for r in range(D):
            k = tuple(h[a] - int(a == r) for a in range(D))
            for j in range(D):
                if not h[j]:
                    continue
                h_front = list(h)
                h_front[j] -= 1
                n_last = multinomial(tuple(h_front))
                f_left = 1 - 6 * int(initial_axis == r)
                f_end = 1 - 6 * int(j == r)
                if m == 1:
                    contribution = n_last * f_left * f_end
                else:
                    q = m - 1
                    t = q - 6 * h_front[r]
                    z = q + 24 * h_front[r]
                    numerator = n_last * (t*t - z + t*(f_left + f_end))
                    assert numerator % q == 0
                    contribution = numerator // q
                positive[(k, j)] += contribution
            terminal = n_all * (m - 6 * h[r])
            assert terminal % m == 0
            negative[(k, r)] += terminal // m
    return dict(positive), dict(negative)


def direct_brc_amplitudes(n, initial_axis=0):
    """Independent exact 12-port BRC numerator recurrence (up to one negative)."""
    # incoming neighbour labels 0..5 for +axes; 6..11 for -axes.
    zero = (0,)*D
    state = {(zero, D+initial_axis, 0): 1}
    for _ in range(n):
        next_state = defaultdict(int)
        for (k, incoming, negatives), amplitude in state.items():
            for outgoing in range(2*D):
                backward = outgoing >= D
                if backward and negatives:
                    continue
                axis = outgoing % D
                new_k = list(k)
                new_k[axis] += -1 if backward else 1
                new_incoming = axis if backward else D+axis
                c = 1 - 6*int(incoming == outgoing)
                next_state[(tuple(new_k), new_incoming,
                            negatives+int(backward))] += amplitude*c
        state = next_state
    positive = {(k, incoming-D): v for (k, incoming, count), v in state.items()
                if count == 1 and incoming >= D}
    negative = {(k, incoming): v for (k, incoming, count), v in state.items()
                if count == 1 and incoming < D}
    return positive, negative


def outer_collision_sequence(limit):
    previous = [1]*limit
    for _ in range(2,D+1):
        previous = [sum(comb(m,r)**2 * previous[m-r]
                        for r in range(m+1)) for m in range(limit)]
    return previous


def evaluate():
    source_numerators = {1:30,2:1080,3:2700,4:48960,5:1087020,
                         6:24222240,7:561368520,8:13634006400,
                         9:346180688460,10:9140285567520}
    checked = {}
    A = outer_collision_sequence(25)
    for n in range(1,8):
        pos, neg = closed_amplitudes(n)
        pos_direct, neg_direct = direct_brc_amplitudes(n)
        assert pos == pos_direct and neg == neg_direct, f'BRC mismatch at n={n}'
        numerator = sum(v*v for v in pos.values()) + sum(v*v for v in neg.values())
        assert numerator == source_numerators[n], f'PREFIX-997 mismatch at n={n}'
        checked[str(n)] = numerator
    values = {}
    for n in (8, 10, 12, 16, 20, 24):
        pos, neg = closed_amplitudes(n)
        numerator_pos = sum(v*v for v in pos.values())
        numerator_neg = sum(v*v for v in neg.values())
        numerator = numerator_pos + numerator_neg
        if n in source_numerators:
            assert numerator == source_numerators[n], f'PREFIX-997 mismatch at n={n}'
        # M_inner/M_outer: both share the Stage46 common denominator 36**n.
        ratio = Fraction(numerator, 6*A[n-1])
        values[str(n)] = {
            'inner_numerator_over_36_power_n': str(numerator),
            'positive_terminal_numerator': str(numerator_pos),
            'negative_terminal_numerator': str(numerator_neg),
            'outer_numerator_over_36_power_n': str(6*A[n-1]),
            'ratio_to_outer_fraction': f'{ratio.numerator}/{ratio.denominator}',
            'ratio_to_outer_decimal_12_digits': format(float(ratio), '.12f'),
            'positive_fibers': len(pos), 'negative_fibers': len(neg),
        }
    return {
        'record':'PREFIX998_R6_EXACT_RESULTS',
        'frozen_p000':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'stage46_rule':'integer numerator 1-6*same_signed_port over denominator 6',
        'observer':'X6 raw displacement + final signed incoming port; square after coherent sum',
        'independent_dp_lengths':list(range(1,8)),
        'source_prefix997_numerator_crosscheck':checked,
        'exact_values':values,
        'analytical_asymptotic_ratio':'35/4',
        'review':'AUTHOR_PROOF; EXACT_INTEGER_CHECKED; NOT_REVIEWED'
    }


if __name__ == '__main__':
    result = evaluate()
    with open('PREFIX998_R6_EXACT_RESULTS.json', 'w', encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(json.dumps({'status':'PASS','dp_lengths':result['independent_dp_lengths'],
                      'ratios':{k:v['ratio_to_outer_decimal_12_digits']
                                for k,v in result['exact_values'].items()}},
                     ensure_ascii=False))
