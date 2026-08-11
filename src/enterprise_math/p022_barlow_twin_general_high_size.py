"""Seven-rank size gate for the general simple-high affine branch.

The general high-digit reduction writes

    q = 8(r-h)-1-c = 8r-(delta+1),
    delta = 8h+c.

Once complete escape has crossed the strict seven-rank barrier

    q > 7r+3,

we obtain

    r > delta+4.

All quantities are integral, hence r>=delta+5 and therefore

    q = 8r-(delta+1) >= 7delta+39.

So a prime common to the two fixed transfer numerators is relevant to an actual
escape branch only if it is not merely residue-compatible but also at least
`7*delta+39`.  This removes the first noncoprime pressure example
(h,c)=(51,-120): its common factor 701 has delta=288 and lies far below the
required threshold 2055.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_twin_general_high_transfer import (
    fixed_general_high_parameters,
    general_high_affine_data,
)


def minimum_affine_prime_after_seven_rank(gap: int, c: int) -> int:
    """Necessary q lower bound 7*delta+39 for a complete affine escape."""
    _, delta, _ = fixed_general_high_parameters(gap, c)
    return 7 * delta + 39


def seven_rank_affine_size_gate(rank: int, gap: int, c: int) -> tuple[int, int]:
    """Return (q,minimum) and certify the exact seven-rank implication."""
    _, prime, _, delta = general_high_affine_data(rank, gap, c)
    if not _is_prime(prime):
        raise ValueError("affine q candidate must be prime")
    if prime <= 7 * rank + 3:
        raise ValueError("the strict seven-rank barrier has not been crossed")
    if rank < delta + 5:
        raise AssertionError("q>7r+3 and q=8r-(delta+1) force r>=delta+5")
    minimum = 7 * delta + 39
    if prime < minimum:
        raise AssertionError("seven-rank affine prime fell below its fixed delta threshold")
    return prime, minimum


def common_transfer_prime_is_large_enough(gap: int, c: int, prime: int) -> bool:
    """Necessary size filter for a prime factor common to both fixed transfers."""
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    return prime >= minimum_affine_prime_after_seven_rank(gap, c)
