#!/usr/bin/env python3
"""R749SUU: exact square-plus-one Q=+1 optimizer verification.

No external dependencies. All operations use exact Python integers.
This script checks the stated finite domains, not mathematical acceptance.
"""
from math import isqrt


def score(x: int, y: int):
    if x < 2 or y < x:
        return None
    n = x * y
    if n - x - y < 1:
        return None
    return (n - 1) * (n - x - 1) * (n - y - 1)


def closed_form(t: int):
    assert t >= 3
    if t & 1:
        d = isqrt(4 * t - 3)
        if d * d == 4 * t - 3 and (d - 1) % 2 == 0:
            r = (d - 1) // 2
            if r >= 1 and r * (r + 1) + 1 == t:
                return t - r, t + r + 1
    else:
        k = isqrt(t // 2)
        if k >= 2 and 2 * k * k == t:
            return t - 2 * k + 1, t + 2 * k + 1
    return t, t


def endpoint_oracle(t: int):
    """Complete x scan; at fixed x the score increases strictly with y."""
    b = t * t + 1
    best = -1
    pairs = []
    for x in range(2, isqrt(b) + 1):
        y = b // x
        value = score(x, y)
        if value is None:
            continue
        if value > best:
            best, pairs = value, [(x, y)]
        elif value == best:
            pairs.append((x, y))
    return best, pairs


def exhaustive_oracle(t: int):
    """Independent complete (x,y) search; no endpoint reduction."""
    b = t * t + 1
    best = -1
    pairs = []
    for x in range(2, isqrt(b) + 1):
        for y in range(x, b // x + 1):
            value = score(x, y)
            if value is None:
                continue
            if value > best:
                best, pairs = value, [(x, y)]
            elif value == best:
                pairs.append((x, y))
    return best, pairs


def count_formula(t_max: int):
    if t_max < 3:
        return 0
    return (isqrt(4 * t_max - 3) - 1) // 2 + isqrt(t_max // 2) - 1


def test_polynomial_identities():
    for t in range(3, 100):
        s = (t * t - 1) * (t * t - t - 1) ** 2
        b = t * t + 1
        at = lambda j: (b - 1) * ((b - 1) ** 2 - (b - 1) * (2 * t + j) + b)
        assert at(1) - s == (t - 1) * (2 * t**3 - 2 * t**2 - 3 * t - 1)
        assert at(2) - s == t**4 - 4 * t**3 - t**2 + 2 * t + 1
        assert s - at(3) == 4 * t**3 + t**2 - 2 * t - 1
        assert s - at(4) == t**4 + 4 * t**3 + t**2 - 2 * t - 1


def run():
    test_polynomial_identities()
    complete_count = 0
    for t in range(3, 71):
        expected = closed_form(t)
        exact = exhaustive_oracle(t)
        assert exact == (score(*expected), [expected]), (t, exact, expected)
        complete_count += 1

    endpoint_count = 0
    gap0 = 0
    for t in range(3, 2201):
        x, y = closed_form(t)
        assert 2 <= x <= y and score(x, y) is not None
        assert endpoint_oracle(t) == (score(x, y), [(x, y)]), t
        gap = t * t + 1 - x * y
        assert gap in (0, 1)
        if gap == 0:
            gap0 += 1
        endpoint_count += 1

    assert gap0 == count_formula(2200) == 78
    assert count_formula(2200) == 46 + 32
    examples = {3: 252, 5: 8664, 7: 84084, 8: 192576,
                13: 4084392, 18: 30128436, 21: 77598360}
    for t, target in examples.items():
        assert score(*closed_form(t)) == target
    print("PASS R749SUU")
    print("all-pair exhaustive: t=3..70, inputs=", complete_count)
    print("independent endpoint: t=3..2200, inputs=", endpoint_count)
    print("zero gap count through 2200=", gap0, "(46 odd, 32 even)")


if __name__ == "__main__":
    run()
