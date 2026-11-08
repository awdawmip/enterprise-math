#!/usr/bin/env python3
"""Independent exact integer 96-port raw-moment DP, residual fourth."""
import json
from fractions import Fraction as F
from math import comb
from PREFIX579_R2_native_kernel import edge,ACTIONS
n=96; rows=[]
for i in range(n):
    row=[]
    for action in ACTIONS:
        j,w=edge(i,action)
        q=64*w[6]-(3*w[0]+w[1]+3*w[2]+w[3])
        row.append((j,q))
    assert len(row)==6
    rows.append(row)
moments=[[1]*n]+[[0]*n for _ in range(4)]
results=[]
for depth in range(129):
    if depth in (1,2,4,8,16,32,64,128):
        assert all(v==6**depth for v in moments[0])
        normalized=[F(sum(row),n*6**depth) for row in moments]
        m,m2,m3,m4=normalized[1:]
        k3=(m3-3*m2*m+2*m**3)/64**3
        k4=(m4-4*m3*m-3*m2*m2+12*m2*m*m-6*m**4)/64**4
        results.append({'depth':depth,'Y_kappa3_over_depth':'%.12f'%float(k3/depth),
          'Y_kappa4_over_depth':'%.12f'%float(k4/depth),
          'Y_kappa4_finite_exact':str(k4)})
    if depth==128:break
    new=[[0]*n for _ in range(5)]
    for i,row in enumerate(rows):
        for j,q in row:
            powers=[1,q,q*q,q**3,q**4]
            for k in range(5):
                new[k][i]+=sum(comb(k,ell)*powers[k-ell]*moments[ell][j] for ell in range(k+1))
    moments=new
assert results[-1]['Y_kappa4_over_depth']=='0.004024753049'
print(json.dumps({'status':'ALL_ASSERTIONS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'method':'all 96 original native ports exact integer DP degrees 0..4',
  'results':results},indent=2))
