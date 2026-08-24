#!/usr/bin/env python3
"""Check the q-by-q nearest-error graph covering under a new prime channel."""

from __future__ import annotations


def epsilon(j: int) -> int:
    return j & 1


def eta(j: int, chi: int) -> int:
    return (3 * j * j + chi * epsilon(j)) // 2


def word(M: int, k: int, R: int, c: int) -> tuple[int, ...]:
    chi = 1 if R % 2 == 0 else -1
    return tuple((c + 3 * R * j + eta(j, chi)) % M for j in range(k))


def params(M: int):
    U = M // 6
    return [(R, c) for R in range(2 * U) for c in range(M)]


def T_even(M: int, x: tuple[int, int]):
    R, c = x
    U = M // 6
    return ((R + U) % (2 * U), c)


def T_odd(M: int, x: tuple[int, int]):
    R, c = x
    U = M // 6
    chi = 1 if R % 2 == 0 else -1
    return ((R + U) % (2 * U), (c + chi - 3 * U) % M)


def reduce_param(N: int, M: int, x: tuple[int, int]):
    assert N % M == 0
    R, c = x
    U = M // 6
    return (R % (2 * U), c % M)


def even_cycles(M: int):
    V = set(params(M))
    adj = {x: (T_even(M, x), T_odd(M, x)) for x in V}
    seen = set()
    cycles = []
    for start in V:
        if start in seen:
            continue
        cycle = []
        prev = None
        cur = start
        while cur not in seen:
            seen.add(cur)
            cycle.append(cur)
            a, b = adj[cur]
            nxt = a if a != prev else b
            prev, cur = cur, nxt
        cycles.append(tuple(cycle))
    return cycles


def main() -> None:
    for M, q in ((6, 5), (30, 7), (210, 11)):
        N = M * q

        # Involution intertwining on all high parameters.
        for x in params(N):
            y = reduce_param(N, M, x)
            assert reduce_param(N, M, T_even(N, x)) == T_even(M, y)
            assert reduce_param(N, M, T_odd(N, x)) == T_odd(M, y)

        base_cycles = even_cycles(M)
        high_cycles = even_cycles(N)
        assert len(base_cycles) == M // 3
        assert len(high_cycles) == N // 3
        assert {len(c) for c in base_cycles} == {M}
        assert {len(c) for c in high_cycles} == {N}

        base_index = {}
        for idx, cycle in enumerate(base_cycles):
            for x in cycle:
                base_index[x] = idx

        over = {idx: [] for idx in range(len(base_cycles))}
        for cycle in high_cycles:
            image = [reduce_param(N, M, x) for x in cycle]
            targets = {base_index[x] for x in image}
            assert len(targets) == 1
            target = next(iter(targets))
            # The high Mq-cycle visits each base vertex exactly q times.
            counts = {}
            for x in image:
                counts[x] = counts.get(x, 0) + 1
            assert set(counts.values()) == {q}
            assert len(counts) == M
            over[target].append(cycle)

        assert {len(v) for v in over.values()} == {q}

        # Odd-k matching edges: exactly q^2 high edges over every base edge.
        base_edges = {
            tuple(sorted((x, T_even(M, x)))) for x in params(M)
        }
        high_counts = {e: 0 for e in base_edges}
        high_edges = {
            tuple(sorted((x, T_even(N, x)))) for x in params(N)
        }
        for x, y in high_edges:
            e = tuple(sorted((reduce_param(N, M, x), reduce_param(N, M, y))))
            high_counts[e] += 1
        assert set(high_counts.values()) == {q * q}

    print("GENERIC_CHANNEL_INVOLUTIONS_COMMUTE_WITH_REDUCTION=PASS")
    print("EVEN_K_HIGH_CYCLES_PER_BASE=q")
    print("EVEN_K_COVERING_DEGREE=q")
    print("ODD_K_MATCHING_EDGES_PER_BASE=q^2")
    print("GENERIC_CHANNEL_GRAPH_LIFT=q_BY_q")


if __name__ == "__main__":
    main()
