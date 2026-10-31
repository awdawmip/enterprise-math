#!/usr/bin/env python3
"""Exact, standard-library-only reproduction of R5 2026-10-29 facet/Bellman audit.

The second three-control example is an abstract *algebraic* illustration,
not an asserted two-measure sequential experiment or a mother counterexample.
"""
from fractions import Fraction as F
from itertools import combinations, product
from functools import reduce
from math import gcd

QA = (F(1, 4), F(1, 2), F(1, 4))
PA = (F(1, 8), F(1, 2), F(3, 8))
QB = (F(1, 3), F(1, 3), F(1, 3))
PB = (F(1, 6), F(1, 3), F(1, 2))
P = (PA, PB)
Q = (QA, QB)
RHO = (F(1, 2), F(1, 2))


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def primitive(v):
    lcm = 1
    for a in v:
        lcm = lcm * a.denominator // gcd(lcm, a.denominator)
    z = tuple(int(a * lcm) for a in v)
    g = reduce(gcd, (abs(a) for a in z))
    assert g > 0
    return tuple(a // g for a in z)


def observe(source_actions, terminal_actions):
    """Source action 0=stop P, 1=stop Q, 2=continue.
    Terminal action bit 1=declare P, 0=declare Q; labels have LR 1/2,1,3/2.
    """
    ep = eq = tp = tq = F(0)
    for i, choice in enumerate(source_actions):
        mass = RHO[i]
        if choice == 0:
            eq += mass
            tp += mass
            tq += mass
        elif choice == 1:
            ep += mass
            tp += mass
            tq += mass
        else:
            tp += 2 * mass
            tq += 2 * mass
            for j, action in enumerate(terminal_actions[i]):
                ep += mass * P[i][j] * (1 - action)
                eq += mass * Q[i][j] * action
    return (ep, eq, tp, tq)


def full_vertices_and_witnesses():
    out = {}
    for actions in product(range(3), repeat=2):
        for bits in product(range(2), repeat=6):
            o = observe(actions, (bits[:3], bits[3:]))
            out.setdefault(o, (actions, bits))
    return out


def lr_vertices_and_witnesses():
    out = {}
    for action in range(3):
        for bits in product(range(2), repeat=3):
            o = observe((action, action), (bits, bits))
            out.setdefault(o, (action, bits))
    return out


def facets_3d(points):
    """Complete exact 3D H-representation by all non-collinear vertex triples.
    Requires a full-dimensional rational point set (verified separately).
    Returns primitive oriented integer normals n with n.dot(v)>=b.
    """
    facets = {}
    for a, b, c in combinations(points, 3):
        n = cross(tuple(y-x for x, y in zip(a, b)),
                  tuple(y-x for x, y in zip(a, c)))
        if n == (0, 0, 0):
            continue
        n = primitive(n)
        bound = dot(n, a)
        slacks = [dot(n, z) - bound for z in points]
        if all(s >= 0 for s in slacks):
            pass
        elif all(s <= 0 for s in slacks):
            n = tuple(-x for x in n)
            bound = -bound
        else:
            continue
        facets[(n, bound)] = tuple(z for z in points if dot(n, z) == bound)
    return facets


def full_bellman(n):
    a, b, c = n
    total = F(0)
    for i in range(2):
        stop_p = RHO[i] * (b + c)
        stop_q = RHO[i] * (a + c)
        continue_cost = RHO[i] * (2*c + sum(
            (min(a * P[i][j], b * Q[i][j]) for j in range(3)), F(0)))
        total += min(stop_p, stop_q, continue_cost)
    return total


def lr_bellman(n):
    a, b, c = n
    continue_cost = 2*c + sum(
        (RHO[i] * min(a * P[i][j], b * Q[i][j])
         for i in range(2) for j in range(3)), F(0))
    return min(a+c, b+c, continue_cost)


def rank3(vectors):
    base = vectors[0]
    diffs = [tuple(y-x for x, y in zip(base, v)) for v in vectors[1:]]
    for a, b, c in combinations(diffs, 3):
        if dot(a, cross(b, c)):
            return True
    return False


def main():
    for pi, qi in zip(P, Q):
        assert all(x > 0 for x in pi + qi)
        assert sum(pi) == sum(qi) == 1
        assert tuple(p/q for p, q in zip(pi, qi)) == (F(1, 2), F(1), F(3, 2))
    assert sum(RHO) == 1
    full = full_vertices_and_witnesses()
    lr = lr_vertices_and_witnesses()
    assert len(full) == 83 and len(lr) == 10
    assert set(lr).issubset(full)
    assert all(t == u for e, q, t, u in full)
    assert all(t == u for e, q, t, u in lr)
    lp = sorted({(e, q, t) for e, q, t, u in lr})
    fp = sorted({(e, q, t) for e, q, t, u in full})
    assert rank3(lp)
    faces = facets_3d(lp)
    assert len(faces) == 7
    expected = {
        (-48, -48, 7): (F(-41), F(-83, 2), 4),
        (-2, -3, 0): (F(-3), F(-3), 3),
        (-2, -1, 0): (F(-2), F(-2), 3),
        (0, 0, -1): (F(-2), F(-2), 8),
        (2, 1, 0): (F(1), F(1), 3),
        (2, 3, 0): (F(2), F(2), 3),
        (48, 48, 7): (F(55), F(109, 2), 4),
    }
    assert set(n for n, b in faces) == set(expected)
    print('EXPERIMENT: TWO-LAW ONE-MERGER SOURCE-SENSITIVE RATIONAL MODEL')
    print('SOURCE_Q', Q, 'SOURCE_P', P, 'SOURCE_MASS', RHO)
    print('LR_DETERMINISTIC_RAW', 3*2**3, 'LR_DISTINCT', len(lp))
    print('FULL_DETERMINISTIC_RAW', 3**2*2**6, 'FULL_DISTINCT', len(fp))
    print('LR_AFFINE_RANK', 3, 'EXACT_FACET_COUNT', len(faces))
    violations = []
    for (n, bound), face in sorted(faces.items()):
        assert expected[n] == (bound, min(dot(n, v) for v in fp), len(face))
        assert min(dot(n, v) for v in lp) == bound
        assert lr_bellman(n) == bound
        fb = full_bellman(n)
        assert fb == min(dot(n, v) for v in fp)
        violation = fb - bound
        if violation < 0:
            violations.append(n)
        print('FACET', 'n='+str(n), 'LR_MIN='+str(bound),
              'FULL_BELLMAN_MIN='+str(fb), 'SLACK='+str(violation),
              'FACE_VERTICES='+str(len(face)))
    assert sorted(violations) == [(-48, -48, 7), (48, 48, 7)]
    for n in violations:
        opt, o = min((dot(n, z[:3]), z) for z in full)
        assert opt == full_bellman(n)
        print('SEPARATOR', n, 'FULL_WITNESS_4D', tuple(str(x) for x in o),
              'ALL_REAL_LR_BOUND', str(lr_bellman(n)),
              'FULL_VALUE', str(opt), 'EXACT_GAP', str(lr_bellman(n)-opt),
              'L_INFINITY_DISTANCE_LOWER', str(F(1,206)))

    # Algebraic fixture: a two-key exposed rectangular face plus one escape key.
    # It is NOT claimed to be realizable as the original stopping experiment.
    zero = (F(0),)*4
    V = {(0,0):zero, (1,0):(F(1),F(0),F(0),F(0)),
         (0,1):(F(0),F(1),F(0),F(0)),
         (1,1):(F(0),F(0),F(1),F(0))}
    W = (F(0),F(0),F(0),F(1))
    all_vertices = [V[(a,b)] if c==0 else W
                    for a,b,c in product(range(2),repeat=3)]
    assert len(set(all_vertices)) == 5
    assert rank3([(x[0],x[1],x[2]) for x in V.values()])
    assert [v for v in all_vertices if v[3]==0].count(V[(0,0)]) == 1
    assert len([v for v in all_vertices if v[3]==0]) == 4
    U = tuple((V[(0,0)][i]+V[(1,1)][i])/2 for i in range(4))
    assert U==(F(0),F(0),F(1,2),F(0))
    count = 0
    best = None
    for ip,iq,is_ in product(range(11), repeat=3):
        p,q,s = F(ip,10),F(iq,10),F(is_,10)
        Y=((1-s)*p*(1-q), (1-s)*(1-p)*q,
           (1-s)*p*q, s)
        dist = max(abs(x-y) for x,y in zip(Y,U))
        assert dist >= F(1,20)
        best = dist if best is None or dist<best else best
        count+=1
    assert count==1331
    print('ALGEBRAIC_FIXTURE_ONLY', 'FACE_CORNERS=4', 'RANK=3',
          'OFF_FACE_GAP=1', 'TARGET='+str(U))
    print('ALGEBRAIC_PRODUCT_INVARIANT',
          'mu00*mu11=mu01*mu10', 'target_products=1/4,0')
    print('UNIVERSAL_PROVED_DISTANCE_LOWER',F(1,20),
          'RATIONAL_GRID_CHECKED',count,'GRID_MIN_DISTANCE',best)
    print('PASS_EXACT_R5_FACET_BELLMAN_AND_FACE_RECTANGLE')

if __name__=='__main__':
    main()
