"""One-dimensional quotient-channel normal form for ordered Möbius descent.

Start at the fourth-root cutoff z=floor((k^2+2k)^(1/4)).  The ordered
Möbius/Buchstab transport is

    B = sum_{z<p<=k} sum_{k^2<pq<=U, P^-(q)>p} mu(q).

Every quotient q is >k.  Therefore, after swapping the order of summation, the
admissible p-interval

    k^2/q < p <= U/q

has length 2k/q<2.  Since every nonzero row is odd, this interval contains at
most one parity-compatible odd integer.  Let

    m = floor(U/q),
    p_*(q) = m          if m is odd,
             m-1        if m is even.

Then q contributes exactly when

    k^2 < p_*(q) q <= U,
    z < p_*(q) <= k,
    p_*(q) is prime,
    P^-(q) > p_*(q).

Thus the ordered transport is an exact one-dimensional scan over

    k < q < U/(z+1) < (z+1)^3,

with weight mu(q) and one deterministic prime-candidate gate.

The P2 quotient ceiling creates a directional sign barrier.  Any nonzero
positive row has mu(q)=+1, hence q is a squarefree semiprime.  If a=P^-(q),
then the ordered condition gives

    k^2/q < p_*(q) < a <= sqrt(q).

Therefore q^(3/2)>k^2, equivalently

    q^3 > k^4.

Consequently the entire exact integer band

    q^3 <= k^4

contains no positive transport at all: every nonzero contribution there comes
from a prime quotient and has sign -1.  Positive squarefree-triple transport is
confined to q^3>k^4, i.e. asymptotically q>k^(4/3)=X^(2/3) for X=k^2.

Equivalently in least-factor coordinates, positive transport is possible only
below the cubic-root P2 factor boundary.  The root-cutoff ladder is therefore
visible directly as a sign-support transition in ordered quotient space.
"""

from __future__ import annotations

from .legendre import is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import square_interval_upper
from .p017_p018_root_p3_mobius_support import mobius_value
from .p017_p018_root_p3_ordered_mobius_buchstab import least_prime_factor
from .p017_p018_root_p3_support_recovery import root_p3_cutoff


def ordered_prime_candidate(k: int, q: int) -> dict[str, int | bool]:
    """Return the unique parity-compatible p candidate for one quotient q>k."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(q, bool) or not isinstance(q, int) or q <= k:
        raise ValueError("q must be an integer >k")
    upper = square_interval_upper(k)
    m = upper // q
    p = m if m % 2 == 1 else m - 1
    in_shell = k * k < p * q <= upper
    return {
        "k": k,
        "q": q,
        "floor_upper_quotient": m,
        "prime_candidate": p,
        "candidate_is_odd": p % 2 == 1,
        "candidate_in_square_shell": in_shell,
        "candidate_at_most_k": (not in_shell) or p <= k,
    }


def ordered_quotient_row(k: int, q: int) -> dict[str, object]:
    """Classify one z_3-rough quotient in the one-dimensional transport scan."""
    z = root_p3_cutoff(k)
    if not (k < q < (z + 1) ** 3):
        raise ValueError("q must lie in the fourth-root P2 quotient range")
    if any(q % p == 0 for p in primes_up_to(z)):
        raise ValueError("q must be fourth-root rough")

    candidate = ordered_prime_candidate(k, q)
    p = int(candidate["prime_candidate"])
    mu_q = mobius_value(q)
    least = least_prime_factor(q)
    active = (
        bool(candidate["candidate_in_square_shell"])
        and p > z
        and is_prime(p)
        and least > p
    )
    contribution = mu_q if active else 0

    if contribution > 0:
        if mu_q != 1:
            raise AssertionError("positive transport did not come from mu=+1")
        if q**3 <= k**4:
            raise AssertionError("positive ordered transport entered the lower quotient band")
    return {
        **candidate,
        "fourth_root_cutoff": z,
        "mobius": mu_q,
        "least_prime_factor": least,
        "ordered_gate_active": active,
        "ordered_transport_contribution": contribution,
        "positive_transport_forces_q_cubed_above_k_fourth": contribution <= 0 or q**3 > k**4,
    }


def one_dimensional_ordered_transport(k: int) -> dict[str, object]:
    """Enumerate the swapped quotient scan and its sign-separated bands."""
    z = root_p3_cutoff(k)
    upper = square_interval_upper(k)
    q_max = upper // (z + 1)
    rows: list[dict[str, object]] = []
    negative_lower = 0
    negative_upper = 0
    positive_upper = 0
    total = 0
    small_primes = tuple(primes_up_to(z))

    for q in range(k + 1, q_max + 1):
        if any(q % p == 0 for p in small_primes):
            continue
        row = ordered_quotient_row(k, q)
        contribution = int(row["ordered_transport_contribution"])
        if contribution == 0:
            continue
        rows.append(row)
        total += contribution
        lower_band = q**3 <= k**4
        if lower_band:
            if contribution > 0:
                raise AssertionError("positive transport appeared at q^3<=k^4")
            negative_lower += -contribution
        elif contribution < 0:
            negative_upper += -contribution
        else:
            positive_upper += contribution

    return {
        "k": k,
        "fourth_root_cutoff": z,
        "quotient_scan_max": q_max,
        "active_rows": tuple(rows),
        "ordered_transport_sum": total,
        "negative_lower_band_mass": negative_lower,
        "negative_upper_band_mass": negative_upper,
        "positive_upper_band_mass": positive_upper,
        "lower_band_has_no_positive_transport": True,
        "sign_barrier_exact_form": "q^3<=k^4 => contribution<=0",
    }
