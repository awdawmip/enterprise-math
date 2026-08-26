"""Zero-repair square-root decoder for P017 high-product sign-split tokens.

Let ``M=k(k+1)`` and ``0<|x|<k``.  Suppose an odd residual divisor ``A`` and
an odd partner factor ``p`` satisfy

    1 <= A < k,
    1 <= p <= k,
    A*p | M^2-x^2.

Write ``S=A*p`` and assume the high-product regime ``S>=k``.  Put

    t = R_2((M^2-x^2)/S).

The residual divisor A is enough to decode p (hence S) from t with zero repair.
No assumption ``S<k`` is used.

Indeed S<=k(k-1).  With

    L=M^2-(k-1)^2,
    U=M^2-1,

we have

    (M^2-x^2)/S >= L/[k(k-1)] > (k+1)^2,

so ``t>=k+1``.  Any other product T=A*q with odd ``q<=k`` producing the same
square root must lie in the common moving-state decoder interval

    L/(t+1)^2 < T <= U/t^2.

Its rational width W satisfies ``W<2A``.  The proof uses the actual product
``S=A*p`` only to note

    A = S/p > L/[k(t+1)^2],

while for every ``t>=k+1``

    U/t^2 - L/(t+1)^2 < 2L/[k(t+1)^2].

The latter inequality reduces at the worst case ``t=k+1`` to

    L(k+1)^2 - kU(k+2)
      = 2k^3+4k^2+2k-1 > 0.

Distinct odd q values differ by at least two, so the corresponding multiples
A*q differ by at least ``2A`` and cannot both fit.  Thus ``(A,t)`` recovers the
unique odd partner quotient p and combined product S.

Combining this with the high-product sign-split single-use theorem gives a
second consequence: for fixed A, different valid high-product signed rows have
different square-root channel states t.  The result is a routing/injectivity
theorem, not a Legendre proof.
"""

from __future__ import annotations

from .core import integer_nth_root
from .p017_mirror_product_bridge import p017_mirror_product_embedding


def high_product_square_candidate_window(k: int, square_root: int) -> dict[str, int]:
    """Return the integer product interval compatible with one square-root state."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if (
        isinstance(square_root, bool)
        or not isinstance(square_root, int)
        or square_root < k + 1
    ):
        raise ValueError("high-product square root must be an integer >=k+1")

    center = k * (k + 1)
    lower_numerator = center * center - (k - 1) * (k - 1)
    upper_numerator = center * center - 1
    t = square_root
    minimum = lower_numerator // ((t + 1) * (t + 1)) + 1
    maximum = upper_numerator // (t * t)
    return {
        "k": k,
        "square_root": t,
        "minimum_product": minimum,
        "maximum_product": maximum,
        "integer_width": max(0, maximum - minimum + 1),
        "lower_numerator": lower_numerator,
        "upper_numerator": upper_numerator,
    }


def selected_residual_divisor_square_decoder(
    k: int,
    signed_point: int,
    residual_divisor: int,
    partner_factor: int,
) -> dict[str, object]:
    """Decode S=A*p from the pair (A, square-root channel) with zero repair."""
    if isinstance(signed_point, bool) or not isinstance(signed_point, int) or signed_point == 0 or abs(signed_point) >= k:
        raise ValueError("signed_point must satisfy 0<|x|<k")
    if isinstance(residual_divisor, bool) or not isinstance(residual_divisor, int) or not (1 <= residual_divisor < k) or residual_divisor % 2 == 0:
        raise ValueError("residual_divisor must be odd and satisfy 1<=A<k")
    if isinstance(partner_factor, bool) or not isinstance(partner_factor, int) or not (1 <= partner_factor <= k) or partner_factor % 2 == 0:
        raise ValueError("partner_factor must be odd and satisfy 1<=p<=k")

    center = k * (k + 1)
    product_value = residual_divisor * partner_factor
    if product_value < k:
        raise ValueError("decoder requires the high-product regime A*p>=k")
    mirror_product = int(p017_mirror_product_embedding(k, abs(signed_point))["product"])
    if mirror_product % product_value:
        raise ValueError("A*p must divide the mirror product")
    quotient = mirror_product // product_value
    root = integer_nth_root(quotient, 2)
    if root < k + 1:
        raise AssertionError("A*p<=k(k-1) failed to force square-root state >=k+1")

    window = high_product_square_candidate_window(k, root)
    minimum = int(window["minimum_product"])
    maximum = int(window["maximum_product"])
    if not minimum <= product_value <= maximum:
        raise AssertionError("true high product escaped the square-root decoder window")

    # Exact rational-width proof.  W < 2A is checked without floating point.
    lower_numerator = int(window["lower_numerator"])
    upper_numerator = int(window["upper_numerator"])
    width_numerator = (
        upper_numerator * (root + 1) * (root + 1)
        - lower_numerator * root * root
    )
    width_denominator = root * root * (root + 1) * (root + 1)
    if width_numerator >= 2 * residual_divisor * width_denominator:
        raise AssertionError("high-product square decoder width reached 2A")

    first_multiple = ((minimum + residual_divisor - 1) // residual_divisor) * residual_divisor
    multiples = tuple(range(first_multiple, maximum + 1, residual_divisor))
    odd_quotient_products = tuple(
        value
        for value in multiples
        if (value // residual_divisor) % 2 == 1 and value // residual_divisor <= k
    )
    if len(odd_quotient_products) != 1 or odd_quotient_products[0] != product_value:
        raise AssertionError("(A,square-root) did not uniquely decode the odd partner quotient")

    return {
        **window,
        "signed_point": signed_point,
        "residual_divisor": residual_divisor,
        "partner_factor": partner_factor,
        "combined_product": product_value,
        "mirror_product": mirror_product,
        "joint_quotient": quotient,
        "decoder_width_numerator": width_numerator,
        "decoder_width_denominator": width_denominator,
        "decoder_width_less_than_2A": True,
        "candidate_multiples_of_A": multiples,
        "candidate_odd_partner_products": odd_quotient_products,
        "decoded_partner_factor": partner_factor,
        "decoded_product": product_value,
        "remaining_repair_bits": 0,
    }
