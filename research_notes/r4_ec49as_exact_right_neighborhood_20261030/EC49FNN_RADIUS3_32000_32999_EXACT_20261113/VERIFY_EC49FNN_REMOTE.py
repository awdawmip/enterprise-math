#!/usr/bin/env python3
"""Source-standalone verifier for EC49FNN compact finite data and original prefix witnesses.

This checks exact stored evidence/claimed summaries, not independent global DP
optimization of all 1000 cases. The frozen-input C++ and independent Python
solvers, complete original catalogue and full run logs are in the reproduction
bundle described in README_EC49FNN.md.
"""
from pathlib import Path
import base64
import collections
import hashlib
import json
import lzma

D = Path(__file__).resolve().parent
c = json.loads(lzma.decompress(base64.b64decode(
    (D / "EXACT_CERTIFICATE_EC49FNN.json.xz.b64").read_text().strip(),
    validate=True
)))
assert c["schema"] == "EC49FNN_RADIUS3_32000_32999_EXACT_V1"
assert c["scientific_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert c["interval"] == [32000, 32999]
v = c["cases"]
assert len(v["cost"]) == len(v["optimal_assignment_count"]) == len(
    v["second_distinct_assignment_cost"]) == len(v["root_count"]) == 1000
assert min(v["cost"]) == c["min_cost"] == 122
assert [i + 32000 for i, x in enumerate(v["cost"]) if x == 122] == [32970, 32997]
assert max(v["cost"]) == c["max_cost"] == 204
assert [i + 32000 for i, x in enumerate(v["cost"]) if x == 204] == [32813, 32936]
assert all(s > b for s, b in zip(v["second_distinct_assignment_cost"], v["cost"]))
h1 = collections.Counter(v["optimal_assignment_count"])
h2 = collections.Counter(s - b for s, b in zip(
    v["second_distinct_assignment_cost"], v["cost"]))
assert dict(h1) == {1: 421, 2: 466, 3: 62, 4: 29, 5: 6, 6: 2, 7: 2, 8: 10, 12: 2}
assert dict(h2) == {1: 703, 2: 156, 3: 86, 4: 9, 5: 19, 6: 11, 7: 16}

for i, expected in {32281: (134, 1, 140), 32551: (134, 5, 135),
                    32970: (122, 1, 123), 32997: (122, 1, 124)}.items():
    j = i - 32000
    assert (v["cost"][j], v["optimal_assignment_count"][j],
            v["second_distinct_assignment_cost"][j]) == expected
    witness = c["witnesses"][str(i)]
    assert witness["case_index"] == i
    assert witness["seven_key_indices"] == c["key_indices"][str(i)]
    assert witness["exact_optimal_cost"] == v["cost"][j]
    paths = [row["path_hex"] for root in witness["root_certificates"]
             for row in root["witnesses"]]
    rows = [row for root in witness["root_certificates"]
            for row in root["witnesses"]]
    assert len(rows) == 24
    labels = [tuple(row["label"]) for row in rows]
    assert len(set(labels)) == 24
    assert all(row["key"] and len(row["path_hex"]) > 0 for row in rows)
    assert all(len(row["key"]) == 3 for row in rows)
    assert all(p == p.lower() and all(x in "0123456789abcdef" for x in p)
               for path in paths for p in path)
    assert all(all(len(path[k+1]) == len(path[k]) + 2 and path[k+1].startswith(path[k])
                   for k in range(len(path)-1)) for path in paths)
    assert all(row["path_hex"][0] == root["root_hex"]
               for root in witness["root_certificates"] for row in root["witnesses"])
    assert len({p for path in paths for p in path}) == v["cost"][j]
    print("SAVED_ORIGINAL_PREFIX_WITNESS_PASS", i, len(rows), v["cost"][j])
assert set(c["witnesses"]) == {"32281", "32551", "32970", "32997"}
print("SAVED_CERTIFICATE_PASS", c["interval"], c["min_cost"], c["max_cost"])
print("INDEPENDENT_SCIENCE_SCOPE: four instances separately rerun with independent Python solver; see full evidence bundle")
