"""Bounded integer ideal-membership checks for the three remaining twists.

No square root, rational-function value or local parameter is evaluated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from research_artifacts.RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908 import check_squareclass_rr as p

REL = "research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908"
PINS = {
    "check_squareclass_rr.py": "32282b30357638b5f0a2b709a0c917b29711b43a4d7f407a113bfb6502ddf269",
    "squareclass_rr_certificate.json": "d861e5b4d9d5b562c7e2a972c56b30144f2cd41275963f80a3aa80c5f1d3a289",
    "empty_fiber_obstruction_certificate.json": "1757b252b5926bcda198e4a652259e8d46da4cd3a32464ae66c09f3d403eafb9",
}


def twisted_numerator(gamma, t, n, d, Dn, Dd):
    return p.add(p.multiply(t, n, d), p.multiply(gamma, p.add(p.multiply(Dn, d),
                                                           p.scale(p.multiply(n, Dd), -1))))


def checked_identities():
    # Independent formal variables; these aliases are local to this identity.
    zeta, Dzeta, n, d, Dn, Dd, R, t, k, s = (p.variable(i) for i in range(len(p.NAMES)))
    rows = []
    for label, gamma in (("T0", R), ("Tplus", p.add(R, p.scale(s, -1))), ("Tminus", p.add(R, s))):
        if p.twice_delta(gamma) != p.scale(t, 2):
            raise AssertionError("D(gamma)=2t failed")
        Dnumerator = p.add(p.multiply(Dzeta, n), p.multiply(zeta, Dn))
        left = p.multiply(gamma, p.add(p.multiply(Dnumerator, d),
                                     p.scale(p.multiply(zeta, n, Dd), -1)))
        W = twisted_numerator(gamma, t, n, d, Dn, Dd)
        right = p.multiply(zeta, W)
        difference = p.add(left, p.scale(right, -1))
        cover_relation = p.add(p.multiply(zeta, zeta), p.scale(gamma, -1))
        derivative_relation = p.add(p.multiply(zeta, Dzeta), p.scale(t, -1))
        witness = p.multiply(n, d, p.add(p.multiply(zeta, derivative_relation),
                                        p.scale(p.multiply(Dzeta, cover_relation), -1)))
        if difference != witness:
            raise AssertionError("cleared twisted derivative ideal-membership identity failed")

        # A distinct identity: a common frame factor rho scales W by rho^2.
        # The first two variables now denote rho, D(rho), without imposing cover relations.
        rho, Drho = zeta, Dzeta
        scaled_n, scaled_d = p.multiply(rho, n), p.multiply(rho, d)
        scaled_Dn = p.add(p.multiply(Drho, n), p.multiply(rho, Dn))
        scaled_Dd = p.add(p.multiply(Drho, d), p.multiply(rho, Dd))
        frame_left = twisted_numerator(gamma, t, scaled_n, scaled_d, scaled_Dn, scaled_Dd)
        if frame_left != p.multiply(rho, rho, W):
            raise AssertionError("common-frame covariance failed")

        one = p.constant(1)
        zero = {}
        honest = twisted_numerator(gamma, t, one, one, zero, zero)
        naive = p.multiply(gamma, p.add(p.multiply(zero, one), p.scale(p.multiply(one, zero), -1)))
        at_Q = p.restrict_to_critical_divisor(honest)
        if honest != t or naive or at_Q != p.scale(k, -1) or honest == naive:
            raise AssertionError("missing-connection-term counterexample failed")
        # A vanishing nonunit common factor would produce a spurious zero unless
        # the known square factor is removed in the local section frame.
        vanishing_factor = p.add(t, k)
        unframed_at_Q = p.restrict_to_critical_divisor(p.multiply(vanishing_factor, vanishing_factor, honest))
        if unframed_at_Q or not at_Q:
            raise AssertionError("nonunit common-frame counterexample failed")
        rows.append({"torsion_label": label,
                     "gamma": {"T0": "R", "Tplus": "R-s", "Tminus": "R+s"}[label],
                     "Dgamma_equals_2t": True,
                     "cleared_derivative_ideal_membership": True,
                     "common_frame_covariance": "W(rho*n,rho*d)=rho^2*W(n,d)",
                     "omitted_connection_term_counterexample": {"n": "1", "d": "1", "true_W": "t", "naive_W": "0", "true_W_at_Q": "-k != 0"},
                     "nonunit_frame_counterexample": {"rho": "t+k", "unframed_W_at_Q": "0", "regular_frame_W_at_Q": "-k != 0"},
                     "counterexample_scope": "Differential identity and frame guard only; g=zeta is not a degree-six task candidate."})
    return rows


def build_certificate(root):
    for name, expected in PINS.items():
        if hashlib.sha256(root.joinpath(REL, name).read_bytes()).hexdigest() != expected:
            raise ValueError("frozen dependency changed: " + name)
    residue = json.loads(root.joinpath(REL, "empty_fiber_obstruction_certificate.json").read_bytes())
    if residue["counts"] != {"excluded_4_plus_2": 180, "remaining_4_plus_2": 540,
                             "untouched_2_plus_2_plus_2": 1440, "remaining_total": 1980}:
        raise ValueError("unexpected prior residual boundary")
    return {"schema": "RB_BLIND_TWISTED_CRITICAL_NUMERATOR_V1",
            "phase": "BLIND_FORWARD_PROGRESS_NOT_FINAL_RAW_FREEZE",
            "dependencies": PINS,
            "scope": "Necessary critical-point conditions for the remaining nontrivial finite empty square classes of 4+2 only.",
            "derivation": "D=2*delta; D(R)=2t; D(t)=3R^2-3; D(s)=0",
            "critical_numerator": "W_T=t*n*d+gamma_T*((D n)*d-n*(D d))",
            "section_spaces": {"denominator": "L(2O+S), dimension 3", "numerator": "L(3O+S-T), dimension 3"},
            "cover": "Connected normalized unramified degree-two cover C_T: zeta^2=gamma_T; g=zeta*n/d has degree six for an exact degree-six X on C.",
            "formal_checks": checked_identities(),
            "local_gate": "At each of the three Q, first use regular numerator/denominator sections with no common zero; only their W_T=0 is the criticality test. Common nonunit factors must not be evaluated as extra critical zeros.",
            "critical_forms": "Three bilinear scalar equations in the 3 numerator and 3 denominator coefficients, on any regular RR basis chart; local exceptional charts still require exact treatment.",
            "unchanged_residual": residue["counts"],
            "new_components_excluded": 0,
            "not_claimed": ["solution of the bilinear or RR system", "new field descent", "full ODE from criticality alone", "map or period", "a condition for the 2+2+2 pattern", "raw freeze or unblinding"],
            "arithmetic": {"evaluated_divisions": 0, "evaluated_roots": 0, "brc_calls": 0,
                           "formal_integer_polynomial_checks_only": True}}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    result = build_certificate(args.root)
    data = p.encoded(result)
    output = args.root.joinpath(REL, "twisted_critical_certificate.json")
    if args.write:
        output.write_bytes(data)
    elif output.read_bytes() != data:
        raise SystemExit("TWISTED_CRITICAL: FAIL (certificate bytes differ)")
    print(json.dumps({"status": "PASS", "certificate_sha256": hashlib.sha256(data).hexdigest(),
                      "three_nontrivial_twists": len(result["formal_checks"]),
                      "derivative_and_frame_identities": 6,
                      "missing_term_and_nonunit_frame_counterexamples": 6,
                      "new_components_excluded": 0, "remaining_total": 1980}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
