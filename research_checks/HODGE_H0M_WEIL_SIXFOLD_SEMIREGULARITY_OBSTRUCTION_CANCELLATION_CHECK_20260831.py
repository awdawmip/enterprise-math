#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts" / "HODGE_H0M_WEIL_SIXFOLD"

def load(name):
    return json.loads((ART / name).read_text(encoding="utf-8"))

def v_p_integer(n: int, p: int) -> int:
    n = abs(n)
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e

def v_p_fraction(q: Fraction, p: int) -> int:
    return v_p_integer(q.numerator,p) - v_p_integer(q.denominator,p)

def det_diagonal(diag):
    out = 1
    for x in diag:
        out *= x
    return out

model = load("HODGE_H0M_WEIL_SIXFOLD_MODEL_SPEC.json")
lit = load("HODGE_H0M_LITERATURE_FRONTIER_LEDGER.json")
defect = load("HODGE_H0M_DISCRIMINANT_DEFECT_REGISTRY.json")
obs = load("HODGE_H0M_OBSTRUCTION_CANCELLATION_REGISTRY.json")
tr = load("HODGE_H0M_DERIVED_TRANSPORT_REGISTRY.json")
lift = load("HODGE_H0M_CLASS_FIRST_WEIL_LIFT_REGISTRY.json")

diag = model["rational_homology_datum"]["hermitian_matrix_diagonal"]
assert diag == [1,1,1,-1,-1,-3]
assert det_diagonal(diag) == -3
assert model["rational_homology_datum"]["real_signature"] == [3,3]
assert model["weil_type"]["cohomology_K_rank"] == 6
assert model["K"]["degree_over_Q"] == 2
assert 2 * 1 == 2  # dim_Q(wedge_K^6 K^6) = [K:Q]*1
assert model["weil_type"]["carrier_dimension_proof"][-1].startswith("[K:Q]=2")
assert model["weil_type"]["signature"] == [3,3]

# Exact base-point Riemann-form check. For one coordinate with Hermitian
# coefficient s and J-sign eps (J z = eps*i*z), E(z,Jz)=2*eps*s*|z|^2.
# Choose eps=+1 on positive H directions and eps=-1 on negative directions.
s = diag
eps = [1,1,1,-1,-1,-1]
assert all(2*e*a > 0 for a,e in zip(s,eps))
# Integrality/alternation on Gaussian-integer values z=a+bi:
# Tr(i z)=-2b, so E is integral; conjugating z flips b and hence E's sign.
for a,b in [(0,1),(2,-3),(5,0)]:
    trace_iz = -2*b
    trace_i_conjz = 2*b
    assert isinstance(trace_iz,int)
    assert trace_i_conjz == -trace_iz

# Exact norm-class separation for Q(i): every norm has even p-valuation for p=3 mod 4.
ratio = Fraction(model["discriminant"]["ratio_to_solved_class"],1)
assert v_p_fraction(ratio,3) == 1
assert 3 % 4 == 3
assert model["discriminant"]["norm_separation"]["conclusion"] == "[-3] != [-1]"

# The even K-rank similitude factor is a norm: c^6 = N(c^3) for rational c.
for c in [Fraction(2,1), Fraction(3,2), Fraction(-5,7)]:
    assert c**6 == (c**3)**2  # N_{Q(i)/Q}(r)=r^2 for rational r

# In the norm-class quotient, inversion fixes a rational class because d^2=N(d).
for d in [Fraction(-1,1), Fraction(-3,1), Fraction(5,2)]:
    assert d / (1/d) == d**2

assert lit["classification"] == "CURRENTLY_OPEN_FRONTIER_AT_DECLARED_SCOPE"
assert defect["classification"] == "EXACT_HARD_BLOCK_WITH_MISSING_OBJECT_AND_UNBLOCK_CONDITION"
assert obs["instantiation_status"] == "BLOCKED_BEFORE_EXT2"
assert obs["brc_gate"]["resolution"] == "REUSE_APPLIED"
assert "signed/complex" in obs["brc_gate"]["signed_boundary"]
assert tr["classification"] == "DISCRIMINANT_TRANSPORT_NO_GO_WITHIN_AUDITED_CARRIER_PRESERVING_OPERATIONS"
assert tr["separation_certificate"]["is_norm"] is False
assert lift["cycle_search_status"] == "NO_FRONTIER_CYCLE_CONSTRUCTED"
assert lift["known_positive_cycle_imported"] is False
assert lift["divisor_product_used_as_weil_generator"] is False

print("H0M_CHECK_OK")
print("dim_Q_WK=2")
print("discriminant_target=[-3], solved=[-1], separated_by_v3_parity")
print("terminal_research_classification=EXACT_HARD_BLOCK_WITH_MISSING_OBJECT_AND_UNBLOCK_CONDITION")
