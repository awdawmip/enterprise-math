"""Dual one-dimensional coordinates for fourth-root squarefree triples.

Let X=k^2, U=k^2+2k and z=floor(U^(1/4)).  A squarefree z-rough triple in the
consecutive-square interval has

    n=a*b*c,  z<a<b<c<=k.

Attach the two overlapping semiprime products

    D=a*b   (canonical two-smallest token),
    Q=b*c   (ordered least-factor quotient).

They lie on opposite sides of the cubic pivot:

    sqrt(U) < D <= n^(2/3) <= U^(2/3),
    X^(2/3) < n^(2/3) <= Q < U/(z+1) < (z+1)^3.

Moreover gcd(D,Q)=b, so the middle prime is recoverable from the two channel
coordinates and

    a=D/gcd(D,Q),  c=Q/gcd(D,Q).

The same triple therefore has two equivalent one-dimensional floor-channel
representations:

* low side:  D -> unique odd prime cofactor c;
* high side: Q -> unique odd prime candidate a.

The exponent 2/3 is the exact separator between the two representations.
Balanced triples are precisely the regime in which both coordinates approach
the cubic pivot; unbalanced triples separate to opposite sides.

This identifies the Generation-2 balanced-cubic localisation and the
Generation-4 canonical-pair / ordered-quotient routes as two coordinate charts
on the same triple contamination set.
"""

from __future__ import annotations

from math import gcd, isqrt

from .p017_p018_buchstab_cutoff_ladder import square_interval_upper
from .p017_p018_root_p3_canonical_pair import canonical_pair_triple_rows
from .p017_p018_root_p3_support_recovery import root_p3_cutoff


def triple_cubic_duality_row(k: int, a: int, b: int, c: int) -> dict[str, int | bool]:
    """Return the two semiprime coordinates for one ordered triple."""
    if not (a < b < c):
        raise ValueError("require distinct ordered factors a<b<c")
    z = root_p3_cutoff(k)
    if not (z < a and c <= k):
        raise ValueError("triple factors must lie in the fourth-root medium band")
    n = a * b * c
    upper = square_interval_upper(k)
    if not (k * k < n <= upper):
        raise ValueError("triple product must lie in the square interval")

    D = a * b
    Q = b * c
    middle = gcd(D, Q)
    if middle != b:
        raise AssertionError("cubic dual coordinates failed to recover middle factor")
    if not D * D > upper:
        raise AssertionError("canonical pair did not lie above sqrt(U)")
    if D**3 > upper**2:
        raise AssertionError("canonical pair exceeded U^(2/3)")
    if Q**3 <= (k * k) ** 2:
        raise AssertionError("ordered quotient did not lie above X^(2/3)")
    if Q >= (z + 1) ** 3:
        raise AssertionError("ordered quotient exceeded fourth-root P2 ceiling")

    return {
        "k": k,
        "value": n,
        "a": a,
        "b": b,
        "c": c,
        "canonical_pair_D": D,
        "ordered_quotient_Q": Q,
        "middle_factor_gcd": middle,
        "recover_a": D // middle,
        "recover_c": Q // middle,
        "D_above_sqrt_U": D * D > upper,
        "D_at_most_U_two_thirds": D**3 <= upper**2,
        "Q_above_X_two_thirds": Q**3 > (k * k) ** 2,
        "Q_below_fourth_root_P2_ceiling": Q < (z + 1) ** 3,
    }


def triple_cubic_duality_profile(k: int) -> dict[str, object]:
    """Enumerate the dual charts for every squarefree fourth-root triple."""
    rows = tuple(
        triple_cubic_duality_row(k, a, b, c)
        for a, b, c, _, _ in canonical_pair_triple_rows(k)
    )
    D_values = tuple(int(row["canonical_pair_D"]) for row in rows)
    Q_values = tuple(int(row["ordered_quotient_Q"]) for row in rows)
    if len(D_values) != len(set(D_values)):
        raise AssertionError("canonical low-side chart is not injective")
    # Q alone need not identify the factorization abstractly, but paired (D,Q)
    # always does through the gcd middle-factor reconstruction.
    pairs = tuple(zip(D_values, Q_values))
    if len(pairs) != len(set(pairs)):
        raise AssertionError("dual cubic chart pair is not injective")
    return {
        "k": k,
        "triple_count": len(rows),
        "rows": rows,
        "canonical_pair_values": D_values,
        "ordered_quotient_values": Q_values,
        "dual_chart_pairs": pairs,
        "cubic_pivot_duality": True,
    }
