"""Critical root precision for moving mirror-product labels.

CG12-CG14 show that a cubic observation of

    (M^2-r^2)/S

has at most two odd product candidates, and that one nontrivial divisor of the
true product removes the remaining ambiguity.  This module closes the opposite
side of that story.

CG15 gives the exact observation-only candidate interval for every root degree.
CG16 constructs, for every degree m>=4, arbitrarily large families of distinct
odd product labels that produce the same m-th root.  Thus degree three is the
largest root degree for which this moving-state product observation has a
uniform constant repair bound from the root state alone.

The construction concerns valid divisor labels S of mirror products.  It does
not claim that every constructed S is the exact P017 full-core product of the
corresponding radius; exact-full-core restrictions can only reduce the fiber.
"""

from __future__ import annotations

from .core import integer_nth_root
from .p017_mirror_product_bridge import joint_product_root


def power_product_candidate_window(
    k: int,
    observed_root: int,
    degree: int,
) -> dict[str, object]:
    """CG15: exact universal product-label window for one m-th-root observation.

    If an odd label 1<=S<k and radius 1<=r<k satisfy

        observed_root = R_m((M^2-r^2)/S),
        M=k(k+1),

    then necessarily

        [M^2-(k-1)^2] / (t+1)^m < S <= [M^2-1] / t^m.

    The returned odd-candidate set is therefore a finite observation-only repair
    set.  It can contain labels that are not actually realized by a radius or
    that are not exact full-core products; those additional constraints are
    deliberately not smuggled into this universal decoder.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 2:
        raise ValueError("degree must be an integer >= 2")
    if isinstance(observed_root, bool) or not isinstance(observed_root, int) or observed_root < 1:
        raise ValueError("observed_root must be a positive integer")

    center = k * (k + 1)
    lower_numerator = center * center - (k - 1) * (k - 1)
    lower_denominator = (observed_root + 1) ** degree
    upper_numerator = center * center - 1
    upper_denominator = observed_root**degree

    minimum = lower_numerator // lower_denominator + 1
    maximum = upper_numerator // upper_denominator
    minimum = max(1, minimum)
    maximum = min(k - 1, maximum)
    odd_candidates = (
        tuple(value for value in range(minimum, maximum + 1) if value % 2 == 1)
        if minimum <= maximum
        else ()
    )

    width_numerator = (
        upper_numerator * lower_denominator
        - lower_numerator * upper_denominator
    )
    width_denominator = upper_denominator * lower_denominator

    return {
        "k": k,
        "degree": degree,
        "observed_root": observed_root,
        "minimum_product": minimum,
        "maximum_product": maximum,
        "odd_candidates": odd_candidates,
        "candidate_count": len(odd_candidates),
        "width_numerator": width_numerator,
        "width_denominator": width_denominator,
    }


def unbounded_power_collision_family(degree: int, scale: int) -> dict[str, object]:
    """CG16: every root degree m>=4 has unbounded actual label ambiguity.

    Let m>=4, u>=2 and set

        k=u^m,
        M=k(k+1).

    For each 1<=j<u such that S_j=k-j is odd, put

        S_j=k-j,
        r_j=j(j+1).

    Then r_j<k and

        M-r_j=(k-j)(k+j+1)=S_j(k+j+1),

    so S_j is a genuine odd divisor label of the lower mirror state and hence of
    the mirror product.  The joint quotient is exactly

        Q_j=(k+j+1)(k(k+1)+j(j+1))
           =k^3+(j+2)k^2+(j+1)^2 k+j(j+1)^2.

    The lower bound Q_j>k^3=(u^3)^m is immediate.  For the upper bound, j<u,
    u>=2 and m>=4 give

        Q_j-k^3 < 2 u^(2m+1)
                 < m u^(3m-3)
                 <= (u^3+1)^m-u^(3m).

    Therefore

        R_m(Q_j)=u^3

    for every retained j.  There are exactly floor(u/2) such parity-compatible
    j values, so one m-th-root state has at least floor(u/2) distinct odd product
    labels.  The ambiguity is unbounded as u grows.

    This proves a sharp precision threshold for the universal moving-state
    product observation: cubic degree has constant two-label repair (CG12),
    while every degree m>=4 admits unbounded label fibers.  Extra side
    information such as an exact endpoint core may still repair those fibers.
    """
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 4:
        raise ValueError("degree must be an integer >= 4")
    if isinstance(scale, bool) or not isinstance(scale, int) or scale < 2:
        raise ValueError("scale must be an integer >= 2")

    u = scale
    k = u**degree
    center = k * (k + 1)
    common_root = u**3
    entries: list[dict[str, int]] = []

    for j in range(1, u):
        product_label = k - j
        if product_label % 2 == 0:
            continue
        radius = j * (j + 1)
        if not (1 <= radius < k):
            raise AssertionError("critical-family radius left the mirror interval")
        lower = center - radius
        if lower % product_label != 0:
            raise AssertionError("critical-family product label lost exact divisibility")

        quotient_data = joint_product_root(k, radius, product_label)
        quotient = int(quotient_data["joint_quotient"])
        observed = integer_nth_root(quotient, degree)
        if observed != common_root:
            raise AssertionError("critical-family m-th-root state is not u^3")

        exact_formula = (k + j + 1) * (k * (k + 1) + j * (j + 1))
        if quotient != exact_formula:
            raise AssertionError("critical-family quotient formula failed")
        expanded = (
            k**3
            + (j + 2) * k * k
            + (j + 1) * (j + 1) * k
            + j * (j + 1) * (j + 1)
        )
        if quotient != expanded:
            raise AssertionError("critical-family expanded quotient formula failed")
        if not (common_root**degree < quotient < (common_root + 1) ** degree):
            raise AssertionError("critical-family quotient escaped the common root basin")

        window = power_product_candidate_window(k, common_root, degree)
        if product_label not in window["odd_candidates"]:
            raise AssertionError("critical-family label escaped the universal decoder window")

        entries.append(
            {
                "j": j,
                "product_label": product_label,
                "radius": radius,
                "quotient": quotient,
                "root": observed,
            }
        )

    expected_count = u // 2
    if len(entries) != expected_count:
        raise AssertionError("critical-family parity count is not floor(u/2)")
    if len({entry["product_label"] for entry in entries}) != expected_count:
        raise AssertionError("critical-family product labels are not distinct")

    return {
        "degree": degree,
        "scale": u,
        "k": k,
        "common_root": common_root,
        "entries": tuple(entries),
        "label_count": len(entries),
        "expected_label_count": expected_count,
    }
