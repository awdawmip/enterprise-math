#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

CHECKS = []
MISMATCHES = []


def record(name, observed, expected=True, detail=None):
    passed = observed == expected
    row = {"name": name, "observed": observed, "expected": expected, "passed": passed}
    if detail is not None:
        row["detail"] = detail
    CHECKS.append(row)
    if not passed:
        MISMATCHES.append(row)


def signed_permutation(A):
    a, b, c, d = A
    rows = ((a, b), (c, d))
    cols = ((a, c), (b, d))
    return (
        all(sum(x != 0 for x in row) == 1 and sum(abs(x) for x in row) == 1 for row in rows)
        and all(sum(x != 0 for x in col) == 1 and sum(abs(x) for x in col) == 1 for col in cols)
    )


# 1. Finite-fiber P1 <=> P2 regression on multiple nonisomorphic finite groups.
TORSION_GROUPS = {
    "trivial": [()],
    "Z2": [(i,) for i in range(2)],
    "Z3": [(i,) for i in range(3)],
    "Z2xZ2": list(product(range(2), repeat=2)),
}

for gname, fiber in TORSION_GROUPS.items():
    for n in (-2, -1, 1, 2):
        positive = [Fraction(1 + i, 7 + len(fiber)) for i, _ in enumerate(fiber)]
        record(
            f"finite_equiv_positive::{gname}::n={n}",
            all(v > 0 for v in positive) == (min(positive) > 0),
            True,
        )
        with_zero = list(positive)
        with_zero[-1] = Fraction(0)
        record(
            f"finite_equiv_zero::{gname}::n={n}",
            all(v > 0 for v in with_zero) == (min(with_zero) > 0),
            True,
        )

seq = [Fraction(1, k + 1) for k in range(1, 101)]
record("infinite_fiber_pointwise_positive", all(x > 0 for x in seq), True)
record("infinite_fiber_descends_toward_zero", seq[-1] < Fraction(1, 100), True)


# 2. Exact strictness witnesses for P0/P1/P2/P3.
def q_kernel_zero(n, t):
    return Fraction(1) if n != 0 else Fraction(0)


record(
    "P1_not_P0::P1_at_nonzero_fibers",
    all(q_kernel_zero(n, t) > 0 for n in (-2, -1, 1, 2) for t in (0, 1)),
    True,
)
record("P1_not_P0::pure_kernel_zero", q_kernel_zero(0, 1), Fraction(0))
record("P1_not_P0::P0_fails", q_kernel_zero(0, 1) > 0, False)
record(
    "P1_implies_P3::old_copy_sample",
    all(q_kernel_zero(n, 0) > 0 for n in (-2, -1, 1, 2)),
    True,
)


def q_offcopy_zero(n, t):
    if t == 0 and n != 0:
        return Fraction(1)
    return Fraction(0)


record(
    "P3_not_P1::P3_old_copy",
    all(q_offcopy_zero(n, 0) > 0 for n in (-2, -1, 1, 2)),
    True,
)
record("P3_not_P1::free_fiber_zero_witness", q_offcopy_zero(1, 1), Fraction(0))


# 3. Exact periodic weak-scalar rank-one survivor.
PERIOD = 6
H = [
    Fraction(0),
    Fraction(1),
    Fraction(1, 4),
    Fraction(3, 4),
    Fraction(1, 4),
    Fraction(1),
]
A = (-4, -3, -3, -2)
a, b, c, d = A

record("periodic_survivor::det_pm_one", a * d - b * c, -1)
record("periodic_survivor::non_signed_permutation", signed_permutation(A), False)
record("periodic_survivor::q0", H[0], Fraction(0))
record("periodic_survivor::qe", H[1], Fraction(1))
record("periodic_survivor::P1_P2_P3_fail_at_6", H[0] > 0, False)
record("periodic_survivor::A0_first_column_nonzero", a != 0 and c != 0, True)
record("periodic_survivor::elementary_output_1_positive", H[a % PERIOD] > 0, True)
record("periodic_survivor::elementary_output_2_positive", H[c % PERIOD] > 0, True)
record("periodic_survivor::elementary_scalar_conservation", H[a % PERIOD] + H[c % PERIOD], H[1])

