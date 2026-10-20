"""Collapse the incidence-optimal symmetric reusable Walsh core to one conductor axis.

Let C=floor((k-1)/2).  For one squarefree transverse total conductor m=e*d<=C,
with coprime orientation factors e,d, the incidence-optimal symmetric hyperbola
coefficient is

    c_C(e,d)=1/2[mu(d)+mu(e)].

Since mu(d)=mu(m)mu(e), this becomes

    c_C(e,d)=0       if omega(m) is odd,
               mu(e) if omega(m) is even.

The bi-primitive tent block is self-dual in the orientation factors.  Moreover
the selected-modulus signed Walsh tent column of an odd-support conductor
vanishes identically because its root character is odd under r->-r while the
tent is even.  Therefore for every nontrivial m<=C,

    sum_(e*d=m) c_C(e,d) B(e,d)
      = B_m^Walsh(k).

Thus the entire reusable low-product boundary core of the actual
incidence-optimal symmetric compiler recoalesces from the two-dimensional
orientation-divisor plane to the one-dimensional total-conductor family

    {B_m^Walsh(k): 1<m<=C, m squarefree transverse}.

Every such column then admits the exact Euclidean remainder descent

    B_m^Walsh(k)=(r/k)B_m^Walsh(r),  r=k mod m < k/2,

so the strict half-scale child atlas applies directly to the irreducible
symmetric low-product core, not merely to an auxiliary analytic aggregate.

High-total-conductor patterns m>C are not covered by this theorem: the symmetric
hyperbola coefficient there is only partially retained according to the two
orientation budgets.  They remain a separate boundary-tail language.

This is an exact compiler/BRC theorem.  It does not estimate the one-conductor
sum, the high-product tail, or prove Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p017_p018_euclidean_biprimitive import biprimitive_block
from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff
from .p017_p018_walsh_remainder_descent import selected_modulus_tent_contribution
from .p017_p018_walsh_symmetric_hyperbola import symmetric_hyperbola_coefficient


def _divisors(value: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, value + 1) if value % d == 0)


def _mobius(value: int) -> int:
    if value < 1:
        raise ValueError("value must be positive")
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


def selected_odd_support_vanishes(k: int, conductor: int) -> dict[str, object]:
    """Verify B_m(k)=0 for one odd-support squarefree transverse conductor."""
    if _mobius(conductor) != -1:
        raise ValueError("conductor must be squarefree with odd support degree")
    M = k * (k + 1)
    if gcd(M, conductor) != 1:
        raise ValueError("conductor must be transverse to k(k+1)")
    selected = selected_modulus_tent_contribution(k, conductor)
    if selected != 0:
        raise AssertionError("odd-support selected Walsh tent column did not vanish")
    return {
        "k": k,
        "conductor": conductor,
        "selected_modulus_tent": selected,
        "odd_support_vanishes_by_tent_symmetry": True,
    }


def symmetric_core_fixed_total_collapse(k: int, conductor: int) -> dict[str, object]:
    """Verify the symmetric reusable split sum equals the selected total-conductor column."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(conductor, bool) or not isinstance(conductor, int) or conductor <= 1 or conductor % 2 == 0:
        raise ValueError("conductor must be an odd integer >1")
    mu_m = _mobius(conductor)
    if mu_m == 0:
        raise ValueError("conductor must be squarefree")
    C = reusable_floor_product_cutoff(k)
    if conductor > C:
        raise ValueError("conductor must lie in the reusable symmetric core m<=C")
    M = k * (k + 1)
    if gcd(M, conductor) != 1:
        raise ValueError("conductor must be transverse to the pronic center")

    split_sum = Fraction(0, 1)
    rows: list[dict[str, object]] = []
    for e in _divisors(conductor):
        d = conductor // e
        if gcd(e, d) != 1:
            raise AssertionError("squarefree conductor produced noncoprime split")
        coefficient = symmetric_hyperbola_coefficient(k, e, d)
        block = biprimitive_block(M, k, e, d)
        term = coefficient * block
        split_sum += term
        rows.append(
            {
                "lower_orientation_divisor_e": e,
                "upper_orientation_divisor_d": d,
                "coefficient": coefficient,
                "biprimitive_block": block,
                "term": term,
            }
        )

    selected = selected_modulus_tent_contribution(k, conductor)
    if split_sum != selected:
        raise AssertionError("symmetric core did not collapse to selected total-conductor column")
    if mu_m == -1 and selected != 0:
        raise AssertionError("odd-support reusable conductor failed parity annihilation")

    return {
        "k": k,
        "center": M,
        "reusable_floor_cutoff_C": C,
        "total_conductor_m": conductor,
        "mobius_mu_m": mu_m,
        "support_parity": "EVEN" if mu_m == 1 else "ODD",
        "symmetric_split_sum": split_sum,
        "selected_total_conductor_column": selected,
        "odd_support_zero": mu_m == -1,
        "fixed_total_symmetric_core_collapse": True,
        "split_rows": tuple(rows),
    }
