#!/usr/bin/env python3
"""Deterministic exact checker for Seed-6 four-atom three-pairing orbit.

The checker uses only finite enumeration and exact integer arithmetic. It does not
assign a numerical metric to the pairing states and does not interpret them as a
factorization search space.
"""
from __future__ import annotations

import hashlib
import itertools
import math
from collections import Counter
from pathlib import Path

ATOMS = ("a", "b", "c", "d")
TASKBOOK = "research_tasks/SEED6_THREE_PAIRING_ORBIT_BRIDGE_RECTANGLE_20260829.md"
TASKBOOK_BLOB_SHA1 = "5bc9ca750300b846bec6c8756f7c981543483eaf"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canon_edge(edge):
    return tuple(sorted(edge))


def canon_matching(edges):
    return tuple(sorted(canon_edge(e) for e in edges))


def all_matchings():
    out = set()
    for perm in itertools.permutations(ATOMS):
        out.add(canon_matching(((perm[0], perm[1]), (perm[2], perm[3]))))
    return tuple(sorted(out))


MATCHINGS = all_matchings()


def matching_action(atom_perm):
    p = dict(zip(ATOMS, atom_perm))
    image = []
    for matching in MATCHINGS:
        moved = canon_matching((p[x], p[y]) for x, y in matching)
        image.append(MATCHINGS.index(moved))
    return tuple(image)


def support_vertices():
    return tuple(frozenset(e) for e in itertools.combinations(ATOMS, 2))


Q = support_vertices()


def support_adjacent(s, t):
    return len(s & t) == 1


def support_complement(s):
    return frozenset(set(ATOMS) - set(s))


def graph_automorphisms():
    out = set()
    for values in itertools.permutations(Q):
        m = dict(zip(Q, values))
        if all(
            support_adjacent(s, t) == support_adjacent(m[s], m[t])
            for s in Q for t in Q
        ):
            out.add(values)
    return out


def atom_induced_support_automorphisms():
    out = set()
    for values in itertools.permutations(ATOMS):
        p = dict(zip(ATOMS, values))
        out.add(tuple(frozenset(p[x] for x in s) for s in Q))
    return out


def compose_state_actions(f, g):
    """Return f after g on {0,1,2}."""
    return tuple(f[g[i]] for i in range(3))


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def first_primes_gt_three(count):
    out = []
    n = 5
    while len(out) < count:
        if is_prime(n):
            out.append(n)
        n += 1
    return out


def numeric_regression():
    primes = first_primes_gt_three(25)
    assert primes == [
        5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
    ]
    pairs = list(itertools.combinations(primes, 2))
    assert len(pairs) == 300

    order_signatures = Counter()
    for p, q in pairs:
        values = (6, 2*p, 2*q, 3*p, 3*q, p*q)
        assert len(set(values)) == 6

        states = ((6, p*q), (2*p, 3*q), (2*q, 3*p))
        assert len({tuple(sorted(s)) for s in states}) == 3
        assert {x*y for x, y in states} == {6*p*q}
        assert all(math.gcd(x, y) == 1 for x, y in states)

        # Between any two distinct pairing states the 2x2 gcd matrix
        # contains the four underlying atoms exactly once.
        for i, j in ((0, 1), (0, 2), (1, 2)):
            cross = sorted(math.gcd(x, y) for x in states[i] for y in states[j])
            assert cross == sorted((2, 3, p, q))

        # Three bridge rectangles, one for each carrier matching.
        a, b, c, d = 2, 3, p, q
        rectangles = (
            ((a*c, a*d), (b*c, b*d)),
            ((a*b, a*d), (c*b, c*d)),
            ((a*b, a*c), (d*b, d*c)),
        )
        for row1, row2 in rectangles:
            assert row1[0] * row2[1] == row1[1] * row2[0]

        if 2*q < 3*p:
            order_signatures["2q<3p"] += 1
            assert 6 < 2*p < 2*q < 3*p < 3*q < p*q
        else:
            assert 3*p < 2*q  # equality would imply q=3 or p even
            order_signatures["3p<2q"] += 1
            assert 6 < 2*p < 3*p < 2*q < 3*q < p*q

    assert order_signatures == Counter({"2q<3p": 85, "3p<2q": 215})
    return primes, order_signatures


