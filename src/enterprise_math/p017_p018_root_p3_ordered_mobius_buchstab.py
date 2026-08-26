"""Ordered Möbius/Buchstab descent from the fourth-root cutoff to primes.

For a real/integer cutoff y define

    M_k(y) = sum_{n in I_k, gcd(n,P_y)=1} mu(n),

where I_k=(k^2,k^2+2k] and P_y is the product of primes <=y.

When the cutoff crosses one prime p, the only newly removed states have least
prime factor p.  Writing n=pq, the nonzero Möbius rows are exactly those with
p not dividing q and no prime factor of q below p, so

    mu(pq) = -mu(q),   P^-(q)>p.

Hence the exact jump law is

    M_k(p) - M_k(p^-)
      = sum_{k^2 < p q <= k^2+2k, P^-(q)>p} mu(q).

Telescoping from any starting cutoff z to k gives

    M_k(k) = M_k(z) + B_k(z),

with the ordered transport

    B_k(z) = sum_{z<p<=k} sum_{k^2<pq<=U, P^-(q)>p} mu(q).

At cutoff k every survivor in the consecutive-square interval is prime, so

    M_k(k) = -pi(I_k).

Therefore

    pi(I_k) = -M_k(z) - B_k(z).

At the fourth-root start z=z_3=floor(U^(1/4)), every ordered quotient satisfies

    q < U/(z+1) < (z+1)^3.

Together with P^-(q)>p>z this places every nonzero quotient in a P2 world:
mu(q)=-1 for a prime quotient, +1 for a squarefree semiprime quotient, and 0
for a squareful quotient.

For fourth-root rough state types this ordered transport counts each state at
most once:

    squarefree semiprime -> -1,
    squarefree triple    -> +1,
    every squareful row  -> 0,
    prime                -> no transport row.

Thus if P,E,T are prime, squarefree-semiprime and squarefree-triple counts,

    M_3 = -P + E - T,
    B_ord = -E + T,
    P = -M_3 - B_ord.

This is the signed analogue of Buchstab cutoff evolution.  The generic
cutoff-telescoping identity is prior sieve mathematics; the square-diagonal
fourth-root specialization is recorded here as the project parity-transport
interface.  It is not by itself a proof of the needed pointwise sign.
"""

from __future__ import annotations

from .legendre import direct_square_interval_prime_count, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import square_interval_upper
from .p017_p018_root_p3_mobius_support import mobius_value
from .p017_p018_root_p3_support_recovery import root_p3_cutoff


def least_prime_factor(value: int) -> int:
    """Return the least prime factor of value>1."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 1:
        raise ValueError("value must be an integer >1")
    for p in range(2, int(value**0.5) + 2):
        if value % p == 0:
            return p
    return value


def mobius_rough_sum(k: int, cutoff: int) -> int:
    """Evaluate M_k(cutoff) by exact bounded enumeration."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    small = tuple(primes_up_to(cutoff))
    return sum(
        mobius_value(n)
        for n in range(k * k + 1, square_interval_upper(k) + 1)
        if all(n % p for p in small)
    )


def ordered_cutoff_jump(k: int, p: int) -> int:
    """Return the exact Möbius jump when the sieve cutoff crosses prime p."""
    if p not in primes_up_to(k):
        raise ValueError("p must be a prime <=k")
    lower = k * k
    upper = square_interval_upper(k)
    total = 0
    for q in range(lower // p + 1, upper // p + 1):
        if q <= 1:
            continue
        if least_prime_factor(q) <= p:
            continue
        total += mobius_value(q)
    return total


def ordered_mobius_transport(k: int, cutoff: int) -> dict[str, object]:
    """Evaluate B_k(cutoff) and the telescoping prime identity."""
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or not 0 <= cutoff <= k:
        raise ValueError("cutoff must lie in 0..k")
    rows: list[tuple[int, int]] = []
    total = 0
    for p in primes_up_to(k):
        if p <= cutoff:
            continue
        jump = ordered_cutoff_jump(k, p)
        rows.append((p, jump))
        total += jump

    start = mobius_rough_sum(k, cutoff)
    terminal = mobius_rough_sum(k, k)
    prime_count = direct_square_interval_prime_count(k)
    if terminal != -prime_count:
        raise AssertionError("terminal cutoff Möbius sum is not minus the prime count")
    if terminal != start + total:
        raise AssertionError("ordered Möbius cutoff jumps failed to telescope")
    if prime_count != -start - total:
        raise AssertionError("ordered Möbius prime recovery failed")

    return {
        "k": k,
        "start_cutoff": cutoff,
        "start_mobius_sum": start,
        "ordered_jump_rows": tuple(rows),
        "ordered_transport_sum": total,
        "terminal_mobius_sum": terminal,
        "prime_count": prime_count,
        "exact_ordered_recovery": True,
    }


def fourth_root_ordered_transport(k: int) -> dict[str, object]:
    """Specialize the ordered transport to z_3(k) and verify the P2 quotient ceiling."""
    z = root_p3_cutoff(k)
    data = ordered_mobius_transport(k, z)
    upper = square_interval_upper(k)
    quotient_rows: list[tuple[int, int, int]] = []
    for p in primes_up_to(k):
        if p <= z:
            continue
        for q in range(k * k // p + 1, upper // p + 1):
            if q <= 1 or least_prime_factor(q) <= p:
                continue
            if q >= (z + 1) ** 3:
                raise AssertionError("ordered fourth-root quotient escaped the P2 ceiling")
            quotient_rows.append((p, q, mobius_value(q)))
    return {
        **data,
        "fourth_root_cutoff": z,
        "ordered_quotient_rows": tuple(quotient_rows),
        "quotient_p2_ceiling": (z + 1) ** 3 - 1,
    }