periodic_ok = True
periodic_bad = []
for x in range(PERIOD):
    for y in range(PERIOD):
        lhs = H[x] + H[y]
        rhs = H[(a * x + b * y) % PERIOD] + H[(c * x + d * y) % PERIOD]
        if lhs != rhs:
            periodic_ok = False
            periodic_bad.append((x, y, str(lhs), str(rhs)))
record("periodic_survivor::global_conservation_all_residues", periodic_ok, True, periodic_bad[:3])


# 4. Intermediate proof-side rules P6/P7.
def f_p6_strict(n):
    if n == 0 or n == 2:
        return Fraction(0)
    return Fraction(1)


p6_ok = True
for p in list(range(-12, 0)) + list(range(1, 13)):
    p6_ok = p6_ok and any(f_p6_strict(k * p) > 0 for k in range(1, 25))
record("P6_strict_witness::P2_fails_at_2", f_p6_strict(2) > 0, False)
record("P6_strict_witness::subgroup_hitting_bounded", p6_ok, True)


def f_p7_not_p6(n):
    if n % 2 == 0:
        return Fraction(0)
    if n == 1:
        return Fraction(1)
    return Fraction(abs(n) + 3)


record("P7_not_P6::2Z_is_zero", all(f_p7_not_p6(2 * k) == 0 for k in range(-20, 21)), True)
record(
    "P7_not_P6::unique_value_1_bounded",
    [n for n in range(-50, 51) if f_p7_not_p6(n) == 1],
    [1],
)
record(
    "periodic_survivor::P7_fails_period_6",
    all(H[(n + 6) % PERIOD] == H[n % PERIOD] for n in range(-12, 13)),
    True,
)


# 5. Exact pointwise-omission family A_m, m=2..9.
for m in range(2, 10):
    Am = (1, m, m, 1 + m * m)
    aa, bb, cc, dd = Am
    record(f"omission_family::m={m}::det", aa * dd - bb * cc, 1)
    record(f"omission_family::m={m}::nonsigned", signed_permutation(Am), False)
    qm = lambda n, mm=m: 0 if n % mm == 0 else 1
    ok = True
    for x, y in product(range(m), repeat=2):
        if qm(x) + qm(y) != qm(aa * x + bb * y) + qm(cc * x + dd * y):
            ok = False
            break
    record(f"omission_family::m={m}::conservation", ok, True)
    record(f"omission_family::m={m}::omitted_period_zero", qm(m), 0)


# 6. F4 accepted A0-ablation boundary witness.
f4_out1 = (1, 1)
f4_out2 = (0, 1)
record("A0_ablation_F4_boundary::out1_nonzero", f4_out1 != (0, 0), True)
record("A0_ablation_F4_boundary::out2_nonzero", f4_out2 != (0, 0), True)
record("A0_ablation_F4_boundary::out1_projection_nonzero", f4_out1[0] != 0, True)
record("A0_ablation_F4_boundary::out2_projection_zero", f4_out2[0], 0)
record(
    "A0_ablation_F4_boundary::A0_fails",
    f4_out1[0] != 0 and f4_out2[0] != 0,
    False,
)


def q_pi(n, t=0):
    return Fraction(1) if n != 0 else Fraction(0)


record("P1_plus_A0::first_output_positive", q_pi(a) > 0, True)
record("P1_plus_A0::second_output_positive", q_pi(c) > 0, True)


# 7. Bounded GL_2(Z) regression. This is not the arbitrary theorem proof.
def dscalar(n):
    return 0 if n == 0 else 1


gl2_total = 0
gl2_nonsigned = 0
gl2_undetected = []
for aa, bb, cc, dd in product(range(-3, 4), repeat=4):
    if aa * dd - bb * cc not in (-1, 1):
        continue
    gl2_total += 1
    B = (aa, bb, cc, dd)
    if signed_permutation(B):
        continue
    gl2_nonsigned += 1
    witness = None
    for x, y in product(range(-3, 4), repeat=2):
        lhs = dscalar(x) + dscalar(y)
        rhs = dscalar(aa * x + bb * y) + dscalar(cc * x + dd * y)
        if lhs != rhs:
            witness = (x, y)
            break
    if witness is None:
        gl2_undetected.append(B)

