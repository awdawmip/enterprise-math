#!/usr/bin/env python3
"""R005-A p=2 Omega=3 extension using Campbell 2026 finite prime-gap input.

External premise quoted in Campbell 2026: for every positive real x<6.8e19, there is a prime in (x,x+1724]. Square-basin fourth-root witnesses then force whenever 1724<=2k/q. T-A21 converts this to residual Omega=3.
"""

from __future__ import annotations
from math import isqrt
import json

X = 68_000_000_000_000_000_000
G = 1724
K0 = 862**2


def largest_k() -> int:
    return isqrt(2 * X - 1)


def main() -> None:
    K1 = largest_k()
    assert K0 == 743_044
    assert K1 == 11_661_903_789
    assert 2 * isqrt(K0) == G
    assert 2 * ((K0 - 1) ** 0.5) < G
    assert K1 * K1 < 2 * X
    assert (K1 + 1) * (K1 + 1) >= 2 * X

    for k in (K0, K0 + 1, 894_427_190, K1):
        C4 = isqrt(k)
        assert 2 * k >= G * C4
        assert k * k // max(C4, 1) > k

    result = {
        "status": "R005-A P2 CAMPBELL-GAP OMEGA3 TRANSFER / DOWNSTREAM ARITHMETIC VERIFIED / EXTERNAL PUBLISHED PREMISE",
        "external_premise": {
            "x_upper_strict": X,
            "gap": G,
            "statement": "for every real x<X, a prime exists in (x,x+1724]",
        },
        "direct_transfer_range": [K0, K1],
        "combined_with_prior_exact_record_certificate": [2, K1],
        "conclusion": f"Combining with the prior exact/record-gap certificate, for every 2<=k<={K1}, every square-basin residual, if any, has Omega=3.",
        "nonclaim": "This is not a proof that residuals exist or that least bases fail; Campbell's ambient almost-prime theorem and R005 residual arity theorem are logically distinct.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
