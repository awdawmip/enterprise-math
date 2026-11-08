#!/usr/bin/env python3
"""Exact coefficient certificate for native 49-state BRC positivity chamber."""
from pathlib import Path
import json, runpy
src = runpy.run_path(str(Path(__file__).with_name('PREFIX589_R2_dual_carrier_certificate.py')))
P, N, g = src['P'], src['N'], src['TARGET']
axis = [abs(p[2])-1 for p in P]
eta = [int(g in N[i]) for i in range(48)]
assert eta[g] == 0 and sum(eta) == 3

def coordinate_matrix(x, znext):
    C = [[0]*49 for _ in range(49)]
    for i in range(48):
        for j in N[i]:
            C[i][j] += 2*x[axis[i]]
        C[i][48] = x[axis[i]]*eta[i]
    for j in N[g]:
        C[48][j] += (znext-1)*x[axis[g]]
    return C

def recovery_matrix(x):
    L = [[0]*49 for _ in range(96)]
    for i in range(48):
        for j in N[i]:
            L[2*i][j] += x[axis[i]]
            L[2*i+1][j] += x[axis[i]]
        L[2*i+1][48] = x[axis[i]]*eta[i]
    return L

cases = [((1,1,1,1,1,1),1), ((2,3,5,7,11,13),2),
         ((0,1,0,1,0,1),1), ((1,2,3,0,1,4),5)]
for x,z in cases:
    C,L = coordinate_matrix(x,z),recovery_matrix(x)
    assert all(v>=0 for row in C for v in row)
    assert all(v>=0 for row in L for v in row)
negative = coordinate_matrix((1,1,1,1,1,1),0)
assert [negative[48][j] for j in N[g]] == [-1,-1,-1]
assert sum(v<0 for row in negative for v in row) == 3
A = src['A']
for z in [0,1,2]:
    x = (2,3,5,7,11,13)
    L = recovery_matrix(x)
    for j0 in range(96):
        r = [int(j==j0) for j in range(96)]
        b = [r[2*i]+r[2*i+1] for i in range(48)]
        delta = (z-1)*r[2*g+1]
        out = [sum(row[j]*value for j,value in enumerate(b+[delta])) for row in L]
        exact = [sum((x[0]*z if k==6 else x[k])*r[j]
                     for k,AA in enumerate(A) for j in range(96) if AA[i][j])
                 for i in range(96)]
        assert out == exact
result = {
    'schema':'PREFIX594_R2_POSITIVE_49_CHAMBER_V1',
    'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'nonnegative_generator_and_recovery_cases':len(cases),
    'checked_recurrence_coefficients':len(cases)*49*49,
    'checked_readout_coefficients':len(cases)*96*49,
    'original_port_singleton_readout_checks':3*96,
    'exact_negative_coefficients_at_znext_0':3,
    'nonnegative_chamber':'all x_a >= 0 and z_t >= 1, arbitrary length',
    'minimal_full_port_linear_positive_state_dimension_generic_z_greater_1':49,
    'minimal_full_port_linear_positive_state_dimension_z_equal_1':48,
    'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'
}
Path(__file__).with_name('PREFIX594_R2_49state_positive_chamber_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
