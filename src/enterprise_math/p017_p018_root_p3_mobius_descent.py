"""One-step Möbius quotient descent at the fourth-root P3 cutoff.

For a fourth-root rough square-interval state n, let

    c(n) = #{p prime : z<p<=k and p|n},

and define the one-step medium-prime quotient Möbius sum

    J(n) = sum_{p|n, z<p<=k} mu(n/p).

A complete P3 type check gives the exact pointwise transport law

    J(n) = c(n) - 1 - mu(n).

Consequently, if J_3 is summed over the fourth-root rough survivor set,

    J_3 = S_1 - R_3 - M_3.

Combining this with the affine Möbius/support identity yields

    3*prime_gap(k) = R_3 - 2*M_3 - J_3 - C_3,

where C_3 is the at-most-one rough prime-cube correction.

The quotient sum has a direct channel form:

    J_3 = sum_{z<p<=k, p prime}
            sum_{k^2/p < q <= (k^2+2k)/p, (q,P_z)=1} mu(q).

No prime condition is imposed on q.  Because p>=z+1 and

    U < (z+1)^4,

we have q < U/(z+1) < (z+1)^3.  Thus every z-rough quotient has Omega(q)<=2.
One medium-prime factor removal therefore transports the P3 state exactly into
a P2 quotient world, where the quotient Möbius sign distinguishes squarefree
prime quotients (-1) from squarefree semiprime quotients (+1), with squareful
quotients killed by mu=0.

This is a quotient-channel parity interface, not a proof of the required
pointwise cancellation.
"""

from __future__ import annotations

from .legendre import primes_up_to
from .p017_p018_buchstab_cutoff_ladder import rough_survivor_offsets, square_interval_upper
from .p017_p018_root_p3_mobius_support import (
    mobius_value,
    root_p3_mobius_support_profile,
    rough_prime_cube_offsets,
)
from .p017_p018_root_p3_support_recovery import medium_prime_support, root_p3_cutoff


def state_quotient_mobius_sum(k: int, value: int) -> int:
    """Return sum_p mu(value/p) over distinct medium prime divisors p."""
    if not (k * k < value <= square_interval_upper(k)):
        raise ValueError("value must lie in the square interval")
    z = root_p3_cutoff(k)
    if any(value % p == 0 for p in primes_up_to(z)):
        raise ValueError("value must survive the fourth-root pre-sieve")
    return sum(mobius_value(value // p) for p in medium_prime_support(k, value))


def mobius_descent_transport_row(k: int, value: int) -> dict[str, int | bool]:
    """Verify J(n)=c(n)-1-mu(n) on one bounded state."""
    mu = mobius_value(value)
    depth = len(medium_prime_support(k, value))
    quotient_sum = state_quotient_mobius_sum(k, value)
    expected = depth - 1 - mu
    if quotient_sum != expected:
        raise AssertionError("one-step Möbius descent law failed")
    curvature = 1 - 2 * mu - quotient_sum
    return {
        "k": k,
        "value": value,
        "mobius": mu,
        "support_depth": depth,
        "quotient_mobius_sum": quotient_sum,
        "transport_rhs": expected,
        "mobius_descent_curvature": curvature,
        "transport_identity": True,
    }


def quotient_channel_mobius_sum(k: int) -> dict[str, object]:
    """Evaluate the swapped p/q channel form of J_3 for bounded research."""
    z = root_p3_cutoff(k)
    lower = k * k
    upper = square_interval_upper(k)
    small_primes = tuple(primes_up_to(z))
    medium_primes = tuple(p for p in primes_up_to(k) if p > z)
    channel_rows: list[tuple[int, int, int]] = []
    total = 0

    for p in medium_primes:
        q_min = lower // p + 1
        q_max = upper // p
        if q_max >= (z + 1) ** 3:
            raise AssertionError("P3 quotient channel escaped the P2 root ceiling")
        for q in range(q_min, q_max + 1):
            if any(q % r == 0 for r in small_primes):
                continue
            mu_q = mobius_value(q)
            total += mu_q
            channel_rows.append((p, q, mu_q))

    return {
        "k": k,
        "fourth_root_cutoff": z,
        "channel_rows": tuple(channel_rows),
        "quotient_channel_mobius_sum": total,
        "quotient_root_p2_ceiling": (z + 1) ** 3 - 1,
    }


def root_p3_mobius_descent_profile(k: int) -> dict[str, object]:
    """Cross-check state and quotient-channel Möbius recovery forms."""
    z = root_p3_cutoff(k)
    offsets = rough_survivor_offsets(k, z)
    state_sum = 0
    curvature_sum = 0
    for offset in offsets:
        row = mobius_descent_transport_row(k, k * k + offset)
        state_sum += int(row["quotient_mobius_sum"])
        curvature_sum += int(row["mobius_descent_curvature"])

    channel = quotient_channel_mobius_sum(k)
    if state_sum != int(channel["quotient_channel_mobius_sum"]):
        raise AssertionError("state and swapped quotient-channel sums disagree")

    affine = root_p3_mobius_support_profile(k)
    expected_transport = (
        int(affine["support_moment_1"])
        - int(affine["rough_count"])
        - int(affine["mobius_sum"])
    )
    if state_sum != expected_transport:
        raise AssertionError("global Möbius transport identity failed")

    cube_count = len(rough_prime_cube_offsets(k))
    prime_count = int(affine["prime_count"])
    exact_rhs = int(affine["rough_count"]) - 2 * int(affine["mobius_sum"]) - state_sum - cube_count
    if exact_rhs != 3 * prime_count:
        raise AssertionError("Möbius descent prime recovery failed")
    if curvature_sum != 3 * prime_count + cube_count:
        raise AssertionError("Möbius descent curvature type table failed")

    return {
        **affine,
        "quotient_mobius_sum": state_sum,
        "quotient_channel_rows": channel["channel_rows"],
        "mobius_descent_curvature_sum": curvature_sum,
        "descent_prime_identity_rhs": exact_rhs,
        "exact_mobius_descent_recovery": True,
    }
