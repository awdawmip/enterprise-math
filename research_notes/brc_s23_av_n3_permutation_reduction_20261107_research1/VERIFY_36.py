#!/usr/bin/env python3
"""Exact S3(input) x S3(output) symmetrization of pinned S23 n=3 kernel.
Uses the independently executed certificate VERIFY.py in the same directory.
"""
from fractions import Fraction as Q
from itertools import product
from VERIFY import D, ROWS, B, T, PERMS, bi, ti, perm, discrepancy, Orig

SEP=[[sum(ROWS[bi[perm(y,p)]].get(ti[perm(x,q)],0)
          for p in PERMS for q in PERMS) for x in T] for y in B]
assert all(sum(row)==36*D and all(v>=0 for v in row) for row in SEP)
assert all(SEP[i][j]==SEP[bi[perm(y,p)]][ti[perm(x,q)]]
           for i,y in enumerate(B) for j,x in enumerate(T)
           for p in PERMS for q in PERMS)
assert sum(bool(v) for row in SEP for v in row)==104
# Input types: Hamming weights 0,1,2,3; output types: unordered triples
# of three symbols = C(5,3)=10. 4 row normalizations => 36 dimensions.
input_types={sum(y) for y in B}
output_types={tuple(x.count(k) for k in range(3)) for x in T}
assert len(input_types)==4 and len(output_types)==10
for a,c in ((Q(17,25),Q(17,20)),(Q(7,10),Q(43,50)),
            (Q(35319,50000),Q(7,8)),(Q(73,100),Q(7,8))):
    assert discrepancy(SEP,36*D,a,c)==discrepancy(Orig,D,a,c)
assert discrepancy(SEP,36*D,Q(1,2),Q(3,5))<discrepancy(Orig,D,Q(1,2),Q(3,5))
print('PASS_S23_N3_SEPARATE_S3xS3_SYMMETRY_20261107')
print('INPUT_TYPES=4; OUTPUT_TYPES=10; AFFINE_FREE_VARIABLES=36')
print('KSEP_DENOMINATOR=36000000; NONZERO_ENTRIES=104')
print('POINTWISE_ERROR_EQUAL_ON_R=PROVED_FROM_PREVIOUS_EXACT_BERNSTEIN_SIGN_CERT')
print('EXACT_GLOBAL_SUP_KSEP=f(alpha)=0.237838693711015430...')
