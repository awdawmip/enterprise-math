#!/usr/bin/env python3
"""PREFIX-1030: frozen Stage46 BRC-observer spectral contrast; exact integer verification.

The positive spectral witnesses E[m,k] are observer-level values, not native
X6 state transitions or a replacement for signed coherent amplitude data.
No floats are used to establish signs. Decimal formatting is reporting only.
"""
from fractions import Fraction
from math import comb
from decimal import Decimal, localcontext
import json
import sys
import time

sys.set_int_max_str_digits(0)


def a6_values(N):
    A = [1, 6, 66]
    for r in range(2, N + 3):
        numerator = (
            2 * (2*r + 1) * (14*r**4 + 28*r**3 + 28*r**2 + 14*r + 3) * A[r]
            - 4*r**3 * (196*r**2 + 59) * A[r-1]
            + 1152 * (2*r - 1) * r*r * (r - 1)**2 * A[r-2]
        )
        denominator = (r + 1)**5
        assert numerator % denominator == 0
        A.append(numerator // denominator)
    return A


def contrast(m, A):
    q = (
        Fraction(-72*(72*m*m + 163*m + 80), 5*(m+1))*A[m+1]
        + Fraction(2*(144*m**3 + 1135*m*m + 2367*m + 1310), 5*(m+1)*(m+2))*A[m+2]
        - Fraction(2*(m+8)*(2*m+5), 5*(m+2))*A[m+3]
    )
    assert q.denominator == 1
    return q.numerator


def check(N=5000):
    start = time.monotonic()
    A = a6_values(N)
    a = [contrast(m, A) for m in range(N+1)]
    assert a[:3] == [2412, 25620, 386028]

    levels = sorted(set(x for x in (400, 800, 1200, N) if x <= N))
    proportions = [(1,20), (1,10), (1,5), (1,3), (1,2),
                   (2,3), (4,5), (9,10), (19,20)]
    targets = {(n, n*u//v) for n in levels for (u,v) in proportions}
    samples = []
    positive_count = 0
    first_nonpositive = None
    row = a

    for k in range(N+1):
        for m, E in enumerate(row):
            if E > 0:
                positive_count += 1
            elif first_nonpositive is None:
                first_nonpositive = {"m":m, "k":k, "E":str(E)}
            n = m+k
            if (n,m) in targets:
                # Exact rational normalized Beta probe:
                # D=(n+1)*binom(n,m)*E/36^(n+1).
                d = Fraction((n+1)*comb(n,m)*E, 36**(n+1))
                with localcontext() as ctx:
                    ctx.prec = 45
                    formatted = str(Decimal(d.numerator)/Decimal(d.denominator))
                samples.append({"n":n,"m":m,"k":k,
                                "spectral_y":str(Fraction(36*m,n)),
                                "D_decimal":formatted, "E_digits":len(str(E))})
        row = [36*row[j]-row[j+1] for j in range(len(row)-1)]

    return {
        "schema":"PREFIX1030_BERNSTEIN_LOCALIZATION_EXACT_V1",
        "N":N,
        "checked_pairs":(N+1)*(N+2)//2,
        "strictly_positive_pairs":positive_count,
        "first_nonpositive":first_nonpositive,
        "a0_to_a4":a[:5],
        "probes":sorted(samples,key=lambda x:(x["n"],x["m"])),
        "elapsed_seconds":time.monotonic()-start,
        "claim":"Exact integer sign check. Probe decimal comes from exact Fraction.",
        "review":"AUTHOR_CALCULATION_NOT_INDEPENDENTLY_REVIEWED"
    }


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv)>1 else 5000
    print(json.dumps(check(N),indent=2,ensure_ascii=False))
