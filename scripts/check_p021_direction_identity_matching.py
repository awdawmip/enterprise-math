#!/usr/bin/env python3
"""Exact finite regression for the P021 support-matching semantic correction.

The proof in the research return is symbolic. This checker only:
1. freezes the minimal 2x2 counterexample to "permutation support is necessary";
2. exhausts all square boolean supports through n=4;
3. verifies the perfect-matching / alternating-cycle uniqueness criterion;
4. verifies the bipartite matching-deficiency (Hall-defect) identity;
5. checks the strict upper-triangular unique-matching family through n=8.

No CAS or external package is used.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass


def support_from_bits(n: int, bits: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple((bits >> (i * n + j)) & 1 for j in range(n))
        for i in range(n)
    )


def is_permutation_support(s: tuple[tuple[int, ...], ...]) -> bool:
    n = len(s)
    return (
        all(sum(row) == 1 for row in s)
        and all(sum(s[i][j] for i in range(n)) == 1 for j in range(n))
    )


def perfect_matchings(s: tuple[tuple[int, ...], ...]) -> list[tuple[int, ...]]:
    n = len(s)
    return [
        p for p in itertools.permutations(range(n))
        if all(s[i][p[i]] for i in range(n))
    ]


def maximum_matching_size(s: tuple[tuple[int, ...], ...]) -> int:
    n = len(s)
    match_right = [-1] * n

    def augment(i: int, seen: list[bool]) -> bool:
        for j in range(n):
            if not s[i][j] or seen[j]:
                continue
            seen[j] = True
            if match_right[j] == -1 or augment(match_right[j], seen):
                match_right[j] = i
                return True
        return False

    matched = 0
    for i in range(n):
        if augment(i, [False] * n):
            matched += 1
    return matched


def hall_defect(s: tuple[tuple[int, ...], ...]) -> int:
    n = len(s)
    best = 0
    for mask in range(1 << n):
        rows = [i for i in range(n) if (mask >> i) & 1]
        nbrs = {
            j
            for i in rows
            for j in range(n)
            if s[i][j]
        }
        best = max(best, len(rows) - len(nbrs))
    return best


def has_alternating_cycle(
    s: tuple[tuple[int, ...], ...],
    matching: tuple[int, ...],
) -> bool:
    """Detect an M-alternating cycle through the induced digraph on left vertices.

    For every non-matching support edge i--matching[k], add directed edge i -> k.
    A directed cycle is exactly an M-alternating cycle.
    """
    n = len(s)
    inverse = [0] * n
    for i, j in enumerate(matching):
        inverse[j] = i

    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] and j != matching[i]:
                adj[i].append(inverse[j])

    state = [0] * n

    def visit(v: int) -> bool:
        state[v] = 1
        for w in adj[v]:
            if state[w] == 1:
                return True
            if state[w] == 0 and visit(w):
                return True
        state[v] = 2
        return False

    return any(state[v] == 0 and visit(v) for v in range(n))


@dataclass(frozen=True)
class Census:
    n: int
    total: int
    no_perfect_matching: int
    unique_perfect_matching: int
    multiple_perfect_matchings: int
    permutation_support: int


def census(n: int) -> Census:
    no_pm = unique = multiple = permutation = 0
    for bits in range(1 << (n * n)):
        s = support_from_bits(n, bits)
        matchings = perfect_matchings(s)

        if not matchings:
            no_pm += 1
        elif len(matchings) == 1:
            unique += 1
        else:
            multiple += 1

        if is_permutation_support(s):
            permutation += 1

        # Exact Hall-defect identity: n - nu(S) = max_A(|A|-|N(A)|).
        assert n - maximum_matching_size(s) == hall_defect(s)

        # If M exists, uniqueness iff there is no M-alternating cycle.
        if matchings:
            assert (len(matchings) == 1) == (
                not has_alternating_cycle(s, matchings[0])
            )

        # Historical condition remains sufficient, but not necessary.
        if is_permutation_support(s):
            assert len(matchings) == 1

    return Census(
        n=n,
        total=1 << (n * n),
        no_perfect_matching=no_pm,
        unique_perfect_matching=unique,
        multiple_perfect_matchings=multiple,
        permutation_support=permutation,
    )


def upper_triangular_support(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(int(i <= j) for j in range(n))
        for i in range(n)
    )


def main() -> None:
    minimal = ((1, 1), (0, 1))
    assert not is_permutation_support(minimal)
    assert perfect_matchings(minimal) == [(0, 1)]

    censuses = [census(n) for n in range(1, 5)]
    expected = [
        Census(1, 2, 1, 1, 0, 1),
        Census(2, 16, 9, 6, 1, 2),
        Census(3, 512, 265, 150, 97, 6),
        Census(4, 65536, 27713, 13032, 24791, 24),
    ]
    assert censuses == expected

    for n in range(2, 9):
        tri = upper_triangular_support(n)
        assert not is_permutation_support(tri)
        assert perfect_matchings(tri) == [tuple(range(n))]

    print("P021 direction-identity matching regression: PASS")
    for c in censuses:
        print(
            f"n={c.n}: total={c.total}, no_pm={c.no_perfect_matching}, "
            f"unique_pm={c.unique_perfect_matching}, "
            f"multiple_pm={c.multiple_perfect_matchings}, "
            f"permutation_support={c.permutation_support}"
        )
    print("minimal_nonpermutation_unique_pm=((1,1),(0,1))")
    print("upper_triangular_unique_pm_checked=2..8")
    print("hall_defect_identity_checked=all_supports_n<=4")
    print("alternating_cycle_uniqueness_checked=all_supports_with_pm_n<=4")


if __name__ == "__main__":
    main()
