"""Fixed-anchor Selberg--Delange interface for the residual singular core mass.

Prior art used here is the non-negative multiplicative-function theorem of
R. de la Bretèche and G. Tenenbaum, *Remarks on the Selberg--Delange method*,
Acta Arith. 200 (2021), Theorem 2.1, DOI 10.4064/aa201024-26-5.

Fix M.  After factoring out the generic odd two-linear-form product, define on
allowed odd primes p∤M

    f_M(p^nu) = 2(p-1)/(p-2)    (nu>=1),

and put f_M(p^nu)=0 at p=2 and p|M.  This is non-negative and multiplicative.
For allowed primes

    f_M(p)=2+2/(p-2),

so the prime average has parameter r=2 by the prime number theorem; the
prime-power square/convergence hypothesis of Theorem 2.1 holds for every fixed
sigma>1/2 because the prime-power values are uniformly bounded.  The theorem
therefore gives

    sum_{n<=x} f_M(n) = lambda_M x log x + O_M(x).

The exact local cancellation proved in ``p017_p018_singular_core_euler`` gives

    C_M lambda_M = delta_M^2/4,

where C_M is the factored generic odd twin product and

    delta_M = prod_{odd p|M}(1-1/p).

Partial summation then yields the fixed-M singular leading-core asymptotic

    C_M sum_{n<=x} f_M(n)/n
      = (delta_M^2/8) log(x)^2 + O_M(log x).

For the ``-2`` correction in the ordered nontrivial split count
``2^omega(S)-2``, use instead

    g_M(p^nu)=(p-1)/(p-2).

Its prime-average parameter is r=1, so its weighted partial sum is only
O_M(log x); it cannot change the log^2 leading coefficient.  Thus the same
``delta_M^2/8`` coefficient belongs to the ordered-split singular core mass.

Important boundary: M=k(k+1) moves in P017.  This file records a fixed-M theorem
and exact coefficient only.  It does not claim that the O_M(log x) remainder is
uniform in k.  The separate Rankin module supplies a rigorous moving-M upper
bound without the sharp coefficient.
"""

from __future__ import annotations

from .legendre import is_prime
from .p017_p018_singular_core_euler import finite_leading_correction, reduced_pair


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or not is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def leading_prime_power_value(prime: int) -> tuple[int, int]:
    """Return f_M(p^nu)=2(p-1)/(p-2) on an allowed odd prime."""
    _require_odd_prime(prime)
    return reduced_pair(2 * (prime - 1), prime - 2)


def split_correction_prime_power_value(prime: int) -> tuple[int, int]:
    """Return g_M(p^nu)=(p-1)/(p-2), the r=1 correction layer."""
    _require_odd_prime(prime)
    return reduced_pair(prime - 1, prime - 2)


def fixed_anchor_log2_coefficient(anchor_primes: tuple[int, ...]) -> dict[str, object]:
    """Return the exact fixed-M log^2 coefficient delta_M^2/8.

    The analytic existence of the asymptotic is supplied by the cited
    Selberg--Delange theorem; this helper audits only the exact Euler coefficient.
    """
    data = finite_leading_correction(anchor_primes)
    coefficient = data["candidate_log2_coefficient"]
    return {
        "anchor_primes": data["anchor_primes"],
        "odd_anchor_density": data["odd_anchor_density"],
        "log2_leading_coefficient": coefficient,
        "analytic_scope": "FIXED_M",
        "moving_M_uniformity": False,
    }
