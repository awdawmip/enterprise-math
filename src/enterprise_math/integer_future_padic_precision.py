"""Prime-power future precision ladder from integer Smith invariant factors.

For nonzero Smith factor ``d`` write ``v_p(d)=a``.  Modulo ``p^e`` that
coordinate contributes

    kernel residues   = p^min(a,e),
    observable phases = p^max(e-a,0).

Thus a finite Smith obstruction is completely invisible at low p-adic precision
``e<=a`` and then reveals one further p-adic digit per extra modulus level.

A free hidden state direction behaves differently: it contributes ``p^e``
kernel residues at every level, so its hidden kernel keeps growing with e rather
than saturating at a finite p-power.

For a full integer observation matrix with hidden free rank h and Smith factors
d_i, the mod-p^e kernel exponent is

    e*h + sum_i min(e, v_p(d_i)),

and the observable image exponent is

    sum_i max(e-v_p(d_i), 0).

Their sum is ``e*n``.  The ladder therefore separates persistent free hidden
state from finite coordinate torsion using only modular precision growth.

This is standard Smith/p-adic arithmetic.  The project value is the precision-
diagnostic interpretation across declared modulus levels.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_future_smith_precision import integer_smith_precision_profile


def _prime(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("prime must be an integer")
    if value < 2:
        raise ValueError("prime must be at least two")
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            raise ValueError("prime must be prime")
        divisor += 1
    return value


def _exponent(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("exponent must be an integer")
    if value <= 0:
        raise ValueError("exponent must be positive")
    return value


def p_adic_valuation(value: int, prime: int) -> int:
    p = _prime(prime)
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value == 0:
        raise ValueError("p-adic valuation of zero is not finite")
    remaining = abs(value)
    valuation = 0
    while remaining % p == 0:
        valuation += 1
        remaining //= p
    return valuation


@dataclass(frozen=True)
class PrimePowerSmithPrecision:
    prime: int
    exponent: int
    modulus: int
    state_dimension: int
    hidden_free_rank: int
    smith_factors: tuple[int, ...]
    smith_p_adic_valuations: tuple[int, ...]
    kernel_exponent: int
    observable_phase_exponent: int
    kernel_size: int
    observable_phase_count: int

    @property
    def fully_modularly_injective(self) -> bool:
        return self.kernel_exponent == 0


def prime_power_smith_precision(
    observation_matrix: Sequence[Sequence[int]],
    prime: int,
    exponent: int,
) -> PrimePowerSmithPrecision:
    p = _prime(prime)
    e = _exponent(exponent)
    profile = integer_smith_precision_profile(observation_matrix)
    valuations = tuple(p_adic_valuation(factor, p) for factor in profile.smith_invariant_factors)
    kernel_exponent = (
        e * profile.hidden_free_rank
        + sum(min(e, valuation) for valuation in valuations)
    )
    image_exponent = sum(max(e - valuation, 0) for valuation in valuations)
    dimension = profile.state_dimension
    if kernel_exponent + image_exponent != e * dimension:
        raise AssertionError("p-adic kernel/image exponent identity failed")
    return PrimePowerSmithPrecision(
        prime=p,
        exponent=e,
        modulus=p ** e,
        state_dimension=dimension,
        hidden_free_rank=profile.hidden_free_rank,
        smith_factors=profile.smith_invariant_factors,
        smith_p_adic_valuations=valuations,
        kernel_exponent=kernel_exponent,
        observable_phase_exponent=image_exponent,
        kernel_size=p ** kernel_exponent,
        observable_phase_count=p ** image_exponent,
    )


def prime_power_precision_ladder(
    observation_matrix: Sequence[Sequence[int]],
    prime: int,
    max_exponent: int,
) -> tuple[PrimePowerSmithPrecision, ...]:
    maximum = _exponent(max_exponent)
    return tuple(
        prime_power_smith_precision(
            observation_matrix,
            prime,
            exponent,
        )
        for exponent in range(1, maximum + 1)
    )
