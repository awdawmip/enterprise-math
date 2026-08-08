"""Integer-only research tools for the Legendre pressure test.

This module does not claim a proof of Legendre's conjecture.  It packages exact
finite identities discovered while using consecutive square-collapse basins as
a stress test for Enterprise Math.
"""

from math import gcd, isqrt


def primes_up_to(limit: int) -> list[int]:
    """Return all primes p <= limit using integer trial division."""
    if limit < 2:
        return []
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                prime = False
                break
        if prime:
            primes.append(candidate)
    return primes


def squarefree_divisors_with_mu(primes: list[int]) -> list[tuple[int, int]]:
    """Return (d, mu(d)) for divisors of the square-free product of primes."""
    items = [(1, 1)]
    for p in primes:
        items += [(d * p, -mu) for d, mu in items.copy()]
    return items


def power_gap(k: int, power: int) -> int:
    """Return (k+1)^power - k^power."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    if power < 1:
        raise ValueError("power must be positive")
    return (k + 1) ** power - k**power


def interior_hit_count(k: int, d: int, power: int = 2) -> int:
    """Count multiples of d strictly between k^power and (k+1)^power."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    if d <= 0:
        raise ValueError("d must be positive")
    if power < 1:
        raise ValueError("power must be positive")
    return (((k + 1) ** power - 1) // d) - (k**power // d)


def euclidean_basin_descent(k: int, d: int, power: int = 2) -> tuple[int, int]:
    """Split an interior hit count into a coarse term plus a smaller local basin.

    If t = k mod d and W_p(x)=(x+1)^p-x^p, then

        H_{p,d}(k) = (W_p(k)-W_p(t))//d + H_{p,d}(t).

    The first returned value is the coarse term; the second is the local term.
    """
    if d <= 0:
        raise ValueError("d must be positive")
    t = k % d
    coarse = (power_gap(k, power) - power_gap(t, power)) // d
    local = interior_hit_count(t, d, power)
    return coarse, local


def square_carry(k: int, d: int) -> int:
    """Return the local square-basin correction kappa_d(k)."""
    if d <= 0:
        raise ValueError("d must be positive")
    return interior_hit_count(k % d, d, 2)


def centered_square_carry(k: int, d: int) -> int:
    """Evaluate kappa_d(k) by the centered-residue boundary criterion.

    If t=k mod d and a=t(t+1) mod d, the local centered interval is
    {1-t,...,t}.  For t>0, the two possible representatives of -a mod d
    enter this interval exactly when a<t and a>=d-t.
    """
    if d <= 0:
        raise ValueError("d must be positive")
    t = k % d
    if t == 0:
        return 0
    a = (t * (t + 1)) % d
    return int(a < t) + int(a >= d - t)


def square_hit_count_from_carry(k: int, d: int) -> int:
    """Recover H_d(k)=2*(k//d)+kappa_d(k)."""
    if d <= 0:
        raise ValueError("d must be positive")
    return 2 * (k // d) + square_carry(k, d)


def is_prime(n: int) -> bool:
    """Deterministic integer primality test suitable for bounded experiments."""
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return False
    return True


def direct_square_interval_prime_count(k: int) -> int:
    """Count primes strictly between k^2 and (k+1)^2."""
    if k < 1:
        raise ValueError("k must be positive")
    return sum(is_prime(n) for n in range(k * k + 1, (k + 1) * (k + 1)))


def mobius_square_interval_prime_count(k: int) -> int:
    """Exact inclusion-exclusion count using all primes p <= k."""
    if k < 1:
        raise ValueError("k must be positive")
    total = 0
    for d, mu in squarefree_divisors_with_mu(primes_up_to(k)):
        total += mu * interior_hit_count(k, d, 2)
    return total


def carry_square_interval_prime_count(k: int) -> int:
    """Exact carry identity: prime_count = 2 + sum mu(d)*kappa_d(k)."""
    if k < 1:
        raise ValueError("k must be positive")
    correction = 0
    for d, mu in squarefree_divisors_with_mu(primes_up_to(k)):
        correction += mu * square_carry(k, d)
    return 2 + correction


def binary_carry_delta(k: int, odd_d: int) -> int:
    """Return kappa_d(k)-kappa_{2d}(k) for odd d.

    If q=k//d, the result is always 0 or (-1)^q.
    """
    if odd_d <= 0 or odd_d % 2 == 0:
        raise ValueError("odd_d must be a positive odd integer")
    return square_carry(k, odd_d) - square_carry(k, 2 * odd_d)


def binary_carry_event(k: int, odd_d: int) -> int:
    """Return the explicit 0/1 event behind binary_carry_delta.

    Write k=q*d+t, a=t(t+1) mod d, and h=floor(t(t+1)/d).
    The result epsilon satisfies

        kappa_d(k)-kappa_{2d}(k) = (-1)^q * epsilon.

    The branch conditions locate which side of the centered local window is
    crossed when the residue class is lifted from modulus d to 2d.
    """
    if odd_d <= 0 or odd_d % 2 == 0:
        raise ValueError("odd_d must be a positive odd integer")
    q, t = divmod(k, odd_d)
    a = (t * (t + 1)) % odd_d
    h = (t * (t + 1)) // odd_d
    if q % 2 == 0:
        if h % 2 == 0:
            return int(a >= odd_d - t)
        return int(a < t)
    if h % 2 == 0:
        return int(a >= t)
    return int(a < odd_d - t)


def binary_carry_square_interval_prime_count(k: int) -> int:
    """Exact prime count after pairing Möbius terms d <-> 2d."""
    if k < 1:
        raise ValueError("k must be positive")
    if k == 1:
        return 2
    odd_primes = [p for p in primes_up_to(k) if p != 2]
    correction = 0
    for d, mu in squarefree_divisors_with_mu(odd_primes):
        correction += mu * binary_carry_delta(k, d)
    return 2 + correction


def anchor_primes(k: int) -> list[int]:
    """Primes p <= k dividing the centered anchor M=k(k+1)."""
    if k < 1:
        raise ValueError("k must be positive")
    anchor = k * (k + 1)
    return [p for p in primes_up_to(k) if anchor % p == 0]


def anchor_product(k: int) -> int:
    """Return the square-free product of anchor primes."""
    product = 1
    for p in anchor_primes(k):
        product *= p
    return product


def anchor_face_sum(k: int) -> int:
    """Möbius carry contribution from the Boolean face supported on anchor primes."""
    if k < 2:
        raise ValueError("k must be at least 2")
    return sum(
        mu * square_carry(k, d)
        for d, mu in squarefree_divisors_with_mu(anchor_primes(k))
    )


def anchor_transfer(k: int, transverse_d: int) -> int:
    """Apply the anchor-face Möbius transform to a transverse modulus."""
    if k < 2:
        raise ValueError("k must be at least 2")
    if transverse_d <= 0:
        raise ValueError("transverse_d must be positive")
    return sum(
        mu * square_carry(k, a * transverse_d)
        for a, mu in squarefree_divisors_with_mu(anchor_primes(k))
    )


def coprime_prefix_count(limit: int, modulus: int) -> int:
    """Count 1<=m<=limit with gcd(m,modulus)=1."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if limit <= 0:
        return 0
    return sum(gcd(m, modulus) == 1 for m in range(1, limit + 1))


def centered_anchor_survivor_count(k: int, transverse_d: int) -> int:
    """Count centered hits of transverse_d surviving all anchor primes.

    The centered coordinate is n=k(k+1)+s with 1-k<=s<=k.  This function
    requires transverse_d to be coprime to the square-free anchor product.
    """
    if k < 2:
        raise ValueError("k must be at least 2")
    if transverse_d <= 0:
        raise ValueError("transverse_d must be positive")
    anchor = anchor_product(k)
    if gcd(transverse_d, anchor) != 1:
        raise ValueError("transverse_d must be coprime to the anchor product")
    center = k * (k + 1)
    return sum(
        (center + s) % transverse_d == 0 and gcd(s, anchor) == 1
        for s in range(1 - k, k + 1)
    )


def anchor_transfer_discrepancy(k: int, transverse_d: int) -> int:
    """Evaluate Lambda_b as a centered survivor discrepancy.

    Lambda_b(k) equals the number of b-hits in the centered square interval
    surviving all anchor primes, minus twice the anchor-coprime prefix count up
    to floor(k/b).
    """
    if k < 2:
        raise ValueError("k must be at least 2")
    anchor = anchor_product(k)
    if gcd(transverse_d, anchor) != 1:
        raise ValueError("transverse_d must be coprime to the anchor product")
    survivors = centered_anchor_survivor_count(k, transverse_d)
    baseline = 2 * coprime_prefix_count(k // transverse_d, anchor)
    return survivors - baseline


def bounded_common_root_witness() -> tuple[int, int, int]:
    """Return a checked witness showing that an unbounded common square root is insufficient.

    For y=73 and the returned x, every x^2+r with 1<=r<=146 has a
    prime divisor <=73.  The witness does NOT satisfy x<=y; that failure is the
    point of the bounded-common-root distinction.
    """
    y = 73
    x = 33641709557196602631265058865
    primorial = 40729680599249024150621323470
    return y, x, primorial


def verify_bounded_common_root_witness() -> bool:
    """Verify the fixed y=73 common-root covering witness."""
    y, x, primorial = bounded_common_root_witness()
    expected = 1
    for p in primes_up_to(y):
        expected *= p
    if expected != primorial:
        return False
    return all(gcd(x * x + r, primorial) > 1 for r in range(1, 2 * y + 1))
