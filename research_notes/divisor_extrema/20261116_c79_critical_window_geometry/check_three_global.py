"""Exact small-cube phase counts by cosets of a rank-two integer lattice."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


def exact_phase(base, denominator):
    """Rows of base/denominator; first two rows must be independent."""
    (a, b), (c, d), (e, f) = base
    det = a*d-b*c
    if det == 0:
        raise ValueError("the selected first two rows are dependent")
    counts = Counter()
    # On each elementary half-open cube all candidate tests are constant.
    # Two lower vertices differ by an integer combination of the columns
    # iff the first two Cramer coordinates differ by integers and the third
    # coincides with that same combination.
    for i, j, k in product(range(denominator), repeat=3):
        first = d*i-b*j
        second = a*j-c*i
        key = (first % abs(det), second % abs(det), det*k-e*first-f*second)
        counts[key] += 1
    return F(sum(v == 1 for v in counts.values()), denominator**3)


def check():
    rows = []
    for n, k in [(1, 2), (2, 3), (3, 5), (4, 7), (5, 6)]:
        lattice = [(n, 0), (0, n), (1, n)]
        value = exact_phase(lattice, n*k)
        assert value == F(2, n*k**3)
        rows.append(dict(a=str(F(1,n)), b="1", L=str(F(1,k)),
                         probability=str(value), cubic_coefficient=str(value*k**3)))

    # A different, oblique integral lattice with no axis-aligned input basis.
    oblique = [(3,1),(-1,2),(2,5)]
    samples = []
    for q in (10, 12, 14, 16, 18, 20, 24, 28, 32):
        p = exact_phase(oblique, q)
        assert p == exact_phase([(b,a+b) for a,b in oblique], q)
        assert p * q**3 <= 608 * max(abs(a)+abs(b) for a,b in oblique)**3
        samples.append((q,str(p),str(p*q**3)))
    assert len(set(entry[-1] for entry in samples[-4:])) == 1
    # Universal integrated constant from the two sorted-distance regions.
    upper = 48*(F(4**3,6)+2)
    assert upper == 608
    return dict(rectangular_examples=rows, oblique_examples=samples,
                universal_upper_constant=int(upper), inherited_sublevel_degree=412)


if __name__ == "__main__":
    print(json.dumps(check(),indent=2))
