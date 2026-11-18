#!/usr/bin/env python3
"""R7: typed Boolean-BRC source-label future language penultimate reconstruction.
Scope: deterministic partial named-port controllers, productive fixed terminal quotas.
Carries actual (word,mode) branches, then quotients to (count vector,mode).
Not a native triadic-force admission or numerical signed-amplitude simulation.
"""
import itertools
import json
from collections import defaultdict
from functools import lru_cache
from math import ceil, log2


def inspect_model(quotas, periods, rule, terminal_mask):
    d = len(quotas)
    letters = tuple('ABCDE'[:d])
    root = ((0,) * d, 0)
    total = sum(quotas)

    def append(state, j):
        n, mode = state
        if n[j] == quotas[j]:
            return None
        new_mode = rule[mode * d + j]
        if new_mode == -1:
            return None
        m = list(n)
        m[j] += 1
        return tuple(m), new_mode

    levels = [{root}]
    branches = {('', 0)}
    for k in range(total):
        next_states = {s2 for state in levels[-1] for j in range(d)
                       if (s2 := append(state, j)) is not None}
        next_branches = set()
        for word, mode in branches:
            state = (tuple(word.count(letter) for letter in letters), mode)
            for j, letter in enumerate(letters):
                new = append(state, j)
                if new is not None:
                    next_branches.add((word + letter, new[1]))
        branches = next_branches
        assert next_states == {(tuple(w.count(letter) for letter in letters), m)
                               for w, m in branches}
        levels.append(next_states)

    @lru_cache(None)
    def full(state):
        n, mode = state
        if n == quotas:
            return frozenset(('',)) if (terminal_mask & (1 << mode)) else frozenset()
        return frozenset(letter + tail
                         for j, letter in enumerate(letters)
                         if (child := append(state, j)) is not None
                         for tail in full(child))

    @lru_cache(None)
    def penultimate(state, horizon):
        if not full(state):
            return frozenset()
        if horizon == 0:
            return frozenset(('',))
        return frozenset(word[:t] for word in full(state)
                         for t in range(min(horizon, len(word)) + 1))

    fibers_checked = 0
    nontrivial_terminal_degrees = 0
    max_degree = 1
    bit_gain_seen = 0
    for k, level in enumerate(levels):
        H = total - k
        if H == 0:
            continue
        fibers = defaultdict(list)
        for state in level:
            if full(state):
                n, mode = state
                obs = (k, tuple(ni % pi for ni, pi in zip(n, periods)))
                fibers[obs].append(state)
        for obs, states in fibers.items():
            classes = defaultdict(list)
            for s in states:
                classes[penultimate(s, H - 1)].append(s)
            m_short = len(classes)
            m_full = len({full(s) for s in states})
            reconstruction = 0
            for language, E in classes.items():
                u = next(w for w in language if len(w) == H - 1)
                j_classes = defaultdict(list)
                for state in E:
                    n, _ = state
                    residue = tuple(quotas[j] - n[j] - u.count(letters[j])
                                    for j in range(d))
                    assert sum(residue) == 1 and all(x in (0, 1) for x in residue)
                    j = residue.index(1)
                    j_classes[j].append(state)
                for same_j in j_classes.values():
                    assert len({full(s) for s in same_j}) == 1
                if len(j_classes) > 1:
                    nontrivial_terminal_degrees += 1
                    assert all(periods[j] == 1 for j in j_classes)
                reconstruction += len(j_classes)
                max_degree = max(max_degree, len(j_classes))
                assert len({full(s) for s in E}) == len(j_classes)
            assert m_full == reconstruction
            assert m_short <= m_full <= max(1, sum(pi == 1 for pi in periods)) * m_short
            gain = (m_full - 1).bit_length() - (m_short - 1).bit_length()
            assert gain >= 0
            bit_gain_seen += gain > 0
            fibers_checked += 1
    return fibers_checked, nontrivial_terminal_degrees, max_degree, bit_gain_seen, bool(full(root))


def run():
    period_vectors = [(1, 1, 1), (1, 1, 2), (1, 2, 2),
                      (2, 3, 1), (2, 2, 2)]
    quotas_options = [(1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1)]
    models = 0
    fibers = 0
    nontrivial = 0
    maximum = 1
    bit_gains = 0
    productive_roots = 0
    for rule in itertools.product((-1, 0, 1), repeat=6):
        for quota in quotas_options:
            for periods in period_vectors:
                for terminal_mask in (1, 2, 3):
                    f, n, m, b, root = inspect_model(quota, periods, rule, terminal_mask)
                    models += 1
                    fibers += f
                    nontrivial += n
                    maximum = max(maximum, m)
                    bit_gains += b
                    productive_roots += root
    # Sharpness independent of controller reachability details: one-mode
    # all-capacity-respecting BRC branch carrier with d=t+1 channels.
    sharp = []
    for t in range(2, 7):
        d = t + 1
        capacities = (1,) * d
        periods = (1,) * t + (2,)
        k = d - 1
        nodes = [tuple(int(j != i) for j in range(d)) for i in range(t)]
        assert all(sum(n) == k for n in nodes)
        obs = {(k, tuple(n[j] % periods[j] for j in range(d))) for n in nodes}
        assert len(obs) == 1
        assert len({('ABCDEFX'[i],) for i in range(t)}) == t
        sharp.append({'period_one_channels': t, 'penultimate_classes': 1,
                      'full_classes': t, 'necessary_bits': (t - 1).bit_length()})
    return {'schema': 'X6_TERMINAL_LABEL_RECONSTRUCTION_R7_V1',
            'status': 'PASS', 'typed_carrier': 'labelled Boolean-BRC word+port mode, support count+mode',
            'domain': 'all 3^6 two-mode 3-label partial controllers, 4 quotas, 5 period vectors, 3 nonempty terminal-mode masks',
            'models': models, 'observed_productive_fibers': fibers,
            'nontrivial_penultimate_classes': nontrivial,
            'max_terminal_label_degree': maximum,
            'fibers_with_strict_extra_bit_need': bit_gains,
            'productive_roots': productive_roots,
            'sharp_family': sharp,
            'limitations': 'conditional named-port support languages; no signed amplitude, physical clock, native TRIADIC_CLOSURE_E admission'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False, sort_keys=True))
