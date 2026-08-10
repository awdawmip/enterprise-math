"""Prime-axis decomposition of the positive-integer precision lattice.

Unique factorization gives every positive scale ``lambda`` a finite exponent
vector over its prime support.  The divisor interval below ``lambda`` is the
Cartesian product of the corresponding exponent chains.  This is standard
number theory/divisor-lattice structure, not an Enterprise Math invention.

R004 uses it as a candidate answer to a narrower question: can one scalar
integer precision factor contain a canonical finite *scale-axis rank* without
first declaring a dimension by hand?  The arithmetic rank is the number of
distinct prime divisors.  Interpreting that rank as physical spatial dimension
is a separate hypothesis and is not proved here.
"""
from __future__ import annotations

from math import prod
from collections.abc import Sequence


def _pos(value: int, name: str = "value") -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def prime_factorization(value: int) -> tuple[tuple[int, int], ...]:
    _pos(value)
    remaining = value
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def prime_axis_rank(scale: int) -> int:
    return len(prime_factorization(scale))


def prime_axis_support(scale: int) -> tuple[int, ...]:
    return tuple(prime for prime, _ in prime_factorization(scale))


def divisor_lattice_shape(scale: int) -> tuple[int, ...]:
    """Chain cardinalities of the canonical divisor-lattice product."""
    return tuple(exponent + 1 for _, exponent in prime_factorization(scale))


def divisor_lattice_size(scale: int) -> int:
    """Number of positive divisors, with tau(1)=1."""
    shape = divisor_lattice_shape(scale)
    return prod(shape) if shape else 1


def divisor_exponent_coordinates(divisor: int, scale: int) -> tuple[int, ...]:
    _pos(divisor, "divisor")
    _pos(scale, "scale")
    if scale % divisor:
        raise ValueError("divisor must divide scale")
    factors = prime_factorization(scale)
    remaining = divisor
    coordinates: list[int] = []
    for prime, maximum in factors:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent > maximum:
            raise AssertionError("divisor exponent cannot exceed scale exponent")
        coordinates.append(exponent)
    if remaining != 1:
        raise AssertionError("a divisor cannot contain primes outside the scale support")
    return tuple(coordinates)


def divisor_from_exponent_coordinates(coordinates: Sequence[int], scale: int) -> int:
    _pos(scale, "scale")
    factors = prime_factorization(scale)
    row = tuple(coordinates)
    if len(row) != len(factors):
        raise ValueError("one exponent coordinate is required per prime axis")
    value = 1
    for coordinate, (prime, maximum) in zip(row, factors):
        if (
            isinstance(coordinate, bool)
            or not isinstance(coordinate, int)
            or not 0 <= coordinate <= maximum
        ):
            raise ValueError("exponent coordinate outside divisor-lattice axis")
        value *= prime**coordinate
    return value


def prime_power_axis_sizes(scale: int) -> tuple[int, ...]:
    """Pairwise-coprime side lengths whose product is the scalar scale."""
    return tuple(prime**exponent for prime, exponent in prime_factorization(scale))


def prime_power_axis_scale_chains(scale: int) -> tuple[tuple[int, ...], ...]:
    """Ordered precision chains ``1,p,...,p^a`` for each prime axis."""
    return tuple(
        tuple(prime**level for level in range(exponent + 1))
        for prime, exponent in prime_factorization(scale)
    )


def refinement_multiplier(coarse: int, fine: int) -> int:
    _pos(coarse, "coarse")
    _pos(fine, "fine")
    if fine % coarse:
        raise ValueError("coarse scale must divide fine scale")
    return fine // coarse


def refinement_new_primes(coarse: int, fine: int) -> tuple[int, ...]:
    multiplier = refinement_multiplier(coarse, fine)
    old = set(prime_axis_support(coarse))
    return tuple(prime for prime in prime_axis_support(multiplier) if prime not in old)


def refinement_rank_increment(coarse: int, fine: int) -> int:
    """Exact new-axis count for one divisibility refinement."""
    refinement_multiplier(coarse, fine)
    increment = prime_axis_rank(fine) - prime_axis_rank(coarse)
    expected = len(refinement_new_primes(coarse, fine))
    if increment != expected:
        raise AssertionError("prime-support union must equal the fine support")
    return increment


def refinement_rank_monotone(coarse: int, fine: int) -> bool:
    return refinement_rank_increment(coarse, fine) >= 0


def prime_support_stable(coarse: int, fine: int) -> bool:
    refinement_multiplier(coarse, fine)
    return prime_axis_support(coarse) == prime_axis_support(fine)


def dimension_preserving_refinement(coarse: int, fine: int) -> bool:
    """Candidate-dimension preserving iff the refinement introduces no new prime."""
    return refinement_rank_increment(coarse, fine) == 0


def refinement_support_balance_holds(coarse: int, fine: int) -> bool:
    """Check ``Delta rank = |supp(fine/coarse) \ supp(coarse)|`` exactly."""
    return refinement_rank_increment(coarse, fine) == len(
        refinement_new_primes(coarse, fine)
    )


def coarsening_lost_primes(fine: int, coarse: int) -> tuple[int, ...]:
    refinement_multiplier(coarse, fine)
    coarse_support = set(prime_axis_support(coarse))
    return tuple(prime for prime in prime_axis_support(fine) if prime not in coarse_support)


def coarsening_rank_loss(fine: int, coarse: int) -> int:
    """Exact candidate-axis loss when moving from fine scale to a divisor scale."""
    refinement_multiplier(coarse, fine)
    loss = prime_axis_rank(fine) - prime_axis_rank(coarse)
    expected = len(coarsening_lost_primes(fine, coarse))
    if loss != expected:
        raise AssertionError("coarsening rank loss must equal removed prime support")
    return loss


def prime_axis_rank_sequence(scales: Sequence[int]) -> tuple[int, ...]:
    chain = tuple(scales)
    if not chain:
        raise ValueError("scale sequence must be nonempty")
    for scale in chain:
        _pos(scale, "scale")
    if any(right % left for left, right in zip(chain, chain[1:])):
        raise ValueError("scales must form a divisibility refinement chain")
    return tuple(prime_axis_rank(scale) for scale in chain)


def prime_axis_rank_stabilized_after(scales: Sequence[int], index: int) -> bool:
    ranks = prime_axis_rank_sequence(scales)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < len(ranks):
        raise ValueError("index outside scale sequence")
    return all(rank == ranks[index] for rank in ranks[index:])


def total_rank_opening(scales: Sequence[int]) -> int:
    """Path-independent total number of prime-axis opening events."""
    chain = tuple(scales)
    ranks = prime_axis_rank_sequence(chain)
    total = sum(
        refinement_rank_increment(coarse, fine)
        for coarse, fine in zip(chain, chain[1:])
    )
    expected = ranks[-1] - ranks[0]
    if total != expected:
        raise AssertionError("rank increments must telescope")
    return total


def total_rank_contraction(scales: Sequence[int]) -> int:
    """Total lost prime-axis rank along a descending divisibility chain."""
    chain = tuple(scales)
    if not chain:
        raise ValueError("scale sequence must be nonempty")
    for scale in chain:
        _pos(scale, "scale")
    if any(left % right for left, right in zip(chain, chain[1:])):
        raise ValueError("scales must form a descending divisor chain")
    total = sum(
        coarsening_rank_loss(fine, coarse)
        for fine, coarse in zip(chain, chain[1:])
    )
    expected = prime_axis_rank(chain[0]) - prime_axis_rank(chain[-1])
    if total != expected:
        raise AssertionError("rank losses must telescope")
    return total
