#!/usr/bin/env python3
"""EC49FSD independent all-228 original-family Bellman endpoint verification.
Run in extracted EC49FSA_FSB_FSC_COMPLETE_AND_PARTIAL_EVIDENCE directory.
Dependency EC49FSA_FSB_INDEPENDENT_CHECK.py decodes separately from the
original frozen 94-family source and implements independent finite integer DP.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from EC49FSA_FSB_INDEPENDENT_CHECK import certify

BASE = Path(__file__).resolve().parent
OUT = BASE / "ec49fsd_runs"
record = json.loads((OUT / "CERTIFICATE.json").read_text())
results = []
for item in record["endpoints"]:
    z = F(item["z"])
    got = certify({32: F(1, 2), 34: F(1, 2), 140: z})
    assert F(got["value"]) == F(item["global_optimum"]), (z, got, item)
    results.append({"z": str(z), "exact_value": got["value"],
                    "integer_value": got["integer_value"],
                    "denominator": got["denominator"],
                    "bellman_subsets": got["states"], "status": "MATCH"})
    print("PASS", str(z), got["value"], got["states"], flush=True)
(OUT / "INDEPENDENT_BELLMAN_ENDPOINTS.json").write_text(
    json.dumps({"status": "EXACT_FINITE_CROSSCHECKED",
                "method": "independent original 94-family source parsing, all 228 named observations",
                "results": results}, indent=2) + "\n")
print("SUCCESS", len(results), "independent exact endpoints", flush=True)
