#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "research_artifacts/SEMIPRIME_SQUARE_SHELL_RESIDUAL_PRIORITY_PRIOR_ART_AUDIT/prior_art_ledger_20260829.json"

data = json.loads(LEDGER.read_text(encoding="utf-8"))

required_claims = {
    "C1_SHELL_MIDPOINT_EQUALS_FERMAT": "EXACT_DUPLICATE",
    "C2_QR_FILTER": "EXACT_DUPLICATE",
    "C3_MULTI_K_RESIDUAL_OBJECT": "EXACT_DUPLICATE",
    "C4_ASCENDING_MULTIPLIER_BASELINE": "EXACT_DUPLICATE",
    "C5_NORMALIZED_RESIDUAL_PRIORITY": "NO_MATERIAL_MATCH_IN_AUDITED_SET",
    "C6_ALTERNATIVE_K_SELECTORS": "ADJACENT_METHOD",
    "C7_OTHER_FERMAT_ACCELERATIONS": "ADJACENT_METHOD",
}
got = {x["claim_id"]: x["label"] for x in data["claim_classification"]}
assert got == required_claims, (got, required_claims)

source_ids = {x["id"] for x in data["sources"]}
for required in {
    "HART2012", "LEHMAN1974", "HITTMEIR2021",
    "HITTMEIR2023", "MCKEE1999", "FLINT2026",
    "OVERMARS_VENKATRAMAN2024"
}:
    assert required in source_ids, required

# Exact integer verification of the normalized next-square phase.
tested = 0
for N in range(3, 500):
    if N % 2 == 0:
        continue
    for k in range(1, 65):
        z = 4 * k * N
        r = math.isqrt(z)
        if r * r == z:
            continue
        x = r + 1
        e = x * x - z
        assert 0 < e < 2 * x - 1
        assert z == x * x - e
        tested += 1

assert tested > 10000
assert data["terminal_caveat"].startswith("NO_MATERIAL_MATCH_IN_AUDITED_SET")
print(f"PASS claims={len(got)} sources={len(source_ids)} phase_cases={tested}")
