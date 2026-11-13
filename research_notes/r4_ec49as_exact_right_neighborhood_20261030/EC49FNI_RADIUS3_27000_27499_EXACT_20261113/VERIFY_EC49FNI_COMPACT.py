#!/usr/bin/env python3
"""Verify the compact EC49FNI finite vector and lawfully labeled witness metadata.

This checks serialization and finite report consistency; the full native BRC
operation-word/path and exact lower-bound checks require the frozen input and
the separate full-evidence archive.
"""
import base64
import hashlib
import json
import sys
import zlib
from collections import Counter
from pathlib import Path

def main(path):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    assert d["schema"] == "EC49FNI_BRC_EXACT_VECTOR_AND_WITNESS_V1"
    costs = json.loads(zlib.decompress(base64.b85decode(d["cost_vector_zlib_b85"])))
    assert len(costs) == d["vector_count"] == 500
    assert d["index_range_inclusive"] == [27000, 27499]
    assert all(type(c) is int and c > 0 for c in costs)
    encoded = json.dumps(costs, separators=(",", ":")).encode()
    assert hashlib.sha256(encoded).hexdigest() == d["cost_vector_decimal_sha256"]
    assert min(costs) == d["min_cost"] == 98
    assert [i + 27000 for i,c in enumerate(costs) if c == 98] == d["min_indices"]
    assert max(costs) == d["max_cost"] == 138
    assert costs.count(138) == d["max_count"] == 224
    assert d["first_max_index"] == 27188
    assert {str(i):costs[i-27000] for i in [27000,27086,27499]} == d["selected_crosschecks"]
    w = d["optimal_case_27086"]
    assert len(w["demanded_label_to_original_lawful_word"]) == w["lawful_witness_count"] == 24
    labels=[tuple(x[0]) for x in w["demanded_label_to_original_lawful_word"]]
    assert len(set(labels)) == 24
    assert all(isinstance(x[1],str) and x[1] for x in w["demanded_label_to_original_lawful_word"])
    assert w["signed_native_X6_distinct_nonempty_prefixes_by_first_microstep"] == {"05":49,"06":49,"07":0}
    assert w["total_distinct_nonempty_native_prefixes"] == 98
    shadows = d["exact_shadow_transfer"]
    for idx, base in [("26955",92),("26966",92),("27086",98)]:
        assert shadows[idx]["base"] == base
        assert shadows[idx]["strict_positive_gap"] == 8
        assert len(shadows[idx]["cardinality_envelope_by_k_1_to_8"]) == 8
    print("PASS: 500 lossless costs, 24 labeled original words, finite summaries")
    print("NOTE: native legality and 256-mask optimality require full evidence archive")

if __name__=="__main__":
    main(sys.argv[1] if len(sys.argv)>1 else str(Path(__file__).with_name("EXACT_DATA_EC49FNI.json")))
