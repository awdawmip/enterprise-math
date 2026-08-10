"""Prime-only versus prime-power local-global reachability.

For ``A:Z^n->Z^m`` let

    E = exp(Tor(coker(A))).

Consider the prime-only local condition

    A x == b (mod p) is solvable for every prime p.

This condition decides exact integer reachability for **every** target b iff E is
squarefree.

Why free cokernel causes no extra prime-power requirement: a nonzero vector in a
free abelian group cannot be divisible by every prime.  Hence the family of all
prime moduli already kills every free cokernel coordinate.

For torsion, the story is different.  If the p-primary exponent is exactly p,
then ``p T_p=0`` and mod-p solvability forces the p-component of the target class
to vanish.  If ``p^2`` divides E, choose an element u of order at least p^2 and
the nonzero class ``p u``.  It lies in ``p T`` and is therefore invisible modulo
p; it is also divisible by every other prime because those primes act invertibly
on the p-primary component.  Thus all prime tests can pass while the exact class
is nonzero.

Sharp scalar witness for every depth K>=2:

    p^K x = p^(K-1)

is not integrally solvable, is solvable modulo p because both sides vanish, and
is solvable modulo every other prime q because p^K is invertible mod q.  The
first p-adic failure occurs only at a deeper prime power.

Consequently:

* prime breadth detects free directions;
* prime-power depth detects repeated p-primary torsion;
* all prime moduli are complete exactly at squarefree torsion exponent;
* full prime-power local-global testing is needed in the generic case.

These are standard finitely-generated-abelian-group facts.  The project value is
the exact precision split between breadth and p-adic depth.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_affine_fiber_diagnostic import integrally_reachable, modularly_reachable
from .integer_affine_local_global import cokernel_torsion_exponent


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


def integer_is_squarefree(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value <= 0:
        raise ValueError("value must be positive")
    prime = 2
    remaining = value
    while prime * prime <= remaining:
        if remaining % prime:
            prime = 3 if prime == 2 else prime + 2
            continue
        remaining //= prime
        if remaining % prime == 0:
            return False
        while remaining % prime == 0:
            remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    return True


def prime_only_local_global_complete_for_all_targets(
    matrix: Sequence[Sequence[int]],
) -> bool:
    """Whether all prime-level congruences suffice uniformly for exact IMAGE."""
    return integer_is_squarefree(cokernel_torsion_exponent(matrix))


def prime_power_depths_required_by_torsion(
    matrix: Sequence[Sequence[int]],
) -> tuple[tuple[int, int], ...]:
    """Return ``(p,a)`` for ``p^a || E`` with a>0."""
    exponent = cokernel_torsion_exponent(matrix)
    if exponent == 1:
        return ()
    remaining = exponent
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
class PrimeOnlyFalsePositiveWitness:
    prime: int
    depth: int
    coefficient: int
    target: int

    def solvable_mod_prime(self, tested_prime: int) -> bool:
        q = _prime(tested_prime)
        return modularly_reachable(((self.coefficient,),), (self.target,), q)

    @property
    def exact_reachable(self) -> bool:
        return integrally_reachable(((self.coefficient,),), (self.target,))


def prime_only_false_positive_witness(
    prime: int,
    depth: int,
) -> PrimeOnlyFalsePositiveWitness:
    p = _prime(prime)
    if isinstance(depth, bool) or not isinstance(depth, int):
        raise TypeError("depth must be an integer")
    if depth < 2:
        raise ValueError("depth must be at least two")
    witness = PrimeOnlyFalsePositiveWitness(
        prime=p,
        depth=depth,
        coefficient=p ** depth,
        target=p ** (depth - 1),
    )
    if witness.exact_reachable:
        raise AssertionError("prime-only false-positive witness unexpectedly reachable")
    if not witness.solvable_mod_prime(p):
        raise AssertionError("witness unexpectedly failed at its base prime")
    return witness


def prime_only_false_positive_is_solvable_for_every_prime(
    witness: PrimeOnlyFalsePositiveWitness,
    tested_prime: int,
) -> bool:
    """Analytic per-prime check for the universal prime-only witness theorem."""
    if not isinstance(witness, PrimeOnlyFalsePositiveWitness):
        raise TypeError("witness must be PrimeOnlyFalsePositiveWitness")
    q = _prime(tested_prime)
    result = witness.solvable_mod_prime(q)
    # q=p: both coefficient and target vanish modulo p.  q!=p: coefficient is
    # a unit modulo q.  Either way solvability is guaranteed.
    if not result:
        raise AssertionError("prime-only witness failed its universal local condition")
    return True
