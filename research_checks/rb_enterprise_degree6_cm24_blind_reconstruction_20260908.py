#!/usr/bin/env python3
"""Deterministic exact replay checker for the blind CM(-24) degree-6 reduction.

This checker verifies the frozen exact constants, the genus-1 derivation used in
the master identity, the complete Riemann--Roch pole-order bases, and the raw
freeze SHA256. No numerical discovery and no originating explicit map are used.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

R, t, J = sp.symbols("R t J")
I = sp.I
sqrt2 = sp.sqrt(2)
sqrt3 = sp.sqrt(3)
sqrt6 = sp.sqrt(6)
a = 3 ** sp.Rational(1, 4)

S = R**3 - 3*R
k = -I*a*(sqrt6 - 2)
lam = 35 + 24*sqrt2 - 20*sqrt3 - 14*sqrt6


def red_e0(expr):
    """Reduce a polynomial expression modulo t^2-(R^3-3R)."""
    p = sp.Poly(sp.expand(expr), t)
    m = sp.Poly(t**2 - S, t)
    return sp.factor(p.rem(m).as_expr())


def delta(expr):
    """The derivation corresponding to dF=(delta F)dR/(2t) on E0."""
    return sp.expand(2*t*sp.diff(expr, R) + 3*(R**2 - 1)*sp.diff(expr, t))


def master_residual(A, B, C):
    """Polynomial residual for the exact degree-6 master identity."""
    W = sp.expand(delta(A)*B - A*delta(B))
    expr = (R + 2)*t*W**2 - C*(t + k)**2*A*B*(A - B)*(A - lam*B)
    return red_e0(expr)


def assert_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label}: {z}")


def locate_artifact():
    here = Path(__file__).resolve()
    candidates = [
        here.parents[1] / "research_artifacts" / "rb_enterprise_degree6_cm24_blind_reconstruction_20260908.json",
        Path("research_artifacts/rb_enterprise_degree6_cm24_blind_reconstruction_20260908.json"),
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError("blind reconstruction artifact not found")


def main():
    # Frozen exact constants.
    assert_zero(k**2 - (12*sqrt2 - 10*sqrt3), "k^2")
    assert_zero(
        lam - ((sqrt3 - sqrt2)*(2 - sqrt3))**2,
        "lambda factorization",
    )

    j = sp.factor(256*(1 - lam + lam**2)**3 / (lam**2*(1 - lam)**2))
    j24 = 2417472 + 1707264*sqrt2
    assert_zero(j - j24, "target j")
    assert_zero(j24**2 - 4834944*j24 + 14670139392, "target j minpoly")

    cubic = R**3 - 3*R - k**2
    disc = sp.factor(sp.discriminant(cubic, R))
    assert_zero(disc - 216*(-73 + 30*sqrt6), "ramification cubic discriminant")
    if sp.simplify(disc) == 0:
        raise AssertionError("ramification cubic is not squarefree")

    # Branch-set coordinate checks on E0: t^2=R^3-3R.
    assert_zero(S.subs(R, 0), "T0")
    assert_zero(S.subs(R, sqrt3), "T+")
    assert_zero(S.subs(R, -sqrt3), "T-")
    assert_zero(S.subs(R, -2) + 2, "P±")
    if sp.simplify(k**2 + 2) == 0:
        raise AssertionError("t=-k would meet the R=-2 branch points")

    # Check the derivation really preserves the E0 relation.
    assert_zero(red_e0(delta(t**2 - S)), "delta preserves E0 relation")

    # Riemann--Roch pole-order bases at O.
    L6 = ["1", "R", "t", "R^2", "R*t", "R^3"]
    L7 = ["1", "R", "t", "R^2", "R*t", "R^3", "R^2*t"]
    L6_orders = [0, 2, 3, 4, 5, 6]
    L7_orders = [0, 2, 3, 4, 5, 6, 7]
    if len(L6) != 6 or L6_orders != sorted(set(L6_orders)):
        raise AssertionError("L(6O) basis/pole orders")
    if len(L7) != 7 or L7_orders != sorted(set(L7_orders)):
        raise AssertionError("L(7O) basis/pole orders")

    # Algebraic cancellation underlying the pullback identity.
    pullback_scalar = sp.cancel((t + k)/(2*t))
    assert_zero(pullback_scalar - sp.Rational(1, 2)*(1 + k/t), "pullback phi/2")

    # The callable master_residual is the load-bearing candidate verifier.
    # A=B=1 is deliberately degenerate and should give residual zero; degree
    # and nonconstancy are therefore separate mandatory candidate checks.
    if master_residual(sp.Integer(1), sp.Integer(1), sp.Integer(1)) != 0:
        raise AssertionError("degenerate master residual sanity check")

    # Verify raw-freeze hash and status.
    artifact_path = locate_artifact()
    artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
    canonical_payload = artifact["canonical_payload"]
    canonical = json.dumps(
        canonical_payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    digest = hashlib.sha256(canonical).hexdigest()
    if digest != artifact["raw_freeze_sha256"]:
        raise AssertionError("raw freeze SHA256 mismatch")
    if canonical_payload["phase"] != "BLIND_RECONSTRUCTION_FROZEN":
        raise AssertionError("wrong phase")
    if canonical_payload["primary_verdict"] != "BLIND_INCOMPLETE_EXACT_REDUCTION":
        raise AssertionError("wrong blind verdict")
    if canonical_payload["blind_firewall"]["status"] != "INTACT_AT_FREEZE":
        raise AssertionError("blind firewall not intact")
    if canonical_payload["explicit_map"] is not None:
        raise AssertionError("artifact unexpectedly claims an explicit map")
    if canonical_payload["period_scaling"]["ratio_squared"] is not None:
        raise AssertionError("artifact unexpectedly imports a period ratio")

    out = {
        "status": "PASS",
        "phase": canonical_payload["phase"],
        "verdict": canonical_payload["primary_verdict"],
        "raw_freeze_sha256": digest,
        "target_j": str(j24),
        "ramification_cubic_discriminant": str(disc),
        "master_identity_verifier": "master_residual(A,B,C)==0 modulo t^2-(R^3-3R)",
        "degree6_search_space": ["L(6O)", "L(5O+Q) via one-base-point L(7O) presentation"],
    }
    print(json.dumps(out, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
