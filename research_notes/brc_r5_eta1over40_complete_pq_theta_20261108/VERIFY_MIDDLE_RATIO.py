#!/usr/bin/env python3
"""Exact middle-ratio 1/30 two-face Blackwell certificates; stdlib only."""
from fractions import Fraction as F
from pathlib import Path
import json
from VERIFY import check, source, mass, time, ZERO

D=json.loads((Path(__file__).parent/'MIDDLE_RATIO_EXACT.json').read_text())
x=source(F(1,2),F(1,2),F(1,2),F(1,30))
assert list(map(str,x))==D['source']
assert list(map(str,mass(x)))==D['source_masses']
assert list(map(str,time(x)))==D['stop_times']
for face,z in D['target_face_certificates'].items():
    y=tuple(map(F,z['target']))
    Q=[[ZERO for _ in range(7)] for _ in range(7)]
    for i,j,s in z['edges']:
        Q[i][j]=F(s)
    check((x,y,tuple(map(tuple,Q))),face)
    print('EXACT_MIDDLE_FACE_PASS',face,'SPARSE_EDGES',len(z['edges']))
print('PASS_R5_MIDDLE_ETA_1_OVER_30_THETA_P_Q_HALF_TWO_FACES')
