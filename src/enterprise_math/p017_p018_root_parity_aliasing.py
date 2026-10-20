"""Generation 3D: root-cutoff Möbius sign aliasing ladder.

At the exact P_m root cutoff z_m=floor(U^(1/(m+1))), every rough state has
Omega<=m.  On squarefree states, mu(n)=(-1)^Omega(n), so the Möbius sign only
identifies the parity of factor depth, not the depth itself.

For m=3 this yields the exact negative boundary

    mu(n)=-1  <=>  n is prime OR a squarefree triple-prime state,

on the z3-rough square shell.  Therefore a root-P3 Möbius sign theorem cannot
by itself distinguish a prime from the squarefree fully-k-smooth triple core.

For m=2, the square shell contains no perfect square and every z2-rough
composite is a squarefree semiprime, so

    mu(n)=-1  <=>  n is prime.

Thus the root-P2 cutoff is the first root layer at which negative Möbius sign
becomes a perfect prime selector.  The cost is that every nontrivial
factorization of the remaining composite support has state sign +1
(`P2_BILINEAR_MOBIUS_SIGN_FREEZE`).

This module records the exact finite aliasing; it does not supply the analytic
transport needed to carry pre-P2 sign information through the triple-core
removal.
"""

from __future__ import annotations

from math import isqrt

from .legendre import is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff, rough_survivor_offsets
from .p017_p018_square_parity_bilinear_target import mobius


def _omega_multiset(value: int) -> tuple[int, tuple[int, ...]]:
    remaining = value
    factors: list[int] = []
    for p in primes_up_to(isqrt(value) + 1):
        while remaining % p == 0:
            factors.append(p)
            remaining //= p
        if remaining == 1:
            break
        if p * p > remaining:
            break
    if remaining > 1:
        factors.append(remaining)
    return len(factors), tuple(sorted(factors))


def root_parity_aliasing_profile(k: int) -> dict[str, object]:
    """Verify the exact z3 aliasing and z2 prime-selector endpoint."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")

    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])

    z3_negative_prime_rows: list[tuple[int, int]] = []
    z3_negative_triple_rows: list[tuple[int, int, tuple[int, ...]]] = []
    z3_zero_repeated_rows: list[tuple[int, int, tuple[int, ...]]] = []
    z3_positive_rows: list[tuple[int, int, tuple[int, ...]]] = []

    for offset in rough_survivor_offsets(k, z3):
        value = k * k + offset
        mu = mobius(value)
        omega, factors = _omega_multiset(value)
        if omega > 3:
            raise AssertionError("z3 rough state exceeded Omega=3")
        if mu == -1:
            if omega == 1:
                if not is_prime(value):
                    raise AssertionError("Omega=1 negative row was not prime")
                z3_negative_prime_rows.append((value, offset))
            elif omega == 3 and len(set(factors)) == 3:
                z3_negative_triple_rows.append((value, offset, factors))
            else:
                raise AssertionError("z3 negative Möbius row escaped prime/squarefree-triple alias")
        elif mu == 0:
            if len(set(factors)) == len(factors):
                raise AssertionError("zero Möbius row was unexpectedly squarefree")
            z3_zero_repeated_rows.append((value, offset, factors))
        elif mu == 1:
            if omega != 2 or len(set(factors)) != 2:
                raise AssertionError("z3 positive Möbius row was not a squarefree semiprime")
            z3_positive_rows.append((value, offset, factors))
        else:
            raise AssertionError("invalid Möbius value")

    z2_negative_rows: list[tuple[int, int]] = []
    z2_positive_rows: list[tuple[int, int, tuple[int, ...]]] = []
    for offset in rough_survivor_offsets(k, z2):
        value = k * k + offset
        mu = mobius(value)
        omega, factors = _omega_multiset(value)
        if mu == -1:
            if omega != 1 or not is_prime(value):
                raise AssertionError("z2 negative Möbius sign failed to select a prime")
            z2_negative_rows.append((value, offset))
        elif mu == 1:
            if omega != 2 or len(set(factors)) != 2:
                raise AssertionError("z2 positive Möbius row was not squarefree semiprime")
            z2_positive_rows.append((value, offset, factors))
        else:
            raise AssertionError("z2 rough support should contain no zero-Möbius square")

    return {
        "k": k,
        "p3_cutoff": z3,
        "p2_cutoff": z2,
        "z3_negative_prime_rows": tuple(z3_negative_prime_rows),
        "z3_negative_squarefree_triple_rows": tuple(z3_negative_triple_rows),
        "z3_zero_repeated_rows": tuple(z3_zero_repeated_rows),
        "z3_positive_semiprime_rows": tuple(z3_positive_rows),
        "z2_negative_prime_rows": tuple(z2_negative_rows),
        "z2_positive_semiprime_rows": tuple(z2_positive_rows),
        "z3_negative_sign_aliases_prime_and_squarefree_triple": True,
        "z2_negative_sign_is_prime_selector": True,
        "status": "ROOT_PARITY_ALIASING_LADDER",
    }
