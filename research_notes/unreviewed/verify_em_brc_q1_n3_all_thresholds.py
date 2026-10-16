#!/usr/bin/env python3
"""Standalone, unreviewed, no-dependency crosscheck of n=3, Q=1 BRC result."""
from itertools import product, combinations


def reset(x, i):
    return tuple(0 if k == i else value for k, value in enumerate(x))


def safe(x, T, policy):
    def recurse(state, history):
        protected = policy(history)
        if protected is None:
            return sum(state) > 0
        return all(recurse(y, history + (int(sum(y) >= T),))
                   for i in range(3) if i != protected
                   for y in [reset(state, i)])
    return recurse(x, ())


def positive(j):
    return lambda history: j if len(history) < 2 else None


def high(j):
    return lambda history: (j if len(history) < 2 else
                            (j+1) % 3 if len(history) == 2 and history[-1] == 0
                            else None)


def pair(i, k):
    third = 3 - i - k
    return lambda history: (i if not history else
                            None if history[0] == 0 else
                            third if len(history) < 3 else None)


def signature(x, T):
    if T == 1:
        return tuple(int(z > 0) for z in x)
    categories = tuple(0 if z == 0 else 2 if z >= T else 1 for z in x)
    edges = tuple(int(x[i] + x[k] >= T) for i, k in combinations(range(3), 2))
    return categories + edges


def main():
    counts = {'Pos': 0, 'High': 0, 'Pair': 0}
    exact = []
    for T in range(1, 13):
        states = list(product(range(T+1), repeat=3))
        classes = {signature(x, T) for x in states}
        expected = 8 if T == 1 else 27 if T == 2 else 37 if T == 3 else 40
        assert len(classes) == expected, (T, len(classes))
        exact.append((T, len(states), len(classes)))
        if T > 8:
            continue
        for x in states:
            for j in range(3):
                assert safe(x, T, positive(j)) == (x[j] > 0), ('Pos', T, x, j)
                counts['Pos'] += 1
                if T >= 2:
                    assert safe(x, T, high(j)) == (x[j] >= T), ('High', T, x, j)
                    counts['High'] += 1
            for i, k in combinations(range(3), 2):
                if 0 < x[i] < T and 0 < x[k] < T:
                    assert safe(x, T, pair(i,k)) == (x[i]+x[k] < T), ('Pair', T, x, i, k)
                    counts['Pair'] += 1
    print('Exact signatures (T, #states, #classes):', exact)
    print('All hidden-reset policy checks passed:', counts)
    assert counts == {'Pos': 6072, 'High': 6048, 'Pair': 3192}


if __name__ == '__main__':
    main()
