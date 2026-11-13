#!/usr/bin/env python3
"""R131.3: exact eight-word rational certificate tests for primitive K>=3."""
from fractions import Fraction as F
from check_r131 import word

def witnesses(K):
    assert K >= 3
    return {
        '000': F(1, 2*K),
        '001': F(1, K+2),
        '010': F(1, K+1),
        '011': F(1) - F(2, 2*K-1),
        '100': F(1, K),
        '101': F(1) - F(1, K),
        '110': F(1) - F(1, K+1),
        '111': F(1) - F(1, K+2),
    }

def main():
    checked = 0
    for K in range(3, 1024):
        for expected, theta in witnesses(K).items():
            assert F(0) < theta < F(1)
            found = ''.join(map(str, word(F(0), K, 1, 1, 3, theta)))
            assert found == expected, (K, expected, theta, found)
            checked += 1
    print(f'R131_ALL_EIGHT_WITNESSES_PASS K=3..1023; cases={checked}')
if __name__ == '__main__': main()
