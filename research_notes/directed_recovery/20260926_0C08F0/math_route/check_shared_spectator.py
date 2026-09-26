"""Exact source-local certificate for the spectator identities in the proof.

All executed gate columns come unchanged from stage78.native_quartet, which
executes the frozen actual BRC C12 and matched-companion primitives. No ideal
QFT, floating rotation or new phase input is constructed here.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import os
import sys

ROOT = Path(__file__).resolve().parent
DEFAULT = ROOT.parents[1] / "sep26-local-takeover" / "intake_brc" / "stage87-source"
SOURCE = Path(os.environ.get("BRC_STAGE87_SOURCE", str(DEFAULT))).resolve()
sys.path.insert(0, str(SOURCE))
from stage78.shor_benchmark import native_quartet
from stage45.brc_loop_recheck import CALLS, verify_vendor


def apply_h4(v, a, b, cols):
    out = [F(0)] * len(v)
    mask = (1 << a) | (1 << b)
    for old, weight in enumerate(v):
        src = ((old >> a) & 1) | (((old >> b) & 1) << 1)
        for coefficient, target in cols[src]:
            new = (old & ~mask) | ((target & 1) << a) | ((target >> 1) << b)
            out[new] += weight * F(coefficient, 2)
    return out


def z_project(v, bit, outcome):
    return [x if ((i >> bit) & 1) == outcome else F(0) for i, x in enumerate(v)]


def masses(v, bit):
    return [sum((x*x for i, x in enumerate(v) if ((i >> bit) & 1) == r), F(0))
            for r in (0, 1)]


def main():
    receipt = verify_vendor()
    cols = native_quartet()
    rows = []
    for source in range(8):
        v = [F(i == source) for i in range(8)]
        left = apply_h4(apply_h4(v, 1, 2, cols), 0, 2, cols)
        reversed_order = apply_h4(apply_h4(v, 0, 2, cols), 1, 2, cols)
        direct = apply_h4(v, 0, 1, cols)
        assert left == reversed_order == direct
        rows.append({"input_basis": source, "output_column": list(map(str, left))})

    initial = [F(i == 0) for i in range(4)]
    middle = apply_h4(initial, 0, 1, cols)
    without_record = apply_h4(middle, 0, 1, cols)
    recorded = [apply_h4(z_project(middle, 0, r), 0, 1, cols) for r in (0, 1)]
    law_without_record = masses(without_record, 0)
    law_with_record = [sum((masses(v, 0)[r] for v in recorded), F(0)) for r in (0, 1)]
    assert law_without_record == [F(1), F(0)]
    assert law_with_record == [F(1, 2), F(1, 2)]
    assert all(masses(v, 1)[1] == 0 for v in recorded)
    result = {
        "schema": "BRC_SHARED_SPECTATOR_STREAMING_IDENTITY_CERTIFICATE_V1",
        "status": "AUTHOR_EXECUTED_UNREVIEWED",
        "source_head": "0852cad130c1d877174d235687cf60c19f318c58",
        "activity_id": "RA-40F334CAC4876C16B82B0215",
        "scientific_route": "ACTUAL_TYPED_BRC_ONLY",
        "core_receipt": receipt,
        "entrypoint": "stage78.shor_benchmark.native_quartet",
        "gate_input": "all eight three-bit basis vectors; actual inherited H4 columns",
        "branch_identity": "two controls and one shared spectator, no record erased during gate execution",
        "observer_scope": "complete amplitude columns; separately declared terminal Z-record negative control",
        "allowed_future_operations": "fixed H4 words and declared terminal square observer",
        "operation_semantics": "exact serial/alternative signed-column extension of inherited BRC gate",
        "shared_spectator_identity_columns": rows,
        "identity_residual": "exact zero on all eight basis columns",
        "coherent_revisit_negative_control": {
            "no_inserted_Z_record_control_law": list(map(str, law_without_record)),
            "inserted_Z_record_control_law": list(map(str, law_with_record)),
            "spectator_one_mass_after_second_H4": "0"
        },
        "actual_BRC_kernel_calls": len(CALLS),
        "checks": {"full_columns": 8, "negative_control": 1},
        "not_claimed": ["independent review", "Born derivation", "all-Shor finite regression", "speedup"]
    }
    target = ROOT / "SHARED_SPECTATOR_CERTIFICATE.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"full_columns_passed": 8, "negative_control_passed": True,
                      "actual_BRC_kernel_calls": len(CALLS), "result": str(target)}))


if __name__ == "__main__":
    main()
