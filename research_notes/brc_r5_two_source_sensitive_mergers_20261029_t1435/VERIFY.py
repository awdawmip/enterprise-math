#!/usr/bin/env python3
"""All-Fraction certificate for two source-sensitive serial LR mergers."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

S = (F(1, 2), F(1), F(3, 2))
THETA = F(27, 496)


def kernel(origin, t):
    p = (F(1, 4) if origin == 'A' else F(1, 8)) if t == 1 else (
        F(1, 4) if t == 2 else F(1, 4) + (F(1, 256) if origin == 'A' else -F(1, 256)))
    return (p, 1 - 2 * p, p)


def stop(t, r):
    return min(r, F(1)) + t * THETA * (r + 1)


@lru_cache(None)
def full(origin, t, r):
    return stop(t, r) if t == 4 else min(stop(t, r), cont(origin, t, r))


def cont(origin, t, r):
    return sum((q * full(origin, t + 1, r * s)
                for s, q in zip(S, kernel(origin, t))), F(0))


@lru_cache(None)
def observer(origin, t, r):
    action = ('P' if origin == 'B' else 'C') if t == 1 else (
        'C' if t < 4 and r == 1 else ('P' if r >= 1 else 'Q'))
    if action == 'P':
        return (F(0), F(1), t * r, F(t))
    if action == 'Q':
        return (r, F(0), t * r, F(t))
    vectors = [observer(origin, t + 1, r * s) for s in S]
    return tuple(sum((q * v[j] for q, v in zip(kernel(origin, t), vectors)), F(0))
                 for j in range(4))


def lr_brute_force():
    keys = sorted({(1, F(1))} | {(2, s) for s in S} |
                  {(3, s * u) for s, u in product(S, repeat=2)})
    assert len(keys) == 10
    lowest, ties = None, 0
    for bits in product((0, 1), repeat=len(keys)):
        decisions = dict(zip(keys, bits))

        @lru_cache(None)
        def v(origin, t, r):
            if t == 4 or not decisions[(t, r)]:
                return stop(t, r)
            return sum((q * v(origin, t + 1, r * s)
                        for s, q in zip(S, kernel(origin, t))), F(0))

        score = (v('A', 1, F(1)) + v('B', 1, F(1))) / 2
        if lowest is None or score < lowest:
            lowest, ties = score, 1
        elif score == lowest:
            ties += 1
    return lowest, ties


def main():
    for origin in 'AB':
        for t in (1, 2, 3):
            q = kernel(origin, t)
            assert all(x > 0 for x in q) and sum(q, F(0)) == 1
            assert sum((s * x for s, x in zip(S, q)), F(0)) == 1
    assert kernel('A', 1) != kernel('B', 1)
    assert kernel('A', 3) != kernel('B', 3)
    arrivals = {}
    for origin in 'AB':
        for s, u in ((F(1, 2), F(3, 2)), (F(3, 2), F(1, 2))):
            q = kernel(origin, 1)[S.index(s)] * kernel(origin, 2)[S.index(u)] / 2
            arrivals[(origin, s, u)] = (q, q * s * u)
    assert sorted(q for q, p in arrivals.values()) == [F(1, 64)] * 2 + [F(1, 32)] * 2
    assert all(q > 0 and p > 0 for q, p in arrivals.values())
    for t, rs in ((2, S), (3, sorted({a * b for a, b in product(S, repeat=2)}))):
        for r in rs:
            margins = [stop(t, r) - cont(origin, t, r) for origin in 'AB']
            assert all(m > 0 for m in margins) if r == 1 else all(m < 0 for m in margins)

    initial = stop(1, F(1))
    ca, cb = cont('A', 1, F(1)), cont('B', 1, F(1))
    assert (initial, ca, cb) == (F(275, 248), F(68577, 63488), F(144477, 126976))
    assert ca < initial < cb and (ca + cb) / 2 == initial + F(1, 8192)
    full_min = (ca + initial) / 2
    assert full_min == F(138977, 126976)
    Oa, Ob = observer('A', 1, F(1)), observer('B', 1, F(1))
    O = tuple((a + b) / 2 for a, b in zip(Oa, Ob))
    assert O == (F(449, 4096), F(1599, 2048), F(15, 8), F(15, 8))
    assert O[0] + O[1] + THETA * (O[2] + O[3]) == full_min
    lr_min, ties = lr_brute_force()
    assert (lr_min, ties) == (F(275, 248), 512)
    assert lr_min - full_min == F(1823, 126976)
    assert 496 * O[0] + 496 * O[1] + 27 * O[2] + 27 * O[3] == F(138977, 256)
    assert (lr_min - full_min) / (2 + 2 * THETA) == F(1823, 267776)
    print('input: theta=27/496, epsilon=1/256; two origins, horizon=4')
    print('first_source_kernels:', kernel('A', 1), kernel('B', 1))
    print('second_source_kernels:', kernel('A', 3), kernel('B', 3))
    print('t3_r3/4_positive_Q_P_flows:', arrivals)
    print('initial_stop_and_full_continuations:', initial, ca, cb)
    print('full_observer:', O, 'full_min:', full_min)
    print('LR_min:', lr_min, 'exact_deterministic_masks:', 1024, 'ties:', ties)
    print('gap:', lr_min - full_min, 'integer_gap:', F(1823, 256))
    print('LR_plane: 496eP+496eQ+27TP+27TQ >= 550')
    print('FULL_plane_value:', F(138977, 256))
    print('L_infinity_distance_lower_bound:', F(1823, 267776))
    print('PASS_EXACT_R5_TWO_SOURCE_SENSITIVE_MERGERS')


if __name__ == '__main__':
    main()
