"""Bernstein spectral-gap recovery of the exact P017 high-core correction.

This module upgrades the logarithmic moment-pressure hierarchy from an adaptive
lower bound to a universal finite-precision recovery theorem for the integer
high-complete-core Bonferroni correction.

Fix k>=3 and odd Bonferroni order m.  Put

    X = k(k+2)-1,
    z(n)=log C(n)/log X,

where C(n) is the complete transverse small-prime core of an anchor-surviving
signed basin state.  P017 complete-core dichotomy creates a genuine empty band:

    low core:  C(n)<=k-1       => z < 1/2,
    high core: C(n)=n>=k^2+1   => z > 4/5.

The first inequality follows from X>(k-1)^2.  For the second, k=3 is checked
directly.  For k>=4,

    (k^2+1)^5 > k^10 > (k+1)^8 > X^4,

so log(k^2+1)/log X > 4/5.

Let n be a positive integer degree and

    t = ceil(13n/20),
    R_n(z) = sum_{j=t}^n binom(n,j) z^j (1-z)^(n-j).

R_n is the upper tail probability of Binomial(n,z).  Hoeffding's inequality and
the fixed gaps

    13/20 - 1/2 = 3/20,
    4/5 - 13/20 = 3/20

give on the two physically admissible core bands

    R_n(z_low) <= exp(-9n/200),
    1-R_n(z_high) <= exp(-9n/200).

Let J_H be the maximum number of distinct transverse odd primes whose primorial
fits below X, and

    E_max = binom(J_H-1,m).

There are at most k signed odd points, hence the total defect mass T_m satisfies

    T_m <= U := k E_max.

If E_max=0 then H_m^core=0.  Otherwise choose

    r = ceil_log2(4U),
    n = 16r,
    epsilon = 2^(-r).

Since 16*(9/200)=0.72>log 2, both Bernstein tail errors are <=epsilon.  Define

    q = sum_x E_m(x) R_n(z(x)) - epsilon U.

Then, without knowing the exact total defect T_m,

    q <= H_m^core,
    0 <= H_m^core-q <= 2 epsilon U <= 1/2.

Because H_m^core is an integer,

    H_m^core = ceil(q).

Thus the exact high-core correction is recoverable from O(log k) logarithmic
moments, with no complete-core label classification and no exact support-tail
summation.

The Bernstein tail has the exact monomial expansion

    R_n(z)
      = sum_{ell=t}^n
          (-1)^(ell-t) binom(n,ell) binom(ell-1,t-1) z^ell.

Therefore q is a finite linear combination of the defect-weighted log moments
M_ell together with the explicit rational subtraction epsilon U.  The moment
module reconstructs every M_ell from anchor-surviving divisor fibers; nonzero
columns automatically saturate at the transverse primorial support depth.

This is a finite-precision representation theorem, not a Legendre proof.  It
recovers the correction H exactly *if the required real log moments are known*.
A machine-checked numerical ceil at large scale still requires rigorous real /
interval arithmetic; ordinary binary floats are diagnostic only.
"""

from __future__ import annotations

from math import ceil, comb, log

