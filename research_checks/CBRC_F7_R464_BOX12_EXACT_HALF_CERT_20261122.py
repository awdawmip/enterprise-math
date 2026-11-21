#!/usr/bin/env python3
"""Exact F7 B12 finite minimax certificate checker (stdlib only)."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

B = 12
DEN = 30000000000000
TABLE_SHA256 = "340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5"

def check(path):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == TABLE_SHA256, f"Unexpected witness digest {digest}"
    rows = json.loads(raw)
    assert len(rows) == 2813 and rows == sorted(rows)
    increments = {}
    for a, b, n in rows:
        assert all(type(v) is int for v in (a,b,n))
        assert a >= 0 and b != 0 and n > 0
        assert (a,b) not in ((2,1),(1,-1))
        assert (a,b) not in increments
        increments[a,b] = n
    def q(a,b):
        if a == b == 0:
            return 0
        if b == 0:
            return DEN
        key = (abs(a),b)
        if key in ((2,1),(1,-1)):
            return DEN//2
        return DEN//2 + increments.get(key,0)
    maximum = 0
    saturators = 0
    checked = 0
    for a,b,c,d in itertools.product(range(-B,B+1),repeat=4):
        k = a-2*b-c+2*d
        delta = q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)
        magnitude = abs(delta)
        assert magnitude <= DEN//2, (a,b,c,d,magnitude)
        if magnitude > maximum:
            maximum, saturators = magnitude, 1
        elif magnitude == maximum:
            saturators += 1
        checked += 1
    assert checked == 390625
    assert maximum == DEN//2 and saturators == 514
    assert q(4,2)+q(-3,-3)-q(1,-1)==DEN//2
    print(f"VERIFIED E*_12=1/2 inputs={checked} rows={len(increments)} saturated={saturators}")
    print(f"SHA256={digest}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("witness_json")
    check(parser.parse_args().witness_json)
