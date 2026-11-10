#!/usr/bin/env python3
"""Exact rational implication checker for PREFIX-687.

Frozen observer scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Depends on exact endpoint moment enclosures (PREFIX-685), and entire-I
first/second derivative bounds and root uniqueness (PREFIX-682/684).
No 189-level recurrence is rerun; this verifies the declared deductions.
"""
from fractions import Fraction as Q
from math import floor

SCIENCE_PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
S = 10**24
A0 = 803334881118283114227
B0 = 7930886194096894324395803
AL, AU = Q(A0,S),Q(A0+1,S)
BL, BU = Q(B0,S),Q(B0+1,S)
T = 10**12

def envelope(q):
    assert isinstance(q,int) and q>=9873
    fmin=q*AL-BU
    fmax=q*AU-BL
    assert fmin>0
    return fmin/(1800*q+150), fmax/(1600*q+100)

def proof():
    # The original PREFIX685 RESULTS JSON recorded ...356,
    # while the original source code and exact bracket prove ...357.
    lo, hi = B0*T//(A0+1), (B0+1)*T//A0
    assert lo==hi==9872453419496357
    assert B0*T>lo*(A0+1)
    assert (B0+1)*T<(lo+1)*A0
    # Uniform error: q>=q_c, delta=z_A-z(q), 0<delta<C/q.
    C = Q(794,100*1600)
    MA = 110000000
    K = (150*C+Q(MA,2)*C*C)/1600
    assert K==Q(8673259,10240000)
    assert 0<K<Q(847,1000)
    d73=envelope(9873)
    d74=envelope(9874)
    assert Q(247,10**13)<d73[0]<d73[1]<Q(278,10**13)
    assert Q(699,10**13)<d74[0]<d74[1]<Q(787,10**13)
    assert d73[1]<d74[0]
    assert (envelope(10000)[1] < Q(7,10**9))
    return {
      'result':'ALL_CHECKS_PASS PREFIX687-R6',
      'scientific_pin':SCIENCE_PIN,
      'correct_q_c_12digit_floor':lo,
      'prior_json_reported_floor':9872453419496356,
      'K_exact':str(K),
      'K_lt':str(Q(847,1000)),
      'q9873_delta_bounds':list(map(str,d73)),
      'q9874_delta_bounds':list(map(str,d74)),
      'q9874_window_is_right_of_q9873':True,
      'arithmetic':'Python Fraction exact implication checker; no 189-level recurrence rerun'
    }

if __name__=='__main__':
    import json
    print(json.dumps(proof(),indent=2,ensure_ascii=False))
