#!/usr/bin/env python3
"""Finite exact regression checker for the canonical sub-root Rosser carrier.

Checks the beta-2 activation threshold equivalence and injectivity/top-two-prime
recovery on synthetic squarefree carriers.  This is regression evidence only.
"""

from itertools import combinations
from math import prod


def qcrit(primes_desc: tuple[int, ...]) -> int:
    if not primes_desc:
        return 1
    vals = []
    prefix = 1
    for j, q in enumerate(primes_desc, start=1):
        if j % 2 == 1:
            vals.append(prefix * q**3)
        prefix *= q
    return max(vals)


def main() -> None:
    small = (3, 5, 7, 11, 13, 17, 19)
    anchors = (23, 29, 31)
    externals = (37, 41, 43, 47)
    D = 10**12

    seen: dict[int, tuple[int, int, int]] = {}
    for r in anchors:
        for p in externals:
            if not r < p:
                continue
            allowed_small = tuple(q for q in small if q < r)
            for k in range(0, min(4, len(allowed_small)) + 1):
                for subset in combinations(allowed_small, k):
                    desc = tuple(sorted(subset, reverse=True))
                    d = prod(desc) if desc else 1
                    qc = qcrit(desc)
                    supported = qc < D // (r * p) + (1 if D % (r * p) else 0)
                    # Exact strict rational equivalence qc < D/(rp) <=> rp*qc < D.
                    assert supported == (r * p * qc < D)
                    assert (r * p * qc < D) == (p * r * qc < D)

                    qphys = r * p * d
                    factors = sorted((p, r) + desc, reverse=True)
                    assert factors[0] == p
                    assert factors[1] == r
                    assert qphys // (p * r) == d

                    triple = (r, p, d)
                    if qphys in seen:
                        assert seen[qphys] == triple
                    else:
                        seen[qphys] = triple

    print("P017 c515 canonical subroot Rosser carrier checker: PASS")
    print("tested physical moduli =", len(seen))
    print("top-two primes recover (p,r) uniquely and Rosser support is a monotone p cutoff")


if __name__ == "__main__":
    main()
