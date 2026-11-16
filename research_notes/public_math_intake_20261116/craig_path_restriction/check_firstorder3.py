"""Certified two-sample moments and first-order coherent readings (stdlib only)."""

from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
for path in (HERE, HERE.parent / "craig_path_restriction", HERE.parent):
    if (path / "check_weighted.py").is_file():
        sys.path.insert(0, str(path))
        break
from check_weighted import area, law_weight, load_signed_brc, words
from check_coherent import histogram, multiply_and_round, positive_root_coordinates, round_out

ZERO = (F(0), F(0))
ONE = (F(1), F(1))
IDENTITY = (ONE, ZERO)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def subtract(x, y):
    return x[0] - y[1], x[1] - y[0]


def scale(q, x):
    return (q * x[0], q * x[1]) if q >= 0 else (q * x[1], q * x[0])


def scale_complex(q, z):
    return tuple(scale(q, coord) for coord in z)


def minus(z, w):
    return tuple(subtract(a, b) for a, b in zip(z, w))


def multiply(z, w):
    a, b = z
    c, d = w
    r = subtract(multiply_and_round(a, c), multiply_and_round(b, d))
    i = add(multiply_and_round(a, d), multiply_and_round(b, c))
    return round_out(*r), round_out(*i)


def powers(n):
    unit = positive_root_coordinates(4 * n)
    z = IDENTITY
    result = [z]
    for _ in range(n):
        z = multiply(z, unit)
        result.append(z)
    return result


def norm_squared(z):
    lo = hi = F(0)
    for a, b in z:
        hi += max(abs(a), abs(b))**2
        if a > 0 or b < 0:
            lo += min(abs(a), abs(b))**2
    return lo, hi


def early_probability(word, t):
    n = len(word) // 2
    left = word.index("Y")
    if word != "X" * left + "Y" * n + "X" * (n - left):
        return F(0)
    return comb(n, left) * t**left * (1-t)**(n-left)


def check_moments():
    kernel = load_signed_brc()
    quarter = F(1, 4)
    models = (
        ("uniform", F(1, 2), F(1, 3), lambda w: F(1, comb(len(w), len(w)//2))),
        ("PL-2:1", F(2, 3), F(13, 45), lambda w: law_weight(w, 2, 1)),
        ("early-1/4", quarter, F(3, 8), lambda w: early_probability(w, quarter)),
        ("early-3/4", 1-quarter, F(3, 8), lambda w: early_probability(w, 1-quarter)),
    )
    count = 0
    for name, p, b, weight in models:
        assert b == weight("XYYX") + weight("YXXY")
        c = weight("XYXY") + weight("YXYX")
        for n in range(1, 7):
            items = [(F(area(w), n*n) - p, weight(w)) for w in words(n)]
            assert len(items) == kernel.shortest_path_multiplicity((n,n,0,0,0,0))
            moments = [sum(prob * d**k for d, prob in items) for k in range(5)]
            assert moments[:2] == [1, 0]
            assert moments[2] == b/(2*n) + c/(4*n*n)
            assert abs(moments[3]) <= F(12,n*n)
            assert moments[4] <= F(1,4*n*n)
            count += len(items)
        print(f"{name}: p={p}, b={b}, c={c}; central moments exact through n=6")
    return count


def marked_statistic(word):
    """Average over enclosures and all matchings of unused positions."""
    xs = [i for i,c in enumerate(word) if c == "X"]
    ys = [i for i,c in enumerate(word) if c == "Y"]
    num = den = 0
    for first_x in combinations(xs, 2):
        rest_x = [x for x in xs if x not in first_x]
        for first_y in combinations(ys, 2):
            four = "".join(word[i] for i in sorted(first_x + first_y))
            for order_y in permutations(y for y in ys if y not in first_y):
                if four in ("XYYX", "YXXY"):
                    num += prod(1 if x < y else -1 for x, y in zip(rest_x,order_y))
                den += 1
    return F(num, den)


def check_marked():
    for j in range(4):
        n = j + 2
        stats = {w: marked_statistic(w) for w in words(n)}
        assert sum(stats.values()) / comb(2*n, n) == F(1,3) * F(0)**j
        pl = sum(v*law_weight(w,2,1) for w,v in stats.items())
        assert pl == F(13,45)*F(1,3)**j
        mix = sum(v*(early_probability(w,F(1,4)) + early_probability(w,F(1,2)))/2
                  for w,v in stats.items())
        assert mix == (F(3,8)*F(-1,2)**j + F(1,2)*F(0)**j)/2
    print("12 marked moments checked on named disjoint pairs, through layer 5")


def reading(n, t, uniform):
    root_powers = powers(n*n)
    if uniform:
        weights = {k: F(mult, comb(2*n, n)) for k, mult in histogram(n).items()}
    else:
        weights = {n*j: comb(n, j)*t**j*(1-t)**(n-j) for j in range(n+1)}
    assert sum(weights.values()) == 1
    return tuple(tuple(sum(weights[k] * root_powers[k][coord][end] for k in weights)
                       for end in range(2)) for coord in range(2))


def check_characters():
    h = 1024
    a, _ = positive_root_coordinates(8*h)
    c_h = scale(2*h*h, subtract(ONE, a))
    c_limit = (c_h[0], c_h[1] + F(1,12*h*h))
    for t, b, uniform in ((F(1,2), F(1,3), True), (F(1,4), F(3,8), False),
                          (F(3,4), F(3,8), False)):
        z_inf = powers(t.denominator)[t.numerator]
        lead = tuple(multiply_and_round(scale(b, c_limit), v) for v in z_inf)
        vals = {n: reading(n,t,uniform) for n in (1,2,4,8,16)}
        for n, val in vals.items():
            scaled_gap = scale_complex(n, minus(z_inf, val))
            residual = norm_squared(scale_complex(n, minus(scaled_gap, lead)))
            assert residual[1] < 18**2
            if n < 16:
                extrapolation = minus(minus(scale_complex(2, vals[2*n]), val), z_inf)
                assert norm_squared(extrapolation)[1] < F(27**2, n**4)
                assert norm_squared(extrapolation)[1] < norm_squared(minus(z_inf, val))[0]
        gap16 = norm_squared(scale_complex(16, minus(z_inf, vals[16])))
        tight = (gap16[0]*10**8).__floor__(), (gap16[1]*10**8).__ceil__()
        print(f"t={t}, uniform={uniform}: 16^2 |Z_inf-Z_16|^2 in {tight}/10^8")


if __name__ == "__main__":
    print(f"checked {check_moments()} model-word combinations")
    check_marked()
    check_characters()
