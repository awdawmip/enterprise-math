"""Terminal half-cutoff Buchstab staircase on the square-root diagonal.

This module refines the half-cutoff decomposition in
``p017_p018_square_anchor_sieve_diagonal`` without changing its proof status.
For k>=10, every half-rough composite in

    I_k = {k^2+1, ..., k^2+2k}

is a semiprime pq with k/2<p<=k<q<2k+4.  The high factor p does more than give
a degree-two bound: its possible odd cofactors are explicit.

Let p be an odd prime with k/2<p<=k, put a=k-p, and divide

    a^2 = 2 p u + v,             0 <= v < 2p.

Then the first multiple of p strictly above k^2 whose quotient by p is odd is

    k^2 + r_1 = p q_1,
    r_1 = 2p-v,
    q_1 = k+a+2u+2.

It always lies in I_k.  There is exactly one further possible odd-quotient
multiple in I_k, namely

    q_2=q_1+2,   r_2=r_1+2p,

and it exists exactly when r_1<=2a.  Hence the half-rough composite deletion at
p is

    Delta_p(k)
      = 1_P(q_1)
        + 1_{r_1<=2a} 1_P(q_1+2),

so Delta_p is 0, 1, or 2, and Delta_p=2 forces a twin-prime pair.  Moreover the
two halves of I_k are separately matchings: a fixed p contributes at most one
semiprime to each half, and a double contribution places q_1 in the first half
and q_1+2 in the second.

Consequently, if R_half(k) denotes the count after sieving only by primes
<=k/2, then the terminal Buchstab band is the exact staircase

    pi((k+1)^2)-pi(k^2)
      = R_half(k) - sum_{k/2<p<=k} Delta_p(k).

There is also an additive shell interpretation.  For the primary candidate,

    p + q_1 = 2(k+u+1).

Thus fixing u turns the reciprocal hyperbola into a restricted Goldbach shell;
the shell condition is exactly

    2pu <= (k-p)^2 < 2p(u+1).

The optional second candidate moves to the adjacent even sum.  This is a
coordinate reduction for the high-prime tail, not a prime-existence theorem.
"""

from __future__ import annotations

from .legendre import direct_square_interval_prime_count, is_prime, primes_up_to
from .p017_p018_square_anchor_sieve_diagonal import half_cutoff_rough_decomposition


