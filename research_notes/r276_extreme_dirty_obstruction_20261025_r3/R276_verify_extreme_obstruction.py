"""R276 exact six-channel BRC check: Python standard library, no floats."""
import json
from itertools import product
from collections import defaultdict

E = (((2, -1, -1), (2, 1, -1)),
     ((0, -1, -1), (0, 1, -1)),
     ((1, 1, 1), (2, 1, -1)))
CH = tuple((d, q) for d in (False, True) for q in range(3))


def advance(state, bit):
    dirty, q, last, eps, k = state
    nq, eta, b = E[q][bit]
    return dirty or last == bit == 0, nq, bit, eta * eps, eta * k + b


def histogram(states):
    h = {c: defaultdict(int) for c in CH}
    for (dirty, q, last, eps, k), count in states.items():
        h[dirty, q][eps, k] += count
    return h


def raw_histogram(n):
    h = {c: defaultdict(int) for c in CH}
    for word in product((0, 1), repeat=n):
        state = (False, 0, None, 1, 0)
        for bit in word:
            state = advance(state, bit)
        dirty, q, last, eps, k = state
        h[dirty, q][eps, k] += 1
    return h


def run():
    states = {(False, 0, None, 1, 0): 1}
    samples = {}
    for n in range(401):
        h = histogram(states)
        assert sum(sum(x.values()) for x in h.values()) == 2**n
        if n <= 15:
            raw = raw_histogram(n)
            assert all(h[c] == raw[c] for c in CH), n
        if n >= 4:
            for eps in (1, -1):
                g = (eps, -(n - 2))
                expected = ((1, 1, n-3, 0, 0, 1) if eps == 1
                            else (1, 1, n-4, 0, 0, 2))
                assert tuple(h[c].get(g, 0) for c in CH) == expected, (n, g)
        if n >= 12:
            peak = max(h[False, 0].values())
            maximizers = [g for g, v in h[False, 0].items() if v == peak]
            assert any(all(h[c].get(g, 0) >= peak for c in CH)
                       for g in maximizers), n
        if n in (4, 12, 30, 100, 200, 400):
            p = max(h[False, 0].values())
            samples[str(n)] = {'Lambda': str(p), 'effects': [list(g) for g, v in
                                 h[False, 0].items() if v == p]}
        if n < 400:
            nxt = defaultdict(int)
            for state, mass in states.items():
                for bit in (0, 1):
                    nxt[advance(state, bit)] += mass
            states = nxt
    return {
        'schema': 'R276_EXACT_CHECK_V1', 'status': 'PASS',
        'model': 'R275 exact positive-weight ordered-word BRC',
        'channel_order': ['C0', 'C1', 'C2', 'D0', 'D1', 'D2'],
        'raw_words': {'depths': [0, 15], 'count': 65535},
        'integer_DP': {'depths': [0, 400], 'full_affine_effects': True},
        'edge_profile': {'depths': [4, 400], 'cases': 4764},
        'finite_B_equals_Lambda': {'depths': [12, 400], 'cases': 389},
        'samples': samples,
        'limits': 'Finite checks only; no original enterprise_math package or Driver review.'}


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
