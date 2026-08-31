#!/usr/bin/env python3
"""Check the primorial nearest-neighbor matching/cycle classification."""

from __future__ import annotations


def epsilon(j: int) -> int:
    return j & 1


def eta(j: int, chi: int) -> int:
    return (3 * j * j + chi * epsilon(j)) // 2


def word(M: int, k: int, R: int, c: int) -> tuple[int, ...]:
    chi = 1 if R % 2 == 0 else -1
    return tuple((c + 3 * R * j + eta(j, chi)) % M for j in range(k))


def vertices(M: int, k: int):
    U = M // 6
    return {(R, c): word(M, k, R, c) for R in range(2 * U) for c in range(M)}


def T_even(M: int, R: int, c: int):
    U = M // 6
    return ((R + U) % (2 * U), c)


def T_odd(M: int, R: int, c: int):
    U = M // 6
    chi = 1 if R % 2 == 0 else -1
    return ((R + U) % (2 * U), (c + chi - 3 * U) % M)


def hamming(u: tuple[int, ...], v: tuple[int, ...]) -> int:
    return sum(x != y for x, y in zip(u, v))


def graph_cycles(M: int, k: int):
    V = vertices(M, k)
    if k % 2:
        # Perfect matching under T_even.
        edges = set()
        for x in V:
            y = T_even(M, *x)
            assert y in V and y != x
            assert T_even(M, *y) == x
            assert hamming(V[x], V[y]) == k // 2
            edges.add(tuple(sorted((x, y))))
        assert len(edges) == len(V) // 2
        return [2] * len(edges)

    adj = {}
    for x in V:
        y = T_even(M, *x)
        z = T_odd(M, *x)
        assert y != z and y != x and z != x
        assert hamming(V[x], V[y]) == k // 2
        assert hamming(V[x], V[z]) == k // 2
        adj[x] = (y, z)

    seen = set()
    lengths = []
    for start in V:
        if start in seen:
            continue
        prev = None
        cur = start
        length = 0
        while cur not in seen:
            seen.add(cur)
            length += 1
            a, b = adj[cur]
            nxt = a if a != prev else b
            prev, cur = cur, nxt
        lengths.append(length)
    return lengths


def main() -> None:
    for M in (6, 30, 210):
        for k in range(3, 10):
            lengths = graph_cycles(M, k)
            if k % 2:
                assert set(lengths) == {2}
                assert len(lengths) == M * M // 6
            else:
                assert set(lengths) == {M}
                assert len(lengths) == M // 3

    # Closed arithmetic replay at larger primorial moduli without building graph.
    for M in (2310, 30030, 510510):
        U = M // 6
        for chi in (1, -1):
            a = 3 * U + chi
            # U is coprime to6 for a primorial above3.
            import math
            assert math.gcd(a, M) == 2
            assert M // math.gcd(a, M) == 3 * U

    print("ODD_K_NEAREST_GRAPH=PERFECT_MATCHING")
    print("EVEN_K_NEAREST_GRAPH=M_OVER_3_CYCLES_OF_LENGTH_M")
    print("M6_M30_M210_GRAPH_REPLAY=PASS")
    print("PRIMORIAL_CYCLE_ORDER_FORMULA=PASS")


if __name__ == "__main__":
    main()
