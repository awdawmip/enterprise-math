"""Check sharp zero-count endpoints against all moment-polytope vertices."""
from fractions import Fraction
from itertools import combinations


def formula(m, mean, second):
    if mean == 0:
        return Fraction(1), Fraction(1)
    if m == 1:
        return 1 - mean, 1 - mean
    j = min(m - 1, int(second // mean))
    upper = 1 - ((2 * j + 1) * mean - second) / (j * (j + 1))
    lower = max(Fraction(0), (second - (m + 1) * mean + m) / m)
    return lower, upper


def vertices(m, mean, second):
    # Two- and one-point supports occur as zero weights of a triple.
    if m < 2:
        return formula(m, mean, second)
    values = []
    for a, b, c in combinations(range(m + 1), 3):
        w = (second - (b + c) * mean + b * c) / ((a-b)*(a-c))
        x = (second - (a + c) * mean + a * c) / ((b-a)*(b-c))
        y = 1 - w - x
        if min(w,x,y) >= 0:
            assert w*a + x*b + y*c == mean
            assert w*a*a + x*b*b + y*c*c == second
            values.append(w if a == 0 else Fraction(0))
    return min(values), max(values)


def hypergeom(n, k, slots):
    mean = Fraction(k * slots, n)
    second = mean + Fraction(slots*(slots-1)*k*(k-1), n*(n-1))
    return mean, second


if __name__ == '__main__':
    checked = 0
    for n in range(2, 17):
        for k in range(n + 1):
            for slots in range(n - k + 1):
                m = min(k, slots)
                moments = hypergeom(n, k, slots)
                assert formula(m, *moments) == vertices(m, *moments)
                checked += 1
    full = formula(17, *hypergeom(69, 29, 17))
    assert full == (0, Fraction(5,92))
    assert vertices(17, *hypergeom(69,29,17)) == full
    print(checked, 'small fibers;', full, 'for (69,29,17)')
