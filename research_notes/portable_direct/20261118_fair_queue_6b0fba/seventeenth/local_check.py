"""Integer census of short witness directions at kappa=1/sqrt(42)."""
import json
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt, pi


def strict_cutoff(p):
    n = 0
    while 42**3 * (n + 1)**3 < p**5:
        n += 1
    return n


def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def mobius(n):
    result = 1
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            n //= k
            if n % k == 0:
                return 0
            result = -result
    return -result if n > 1 else result


def ball_count(dimension, cutoff):
    counts = [1] + [0] * cutoff
    for _ in range(dimension):
        following = counts.copy()
        for coordinate in range(1, isqrt(cutoff) + 1):
            square = coordinate**2
            for n in range(square, cutoff + 1):
                following[n] += 2 * counts[n - square]
        counts = following
    return sum(counts) - 1


def primitive_pairs(dimension, cutoff):
    signed = sum(mobius(t) * ball_count(dimension, cutoff // t**2)
                 for t in range(1, isqrt(cutoff) + 1))
    assert signed % 2 == 0
    return signed // 2


def projective(v, p):
    pivot = next(x for x in v if x % p)
    return tuple(x * pow(pivot, -1, p) % p for x in v)


def plane_counts(p, cutoff):
    hits = {}
    for x in range(isqrt(cutoff) + 1):
        ymax = isqrt(cutoff - x*x)
        for y in range(-ymax, ymax + 1):
            if (x == 0 and y <= 0) or gcd(x, y) != 1:
                continue
            hits.setdefault(projective((x, y), p), []).append((x, y))
    assert sum(map(len, hits.values())) == primitive_pairs(2, cutoff)
    return hits


def direct_six(p, cutoff):
    counts = Counter()

    def visit(v, budget):
        if len(v) == 6:
            if gcd(*v) == 1 and next(x for x in v if x) > 0:
                counts[projective(v, p)] += 1
            return
        for x in range(-isqrt(budget), isqrt(budget) + 1):
            visit(v + (x,), budget - x*x)

    visit((), cutoff)
    return len(counts), sum(n*(n-1) for n in counts.values())


def census(p):
    assert p**4 <= 8 * 42**6  # R^2 <= sqrt(2)*p
    cutoff = strict_cutoff(p)
    plane = plane_counts(p, cutoff)
    repeated = sorted(group for group in plane.values() if len(group) > 1)
    for group in repeated:
        for i, (x, y) in enumerate(group):
            for u, v in group[i + 1:]:
                assert abs(x*v - y*u) == p
    primitive = primitive_pairs(6, cutoff)
    excess = 15 * sum(len(group)-1 for group in repeated)
    ordered = 15 * sum(len(group)*(len(group)-1) for group in repeated)
    hit = primitive - excess
    if p <= 59:
        assert direct_six(p, cutoff) == (hit, ordered)
    if p*p <= 42**3:
        assert excess == 0
    return dict(p=p, max_squared_norm=cutoff, primitive_pairs=primitive,
                hit_lines=hit, primitive_excess=excess, ordered_collisions=ordered,
                plane_multiplicities=dict(sorted(Counter(map(len, repeated)).items())),
                first_plane_witness=repeated[0] if repeated else None,
                seed_count=(p**6 - 1)//(p-1))


def main():
    rows = [census(p) for p in range(2, 1000)
            if p % 7 in (3, 5) and prime(p) and p**4 <= 8 * 42**6]
    indexed = {r['p']:r['hit_lines'] for r in rows}
    for p, hits in {17:36, 31:1144, 59:24572, 73:71136, 101:368864}.items():
        assert indexed[p] == hits
    # zeta(6)=pi^6/945. The interval is analytical; decimals are a display.
    alpha = 945 / (12*pi**3*42**3)
    lower = max(alpha/(1+alpha), alpha - alpha*alpha/2)
    theta_upper = sum(float(density)*m*alpha/(1-m*alpha)
                      for density, m in [(Fraction(1,6),1),(Fraction(1,3),2),(Fraction(1,3),5)])
    return dict(population="all inert primes in the coordinate-plane regime",
                penultimate_strict_cutoff="42^3 Q^3 < p^5",
                first_inert_collision=next(r['p'] for r in rows if r['primitive_excess']),
                last_tested_prime=rows[-1]['p'], analytical_decimal_values={
                    'alpha':alpha, 'b_lower':lower, 'theta_lower_certified':lower/(3*(1-lower)),
                    'theta_upper':theta_upper, 'window_upper_endpoint':0.25-theta_upper,
                    'single_target_lower_endpoint':(2+theta_upper)/6},
                rows=rows)


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
