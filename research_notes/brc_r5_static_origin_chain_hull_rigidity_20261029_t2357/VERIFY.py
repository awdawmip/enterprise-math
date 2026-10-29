"""Exact Fractions: static-origin absorbing stop-chain convex-image rigidity."""
from fractions import Fraction as F
from itertools import product, permutations

ZERO, ONE = F(0), F(1)
S = ('A', 'B', 'C')
P = {'A': F(1,8), 'B': F(1,8), 'C': F(3,4)}
Q = {'A': F(1,4), 'B': F(1,4), 'C': F(1,2)}
P_ERR = {
    'A': (F(1,5), F(3,10), F(1,5)),
    'B': (F(1,4), F(7,20), F(1,4)),
    'C': (F(1,4), F(1,4), F(1,2)),
}
Q_ERR = {
    'A': (F(1,5), F(1,5), F(3,10)),
    'B': (F(1,4), F(1,4), F(7,20)),
    'C': (F(1,4), F(1,2), F(1,4)),
}
GROUPS = {'A':'AB', 'B':'AB', 'C':'C'}


def observe(d, P0=P, Q0=Q, p0=P_ERR, q0=Q_ERR):
    assert all(sum(d[s]) == ONE and all(x >= ZERO for x in d[s]) for s in d)
    return (
        sum((P0[s] * d[s][j] * p0[s][j] for s in d for j in range(len(d[s]))), ZERO),
        sum((Q0[s] * d[s][j] * q0[s][j] for s in d for j in range(len(d[s]))), ZERO),
        sum((P0[s] * d[s][j] * (j+1) for s in d for j in range(len(d[s]))), ZERO),
        sum((Q0[s] * d[s][j] * (j+1) for s in d for j in range(len(d[s]))), ZERO),
    )


def aggregate(d, P0=P, Q0=Q, classes=GROUPS):
    ans = {}
    for g in set(classes.values()):
        members = [s for s in d if classes[s] == g]
        weight = sum((Q0[s] for s in members), ZERO)
        for s in members:
            assert P0[s] * Q0[members[0]] == P0[members[0]] * Q0[s]
        flow = tuple(sum((Q0[s]*d[s][j] for s in members), ZERO)/weight
                     for j in range(len(d[members[0]])))
        for s in members:
            ans[s] = flow
    return ans


def hazards(row):
    survival = ONE
    out = []
    for probability in row[:-1]:
        a = probability / survival if survival else ZERO
        assert ZERO <= a <= ONE
        out.append(a)
        survival -= probability
    assert survival == row[-1]
    out.append(ONE if survival else ZERO)
    return tuple(out)


def deterministic(names, m, indices):
    return {s:tuple(ONE if j == indices[i] else ZERO for j in range(m))
            for i,s in enumerate(names)}


def det4(rows):
    total = ZERO
    for perm in permutations(range(4)):
        sign = -ONE if sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4)) % 2 else ONE
        term = sign
        for i, j in enumerate(perm):
            term *= rows[i][j]
        total += term
    return total