from .p017_p018_bonferroni_precision import signed_support_profile
from .p017_p018_core_adaptive_bonferroni import complete_transverse_core
from .p017_p018_moment_precision_ceiling import transverse_primorial_depth_below


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def ceil_log2(value: int) -> int:
    """Return the least r>=0 with 2^r>=value."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    return (value - 1).bit_length()


def bernstein_tail_coefficients(degree: int, threshold: int) -> tuple[tuple[int, int], ...]:
    """Return exact monomial coefficients of the binomial upper-tail polynomial."""
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")
    if (
        isinstance(threshold, bool)
        or not isinstance(threshold, int)
        or not (1 <= threshold <= degree)
    ):
        raise ValueError("threshold must satisfy 1<=threshold<=degree")
    return tuple(
        (
            ell,
            ((-1) ** (ell - threshold))
            * comb(degree, ell)
            * comb(ell - 1, threshold - 1),
        )
        for ell in range(threshold, degree + 1)
    )


def bernstein_tail_value(z: float, degree: int, threshold: int) -> float:
    """Evaluate R_n(z) directly in Bernstein form for bounded diagnostics."""
    if not (0.0 <= z <= 1.0):
        raise ValueError("z must lie in [0,1]")
    coefficients = bernstein_tail_coefficients(degree, threshold)
    # Direct Bernstein form is numerically much better than the alternating
    # monomial coefficients near z=1.
    return sum(
        comb(degree, j) * (z**j) * ((1.0 - z) ** (degree - j))
        for j in range(threshold, degree + 1)
    )


def bernstein_recovery_parameters(k: int, order: int) -> dict[str, object]:
    """Return the universal O(log k) degree and <=1/2 recovery-gap certificate."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    _require_order(order)

    X = k * (k + 2) - 1
    high = transverse_primorial_depth_below(k, X)
    j_high = int(high["depth"])
    emax = comb(j_high - 1, order) if j_high - 1 >= order else 0
    if emax == 0:
        return {
            "k": k,
            "order": order,
            "high_transverse_depth": j_high,
            "max_defect_per_row": 0,
            "total_defect_upper": 0,
            "epsilon_exponent": 0,
            "bernstein_degree": 0,
            "bernstein_threshold": 0,
            "epsilon_numerator": 0,
            "epsilon_denominator": 1,
            "recovery_gap_ceiling": 0.0,
            "exact_high_core_correction_is_zero": True,
        }

    total_upper = k * emax
    epsilon_exponent = ceil_log2(4 * total_upper)
    degree = 16 * epsilon_exponent
    threshold = ceil(13 * degree / 20)
    epsilon_denominator = 2**epsilon_exponent
    gap_ceiling = 2.0 * total_upper / epsilon_denominator
    if gap_ceiling > 0.5 + 1e-15:
        raise AssertionError("Bernstein parameter choice lost the half-unit recovery gap")

    return {
        "k": k,
        "order": order,
        "high_transverse_depth": j_high,
        "max_defect_per_row": emax,
        "total_defect_upper": total_upper,
        "epsilon_exponent": epsilon_exponent,
        "bernstein_degree": degree,
        "bernstein_threshold": threshold,
        "epsilon_numerator": 1,
        "epsilon_denominator": epsilon_denominator,
        "recovery_gap_ceiling": gap_ceiling,
        "exact_high_core_correction_is_zero": False,
    }


def bernstein_moment_linear_form(
    normalized_moments: tuple[float, ...],
    degree: int,
    threshold: int,
) -> float:
    """Evaluate sum E R_n(z) from normalized moments sum E z^ell.

    The tuple is indexed by ell and must reach degree.  This float routine is a
    diagnostic; rigorous integer recovery requires certified real intervals.
    """
    if len(normalized_moments) <= degree:
        raise ValueError("normalized_moments must include indices through degree")
    return sum(
        coefficient * float(normalized_moments[ell])
        for ell, coefficient in bernstein_tail_coefficients(degree, threshold)
    )


def bernstein_recovery_profile(k: int, order: int) -> dict[str, object]:
    """Bounded direct-row diagnostic of the universal recovery theorem."""
    params = bernstein_recovery_parameters(k, order)
    if bool(params["exact_high_core_correction_is_zero"]):
        return {
            **params,
            "actual_high_core_correction": 0,
            "diagnostic_q": 0.0,
            "diagnostic_gap": 0.0,
            "diagnostic_ceil_q": 0,
            "diagnostic_recovery_matches": True,
        }

    profile = signed_support_profile(k)
    X = k * (k + 2) - 1
    logX = log(X)
    degree = int(params["bernstein_degree"])
    threshold = int(params["bernstein_threshold"])
    epsilon = 1.0 / int(params["epsilon_denominator"])
    total_upper = int(params["total_defect_upper"])

    tail_sum = 0.0
    high = 0
    total_defect = 0
    for row in profile["rows"]:
        c = int(row["support_size"])
        defect = comb(c - 1, order) if c > 0 and c - 1 >= order else 0
        if defect == 0:
            continue
        state = int(row["state"])
        support = tuple(int(p) for p in row["support"])
        core = complete_transverse_core(state, support)
        z = log(core) / logX
        tail_sum += defect * bernstein_tail_value(z, degree, threshold)
        total_defect += defect
        if core > k - 1:
            high += defect

    q = tail_sum - epsilon * total_upper
    gap = high - q
    return {
        **params,
        "actual_total_defect": total_defect,
        "actual_high_core_correction": high,
        "diagnostic_tail_sum": tail_sum,
        "diagnostic_q": q,
        "diagnostic_gap": gap,
        "diagnostic_ceil_q": ceil(q),
        "diagnostic_recovery_matches": ceil(q) == high,
    }
