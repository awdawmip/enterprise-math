#!/usr/bin/env python3
"""Exact integer-vector and optional native-output verifier for EC49FMN.

This checks the complete recorded 1,000-case vector against its immutable
digest, histogram, unique minimizers and optional full C++ native-output rows.
Scientific exhaustiveness also requires replaying the frozen lawful-word
generator and exact native-prefix solver described in README_EC49FMN.md.
"""
import argparse
import base64
import collections
import hashlib
import json
from pathlib import Path
import zlib

def sha(data):
    return hashlib.sha256(data).hexdigest()

def verify(vector_path, native_output=None, catalog=None):
    d = json.loads(Path(vector_path).read_text(encoding="utf-8"))
    assert d["schema"] == "EM_EC49FMN_RADIUS3_EXACT_VECTOR_V1"
    assert d["scientific_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    assert (d["first_index"], d["end_exclusive"], d["row_count"]) == (3700, 4700, 1000)
    costs = zlib.decompress(base64.b64decode(d["costs_b64"]))
    assert len(costs) == 1000 and sha(costs) == d["cost_sha256"]
    hist = dict(sorted((str(k), v) for k, v in collections.Counter(costs).items()))
    assert hist == d["histogram"]
    minimizers = [3700 + i for i, cost in enumerate(costs) if cost == min(costs)]
    assert (min(costs), max(costs), minimizers) == (116, 168, [4300, 4459, 4616])
    for index, expected in d["independent_checks"].items():
        assert costs[int(index) - 3700] == expected
    if native_output is not None:
        raw = Path(native_output).read_bytes()
        assert sha(raw) == d["raw_lines_sha256"]
        lines = raw.decode("utf-8").splitlines()
        assert len(lines) == 1000
        for j, line in enumerate(lines):
            fields = line.split()
            assert int(fields[0]) == 3700 + j and int(fields[1]) == costs[j]
    if catalog is not None:
        assert sha(Path(catalog).read_bytes()) == d["catalog_sha256"]
    print("PASS: 1000 exact recorded integer costs; min=116 at 4300,4459,4616; max=168")
    print("cost_vector_sha256:", d["cost_sha256"])
    if native_output is not None:
        print("PASS: all 1000 contiguous native-output rows and raw SHA-256")
    if catalog is not None:
        print("PASS: frozen catalog SHA-256")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("vector", nargs="?", default="EXACT_VECTOR_EC49FMN.json")
    p.add_argument("--native-output")
    p.add_argument("--catalog")
    a = p.parse_args()
    verify(a.vector, a.native_output, a.catalog)
