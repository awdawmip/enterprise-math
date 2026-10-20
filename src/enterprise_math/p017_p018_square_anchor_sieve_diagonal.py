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
the distinguished small CRT representative k itself.  The sieve cutoff and
the square root of the anchor are the same parameter.  No minimal-CRT-root
claim is made here.

This is the precise moving-horizon structure left after the carry machinery is
stripped away.  Fixed-wheel CRT independence remains true when the root may be
chosen after the wheel is fixed, but it does not preserve the self-consistency
condition

    distinguished root = sieve cutoff = k.

Accordingly the only surviving non-generic question is a square-root-diagonal
one: can a primorial covering gap of length 2k begin immediately after k^2
when the same k also defines the entire wheel P_k?

A second exact reduction is available at the half cutoff.  For k>=10 let

    P_{k/2} = product_(p<=k/2, p prime) p

and call an interval state half-rough when it is coprime to P_{k/2}.  Every
composite half-rough state is then exactly a semiprime pq with

    k/2 < p <= k < q < 2k+4.

The resulting semiprime incidence graph is bipartite.  A fixed right prime q
has degree at most one, while a fixed left prime p has degree at most two.  A
left degree of two forces the two right primes to differ by two.  Consequently

    H_half(k)
      <= [pi(k)-pi(floor(k/2))]
         + Twin(k, 2k+4),

where H_half is the number of composite half-rough states and Twin counts
ordinary twin-prime pairs wholly inside the indicated right-prime range.
Hence the finite implication

    R_half(k) > [pi(k)-pi(floor(k/2))] + Twin(k,2k+4)
      => pi((k+1)^2)-pi(k^2) > 0

is an exact factor-scale certificate.  Its inputs use divisibility only by
primes <=k/2 plus prime/twin data at O(k) scale; it does not inspect primality
at k^2 scale.  Proving a uniform lower bound strong enough to make this
certificate positive is still open here and is the new half-Buchstab target.

These identities are exact reformulations/reductions, not a proof of
Legendre's conjecture.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime, primes_up_to


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


def half_cutoff_rough_decomposition(k: int) -> dict[str, object]:
    """Split the half-cutoff rough set into primes plus a sparse semiprime graph.

    For k>=10, remove from the open consecutive-square interval every integer
    divisible by a prime <=k/2.  A surviving composite n has least prime factor
    p>k/2.  Since p<=sqrt(n)<k+1, p<=k and n=pq with q>k.  Moreover

        q < (k^2+2k)/(k/2) = 2k+4.

    If q were composite it would have a prime factor <=sqrt(q)<k/2 for k>=10,
    contradicting half-roughness.  Thus q is prime.

    For fixed p the admissible q-window has length 2k/p<4, hence contains at
    most two odd primes.  For fixed q the admissible p-window has length
    2k/q<2, hence contains at most one odd prime.  Two right neighbours of one
    left prime must therefore form a twin-prime pair.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")

    low_primes = tuple(primes_up_to(k // 2))
    low_wheel = 1
    for prime in low_primes:
        low_wheel *= prime

    interval_offsets = range(1, 2 * k + 1)
    half_rough_offsets = tuple(
        offset
        for offset in interval_offsets
        if gcd(k * k + offset, low_wheel) == 1
    )

    factor_primes = tuple(primes_up_to(k))
    prime_offsets: list[int] = []
    semiprime_edges: list[tuple[int, int, int, int]] = []
    for offset in half_rough_offsets:
        value = k * k + offset
        if is_prime(value):
            prime_offsets.append(offset)
            continue

        left_prime = next(
            (prime for prime in factor_primes if value % prime == 0),
            None,
        )
        if left_prime is None:
            raise AssertionError("composite half-rough state lost its small factor")
        right_prime = value // left_prime

        if not (2 * left_prime > k and left_prime <= k):
            raise AssertionError("half-rough least factor left the half-cutoff band")
        if not (k < right_prime < 2 * k + 4):
            raise AssertionError("half-rough cofactor left the short right-prime band")
        if not is_prime(right_prime):
            raise AssertionError("half-rough cofactor must be prime for k>=10")
        if left_prime * right_prime != value:
            raise AssertionError("semiprime factorization identity failed")

        semiprime_edges.append((left_prime, right_prime, value, offset))

    left_degrees: dict[int, list[int]] = {}
    right_degrees: dict[int, list[int]] = {}
    for left_prime, right_prime, _value, _offset in semiprime_edges:
        left_degrees.setdefault(left_prime, []).append(right_prime)
        right_degrees.setdefault(right_prime, []).append(left_prime)

    if any(len(neighbours) > 2 for neighbours in left_degrees.values()):
        raise AssertionError("left semiprime degree exceeded two")
    if any(len(neighbours) > 1 for neighbours in right_degrees.values()):
        raise AssertionError("right semiprime degree exceeded one")

    occupied_twin_pairs: list[tuple[int, int, int]] = []
    for left_prime, neighbours in left_degrees.items():
        ordered = sorted(neighbours)
        if len(ordered) == 2:
            if ordered[1] - ordered[0] != 2:
                raise AssertionError("left degree two must be a twin-prime pair")
            occupied_twin_pairs.append((left_prime, ordered[0], ordered[1]))

    right_primes = tuple(
        prime
        for prime in primes_up_to(2 * k + 3)
        if k < prime < 2 * k + 4
    )
    right_prime_set = set(right_primes)
    ambient_twin_pairs = tuple(
        (prime, prime + 2)
        for prime in right_primes
        if prime + 2 in right_prime_set
    )
    left_band_primes = tuple(
        prime
        for prime in factor_primes
        if 2 * prime > k and prime <= k
    )

    semiprime_capacity_bound = len(left_band_primes) + len(ambient_twin_pairs)
    prime_count_from_decomposition = len(half_rough_offsets) - len(semiprime_edges)
    certificate_margin = len(half_rough_offsets) - semiprime_capacity_bound

    if prime_count_from_decomposition != len(prime_offsets):
        raise AssertionError("half-cutoff prime/semiprime partition failed")
    if len(semiprime_edges) > semiprime_capacity_bound:
        raise AssertionError("semiprime graph exceeded left-plus-twin capacity")

    return {
        "k": k,
        "half_cutoff": k / 2,
        "low_wheel_primes": low_primes,
        "low_prime_wheel": low_wheel,
        "half_rough_offsets": half_rough_offsets,
        "half_rough_count": len(half_rough_offsets),
        "prime_offsets": tuple(prime_offsets),
        "prime_count_from_decomposition": prime_count_from_decomposition,
        "semiprime_edges": tuple(semiprime_edges),
        "semiprime_count": len(semiprime_edges),
        "left_band_primes": left_band_primes,
        "right_band_primes": right_primes,
        "left_degrees": tuple(
            (prime, tuple(sorted(neighbours)))
            for prime, neighbours in sorted(left_degrees.items())
        ),
        "right_degrees": tuple(
            (prime, tuple(sorted(neighbours)))
            for prime, neighbours in sorted(right_degrees.items())
        ),
        "occupied_twin_pairs": tuple(sorted(occupied_twin_pairs)),
        "ambient_twin_pairs": ambient_twin_pairs,
        "semiprime_capacity_bound": semiprime_capacity_bound,
        "half_buchstab_certificate_margin": certificate_margin,
        "half_buchstab_certificate_positive": certificate_margin > 0,
    }
