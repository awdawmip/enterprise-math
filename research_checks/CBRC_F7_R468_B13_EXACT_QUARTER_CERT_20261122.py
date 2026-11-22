#!/usr/bin/env python3
"""Independent exact B=13 F7 minimax witness checker (Python standard library)."""
import hashlib
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

M = 4
EXPECTED_SHA256 = 'f1a99c48a463d27c180010f034d6981e662a2502d6f4b6ea102c2a372caf8982'
EXPECTED_ROWS = 1026
EXPECTED_EQUALITY_COUNT = 36442

def check(path):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    rows = json.loads(raw)
    assert len(rows) == EXPECTED_ROWS
    assert rows == sorted(rows)
    assert all(len(row) == 3 for row in rows)
    assert all(type(x) is int and type(y) is int and type(n) is int
               and x >= 0 and y != 0 and n in (1, 2)
               and (x, y) not in ((2, 1), (1, -1)) for x, y, n in rows)
    increments = {(x, y): n for x, y, n in rows}
    assert len(increments) == EXPECTED_ROWS

    def mq(x, y):
        if x == 0 and y == 0:
            return 0
        if y == 0:
            return M
        return M // 2 + increments.get((abs(x), y), 0)

    assert mq(0, 0) == 0 and mq(2, 1) == mq(-1, -1) == M // 2
    assert mq(4, 0) == M and mq(-8, 5) == mq(8, 5)
    maximum = 0
    ties = 0
    distribution = Counter()
    for a, b, c, d in itertools.product(range(-13, 14), repeat=4):
        k = a - 2 * b - c + 2 * d
        numerator = mq(a+k, b+k) + mq(c-k, d-k) - mq(a, b) - mq(c, d)
        maximum = max(maximum, abs(numerator))
        distribution[numerator] += 1
        if abs(numerator) == M // 2:
            ties += 1
        assert abs(numerator) <= M // 2, (a, b, c, d, numerator)
    assert sum(distribution.values()) == 27**4 == 531441
    assert maximum == M // 2 and ties == EXPECTED_EQUALITY_COUNT
    assert distribution == Counter({-2: 25760, -1: 150438, 0: 252001, 1: 92560, 2: 10682})
    assert mq(4, 2) + mq(-3, -3) - mq(1, -1) >= M // 2
    print('CERTIFIED: E_B^* = 1/2 for all 1<=B<=13')
    print('inputs=531441 rows=1026 denominator=4 maximum_numerator=2 equality=36442')
    print('distribution:', sorted(distribution.items()))

if __name__ == '__main__':
    check(sys.argv[1])
