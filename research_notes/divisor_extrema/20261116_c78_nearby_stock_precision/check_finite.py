"""Check the C78 transcript and compare its kernel with native three-state paths.

Usage: python3 check_finite.py [path/to/two_blocks]
With no argument a temporary C++17 binary is compiled.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, isqrt
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
P = 2**61 - 1
ROW = re.compile(r'c=(\d+) words=(\d+) duplicate_mod_single_h_fingerprint=(\d+) min_residue=(\d+) max_residue=(\d+)')


def is_prime_modulus():
    # Lucas-Lehmer criterion on the prime exponent 61.
    if any(61 % d == 0 for d in range(2, isqrt(61) + 1)):
        return False
    s = 4
    for _ in range(59):
        s = (s*s - 2) % P
    return s == 0


def native_tail_ratios(c, v, w):
    def consume(masses, stock, symbol):
        weights = []
        for rate, mass in zip((Q(1,4), Q(1), Q(4)), masses):
            den = stock[0] + stock[1] + rate*stock[2] + stock[3]
            weights.append(mass * stock[symbol] * (rate if symbol == 2 else 1) / den)
        stock[symbol] -= 1
        if symbol == 0:
            return [Q(0), weights[0], weights[1]+weights[2]]
        if symbol == 1:
            return [(7*sum(weights)+weights[0])/8, weights[1]/8, weights[2]/8]
        return weights

    body = [2]*(c-v) + [0,1] + [2]*(v-w) + [0,1] + [2]*(w-2)
    tails = ((2,2,3),(2,3,2),(3,2,2))
    rows = []
    for prep in (0, 1):
        state = [Q(7),Q(prep),Q(1-prep)]
        stock = [2,2,c,1]
        for symbol in body:
            state = consume(state,stock,symbol)
        vals = []
        for tail in tails:
            copy_stock, copy_state = stock.copy(), state.copy()
            for symbol in tail:
                copy_state = consume(copy_state,copy_stock,symbol)
            vals.append(sum(copy_state))
        assert sum(vals) == sum(state)
        rows.append(vals)
    return [b/a for a,b in zip(*rows)]


def check_rows(rows, stocks):
    assert len(rows) == len(stocks)
    for stock, row in zip(stocks, rows):
        match = ROW.fullmatch(row)
        assert match, row
        c, n, dup, low, high = map(int, match.groups())
        assert stock == c and n == comb(c,2) and dup == 0 and 0 <= low <= high < P
        yield c, n, low, high


def verify(binary):
    assert is_prime_modulus()
    stocks = list(range(3301,3401))
    all_rows = (HERE/'finite_c3301_3400.txt').read_text().splitlines()
    words = sum(n for _,n,_,_ in check_rows(all_rows,stocks))
    print('C78 scanned stocks',len(stocks),'new words',words)
    print('continuous new words',sum(comb(c,2) for c in range(3301,3401)))
    print('continuous total c=2..3400',comb(3401,3))

    count = 0
    small = list(range(2,19))
    control = subprocess.check_output([str(binary),str(small[0]),str(small[-1])],text=True)
    a, b = Q(P,3*P+1), Q(2*P+1,3*P+1)
    for c,n,lower,upper in check_rows(control.splitlines(),small):
        keys = set()
        for v in range(2,c+1):
            for w in range(2,v+1):
                vals = native_tail_ratios(c,v,w)
                lo, hi = min(vals), max(vals)
                g = hi/lo
                h = (1+b*(hi-1))*(1+a*(lo-1))/((1+a*(hi-1))*(1+b*(lo-1)))
                key, control_key = g+1/g,h+1/h
                residue = lambda x: x.numerator*pow(x.denominator,-1,P)%P
                assert residue(key) == residue(control_key)
                keys.add(residue(key))
        assert len(keys)==n and min(keys)==lower and max(keys)==upper
        count += n
    print('positive native three-state and rational-probe controls',count)


if __name__ == '__main__':
    if len(sys.argv)>1:
        verify(Path(sys.argv[1]).resolve())
    else:
        with tempfile.TemporaryDirectory() as tmp:
            binary = Path(tmp)/'two_blocks'
            subprocess.run(['c++','-O3','-std=c++17',str(HERE/'two_blocks.cpp'),'-o',str(binary)],check=True)
            verify(binary)
