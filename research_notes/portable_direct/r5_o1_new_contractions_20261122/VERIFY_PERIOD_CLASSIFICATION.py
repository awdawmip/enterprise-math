#!/usr/bin/env python3
"""Check exact finite-field witness coverage in VERIFY_R5_PHASE_SCAN.cpp output.
Run: ./scan 100 > scan_1_100.csv; python VERIFY_PERIOD_CLASSIFICATION.py scan_1_100.csv
CRT cancellation and order-16 zero-jet are separately certified in RESEARCH.md.
"""
import csv
import math
import sys

W = [7, 9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 32, 37, 43]
L = 229746052653717600

def expected_missing(m):
    if 54 <= m <= 58:
        return {29}
    if 60 <= m <= 64:
        return {32}
    if 80 <= m <= 86:
        return {43}
    return set()

def main(filename):
    rows = {}
    with open(filename, newline='', encoding='utf8') as src:
        for row in csv.DictReader(src):
            m, d = int(row['m']), int(row['d'])
            if 51 <= m <= 100:
                assert d in W and (m, d) not in rows
                rows[m, d] = row
    assert len(rows) == 50 * len(W)
    assert math.lcm(*W) == L
    counts = {}
    for m in range(51, 101):
        missing = {d for d in W if rows[m, d]['witness'] == '0'}
        assert missing == expected_missing(m), (m, missing)
        for d in W:
            row = rows[m, d]
            R0, DR0, pole = (int(row[x]) for x in ('R0', 'DR0', 'pole'))
            assert (row['witness'] == '1') == (R0 != 0 or (pole >= 4 and DR0 != 0))
        factor = 29 if missing == {29} else 2 if missing == {32} else 43 if missing == {43} else 1
        lower = math.lcm(*([d for d in W if d not in missing] + ([16] if factor == 2 else [])))
        assert lower == L // factor, (m, lower, factor)
        counts[factor] = counts.get(factor, 0) + 1
        print('PASS', m, 'factor', factor, 'lower', lower)
    assert counts == {1: 33, 29: 5, 2: 5, 43: 7}
    print('ALL CHECKS PASS', len(rows), 'finite-field witness pairs', counts)

if __name__ == '__main__':
    main(sys.argv[1])
