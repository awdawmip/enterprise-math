#!/usr/bin/env python3
"""Exact scoped R063 -> signed-X6 fixed-two-axis lift, not full X6 shell.

Scientific inputs: X6 frozen pin 59538f585d037d09ef687b28715c4bc1a3f9fe03
and active R063 original positive component-root list. No external package.
"""
from math import comb, isqrt


def positive_pairs(r: int) -> tuple[tuple[int, int], ...]:
    assert isinstance(r, int) and r >= 1
    pairs = []
    for a in range(r + 1):
        b2 = r * r - a * a
        b = isqrt(b2)
        if b * b == b2:
            pairs.append((a, b))
    return tuple(pairs)


def sign_fiber(a: int, b: int) -> set[tuple[int, int]]:
    return {(sa * a, sb * b) for sa in (-1, 1) for sb in (-1, 1)}


def shortest_word_count(x: int, y: int) -> int:
    """Pinned signed BRC shortest-event multinomial, restricted to two axes."""
    return comb(abs(x) + abs(y), abs(x))


def check_radius(r: int) -> tuple[int, int, int]:
    roots = positive_pairs(r)
    signed = set().union(*(sign_fiber(a, b) for a, b in roots))
    predicted_endpoints = sum(2 ** (int(a != 0) + int(b != 0))
                              for a, b in roots)
    predicted_words = sum(
        2 ** (int(a != 0) + int(b != 0)) * comb(a + b, a)
        for a, b in roots
    )
    observed_words = sum(shortest_word_count(x, y) for x, y in signed)
    assert len(signed) == predicted_endpoints, (r, "endpoint fibers")
    assert observed_words == predicted_words, (r, "BRC words")
    assert all(x * x + y * y == r * r for x, y in signed)
    assert all((-x, -y) in signed for x, y in signed)
    assert all(shortest_word_count(x, y) == shortest_word_count(-x, -y)
               for x, y in signed)
    return len(roots), len(signed), observed_words


def main() -> None:
    # Fully enumerated finite regression, exact integers only.
    checked = [check_radius(r) for r in range(1, 101)]
    roots_50 = positive_pairs(50)
    assert roots_50 == (
        (0, 50), (14, 48), (30, 40),
        (40, 30), (48, 14), (50, 0),
    )
    assert comb(62, 14) == 29078984349975
    assert comb(70, 30) == 55347740058143507128
    # R063 positive two-generator observer mass (not signed native shell).
    positive_50 = sum(comb(a + b, a) for a, b in roots_50)
    assert positive_50 == 110695538274255714208
    assert checked[49] == (6, 20, 442782153097022856828)
    assert len(sign_fiber(0, 50)) == 2
    assert len(sign_fiber(14, 48)) == 4
    print("PASS X6_R063_SIGNED_TWO_AXIS_LIFT: "
          "radii=100 r50_positive_roots=6 r50_signed_endpoints=20 "
          "r50_R063_positive_words=110695538274255714208 "
          "r50_signed_shortest_words=442782153097022856828")


if __name__ == "__main__":
    main()
