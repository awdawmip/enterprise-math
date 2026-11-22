"""Prime-power-sensitive reuse threshold for Bonferroni defect tokens.

The squarefree defect token records which support primes were selected.  P017
CG12, however, applies to *any* odd transverse divisor, so the stronger capacity
label is the complete selected prime-power block

    D_full = product_{p selected} p^{v_p(n)}.

It may cross the single-use threshold even when its squarefree radical does not.
For example in the k=22 square basin,

    n=525=3*5^2*7,

selecting {3,5} gives D_rad=15<=21 but D_full=75>21.

For every anchor-surviving basin state and selected support-prime set:

* D_full is odd, transverse to M=k(k+1), and divides n=M-x;
* CG12 therefore gives signed reuse capacity
      floor((k-1)/D_full)+1;
* if D_full>k-1, transversality excludes D_full=k,k+1, hence D_full>=k+2;
* q=n/D_full<=k;
* every unselected small support prime survives in q, while every selected
  prime is removed completely;
* a canonical L020 large tail >k would also survive in q, impossible.

Thus D_full>k-1 forces the state to be fully k-smooth and therefore makes its
full core equal to the state itself (>k^2).  Any mirror full-core product
containing that side is >k, so canonical L053 places it in a singleton cell.

Consequently a Bonferroni defect token can participate in a repeated residual
S<k hard-core cell only if

    D_full <= k-1.

This strictly strengthens the radical-only necessary condition and is the
correct multiplicity-preserving boundary to use downstream.
"""

from __future__ import annotations

from math import gcd, prod

from .cutoff_pairing import distinct_prime_factors, transverse_prime_support
from .legendre import anchor_product, is_prime
from .p017_cofactor_window import square_basin_smooth_tail


def _prime_power_block(state: int, prime: int) -> int:
    block = 1
    remaining = state
    while remaining % prime == 0:
        block *= prime
        remaining //= prime
    return block


def full_block_token_capacity(
    k: int,
    state: int,
    selected_primes: tuple[int, ...],
) -> dict[str, object]:
    """Return the multiplicity-sensitive token label and CG12 capacity data."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(state, bool) or not isinstance(state, int) or not (k * k < state < (k + 1) ** 2):
        raise ValueError("state must lie in the open k-th square basin")
    if not selected_primes or len(set(selected_primes)) != len(selected_primes):
        raise ValueError("selected_primes must be a nonempty tuple of distinct primes")

    center = k * (k + 1)
    if gcd(state, center) != 1:
        raise ValueError("state must be anchor-surviving")
    support = tuple(transverse_prime_support(state, k, anchor_product(k)))
    selected = tuple(sorted(selected_primes))
    if any(prime not in support or not is_prime(prime) for prime in selected):
        raise ValueError("selected primes must belong to the complete transverse support")

    radical = prod(selected)
    full = prod(_prime_power_block(state, prime) for prime in selected)
    quotient = state // full
    if state % full or full < radical:
        raise AssertionError("full prime-power token construction failed")
    if gcd(full, center) != 1 or full % 2 == 0:
        raise AssertionError("full token lost odd transversality")

    omitted = tuple(prime for prime in support if prime not in selected)
    if any(quotient % prime == 0 for prime in selected):
        raise AssertionError("selected prime survived its complete block removal")
    if any(quotient % prime != 0 for prime in omitted):
        raise AssertionError("omitted support prime disappeared from quotient")

    capacity = (k - 1) // full + 1
    single_use = full > k - 1
    fully_smooth = False
    singleton = False
    quotient_support: tuple[int, ...] | None = None
    if single_use:
        if full in (k, k + 1) or full < k + 2:
            raise AssertionError("odd transverse full token did not jump from k-1 to k+2")
        if quotient > k:
            raise AssertionError("single-use full token quotient did not descend to <=k")
        smooth = square_basin_smooth_tail(k, state)
        if int(smooth["tail"]) != 1 or int(smooth["smooth_core"]) != state:
            raise AssertionError("single-use full token state is not fully k-smooth")
        fully_smooth = True
        singleton = True
        quotient_support = tuple(distinct_prime_factors(quotient)) if quotient > 1 else ()
        if quotient_support != omitted:
            raise AssertionError("full-block quotient support is not the selected-support complement")

    return {
        "k": k,
        "state": state,
        "support": support,
        "selected_primes": selected,
        "omitted_support_primes": omitted,
        "squarefree_token": radical,
        "full_block_token": full,
        "quotient": quotient,
        "full_block_cg12_capacity": capacity,
        "squarefree_radical_single_use": radical > k - 1,
        "full_block_single_use": single_use,
        "prime_power_multiplicity_strictly_strengthened_threshold": (
            radical <= k - 1 < full
        ),
        "fully_k_smooth": fully_smooth,
        "l053_singleton_side": singleton,
        "quotient_support": quotient_support,
        "repeated_residual_token_possible": full <= k - 1,
    }
