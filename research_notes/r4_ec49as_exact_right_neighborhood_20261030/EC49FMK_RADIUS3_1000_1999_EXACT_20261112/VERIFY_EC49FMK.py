#!/usr/bin/env python3
"""Verify EC49FMK packed exact vector and optionally complete raw C++ output.
Usage: python VERIFY_EC49FMK.py EXACT_VECTOR_EC49FMK.json [EXACT_NATIVE_OUTPUT_1000_1999.txt]
This validates published evidence; full mathematical replay uses scan_cached_radius3.cpp.
"""
import base64
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import sys

v = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
assert v['input_pin'] == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert v['case_catalog_sha256'] == 'cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
assert (v['index_start'], v['index_end_inclusive'], v['case_count']) == (1000, 1999, 1000)
values = list(base64.b64decode(v['u8_values_base64'], validate=True))
assert len(values) == 1000
assert min(values) == v['min_prefix_cost'] == 106
assert max(values) == v['max_prefix_cost'] == 138
assert [i+1000 for i, x in enumerate(values) if x == 106] == v['min_indices'] == [1724]
assert {str(k): n for k, n in sorted(Counter(values).items())} == v['histogram']
for idx, expected in v['independent_python_checks'].items():
    assert values[int(idx)-1000] == expected
assert v['prior_0_999_minimum'] == v['combined_0_1999_minimum'] == 102
if len(sys.argv) > 2:
    raw = Path(sys.argv[2]).read_bytes()
    assert sha256(raw).hexdigest() == v['raw_native_output_sha256']
    rows = raw.decode('utf-8').splitlines()
    assert len(rows) == 1000
    assert [(int(row.split()[0]), int(row.split()[1])) for row in rows] == list(enumerate(values, 1000))
    print('RAW_1000_CASES_SHA_AND_COST_PASS')
print('EC49FMK_VECTOR_PASS',len(values),min(values),max(values),'winner',v['min_indices'])
