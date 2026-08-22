#!/usr/bin/env python3
"""Executable regression for RS-QRF-R1-INDEPENDENT-FOUNDATION-VERIFICATION.

The theorem-level argument is in QRF_R1_INDEPENDENT_FOUNDATION_VERIFICATION_20260822.md.
This script only checks finite witnesses/regressions with exact integer arithmetic.
"""


def iroot_floor(n: int, p: int) -> int:
    lo, hi = 0, 1
    while hi ** p <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** p <= n:
            lo = mid
        else:
            hi = mid
    return lo


def S(p: int, n: int) -> int:
    return n ** p


def R(p: int, N: int) -> int:
    return iroot_floor(N, p)


def fiber_rank_detail(p: int, N: int, d: int) -> int:
    k = R(p, N)
    width = S(p, k + 1) - S(p, k)
    rank = N - S(p, k)
    return (d * rank) // width


def scale_equivariant_detail(p: int, N: int, d: int) -> int:
    return R(p, N * S(p, d)) - d * R(p, N)


def first_fiber(p: int):
    return range(1, 2 ** p)


def main() -> None:
    # Literal-premise countermodel: rank refinement is tight for every tested p.
    for p in range(2, 13):
        W = 2 ** p - 1
        rank_labels = [fiber_rank_detail(p, N, W) for N in first_fiber(p)]
        assert rank_labels == list(range(W)), (p, rank_labels)

    # Natural scale-equivariant repair: p=2 is tight; p>=3 fails in regression range.
    rows = []
    for p in range(2, 13):
        W = 2 ** p - 1
        labels = [scale_equivariant_detail(p, N, W) for N in first_fiber(p)]
        image_size = len(set(labels))
        rows.append((p, W, image_size, image_size == W))

    assert rows[0] == (2, 3, 3, True)
    assert all(not tight for p, W, image_size, tight in rows[1:])

    # Exact p=3 collision used in the proof.
    assert scale_equivariant_detail(3, 4, 7) == 4
    assert scale_equivariant_detail(3, 5, 7) == 4

    print("p  W     image(scale)  tight")
    for p, W, image_size, tight in rows:
        print(f"{p:<2} {W:<5} {image_size:<13} {tight}")


if __name__ == "__main__":
    main()
