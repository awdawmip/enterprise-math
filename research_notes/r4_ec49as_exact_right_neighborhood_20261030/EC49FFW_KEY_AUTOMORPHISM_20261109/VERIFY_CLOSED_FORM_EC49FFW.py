#!/usr/bin/env python3
"""Reproduce EC49FFW all-h BRC candidate formulas against independent exact DFA.
Execute from this directory: python VERIFY_CLOSED_FORM_EC49FFW.py
Word counts only: never interpret as signed X6 prefix-union optimization.
"""
from itertools import product
from math import factorial
from VERIFY_EC49FFW import T,S,forward

def coefficient(h,m,r=1):
    if h<r:return 0
    return sum(factorial(h)//(factorial(k)*factorial(k+r)*factorial(h-2*k-r))
               *m**(h-2*k-r) for k in range((h-r)//2+1))

def formulas(h):
    legal=coefficient(h,4)-coefficient(h,1)
    total_low=2*(coefficient(h,3)-coefficient(h,2))
    a14=2*coefficient(h-1,3)-coefficient(h-1,2)
    a28=total_low//2-a14
    return legal,{'1':a14,'2':a28,'4':a14,'8':a28},total_low

def exhaustive_dfa_word_check(maxh=7):
    tested=0
    for h in range(maxh+1):
        for ops in product(range(6),repeat=h):
            q=0
            for j in ops:q=T[q][j]
            c=ops.count(1);d=ops.count(2)
            assert (S[q] in (1,2,4,8)) == ((c>0)!=(d>0)),(ops,S[q])
            if (c>0)!=(d>0):
                first=ops[0]
                expected=(4 if first in (1,4) else 8) if c else (
                          1 if first in (2,5) else 2)
                assert S[q]==expected,(ops,S[q],expected)
            tested+=1
    return tested

def main():
    n=exhaustive_dfa_word_check()
    rows=forward(32)
    for h in range(1,33):
        legal,classes,low=formulas(h)
        r=rows[h-1]
        assert legal==r['legal_words'],(h,legal,r)
        assert classes==r['low_counts_by_signature'],(h,classes,r)
        assert low==r['low_candidate_words'],(h,low,r)
    assert formulas(11)[2]==15233900
    assert formulas(14)[2]==1801977660
    print('EC49FFW_EXACT_ALL_H_FORMULA_PASS: checked',n,'raw DFA words and H1..H32 transfer')
    for h in (2,9,10,11,14,20,32):
        print('H',h,formulas(h))
if __name__=='__main__':main()
