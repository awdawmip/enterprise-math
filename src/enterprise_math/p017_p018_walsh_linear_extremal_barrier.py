"""Cutoff-wide extremal linear-sieve barrier for the Walsh linear minorant.

Consider power cutoffs z=k^alpha for the one-sided cutoff-linear Walsh minorant

    H_z = A_z (1-c_high).

The complete-coordinate local model has high-band harmonic mass

    L_z -> log(1/alpha).

Thus an asymptotically positive local coefficient 1-L_z requires

    alpha > e^(-1).

Suppose one ignores the signed Walsh correlation and treats the two pieces by
independent classical dimension-one linear-sieve extremal bounds on the radius
sequence, whose natural level is D~k.  Then

    s = log D / log z -> 1/alpha.

A positive lower linear-sieve function requires s>2, so alpha<1/2.  The only
possible overlap with the local-margin condition is therefore

    e^(-1) < alpha < 1/2,
    2 < s < e < 3.

On 2<s<3 the standard delay-system functions are

    F(s)=2 e^gamma / s,
    f(s)=2 e^gamma log(s-1) / s,

so

    f(s)/F(s)=log(s-1).

An independent lower-bound for the base mass and upper-bound for the high-prime
first moment would need, even in the optimistic same-s extremal comparison,

    f(s) > F(s) log(s),

because log(s)=log(1/alpha) is the limiting high-band harmonic mass.  But

    log(s-1) < log(s)

for every s>2.  Hence the independent extremal treatment fails throughout the
only parameter window where both a positive base lower sieve and a positive
local Walsh margin could coexist.

Together with the endpoint regions:

* alpha>=1/2: s<=2 and the lower linear sieve has no positive main;
* alpha<=e^(-1): the Walsh local coefficient 1-log(1/alpha) is nonpositive;

this covers every power cutoff.  Therefore tuning z alone cannot make an
independent `lower base - upper first moment` linear-sieve proof work.  Any
successful use of the cutoff-linear Walsh family must retain correlation between
its signed/base and first-moment pieces (or use genuinely stronger arithmetic
input).

This is a prior-art extremal-constant routing theorem, not a statement that all
possible weighted/bilinear sieves fail, and not a Legendre proof.
"""

from __future__ import annotations

from math import e, log


def power_cutoff_extremal_diagnostic(alpha: float) -> dict[str, object]:
    """Classify one power exponent alpha against local-margin/lower-sieve barriers."""
    alpha = float(alpha)
    if not (0.0 < alpha < 1.0):
        raise ValueError("alpha must lie in (0,1)")
    s = 1.0 / alpha
    local_harmonic_limit = log(s)
    local_margin_positive = local_harmonic_limit < 1.0
    lower_sieve_positive = s > 2.0

    if 2.0 < s < 3.0:
        extremal_ratio = log(s - 1.0)
        independent_gap = extremal_ratio - local_harmonic_limit
        if independent_gap >= 0.0:
            raise AssertionError("linear-sieve extremal ratio unexpectedly beat log(s)")
    else:
        extremal_ratio = None
        independent_gap = None

    if alpha >= 0.5:
        route = "LOWER_SIEVE_NONPOSITIVE_S_LE_2"
    elif alpha <= 1.0 / e:
        route = "LOCAL_WALSH_MARGIN_NONPOSITIVE"
    else:
        if not (2.0 < s < e < 3.0):
            raise AssertionError("overlap window left 2<s<e<3")
        route = "EXTREMAL_CONSTANTS_FAIL_LOG_S_MINUS_LOG_S_MINUS_1"

    return {
        "alpha": alpha,
        "s": s,
        "local_harmonic_limit_log_s": local_harmonic_limit,
        "local_margin_positive": local_margin_positive,
        "ordinary_lower_linear_sieve_positive": lower_sieve_positive,
        "f_over_F_when_2_lt_s_lt_3": extremal_ratio,
        "independent_extremal_margin": independent_gap,
        "route_classification": route,
        "independent_linear_sieve_route_closes": False,
    }


def cutoff_family_negative_boundary() -> dict[str, object]:
    """Return the exact interval logic proving there is no power-cutoff escape."""
    lower_alpha = 1.0 / e
    upper_alpha = 0.5
    s_lower = 2.0
    s_upper = e
    if not lower_alpha < upper_alpha:
        raise AssertionError("e^-1 should lie below one half")
    if not 2.0 < e < 3.0:
        raise AssertionError("Euler e should lie in the linear-sieve 2<s<3 range")
    # Representative interior point checks the strict extremal inequality.
    alpha = 0.4
    row = power_cutoff_extremal_diagnostic(alpha)
    if row["independent_extremal_margin"] is None or row["independent_extremal_margin"] >= 0:
        raise AssertionError("representative overlap point did not retain the extremal deficit")
    return {
        "positive_local_margin_requires_alpha_gt": lower_alpha,
        "positive_ordinary_lower_sieve_requires_alpha_lt": upper_alpha,
        "only_apparent_overlap_alpha_interval": (lower_alpha, upper_alpha),
        "corresponding_s_interval": (s_lower, s_upper),
        "extremal_identity": "f(s)/F(s)=log(s-1) < log(s)=high-band harmonic mass",
        "all_power_cutoffs_fail_independent_extremal_treatment": True,
        "required_new_input": "SIGNED_CORRELATION_OR_BILINEAR_INFORMATION",
    }