def main():
    root = Path(__file__).resolve().parents[1]
    taskbook = root / TASKBOOK
    assert taskbook.exists()
    assert git_blob_sha1(taskbook) == TASKBOOK_BLOB_SHA1

    # A. Exactly three unordered perfect matchings of four distinct atoms.
    assert MATCHINGS == (
        (("a", "b"), ("c", "d")),
        (("a", "c"), ("b", "d")),
        (("a", "d"), ("b", "c")),
    )

    # B/C. Exact S4 action on the three pairing states.
    actions = {perm: matching_action(perm) for perm in itertools.permutations(ATOMS)}
    image = set(actions.values())
    kernel = {perm for perm, action in actions.items() if action == (0, 1, 2)}
    stabilizer0 = {perm for perm, action in actions.items() if action[0] == 0}
    assert len(actions) == 24
    assert len(image) == 6  # full S3
    assert len(kernel) == 4
    assert kernel == {
        ("a", "b", "c", "d"),
        ("b", "a", "d", "c"),
        ("c", "d", "a", "b"),
        ("d", "c", "b", "a"),
    }
    assert len(stabilizer0) == 8
    assert Counter(actions.values()) == Counter({
        (0, 1, 2): 4, (0, 2, 1): 4, (1, 0, 2): 4,
        (1, 2, 0): 4, (2, 0, 1): 4, (2, 1, 0): 4,
    })

    # Single atom transpositions: each quotient edge-switch has exactly
    # two single-transposition lifts.
    transposition_actions = Counter()
    for i, j in itertools.combinations(range(4), 2):
        vals = list(ATOMS)
        vals[i], vals[j] = vals[j], vals[i]
        transposition_actions[matching_action(tuple(vals))] += 1
    assert transposition_actions == Counter({
        (0, 2, 1): 2,
        (2, 1, 0): 2,
        (1, 0, 2): 2,
    })

    # D/E. Six two-atom supports form J(4,2): six vertices, degree 4,
    # twelve edges; complement gives exactly the three antipodal states.
    assert len(Q) == 6
    degrees = {s: sum(support_adjacent(s, t) for t in Q if t != s) for s in Q}
    assert set(degrees.values()) == {4}
    edge_count = sum(degrees.values()) // 2
    assert edge_count == 12

    complement_pairs = {
        frozenset((s, support_complement(s))) for s in Q
    }
    assert len(complement_pairs) == 3
    expected_states = {
        frozenset(frozenset(e) for e in matching) for matching in MATCHINGS
    }
    assert complement_pairs == expected_states

    # Each carrier state removes one antipodal pair and leaves K2,2=C4.
    # The two alternating perfect matchings of that C4 are the other two states.
    for carrier in expected_states:
        remaining = [s for s in Q if s not in carrier]
        assert len(remaining) == 4
        rem_degrees = {
            s: sum(support_adjacent(s, t) for t in remaining if t != s)
            for s in remaining
        }
        assert set(rem_degrees.values()) == {2}
        assert sum(rem_degrees.values()) // 2 == 4

    # Bare support graph has an extra complement symmetry: Aut J(4,2)=48,
    # whereas atom permutations induce only 24 automorphisms.
    graph_aut = graph_automorphisms()
    atom_aut = atom_induced_support_automorphisms()
    complement_auto = tuple(support_complement(s) for s in Q)
    assert len(graph_aut) == 48
    assert len(atom_aut) == 24
    assert complement_auto in graph_aut
    assert complement_auto not in atom_aut

    # Edge-decorated quotient loop has nontrivial operator holonomy even
    # though it returns to the starting state.
    tau01 = (1, 0, 2)
    tau12 = (0, 2, 1)
    tau20 = (2, 1, 0)
    holonomy = compose_state_actions(tau20, compose_state_actions(tau12, tau01))
    assert holonomy == tau12
    assert compose_state_actions(holonomy, holonomy) == (0, 1, 2)

    primes, order_signatures = numeric_regression()

    print("PASS SEED6_THREE_PAIRING_ORBIT_EXACTLY_CLASSIFIED")
    print("matching_states=3 S4_image=6 kernel=4 stabilizer=8")
    print("support_graph=J(4,2) vertices=6 edges=12 aut=48 atom_aut=24")
    print("regression_pairs=300 primes=25 last_prime=%d" % primes[-1])
    print("numeric_order_strata=%s" % dict(order_signatures))


if __name__ == "__main__":
    main()
