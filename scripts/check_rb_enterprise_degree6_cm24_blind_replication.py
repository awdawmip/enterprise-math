#!/usr/bin/env python3
"""Exact arithmetic replay for the blind CM(-24) reduction certificate.

This checker deliberately verifies only the exact arithmetic identities used by
the Phase-A reduction. It does not claim to construct the missing degree-6 map.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "research_artifacts" / "RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION" / "raw_freeze_reduction.json"
EXPECTED_SHA256 = "5805be4031f73b0a5d92589326d7188fc129cde6d14be46861d7214d7690e2c1"


def exact_zero(expr: sp.Expr, label: str) -> None:
    got = sp.simplify(sp.radsimp(expr))
    if got != 0:
        raise AssertionError(f"{label}: expected 0, got {got!s}")


def main() -> None:
    obj = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    payload = obj["payload"]
    canonical = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    got_sha = hashlib.sha256(canonical).hexdigest()
    assert got_sha == EXPECTED_SHA256
    assert obj["payload_sha256"] == f"sha256:{EXPECTED_SHA256}"
    assert payload["phase"] == "BLIND_RECONSTRUCTION_FROZEN"
    assert payload["primary_verdict"] == "BLIND_INCOMPLETE_EXACT_REDUCTION"

    R = sp.symbols("R")
    sqrt2, sqrt3, sqrt6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
    a = sp.Pow(3, sp.Rational(1, 4))
    k = -sp.I * a * (sqrt6 - 2)
    k2_expected = 12 * sqrt2 - 10 * sqrt3
    exact_zero(k**2 - k2_expected, "k^2")

    lam = 35 + 24 * sqrt2 - 20 * sqrt3 - 14 * sqrt6
    ell = (2 - sqrt3) * (sqrt3 - sqrt2)
    exact_zero(lam - ell**2, "lambda square")

    j = 256 * (1 - lam + lam**2) ** 3 / (lam**2 * (1 - lam) ** 2)
    j_expected = 2417472 + 1707264 * sqrt2
    exact_zero(j - j_expected, "Legendre j")

    H24 = j_expected**2 - 4834944 * j_expected + 14670139392
    exact_zero(H24, "H_-24(j)")

    cubic = R**3 - 3 * R - k2_expected
    disc = sp.discriminant(cubic, R)
    disc_expected = 216 * (30 * sqrt6 - 73)
    exact_zero(disc - disc_expected, "Q-cubic discriminant")
    # Exact positivity: 30*sqrt(6) > 73 because both sides are positive and
    # (30*sqrt(6))^2 = 5400 > 5329 = 73^2.
    assert 5400 > 5329

    # The five finite branch points listed for D -> C lie on C:t^2=R^3-3R.
    branch_points = [
        (sp.Integer(0), sp.Integer(0)),
        (sqrt3, sp.Integer(0)),
        (-sqrt3, sp.Integer(0)),
        (-sp.Integer(2), sp.I * sqrt2),
        (-sp.Integer(2), -sp.I * sqrt2),
    ]
    for idx, (r, t) in enumerate(branch_points):
        exact_zero(t**2 - (r**3 - 3 * r), f"branch point {idx}")

    # t=-k is disjoint from finite branch support: k != 0 and k^2 != -2.
    assert sp.simplify(k2_expected) != 0
    assert sp.simplify(k2_expected + 2) != 0

    # Corrected Riemann-Hurwitz bookkeeping. If s of the three Q points
    # have special critical values, special fibers contribute 9+s and the
    # remaining non-special Q contribute 3-s. The total is always 12.
    for s in range(4):
        assert (9 + s) + (3 - s) == 2 * 6

    print("PASS: blind CM(-24) exact reduction arithmetic replay")
    print(f"artifact_sha256={EXPECTED_SHA256}")


if __name__ == "__main__":
    main()
