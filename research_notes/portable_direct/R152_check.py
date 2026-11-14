#!/usr/bin/env python3
"""R152 exact coprime phase-increment observability and R152B finite horizon checks."""
from fractions import Fraction
from math import gcd, lcm
import json

def slopes(word):
    p = [0]
    for bit in word:
        p.append(p[-1] + bit)
    n = len(word)
    alpha, beta = Fraction(0), Fraction(1)
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            alpha = max(alpha, Fraction(p[j] - p[i] - 1, j - i))
            beta = min(beta, Fraction(p[j] - p[i] + 1, j - i))
    if alpha >= beta:
        return None
    a, b, c, d = alpha.numerator, alpha.denominator, beta.numerator, beta.denominator
    U = min(b * (p[j] + 1) - j * a for j in range(n + 1))
    V = max(d * p[j] - j * c for j in range(n + 1))
    return a, b, c, d, U, V

def ci(x, den):
    return -((-x) // den)

def count(L, a, b, c, d, U, V):
    return ci(c * L - V, d) - ((a * L - U) // b) - 1

def increments(a, b, c, d, U, V):
    P = lcm(b, d)
    return tuple(count(L + 1, a,b,c,d,U,V) - count(L,a,b,c,d,U,V)
                 for L in range(P))

def check_coprime():
    cases = waves = 0
    for b in range(2, 11):
        for d in range(2, 11):
            if gcd(b,d) != 1:
                continue
            for a in range(1,b):
                if gcd(a,b) != 1:
                    continue
                for c in range(1,d):
                    if gcd(c,d) != 1 or a*d >= b*c:
                        continue
                    seqs = set()
                    for U in range(b):
                        for V in range(d):
                            sig = increments(a,b,c,d,U,V)
                            assert sig not in seqs, (a,b,c,d,U,V)
                            seqs.add(sig)
                            waves += 1
                    assert len(seqs) == b*d
                    cases += 1
    return cases, waves

def check_words():
    row = []
    for m in range(1, 13):
        seen = missing_period = 0
        last_missing = largest_P = 0
        for x in range(1 << m):
            w = [(x >> (m-1-j)) & 1 for j in range(m)]
            z = slopes(w)
            if z is None:
                continue
            seen += 1
            a,b,c,d,U,V = z
            P = lcm(b,d)
            Q = P * Fraction(b*c-a*d,b*d)
            assert Q.denominator == 1 and Q >= 1
            largest_P = max(largest_P, P)
            for L in range(1, P+1):
                C = count(L,*z)
                assert C >= 0,(w,L,C)
                assert count(L+P,*z) == C + Q
                if C == 0:
                    missing_period += 1
                    last_missing = max(last_missing,L)
            for L in range(P+1,2*P+1):
                assert count(L,*z) >= 1
        row.append({'m':m,'words':seen,'last_missing_L':last_missing,
                    'T':last_missing+2,'max_period_P':largest_P,
                    'missing_in_first_period':missing_period})
    return row

def main():
    cases,waves = check_coprime()
    rows = check_words()
    assert next(z['T'] for z in rows if z['m']==4) == 4
    for z in rows:
        if z['m']>=5:
            m=z['m']
            assert z['T'] == (m-2)*((m-1)//2)+1,z
    result = {'result':'R152_COPRIME_INCREMENT_AND_FIRST_PERIOD_PASS',
              'coprime_slope_pairs':cases,
              'distinct_increment_waveforms':waves,
              'finite_word_rows':rows,
              'arithmetic':'Python unbounded integers and Fraction; exhaustive binary strings at length <=12'}
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
