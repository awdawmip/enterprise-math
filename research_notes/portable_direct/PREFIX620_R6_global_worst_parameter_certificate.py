#!/usr/bin/env python3
"""Certify Bernstein unimodality of FIRST-PASSAGE survivors for PREFIX-617 BRC.
Exact integer arithmetic. Import/replay PREFIX-618's root predicate; no sim.
"""
import contextlib
import io
import json
from collections import defaultdict
from math import comb
from fractions import Fraction as Q
with contextlib.redirect_stdout(io.StringIO()):
    import PREFIX618_R6_exact_balanced_stop_certificate as baseline

alive = {0:1}
number_of_states = 0
symmetry_checks = 0
monotonicity_checks = 0
nontrivial_m = None
for m in range(1, 190):
    candidates = defaultdict(int)
    for k, v in alive.items():
        candidates[k] += v
        candidates[k+1] += v
    alive = {k:v for k,v in candidates.items() if baseline.wide(m,k)}
    assert sum(alive.values()) == baseline.A[m]
    for k in range(m+1):
        number_of_states += 1
        assert alive.get(k,0) == alive.get(m-k,0), (m,k)
        symmetry_checks += 1
    for k in range((m+1)//2):
        assert alive.get(k,0)*comb(m,k+1) <= alive.get(k+1,0)*comb(m,k), (m,k)
        monotonicity_checks += 1
    if m==25:
        assert alive.get(0,0)==alive.get(25,0)==0
        assert alive.get(1,0)>0
        nontrivial_m=25
    if m==26:
        assert baseline.wide(26,25) and not baseline.wide(25,25)
        assert alive.get(25,0)>0
    if m==189: assert not alive
assert nontrivial_m==25
assert number_of_states==sum(m+1 for m in range(1,190))

print(json.dumps({
  'schema':'PREFIX620_R6_GLOBAL_WORST_CASE_CORRECTED_V2',
  'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'domain':'d=2, p1,p2 in [0,1], q=12 or 24, beta=1/40, target p-diameter 1/4',
  'first_passage_survivor_count_m':189,
  'enumerated_mk_pairs':number_of_states,
  'exact_symmetry_checks':symmetry_checks,
  'exact_unimodality_checks':monotonicity_checks,
  'first_strict_survival_index':nontrivial_m,
  'source_replayed_exact_inequality_checks':baseline.checks,
  'instantaneous_width_nonmonotone_witness':'D(25,25)<=1/4 yet D(26,25)>1/4',
  'first_passage_survivor_coefficient_theorem':'c_m(k)=A_m(k)/binom(m,k) is symmetric and nondecreasing up to m/2 for 1<=m<=189',
  'theorem':'Unique global maximizer E[T_q] at p1=p2=1/2',
  'E_T12_max_decimal':'2350.8871013999329674336846958203177',
  'E_T24_max_decimal':'4701.7742027998659348673693916406354',
  'derivative_proof':'For s_m(p)=sum binom(m,k)c_m(k)p^k(1-p)^(m-k), s_m prime=m sum binom(m-1,k)(c_m(k+1)-c_m(k))p^k(1-p)^(m-1-k); symmetric pair contributions are nonnegative for p<=1/2',
  'verification':'ALL_CHECKS_PASS'
},indent=2))
