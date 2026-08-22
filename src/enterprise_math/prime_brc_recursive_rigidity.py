"""Prime-BRC recursive exact-support rigidity in the square basin.

Owner-local L3 research support.

For 1<=d<=k, the exact quotient image of all d-multiples in
I_k={k^2+1,...,(k+1)^2-1} is the consecutive integer window

    Q_d(k)=[floor(k^2/d)+1, floor(k(k+2)/d)].

The lower endpoint is strictly decreasing in d on [1,k].  Indeed for d<e<=k,

    k^2/d-k^2/e >= k^2/(k(k-1)) = k/(k-1) > 1.

Hence distinct cumulative divisors d,e<=k never have equal exact quotient
supports.  Combined with P017-L020's S_k(n)<=k on the large-prime-tail branch,
this means exact recursive factor semantics cannot recoalesce different
cumulative small-core divisors merely after division.  Only paths with the same
cumulative divisor can forget factor order by floor-quotient path flattening.

Coarser observables (root, tail, Boolean summaries) may merge distinct quotient
windows, but such a merge is suffix-safe only for the explicitly declared
coarser future task; it cannot be silently reused for later exact factorization.
"""

from __future__ import annotations


def quotient_support(k: int, divisor: int) -> tuple[int, ...]:
    if k < 1 or not 1 <= divisor <= k:
        raise ValueError("require k>=1 and 1<=divisor<=k")
    lo = k * k // divisor + 1
    hi = (k * (k + 2)) // divisor
    if lo > hi:
        raise AssertionError("divisor <=k unexpectedly has empty quotient support")
    return tuple(range(lo, hi + 1))


def quotient_support_rigidity(k: int, d: int, e: int) -> dict[str, object]:
    """Certify Q_d(k)!=Q_e(k) for distinct 1<=d,e<=k."""
    if k < 2 or not (1 <= d <= k and 1 <= e <= k) or d == e:
        raise ValueError("require k>=2 and distinct d,e in [1,k]")
    small, large = sorted((d, e))
    left_small = k * k // small + 1
    left_large = k * k // large + 1
    if not left_small > left_large:
        raise AssertionError("quotient-window lower endpoints lost strict order")
    qd = quotient_support(k, d)
    qe = quotient_support(k, e)
    if qd == qe:
        raise AssertionError("distinct cumulative divisors acquired equal quotient support")
    return {
        "k": k,
        "d": d,
        "e": e,
        "Q_d": qd,
        "Q_e": qe,
        "lower_endpoint_strict_order": True,
        "equal_support": False,
    }


def root_only_cancellation_witness() -> dict[str, object]:
    """Show why root-level equality is not recursive suffix equivalence.

    In k=22, d=15 and d=17 have different exact quotient supports but every
    quotient lies in root basin 5.  Their squarefree Möbius signs are opposite,
    so a signed *root-terminal* observable can cancel +3[5]-3[5].  Yet exact
    quotient supports differ, so the cancellation is invalid if future work
    still factors the quotient values.
    """
    k = 22
    q15 = quotient_support(k, 15)
    q17 = quotient_support(k, 17)
    if q15 != (33, 34, 35) or q17 != (29, 30, 31):
        raise AssertionError("root-only witness quotient windows changed")
    roots15 = tuple(int(x**0.5) for x in q15)
    roots17 = tuple(int(x**0.5) for x in q17)
    if roots15 != (5, 5, 5) or roots17 != (5, 5, 5):
        raise AssertionError("root-only witness root multiplicities changed")
    return {
        "k": k,
        "positive_modulus": 15,
        "negative_modulus": 17,
        "Q_15": q15,
        "Q_17": q17,
        "root_multiset": ((5, 3),),
        "signed_root_sum": 0,
        "exact_quotient_supports_equal": False,
        "verdict": "ROOT_TERMINAL_CANCELLATION_ONLY_NOT_RECURSIVE_SUFFIX_EQUIVALENCE",
    }
