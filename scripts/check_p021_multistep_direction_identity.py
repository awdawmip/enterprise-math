#!/usr/bin/env python3
"""Exact finite regression for P021 multistep canonical direction identity.

This checker supports the symbolic proof in the research return. It verifies:
1. normalized one-step unique-identity supports through n=4;
2. the pair theorem exhaustively through n=4;
3. the three-step theorem exhaustively through n=3;
4. the minimal 2-class/2-step cross-time counterexample;
5. two fine witness refinements with identical one-step supports but different
   exact endpoint identity outcomes.
"""

from __future__ import annotations

import itertools
from collections import deque


Matrix = tuple[tuple[int, ...], ...]


def identity_matrix(n: int) -> Matrix:
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def support_from_off_diagonal_bits(n: int, bits: int) -> Matrix:
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        out[i][i] = 1
    k = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            out[i][j] = (bits >> k) & 1
            k += 1
    return tuple(tuple(row) for row in out)


def perfect_matchings(s: Matrix) -> list[tuple[int, ...]]:
    n = len(s)
    return [
        p
        for p in itertools.permutations(range(n))
        if all(s[i][p[i]] for i in range(n))
    ]


def unique_identity_supports(n: int) -> list[Matrix]:
    identity = tuple(range(n))
    return [
        s
        for bits in range(1 << (n * (n - 1)))
        if perfect_matchings(
            s := support_from_off_diagonal_bits(n, bits)
        )
        == [identity]
    ]


