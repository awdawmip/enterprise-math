#!/usr/bin/env python3
"""Bounded exact audit of the original m=3 PP finite-HCM moment claim.

The cofactor is constructed as a polynomial and expanded by Leibniz, without
the legacy interpolation/q_coefficients route.  The legacy signed-secant route
is reused only as an independent input-model cross-check.  Standard library
only; no other m is run.  This is auxiliary evidence, not an official claim.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import permutations, product
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "research_checks/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_CHECK_20260903.py"
RETURN = ROOT / "research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md"


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] += c
    for i, c in enumerate(b):
        out[i] += c
    return out


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def scale(a, c):
    return [c * x for x in a]


def trim(a):
    out = list(a)
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def polynomial_determinant(a):
    """Leibniz over Q[t]; size five here, 120 bounded terms."""
    n = len(a)
    out = [F(0)]
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = [F((-1) ** inversions)]
        for i, j in enumerate(perm):
            term = mul(term, a[i][j])
        out = add(out, term)
    return trim(out)


def direct_m3_cofactor():
    # From the original AP model, with m=3, n=2, b=9 and w=(1,-2,1).
    # H_ij(t)=1/(i+1+3j)-2t/(i+1+3j+9)+t^2/(i+1+3j+18).
    w = (1, -2, 1)
    h = [[[F(w[s], i + 1 + 3 * j + 9 * s) for s in range(3)]
          for j in range(3)] for i in range(3)]
    lap = [[[F(0)] for _ in range(6)] for _ in range(6)]
    for i in range(3):
        for j in range(3):
            edge = scale(h[i][j], w[i] * w[j])
            lap[i][i] = add(lap[i][i], edge)
            lap[3 + j][3 + j] = add(lap[3 + j][3 + j], edge)
            lap[i][3 + j] = scale(edge, -1)
            lap[3 + j][i] = scale(edge, -1)
    tau = polynomial_determinant([row[:5] for row in lap[:5]])
    assert len(tau) == 9 and tau[:2] == [0, 0]
    q = tau[2:]
    assert len(q) == 7 and q[0] > 0
    return tau, q


def signed_difference(h, r, k):
    return sum(((-1) ** i * comb(k, i) * h[r + i] for i in range(k + 1)), F(0))


def rational_strings(xs):
    return [str(x) for x in xs]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    spec = importlib.util.spec_from_file_location("legacy_pp_coefficient_check", LEGACY)
    legacy = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(legacy)

    tau, q = direct_m3_cofactor()
    # This function enumerates the 126 five-element subsets of nine atoms;
    # it does not call q_coefficients or interpolate the cofactor.
    secant_q = legacy.cb_q_coefficients(3)
    assert q == secant_q
    d = 6
    h_raw = [(-1) ** a * q[a] / comb(d, a) for a in range(d + 1)]
    h = [x / h_raw[0] for x in h_raw]
    expected_h = [F(1), F(1445864051, 6614047440), F(50080057, 1027026000),
                  F(4900831, 513912000), F(12679829, 10737090000),
                  F(1597417, 33070237200), F(1, 4686825)]
    assert h == expected_h

    p = [F(-3, 10), F(8, 7), F(1)]
    p_squared = mul(p, p)
    square_value = sum((c * h[a] for a, c in enumerate(p_squared)), F(0))
    assert square_value == F(-7205915063, 2893645755000) < 0
    hankel = [[[h[i + j]] for j in range(3)] for i in range(3)]
    hankel_det = polynomial_determinant(hankel)[0]
    assert hankel_det < 0

    cells = {(r, k): signed_difference(h, r, k)
             for r in range(d + 1) for k in range(d + 1 - r)}
    assert len(cells) == 28 and all(value > 0 for value in cells.values())
    beta = [cells[j, d - j] for j in range(d + 1)]
    weights = [comb(d, j) * beta[j] for j in range(d + 1)]
    assert sum(weights) == h[0] == 1
    for a in range(d + 1):
        assert h[a] == sum((weights[j] * F(comb(j, a), comb(d, a))
                            for j in range(a, d + 1)), F(0))
    for (r, k), value in cells.items():
        assert value == sum((comb(d - r - k, j - r) * beta[j]
                             for j in range(r, d - k + 1)), F(0))

    # Explicit BRC on the 64 binary label words: each word has weight beta_|word|.
    # For every (r,k), independently sum words with the first r labels one and
    # the next k labels zero.  This confirms the actual finite branch readout.
    words = list(product((0, 1), repeat=d))
    for (r, k), value in cells.items():
        cylinder_mass = sum((beta[sum(word)] for word in words
                             if all(word[i] == 1 for i in range(r))
                             and all(word[i] == 0 for i in range(r, r + k))), F(0))
        assert cylinder_mass == value

    q_normalized = [x / q[0] for x in q]
    q_from_urn = [sum((weights[j] * (-1) ** a * comb(j, a)
                       for j in range(a, d + 1)), F(0)) for a in range(d + 1)]
    assert q_normalized == q_from_urn
    bhat_direct = [sum((q_normalized[a] * comb(d - a, k - a)
                       for a in range(k + 1)), F(0)) for k in range(d + 1)]
    bhat_urn = [sum((weights[j] * comb(d - j, k)
                    for j in range(d - k + 1)), F(0)) for k in range(d + 1)]
    assert bhat_direct == bhat_urn
    assert all(bhat_direct[k] == comb(d, k) * cells[0, k] > 0 for k in range(d + 1))

    return {
        "schema": "owner_pp_finite_moment_independent_audit_v1",
        "status": "PASS",
        "scope": "m=3 original model; finite-HCM repair identities; no all-m conclusion",
        "arithmetic": "Python standard-library fractions.Fraction; no floating point",
        "provenance": {
            "audit_source_sha256": sha(Path(__file__)),
            "legacy_check_path": LEGACY.relative_to(ROOT).as_posix(),
            "legacy_check_sha256": sha(LEGACY),
            "frozen_return_path": RETURN.relative_to(ROOT).as_posix(),
            "frozen_return_sha256": sha(RETURN),
            "global_knowledge_canonical": "4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563",
        },
        "model_binding": {
            "m": 3, "n": 2, "D": 5, "d": d,
            "route_1": "direct Q[t] 5x5 cofactor Leibniz expansion (120 permutations)",
            "route_2": "legacy cb_q_coefficients(3), 126 candidate signed-secant subsets",
            "routes_agree": True,
            "q_coefficients_interpolation_called": False,
            "tau_coefficients": rational_strings(tau),
            "q_coefficients": rational_strings(q),
            "normalizing_mass_q0": str(q[0]),
            "h_raw": rational_strings(h_raw),
            "h_normalized": rational_strings(h),
        },
        "positive_power_moment_obstruction": {
            "p_coefficients_ascending": rational_strings(p),
            "p_squared_coefficients_ascending": rational_strings(p_squared),
            "normalized_L_h_p_squared": str(square_value),
            "raw_L_h_p_squared": str(square_value * q[0]),
            "leading_3x3_hankel_determinant": str(hankel_det),
            "conclusion": "No positive Borel measure on R with these moments; in particular none on [0,1]",
        },
        "finite_branch_repair": {
            "all_28_finite_difference_cells_strictly_positive": True,
            "beta": rational_strings(beta),
            "count_weights_w": rational_strings(weights),
            "total_mass": str(sum(weights)),
            "binary_label_words": len(words),
            "cylinder_readouts_checked": len(cells),
            "normalization": "h=h_raw/q0; qbar=q/q0; Bhatbar=Bhat/q0; d is label length, not spatial dimension",
            "qbar_coefficients": rational_strings(q_normalized),
            "Bhatbar_coefficients": rational_strings(bhat_direct),
            "HCM0_identity_and_strict_positivity_preserved": True,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    encoded = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8", newline="\n")
        print(json.dumps({"status": payload["status"], "output": str(args.output),
                          "output_sha256": sha(args.output),
                          "negative_square": payload["positive_power_moment_obstruction"]["normalized_L_h_p_squared"]}))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
