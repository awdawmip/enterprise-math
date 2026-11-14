#!/usr/bin/env python3
"""R143 exact integer-elimination membership + independent breakpoint enumeration.
No external dependencies; Python 3.10+; arbitrary-precision integers/Fraction.
"""
from fractions import Fraction
from random import Random
import json


def ceildiv(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def observed(K: int, word_len: int, theta: Fraction) -> tuple[int, ...]:
    assert K >= 1 and 0 < theta < 1
    L = K - 1
    q = theta.denominator
    p = theta.numerator
    f = [((L + j) * p) // q for j in range(word_len + 1)]
    return tuple(f[j + 1] - f[j] for j in range(word_len))


def membership(K: int, word: tuple[int, ...]):
    """Return (witness_or_None, exact_feasibility_certificate).

    For K>=2 infeasibility is certified by at most two extremal prefix pairs
    (or natural bounds 0 <= N <= K-2). For K=1 interval endpoints suffice.
    """
    m = len(word)
    assert K >= 1 and m >= 1 and set(word) <= {0, 1}
    s = [0]
    for bit in word:
        s.append(s[-1] + bit)
    if K == 1:
        lo = max([Fraction(0)] + [Fraction(s[j], j) for j in range(1, m + 1)])
        hi = min([Fraction(1)] + [Fraction(s[j] + 1, j) for j in range(1, m + 1)])
        if lo >= hi:
            return None, {"case": "K1", "lower": str(lo), "upper": str(hi)}
        t = (lo + hi) / 2
        assert observed(K, m, t) == word
        return t, {"case": "K1", "lower": str(lo), "upper": str(hi)}
    L = K - 1
    nmin, nmax = 0, L - 1
    low_source, high_source = ("boundary", 0), ("boundary", L - 1)
    for i in range(m + 1):
        for j in range(i + 1, m + 1):
            h = j - i
            d = s[j] - s[i]
            b_num = L * (d - 1) + i * s[j] - j * (s[i] + 1)
            a_num = L * (d + 1) + i * (s[j] + 1) - j * s[i]
            cur_min = b_num // h + 1
            cur_max = ceildiv(a_num, h) - 1
            if cur_min > nmin:
                nmin = cur_min
                low_source = (i, j, b_num, h)
            if cur_max < nmax:
                nmax = cur_max
                high_source = (i, j, a_num, h)
    certificate = {"case": "K_ge_2", "nmin": nmin, "nmax": nmax,
                   "lower_source": low_source, "upper_source": high_source}
    if nmin > nmax:
        return None, certificate
    n = nmin
    lo = max(Fraction(n + s[j], L + j) for j in range(m + 1))
    hi = min(Fraction(n + s[j] + 1, L + j) for j in range(m + 1))
    assert lo < hi
    theta = (lo + hi) / 2
    assert 0 < theta < 1
    assert theta.denominator <= 2 * (L + m) ** 2
    assert observed(K, m, theta) == word
    certificate.update({"N": n, "theta": str(theta)})
    return theta, certificate


def exhaustive_breakpoint_words(K: int, m: int):
    L = K - 1
    events = {Fraction(0), Fraction(1)}
    for n in range(max(1, L), L + m + 1):
        for r in range(1, n):
            events.add(Fraction(r, n))  # include non-coprime numerators!
    ordered = sorted(events)
    words = set()
    for i in range(len(ordered) - 1):
        words.add(observed(K, m, (ordered[i] + ordered[i + 1]) / 2))
        if i:
            words.add(observed(K, m, ordered[i]))
    return words


def run():
    counts = {"fully_exhaustive_memberships": 0, "K1_memberships": 0,
              "large_K_positive_witnesses": 0, "boundary_word_checks": 0,
              "saturation_cases": 0}
    for m in range(1, 10):
        for K in range(2, 26):
            actual = exhaustive_breakpoint_words(K, m)
            derived = set()
            for bits in range(1 << m):
                w = tuple((bits >> i) & 1 for i in range(m))
                t, _ = membership(K, w)
                if t is not None:
                    derived.add(w)
                counts["fully_exhaustive_memberships"] += 1
            assert derived == actual, (K, m, actual.symmetric_difference(derived))
        actual = exhaustive_breakpoint_words(1, m)
        derived = {tuple((bits >> i) & 1 for i in range(m))
                   for bits in range(1 << m)
                   if membership(1, tuple((bits >> i) & 1 for i in range(m)))[0] is not None}
        assert derived == actual
        counts["K1_memberships"] += 1 << m
    rng = Random(20261114)
    for m in (10, 20, 40, 60):
        for delta in (0, 11, 10 ** 80 + 137):
            K = 2 + delta
            for _ in range(100):
                theta = Fraction(rng.randrange(1, 1000000), 1000003)
                w = observed(K, m, theta)
                witness, cert = membership(K, w)
                assert witness is not None and observed(K, m, witness) == w
                counts["large_K_positive_witnesses"] += 1
    for m in range(5, 14):
        E = (m - 2) * ((m - 1) // 2) + 1
        language = exhaustive_breakpoint_words((m - 1) ** 2 + 2, m)
        missing_E = [w for w in language if membership(E, w)[0] is None]
        missing_prior = [w for w in language if membership(E - 1, w)[0] is None]
        assert not missing_E
        extremal = tuple([1] + [0] * (m - 2) + [1])
        assert set(missing_prior) == {extremal, tuple(1 - x for x in extremal)}
        counts["boundary_word_checks"] += 2 * len(language)
        counts["saturation_cases"] += 1
    print(json.dumps({"status": "R143_PREFIX_INTEGER_ELIMINATION_PASS", **counts}, indent=2))


if __name__ == "__main__":
    run()
