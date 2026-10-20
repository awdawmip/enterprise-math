"""Boundary-carry-only Bernstein recovery for the P017×P018 complete-core correction.

This module consumes the spectral-gap Bernstein separator and reorganizes its
moment expansion directly at the divisor-fiber level.

For one anchor-surviving signed basin state, let

    E_m = binom(c-1,m),
    z = log C / log X,
    X = k(k+2)-1,

where C is the complete transverse small-prime core.  For any function f with
f(0)=0, multivariate Newton telescoping over the prime-power level lattice and
Vandermonde's identity give an exact divisor kernel

    sum_x E_m(x) f(z_x) = sum_D K_{m,f}(D) F_surv(D).

Write D=prod p^e_p, S=supp(D), u=|S|.  A subset R of S is moment-active; every
prime with e_p>=2 must lie in R.  Put s=|R| and j=s+m-u.  The subset is
admissible exactly when 0<=j<=min(m,s-1), and its support-overlap multiplicity
is binom(s-1,j).  Its local analytic weight is the mixed forward difference

    Delta_R f = sum_(A subset R) (-1)^(s-|A|)
        f( sum_(p in R) (e_p-1+1_(p in A)) log p / log X ).

Thus K_{m,f}(D) is a finite sum of local mixed differences; the apparent ordered
O(log k)-moment expansion never has to be materialized.

For the Bernstein tail separator R_n from p017_p018_bernstein_core_recovery,
this exact kernel has a second collapse.  Decompose the anchor-surviving fiber
as

    F_surv(D) = B(D) + C_boundary(D),

where B is the anchor-Mobius floor bulk and C_boundary is the signed finite carry
mass from p017_p018_signed_boundary_carry.  For any divisor weight w(D), the bulk
has the exact Dirichlet-convolution shadow

    sum_D w(D) B(D)
      = sum_(q<=K, gcd(q,A_eff)=1)
          sum_(D|q, D transverse) w(D),
    K=k-1.

For w=K_{m,R_n}, the inner divisor sum Newton-telescopes back to

    E_m(c(q)) R_n(log C(q)/log X).

Every q<=K lies in the Bernstein low band, so if the Bernstein point error is
at most epsilon,

    0 <= Z_bulk
       <= epsilon K binom(J_L-1,m),

where J_L is the maximum transverse primorial depth below K.

On the original basin rows, the same spectral-gap theorem gives

    |Z_total-H_m^core| <= epsilon k binom(J_H-1,m),

with J_H the depth below X.  Hence the boundary-only linear form

    Z_carry = sum_D K_{m,R_n}(D) C_boundary(D)

satisfies

    |Z_carry-H_m^core|
      <= epsilon [k binom(J_H-1,m) + K binom(J_L-1,m)].

Choose r with 2^r >= 4 times the bracket and take Bernstein degree n=16r.
The current Hoeffding bound gives epsilon<=2^-r, so the right side is <=1/4.
Because H_m^core is an integer, it is the unique nearest integer to Z_carry.

Therefore the exact high-complete-core Bonferroni correction is recoverable from
**boundary carries alone** with O(log k) Bernstein precision.  The repeatable
floor-density bulk is not required information: it collapses to a low-scale
shadow and is uniformly suppressed by the separator.

This is a finite representation theorem, not a proof of Legendre's conjecture.
Rigorous numerical use of nearest-integer recovery requires certified real /
interval arithmetic for the logarithmic mixed-difference linear form.
"""

from __future__ import annotations

from itertools import combinations
from math import ceil, comb, gcd, log

from .legendre import primes_up_to
from .p017_p018_bernstein_core_recovery import (
    bernstein_tail_value,
    ceil_log2,
)
from .p017_p018_effective_anchor import effective_odd_anchor_primes
from .p017_p018_moment_precision_ceiling import transverse_primorial_depth_below


def _require_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")


def _transverse_factorization(k: int, value: int) -> dict[int, int]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    center = k * (k + 1)
    remaining = value
    factors: dict[int, int] = {}
    for prime in primes_up_to(k):
        if prime == 2 or center % prime == 0:
            continue
        if remaining % prime != 0:
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        factors[prime] = exponent
        if remaining == 1:
            break
    if remaining != 1:
        raise ValueError("value is not composed only of transverse primes <=k")
    return factors


def _mixed_log_difference(
    factorization: dict[int, int],
    active: tuple[int, ...],
    log_xmax: float,
    degree: int,
    threshold: int,
) -> float:
    """Return the local mixed forward difference of the Bernstein separator."""
    size = len(active)
    base = sum((factorization[p] - 1) * log(p) / log_xmax for p in active)
    steps = tuple(log(p) / log_xmax for p in active)
    total = 0.0
    for mask in range(1 << size):
        z = base
        bits = 0
        for index, step in enumerate(steps):
            if (mask >> index) & 1:
                z += step
                bits += 1
        total += ((-1) ** (size - bits)) * bernstein_tail_value(
            z, degree, threshold
        )
    return total


