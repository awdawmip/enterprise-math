#!/usr/bin/env python3
"""R5 interval support / maximal-clique exact-carrier reproducibility checks.

Pure Python standard library. No frozen R5 center data is loaded.
All sampled claims are limited to synthetic integer-center instances.
"""
from functools import lru_cache
import random


def maximal(masks):
    masks = set(masks)
    return frozenset(
        x for x in masks
        if not any(x != y and (x & y) == x for y in masks)
    )


def forward_windows(centers, tau):
    return maximal(
        sum(1 << j for j, y in enumerate(centers)
            if x <= y <= x + tau)
        for x in centers
    )


def left_endpoints(centers, tau):
    # z = 2*x - tau gives x-tau <= N_j <= x, NOT the forward window.
    return maximal(
        sum(1 << j for j, y in enumerate(centers)
            if x - tau <= y <= x)
        for x in centers
    )


def neighbors(centers, tau):
    return [
        sum(1 << j for j, y in enumerate(centers)
            if i != j and abs(x-y) <= tau)
        for i, x in enumerate(centers)
    ]


def maximal_graph_cliques(centers, tau):
    # Independent brute force: examine every nonempty labeled subset.
    n = len(centers)
    adj = neighbors(centers, tau)
    cliques = [
        subset for subset in range(1, 1 << n)
        if all((subset & ~(1 << i) & ~adj[i]) == 0
               for i in range(n) if subset & (1 << i))
    ]
    return maximal(cliques)


def append_one(old_family, neighbor_bitmap, old_n):
    old_maximal_without_new = {
        C for C in old_family if (C & neighbor_bitmap) != C
    }
    new_maximal_with_new = {
        D | (1 << old_n)
        for D in maximal(C & neighbor_bitmap for C in old_family)
    }
    return frozenset(old_maximal_without_new | new_maximal_with_new)


def value(actions, f, n):
    # For a positive-cost action containing all currently live labels,
    # the adversary can retain the state. Such an action is not optimal.
    @lru_cache(None)
    def solve(e):
        live = sum(1 << i for i, z in enumerate(e) if z <= f)
        if live.bit_count() <= 1:
            return 0
        choices = []
        for cost, family in actions:
            if any((s & live) == live for s in family):
                continue
            worst = max(
                solve(tuple(min(f + 1, z + (0 if (s >> i) & 1 else 1))
                            for i, z in enumerate(e)))
                for s in family
            )
            choices.append(cost + worst)
        return min(choices, default=float("inf"))

    answer = solve((0,) * n)
    return answer, solve.cache_info().misses


def test_clique_and_append():
    rng = random.Random(20261123)
    for trial in range(15000):
        n = rng.randint(2, 10)
        centers = [rng.randint(-60, 60) for _ in range(n)]
        tau = rng.randint(0, 30)
        expected = forward_windows(centers, tau)
        assert expected == left_endpoints(centers, tau), ("left", trial)
        assert expected == maximal_graph_cliques(centers, tau), ("graph", trial)
        N_new = neighbors(centers, tau)[-1] & ((1 << (n - 1)) - 1)
        increment = append_one(
            forward_windows(centers[:-1], tau), N_new, n - 1
        )
        assert expected == increment, ("increment", trial)
    print("PASS support/maximal-clique/left-endpoint/append: 15000 cases")


def test_bellman():
    rng = random.Random(2026112301)
    states = 0
    max_states = 0
    for trial in range(180):
        n = 4
        tau = rng.randint(1, 5)
        centers_per_action = [
            [rng.randrange(20) for _ in range(n)] for _ in range(4)
        ]
        # Final fifth action makes all labels distinguishable.
        centers_per_action.append([j * (2*tau + 1) for j in range(n)])
        actions_forward = [
            (k, forward_windows(x, tau))
            for k, x in enumerate(centers_per_action, start=1)
        ]
        actions_append = [
            (k, append_one(
                forward_windows(x[:-1], tau),
                neighbors(x, tau)[-1] & ((1 << (n-1)) - 1), n-1))
            for k, x in enumerate(centers_per_action, start=1)
        ]
        for f in range(3):
            a, numstates = value(actions_forward, f, n)
            b, _ = value(actions_append, f, n)
            assert a == b, (trial, f, a, b)
            states += numstates
            max_states = max(max_states, numstates)
    print("PASS exact Bellman: 540 comparisons; states", states,
          "max single", max_states)


def test_perturbation():
    rng = random.Random(2026112302)
    for trial in range(5000):
        n = rng.randrange(2, 11)
        centers = [10 * rng.randrange(-10, 11) for _ in range(n)]
        tau = 15
        margins = []
        for i in range(n):
            for j in range(i+1, n):
                d = abs(centers[i] - centers[j])
                margins.append(tau - d if d <= tau else d - tau - 1)
        gamma = min(margins)
        assert gamma >= 4
        changed_centers = [x + rng.randrange(-1, 2) for x in centers]
        changed_tau = tau + rng.randrange(-2, 3)
        assert 2*1 + 2 <= gamma
        assert neighbors(centers, tau) == neighbors(changed_centers, changed_tau), trial
    print("PASS integer-threshold perturbation: 5000 cases")


if __name__ == "__main__":
    test_clique_and_append()
    test_bellman()
    test_perturbation()
