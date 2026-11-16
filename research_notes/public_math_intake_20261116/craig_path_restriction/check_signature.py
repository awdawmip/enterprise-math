"""Integer BRC subset counts, triangular minors, deck collisions, and two-scale energy."""
from collections import Counter
from fractions import Fraction
from math import comb

from check_deletion import observables, operator, words
from check_weighted import law_weight


def count_subword(word, pattern):
    counts = [1] + [0] * len(pattern)
    for symbol in word:
        for j in range(len(pattern), 0, -1):
            if pattern[j-1] == symbol:
                counts[j] += counts[j-1]
    return counts[-1]


def verify_triangular_certificate():
    checked_rows = 0
    for n in range(1, 8):
        for k in range(1, n+1):
            for coarse in words(k):
                padded = 'X' * (n-k) + coarse + 'Y' * (n-k)
                bins = operator(padded, k)
                leading = len(coarse) - len(coarse.lstrip('X'))
                trailing = len(coarse) - len(coarse.rstrip('Y'))
                diagonal = comb(n-k+leading, leading) * comb(n-k+trailing, trailing)
                assert bins[coarse] == count_subword(padded, coarse) == diagonal
                assert all(u == coarse or observables(u)[0] > observables(coarse)[0] for u in bins)
                checked_rows += 1
    return checked_rows


def verify_decks():
    sizes = []
    patterns = words(2)
    for n in range(2, 7):
        signatures = Counter()
        for word in words(n):
            profile = tuple(count_subword(word, u) for u in patterns)
            assert profile == tuple(operator(word, 2)[u] for u in patterns)
            signatures[profile] += 1
        sizes.append(len(signatures))
    assert sizes == [6, 20, 70, 252, 920]
    assert Counter(signatures.values()) == {1:916, 2:4}
    x, y = 'XYYXXXYXYYYX', 'YXXXYXYYYXXY'
    assert [operator(x, 2)[u] for u in patterns] == [48,42,42,42,39,12]
    assert all(operator(x, 2)[u] == operator(y, 2)[u] for u in patterns)
    assert (operator(x,3)['XXYYXY'],operator(y,3)['XXYYXY']) == (0,54)
    assert len({tuple(count_subword(w,u) for u in words(3)) for w in words(6)}) == 924
    # Means and conditional variances agree for this different pair, full tag laws differ.
    a,b = 'XYXYYX','XYYXXY'
    assert observables(a)[1:] == observables(b)[1:]
    assert (operator(a,2)['YYXX'],operator(b,2)['YYXX']) == (0,1)
    return sizes


def verify_mixing():
    checked = 0
    for n in range(2, 6):
        for k in range(1,n+1):
            for w in words(n):
                a = observables(w)[1]
                numerator = sum(count * observables(u)[1] * (1-observables(u)[1])
                                for u,count in operator(w,k).items())
                assert a*(1-a) >= numerator / comb(n,k)**2
                checked += 1
        for rate_x,rate_y in [(1,1),(2,1),(1,3)]:
            energies = []
            for m in (2,n):
                energies.append(sum(law_weight(w,rate_x,rate_y)*observables(w)[1]*(1-observables(w)[1])
                                    for w in words(m)))
            assert 0 < energies[0] <= energies[1]
    return checked


if __name__ == '__main__':
    print('exact triangular certificate rows:', verify_triangular_certificate())
    print('distinct level-2 decks, N=2..6:', verify_decks())
    print('sourcewise mixing inequalities:', verify_mixing())
