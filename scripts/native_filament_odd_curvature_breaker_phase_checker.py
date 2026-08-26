#!/usr/bin/env python3
"""Exact checker for the odd-curvature universal-breaker phase diagram mod 60."""

from __future__ import annotations


def eps(n: int) -> int:
    return n & 1


def F(B: int, H: int, r: int) -> int:
    return H + (B * r * r + eps(r)) // 2


def legendre(a: int, q: int) -> int:
    a %= q
    if a == 0:
        return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1


def transparent_classes(B: int, q: int) -> list[int]:
    period = 2 * q if q > 2 else 4
    out = []
    for H in range(q):
        if all(F(B, H, r) % q != 0 for r in range(period)):
            out.append(H)
    return out


def max_nonzero_run(B: int, H: int, q: int) -> int | None:
    period = 2 * q if q > 2 else 2
    seq = [F(B, H, r) % q for r in range(period)]
    if all(x != 0 for x in seq):
        return None
    cur = best = 0
    for x in seq * 2:
        if x != 0:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return min(best, period - 1)


def breaker_set(B: int) -> set[int]:
    out = set()
    if B % 4 == 1:
        out.add(2)
    if B % 3 != 0:
        out.add(3)
    if B % 5 != 0 and legendre(B, 5) == -1:
        out.add(5)
    return out


def main() -> None:
    # Direct transparency replay for B representatives modulo60.
    for B in range(1, 60, 2):
        predicted = breaker_set(B)
        observed = {
            q for q in (2, 3, 5, 7, 11, 13, 17, 19)
            if not transparent_classes(B, q)
        }
        assert observed == predicted, (B, predicted, observed)

    first2 = []
    first3 = []
    first5 = []
    none = []
    for B in range(1, 60, 2):
        bs = breaker_set(B)
        if 2 in bs:
            first2.append(B)
        elif 3 in bs:
            first3.append(B)
        elif 5 in bs:
            first5.append(B)
        else:
            none.append(B)

    assert first2 == [1,5,9,13,17,21,25,29,33,37,41,45,49,53,57]
    assert first3 == [7,11,19,23,31,35,43,47,55,59]
    assert first5 == [3,27]
    assert none == [15,39,51]

    # Sharp caps of the first-breaker channels.
    # q=2 breaker phase: alternating zero/nonzero, cap1.
    for B in first2:
        assert max(max_nonzero_run(B, H, 2) for H in range(2)) == 1

    # q=3 first-breaker phase: exact cap5=2q-1.
    for B in first3:
        runs = [max_nonzero_run(B, H, 3) for H in range(3)]
        assert all(r is not None for r in runs)
        assert max(runs) == 5

    # q=5 first-breaker phase: exact cap9=2q-1.
    for B in first5:
        runs = [max_nonzero_run(B, H, 5) for H in range(5)]
        assert all(r is not None for r in runs)
        assert max(runs) == 9
        assert max_nonzero_run(B, 0, 5) == 9
        assert max_nonzero_run(B, 2, 5) == 9

    # Native B=3 is the smallest positive odd coefficient whose first breaker is5.
    assert first5[0] == 3

    print("BREAKER_SET_FORMULA=PASS")
    print("FIRST_BREAKER_MOD60_COUNTS=15,10,2,3")
    print("FIRST_BREAKER_5_CLASSES={3,27}")
    print("NO_BREAKER_CLASSES={15,39,51}")
    print("SHARP_CAPS_Q2_Q3_Q5=1,5,9")
    print("NATIVE_B3=MINIMAL_FIRST_BREAKER_5")


if __name__ == "__main__":
    main()
