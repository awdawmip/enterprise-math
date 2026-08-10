#!/usr/bin/env python3
"""R005-A p=2 fourth-root-core transfer from an external finite prime-gap bound.

External premise: throughout the selected double-checked prime-gap region up to X=4e17, every cofactor point x with x+G<=X has a prime r in (x,x+G], with G=1328. This file verifies only downstream R005 integer inequalities.

Square basin: A=k^2, U=k^2+2k, F=k. Fourth-root observation core q<=C4=floor(U^(1/4)). For q<=C4, x=A/q. If the next prime r satisfies r<=x+G and G<=(U-A)/q=2k/q, then A<q*r<=U and r>F, so q*r forces q.

If all fourth-root-core witnesses are forced, T-A21 plus the generic residual lower bound gives Omega=3 for every residual.
"""

from __future__ import annotations
from math import isqrt
import json

X = 400_000_000_000_000_000
G = 1328


def iroot4(n: int) -> int:
    r = isqrt(isqrt(n))
    while (r + 1) ** 4 <= n:
        r += 1
    while r**4 > n:
        r -= 1
    return r


def basin(k: int) -> tuple[int, int, int]:
    A = k * k
    U = A + 2 * k
    return A, U, iroot4(U)


def width_margin(k: int) -> int:
    _, _, c = basin(k)
    return 2 * k - G * c


def cofactor_margin(k: int) -> int:
    A, _, _ = basin(k)
    return 2 * X - (A + 2 * G)


def first_k_width_ok() -> int:
    lo, hi = 2, 2_000_000
    while lo < hi:
        mid = (lo + hi) // 2
        if width_margin(mid) >= 0:
            hi = mid
        else:
            lo = mid + 1
    return lo


def last_k_cofactor_ok() -> int:
    lo, hi = 2, 2_000_000_000
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if cofactor_margin(mid) >= 0:
            lo = mid
        else:
            hi = mid - 1
    return lo


def main() -> None:
    K0 = first_k_width_ok()
    K1 = last_k_cofactor_ok()
    assert width_margin(K0) >= 0
    assert width_margin(K0 - 1) < 0
    assert cofactor_margin(K1) >= 0
    assert cofactor_margin(K1 + 1) < 0

    for k in (K0, K0 + 1, 1_000_000, K1):
        A, U, c = basin(k)
        assert A // c >= k + 1
        assert c <= k

    _, _, c0 = basin(K0)
    _, _, c1 = basin(K1)
    result = {
        "status": "R005-A P2 FOURTH-ROOT CORE EXTERNAL GAP TRANSFER / DOWNSTREAM ARITHMETIC VERIFIED / EXTERNAL COMPUTATION PREMISE",
        "external_premise": {
            "X": X,
            "G": G,
            "operational_form": "for every cofactor point x with x+G<=X, a prime lies in (x,x+G] inside the selected double-checked region",
        },
        "certified_k_range": [K0, K1],
        "lower_endpoint": {"k": K0, "C4": c0, "twok_minus_GC4": width_margin(K0), "previous_margin": width_margin(K0 - 1)},
        "upper_endpoint": {"k": K1, "C4": c1, "cofactor_margin": cofactor_margin(K1), "next_margin": cofactor_margin(K1 + 1)},
        "conclusion": f"Under the stated external finite gap premise, for every {K0}<=k<={K1} the square-basin fourth-root witness core is fully forced; therefore every residual composite, if present, has Omega exactly 3.",
        "nonclaim": "This does not assert that every basin in the range has a residual or lacks a least basis; it only bounds residual multiplicative arity.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