def high_prime_odd_quotient_candidates(k: int, p: int) -> dict[str, object]:
    """Return the one or two possible odd-quotient multiples for a high prime p."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")
    if isinstance(p, bool) or not isinstance(p, int) or not is_prime(p):
        raise ValueError("p must be prime")
    if not (2 * p > k and p <= k):
        raise ValueError("p must satisfy k/2 < p <= k")

    a = k - p
    shell_index, remainder = divmod(a * a, 2 * p)
    q1 = k + a + 2 * shell_index + 2
    r1 = 2 * p - remainder

    if q1 % 2 != 1:
        raise AssertionError("primary cofactor candidate must be odd")
    if not (1 <= r1 <= 2 * k):
        raise AssertionError("primary odd-quotient multiple left the square interval")
    if p * q1 != k * k + r1:
        raise AssertionError("primary high-prime candidate identity failed")
    if not (q1 > k):
        raise AssertionError("primary cofactor must lie above k")
    if p + q1 != 2 * (k + shell_index + 1):
        raise AssertionError("primary Goldbach-shell identity failed")

    candidates: list[dict[str, object]] = [
        {
            "rank": 1,
            "q": q1,
            "offset": r1,
            "half": 1 if r1 <= k else 2,
            "prime_q": is_prime(q1),
        }
    ]

    if r1 <= 2 * a:
        q2 = q1 + 2
        r2 = r1 + 2 * p
        if not (k < r2 <= 2 * k):
            raise AssertionError("secondary candidate must lie in the second half")
        if p * q2 != k * k + r2:
            raise AssertionError("secondary high-prime candidate identity failed")
        candidates.append(
            {
                "rank": 2,
                "q": q2,
                "offset": r2,
                "half": 2,
                "prime_q": is_prime(q2),
            }
        )

    # Moving by another odd quotient adds 2p>k to the offset.  The predecessor
    # of q1 is at offset -remainder<=0, while a successor after q2 (if present)
    # is already beyond 2k.  Hence the list is complete.
    if len(candidates) > 2:
        raise AssertionError("high-prime candidate count exceeded two")

    return {
        "k": k,
        "p": p,
        "a": a,
        "shell_index": shell_index,
        "quadratic_remainder_mod_2p": remainder,
        "candidates": tuple(candidates),
        "prime_jump": sum(bool(item["prime_q"]) for item in candidates),
        "double_candidate": len(candidates) == 2,
    }


def terminal_buchstab_staircase(k: int) -> dict[str, object]:
    """Evaluate the exact high-prime deletion staircase from k/2 up to k."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")

    half = half_cutoff_rough_decomposition(k)
    high_primes = tuple(p for p in primes_up_to(k) if 2 * p > k)

    steps: list[dict[str, object]] = []
    staircase_edges: list[tuple[int, int, int, int]] = []
    first_half_edges: list[tuple[int, int, int]] = []
    second_half_edges: list[tuple[int, int, int]] = []

    for p in high_primes:
        data = high_prime_odd_quotient_candidates(k, p)
        prime_candidates = tuple(
            item for item in data["candidates"] if item["prime_q"]
        )
        jump = len(prime_candidates)
        if jump > 2:
            raise AssertionError("terminal Buchstab jump exceeded two")
        if jump == 2:
            q_values = [int(item["q"]) for item in prime_candidates]
            if q_values[1] - q_values[0] != 2:
                raise AssertionError("double terminal jump must be twin-prime")
            if tuple(int(item["half"]) for item in prime_candidates) != (1, 2):
                raise AssertionError("double terminal jump must split across halves")

        for item in prime_candidates:
            q = int(item["q"])
            offset = int(item["offset"])
            edge = (p, q, k * k + offset, offset)
            staircase_edges.append(edge)
            half_edge = (p, q, offset)
            if item["half"] == 1:
                first_half_edges.append(half_edge)
            else:
                second_half_edges.append(half_edge)

        steps.append(
            {
                "p": p,
                "shell_index": data["shell_index"],
                "jump": jump,
                "prime_candidates": prime_candidates,
            }
        )

    expected_edges = set(half["semiprime_edges"])
    actual_edges = set(staircase_edges)
    if actual_edges != expected_edges:
        raise AssertionError("explicit staircase failed to recover the semiprime tail")

    deletion_count = sum(int(step["jump"]) for step in steps)
    if deletion_count != half["semiprime_count"]:
        raise AssertionError("terminal staircase deletion count mismatch")

    recovered_prime_count = int(half["half_rough_count"]) - deletion_count
    direct_prime_count = direct_square_interval_prime_count(k)
    if recovered_prime_count != direct_prime_count:
        raise AssertionError("terminal staircase failed to recover the prime gap")

    first_lefts = [p for p, _q, _r in first_half_edges]
    second_lefts = [p for p, _q, _r in second_half_edges]
    first_rights = [q for _p, q, _r in first_half_edges]
    second_rights = [q for _p, q, _r in second_half_edges]
    if len(first_lefts) != len(set(first_lefts)):
        raise AssertionError("first half is not a left matching")
    if len(second_lefts) != len(set(second_lefts)):
        raise AssertionError("second half is not a left matching")
    if len(first_rights + second_rights) != len(set(first_rights + second_rights)):
        raise AssertionError("right prime was reused across the terminal band")

    return {
        "k": k,
        "half_rough_count": half["half_rough_count"],
        "high_primes": high_primes,
        "steps": tuple(steps),
        "staircase_edges": tuple(sorted(staircase_edges)),
        "deletion_count": deletion_count,
        "recovered_prime_count": recovered_prime_count,
        "direct_prime_count": direct_prime_count,
        "first_half_edges": tuple(sorted(first_half_edges)),
        "second_half_edges": tuple(sorted(second_half_edges)),
        "terminal_identity_exact": True,
    }
