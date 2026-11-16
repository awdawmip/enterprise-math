#!/usr/bin/env python3
"""R219: exact support-resolved principal right-ideal distribution.

Pure finite-word observer algebra, not native BRC effect propagation.
The frozen model is independent of arbitrary real/complex arithmetic.
"""
from collections import Counter, deque
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json


def stirling2(n, r):
    row = [1]
    for i in range(1, n + 1):
        nxt = [0] * (i + 1)
        for j in range(1, i + 1):
            nxt[j] = j * (row[j] if j < len(row) else 0) + (row[j-1] if j-1 < len(row) else 0)
        row = nxt
    return row[r] if 0 <= r < len(row) else 0


def W(m, r, L):
    return factorial(r) * (m**L) * sum(stirling2(L + 1, j + 1) for j in range(min(r, L) + 1))


def T(m, k, L, r):
    return sum(comb(k-r, j-r) * W(m, j, L) for j in range(r, k + 1))


def support_words(m, k, h, r):
    """Number of length-h words with exactly r nonneutral source tags."""
    if r > min(k, h):
        return 0
    return comb(k, r) * (m**h) * sum((-1)**j * comb(r, j) * (r + 1 - j)**h for j in range(r + 1))


def geometric(a, h, L):
    return sum(a**d for d in range(L - h))


def formula_histogram(m, k, L):
    a = m * (k + 1)
    out = Counter()
    for r in range(k + 1):
        out[T(m, k, L, r)] += comb(k, r) * W(m, r, L)
    for h in range(L):
        for r in range(min(k, h) + 1):
            count = support_words(m, k, h, r)
            out[T(m, k, L, r) + geometric(a, h, L)] += count
    return +out


def append(state, event, L):
    order, tail = state
    tag = event[1]
    if tag:
        order = tuple(x for x in order if x != tag) + (tag,)
    return order, (tail + (event,))[-L:]


def finite_monoid(m, k, L):
    alphabet = tuple((d, s) for d in range(m) for s in range(k + 1))
    seed = ((), ())
    reps = {seed: ()}
    queue = deque([seed])
    while queue:
        s = queue.popleft()
        for e in alphabet:
            t = append(s, e, L)
            if t not in reps:
                reps[t] = reps[s] + (e,)
                queue.append(t)
    return reps


def verify_model(m, k, L):
    reps = finite_monoid(m, k, L)
    states = list(reps)
    n = len(states)
    index = {s: i for i, s in enumerate(states)}
    table = []
    for s in states:
        row = []
        for t in states:
            z = s
            for e in reps[t]:
                z = append(z, e, L)
            row.append(index[z])
        table.append(row)
    actual = Counter()
    right = []
    for i in range(n):
        right_set = set(table[i])
        right.append(right_set)
        actual[len(right_set)] += 1
    expected = formula_histogram(m, k, L)
    assert actual == expected, (m, k, L, actual, expected)
    must_equal = (m * (k + 1) == 1 or L <= 2)
    observed_equal = True
    for i in range(n):
        two = {table[j][z] for j in range(n) for z in right[i]}
        if two != right[i]:
            observed_equal = False
    assert observed_equal == must_equal, (m, k, L, must_equal, observed_equal)
    assert n == sum(expected.values())
    return dict(m=m, k=k, L=L, states=n, pair_products=n*n,
                principal_right_ideals_checked=n, right_equals_two_sided=observed_equal,
                histogram={str(key): val for key, val in sorted(actual.items())})


def main():
    params = [(1,0,1),(1,0,2),(1,0,4),(1,1,1),(1,1,2),(1,1,3),
              (1,1,4),(1,2,2),(1,2,3),(2,0,1),(2,0,2),
              (2,0,3),(2,1,2),(2,1,3),(2,2,2)]
    models = [verify_model(*p) for p in params]
    m,k,L = 12,6,2
    hist = formula_histogram(m,k,L)
    n = sum(hist.values())
    total = sum(size*count for size,count in hist.items())
    total2 = sum(size*size*count for size,count in hist.items())
    assert n == 1407685
    assert total == 863611486297
    assert total2 == 545292876127030381
    assert len(hist) == 10
    assert hist[1407685] == 1 and hist[1407601] == 12 and hist[1174177] == 72
    assert hist[518400] == 518400 and hist[604800] == 518400
    mean = Fraction(total, n)
    variance = Fraction(total2, n) - mean**2
    assert variance > 0
    evidence = {
        'schema':'R219_IDEAL_INCIDENCE_EXACT_CHECK_V1',
        'status':'PASS',
        'arithmetic':'Python arbitrary-precision integers and exact fractions only',
        'test_scope':'Complete generator BFS, full multiplication table, every principal right/two-sided ideal for each declared finite model',
        'models':models,
        'model_count':len(models),
        'states_checked':sum(x['states'] for x in models),
        'pair_products':sum(x['pair_products'] for x in models),
        'x6_L2':{
            'm':m,'k':k,'L':L,'state_count':n,'distinct_ideal_cardinalities':len(hist),
            'histogram':{str(key):val for key,val in sorted(hist.items())},
            'ordered_pair_incidence':total,'squared_size_sum':total2,
            'mean_numerator':mean.numerator,'mean_denominator':mean.denominator,
            'variance_numerator':variance.numerator,'variance_denominator':variance.denominator,
            'all_right_ideals_are_two_sided':True
        },
        'note':'Finite-word observer algebra only; no native BRC runtime or physical calibration tested.'
    }
    path = Path(__file__).with_name('R219_verification.json')
    path.write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:evidence[k] for k in ['status','model_count','states_checked','pair_products']},ensure_ascii=False))
    print('X6 L2 n',n,'sum',total,'mean',str(mean),'variance',str(variance))


if __name__ == '__main__':
    main()
