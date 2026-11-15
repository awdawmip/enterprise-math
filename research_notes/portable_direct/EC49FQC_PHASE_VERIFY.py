#!/usr/bin/env python3
"""Recheck the exact EC49FQC Bellman anchor and affine phase certificates.

Usage:
    python EC49FQC_PHASE_VERIFY.py /path/to/EC49FQC_SHARP_HIGH_PRICE_PHASE_CERT.json /path/to/full_certificates

The full certificates are generated from the frozen source by the already
published EC49FQA_PRICED_BELLMAN.py (PR #2515). This checks both priors and
all breakpoint equalities. Run EC49FQA_INDEPENDENT_REPLAY.py on full certs
to rederive and verify every query tree from original configurations.
"""
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

compact = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
directory = Path(sys.argv[2])
assert compact["schema"] == "EC49FQC_CLASS16943_GLOBAL_PRICED_PHASES_V1"
D = compact["domain"]
assert (D["original_configs"], D["named_root_profiles"], D["terminal_actions"],
        D["named_root_actions"], D["raw_actions"]) == (310, 141, 144, 84, 228)
PIN = compact["frozen_science_commit"]
MASTER = compact["source_master_sha256"]
CSV = compact["root_cost_csv_sha256"]
anchors = {}
for entry in compact["bellman_anchor_certificates"]:
    a, b = entry["r"], entry["t"]
    path = directory / f"EC49FQC_{a}_{b}.json"
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == entry["sha256"]
    cert = json.loads(data)
    assert cert["prices"] == {"root": a, "terminal": b}
    assert cert["frozen_scientific_commit"] == PIN
    assert cert["source_master_sha256"] == MASTER
    assert cert["native_root_costs_sha256"] == CSV
    assert cert["observation_scope"] == "all_228"
    assert (cert["profile_count"], cert["config_count"]) == (141, 310)
    assert (cert["optimal_total_uniform"], cert["optimal_total_config_weighted"]) == (entry["uniform"], entry["weighted"])
    for name, optimum in (("uniform", entry["uniform"]), ("config_weighted", entry["weighted"])):
        counts = cert["replay"][name]
        assert counts["weighted_root_observations"] * a + counts["weighted_terminal_observations"] * b == optimum
    anchors[(a, b)] = (entry["uniform"], entry["weighted"])
    print("BELL_MANCHOR", a, b, entry["uniform"], entry["weighted"])

witness = compact["extra_tree_witness"]
wa, wb = witness["r"], witness["t"]
witness_bytes = (directory / f"EC49FQC_{wa}_{wb}.json").read_bytes()
assert hashlib.sha256(witness_bytes).hexdigest() == witness["sha256"]
w = json.loads(witness_bytes)
assert (w["replay"]["uniform"]["weighted_root_observations"],
        w["replay"]["uniform"]["weighted_terminal_observations"]) == tuple(witness["uniform_aggregate_reads"])

witness_at = {
    "uniform": [(wa, wb), (153, 184), (1, 1), (3, 1)],
    "config_weighted": [(4, 5), (7, 8), (33, 35), (1, 1), (3, 1)],
}

def rational(x):
    return Fraction(10**20) if x == "infinity" else Fraction(x)

for index, kind in enumerate(("uniform", "config_weighted")):
    segments = compact["phase_functions"][kind]["segments"]
    for j, segment in enumerate(segments):
        lo = rational(segment["lower"])
        hi = rational(segment["upper"])
        R, T = segment["reads"]
        a, b = witness_at[kind][j]
        tree_cert = w if (a, b) == (wa, wb) else json.loads((directory / f"EC49FQC_{a}_{b}.json").read_text())
        replay = tree_cert["replay"][kind]
        assert (replay["weighted_root_observations"], replay["weighted_terminal_observations"]) == (R, T)
        if segment["upper"] != "infinity":
            for x in (lo, hi):
                ab = (x.numerator, x.denominator)
                assert ab in anchors
                assert R * ab[0] + T * ab[1] == anchors[ab][index]
            print("EXACT_FINITE_PHASE", kind, segment["lower"], segment["upper"], R, T)
        else:
            assert lo == 3 and R == 4
            assert R*3 + T == anchors[(3,1)][index]
            print("INFINITE_TAIL_AT_LEAST_FOUR_ROOT_READS", kind, R, T)

assert compact["terminal_equivalence"]["nontrivial_profile_pairs"] == [[17928,38165],[24541,38166]]
assert compact["terminal_equivalence"]["forced_root_reads_minimum"] == 4
print("EC49FQC_CERTIFICATE_ARITHMETIC_CHECK_PASS")
