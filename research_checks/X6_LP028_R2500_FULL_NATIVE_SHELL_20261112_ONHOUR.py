#!/usr/bin/env python3
"""Exact R063 N=2500 comparison: scoped positive sector vs signed native X6.

Two independent methods produce the signed-shell census: (1) signed-axis
multinomial dynamic programming on (squared norm, shortest path length), and
(2) sorted absolute-coordinate orbits under the signed-permutation action.
No floating-point arithmetic, native primitive off-axis claim, or random test.
"""
from collections import Counter, defaultdict
from math import comb, factorial, isqrt


def signed_shell_dp(dim: int, squared_norm: int):
    """Map (partial norm, step count) to (endpoint count, shortest BRC mass)."""
    states = {(0, 0): (1, 1)}
    for _ in range(dim):
        next_states = {}
        for (old_q, old_t), (old_endpoints, old_mass) in states.items():
            for a in range(isqrt(squared_norm - old_q) + 1):
                key = (old_q + a * a, old_t + a)
                sign_options = 1 if a == 0 else 2
                prev_e, prev_mass = next_states.get(key, (0, 0))
                next_states[key] = (
                    prev_e + sign_options * old_endpoints,
                    prev_mass + sign_options * old_mass * comb(old_t + a, a),
                )
        states = next_states
    hist = {t: values for (q, t), values in states.items() if q == squared_norm}
    return (
        sum(e for e, mass in hist.values()),
        sum(mass for e, mass in hist.values()),
        hist,
    )


def signed_shell_orbits(dim: int, squared_norm: int):
    """Enumerate nonincreasing nonnegative canonical tuples, expand exact orbits."""
    maximum = isqrt(squared_norm)
    facts = [factorial(i) for i in range(dim * maximum + 1)]
    support_counts = Counter()
    length_hist = defaultdict(lambda: [0, 0])
    canonical_shapes = 0

    def visit(prefix: tuple[int, ...], bound: int, remaining: int):
        nonlocal canonical_shapes
        slots = dim - len(prefix)
        if slots == 0:
            if remaining:
                return
            canonical_shapes += 1
            multiplicities = Counter(prefix)
            symmetry_denom = 1
            for m in multiplicities.values():
                symmetry_denom *= facts[m]
            support = sum(a > 0 for a in prefix)
            orbit_size = facts[dim] // symmetry_denom * (1 << support)
            path_length = sum(prefix)
            denominator = 1
            for a in prefix:
                denominator *= facts[a]
            shortest_brc = facts[path_length] // denominator
            support_counts[support] += orbit_size
            length_hist[path_length][0] += orbit_size
            length_hist[path_length][1] += orbit_size * shortest_brc
            return
        for a in range(min(bound, isqrt(remaining)), -1, -1):
            # Every remaining coordinate is <= a, so an impossible tail is pruned.
            if slots * a * a < remaining:
                continue
            visit(prefix + (a,), a, remaining - a * a)

    visit((), maximum, squared_norm)
    return (
        sum(x[0] for x in length_hist.values()),
        sum(x[1] for x in length_hist.values()),
        canonical_shapes,
        dict(sorted(support_counts.items())),
        {k: tuple(v) for k, v in length_hist.items()},
    )


def main():
    # Existing frozen/task-bounded anchors: 3-axis N25, R063 positive/signed 2-axis,
    # and previously calculated 3-axis N2500. These are consumed, not rediscovered.
    existing = {
        (3, 25): (30, 846),
        (2, 2500): (20, 442782153097022856828),
        (3, 2500): (150, 26860799510260072787603759892561716013678),
        (6, 25): (7812, 2538954612),
    }
    for (dim, norm), expected in existing.items():
        e1, m1, h1 = signed_shell_dp(dim, norm)
        e2, m2, _, _, h2 = signed_shell_orbits(dim, norm)
        assert (e1, m1) == (e2, m2) == expected, (dim, norm, e1, m1)
        assert h1 == h2

    n, norm = 6, 2500
    e1, m1, h1 = signed_shell_dp(n, norm)
    e2, m2, shapes, supports, h2 = signed_shell_orbits(n, norm)
    assert (e1, m1) == (e2, m2)
    assert h1 == h2
    assert e1 == 102539052
    assert m1 == 46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372
    assert shapes == 3356
    assert supports == {1: 12, 2: 240, 3: 1920, 4: 273840, 5: 7610880, 6: 94652160}
    assert len(h1) == 32 and min(h1) == 50 and max(h1) == 122
    assert sum(supports.values()) == e1
    print('PASS: independent exact DP and signed-permutation orbit census agree')
    print('norm=2500, dimension=6, canonical_absolute_shapes=', shapes)
    print('native_signed_endpoints=', e1)
    print('native_shortest_BRC_mass=', m1)
    print('support_endpoints=', supports)
    print('shortest_word_lengths=', len(h1), min(h1), max(h1))
    print('legacy_anchor_regressions=', len(existing))


if __name__ == '__main__':
    main()
