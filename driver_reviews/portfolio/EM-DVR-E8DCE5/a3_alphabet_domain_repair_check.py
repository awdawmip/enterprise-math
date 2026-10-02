#!/usr/bin/env python3
"""Bounded A3 alphabet-domain checks, separate from the author's checker.

Verifies singleton invisibility, binary one-marker faithfulness, and the
order-two H global-witness distinction on n <= 2. This is a delegated local
repair probe, not a Result, Driver Review or replay of the author's enumeration.
Only standard Python is used; nothing is written and no network is contacted.
"""

from itertools import combinations, permutations, product
import json


def signed_permutation(p, x):
    inversions = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
    sign = -1 if inversions % 2 else 1
    y = [0] * 4
    for i, value in enumerate(x):
        y[p[i]] = sign * value
    return tuple(y)


def ball(n):
    return tuple(x for x in product(range(-n, n + 1), repeat=4) if sum(x) == 0)


def radius(x):
    return max(map(abs, x))


def quotient_witness(K, h, points):
    """Return a one/two-marker witness, or None for a global H operator.

    For H={id,h}, all singleton subsets force K to flip or fix each h-pair.
    If two pairs receive different choices, one marker in each witnesses the
    failure of one common h. Thus these probes suffice here; they are not a
    general small-marker assertion for larger quotient groups.
    """
    for p in points:
        if K[p] not in (p, h[p]):
            return (p,)
    for p, q in combinations(points, 2):
        state = frozenset((p, q))
        if frozenset((K[p], K[q])) not in (state, frozenset((h[p], h[q]))):
            return (p, q)
    return None


def main():
    G = tuple(permutations(range(4)))
    identity = (0, 1, 2, 3)
    h_perm = (1, 0, 2, 3)
    cases = singleton_cases = raw_nonidentity = quotient_nonglobal = 0
    raw_marker_checks = quotient_one_marker = quotient_two_marker = 0
    ball_sizes = {}
    for n in (1, 2):
        points = ball(n)
        point_set = set(points)
        ball_sizes[str(n)] = len(points)
        I = {p: p for p in points}
        h = {p: signed_permutation(h_perm, p) for p in points}
        assert all(h[h[p]] == p for p in points)
        for d in range(1, n + 1):
            q = n - d + 1
            for g_minus, g_plus in product(G, repeat=2):
                U = {p: signed_permutation(g_plus, p) if radius(p) >= q + 1 else p
                     for p in points}
                L = {p: signed_permutation(g_minus, p) if radius(p) >= q else p
                     for p in points}
                assert set(U.values()) == set(L.values()) == point_set
                U_inverse = {value: key for key, value in U.items()}
                K = {p: L[U_inverse[p]] for p in points}
                assert all(L[p] == K[U[p]] for p in points)

                # A={0}: the entire state space is this one constant state.
                constant = {p: 0 for p in points}
                assert {U[p]: value for p, value in constant.items()} == constant
                assert {L[p]: value for p, value in constant.items()} == constant
                singleton_cases += 1

                # For binary states with one 1-marker, outputs are precisely
                # {U(p)} and {L(p)}. Checking every marker proves faithfulness
                # for these finite carrier operators without enumerating 2^B.
                marker_equalities = [U[p] == L[p] for p in points]
                raw_marker_checks += len(points)
                assert all(marker_equalities) == (K == I)
                predicted_raw = g_minus == identity and (d == 1 or g_plus == identity)
                assert (K == I) == predicted_raw
                if K != I:
                    raw_nonidentity += 1

                global_h = K == I or K == h
                witness = quotient_witness(K, h, points)
                assert (witness is None) == global_h
                if witness is not None:
                    quotient_nonglobal += 1
                    quotient_one_marker += len(witness) == 1
                    quotient_two_marker += len(witness) == 2
                # Injective labels provide a sufficient fully rigid state.
                labelled = {p: i for i, p in enumerate(points)}
                KU = {K[p]: value for p, value in labelled.items()}
                HU = {h[p]: value for p, value in labelled.items()}
                assert (KU == labelled or KU == HU) == global_h
                cases += 1

    # Pin the exact known singleton counterexample and its binary separation.
    p = (1, -1, 0, 0)
    image = signed_permutation((0, 2, 1, 3), p)
    assert image == (-1, 0, 1, 0) != p
    print(json.dumps({
        "status": "PASS",
        "scope": "new alphabet/marker probe only; no formal disposition or CFD execution",
        "n_max": 2,
        "ball_sizes": ball_sizes,
        "carrier_path_cases": cases,
        "singleton_all_states_equal_cases": singleton_cases,
        "binary_one_marker_checks": raw_marker_checks,
        "raw_nonidentity_separated_cases": raw_nonidentity,
        "quotient_nonglobal_separated_cases": quotient_nonglobal,
        "quotient_one_marker_witnesses": quotient_one_marker,
        "quotient_two_marker_witnesses": quotient_two_marker,
        "singleton_counterexample_image": image,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
