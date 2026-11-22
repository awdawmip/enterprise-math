"""Moving-cutoff dynamics of the square covering height.

Let h(y) be the least positive x whose window x^2+1,...,x^2+2y is fully hit
by the primorial P_y, with h(y)=infinity when no such x exists.

This file records the first genuinely moving-cutoff laws.  They are not visible
in a fixed-wheel square phase.

Composite step monotonicity
---------------------------
If y+1 is composite then P_{y+1}=P_y.  A root covering the longer horizon
2(y+1) also covers the shorter horizon 2y, so the feasible-root set can only
shrink and

    h(y+1) >= h(y).

Thus downward jumps in covering height are possible only when the cutoff itself
crosses a new prime.

Least-counterexample plateau
----------------------------
If y>=3 is the least Legendre counterexample, then h(y)=y.  In fact

    h(y-1)=h(y)=y.

The root x=y covers the full y-horizon by assumption.  When the cutoff is
lowered from y to y-1, the only lost prime can be y itself (when y is prime).
Inside the shorter horizon 1<=r<=2y-2, the only multiple of y above y^2 is at
r=y; for odd prime y this state is y(y+1), already divisible by 2<=y-1.
Hence x=y remains a fixed-(y-1) covering root.  Minimality of the first
Legendre failure, together with the covering-height equivalence, excludes every
root <=y-1 and forces h(y-1)=y.

Prime-block sufficient reduction
--------------------------------
Let p be prime and q the next prime.  For every y in [p,q-1], P_y=P_p.  If y
were a Legendre counterexample, the root x=y would also cover the shorter
fixed-p horizon 2p, so h(p)<=y<=q-1.  Therefore the prime-cutoff condition

    h(p) > q-1

for every prime p is sufficient for Legendre's conjecture.  It is intentionally
not claimed necessary: a root that covers only the p-horizon may fail when the
horizon is later extended to its own diagonal length.
"""

from __future__ import annotations

from .legendre import is_prime, primes_up_to
from .p017_p018_square_covering_height import (
    bounded_square_covering_height,
    is_fixed_y_square_covering_root,
)
from .p017_p018_square_sign_orbit import primorial


def next_prime_after(n: int) -> int:
    """Return the least prime strictly larger than n by deterministic search."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def verify_composite_step_feasible_root_nesting(
    y: int, search_limit: int
) -> dict[str, object]:
    """Boundedly verify fixed-root nesting across a composite cutoff step."""
    if isinstance(y, bool) or not isinstance(y, int) or y < 2:
        raise ValueError("y must be an integer >=2")
    if is_prime(y + 1):
        raise ValueError("y+1 must be composite")
    if primorial(y + 1) != primorial(y):
        raise AssertionError("composite step unexpectedly changed the primorial")

    roots_y = tuple(
        x for x in range(1, search_limit + 1) if is_fixed_y_square_covering_root(x, y)
    )
    roots_next = tuple(
        x
        for x in range(1, search_limit + 1)
        if is_fixed_y_square_covering_root(x, y + 1)
    )
    if not set(roots_next) <= set(roots_y):
        raise AssertionError("longer composite-step horizon created a new fixed root")

    return {
        "y": y,
        "next_cutoff": y + 1,
        "search_limit": search_limit,
        "roots_at_y": roots_y,
        "roots_at_next": roots_next,
        "bounded_feasible_root_nesting": True,
        "theorem": "h(y+1)>=h(y) when y+1 is composite",
    }


def verify_prime_block_counterexample_implication(
    p: int, y: int
) -> dict[str, object]:
    """Verify the fixed-p cover forced by a supplied diagonal counterexample y."""
    if not is_prime(p):
        raise ValueError("p must be prime")
    q = next_prime_after(p)
    if not (p <= y < q):
        raise ValueError("y must lie in the prime block [p,next_prime(p)-1]")
    if primorial(y) != primorial(p):
        raise AssertionError("prime block changed its primorial")
    if not is_fixed_y_square_covering_root(y, y):
        raise ValueError("y is not a Legendre-counterexample covering root")
    if not is_fixed_y_square_covering_root(y, p):
        raise AssertionError("counterexample root failed to cover the prime-block prefix")
    return {
        "p": p,
        "next_prime": q,
        "y": y,
        "fixed_p_covering_root": y,
        "forces_h_p_at_most_y": True,
        "h_p_upper_target": q - 1,
    }


def bounded_prime_block_safety_certificate(p: int, search_limit: int) -> dict[str, object]:
    """Certify only a bounded version of h(p)>next_prime(p)-1 by direct search."""
    if not is_prime(p):
        raise ValueError("p must be prime")
    q = next_prime_after(p)
    required = q - 1
    if search_limit < required:
        raise ValueError("search_limit must reach the end of the prime block")
    data = bounded_square_covering_height(p, required)
    return {
        "p": p,
        "next_prime": q,
        "prime_block_end": required,
        "first_covering_root_through_block_end": data["first_covering_root_in_search"],
        "bounded_prime_block_safe": data["no_covering_root_in_search"],
    }
