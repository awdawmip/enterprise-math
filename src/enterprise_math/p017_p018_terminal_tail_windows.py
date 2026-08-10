"""Exact prime-tail window representation of the even-J terminal residual.

Consume the near-primorial terminal full-core shell.  Every candidate complete
core A satisfies

    1 < A <= k-1,
    omega(rad A)=J.

For a signed basin state n=Aq the exact cofactor window is

    W_A(k) = [ floor(k^2/A)+1, floor(k(k+2)/A) ].

Because A<=k-1,

    min W_A >= floor(k^2/(k-1))+1 = k+2.

If A is the *complete* transverse small-prime core, q has no prime divisor <=k.
The window also has q<(k+1)^2.  Therefore q cannot be a nontrivial composite:
any composite with every prime factor >k is at least (k+1)^2.  Thus q is a
prime >k+1.

Conversely, for any prime q in W_A(k), n=Aq has no additional small-prime
factor beyond A.  Since A is transverse and q>k+1 exceeds every prime divisor
of M=k(k+1), the resulting signed state is anchor-surviving and has complete
core exactly A.

Hence the terminal residual incidence is exactly

    R_terminal(k) = sum_A # (Primes intersect W_A(k)).

Distinct terminal cores are odd and below k.  Consuming the P017 tail-staircase
window-separation theorem, their quotient windows are strictly disjoint in
reverse core order.

The window width is itself an exact P018/P007 quotient response.  Since
`k(k+2)=k^2+2k`, write

    2k = A*b + h,      0<=h<A,
    k^2 = A*q + r,     0<=r<A.

Then

    |W_A| = b + kappa_A,
    kappa_A = floor((r+h)/A) in {0,1}.

Thus the unresolved integer resource mass splits exactly into a reciprocal-core
bulk plus binary quotient carries:

    W_terminal = sum_A floor(2k/A) + sum_A kappa_A.

There is also a scale-wide next-prime width horizon.  Let P_J be the minimum
J-prime transverse radical and let p_{J+1} be the first blocking transverse
prime.  Maximality of J gives

    P_J*p_{J+1} >= k.

Every terminal core has A>=P_J, hence

    |W_A| <= floor(2k/P_J)+1 <= 2*p_{J+1}+1.

So each unresolved tail window lives on the next-transverse-prime scale rather
than a k-sized interval.

This is an exact resource representation, not a prime-distribution bound and not
a Legendre proof.  Its value is that the unresolved terminal correction lives
on a very small union of disjoint integer windows and its raw size uses the same
finite-response/carry algebra as the rest of the precision calculus.
"""

from __future__ import annotations

from .legendre import is_prime
from .p017_p018_terminal_shell_capacity import terminal_full_core_candidates


def terminal_tail_window(k: int, full_core: int) -> dict[str, object]:
    """Return W_A, its quotient-response carry, and its exact prime tails."""
    shell = terminal_full_core_candidates(k)
    candidates = set(int(value) for value in shell["full_core_candidates"])
    if full_core not in candidates:
        raise ValueError("full_core is not in the terminal candidate shell")

    lower_argument = k * k
    increment = 2 * k
    q_min = lower_argument // full_core + 1
    q_max = (lower_argument + increment) // full_core
    if q_min < k + 2:
        raise AssertionError("terminal low core failed q_min>=k+2")
    if q_max >= (k + 1) * (k + 1):
        raise AssertionError("terminal quotient window escaped the composite roughness cutoff")

    bulk, increment_remainder = divmod(increment, full_core)
    lower_remainder = lower_argument % full_core
    carry = (lower_remainder + increment_remainder) // full_core
    if carry not in (0, 1):
        raise AssertionError("terminal quotient-window response carry is not binary")
    window_size = max(0, q_max - q_min + 1)
    if window_size != bulk + carry:
        raise AssertionError("terminal quotient-window width failed bulk+carry transport")

    prime_tails = tuple(q for q in range(q_min, q_max + 1) if is_prime(q))
    center = k * (k + 1)
    rows: list[dict[str, int]] = []
    for q in prime_tails:
        state = full_core * q
        signed_point = center - state
        if not (k * k < state <= k * (k + 2)):
            raise AssertionError("terminal tail state escaped the consecutive-square signed range")
        if signed_point == 0 or abs(signed_point) >= k:
            # The only possible endpoint/unpaired states are non-anchor states;
            # q>k+1 prevents them from occurring here.
            raise AssertionError("prime terminal tail did not produce a signed mirror state")
        from math import gcd

        if gcd(abs(signed_point), center) != 1:
            raise AssertionError("prime terminal tail failed anchor survival")
        rows.append(
            {
                "full_core": full_core,
                "tail_prime": q,
                "state": state,
                "signed_point": signed_point,
            }
        )

    return {
        "k": k,
        "full_core": full_core,
        "q_min": q_min,
        "q_max": q_max,
        "window_size": window_size,
        "window_bulk": bulk,
        "window_carry": carry,
        "lower_argument_remainder": lower_remainder,
        "increment_remainder": increment_remainder,
        "prime_tails": prime_tails,
        "prime_tail_count": len(prime_tails),
        "rows": tuple(rows),
    }


