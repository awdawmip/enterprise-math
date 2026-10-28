#!/usr/bin/env python3
"""PREFIX-314: exact four-state tagged BRC and generic gauge Jacobian check.

Auxiliary static S7-3 Gaussian-rational source register only. Every Q0/Q1/Qi
mass is calculated from all ordered labelled paths, including the reference.
No claim of native heartbeat Detector execution or formal Source admission.
"""
from fractions import Fraction as F
from itertools import combinations
import json

Z = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))

def g(x=0, y=0): return (F(x), F(y))
def add(a, b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[0], -a[1])
def sub(a, b): return add(a, neg(b))
def conj(a): return (a[0], -a[1])
def mul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def scale(a, t): return (a[0]*t, a[1]*t)
def abs2(a): return mul(a, conj(a))[0]
def sumg(seq):
    val = Z
    for z in seq: val = add(val, z)
    return val

def mult_state(a, b): return tuple(mul(z, b) for z in a)
def scale_state(a, b): return tuple(scale(z, b) for z in a)
def sub_state(a, b): return tuple(sub(a[k], b[k]) for k in range(3))
def square_distance(a, b): return sum(abs2(sub(a[k], b[k])) for k in range(3))
def real_inner(a, b):
    return sum(mul(a[k], conj(b[k]))[0] for k in range(3))
def show(x):
    if isinstance(x, tuple): return [show(v) for v in x]
    if isinstance(x, list): return [show(v) for v in x]
    if isinstance(x, dict): return {k: show(v) for k, v in x.items()}
    if isinstance(x, F): return str(x)
    return x

A = (
    (g(4), g(4), Z),
    (Z, g(-4), g(4)),
    (g(-5,3), Z, g(-3,1)),
    (g(-2,-2), g(4,4), g(2,2)),
    (g(-2), Z, g(5,2)),
)
U = tuple(tuple(scale(z, F(1,8)) for z in row) for row in A)
COUNTS = {'ordered_brc_mass_pairs': 0, 'mass_readings': 0,
          'ordered_jacobian_pairs': 0, 'jacobian_product_terms': 0,
          'gram_entries': 0}

def amplitude_paths(j, state, rho=None):
    paths = [(f'source:{k+1}', mul(U[j][k], state[k])) for k in range(3)]
    if rho is not None: paths.append(('reference', rho))
    assert len({label for label, _ in paths}) == len(paths)
    return paths

def mass(j, state, rho=None):
    paths = amplitude_paths(j, state, rho)
    total = Z
    for label_a, a in paths:
        for label_b, b in paths:
            total = add(total, mul(a, conj(b)))
            COUNTS['ordered_brc_mass_pairs'] += 1
    COUNTS['mass_readings'] += 1
    assert total[1] == 0 and total[0] >= 0
    return total[0]

def derivative_mass(j, state, direction):
    # Differentiates the source-tagged ordered-pair BRC polynomial in one real
    # coordinate direction. The reference is absent in baseline Q0.
    paths = amplitude_paths(j, state)
    derivatives = amplitude_paths(j, direction)
    total = Z
    for (label_a, a), (label_da, da) in zip(paths, derivatives):
        assert label_a == label_da
        for (label_b, b), (label_db, db) in zip(paths, derivatives):
            assert label_b == label_db
            total = add(total, add(mul(da, conj(b)), mul(a, conj(db))))
            COUNTS['ordered_jacobian_pairs'] += 1
            COUNTS['jacobian_product_terms'] += 2
    assert total[1] == 0
    return total[0]

def determinant(matrix):
    m = [list(map(F, row)) for row in matrix]
    n = len(m)
    assert all(len(row) == n for row in m)
    out = F(1)
    for col in range(n):
        row = next((r for r in range(col, n) if m[r][col]), None)
        if row is None: return F(0)
        if row != col:
            m[row], m[col] = m[col], m[row]
            out = -out
        pivot = m[col][col]
        out *= pivot
        for r in range(col+1, n):
            factor = m[r][col]/pivot
            for c in range(col+1, n):
                m[r][c] -= factor*m[col][c]
            m[r][col] = F(0)
    return out

# Verify previously pinned SOURCE Gram on the retained three labelled rows.
expected_gram = (
  (g(46),g(-16),Z), (g(-16),g(32),g(16)), (Z,g(16),g(47))
)
for k in range(3):
    for l in range(3):
        entry = sumg(mul(conj(row[k]),row[l]) for row in A[2:])
        assert entry == expected_gram[k][l]
        COUNTS['gram_entries'] += 1

# The four source states extend the PREFIX-313 baseline triple with i*b2,
# but the common noisy ten-reference report changes in two coordinates.
b0=(g(-2),g(0,-2),g(1))
b2=(g(0,2),g(2),g(0,-1))
B=(b0,mult_state(b0,I),b2,mult_state(b2,I))
T=tuple(scale_state(b,F(4,9)) for b in B)
EXPECTED_Q0=(F(32,81),F(20,81),F(37,162),F(50,81),F(85,324))
EXPECTED_REPORTS={
    'Q1':(F(113,81),F(83,81),F(217,162),F(185,81),F(535,324)),
    'Qi':(F(113,81),F(101,81),F(199,162),F(185,81),F(409,324)),
}
READINGS = []
for j in range(5):
    q0 = tuple(mass(j,state) for state in T)
    assert q0 == (EXPECTED_Q0[j],)*4
    datum = {'port': j, 'Q0': EXPECTED_Q0[j], 'references': {}}
    for label,rho in (('Q1',ONE),('Qi',I)):
        values = tuple(mass(j,state,rho) for state in T)
        lo,hi=min(values),max(values)
        observation=(lo+hi)/2
        assert hi-lo <= 2
        assert observation == EXPECTED_REPORTS[label][j]
        assert all(abs(observation-v)<=1 for v in values)
        datum['references'][label]={'values':values,'range':hi-lo,
                'common_observation':observation}
    READINGS.append(datum)

