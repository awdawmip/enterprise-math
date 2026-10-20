"""One-third Euclidean descent for the irreducible symmetric Walsh reusable core.

The incidence-optimal symmetric compiler has reusable total conductors

    1<m<=C=floor((k-1)/2).

After fixed-total-conductor recoalescence, one such column is the selected
Walsh tent column B_m(k).  Put

    k=a*m+r,       0<=r<m.

Transversality to k(k+1) excludes r=0 (and r=m-1), while m<=C forces a>=2.
Since r<m,

    k=a*m+r >=2m+r >3r,

so

    0<r<k/3.

The exact Euclidean remainder theorem gives

    B_m(k)=(r/k)B_m(r).

At the child scale the same conductor satisfies m>r, hence it is already in the
single-use regime: every fixed orientation root class modulo m (or 2m with odd
parity) can occur at most once in the child radius window.

Therefore every nontrivial reusable symmetric-core conductor executes in one
strictly cubic-contracted child world, with transport weight

    r/k < 1/3,

and needs no further same-conductor reuse descent there.  This strengthens the
generic half-scale Walsh Euclidean descent specifically on the actual
floor-forced symmetric core.

The theorem does not bound the sum of all child root classes and does not prove
Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff
from .p017_p018_walsh_remainder_descent import selected_modulus_tent_contribution


def symmetric_core_cubic_descent(k: int, conductor: int) -> dict[str, object]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    if isinstance(conductor, bool) or not isinstance(conductor, int) or conductor <= 1 or conductor % 2 == 0:
        raise ValueError("conductor must be an odd integer >1")
    C = reusable_floor_product_cutoff(k)
    if conductor > C:
        raise ValueError("conductor must lie in the reusable symmetric core m<=C")
    if gcd(conductor, k * (k + 1)) != 1:
        raise ValueError("conductor must be transverse to the parent center")

    a, r = divmod(k, conductor)
    if a < 2:
        raise AssertionError("reusable-core conductor did not have quotient at least two")
    if r == 0:
        raise AssertionError("transverse conductor divided k")
    if not r < conductor:
        raise AssertionError("Euclidean remainder escaped conductor")
    if not 3 * r < k:
        raise AssertionError("reusable-core child failed strict one-third contraction")

    parent = selected_modulus_tent_contribution(k, conductor)
    child = selected_modulus_tent_contribution(r, conductor)
    reconstructed = Fraction(r, k) * child
    if parent != reconstructed:
        raise AssertionError("selected Walsh column failed Euclidean cubic descent")

    return {
        "k": k,
        "reusable_floor_cutoff_C": C,
        "parent_conductor_m": conductor,
        "euclidean_quotient_a": a,
        "child_scale_r": r,
        "parent_selected_column": parent,
        "child_selected_column": child,
        "transport_weight_r_over_k": Fraction(r, k),
        "strict_one_third_contraction": True,
        "child_conductor_exceeds_child_scale": conductor > r,
        "child_root_classes_single_use": conductor > r,
        "euclidean_reconstruction": reconstructed,
    }
