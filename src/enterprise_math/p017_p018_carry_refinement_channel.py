"""Exact quotient-channel refinement of P017 centered divisor fibers.

Fix K=k-1, M=(K+1)(K+2), and an odd parent modulus E.  The signed parent fiber

    -K<=x<=K,  x odd,  E | M-x

is an arithmetic progression

    x_t=x_0+2Et,              0<=t<N,

where N=F_E(K).  Divide the complementary basin state by E:

    y_t=(M-x_t)/E=y_0-2t.

For any positive odd refinement factor d, the child modulus Ed selects exactly
those parent indices for which d|y_t.  Since 2 is invertible modulo d, there is
one index channel

    t = tau_d (mod d),
    tau_d = y_0 * 2^(-1) (mod d),   0<=tau_d<d.

If N=ad+r, the exact child fiber size is therefore

    F_(Ed)(K)=a+chi,
    chi=1 iff tau_d<r.

Equivalently,

    F_(Ed)(K)=floor(F_E(K)/d)+chi_(E->Ed)(K).

This chi is a **quotient-channel carry** in the finite parent-fiber index space,
not an independent new local-density bit.

The channel state closes under repeated refinement.  When the child is nonempty,
its first quotient is

    y'_0=(y_0-2 tau_d)/d,

and its quotient progression is again y'_u=y'_0-2u.  Consequently for all
positive odd d1,d2,

    R_d2(R_d1(N,y_0)) = R_(d1*d2)(N,y_0),

with the empty state absorbing.  Thus positive odd multiplication acts as an
exact refinement monoid on finite quotient-channel states.

In terms of the original binary centered carries, write

    q_E=floor(K/E),
    F_E=q_E+eta_E.

Since floor(K/(Ed))=floor(q_E/d),

    eta_(Ed)
      = chi_(E->Ed)
        + 1_{eta_E=1 and q_E=-1 (mod d)}.

The two terms are automatically mutually exclusive because eta_(Ed) is binary.
In the high-product region E>K, q_E=0 and F_E=eta_E<=1, so child survival is
monotone:

    eta_(Ed)<=eta_E.

Hence the large-modulus carry support is divisibility-downward along the
refinement network.

This theorem is an exact P017 divisor-fiber -> P018 quotient-channel interface.
It does not by itself overcome the terminal Mobius carry-sign / sieve parity
boundary; rather, it identifies the cross-modulus structure that any further
argument must actually use.
"""

from __future__ import annotations

from .p017_p018_carry_phase_mean import unified_centered_carry_bit


