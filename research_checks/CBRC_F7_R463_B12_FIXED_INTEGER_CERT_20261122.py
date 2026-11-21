#!/usr/bin/env python3
"""Verify a frozen F7 B12 integer witness (standard library only).

Input: canonical sorted JSON triples [abs(a),b,increment].
The q definition is global; the objective check enumerates all 25**4 inputs.
"""
import argparse
import hashlib
import json
from itertools import product
from pathlib import Path

B = 12
DEN = 10**13
EXPECTED_SHA256 = "5026e4e8d9ccecd26806d95a096af4f41ff3c4507ea5ec7a43552e1a1edf68b6"
EXPECTED_COUNT = 2734
EXPECTED_MAX_ABS_NUMERATOR = DEN//2 + 1
EXPECTED_SATURATORS = 922

def verify(path):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == EXPECTED_SHA256, (digest, EXPECTED_SHA256)
    rows = json.loads(raw)
    assert len(rows) == EXPECTED_COUNT and rows == sorted(rows)
    values = {}
    for a,b,n in rows:
        assert isinstance(a,int) and isinstance(b,int) and isinstance(n,int)
        assert a >= 0 and b != 0 and n > 0
        assert (a,b) not in values and (a,b) not in ((2,1),(1,-1))
        values[a,b] = n

    def q(a,b):
        if a == b == 0: return 0
        if b == 0: return DEN
        key = (abs(a),b)
        if key in ((2,1),(1,-1)): return DEN//2
        return DEN//2 + values.get(key,0)

    maximum = 0
    count_max = 0
    checked = 0
    for a,b,c,d in product(range(-B,B+1),repeat=4):
        k = a-2*b-c+2*d
        delta = q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)
        mag = abs(delta)
        if mag > maximum:
            maximum = mag
            count_max = 1
        elif mag == maximum:
            count_max += 1
        checked += 1

    assert checked == 25**4
    assert maximum == EXPECTED_MAX_ABS_NUMERATOR, maximum
    assert count_max == EXPECTED_SATURATORS, count_max
    print(f"VERIFIED: {checked} inputs; {len(values)} overrides; "
          f"max|D|={maximum}/{DEN}; {count_max} maximizers")
    print("SHA256="+digest)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("witness_json")
    verify(parser.parse_args().witness_json)
