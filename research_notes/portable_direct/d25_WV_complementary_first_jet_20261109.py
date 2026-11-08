#!/usr/bin/env python3
"""Exact W216/V2304 complementary first-jet check; Python standard library only.
Author-side regression, not native H0/B0 computation or formal proof admission.
"""
from math import comb
import json


def primes_up_to(n):
    for p in range(5, n + 1, 2):
        if all(p % d for d in range(3, int(p ** 0.5) + 1, 2)):
            yield p


def check_prime(p):
    M = p * p
    H = [0] * p
    for n in range(1, p):
        H[n] = (H[n - 1] + pow(n, -1, p)) % p
    x = 32 * pow(3, -1, M) % M
    Q = (pow(x, p - 1, M) - 1) % M // p
    W = []
    V = []
    for n in range(p):
        b = comb(2 * n, n)
        W.append(b * b * comb(3 * n, n))
        V.append(b * b * comb(4 * n, 2 * n))
    dW, dV = pow(216, -p, M), pow(2304, -p, M)
    samples = {}
    for q in range(1, p):
        # Integer division is exact by the complementary valuation theorem.
        a = W[q] * W[p-q]
        b = V[q] * V[p-q]
        assert a % (p ** 3) == b % (p ** 3) == 0
        a_unit = (a // p**3) * dW % M
        b_unit = (b // p**3) * dV % M
        assert a_unit % p != 0 and b_unit % p != 0
        actual = a_unit * pow(b_unit, -1, M) % M
        r2, r3, r4 = (2*q) % p, (3*q) % p, (4*q) % p
        jet = (Q + 2*H[r2-1] + 3*H[r3-1]
                  - 4*H[r4-1] - H[q-1]) % p
        if 4*q < p or 4*q > 3*p:
            rho = 16 * pow(3, -1, M) % M
        elif 3*q < p or 3*q > 2*p:
            rho = (-16) % M
        else:
            rho = 8
        predicted = rho * (1 + p*jet) % M
        assert actual == predicted, (p, q, actual, predicted, jet)
        qm = p-q
        mirror = (Q+2*H[(2*qm)%p-1]+3*H[(3*qm)%p-1]
                    -4*H[(4*qm)%p-1]-H[qm-1]) % p
        assert mirror == jet, (p, q, jet, mirror)
        if p == 373 and q in (125, 126, 247, 248):
            samples[str(q)] = dict(jet=jet, actual_ratio=actual, rho=rho)
    return dict(prime=p, checked=p-1, fermat_quotient=Q,
                samples=samples if p == 373 else None)


def main():
    ps = list(primes_up_to(229)) + [373]
    results = [check_prime(p) for p in ps]
    assert len(ps) == 49
    assert sum(r["checked"] for r in results) == 5436
    assert results[-1]["samples"]["125"]["actual_ratio"] == 123098
    assert results[-1]["samples"]["126"]["actual_ratio"] == 70878
    print(json.dumps(dict(status="PASS", prime_count=len(ps),
        pair_indices_checked=sum(r["checked"] for r in results),
        prime_373=results[-1]), sort_keys=True))


if __name__ == "__main__":
    main()