def boolean_product(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(
        tuple(
            int(any(a[i][k] and b[k][j] for k in range(n)))
            for j in range(n)
        )
        for i in range(n)
    )


def boolean_product_many(mats: tuple[Matrix, ...]) -> Matrix:
    out = identity_matrix(len(mats[0]))
    for m in mats:
        out = boolean_product(out, m)
    return out


def ambiguity_edges(s: Matrix) -> set[tuple[int, int]]:
    n = len(s)
    return {
        (i, j)
        for i in range(n)
        for j in range(n)
        if i != j and s[i][j]
    }


def is_acyclic(n: int, edges: set[tuple[int, int]]) -> bool:
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for i, j in edges:
        adj[i].append(j)
        indeg[j] += 1
    queue = deque(i for i, d in enumerate(indeg) if d == 0)
    seen = 0
    while queue:
        i = queue.popleft()
        seen += 1
        for j in adj[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                queue.append(j)
    return seen == n


def transitive_closure(
    n: int, edges: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    reach = [[False] * n for _ in range(n)]
    for i, j in edges:
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return {
        (i, j)
        for i in range(n)
        for j in range(n)
        if i != j and reach[i][j]
    }


def exact_two_step_support(
    left_tokens: dict[tuple[int, int], frozenset[str]],
    right_tokens: dict[tuple[int, int], frozenset[str]],
    n: int,
) -> Matrix:
    """Join through the same middle-class witness token."""
    return tuple(
        tuple(
            int(
                any(
                    left_tokens.get((i, j), frozenset())
                    & right_tokens.get((j, k), frozenset())
                    for j in range(n)
                )
            )
            for k in range(n)
        )
        for i in range(n)
    )


def support_of_left_tokens(
    tokens: dict[tuple[int, int], frozenset[str]], n: int
) -> Matrix:
    return tuple(
        tuple(int(bool(tokens.get((i, j), frozenset()))) for j in range(n))
        for i in range(n)
    )


def support_of_right_tokens(
    tokens: dict[tuple[int, int], frozenset[str]], n: int
) -> Matrix:
    return tuple(
        tuple(int(bool(tokens.get((j, k), frozenset()))) for k in range(n))
        for j in range(n)
    )


def main() -> None:
    identity_counts = {}
    pair_stats = {}
    triple_stats = {}

    supports_by_n = {
        n: unique_identity_supports(n)
        for n in range(1, 5)
    }
    identity_counts = {
        n: len(supports_by_n[n])
        for n in range(1, 5)
    }
    assert identity_counts == {1: 1, 2: 3, 3: 25, 4: 543}

    for n, supports in supports_by_n.items():
        identity = tuple(range(n))
        assert all(
            is_acyclic(n, ambiguity_edges(s))
            for s in supports
        )

        safe = unsafe = 0
        for a in supports:
            for b in supports:
                product = boolean_product(a, b)
                union = ambiguity_edges(a) | ambiguity_edges(b)
                unique = perfect_matchings(product) == [identity]
                common_order = is_acyclic(n, union)
                assert unique == common_order

                product_edges = ambiguity_edges(product)
                assert union <= product_edges
                assert product_edges <= transitive_closure(n, union)

                safe += int(unique)
                unsafe += int(not unique)

        pair_stats[n] = (len(supports) ** 2, safe, unsafe)

    assert pair_stats == {
        1: (1, 1, 0),
        2: (9, 7, 2),
        3: (625, 289, 336),
        4: (294849, 63487, 231362),
    }

    for n in range(1, 4):
        supports = supports_by_n[n]
        identity = tuple(range(n))
        safe = unsafe = 0
        for mats in itertools.product(supports, repeat=3):
            product = boolean_product_many(mats)
            union = set().union(*(ambiguity_edges(m) for m in mats))
            unique = perfect_matchings(product) == [identity]
            common_order = is_acyclic(n, union)
            assert unique == common_order

            product_edges = ambiguity_edges(product)
            assert union <= product_edges
            assert product_edges <= transitive_closure(n, union)

            safe += int(unique)
            unsafe += int(not unique)

        triple_stats[n] = (len(supports) ** 3, safe, unsafe)

    assert triple_stats == {
        1: (1, 1, 0),
        2: (27, 15, 12),
        3: (15625, 2689, 12936),
    }

    # Minimal 2-class / 2-step cross-time cycle.
    a = ((1, 1), (0, 1))
    b = ((1, 0), (1, 1))
    full = ((1, 1), (1, 1))
    identity2 = ((1, 0), (0, 1))
    assert perfect_matchings(a) == [(0, 1)]
    assert perfect_matchings(b) == [(0, 1)]
    assert boolean_product(a, b) == full
    assert len(perfect_matchings(full)) == 2
    assert not is_acyclic(2, ambiguity_edges(a) | ambiguity_edges(b))

    # Same one-step class supports, two different fine witness refinements.
    saturated_left = {
        (0, 0): frozenset({"t0"}),
        (0, 1): frozenset({"t1"}),
        (1, 1): frozenset({"t1"}),
    }
    saturated_right = {
        (0, 0): frozenset({"t0"}),
        (1, 0): frozenset({"t1"}),
        (1, 1): frozenset({"t1"}),
    }
    filtered_left = {
        (0, 0): frozenset({"d0"}),
        (0, 1): frozenset({"lin"}),
        (1, 1): frozenset({"d1"}),
    }
    filtered_right = {
        (0, 0): frozenset({"d0"}),
        (1, 0): frozenset({"rout"}),
        (1, 1): frozenset({"d1"}),
    }

    for left, right in (
        (saturated_left, saturated_right),
        (filtered_left, filtered_right),
    ):
        assert support_of_left_tokens(left, 2) == a
        assert support_of_right_tokens(right, 2) == b
        # Canonical diagonal chains remain actually realizable.
        assert left[(0, 0)] & right[(0, 0)]
        assert left[(1, 1)] & right[(1, 1)]

    saturated_endpoint = exact_two_step_support(
        saturated_left, saturated_right, 2
    )
    filtered_endpoint = exact_two_step_support(
        filtered_left, filtered_right, 2
    )
    assert saturated_endpoint == full
    assert filtered_endpoint == identity2
    assert len(perfect_matchings(saturated_endpoint)) == 2
    assert perfect_matchings(filtered_endpoint) == [(0, 1)]

    print("P021 multistep direction-identity regression: PASS")
    print(f"unique_identity_support_counts={identity_counts}")
    print(f"pair_common_order_census={pair_stats}")
    print(f"triple_common_order_census={triple_stats}")
    print("minimal_cross_time_cycle=n2_h2")
    print("same_support_fine_refinements=SATURATED_AMBIGUOUS_vs_FILTERED_UNIQUE")
    print("terminal_class=P021_MULTISTEP_DIRECTION_IDENTITY_COMMON_ORDER_EXACT")


if __name__ == "__main__":
    main()
