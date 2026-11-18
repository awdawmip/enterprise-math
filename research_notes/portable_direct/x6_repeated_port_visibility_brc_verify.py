#!/usr/bin/env python3
"""Exact typed Boolean-BRC support for a conditional, repeated Port relocation.

Six native *relative signed* Cell coordinates, three positive Port directions.
The tested alphabet may be restricted to 1/2 directions; that is not a native
2-dimensional plane. Other triads remain static obstacles while B may move.
"""
import itertools
import json
from collections import defaultdict
from math import comb

DIM = 6
ZERO = (0,) * DIM


def add(p, axis):
    z = list(p)
    z[axis] += 1
    return tuple(z)


def support_h(obstacles, start=ZERO, h=3, axes=(0, 1, 2)):
    """All legal decorated B Port words, and directly visible blocked frontier."""
    assert start not in obstacles
    branches = {((), start)}
    legal = {()}
    frontier = set()
    for step in range(h):
        nxt = set()
        for word, point in branches:
            for axis in axes:
                target = add(point, axis)
                if target in obstacles:
                    frontier.add(target)
                else:
                    w = word + (axis,)
                    nxt.add((w, target))
                    legal.add(w)
        branches = nxt
    return frozenset(legal), frozenset(frontier)


def lattice_ball(h, axes):
    out = {ZERO}
    layer = {ZERO}
    for _ in range(h):
        layer = {add(x, axis) for x in layer for axis in axes}
        out |= layer
    out.remove(ZERO)
    return sorted(out)


def complete_test(d, h):
    axes = tuple(range(d))
    pts = lattice_ball(h, axes)
    assert len(pts) == comb(h + d, d) - 1
    assert len(pts) <= 14
    by_frontier = {}
    by_language = {}
    for mask in range(1 << len(pts)):
        O = {p for i, p in enumerate(pts) if mask >> i & 1}
        lang, front = support_h(O, h=h, axes=axes)
        if front in by_frontier:
            assert by_frontier[front] == lang
        else:
            by_frontier[front] = lang
        if lang in by_language:
            assert by_language[lang] == front
        else:
            by_language[lang] = front
        # Future-safe horizon update: one B step consumes one unit of horizon.
        if h >= 2:
            for axis in axes:
                first = add(ZERO, axis)
                if first not in O:
                    _, future_front = support_h(O, start=first, h=h-1, axes=axes)
                    assert future_front <= front
    assert len(by_language) == len(by_frontier)
    return {"alphabet_axes": d, "horizon": h,
            "candidate_target_cells": len(pts),
            "obstacle_assignments": 1 << len(pts),
            "exact_future_language_classes": len(by_language),
            "frontier_signature_classes": len(by_frontier),
            "status": "PASS"}


def constructed_pair(h):
    assert h >= 2
    # B lives at the chosen Cell anchor, A starts at h*e0 - e1.
    a = (h, -1, 0, 0, 0, 0)
    initial_b = ZERO
    # A moves once: Port 1 -> h*e0 (blocked) or Port 2 -> h*e0 - e1 + e2 (clear).
    blocked = add(a, 1)
    clear = add(a, 2)
    assert initial_b != a and blocked != clear and blocked != initial_b
    O_blocked = {blocked}
    O_clear = {clear}
    for k in range(h):
        lang0, front0 = support_h(O_blocked, h=k)
        lang1, front1 = support_h(O_clear, h=k)
        assert lang0 == lang1
        assert front0 == front1
    lang0, front0 = support_h(O_blocked, h=h)
    lang1, front1 = support_h(O_clear, h=h)
    witness = (0,) * h
    assert witness not in lang0 and witness in lang1
    assert blocked in front0 and blocked not in front1
    # Initial R9 X is identical: both relocated triads miss all immediate B targets.
    first_targets = {add(ZERO, i) for i in (0, 1, 2)}
    assert not (O_blocked & first_targets) and not (O_clear & first_targets)
    return {"first_distinguishing_depth": h,
            "A_original": list(a), "A_Port_1_target": list(blocked),
            "A_Port_2_target": list(clear),
            "B_initial": list(initial_b),
            "witness_B_port_word": list(witness),
            "initial_R9_X_both": [], "status": "PASS"}


def run():
    test_pairs = ((1, 1), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4),
                  (3, 1), (3, 2))
    experiments = [complete_test(d,h) for d,h in test_pairs]
    delays = [constructed_pair(h) for h in range(2, 9)]
    return {"model": "conditional X6 signed-cell one-mobile-B repeated positive-Port steps; all other labelled triads static",
            "carrier": "typed Boolean BRC branch-word supports and coordinate-relative targets",
            "tests": experiments,
            "tested_obstacle_assignments": sum(x['obstacle_assignments'] for x in experiments),
            "delayed_collision_examples": delays,
            "native_TRIADIC_CLOSURE_E_admission": "NOT_ESTABLISHED",
            "status": "PASS"}

if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