weights=(F(2,9),F(5,18),F(5,18),F(2,9))
assert sum(weights)==1 and all(t>0 for t in weights)
centre=tuple(sumg(scale(T[i][k],weights[i]) for i in range(4)) for k in range(3))
assert centre==(g(F(-32,81)),g(F(40,81)),g(F(16,81)))
radii=[square_distance(x,centre) for x in T]
assert radii==[F(976,729)]*4
pairwise={f'{i},{j}':square_distance(T[i],T[j]) for i,j in combinations(range(4),2)}
half_diameter=max(pairwise.values())/4
assert half_diameter==F(80,81) < F(16,13) < F(976,729) < F(1062562,458329)
diffs=[sub_state(T[k],T[0]) for k in range(1,4)]
affine_gram=[[real_inner(diffs[i],diffs[j]) for j in range(3)] for i in range(3)]
assert determinant(affine_gram)==F(1310720,59049)>0

# Polynomial gauge x=(Re a1,Re a2,Im a2,Re a3,Im a3), with Im a1=0.
# At a=(1,1,1+i), the nonzero exact Jacobian proves dominance and
# generically finite fibres. Each U(1) orbit with a1!=0 yields the two
# opposite gauge points ±x. Five quadratics give ≤2**5=32 complex points
# in any zero-dimensional fibre by affine Bezout, hence ≤16 such orbits.
sample=(g(1),g(1),g(1,1))
directions=(
    (ONE,Z,Z), (Z,ONE,Z), (Z,I,Z), (Z,Z,ONE), (Z,Z,I)
)
J=[[derivative_mass(j,sample,d) for d in directions] for j in range(5)]
J32=[[32*x for x in row] for row in J]
assert J32==[
 [F(32),F(32),F(0),F(0),F(0)],
 [F(0),F(0),F(-16),F(0),F(16)],
 [F(48),F(0),F(0),F(28),F(6)],
 [F(-16),F(32),F(16),F(16),F(8)],
 [F(-2),F(0),F(0),F(19),F(33)],
]
assert determinant(J)==F(-1287,2048)

# Full five-port Gram U*U is strictly positive definite (also visible by
# summing exact baseline masses), giving convex-position no-go for any
# common-Q0 states on one real affine segment.
D=[sum(abs2(U[j][k]) for j in range(5)) for k in range(3)]
assert D==[F(31,32),F(1),F(63,64)]
for k in range(3):
    for l in range(3):
        inner=sumg(mul(conj(U[j][k]),U[j][l]) for j in range(5))
        assert inner==(g(D[k]) if k==l else Z)

result={
 'schema':'PREFIX314_FOUR_CONTACT_BRC_AND_GENERIC_GAUGE_V1',
 'scope':'auxiliary S7-3 q=1 Q(i)^3, five exact Q0 and ten Q1/Qi with |error|<=1',
 'input_port_matrix':'PREFIX313 A/8 S7-3',
 'source_pins': {'PREFIX313_PROOF_BLOB':'2b46147df679f8702a72af6442d4ab577e1fe508',
                 'PREFIX313_CODE_BLOB':'6fb88ab539b0d8ae91b6ad1f7b2c9328a6fd4215',
                 'PREFIX313_RESULTS_BLOB':'1e708b461742b55e8bc3a75c387b6339cfdfd689'},
 'source_states':T,
 'common_baseline':EXPECTED_Q0,
 'common_references':EXPECTED_REPORTS,
 'all_brc_values':READINGS,
 'chebyshev_contact_weights':weights,
 'chebyshev_centre':centre,
 'chebyshev_r2':F(976,729),
 'pairwise_squared_distances':pairwise,
 'squared_half_diameter':half_diameter,
 'affine_gram_det':determinant(affine_gram),
 'generic_gauge_J32':J32,
 'generic_gauge_det':determinant(J),
 'generic_complex_gauge_root_bound':32,
 'generic_nonzero_first_source_phase_orbit_bound':16,
 'global_minimax_pair_lower_bound_unimproved':F(1062562,458329),
 'full_five_port_gram_diag':D,
 'direct_brc_counts':COUNTS,
 'native_result_or_driver_admission':False,
 'result':'PASS'
}
with open('RESULTS_PREFIX314.json','w',encoding='utf-8') as f:
    json.dump(show(result),f,ensure_ascii=False,indent=2)
    f.write('\n')
print(json.dumps(show({'result':'PASS','counts':COUNTS,'radius2':F(976,729),
                       'previous_triple_radius2':F(16,13),'pair_lower_L':F(1062562,458329),
                       'gauge_det':determinant(J)}),ensure_ascii=False))