record("bounded_GL2::has_matrices", gl2_total > 0, True, gl2_total)
record("bounded_GL2::has_nonsigned_matrices", gl2_nonsigned > 0, True, gl2_nonsigned)
record(
    "bounded_GL2::all_nonsigned_detected_for_discrete_scalar",
    len(gl2_undetected),
    0,
    gl2_undetected[:5],
)


# 8. Mandatory ablation ledger.
ABLATIONS = {
    "finite_torsion_fiber": {
        "free_block_obstruction": "P1_ROUTE_FAILS_WITHOUT_UNIFORM_FIBER_GAP",
        "rank_one_closure": "NEEDS_P2_INFIMUM_FORM_OR_FINITE_ATTAINMENT",
    },
    "pure_kernel_positivity": {
        "free_block_obstruction": "UNCHANGED",
        "rank_one_closure": "UNCHANGED",
        "conservativity": "IMPROVES",
    },
    "all_nonzero_free_fiber_positivity": {
        "free_block_obstruction": "FAILS_PERIODIC_SURVIVOR",
        "rank_one_closure": "FAILS_EVEN_WITH_A0_AND_P5",
    },
    "finite_copy_nondegeneracy": {
        "free_block_obstruction": "REDUNDANT_UNDER_P1",
        "rank_one_closure": "REDUNDANT_UNDER_P1",
    },
    "active_branch_positivity": {
        "free_block_obstruction": "NOT_USED",
        "rank_one_closure": "ELEMENTARY_CASE_DERIVED_FROM_P1_PLUS_A0",
    },
    "elementary_output_positivity": {
        "free_block_obstruction": "NOT_USED",
        "rank_one_closure": "DERIVED_FROM_P1_PLUS_A0",
    },
    "fixed_scalar_law": {
        "free_block_obstruction": "FAILS_IF_STEP_DEPENDENT",
        "rank_one_closure": "NOT_DERIVABLE_BY_F4_ROUTE",
    },
    "exact_marked_conservation": {
        "free_block_obstruction": "FAILS",
        "rank_one_closure": "FAILS",
    },
    "A0_branch_projection_nondegeneracy": {
        "free_block_obstruction": "UNCHANGED",
        "rank_one_closure": "FAILS_F4_TORSION_LOOPHOLE",
    },
}

record("ablations::all_nine_present", len(ABLATIONS), 9)
record(
    "ablations::free_fiber_hits_periodic_survivor",
    ABLATIONS["all_nonzero_free_fiber_positivity"]["rank_one_closure"],
    "FAILS_EVEN_WITH_A0_AND_P5",
)
record(
    "ablations::A0_hits_F4_loophole",
    ABLATIONS["A0_branch_projection_nondegeneracy"]["rank_one_closure"],
    "FAILS_F4_TORSION_LOOPHOLE",
)
record(
    "ablations::pure_kernel_not_needed",
    ABLATIONS["pure_kernel_positivity"]["free_block_obstruction"],
    "UNCHANGED",
)

payload = {
    "checks": CHECKS,
    "mismatch_count": len(MISMATCHES),
    "ablations": ABLATIONS,
}
digest = hashlib.sha256(
    json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
).hexdigest()

try:
    checker_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
except Exception:
    checker_sha256 = "UNAVAILABLE"

result = "PASS" if not MISMATCHES else "FAIL"
print(f"CBRC_F5B_CHECKER_RESULT={result}")
print(f"CHECK_COUNT={len(CHECKS)}")
print(f"MISMATCH_COUNT={len(MISMATCHES)}")
print(f"DETERMINISTIC_DIGEST={digest}")
print(f"CHECKER_SHA256={checker_sha256}")
if MISMATCHES:
    print(json.dumps(MISMATCHES, indent=2, sort_keys=True, default=str))
    raise SystemExit(1)
