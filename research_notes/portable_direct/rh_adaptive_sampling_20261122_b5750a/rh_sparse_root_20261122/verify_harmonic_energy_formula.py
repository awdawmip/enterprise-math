"""Exact finite checks of six harmonic moments and positive-support summation."""
from fractions import Fraction as F
from pathlib import Path
import itertools
import json


def moments(n, harmonic, harmonic2):
    h, h2 = harmonic[n], harmonic2[n]
    return (F(n), h, h2, (n + 1) * h - n,
            (h * h + h2) / 2,
            (n + 1) * h * h - (2 * n + 1) * h + 2 * n)


def positive_segment(left, right, a, b, c, harmonic):
    def value(n):
        return a * n + b - c * n * harmonic[n]
    if left > right:
        return None
    lo, hi = left, right
    while lo < hi:
        mid = (lo + hi) // 2
        if a - c * (harmonic[mid] + 1) <= 0:
            hi = mid
        else:
            lo = mid + 1
    peak = lo
    if value(peak) <= 0:
        return None
    lo, hi = left, peak
    while lo < hi:
        mid = (lo + hi) // 2
        if value(mid) > 0:
            hi = mid
        else:
            lo = mid + 1
    first = lo
    lo, hi = peak, right
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if value(mid) > 0:
            lo = mid
        else:
            hi = mid - 1
    return first, lo


def energy_from_moments(segment, a, b, c, harmonic, harmonic2):
    if segment is None:
        return F(0)
    left, right = segment
    before = moments(left - 1, harmonic, harmonic2)
    after = moments(right, harmonic, harmonic2)
    s0, s1, s2, t0, t1, t2 = [x - y for x, y in zip(after, before)]
    return (a*a*s0 + b*b*s2 + c*c*t2 + 2*a*b*s1
            - 2*a*c*t0 - 2*b*c*t1)


def main():
    nmax = 128
    h, h2 = [F(0)], [F(0)]
    for n in range(1, nmax + 1):
        h.append(h[-1] + F(1, n))
        h2.append(h2[-1] + F(1, n*n))
    direct = [F(0)] * 6
    for n in range(1, nmax + 1):
        terms = [F(1), F(1, n), F(1, n*n), h[n], h[n]/n, h[n]*h[n]]
        direct = [x+y for x, y in zip(direct, terms)]
        assert tuple(direct) == moments(n, h, h2)
    for n in range(1, nmax):
        assert (n+1)*h[n+1] - 2*n*h[n] + (n-1)*h[n-1] == F(1, n)
    parameters = itertools.product(
        [F(-4), F(0), F(1), F(2), F(4), F(9, 2), F(8)],
        [F(-16), F(-8), F(-1), F(0), F(1), F(16), F(64)],
        [F(1, 3), F(1), F(5, 2)])
    windows = [(1, 1), (1, 3), (1, 32), (1, 64), (2, 24), (17, 64)]
    cases = 0
    categories = {"empty": 0, "full": 0, "interior": 0, "one_boundary": 0}
    for a, b, c in parameters:
        for left, right in windows:
            segment = positive_segment(left, right, a, b, c, h)
            positives = [n for n in range(left, right+1)
                         if a*n+b-c*n*h[n] > 0]
            expected = None if not positives else (positives[0], positives[-1])
            assert segment == expected
            if positives:
                assert positives == list(range(positives[0], positives[-1]+1))
            direct_energy = sum(((a+b/n-c*h[n])**2 for n in positives), F(0))
            formula_energy = energy_from_moments(segment, a, b, c, h, h2)
            assert formula_energy == direct_energy
            assert formula_energy >= 0
            if segment is None:
                categories["empty"] += 1
            elif segment == (left, right):
                categories["full"] += 1
            elif segment[0] > left and segment[1] < right:
                categories["interior"] += 1
            else:
                categories["one_boundary"] += 1
            cases += 1
    assert all(categories.values())
    for a in range(2, 33):
        assert h2[4*a]-h2[a-1] <= F(1, a-1)
    result = {
        "status": "PASS",
        "arithmetic": "fractions.Fraction; no floating point or original road inputs",
        "harmonic_moment_prefixes": nmax,
        "potential_second_difference_checks": nmax-1,
        "positive_support_and_energy_cases": cases,
        "support_categories": categories,
        "rounded_sample_weight_checks": 31,
        "scope": "Finite implementation check; all-parameter identities proved by first differences in the accompanying note",
        "new_arithmetic_road_recomputation": False
    }
    target = Path(__file__).with_name("harmonic_energy_formula_certificate.json")
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
