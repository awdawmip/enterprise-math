"""Global large-tail resource uniqueness in the consecutive-square hard core.

A residual hard-core state has the form ``n=d*q`` with odd full k-smooth core
``d`` and prime tail ``q>k``. The tail itself determines the core and the fine
state uniquely.

Indeed, if ``k^2 < d*q < (k+1)^2`` and ``q>k``, the real-free integer multiplier
window has width less than two:

    ((k+1)^2-k^2)/q = (2k+1)/q < 2.

Thus at most two consecutive integer multipliers can place a multiple of q in
the open square basin. Exactly one of two consecutive integers is odd, so an
odd hard-core multiplier is unique. If

    a = floor(k^2/q)+1,

then the unique possible odd core is ``a`` when a is odd and ``a+1`` otherwise.

Consequences:
- a large prime tail cannot be reused by two different hard-core states;
- the tail value recovers its core cell, fine state, mirror radius and side;
- distinct hard-core mirror pairs consume disjoint large-prime tail resources.

This is a P017/P018 bridge consequence, not a new primality theorem.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime
from .p017_mirror import mirror_center


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def odd_core_candidate_from_large_tail(k: int, tail: int) -> int:
    """Return the unique odd multiplier that could place tail in the basin."""
    _require_int("k", k)
    _require_int("tail", tail)
    if k < 2 or tail <= k:
        raise ValueError("require k>=2 and tail>k")
    first = (k * k) // tail + 1
    return first if first % 2 == 1 else first + 1


def recover_odd_core_state(k: int, tail: int) -> dict[str, int | bool]:
    """Recover the unique odd-core square-basin state carried by a large tail."""
    core = odd_core_candidate_from_large_tail(k, tail)
    state = core * tail
    lower = k * k
    upper = (k + 1) * (k + 1)
    exists = lower < state < upper

    # The open multiplier interval has length strictly less than two because
    # tail>=k+1. Hence no second odd integer multiplier can work.
    if 2 * tail <= 2 * k + 1:
        raise AssertionError("large-tail multiplier window was not shorter than two")
    for alternative in (core - 2, core + 2):
        if alternative >= 1 and lower < alternative * tail < upper:
            raise AssertionError("large tail admitted two odd square-basin multipliers")

    result: dict[str, int | bool] = {
        "k": k,
        "tail": tail,
        "core": core,
        "state": state,
        "exists": exists,
    }
    if exists:
        center = mirror_center(k)
        radius = abs(state - center)
        result.update(
            {
                "center": center,
                "radius": radius,
                "side": -1 if state < center else 1,
                "anchor_coprime": gcd(state, center) == 1,
            }
        )
    return result


def recover_hard_core_state_from_prime_tail(k: int, tail: int) -> dict[str, int | bool]:
    """Recover and validate an anchor-surviving hard-core state from its prime tail."""
    if not is_prime(tail):
        raise ValueError("tail must be prime")
    data = recover_odd_core_state(k, tail)
    if not bool(data["exists"]):
        raise ValueError("tail has no odd-core multiple in the open square basin")
    core = int(data["core"])
    radius = int(data["radius"])
    if core <= 1 or core > k:
        raise ValueError("recovered core is not a nontrivial k-smooth-core candidate")
    if radius <= 0 or radius >= k:
        raise ValueError("recovered state is not in an anchor-surviving mirror radius")
    if not bool(data["anchor_coprime"]):
        raise ValueError("recovered state does not survive the anchor sieve")
    return data
