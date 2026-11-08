#!/usr/bin/env python3
"""Exact BRC-boundary first-jet difference and signed W216 mirror Abel test.
Author-side finite regression only; does not run or replace native H0/B0.
Standard library only. All rational reductions are exact finite-field arithmetic.
"""
from math import comb
import json


def primes():
    for p in list(range(5, 230, 2)) + [373]:
        if all(p % d for d in range(3, int(p ** 0.5) + 1, 2)):
            yield p


def check(p):
    H = [0] * p
    for a in range(1, p):
        H[a] = (H[a - 1] + pow(a, -1, p)) % p
    p2 = p*p
    t = 32*pow(3, -1, p2) % p2
    Q = (pow(t, p-1, p2)-1) % p2 // p

    def jet(q):
        return (Q + 2*H[(2*q) % p-1] + 3*H[(3*q) % p-1]
                  - 4*H[(4*q) % p-1] - H[q-1]) % p

    def rational(q):
        den = (3*q+1)*(3*q+2)*(4*q+1)*(4*q+3) % p
        return -5*(2*q+1)*pow(den, -1, p) % p

    regular, singular = 0, []
    for q in range(1, p-1):
        assert jet(p-q) == jet(q)
        den = (3*q+1)*(3*q+2)*(4*q+1)*(4*q+3) % p
        d = (jet(q+1)-jet(q)) % p
        if not den:
            singular.append([q, d])
            continue
        assert d == rational(q), (p, q, d, rational(q))
        regular += 1
    assert jet(1) == jet(p-1)

    weighted = None
    if p % 6 == 1:
        m = (p-1)//6
        prefix, moment, bulk = 0, 0, 0
        for q in range(2*m+1, 3*m+1):
            numerator = comb(2*q, q)**2 * comb(3*q, q)
            assert numerator % p == 0
            U = (numerator//p)*pow(216, -q, p) % p
            assert U != 0
            w = (1-6*q)*pow(36*(q**3)*U % p, -1, p) % p
            prefix = (prefix + w) % p
            moment = (moment + w*jet(q)) % p
            if q < 3*m:
                bulk = (bulk + prefix*rational(q)) % p
        assert moment == (prefix*jet(3*m)-bulk) % p
        weighted = {"mirror_tail_unit": prefix, "endpoint_jet": jet(3*m),
                    "rational_prefix_bulk": bulk, "weighted_jet_moment": moment}

    return {"p": p, "regular": regular, "singular": singular, "weighted": weighted}


def main():
    results = [check(p) for p in primes()]
    assert len(results) == 49
    assert sum(r["regular"] for r in results) == 5193
    assert sum(len(r["singular"]) for r in results) == 194
    z = results[-1]
    assert z["p"] == 373
    assert z["singular"] == [[93, 87], [124, 311], [248, 62], [279, 286]]
    assert z["weighted"] == {"mirror_tail_unit": 266, "endpoint_jet": 278,
                              "rational_prefix_bulk": 105, "weighted_jet_moment": 362}
    print(json.dumps({"status": "PASS", "prime_count": len(results),
         "regular_differences": sum(r["regular"] for r in results),
         "singular_crossings": sum(len(r["singular"]) for r in results),
         "p373": z}, sort_keys=True))


if __name__ == "__main__":
    main()
