"""R027 exact finite mutation/oracle gate.

This is regression/debug evidence only. It is not a substitute for the Lean proof in
EnterpriseMath/Precision/PowerBRCTrichotomy.lean.
"""

from __future__ import annotations


def int_root(p: int, n: int) -> int:
    if p < 1 or n < 0:
        raise ValueError("expected p>=1 and n>=0")
    lo, hi = 0, 1
    while hi**p <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**p <= n:
            lo = mid
        else:
            hi = mid
    return lo


def aligned(p: int, r: int) -> bool:
    a = int_root(p, r)
    return a**p == r


def regime(p: int, r: int) -> str:
    if p < 2 or r < 1:
        raise ValueError("classifier domain is p>=2, r>=1")
    if aligned(p, r):
        return "ALIGNED"
    if r < 2**p:
        return "FUNNEL"
    if 2**p < r:
        return "BINARY"
    raise AssertionError("r=2^p must have been classified ALIGNED")


def child_roots(p: int, r: int, k: int) -> tuple[int, ...]:
    n = r * k**p
    m = int_root(p, n)
    return (m,) if m**p == n else (m, m + 1)


def child_support(p: int, r: int, support: set[int]) -> set[int]:
    out: set[int] = set()
    for k in support:
        out.update(child_roots(p, r, k))
    return out


def run_oracle() -> None:
    # Required aligned boundary coverage.
    for p in range(2, 8):
        assert regime(p, 1) == "ALIGNED"
        assert regime(p, 2**p) == "ALIGNED"
    assert regime(2, 9) == "ALIGNED"

    # Required funnel examples.
    for r in (2, 3):
        assert regime(2, r) == "FUNNEL"
    for r in range(2, 8):
        assert regime(3, r) == "FUNNEL"

    # Required binary examples, excluding aligned squares.
    for r in (5, 6, 7, 8, 10):
        if not aligned(2, r):
            assert regime(2, r) == "BINARY"

    # Zero-support mutation: k=0 is exact and cannot satisfy blanket doubling.
    assert child_support(2, 5, {0}) == {0}
    assert len(child_support(2, 5, {0})) != 2

    # Funnel mutation: this layer has spacing 2 throughout the finite window,
    # so there is no duplicate collision even though the no-hole interval law holds.
    assert child_support(2, 3, {1, 2}) == {1, 2, 3, 4}
    assert len(child_support(2, 3, {1, 2})) == 4

    # Broader bounded regression for the two local spacing laws.
    for p in range(2, 8):
        for r in range(2, 2**p):
            for k in range(80):
                m = int_root(p, r * k**p)
                m_next = int_root(p, r * (k + 1) ** p)
                assert m + 1 <= m_next <= m + 2

        for r in range(2**p + 1, 2**p + 40):
            if aligned(p, r):
                continue
            for k in range(1, 80):
                m = int_root(p, r * k**p)
                m_next = int_root(p, r * (k + 1) ** p)
                assert m + 2 <= m_next
            for support in ({1}, {1, 2}, {2, 5, 9}, set(range(1, 20))):
                assert len(child_support(p, r, support)) == 2 * len(support)


if __name__ == "__main__":
    run_oracle()
    print("R027 oracle PASS")
