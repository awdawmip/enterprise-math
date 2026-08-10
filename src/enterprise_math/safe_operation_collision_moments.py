"""Safe-operation freedom as exact partition collision moments.

Let a finite state set have size ``n`` and let an observation partition have
block sizes ``n_1,...,n_b``.  Put ``p_j=n_j/n``.

Choose one deterministic total endomap uniformly from the ``n^n`` possible maps.
For a source block of size ``k``, quotient compatibility requires all ``k``
independent image choices to land in one target observation block.  The exact
probability of that event is

    sum_j p_j^k.

Source blocks are independent, so the safe-total probability is

    P_total = product_i sum_j p_j^(n_i).

Equivalently, safe-operation freedom is a product of power-sum / collision
moments of the normalized partition masses.  This is exactly the count formula
from ``partial_safe_operation_spectrum`` divided by the full endomap universe.

For partial endomaps sampled uniformly from ``n+1`` outputs per source state
(the extra output is ``UNDEFINED``), a source block of size ``k`` is safe when
all entries are undefined or all defined targets land in one observation block:

    P_partial,k = (1 + sum_j n_j^k) / (n+1)^k.

Again the source-block factors multiply.

The total-operation probability gives an exact finite endpoint reconnection:
``P_total=1`` at both the indiscrete and discrete partitions and is strictly
below one at every genuine intermediate partition.

Equal-block family.  If ``n=b*m`` and the partition has ``b`` blocks of common
size ``m``, every collision factor is ``b^(1-m)`` and

    P_total = b^(b-n) = 1 / b^(n-b),
    N_total = n^n / b^(n-b) = (b*m^m)^b.

Within the continuous relaxation of the equal-block family, minimizing the safe
fraction is equivalent to maximizing ``(n-b) log b``.  Its unique stationary
point satisfies

    n/b = 1 + log b,

or, in block-size form,

    m = W(e*n).

The executable layer remains integer-only and does not evaluate Lambert W; it
uses the exact divisor-restricted formulas.  The analytic calibration only says
that the most constraining equal-block scale drifts slowly with state count and
cannot be one fixed block size.

Power sums, collision probabilities, Renyi entropies and Lambert W are standard
prior mathematics.  The Enterprise Math value is the exact safe-operation /
precision interpretation and the finite endpoint/constraint-valley structure.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from operator import mul
from typing import Hashable, Mapping

from .partial_safe_operation_spectrum import (
    partition_block_sizes,
    safe_partial_endomap_count,
    safe_total_endomap_count,
)

Vertex = Hashable
Partition = Mapping[Vertex, Hashable]


def _state_count(partition: Partition) -> int:
    count = len(partition)
    if count <= 0:
        raise ValueError("partition must be nonempty")
    partition_block_sizes(partition)  # validate shape/hashability through owner
    return count


def collision_power_sum(partition: Partition, exponent: int) -> Fraction:
    """Return ``sum_j (n_j/n)^exponent`` exactly as a rational number."""
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    n = _state_count(partition)
    sizes = partition_block_sizes(partition)
    return Fraction(sum(size**exponent for size in sizes), n**exponent)


def safe_total_probability(partition: Partition) -> Fraction:
    """Exact fraction of all total endomaps that respect the partition."""
    n = _state_count(partition)
    return Fraction(safe_total_endomap_count(partition), n**n)


def safe_total_probability_from_collision_moments(partition: Partition) -> Fraction:
    """Product of the source-block collision moments."""
    sizes = partition_block_sizes(partition)
    factors = [collision_power_sum(partition, source_size) for source_size in sizes]
    return reduce(mul, factors, Fraction(1, 1))


def safe_partial_probability(partition: Partition) -> Fraction:
    """Exact fraction of all deterministic partial endomaps that are safe."""
    n = _state_count(partition)
    return Fraction(safe_partial_endomap_count(partition), (n + 1) ** n)


def safe_partial_probability_from_block_factors(partition: Partition) -> Fraction:
    """Independent source-block probability factorization for partial maps."""
    n = _state_count(partition)
    sizes = partition_block_sizes(partition)
    factors = [
        Fraction(
            1 + sum(target_size**source_size for target_size in sizes),
            (n + 1) ** source_size,
        )
        for source_size in sizes
    ]
    return reduce(mul, factors, Fraction(1, 1))


def total_operation_constraint_deficit(partition: Partition) -> Fraction:
    """Exact unsafe fraction in the total endomap universe."""
    return Fraction(1, 1) - safe_total_probability(partition)


def partial_operation_constraint_deficit(partition: Partition) -> Fraction:
    """Exact unsafe fraction in the partial endomap universe."""
    return Fraction(1, 1) - safe_partial_probability(partition)


def equal_block_total_safe_count(state_count: int, block_size: int) -> int:
    """Exact total-safe count for ``b=n/m`` equal blocks of size ``m``."""
    for name, value in (("state_count", state_count), ("block_size", block_size)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be positive")
    if state_count % block_size:
        raise ValueError("block_size must divide state_count")
    block_count = state_count // block_size
    return (block_count * block_size**block_size) ** block_count


def equal_block_total_safe_probability(state_count: int, block_size: int) -> Fraction:
    """Exact ``1 / b^(n-b)`` equal-block safe probability."""
    count = equal_block_total_safe_count(state_count, block_size)
    return Fraction(count, state_count**state_count)


def proper_divisors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value <= 0:
        raise ValueError("value must be positive")
    return tuple(divisor for divisor in range(2, value) if value % divisor == 0)


@dataclass(frozen=True)
class EqualBlockConstraintMinimum:
    state_count: int
    block_size: int
    block_count: int
    safe_total_count: int
    safe_probability: Fraction


def most_constraining_equal_block_partition(state_count: int) -> EqualBlockConstraintMinimum:
    """Exact minimum safe-total count among nontrivial equal-block partitions."""
    divisors = proper_divisors(state_count)
    if not divisors:
        raise ValueError("state_count has no nontrivial equal-block partition")
    candidates = [
        (equal_block_total_safe_count(state_count, block_size), block_size)
        for block_size in divisors
    ]
    safe_count, block_size = min(candidates)
    return EqualBlockConstraintMinimum(
        state_count=state_count,
        block_size=block_size,
        block_count=state_count // block_size,
        safe_total_count=safe_count,
        safe_probability=Fraction(safe_count, state_count**state_count),
    )
