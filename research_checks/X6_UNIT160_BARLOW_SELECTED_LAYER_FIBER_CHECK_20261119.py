#!/usr/bin/env python3
"""Exact independent check of selected-layer Barlow prefix-observer fibers.

No historical P022 module is imported; this checks the derived combinatorial
count for periodic words truncated to their first n upward interfaces.
"""
import itertools
import json
import math


def fiber_count(n, layers, deltas):
    previous_t = previous_delta = 0
    result = 1
    for t, delta in zip(layers, deltas):
        length = t - previous_t
        drift = delta - previous_delta
        if abs(drift) > length or (length + drift) % 2:
            return 0
        result *= math.comb(length, (length + drift) // 2)
        previous_t, previous_delta = t, delta
    return result * (2 ** (n - previous_t))


def prefix(word):
    current = 0
    out = []
    for sign in word:
        current += sign
        out.append(current)
    return out


def run():
    total_cases = total_fibers = 0
    max_fiber = 0
    for n in range(1, 10):
        words = list(itertools.product((-1, 1), repeat=n))
        trajectories = [prefix(word) for word in words]
        for mask in range(1 << n):
            layers = tuple(t + 1 for t in range(n) if mask & (1 << t))
            fibers = {}
            for trajectory in trajectories:
                key = tuple(trajectory[t - 1] for t in layers)
                fibers[key] = fibers.get(key, 0) + 1
            for key, observed_count in fibers.items():
                exact = fiber_count(n, layers, key)
                if exact != observed_count:
                    raise ArithmeticError((n, layers, key, observed_count, exact))
                if observed_count > max_fiber:
                    max_fiber = observed_count
            total_cases += len(words)
            total_fibers += len(fibers)
            if sum(fibers.values()) != 1 << n:
                raise ArithmeticError('partition total failed')
            if layers and len(fibers) != math.prod((layers[i] - (layers[i - 1] if i else 0)) + 1 for i in range(len(layers))):
                raise ArithmeticError('observed-vector count failed')
        if fiber_count(n, tuple(range(1, n + 1)), tuple(prefix(words[0]))) != 1:
            raise ArithmeticError('full observation not injective')
    witness = {'n': 8, 'layers': [2, 5, 8], 'deltas': [0, 1, 0]}
    witness['fiber_size'] = fiber_count(8, witness['layers'], witness['deltas'])
    witness['min_additional_fixed_bits'] = (witness['fiber_size'] - 1).bit_length()
    if witness['fiber_size'] != 18 or witness['min_additional_fixed_bits'] != 5:
        raise ArithmeticError('witness count failed')
    return {
        'schema': 'X6_BARLOW_SELECTED_PREFIX_FIBER_EXACT_CHECK_V1',
        'frozen_historical_commit': 'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
        'n_range': [1, 9],
        'word_selection_checks': total_cases,
        'distinct_observer_fiber_checks': total_fibers,
        'max_fiber': max_fiber,
        'selected_witness': witness,
        'checked': 'exact enumeration vs product of binomial counts; all sampled-layer subsets including empty set',
        'status': 'PASS',
    }


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, sort_keys=True, separators=(',', ':')))
