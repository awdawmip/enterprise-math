"""Label-free exact quotient channel for P017 high-product mirror tokens.

Let ``M=k(k+1)`` and ``0<|x|<k``.  For an odd high product S satisfying

    k <= S <= k(k-1),
    S | M^2-x^2,

put

    Q=(M^2-x^2)/S.

The exact quotient Q already identifies S globally, without retaining a
residual-divisor label.  Indeed

    Q >= [M^2-(k-1)^2]/[k(k-1)] > (k+1)^2 > k^2.

If two odd products S,T in the same range had the same exact quotient Q, then

    |S-T| Q = |x^2-y^2| < k^2.

Distinct odd products differ by at least two, making the left side larger than
``2k^2``.  Hence S=T.  The same equality then gives ``x^2=y^2``: the only
remaining generic ambiguity is the orientation bit ``y=±x``.

For terminal high-product tokens with support depth J>=2, that orientation bit
also disappears.  A token has a squarefree factorization ``S=A*p`` where A is
the J-prime residual-side radical and p is the one selected partner prime:

    A | M-x,
    p | M+x.

If another terminal token with the same S,Q lived at -x, its J-prime residual
radical B would divide ``M+x`` and also S=A*p.  But every prime of A is odd and
transverse, so ``gcd(A,M+x)=1``; therefore B would have to divide the single
prime p, impossible when J>=2.  Thus exact Q is injective on terminal
high-product rows.

Together with the coarser square decoder this gives a strict precision tradeoff:

* exact Q: zero-repair and label-free;
* square root R_2(Q): zero-repair after retaining A.

This is an integer routing theorem, not a Legendre proof.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime
from .p017_high_product_split_geometry import _factor_squarefree
from .p017_mirror_product_bridge import p017_mirror_product_embedding


def exact_high_product_quotient(k: int, signed_point: int, product_value: int) -> dict[str, int]:
    """Return the exact high-product quotient and certify its >k^2 floor."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(signed_point, bool) or not isinstance(signed_point, int) or signed_point == 0 or abs(signed_point) >= k:
        raise ValueError("signed_point must satisfy 0<|x|<k")
    if isinstance(product_value, bool) or not isinstance(product_value, int) or product_value % 2 == 0 or not (k <= product_value <= k * (k - 1)):
        raise ValueError("product_value must be odd and satisfy k<=S<=k(k-1)")

    mirror_product = int(p017_mirror_product_embedding(k, abs(signed_point))["product"])
    if mirror_product % product_value:
        raise ValueError("S must divide the mirror product")
    quotient = mirror_product // product_value
    if quotient <= k * k:
        raise AssertionError("high-product exact quotient failed the Q>k^2 barrier")
    return {
        "k": k,
        "signed_point": signed_point,
        "combined_product": product_value,
        "mirror_product": mirror_product,
        "exact_joint_quotient": quotient,
    }


def exact_quotient_collision_kernel(
    k: int,
    left_point: int,
    left_product: int,
    right_point: int,
    right_product: int,
) -> dict[str, object]:
    """Certify that equal exact Q forces the same S and the same |x|."""
    left = exact_high_product_quotient(k, left_point, left_product)
    right = exact_high_product_quotient(k, right_point, right_product)
    q_left = int(left["exact_joint_quotient"])
    q_right = int(right["exact_joint_quotient"])
    if q_left != q_right:
        raise ValueError("the two high-product observations do not share an exact quotient")
    quotient = q_left

    product_gap = abs(left_product - right_product)
    square_gap = abs(left_point * left_point - right_point * right_point)
    if product_gap * quotient != square_gap:
        raise AssertionError("exact quotient collision identity failed")
    if left_product != right_product:
        if product_gap < 2:
            raise AssertionError("distinct odd products lost their even gap")
        if not product_gap * quotient > 2 * k * k:
            raise AssertionError("Q>k^2 failed to dominate a distinct odd product gap")
        if not square_gap < k * k:
            raise AssertionError("signed radius-square moving budget reached k^2")
        raise AssertionError("distinct high products cannot share an exact quotient")
    if abs(left_point) != abs(right_point):
        raise AssertionError("same S,Q failed to recover the signed-radius magnitude")

    return {
        "k": k,
        "exact_joint_quotient": quotient,
        "combined_product": left_product,
        "left_signed_point": left_point,
        "right_signed_point": right_point,
        "same_product": True,
        "same_radius_magnitude": True,
        "orientation_ambiguous": left_point == -right_point,
    }


def terminal_exact_quotient_injectivity(
    k: int,
    left_point: int,
    left_residual_radical: int,
    left_partner_prime: int,
    right_point: int,
    right_residual_radical: int,
    right_partner_prime: int,
) -> dict[str, object]:
    """Equal exact Q on two J>=2 terminal tokens forces the identical signed row."""
    for name, value in (
        ("left_residual_radical", left_residual_radical),
        ("right_residual_radical", right_residual_radical),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 3 or value % 2 == 0:
            raise ValueError(f"{name} must be an odd squarefree product")
        _factor_squarefree(value)
    for name, value in (
        ("left_partner_prime", left_partner_prime),
        ("right_partner_prime", right_partner_prime),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 3 or value % 2 == 0 or not is_prime(value):
            raise ValueError(f"{name} must be an odd prime")

    left_support = _factor_squarefree(left_residual_radical)
    right_support = _factor_squarefree(right_residual_radical)
    if len(left_support) != len(right_support) or len(left_support) < 2:
        raise ValueError("terminal residual radicals must have the same support depth J>=2")
    if left_partner_prime in left_support or right_partner_prime in right_support:
        raise ValueError("partner prime must lie outside its residual radical")

    center = k * (k + 1)
    for point, radical, prime in (
        (left_point, left_residual_radical, left_partner_prime),
        (right_point, right_residual_radical, right_partner_prime),
    ):
        if (center - point) % radical or (center + point) % prime:
            raise ValueError("terminal token lost one side of its sign-split divisibility")
        if gcd(radical * prime, center) != 1:
            raise ValueError("terminal high-product label must be transverse to M")

    left_product = left_residual_radical * left_partner_prime
    right_product = right_residual_radical * right_partner_prime
    kernel = exact_quotient_collision_kernel(
        k,
        left_point,
        left_product,
        right_point,
        right_product,
    )

    if left_point == -right_point and left_point != right_point:
        # Equal S plus opposite orientation would make the second residual
        # radical divide M+left_point.  It also divides S=A*p.  Since every
        # prime of A is transverse and A|M-left_point, gcd(A,M+left_point)=1;
        # the second J-prime radical would therefore have to divide p.
        if gcd(left_residual_radical, center + left_point) != 1:
            raise AssertionError("transverse residual radical unexpectedly divides both mirror sides")
        if (center + left_point) % right_residual_radical:
            raise AssertionError("opposite-orientation residual divisibility was lost")
        if left_product % right_residual_radical:
            raise AssertionError("same combined product lost the second residual radical")
        if left_partner_prime % right_residual_radical == 0:
            raise AssertionError("a J>=2 squarefree radical divided one prime")
        raise AssertionError("opposite orientations cannot both be J>=2 terminal high-product rows")

    if left_point != right_point:
        raise AssertionError("terminal exact quotient failed signed-row injectivity")
    return {
        **kernel,
        "terminal_support_depth": len(left_support),
        "signed_row_injective": True,
        "remaining_repair_bits": 0,
    }
