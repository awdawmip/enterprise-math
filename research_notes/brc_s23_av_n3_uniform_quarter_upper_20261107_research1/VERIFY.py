#!/usr/bin/env python3
"""Exact integer and rational continuum certificate for S23 3-trial kernel."""
import json
from fractions import Fraction
from itertools import product
from pathlib import Path

BASE=Path(__file__).parent
obj=json.loads((BASE/'KERNEL.json').read_text())
M=obj['denominator']
K=[[0]*27 for _ in range(8)]
for y,row in enumerate(obj['rows']):
    for xs,val in row.items():
        K[y][int(xs)]=val
    assert all(v>=0 for v in K[y]) and sum(K[y])==M

X=list(product(range(3),repeat=3))
Y=list(product(range(2),repeat=3))
CX=[tuple(x.count(i) for i in range(3)) for x in X]
CY=[y.count(0) for y in Y]
G=[[sum(K[y][x] for y in range(8) if CY[y]==j) for j in range(4)] for x in range(27)]

D=2048
DD=D*D
n_cells=256
max_num=-1
argmax=(-1,-1)
for i in range(n_cells+1):
    A=1024+3*i
    q1=A*D
    for j in range(n_cells+1):
        C=1024+3*j
        z=(D-A)*C
        q4=(D-A)*(D-C)
        p=[q1,z,q4]
        assert sum(p)==DD
        yes=[z**h*(DD-z)**(3-h) for h in range(4)]
        ptypes={c:p[0]**c[0]*p[1]**c[1]*p[2]**c[2] for c in set(CX)}
        total=0
        for x,c in enumerate(CX):
            rec=sum(G[x][h]*yes[h] for h in range(4))
            total+=abs(M*ptypes[c]-rec)
        if total>max_num:
            max_num=total
            argmax=(i,j)
        assert total*4096 < 2*M*D**6*(1024-27)

max_grid=Fraction(max_num,2*M*D**6)
lipschitz=Fraction(27,4096)
bound=max_grid+lipschitz
assert bound<Fraction(1,4)
assert bound<Fraction(49,200)
print('PASS_S23_N3_GLOBAL_KERNEL_EXACT_ALL_REAL_GRID_LIPSCHITZ_20261107')
print('kernel_rows=',len(K),'kernel_entries=',sum(bool(v) for row in K for v in row))
print('grid_points=',(n_cells+1)**2,'integer_probabilities_tested=',(n_cells+1)**2*27)
print('max_grid_at_i_j=',argmax)
print('max_grid_error_exact=',f'{max_grid.numerator}/{max_grid.denominator}')
print('max_grid_error_decimal=',float(max_grid))
print('extension_error_exact=',str(lipschitz),'=',float(lipschitz))
print('certified_global_error_upper_decimal=',float(bound))
print('strict_all_real_bound=delta_3 < 1/4 < 99/343')
print('frozen_science=43ec6098b1330ae86d0a7863be336c5d97f6ef34')
