#!/usr/bin/env python3
"""Exact upper occupancy for S23/AV horizons h=298,377,456.
Floats only choose tentative ordering/cells; every order and saved witness is
verified by integer cross-products. Parent lower bounds come from PROOF.md.
"""
from bisect import bisect_left
from math import log

L7, L10 = log(7), log(10)
for m in (2, 3, 4):
    h = 140 + 79*m
    bound = 880 + 431*m
    threshold = [(i*L10-s*L7, i, s) for s in range(h+1) for i in range(s+1)]
    threshold.sort(key=lambda row:row[0])
    M = len(threshold)
    p7, p10 = [1], [1]
    for _ in range(bound+h+2):
        p7.append(p7[-1]*7)
        p10.append(p10[-1]*10)
    for j in range(M-1):
        _, i, s = threshold[j]
        _, ip, sp = threshold[j+1]
        assert p10[i]*p7[sp] < p10[ip]*p7[s]
    logs = [row[0] for row in threshold]
    witnessed = bytearray(M+1)
    covered = 0
    for n in range(1, bound+1):
        for k in range(n+1):
            j = bisect_left(logs, n*L7-k*L10)
            if witnessed[j]:
                continue
            while j>0 and p7[n+threshold[j-1][2]] <= p10[k+threshold[j-1][1]]:
                j -= 1
            while j<M and p7[n+threshold[j][2]] >= p10[k+threshold[j][1]]:
                j += 1
            if witnessed[j]:
                continue
            assert j == 0 or p7[n+threshold[j-1][2]] > p10[k+threshold[j-1][1]]
            assert j == M or p7[n+threshold[j][2]] < p10[k+threshold[j][1]]
            witnessed[j] = 1
            covered += 1
        if covered == M+1:
            break
    assert covered == M+1 and n == bound, (m, covered, M+1, n, bound)
    print(f'PASS EXACT N({h})={n}; open_cells={M+1}; every cell has an integer-checked prefix witness')
print('PASS_S23_AV_N298_N377_N456_EXACT_UPPER_AND_PARENT_LOWER_20261108')
