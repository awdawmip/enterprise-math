#!/usr/bin/env python3
"""All-K s=1/8 integer-budget theorem: exact Fraction certificate reuse.
Runs the already published predecessor verifier, then checks NEW uniform
strict bounds. The all-K implication is analytic (see PROOF.md).
"""
from fractions import Fraction as F
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy

prior=(Path(__file__).resolve().parents[1] /
       'brc_n4_s23_s18_residue_endpoint_k31_100_20261104_research1' /
       'VERIFY.py')
with redirect_stdout(StringIO()):
    b=runpy.run_path(str(prior))
E, CB, CT, fb0 = (b[x] for x in ('E','CB','CT','fb0'))
sub=b['sub']
d=sub(CB,fb0)
assert E[0]>0
assert 53*E[1] < CB[0]/8
assert 32*E[0]-14*d[1]>F(2772,10**12)
# New ALL-BUDGET lower bound against every non-8-divisible T count.
non8=CB[0]/8-7*E[1]-14*d[1]
assert non8>14*E[0]>0
# New ALL-BUDGET lower bound of the 8L T + r B winner versus K pure B
# for L>=4 (K=15L+r, 0<=r<=14).
endpoint=32*E[0]-14*d[1]
assert endpoint>F(2772,10**12)
# Finite check is combinatorial only; the proof is for every integer K>=60.
checked=0
for K in range(60,201):
    L,r=divmod(K,15)
    assert 15*(8*L)+8*r==8*K and L>=4
    for m in range((8*K)//15+1):
        if m%8:
            n=(8*K-15*m)//8
            assert 8*(K-n)-15*m>=1
            assert m-8*L<=7
            checked+=1
        else:
            assert m<=8*L
print('PASS_BRC_S23_S18_ALL_POSITIVE_INTEGER_BUDGETS_20261104')
for label,z in [('CB',CB),('CT',CT),('E',E),('d',d)]:
    print(label,'lower=',format(float(z[0]),'.17e'),
          'upper=',format(float(z[1]),'.17e'))
print('uniform_non8_gap_lower=',format(float(non8),'.17e'))
print('L_ge_4_endpoint_gap_lower=',format(float(endpoint),'.17e'))
print('integer_sanity_cases=',checked,'K=60..200; all-K proof is symbolic')
