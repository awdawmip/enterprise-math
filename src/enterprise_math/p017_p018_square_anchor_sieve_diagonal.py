"""Square-root diagonal endpoint of the P017/P018 carry/sieve route.

After quotient-channel Mobius recombination and the anchored Jacobsthal change
of coordinates, the surviving special phase admits an even simpler exact form.
For k>=2 put

    P_k = product_(p<=k, p prime) p.

Every integer in the open consecutive-square interval is uniquely

    n = k^2 + r,                 1 <= r <= 2k.

If such n is composite, its least prime factor is at most sqrt(n)<k+1 and is
therefore a prime <=k.  Conversely a prime in the interval is coprime to P_k.
Hence

    pi((k+1)^2)-pi(k^2)
      = #{1<=r<=2k : gcd(k^2+r,P_k)=1}.

For each prime p<=k the excluded offset class is

    r = -k^2 (mod p).

Thus the phase is not an arbitrary wheel translate: every local forbidden
class is the negative of the same square root k, and all local roots glue to
the **small CRT representative k itself**.  The sieve cutoff and the square
root of the anchor are the same parameter.

This is the precise moving-horizon structure left after the carry machinery is
stripped away.  Fixed-wheel CRT independence remains true when the root may be
chosen after the wheel is fixed, but it does not preserve the self-consistency
condition

    root = sieve cutoff = k.

Accordingly the only surviving non-generic question is a square-root-diagonal
one: can a primorial covering gap of length 2k begin immediately after k^2
when the same k also defines the entire wheel P_k?

This identity is an exact reformulation of Legendre's conjecture, not a proof.
It is recorded to prevent further carry/Fourier refinements from obscuring the
actual remaining information constraint.
"""

from __future__ import annotations

from math import gcd

from .legendre import primes_up_to


def prime_wheel(limit: int) -> int:
    """Return the primorial product over all primes p<=limit."""
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    wheel = 1
    for prime in primes_up_to(limit):
        wheel *= prime
    return wheel


def square_root_diagonal_rough_count(k: int) -> dict[str, object]:
    """Count exact P_k-rough survivors in (k^2,(k+1)^2)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    primes = tuple(primes_up_to(k))
    wheel = 1
    for prime in primes:
        wheel *= prime

    survivor_offsets = tuple(
        offset
        for offset in range(1, 2 * k + 1)
        if gcd(k * k + offset, wheel) == 1
    )
    forbidden_residues = tuple((prime, (-k * k) % prime) for prime in primes)

    for prime, residue in forbidden_residues:
        for offset in range(1, 2 * k + 1):
            if ((k * k + offset) % prime == 0) != (offset % prime == residue):
                raise AssertionError("square-anchor forbidden residue identity failed")

    return {
        "k": k,
        "square_anchor": k * k,
        "prime_wheel": wheel,
        "wheel_primes": primes,
        "interval_length": 2 * k,
        "forbidden_offset_residues": forbidden_residues,
        "rough_survivor_offsets": survivor_offsets,
        "rough_survivor_count": len(survivor_offsets),
        "prime_gap_positive": bool(survivor_offsets),
        "root_equals_sieve_cutoff": True,
    }


def verify_negative_square_phase(k: int) -> dict[str, object]:
    """Verify that each odd local forbidden class is a negative-square phase."""
    data = square_root_diagonal_rough_count(k)
    checks: list[tuple[int, int, bool]] = []
    for prime, residue in data["forbidden_offset_residues"]:
        if prime == 2:
            compatible = ((-residue) % prime) == (k * k) % prime
        elif residue == 0:
            compatible = k % prime == 0
        else:
            negative_residue = (-residue) % prime
            compatible = pow(negative_residue, (prime - 1) // 2, prime) == 1
        checks.append((prime, residue, compatible))
        if not compatible:
            raise AssertionError("forbidden phase lost its square-root compatibility")
    return {
        **data,
        "negative_square_phase_checks": tuple(checks),
        "all_local_phases_square_compatible": True,
    }
