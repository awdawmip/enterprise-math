"""Prime-tail mirror matching for the residual P017 hard core.

The canonical mirror involution on fine states,

    n |-> 2*k*(k+1) - n,

 descends to a fixed-point-free partial involution on residual hard-core large
prime tails. The descent is exact because ``p017_p018_tail_resource`` proves
that a tail q>k uniquely recovers its odd full core and fine state.

Thus the residual hard core may be represented as a matching on globally
non-reusable prime resources. Core labels, state, radius and side are derived
coordinates of each prime vertex rather than independent data.
"""

from __future__ import annotations

from .p017_cofactor_window import square_basin_smooth_tail
from .p017_p018_tail_resource import recover_hard_core_state_from_prime_tail


def residual_hard_core_tail_partner(k: int, tail: int) -> dict[str, int]:
    """Return the unique mirror-partner prime tail in the residual S_-S_+<k branch."""
    source = recover_hard_core_state_from_prime_tail(k, tail)
    center = int(source["center"])
    state = int(source["state"])
    core = int(source["core"])
    mirror_state = 2 * center - state
    if not (k * k < mirror_state < (k + 1) ** 2):
        raise AssertionError("mirror state escaped the open square basin")

    mirror_data = square_basin_smooth_tail(k, mirror_state)
    if bool(mirror_data["is_prime"]):
        raise ValueError("mirror state is prime, so the source is not in the residual hard core")
    mirror_core = int(mirror_data["smooth_core"])
    partner = int(mirror_data["tail"])
    if mirror_core <= 1 or partner <= k:
        raise ValueError("mirror state has no nontrivial core plus large prime tail")
    if core * mirror_core >= k:
        raise ValueError("residual hard-core branch requires core product < k")

    recovered = recover_hard_core_state_from_prime_tail(k, partner)
    if int(recovered["state"]) != mirror_state:
        raise AssertionError("partner tail failed to recover the mirror state")
    if int(recovered["core"]) != mirror_core:
        raise AssertionError("partner tail failed to recover the mirror core")
    if int(recovered["radius"]) != int(source["radius"]):
        raise AssertionError("mirror-tail vertices lost their common radius")
    if int(recovered["side"]) != -int(source["side"]):
        raise AssertionError("mirror-tail vertices did not occupy opposite sides")
    if partner == tail:
        raise AssertionError("residual mirror-tail involution acquired a fixed point")

    return {
        "k": k,
        "tail": tail,
        "core": core,
        "state": state,
        "partner_tail": partner,
        "partner_core": mirror_core,
        "partner_state": mirror_state,
        "radius": int(source["radius"]),
        "side": int(source["side"]),
    }


def residual_hard_core_tail_cycle(k: int, tail: int) -> dict[str, int]:
    """Certify that applying the tail partner map twice returns the original tail."""
    first = residual_hard_core_tail_partner(k, tail)
    second = residual_hard_core_tail_partner(k, int(first["partner_tail"]))
    if int(second["partner_tail"]) != tail:
        raise AssertionError("residual hard-core tail map is not an involution")
    if int(second["radius"]) != int(first["radius"]):
        raise AssertionError("two-cycle changed mirror radius")
    return {
        **first,
        "cycle_back_tail": int(second["partner_tail"]),
    }
