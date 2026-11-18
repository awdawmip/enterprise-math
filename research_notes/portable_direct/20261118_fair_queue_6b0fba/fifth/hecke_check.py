"""Replay auxiliary-prime and shared-list examples using only exact integers."""
from collections import Counter
from math import gcd, isqrt, prod


def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def shared_classes():
    candidates = (73, 433)
    orders = (2, 3)
    modulus = prod(candidates)
    assert all(prime(l) and (l - 1) % 72 == 0 for l in candidates)
    histogram = Counter()
    for a in range(modulus):
        if gcd(a, modulus) != 1:
            continue
        key = tuple(any(pow(a, (l - 1)//q, l) != 1 for l in candidates) for q in orders)
        histogram[key] += 1
    assert histogram == {(True, True):20736, (True, False):2592,
                         (False, True):6912, (False, False):864}
    states = sum(histogram.values())
    assert 3*histogram[True, True] == 2*states and states == 31104
    return histogram


def first_aux(q, p_mod_l):
    for l in range(12*q + 1, 100000, 12*q):
        if not prime(l):
            continue
        a = p_mod_l(l)
        residue = pow(a, (l-1)//q, l)
        if a and residue != 1:
            return l, a, residue
    raise ValueError("no auxiliary prime in the example search range")


def main():
    print("shared table (q=2 hit, q=3 hit):", sorted(shared_classes().items()))
    # Primality of this known input is sourced from the independent GIMPS announcement.
    exponent = 82589933
    n = 13
    parameter = 20 + (n+1)*(exponent+1)
    assert parameter == 1156259096 and parameter < 2**31
    assert 31*200000 < exponent-1
    targets = [2, 3, 5, 7, 11, 13]
    expected = [(193,82,192), (109,22,45), (181,139,42),
                (337,168,79), (397,148,167), (157,58,46)]
    for q, wanted in zip(targets, expected):
        found = first_aux(q, lambda l: (pow(2,exponent,l)-1) % l)
        assert found == wanted
        print("q,least ell,p mod ell,p^((ell-1)/q) mod ell:", q, *found)


if __name__ == "__main__":
    main()