def _require_positive_odd(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1 or value % 2 == 0:
        raise ValueError(f"{name} must be a positive odd integer")


def signed_fiber_channel_state(K: int, modulus: int) -> dict[str, object]:
    """Return the exact finite progression state (N,y0) for one odd modulus."""
    if isinstance(K, bool) or not isinstance(K, int) or K < 0:
        raise ValueError("K must be a nonnegative integer")
    _require_positive_odd("modulus", modulus)
    E = modulus
    M = (K + 1) * (K + 2)
    period = 2 * E
    raw = M % E
    residue = raw if raw % 2 else raw + E
    residue %= period

    first_index = -((-K - residue) // period)
    last_index = (K - residue) // period
    count = max(0, last_index - first_index + 1)
    eta = unified_centered_carry_bit(K, E)
    if count != K // E + eta:
        raise AssertionError("channel-state count disagrees with centered carry")

    if count == 0:
        x0 = None
        y0 = None
    else:
        x0 = residue + period * first_index
        if not (-K <= x0 <= K) or x0 % 2 == 0 or (M - x0) % E:
            raise AssertionError("failed to construct first parent-fiber point")
        y0 = (M - x0) // E
        if y0 % 2 == 0:
            raise AssertionError("parent quotient progression must be odd")

    return {
        "K": K,
        "k": K + 1,
        "center": M,
        "modulus": E,
        "fiber_size": count,
        "centered_carry": eta,
        "first_signed_point": x0,
        "first_quotient": y0,
        "quotient_step": -2,
    }


def refine_channel_state(
    fiber_size: int,
    first_quotient: int | None,
    refinement: int,
) -> dict[str, object]:
    """Apply one odd refinement R_d to a finite quotient progression."""
    if isinstance(fiber_size, bool) or not isinstance(fiber_size, int) or fiber_size < 0:
        raise ValueError("fiber_size must be a nonnegative integer")
    _require_positive_odd("refinement", refinement)
    d = refinement
    if fiber_size == 0:
        if first_quotient is not None:
            raise ValueError("empty fiber must use first_quotient=None")
        return {
            "parent_fiber_size": 0,
            "refinement": d,
            "channel_index": None,
            "remainder_length": 0,
            "channel_carry": 0,
            "child_fiber_size": 0,
            "child_first_quotient": None,
            "empty": True,
        }
    if isinstance(first_quotient, bool) or not isinstance(first_quotient, int):
        raise ValueError("nonempty fiber requires an integer first_quotient")
    if first_quotient % 2 == 0:
        raise ValueError("first_quotient must be odd")

    inverse_two = pow(2, -1, d)
    channel = (first_quotient * inverse_two) % d
    coarse, remainder = divmod(fiber_size, d)
    carry = int(channel < remainder)
    child_size = coarse + carry
    direct_size = max(0, 1 + (fiber_size - 1 - channel) // d) if channel < fiber_size else 0
    if child_size != direct_size:
        raise AssertionError("quotient-channel carry failed direct index count")

    if child_size == 0:
        child_first = None
    else:
        child_first = (first_quotient - 2 * channel) // d
        if child_first % 2 == 0:
            raise AssertionError("refined quotient progression must remain odd")

    return {
        "parent_fiber_size": fiber_size,
        "refinement": d,
        "channel_index": channel,
        "remainder_length": remainder,
        "channel_carry": carry,
        "child_fiber_size": child_size,
        "child_first_quotient": child_first,
        "empty": child_size == 0,
    }


def divisor_refinement_channel(K: int, parent_modulus: int, refinement: int) -> dict[str, object]:
    """Verify F_(Ed)=floor(F_E/d)+chi and the induced eta transport."""
    _require_positive_odd("parent_modulus", parent_modulus)
    _require_positive_odd("refinement", refinement)
    parent = signed_fiber_channel_state(K, parent_modulus)
    child = signed_fiber_channel_state(K, parent_modulus * refinement)
    refined = refine_channel_state(
        int(parent["fiber_size"]),
        None if parent["first_quotient"] is None else int(parent["first_quotient"]),
        refinement,
    )
    if int(refined["child_fiber_size"]) != int(child["fiber_size"]):
        raise AssertionError("channel refinement disagrees with direct child fiber")

    q_parent = K // parent_modulus
    parent_eta = int(parent["centered_carry"])
    overflow = int(parent_eta == 1 and q_parent % refinement == refinement - 1)
    child_eta = int(child["centered_carry"])
    if child_eta != overflow + int(refined["channel_carry"]):
        raise AssertionError("parent/child centered-carry transport identity failed")
    if overflow and int(refined["channel_carry"]):
        raise AssertionError("carry transport terms must be mutually exclusive")
    if parent_modulus > K and child_eta > parent_eta:
        raise AssertionError("high-product refinement created a carry below an empty parent")

    return {
        "K": K,
        "parent_modulus": parent_modulus,
        "child_modulus": parent_modulus * refinement,
        "refinement": refinement,
        "parent": parent,
        "refined_parent_state": refined,
        "direct_child": child,
        "parent_floor_quotient": q_parent,
        "parent_floor_overflow_bit": overflow,
        "child_centered_carry": child_eta,
        "child_carry_from_parent_transport": True,
        "high_product_carry_monotone": parent_modulus <= K or child_eta <= parent_eta,
    }


def verify_refinement_monoid(
    K: int,
    parent_modulus: int,
    first_refinement: int,
    second_refinement: int,
) -> dict[str, object]:
    """Verify R_d2 o R_d1 = R_(d1*d2) on one exact parent channel state."""
    _require_positive_odd("parent_modulus", parent_modulus)
    _require_positive_odd("first_refinement", first_refinement)
    _require_positive_odd("second_refinement", second_refinement)
    parent = signed_fiber_channel_state(K, parent_modulus)
    first = refine_channel_state(
        int(parent["fiber_size"]),
        None if parent["first_quotient"] is None else int(parent["first_quotient"]),
        first_refinement,
    )
    staged = refine_channel_state(
        int(first["child_fiber_size"]),
        None if first["child_first_quotient"] is None else int(first["child_first_quotient"]),
        second_refinement,
    )
    direct = refine_channel_state(
        int(parent["fiber_size"]),
        None if parent["first_quotient"] is None else int(parent["first_quotient"]),
        first_refinement * second_refinement,
    )
    if int(staged["child_fiber_size"]) != int(direct["child_fiber_size"]):
        raise AssertionError("refinement monoid lost child fiber size")
    if staged["child_first_quotient"] != direct["child_first_quotient"]:
        raise AssertionError("refinement monoid lost child quotient origin")

    child = signed_fiber_channel_state(
        K, parent_modulus * first_refinement * second_refinement
    )
    if int(direct["child_fiber_size"]) != int(child["fiber_size"]):
        raise AssertionError("direct product refinement disagrees with modulus product fiber")
    if direct["child_first_quotient"] != child["first_quotient"]:
        raise AssertionError("direct product refinement disagrees with child quotient origin")

    return {
        "K": K,
        "parent_modulus": parent_modulus,
        "first_refinement": first_refinement,
        "second_refinement": second_refinement,
        "product_refinement": first_refinement * second_refinement,
        "parent": parent,
        "first_stage": first,
        "staged_second": staged,
        "direct_product": direct,
        "direct_child": child,
        "refinement_monoid_identity": True,
    }
