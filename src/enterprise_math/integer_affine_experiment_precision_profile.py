"""Minimal precision-resource profile for modular local-global experiments.

For ``G=coker(A) ~= Z^f direct_sum T`` with torsion exponent

    E = product_p p^a_p,

an arbitrary modular experiment family matters to exact IMAGE certification only
through two resources:

1. ``free_integer_separating`` — whether

       intersection_(M in family) M Z = {0};

2. the p-adic depth supremum ``s_p=sup_M v_p(M)`` at each torsion prime.

Uniform exact reachability for all targets holds iff

    (f=0 or free_integer_separating)

and

    s_p >= a_p  for every p|E.

This profile unifies several previously separate experiment shapes.

* Finite family: its lcm D is finite, so free_integer_separating is false and
  ``s_p=v_p(D)``.
* All prime moduli: free_integer_separating is true and ``s_p=1`` for every p;
  completeness is therefore equivalent to squarefree E.
* Infinite power ladder ``R^e``: free_integer_separating iff R>1; ``s_p=infinity``
  for p|R and zero otherwise; completeness is equivalent to ``rad(E)|R`` plus
  nontrivial R when a free cokernel is present.

The object below is a theorem-facing summary of the relevant precision resources,
not a claim to encode every detail of an infinite modulus family.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .integer_affine_local_global import cokernel_torsion_exponent
from .integer_affine_prime_local_global import prime_power_depths_required_by_torsion
from .integer_future_smith_precision import integer_smith_precision_profile


INFINITE_DEPTH = "INFINITE"
PrimeDepth = int | str
Matrix = tuple[tuple[int, ...], ...]


def _matrix(values: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("matrix must contain at least one row")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have one common positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
    return rows


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


def _factor_depths(value: int) -> tuple[tuple[int, int], ...]:
    if value <= 0:
        raise ValueError("factor source must be positive")
    remaining = value
    prime = 2
    result = []
    while prime * prime <= remaining:
        if remaining % prime:
            prime = 3 if prime == 2 else prime + 2
            continue
        depth = 0
        while remaining % prime == 0:
            remaining //= prime
            depth += 1
        result.append((prime, depth))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        result.append((remaining, 1))
    return tuple(result)


@dataclass(frozen=True)
class ModularExperimentPrecisionProfile:
    free_integer_separating: bool
    default_prime_depth: int
    prime_depth_overrides: tuple[tuple[int, PrimeDepth], ...]
    description: str

    def depth_at(self, prime: int) -> PrimeDepth:
        p = _prime(prime)
        for current, depth in self.prime_depth_overrides:
            if current == p:
                return depth
        return self.default_prime_depth


def _validate_profile(profile: ModularExperimentPrecisionProfile) -> None:
    if not isinstance(profile, ModularExperimentPrecisionProfile):
        raise TypeError("profile must be ModularExperimentPrecisionProfile")
    if isinstance(profile.default_prime_depth, bool) or not isinstance(profile.default_prime_depth, int):
        raise TypeError("default prime depth must be an integer")
    if profile.default_prime_depth < 0:
        raise ValueError("default prime depth must be nonnegative")
    seen = set()
    for prime, depth in profile.prime_depth_overrides:
        _prime(prime)
        if prime in seen:
            raise ValueError("prime depth overrides must be unique")
        seen.add(prime)
        if depth != INFINITE_DEPTH:
            if isinstance(depth, bool) or not isinstance(depth, int):
                raise TypeError("prime depth must be a nonnegative integer or INFINITE")
            if depth < 0:
                raise ValueError("prime depth must be nonnegative")


def finite_family_precision_profile(
    moduli: Sequence[int],
) -> ModularExperimentPrecisionProfile:
    values = tuple(moduli)
    if not values:
        raise ValueError("modulus family must be nonempty")
    ceiling = 1
    for modulus in values:
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise TypeError("moduli must be integers")
        if modulus <= 0:
            raise ValueError("moduli must be positive")
        ceiling = lcm(ceiling, modulus)
    return ModularExperimentPrecisionProfile(
        free_integer_separating=False,
        default_prime_depth=0,
        prime_depth_overrides=tuple(
            (prime, depth) for prime, depth in _factor_depths(ceiling)
        ),
        description=f"finite family with lcm {ceiling}",
    )


def all_primes_precision_profile() -> ModularExperimentPrecisionProfile:
    return ModularExperimentPrecisionProfile(
        free_integer_separating=True,
        default_prime_depth=1,
        prime_depth_overrides=(),
        description="all prime moduli once",
    )


def power_ladder_precision_profile(base: int) -> ModularExperimentPrecisionProfile:
    if isinstance(base, bool) or not isinstance(base, int):
        raise TypeError("base must be an integer")
    if base <= 0:
        raise ValueError("base must be positive")
    return ModularExperimentPrecisionProfile(
        free_integer_separating=base > 1,
        default_prime_depth=0,
        prime_depth_overrides=tuple(
            (prime, INFINITE_DEPTH) for prime, _ in _factor_depths(base)
        ),
        description=f"all powers of {base}",
    )


def experiment_profile_uniformly_complete(
    matrix: Sequence[Sequence[int]],
    profile: ModularExperimentPrecisionProfile,
) -> bool:
    A = _matrix(matrix)
    _validate_profile(profile)
    smith = integer_smith_precision_profile(A)
    free_rank = len(A) - smith.rational_rank
    if free_rank > 0 and not profile.free_integer_separating:
        return False

    for prime, required_depth in prime_power_depths_required_by_torsion(A):
        available = profile.depth_at(prime)
        if available == INFINITE_DEPTH:
            continue
        if not isinstance(available, int):
            raise AssertionError("validated prime depth lost integer/infinite form")
        if available < required_depth:
            return False
    return True


@dataclass(frozen=True)
class ExperimentPrecisionCompletenessReport:
    free_cokernel_rank: int
    torsion_exponent: int
    required_prime_depths: tuple[tuple[int, int], ...]
    profile: ModularExperimentPrecisionProfile
    complete: bool


def experiment_precision_completeness_report(
    matrix: Sequence[Sequence[int]],
    profile: ModularExperimentPrecisionProfile,
) -> ExperimentPrecisionCompletenessReport:
    A = _matrix(matrix)
    _validate_profile(profile)
    smith = integer_smith_precision_profile(A)
    return ExperimentPrecisionCompletenessReport(
        free_cokernel_rank=len(A) - smith.rational_rank,
        torsion_exponent=cokernel_torsion_exponent(A),
        required_prime_depths=prime_power_depths_required_by_torsion(A),
        profile=profile,
        complete=experiment_profile_uniformly_complete(A, profile),
    )
