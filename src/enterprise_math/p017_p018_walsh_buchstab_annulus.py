"""Prime-extraction/Buchstab annulus transport for one-sided mixed Walsh boundary.

For squarefree R=p*R' and any integer budget B>=0,

    S_R(B)=sum_{b|R,b<=B} mu(b)

splits according to whether p divides b:

    S_R(B)=S_R'(B)-S_R'(floor(B/p))
          =sum_{d|R', floor(B/p)<d<=B} mu(d).

In the one-sided Walsh hyperbola the budget is B=floor(C/a), with
C=floor((k-1)/2) and an opposite-side squarefree divisor a.  The nested floors
collapse exactly:

    floor(floor(C/a)/p)=floor(C/(a*p)).

Therefore

    S_R(floor(C/a))
      = sum_{d|R/p, C/p < a*d <= C} mu(d).

Thus every truncated target-side Mobius sum can be transported to a top annulus
of the reusable product range.  Restoring the extracted target prime p gives

    p*a*d > C.

The corresponding signed mixed root pattern has period 2*p*a*d > k-1 and is
therefore globally single-use in the physical radius window.  This holds for
*any* chosen p|R, so prime extraction is a gauge coordinate: one may choose a
target prime that makes the annulus most useful for the subsequent estimate.

This is an exact Buchstab/BRC transport theorem.  It turns arbitrary truncated
Mobius depth into single-use crossing-token geometry, but it does not bound the
number or signed sum of those tokens and does not prove Legendre's conjecture.
"""

from __future__ import annotations

from math import prod

from .p017_p018_walsh_complement_transport import (
    squarefree_divisors_with_mu,
    truncated_divisor_mobius,
)


def prime_extracted_truncated_mobius(radical: int, prime: int, budget: int) -> dict[str, object]:
    """Verify S_R(B)=sum_{d|R/p,B/p<d<=B}mu(d)."""
    if radical <= 1 or budget < 0:
        raise ValueError("radical must be >1 and budget nonnegative")
    if prime <= 1 or radical % prime:
        raise ValueError("prime must divide radical")
    reduced = radical // prime
    # squarefree_divisors_with_mu validates squarefreeness of each argument.
    full_rows = squarefree_divisors_with_mu(radical)
    reduced_rows = squarefree_divisors_with_mu(reduced)
    # p is a genuine prime factor iff removing it flips Mobius sign and leaves
    # a squarefree coprime reduced radical.
    mu_R = next(mu for d, mu in full_rows if d == radical)
    mu_reduced = next(mu for d, mu in reduced_rows if d == reduced)
    if mu_R != -mu_reduced:
        raise ValueError("declared factor is not a single squarefree prime factor")

    direct = truncated_divisor_mobius(radical, budget)
    lower = budget // prime
    annulus_rows = tuple((d, mu) for d, mu in reduced_rows if lower < d <= budget)
    annulus = sum(mu for _d, mu in annulus_rows)
    if direct != annulus:
        raise AssertionError("prime-extracted Mobius annulus identity failed")
    return {
        "radical_R": radical,
        "extracted_prime_p": prime,
        "reduced_radical_R_over_p": reduced,
        "budget_B": budget,
        "lower_budget_floor_B_over_p": lower,
        "direct_truncated_mobius_sum": direct,
        "annulus_mobius_sum": annulus,
        "annulus_divisor_rows": annulus_rows,
        "prime_extraction_identity": True,
    }


def walsh_buchstab_annulus(k: int, opposite_divisor: int, target_radical: int, extracted_prime: int) -> dict[str, object]:
    """Transport B=floor(C/a) to C/p < a*d <= C and certify single-use crossing."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if opposite_divisor < 1:
        raise ValueError("opposite_divisor must be positive")
    C = (k - 1) // 2
    a = opposite_divisor
    B = C // a
    data = prime_extracted_truncated_mobius(target_radical, extracted_prime, B)
    p = extracted_prime

    rows: list[dict[str, int | bool]] = []
    for d, mu in data["annulus_divisor_rows"]:
        mixed_low = a * d
        crossing = p * mixed_low
        if not (p * mixed_low > C and mixed_low <= C):
            raise AssertionError("Buchstab annulus term left C/p < a*d <= C")
        period = 2 * crossing
        if period <= k - 1:
            raise AssertionError("crossing token is not globally single-use")
        rows.append(
            {
                "opposite_divisor_a": a,
                "target_reduced_divisor_d": d,
                "mu_d": mu,
                "mixed_low_product_ad": mixed_low,
                "crossing_product_pad": crossing,
                "signed_period_2pad": period,
                "single_use": True,
            }
        )

    return {
        **data,
        "k": k,
        "reusable_floor_cutoff_C": C,
        "opposite_divisor_a": a,
        "walsh_budget_floor_C_over_a": B,
        "annulus_lower_ratio_prime": p,
        "annulus_rows": tuple(rows),
        "all_annulus_terms_single_use": all(bool(row["single_use"]) for row in rows),
        "prime_extraction_gauge": True,
    }
