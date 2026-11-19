#!/usr/bin/env python3
"""Unit150: exact signed three-axis reversal versus historical R061 observer spectrum.

Pinned base: X6 signed_brc.py at 59538f585d037d09ef687b28715c4bc1a3f9fe03.
This checker independently counts shortest signed step words via a recurrence.
It does not execute the historical R061 observer/canonical reverse decoder.
"""
import hashlib
import itertools
import json
from functools import lru_cache
from math import factorial

@lru_cache(None)
def paths_count(a, b, c):
    if (a, b, c) == (0, 0, 0):
        return 1
    return sum(paths_count(a-(i==0),b-(i==1),c-(i==2))
               for i in range(3) if (a,b,c)[i]>0)

def count_factorial(z):
    a,b,c = map(abs,z)
    return factorial(a+b+c)//(factorial(a)*factorial(b)*factorial(c))

def step_words(z):
    counts = [abs(x) for x in z]
    letters = [i+1 if x>0 else -(i+1) for i,x in enumerate(z)]
    def rec(prefix):
        if all(c==0 for c in counts):
            yield tuple(prefix);return
        for i in range(3):
            if counts[i]:
                counts[i]-=1;prefix.append(letters[i])
                yield from rec(prefix)
                prefix.pop();counts[i]+=1
    yield from rec([])

def rev_inv(word):
    return tuple(-x for x in reversed(word))

def run():
    triple_cases=0
    for z in itertools.product(range(-6,7),repeat=3):
        n=paths_count(*map(abs,z))
        assert n==count_factorial(z)==paths_count(*map(abs,(-z[0],-z[1],-z[2])))
        assert sum(x*x for x in z)==sum(x*x for x in (-z[0],-z[1],-z[2]))
        triple_cases+=1
    word_cases=0
    for z in itertools.product(range(-2,3),repeat=3):
        a=set(step_words(z));b=set(step_words(tuple(-x for x in z)))
        assert len(a)==count_factorial(z) and {rev_inv(w) for w in a}==b
        word_cases+=1
    d=(3,4,0)
    fwd=set(step_words(d)); backward=set(step_words(tuple(-x for x in d)))
    assert len(fwd)==len(backward)==35
    assert {rev_inv(w) for w in fwd}==backward
    assert sum(x*x for x in d)==25
    result={
      'schema':'X6_UNIT150_SIGNED_R061_REVERSAL_SOURCE_AUDIT_CERT_V1',
      'input_pin':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
      'historical_pin':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
      'historical_R061_observer_counts_source_claim':{'forward':35,'canonical_reverse':5,'sum':40,'not_native':True},
      'native_signed_3_4_0':{'native_norm_squared':25,'forward_shortest_words':35,'reverse_shortest_words':35,'orientation_tagged_union':70},
      'bounded_recurrence_factorial_cases':triple_cases,
      'bounded_explicit_word_reversal_cases':word_cases,
      'first_nonzero_primitive':{'z':[1,0,0],'forward':1,'reverse':1},
      'historical_R061_original_program_executed':False,
      'original_R063_benchmark_executed':False,
      'review':'UNREVIEWED / NOT_ADMITTED'
    }
    return result

if __name__=='__main__':
    data=run()
    output=json.dumps(data,sort_keys=True,ensure_ascii=False,separators=(',',':'))
    print(output)
