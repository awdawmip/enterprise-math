"""Prime-gap consequences of P018 factor proof slack.

Let H(k) be the Stage-7 minimal survivor-prime factor horizon and
sigma(k)=k-H(k).  Near the diagonal p=k-s, sufficiently large least-factor
shells are forced into one semiprime p*q, and the square-basin inequalities force
q=p+2(s+1).  This creates an exact bridge from bounded precision slack to fixed
even prime gaps.

Prime gaps, twin/cousin primes, and bounded-gap theorems are established number
theory.  This module only implements the Enterprise Math change of variables and
finite checks; it does not prove any new bounded-prime-gap result.
"""

from __future__ import annotations

from .factor_precision import first_factor_shell
from .legendre import is_prime
from .p017_precision_horizon import survivor_prime_horizon


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def factor_proof_slack(k: int) -> int:
    """Return sigma(k)=k-H(k)."""
    _require_positive("k", k)
    horizon = survivor_prime_horizon(k)
    if horizon > k:
        raise AssertionError("factor horizon exceeded root-factor horizon")
    return k - horizon


def near_diagonal_prime(k: int, slack: int) -> int:
    """Return p=k-s after validating the near-diagonal shell parameters."""
    _require_positive("k", k)
    _require_natural("slack", slack)
    if slack >= k:
        raise ValueError("slack must be smaller than k")
    return k - slack


def near_diagonal_gap_prime(k: int, slack: int) -> int:
    """Return q=p+2(s+1)=k+s+2."""
    p = near_diagonal_prime(k, slack)
    return p + 2 * (slack + 1)


def near_diagonal_shell_data(k: int, slack: int) -> dict[str, object]:
    """Verify the exact high near-diagonal shell / fixed-gap correspondence.

    The theorem applies when p=k-s is an odd prime and p>(s+1)^2.  Under that
    condition L_p(k) is nonempty iff q=p+2(s+1) is prime, and then the shell is
    the singleton {p*q}.
    """
    p = near_diagonal_prime(k, slack)
    if p < 3 or not is_prime(p):
        raise ValueError("p=k-slack must be an odd prime")
    if p <= (slack + 1) ** 2:
        raise ValueError("near-diagonal theorem requires p>(slack+1)^2")
    q = near_diagonal_gap_prime(k, slack)
    shell = first_factor_shell(k, p)
    expected = [p * q] if is_prime(q) else []
    if shell != expected:
        raise AssertionError("near-diagonal shell / prime-gap theorem failed")
    if expected:
        n = expected[0]
        if not (k * k < n < (k + 1) * (k + 1)):
            raise AssertionError("near-diagonal prime-pair product left the basin")
    return {
        "k": k,
        "slack": slack,
        "p": p,
        "q": q,
        "gap": q - p,
        "shell": shell,
        "nonempty": bool(shell),
    }


def sigma_zero_twin_equivalence(k: int) -> bool:
    """Verify for k>=3 that sigma(k)=0 iff k and k+2 are prime."""
    _require_positive("k", k)
    if k < 3:
        raise ValueError("twin/slack-zero theorem is stated for k>=3")
    return (factor_proof_slack(k) == 0) == (is_prime(k) and is_prime(k + 2))


def sigma_one_cousin_equivalence(k: int) -> bool:
    """Verify for k>=4 that sigma(k)=1 iff k-1 and k+3 are prime."""
    _require_positive("k", k)
    if k < 4:
        raise ValueError("cousin/slack-one theorem is stated for k>=4")
    return (factor_proof_slack(k) == 1) == (
        is_prime(k - 1) and is_prime(k + 3)
    )


def slack_implies_fixed_gap(k: int) -> dict[str, int | bool]:
    """For large-enough actual slack s, verify the forced prime gap 2(s+1)."""
    _require_positive("k", k)
    slack = factor_proof_slack(k)
    p = k - slack
    if p < 3 or p <= (slack + 1) ** 2:
        raise ValueError("actual horizon is not in the near-diagonal theorem range")
    q = p + 2 * (slack + 1)
    if not is_prime(p) or not is_prime(q):
        raise AssertionError("bounded slack did not force its fixed prime pair")
    data = near_diagonal_shell_data(k, slack)
    if not data["nonempty"]:
        raise AssertionError("actual horizon shell must be nonempty")
    return {
        "k": k,
        "slack": slack,
        "p": p,
        "q": q,
        "gap": 2 * (slack + 1),
        "verified": True,
    }


def prime_pair_to_slack_bound(p: int, half_gap: int) -> dict[str, int]:
    """Map a prime pair p,p+2m to a square-basin slack upper bound.

    If p>m^2, set s=m-1 and k=p+s.  The near-diagonal theorem puts p*q in
    L_p(k), so H(k)>=p and sigma(k)<=s=m-1.
    """
    _require_positive("p", p)
    _require_positive("half_gap", half_gap)
    q = p + 2 * half_gap
    if not is_prime(p) or not is_prime(q):
        raise ValueError("p and p+2*half_gap must both be prime")
    if p <= half_gap**2:
        raise ValueError("finite mapping requires p>half_gap^2")
    slack_bound = half_gap - 1
    k = p + slack_bound
    data = near_diagonal_shell_data(k, slack_bound)
    if not data["nonempty"]:
        raise AssertionError("prime pair failed to create the expected shell")
    actual_slack = factor_proof_slack(k)
    if actual_slack > slack_bound:
        raise AssertionError("prime pair did not imply the slack upper bound")
    return {
        "p": p,
        "q": q,
        "gap": 2 * half_gap,
        "k": k,
        "slack_bound": slack_bound,
        "actual_slack": actual_slack,
    }


def bounded_gap_to_slack_constant(max_gap: int) -> int:
    """Convert an even prime-gap bound 2m to the corresponding slack m-1.

    For an upper bound that is not itself even, use the largest possible even
    prime gap not exceeding it.  This helper is only the arithmetic conversion;
    infinitude must come from an external prime-gap theorem.
    """
    _require_positive("max_gap", max_gap)
    even_gap = max_gap if max_gap % 2 == 0 else max_gap - 1
    if even_gap < 2:
        raise ValueError("max_gap must allow a positive even prime gap")
    return even_gap // 2 - 1
