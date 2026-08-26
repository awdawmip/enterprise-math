"""Fixed-total-conductor collapse of the bi-primitive Walsh divisor plane.

Let m>1 be an odd squarefree product of primes transverse to M=k(k+1).  For
coprime factors n*d=m, p017_p018_euclidean_biprimitive defines the bi-primitive
tent block B(n,d).  The n-axis corresponds to the orientation root

    r=-M (mod p)

and the d-axis to

    r=+M (mod p).

Hence the split coefficient mu(n) is exactly the orientation-Walsh root sign.
Since B(n,d) is already primitive on the full modulus m, summing over every
factor split gives the single selected-modulus signed Walsh tent column:

    sum_(n*d=m) mu(n) B(n,d) = B_m^Walsh(k).

Equivalently, in Fourier space the left side has the common primitive tent
coefficient and the root sum

    sum_(n*d=m) mu(n) e(h*rho_(n,d)/m),

which is precisely the signed root cube of conductor m.  Nonprimitive
frequencies vanish on both sides.

Consequently the full ordered low-product aggregate collapses from the divisor
plane to one total-conductor axis:

    sum_(n*d<=k) mu(n) B(n,d)
      = k + sum_(1<m<=k, m squarefree transverse) B_m^Walsh(k).

The m=1 term is the symmetric tent mass k.  For every m>1 the existing exact
Euclidean remainder theorem then gives

    B_m^Walsh(k)
      = (r/k) B_m^Walsh(r),       r=k mod m.

Thus the two-conductor lattice may be recoalesced before any estimate: the
remaining analytic object is a one-dimensional family of Euclidean boundary
columns indexed only by total conductor m and its remainder state k mod m.
The reciprocal-Mobius quotient-strip representation remains an exact alternate
coordinate, but is not an irreducible hard core.

This is an exact algebraic/Fourier collapse, not a bound for the remaining
one-conductor sum and not a proof of Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, prod

from .legendre import primes_up_to
from .p017_p018_euclidean_biprimitive import biprimitive_block
from .p017_p018_walsh_remainder_descent import selected_modulus_tent_contribution


def _mobius_squarefree(value: int) -> int:
    if value < 1:
        raise ValueError("value must be positive")
    if value == 1:
        return 1
    remaining = value
    omega = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            omega += 1
            if remaining % p == 0:
                return 0
        p += 1
    if remaining > 1:
        omega += 1
    return -1 if omega % 2 else 1


def _divisors(value: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, value + 1) if value % d == 0)


def fixed_total_biprimitive_collapse(k: int, conductor: int) -> dict[str, object]:
    """Verify sum_(nd=m)mu(n)B(n,d)=selected_modulus_tent_contribution(k,m)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(conductor, bool) or not isinstance(conductor, int) or conductor <= 1 or conductor % 2 == 0:
        raise ValueError("conductor must be an odd integer >1")
    if _mobius_squarefree(conductor) == 0:
        raise ValueError("conductor must be squarefree")
    M = k * (k + 1)
    if gcd(M, conductor) != 1:
        raise ValueError("conductor must be transverse to the pronic center")

    rows: list[dict[str, object]] = []
    split_sum = Fraction(0, 1)
    for n in _divisors(conductor):
        d = conductor // n
        if gcd(n, d) != 1:
            raise AssertionError("squarefree total conductor produced noncoprime split")
        mu_n = _mobius_squarefree(n)
        block = biprimitive_block(M, k, n, d)
        term = mu_n * block
        split_sum += term
        rows.append(
            {
                "negative_orientation_product_n": n,
                "positive_orientation_product_d": d,
                "mu_n": mu_n,
                "biprimitive_block": block,
                "weighted_term": term,
            }
        )

    selected = selected_modulus_tent_contribution(k, conductor)
    if split_sum != selected:
        raise AssertionError("fixed-total bi-primitive split sum did not collapse to Walsh conductor")
    return {
        "k": k,
        "center": M,
        "total_conductor_m": conductor,
        "split_biprimitive_sum": split_sum,
        "selected_modulus_walsh_tent": selected,
        "fixed_total_conductor_collapse": True,
        "split_rows": tuple(rows),
    }


def _transverse_squarefree_products(k: int, cutoff: int) -> tuple[int, ...]:
    M = k * (k + 1)
    primes = tuple(p for p in primes_up_to(cutoff) if p % 2 == 1 and M % p != 0)
    values = [1]
    for p in primes:
        additions = []
        for value in values:
            if value <= cutoff // p:
                additions.append(value * p)
        values.extend(additions)
    return tuple(sorted(set(values)))


def total_conductor_aggregate_collapse(k: int, cutoff: int | None = None) -> dict[str, object]:
    """Verify the bounded divisor-plane aggregate equals k plus one-conductor Walsh columns."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if cutoff is None:
        cutoff = k
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or not (1 <= cutoff <= k):
        raise ValueError("cutoff must satisfy 1<=cutoff<=k")
    M = k * (k + 1)
    products = _transverse_squarefree_products(k, cutoff)

    plane = Fraction(0, 1)
    plane_rows: list[dict[str, object]] = []
    for n in products:
        mu_n = _mobius_squarefree(n)
        for d in products:
            if n > cutoff // d or gcd(n, d) != 1:
                continue
            block = biprimitive_block(M, k, n, d)
            term = mu_n * block
            plane += term
            plane_rows.append({"n": n, "d": d, "mu_n": mu_n, "term": term})

    conductor_sum = Fraction(k, 1)  # m=1 symmetric tent mass
    conductor_rows: list[dict[str, object]] = []
    for m in products:
        if m == 1:
            continue
        selected = selected_modulus_tent_contribution(k, m)
        conductor_sum += selected
        conductor_rows.append({"m": m, "selected_modulus_tent": selected, "remainder": k % m})

    if plane != conductor_sum:
        raise AssertionError("divisor-plane aggregate did not collapse to one-conductor Walsh sum")
    return {
        "k": k,
        "cutoff": cutoff,
        "center": M,
        "divisor_plane_aggregate": plane,
        "one_conductor_aggregate": conductor_sum,
        "coarse_m_one_term": k,
        "total_conductor_collapse": True,
        "plane_rows": tuple(plane_rows),
        "conductor_rows": tuple(conductor_rows),
    }
