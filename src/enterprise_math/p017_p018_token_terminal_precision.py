"""The least globally single-use token order is automatically one-step terminal.

Let P_perp(k,j) be the product of the first j odd primes transverse to
M=k(k+1), and let

    J = max{j : P_perp(k,j) < k}.

The adjacent precision theorem defines the least globally single-use odd token
order as

    m_* = least positive odd m with m >= J.

Put r=m_*+1.  Then r>J, so the r-prime transverse prefix A=P_perp(k,r)
reaches or exceeds k (unless fewer than r usable primes exist, in which case no
order-m_* defect token exists).  Every prime in A is transverse to M, so A
cannot equal k or k+1; hence

    A >= k+2.

If 2r transverse primes exist, write the 2r-prefix product as A*B where B is the
product of the next r transverse primes.  Those primes are termwise larger than
the first r, so B>A and therefore

    P_perp(k,2r)=A*B > (k+2)^2 > k(k+2).

Thus no state in the open k-th square basin can contain 2r=2m_*+2 distinct
transverse support primes.  Every parent support has size at most 2m_*+1.

At the same time A>=k makes every order-m_* squarefree defect token globally
single-use by P017 CG12.  Full-block token descent removes exactly r=m_*+1
support directions and leaves quotient support size at most

    (2m_*+1)-(m_*+1)=m_*.

Hence the order-m_* Bonferroni defect is zero after one full-block quotient
descent.  The quotient also satisfies q<=k, so its square-root complexity scale
is at most R_2(k)<k.

Therefore the least order needed to make all defect tokens globally single-use
is already sufficient for one-step same-order terminalization; the support
barrier is not an independent hypothesis at that order.

This is a P017/P018 bridge theorem about proof-detail transport.  It does not
show that the original basin has a prime and does not promote CG12 itself out of
its PROVED_WIP owner status.
"""

from __future__ import annotations

from .p017_p018_token_reuse_precision import least_global_single_use_odd_order
from .p017_p018_token_support_descent import one_step_token_terminal_criterion
from .p017_p018_transverse_primorial import transverse_odd_primorial


def least_single_use_order_is_one_step_terminal(k: int) -> dict[str, object]:
    """Certify that the minimal token-single-use odd order is one-step terminal."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")

    token = least_global_single_use_odd_order(k)
    order = int(token["least_global_single_use_odd_order"])
    r = order + 1
    first = transverse_odd_primorial(k, r)
    double = transverse_odd_primorial(k, 2 * r)
    criterion = one_step_token_terminal_criterion(k, order)

    if bool(first["complete"]):
        first_product = int(first["product"])
        if first_product < k:
            raise AssertionError("minimal single-use order did not cross the k token threshold")
        if first_product in (k, k + 1):
            raise AssertionError("transverse prime product cannot equal an anchor factor")
        if first_product < k + 2:
            raise AssertionError("transverse token threshold failed A>=k+2")

    if bool(double["complete"]):
        first_product = int(first["product"])
        double_product = int(double["product"])
        if double_product <= k * (k + 2):
            raise AssertionError("double transverse prefix did not clear the basin state ceiling")
        if first_product <= 0 or double_product % first_product:
            raise AssertionError("double prefix failed exact factorization by the first prefix")
        second_block = double_product // first_product
        if second_block <= first_product:
            raise AssertionError("second transverse prime block is not strictly larger")
    else:
        second_block = None

    if not bool(criterion["all_defect_tokens_single_use"]):
        raise AssertionError("minimal single-use proof order failed its own token threshold")
    if not bool(criterion["all_parent_support_sizes_at_most_2m_plus_1"]):
        raise AssertionError("minimal single-use order failed the automatic support barrier")
    if not bool(criterion["one_step_same_order_terminal"]):
        raise AssertionError("minimal single-use order is not one-step same-order terminal")

    return {
        "k": k,
        "transverse_primorial_depth": int(token["transverse_primorial_depth"]),
        "least_global_single_use_odd_order": order,
        "selected_support_directions_per_token": r,
        "first_token_prefix": first,
        "double_support_prefix": double,
        "second_prime_block_product": second_block,
        "criterion": criterion,
        "one_step_same_order_terminal": True,
        "child_square_root_scale_ceiling": criterion["parent_root_ceiling"],
    }