def run():
    assert sum(P.values()) == sum(Q.values()) == ONE
    assert all(P[s] > 0 and Q[s] > 0 for s in S)
    assert all(ZERO < x < ONE for d in (P_ERR,Q_ERR) for r in d.values() for x in r)
    assert P['A']/Q['A'] == P['B']/Q['B'] == F(1,2)
    assert P['C']/Q['C'] == F(3,2)
    assert all(P_ERR['B'][j]-P_ERR['A'][j] == F(1,20) for j in range(3))
    assert all(Q_ERR['B'][j]-Q_ERR['A'][j] == F(1,20) for j in range(3))
    initial = deterministic(S,3,(0,0,0))
    origin = observe(initial)
    directions = []
    for group, target in (('AB',1),('AB',2),('C',1),('C',2)):
        decision = {s:tuple(ONE if j == (target if GROUPS[s]==group else 0) else ZERO for j in range(3)) for s in S}
        vec = observe(decision)
        directions.append(tuple(vec[i]-origin[i] for i in range(4)))
    determinant = det4(tuple(tuple(directions[j][i] for j in range(4)) for i in range(4)))
    assert determinant == F(1,1280)

    full = {'A':(F(1,3),F(1,2),F(1,6)),
            'B':(F(1,5),F(2,5),F(2,5)),
            'C':(F(1,6),F(1,3),F(1,2))}
    lr = aggregate(full)
    assert lr['A'] == lr['B'] == (F(4,15),F(9,20),F(17,60))
    assert tuple(hazards(lr['A'])) == (F(4,15),F(27,44),ONE)
    assert tuple(hazards(lr['C'])) == (F(1,6),F(2,5),ONE)
    output = observe(full)
    assert output == observe(lr) == (F(279,800),F(22,75),F(541,240),F(87,40))

    cases = 0
    distribution_basis = [(F(a,6),F(b,6),F(6-a-b,6))
                          for a in range(7) for b in range(7-a)]
    # Exhaust exact 28^3=21952 independent full source-stop schedules.
    for a,b,c in product(distribution_basis, repeat=3):
        d = dict(zip(S,(a,b,c)))
        assert observe(d) == observe(aggregate(d))
        cases += 1
    assert cases == 28**3
    assert len({observe(deterministic(S,3,ijk)) for ijk in product(range(3),repeat=3)}) > 0
    assert len({observe({s:tuple(ONE if j== (ab if GROUPS[s]=='AB' else cc) else ZERO for j in range(3)) for s in S}) for ab,cc in product(range(3),repeat=2)}) == 9

    # Nonseparable origin-dependent terminal errors: exact supporting-gap example.
    P2={'A':F(1,2),'B':F(1,2)}
    Q2=P2.copy()
    p2={'A':(F(1,4),F(1,2),F(3,4)), 'B':(F(3,4),F(1,2),F(1,4))}
    q2={'A':(F(1,5),F(1,2),F(4,5)), 'B':(F(4,5),F(1,2),F(1,5))}
    group2={'A':'AB','B':'AB'}
    assert all(ZERO<v<ONE for t in (p2,q2) for row in t.values() for v in row)
    lr_corners=[observe(deterministic(('A','B'),3,(j,j)), P2,Q2,p2,q2) for j in range(3)]
    full_corners=[observe(deterministic(('A','B'),3,(i,j)), P2,Q2,p2,q2)
                  for i,j in product(range(3),repeat=2)]
    assert all(c[0] == F(1,2) and c[1]==F(1,2) for c in lr_corners)
    w=(F(20),F(20),ZERO,ZERO)
    dot=lambda u,v: sum((a*b for a,b in zip(u,v)),ZERO)
    min_lr=min(dot(w,c) for c in lr_corners)
    min_full=min(dot(w,c) for c in full_corners)
    witness=observe(deterministic(('A','B'),3,(0,2)),P2,Q2,p2,q2)
    assert witness == (F(1,4),F(1,5),F(2),F(2))
    assert min_lr==F(20) and min_full==F(9) and dot(w,witness)==F(9)
    print('SAFE_RATIO_CLASSES:', {'AB':str(P['A']/Q['A']),'C':str(P['C']/Q['C'])})
    print('SAFE_FULL_DIMENSION_DETERMINANT:',determinant)
    print('SAFE_EXACT_MATCH:',tuple(str(v) for v in output))
    print('SAFE_LR_HAZARDS_AB:', tuple(str(v) for v in hazards(lr['A'])))
    print('SAFE_LR_HAZARDS_C:', tuple(str(v) for v in hazards(lr['C'])))
    print('SAFE_GRID_FULL_SCHEDULES:',cases)
    print('UNSAFE_WITNESS:',tuple(str(v) for v in witness))
    print('UNSAFE_INTEGER_INEQUALITY: 20*eP+20*eQ>=20; FULL value=9')
    print('UNSAFE_SUPPORT_GAP:',min_lr-min_full)
    print('UNSAFE_LINF_DISTANCE_LOWER_BOUND:',(min_lr-min_full)/sum(map(abs,w)))
    print('PASS_EXACT_R5_STATIC_ORIGIN_CHAIN_HULL_RIGIDITY')

if __name__ == '__main__':
    run()
