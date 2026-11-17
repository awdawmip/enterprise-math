#!/usr/bin/env python3
"""Exact finite tests for a conditional P000-compatible guarded triadic bundle transfer.
Not a physical native event-admission claim. Only standard-library integer arithmetic.
"""
from collections import Counter
from itertools import permutations, product
from math import comb

DIM = 6
ZERO = (0,) * DIM

def add_axis(cell, axis):
    assert 0 <= axis < DIM
    nxt = list(cell)
    nxt[axis] += 1
    return tuple(nxt)

def emit(occupancy, source, frame, slot):
    """Partial guarded transition: ordered positive native-axis triad."""
    assert len(frame) == 3 and len(set(frame)) == 3
    assert 0 <= slot < 3
    dst = add_axis(source, frame[slot])
    assert occupancy.get(source) == frame, 'source triad unavailable'
    assert dst not in occupancy, 'destination occupied'
    result = dict(occupancy)
    result.pop(source)
    result[dst] = frame
    return result, (source, dst, frame, slot)

def assert_guard_rejects(call):
    try:
        call()
    except AssertionError:
        return
    raise AssertionError('guard failed to reject')

def test_all_one_cell_frames():
    frames = list(permutations(range(DIM), 3))
    assert len(frames) == 120
    tested = 0
    for frame in frames:
        init = {ZERO: frame}
        dsts = set()
        for slot in range(3):
            post, witness = emit(init, ZERO, frame, slot)
            dsts.add(witness[1])
            assert ZERO not in post and post[witness[1]] == frame
            assert len(post) == 1
            assert_guard_rejects(lambda: emit(post, ZERO, frame, slot))
            for other in range(3):
                assert_guard_rejects(lambda other=other: emit(post, ZERO, frame, other))
            tested += 1
        assert len(dsts) == 3
    assert tested == 360
    return len(frames), tested

def test_disjoint_sources(max_m=7):
    """Enumerate per-source choices: none/exit0/exit1/exit2."""
    histograms = {}
    frame = (0, 1, 2)
    for m in range(1, max_m + 1):
        sources = [(10*j, 0, 0, 0, 0, 0) for j in range(m)]
        occupancy = {s: frame for s in sources}
        counts = Counter()
        for choices in product(range(4), repeat=m):
            state = occupancy.copy()
            chosen = []
            for j, choice in enumerate(choices):
                if choice:
                    state, event = emit(state, sources[j], frame, choice-1)
                    chosen.append(event)
            assert len(state) == m
            assert len(chosen) == sum(bool(x) for x in choices)
            assert len({e[0] for e in chosen}) == len(chosen)
            counts[len(chosen)] += 1
        expect = [comb(m, k) * 3**k for k in range(m+1)]
        assert [counts[k] for k in range(m+1)] == expect
        assert sum(counts.values()) == 4**m
        histograms[m] = expect
    return histograms

if __name__ == '__main__':
    frames, candidates = test_all_one_cell_frames()
    hist = test_disjoint_sources()
    print('ordered_positive_frames', frames)
    print('guarded_single_hop_candidates', candidates)
    print('m=1', hist[1])
    print('m=2', hist[2])
    print('m=7', hist[7])
    print('all_integer_tests_passed', True)