def terminal_tail_window_profile(k: int) -> dict[str, object]:
    """Return all disjoint terminal prime-tail windows and their exact incidence mass."""
    shell = terminal_full_core_candidates(k)
    cores = tuple(int(value) for value in shell["full_core_candidates"])
    rows = tuple(terminal_tail_window(k, core) for core in cores)

    ordered = sorted(rows, key=lambda row: int(row["full_core"]))
    for left, right in zip(ordered, ordered[1:]):
        a = int(left["full_core"])
        b = int(right["full_core"])
        if not (a < b and a % 2 == 1 and b % 2 == 1 and b - a >= 2):
            raise AssertionError("terminal core ordering lost odd separation")
        # k(b-a)>2a implies a(k+2)<bk and therefore W_b lies below W_a.
        if not k * (b - a) > 2 * a:
            raise AssertionError("odd terminal cores failed strict quotient-window separation")
        if not int(right["q_max"]) < int(left["q_min"]):
            raise AssertionError("distinct terminal tail windows overlap")

    all_tails = tuple(q for row in rows for q in row["prime_tails"])
    if len(all_tails) != len(set(all_tails)):
        raise AssertionError("terminal large-prime tail resource was reused")

    signed_points = tuple(int(item["signed_point"]) for row in rows for item in row["rows"])
    if len(signed_points) != len(set(signed_points)):
        raise AssertionError("distinct terminal prime-tail resources mapped to one signed state")

    total_window = sum(int(row["window_size"]) for row in rows)
    total_bulk = sum(int(row["window_bulk"]) for row in rows)
    total_carry = sum(int(row["window_carry"]) for row in rows)
    if total_window != total_bulk + total_carry:
        raise AssertionError("terminal window profile failed aggregate bulk+carry identity")

    base = int(shell["base_primorial_product"])
    blocking_prime = shell.get("blocking_prime")
    if blocking_prime is None:
        next_prime_width_ceiling = None
    else:
        next_prime = int(blocking_prime)
        if base * next_prime < k:
            raise AssertionError("blocking transverse prime did not push P_J across k")
        next_prime_width_ceiling = 2 * next_prime + 1
        if any(int(row["window_size"]) > next_prime_width_ceiling for row in rows):
            raise AssertionError("terminal tail window exceeded the next-prime width horizon")

    return {
        **shell,
        "window_rows": rows,
        "total_window_integer_mass": total_window,
        "total_window_bulk_mass": total_bulk,
        "total_window_carry_mass": total_carry,
        "next_transverse_prime": None if blocking_prime is None else int(blocking_prime),
        "per_window_next_prime_width_ceiling": next_prime_width_ceiling,
        "terminal_prime_tail_count": len(all_tails),
        "terminal_prime_tails": tuple(sorted(all_tails)),
        "terminal_signed_points": tuple(sorted(signed_points)),
        "tail_windows_pairwise_disjoint": True,
        "prime_tails_globally_distinct": True,
    }