def bernstein_divisor_kernel(
    k: int,
    order: int,
    divisor: int,
    degree: int,
    threshold: int,
) -> float:
    """Return K_{m,R_n}(D) from distinct-prime active/witness compression.

    This float routine is a bounded diagnostic for the exact real identity.
    """
    _require_order(order)
    xmax = k * (k + 2) - 1
    if divisor > xmax:
        return 0.0
    factorization = _transverse_factorization(k, divisor)
    support = tuple(sorted(factorization))
    support_size = len(support)
    if support_size == 0:
        return 0.0
    mandatory = {p for p, exponent in factorization.items() if exponent >= 2}
    log_xmax = log(xmax)

    total = 0.0
    for active_size in range(1, support_size + 1):
        overlap = active_size + order - support_size
        if not (0 <= overlap <= min(order, active_size - 1)):
            continue
        support_weight = comb(active_size - 1, overlap)
        for active in combinations(support, active_size):
            if not mandatory.issubset(active):
                continue
            total += support_weight * _mixed_log_difference(
                factorization,
                active,
                log_xmax,
                degree,
                threshold,
            )
    return total


def carry_only_recovery_parameters(k: int, order: int) -> dict[str, object]:
    """Return an O(log k) Bernstein degree with <=1/4 carry-only error."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    _require_order(order)
    K = k - 1
    xmax = k * (k + 2) - 1
    low = transverse_primorial_depth_below(k, K)
    high = transverse_primorial_depth_below(k, xmax)
    j_low = int(low["depth"])
    j_high = int(high["depth"])
    low_weight = comb(j_low - 1, order) if j_low - 1 >= order else 0
    high_weight = comb(j_high - 1, order) if j_high - 1 >= order else 0
    low_upper = K * low_weight
    high_upper = k * high_weight
    total_upper = low_upper + high_upper

    if total_upper == 0:
        return {
            "k": k,
            "order": order,
            "low_transverse_depth": j_low,
            "high_transverse_depth": j_high,
            "low_bulk_defect_upper": 0,
            "basin_defect_upper": 0,
            "combined_error_weight_upper": 0,
            "epsilon_exponent": 0,
            "bernstein_degree": 0,
            "bernstein_threshold": 0,
            "carry_only_error_ceiling": 0.0,
            "exact_high_core_correction_is_zero": True,
        }

    epsilon_exponent = ceil_log2(4 * total_upper)
    degree = 16 * epsilon_exponent
    threshold = ceil(13 * degree / 20)
    denominator = 2**epsilon_exponent
    error_ceiling = total_upper / denominator
    if error_ceiling > 0.25 + 1e-15:
        raise AssertionError("carry-only Bernstein budget exceeded one quarter")

    return {
        "k": k,
        "order": order,
        "low_transverse_depth": j_low,
        "high_transverse_depth": j_high,
        "low_max_defect_per_shadow_integer": low_weight,
        "high_max_defect_per_basin_row": high_weight,
        "low_bulk_defect_upper": low_upper,
        "basin_defect_upper": high_upper,
        "combined_error_weight_upper": total_upper,
        "epsilon_exponent": epsilon_exponent,
        "epsilon_numerator": 1,
        "epsilon_denominator": denominator,
        "bernstein_degree": degree,
        "bernstein_threshold": threshold,
        "carry_only_error_ceiling": error_ceiling,
        "nearest_integer_recovery_radius": 0.5,
        "exact_high_core_correction_is_zero": False,
    }


def transverse_core_of_small_shadow(k: int, value: int) -> tuple[int, tuple[int, ...]]:
    """Return the transverse core/support of q<=k-1 for bulk-shadow diagnostics."""
    if not (1 <= value <= k - 1):
        raise ValueError("value must satisfy 1<=q<=k-1")
    center = k * (k + 1)
    remaining = value
    core = 1
    support: list[int] = []
    for prime in primes_up_to(k):
        if prime == 2 or center % prime == 0 or remaining % prime:
            continue
        support.append(prime)
        power = 1
        while remaining % prime == 0:
            remaining //= prime
            power *= prime
        core *= power
        if remaining == 1:
            break
    return core, tuple(support)


def bernstein_bulk_shadow_diagnostic(k: int, order: int) -> dict[str, object]:
    """Directly evaluate the collapsed floor bulk on q<=k-1 for small tests."""
    params = carry_only_recovery_parameters(k, order)
    if bool(params["exact_high_core_correction_is_zero"]):
        return {**params, "bulk_shadow_value": 0.0, "bulk_shadow_bound": 0.0}

    degree = int(params["bernstein_degree"])
    threshold = int(params["bernstein_threshold"])
    xmax = k * (k + 2) - 1
    log_xmax = log(xmax)
    anchors = effective_odd_anchor_primes(k)
    bulk = 0.0
    for value in range(1, k):
        if any(value % prime == 0 for prime in anchors):
            continue
        core, support = transverse_core_of_small_shadow(k, value)
        c = len(support)
        defect = comb(c - 1, order) if c > 0 and c - 1 >= order else 0
        if defect == 0:
            continue
        z = log(core) / log_xmax
        bulk += defect * bernstein_tail_value(z, degree, threshold)

    epsilon = 1.0 / int(params["epsilon_denominator"])
    bound = epsilon * int(params["low_bulk_defect_upper"])
    if bulk < -1e-15 or bulk > bound + 1e-12:
        raise AssertionError("collapsed Bernstein bulk left its low-band bound")
    return {
        **params,
        "bulk_shadow_value": bulk,
        "bulk_shadow_bound": bound,
        "bulk_shadow_nonnegative": True,
    }
