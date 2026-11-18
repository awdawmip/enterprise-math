#!/usr/bin/env python3
"""Stage285-B: exact causal mixed-moment hull and source-tagged ordered DFS.

All numerical computations use fractions.Fraction; all universal statements
require the separate algebraic proof in PROOF_STAGE285B.md.
"""
from fractions import Fraction as F

ZERO, ONE, HALF = F(0), F(1), F(1, 2)
INITIAL = {"P": F(1, 4), "Q": F(1, 3)}
SECOND_ZERO = {
    "P": (F(1, 4), F(3, 4)),
    "Q": (F(1, 3), F(2, 3)),
}


def ordered_paths(source, x, y):
    """Preserve (upstream U, initial R, second S, final T, ordered port action)."""
    assert source in INITIAL and 0 <= x <= 1 and 0 <= y <= 1
    out = []
    for u in (0, 1):
        pu = x if u else 1-x
        for r in (0, 1):
            pr = INITIAL[source] if r == 0 else 1-INITIAL[source]
            for s in (0, 1):
                ps0 = SECOND_ZERO[source][r]
                ps = ps0 if s == 0 else 1-ps0
                assert 0 < pr < 1 and 0 < ps < 1
                p = pu * pr * ps
                t = r ^ u
                out.extend([
                    (u, r, s, t, ('Y1_0',), 'A', p*(1-y)),
                    (u, r, s, t, ('Y1_1', 'Y2_0'), 'B', p*y*(1-y)),
                    (u, r, s, t, ('Y1_1', 'Y2_1'), 'C', p*y*y),
                ])
    assert len(out) == 24
    assert sum(item[-1] for item in out) == ONE
    return out


def full_law(source, x, y):
    out = ordered_paths(source, x, y)
    # Exact full ordered-prefix distribution over all 24 leaves.
    return {(u, r, s, t, action, terminal): mass for u,r,s,t,action,terminal,mass in out}


def moments(settings):
    # A source-blind ex ante mixture over *complete* deterministic global settings.
    assert sum(weight for weight, _, _ in settings) == ONE
    assert all(weight >= 0 and 0 <= x <= 1 and 0 <= y <= 1
               for weight,x,y in settings)
    u = sum((weight*x for weight,x,y in settings), ZERO)
    m1 = sum((weight*y for weight,x,y in settings), ZERO)
    m2 = sum((weight*y*y for weight,x,y in settings), ZERO)
    c1 = sum((weight*x*y for weight,x,y in settings), ZERO)
    c2 = sum((weight*x*y*y for weight,x,y in settings), ZERO)
    return u,m1,m2,c1,c2


def common_cone(moment_tuple):
    u,m1,m2,c1,c2 = moment_tuple
    assert 0 <= u <= 1
    blocks = ((1-u,m1-c1,m2-c2),(u,c1,c2))
    return all(0 <= d <= b <= a and b*b <= a*d for a,b,d in blocks)


def endpoint_atoms(moment_tuple):
    """Exact constructive 4-atom realization for a feasible moment tuple."""
    assert common_cone(moment_tuple)
    u,m1,m2,c1,c2 = moment_tuple
    result=[]
    for k, a,b,d in ((0,1-u,m1-c1,m2-c2),(1,u,c1,c2)):
        if a == 0:
            assert b == d == 0
            continue
        if b == 0:
            assert d == 0
            result.append((a,F(k),ZERO))
            continue
        assert d > 0
        y = d/b
        live = b*b/d
        assert 0 <= y <= 1 and 0 < live <= a
        if a-live:
            result.append((a-live,F(k),ZERO))
        result.append((live,F(k),y))
    assert len(result) <= 4
    assert sum(w for w,x,y in result) == 1
    assert moments(result) == moment_tuple
    return result


def mixed_law(source, settings):
    result={k:ZERO for k in full_law(source,ZERO,ZERO)}
    for weight,x,y in settings:
        law=full_law(source,x,y)
        for k,p in law.items():
            result[k] += weight*p
    assert sum(result.values()) == 1
    return result


def reward(source,settings):
    law=mixed_law(source,settings)
    return sum((mass for (u,r,s,t,word,terminal),mass in law.items()
                if (t == 0 and terminal == 'B') or (t == 1 and terminal == 'C')),ZERO)


def reward_formula(source,moment_tuple):
    u,m1,m2,c1,c2 = moment_tuple
    a=INITIAL[source]
    b=1-2*a
    # Shared first and second moments of y, corrected by the missing x-y cross moments.
    return a*m1+(1-2*a)*m2+b*(c1-2*c2)


def route_formula(source,moment_tuple):
    u,m1,m2,c1,c2=moment_tuple
    a=INITIAL[source]
    b=1-2*a
    w0=a+b*u
    z0=a*m1+b*c1
    v0=a*m2+b*c2
    w1=1-w0
    z1=m1-z0
    v1=m2-v0
    assert 0 <= v0 <= z0 <= w0 and 0 <= v1 <= z1 <= w1
    return (w0-z0,z0-v0,v0),(w1-z1,z1-v1,v1)


def main():
    assert all(0<p<1 for p in INITIAL.values())
    assert all(0<p<1 for pair in SECOND_ZERO.values() for p in pair)
    assert SECOND_ZERO['P'] != SECOND_ZERO['Q']
    source_policy_pairs=0
    leaf_checks=0
    for ix in range(9):
        x=F(ix,8)
        for iy in range(9):
            y=F(iy,8)
            m=(x,y,y*y,x*y,x*y*y)
            assert common_cone(m)
            for src in ('P','Q'):
                law=full_law(src,x,y)
                assert sum(law.values()) == 1
                actual={t:tuple(sum((p for (u,r,s,tt,word,terminal),p in law.items()
                                      if tt==t and terminal==term),ZERO) for term in ('A','B','C'))
                        for t in (0,1)}
                pred=route_formula(src,m)
                assert actual[0]==pred[0] and actual[1]==pred[1]
                assert reward(src,[(ONE,x,y)]) == reward_formula(src,m)
                source_policy_pairs += 1
                leaf_checks += len(law)

    A=[(HALF,ZERO,ZERO),(HALF,ONE,ONE)]   # positive x/y association
    B=[(HALF,ZERO,ONE),(HALF,ONE,ZERO)]   # negative x/y association
    assert moments(A)[:3] == moments(B)[:3] == (HALF,HALF,HALF)
    assert moments(A)[3:] == (HALF,HALF)
    assert moments(B)[3:] == (ZERO,ZERO)
    for src,score_a,score_b,gap in [('P',F(1,8),F(3,8),F(1,8)),
                                    ('Q',F(1,6),F(1,3),F(1,12))]:
        assert reward(src,A)==score_a and reward(src,B)==score_b
        assert reward_formula(src,moments(A))==score_a
        assert reward_formula(src,moments(B))==score_b
        assert score_b - F(1,4)==gap
        assert reward(src,[(F(1,4),ZERO,ZERO), (F(1,4),ZERO,ONE),
                           (F(1,4),ONE,ZERO),(F(1,4),ONE,ONE)]) == F(1,4)
    # m1=m2=1/2 -> Y in {0,1}; the joint coupling t belongs to [0,1/2].
    # F_P=3/8-t/2 and F_Q=1/3-t/3. Exact maxima at t=0.
    for it in range(17):
        t=F(it,32)
        setting=[(t,ZERO,ZERO),(HALF-t,ZERO,ONE),
                 (HALF-t,ONE,ZERO),(t,ONE,ONE)]
        assert moments(setting)==(HALF,HALF,HALF,t,t)
        assert reward('P',setting)==F(3,8)-t/2
        assert reward('Q',setting)==F(1,3)-t/3
    # Arbitrary non-degenerate ex ante mixture, recovered by <=4 endpoint atoms.
    trial=[(F(1,8),ZERO,ZERO),(F(2,8),ONE,ONE),
           (F(2,8),F(1,3),F(2,5)),(F(3,8),F(3,4),F(7,9))]
    m=moments(trial)
    assert common_cone(m)
    witness=endpoint_atoms(m)
    for src in ('P','Q'):
        assert mixed_law(src,trial)==mixed_law(src,witness)
        assert reward(src,trial)==reward_formula(src,m)
    # Degenerate boundaries of the full moment cone.
    for moment_tuple in [(ZERO,ZERO,ZERO,ZERO,ZERO),
                         (ONE,ONE,ONE,ONE,ONE),
                         (HALF,ZERO,ZERO,ZERO,ZERO),
                         (HALF,HALF,HALF,ZERO,ZERO)]:
        assert moments(endpoint_atoms(moment_tuple))==moment_tuple
    print('STAGE285B_SOURCES',INITIAL)
    print('STRICTLY_POSITIVE_NONIID_SECOND_TRANSITIONS',SECOND_ZERO)
    print('ORDERED_TERMINALS_PER_SOURCE',24)
    print('EXACT_SOURCE_POLICY_PAIRS',source_policy_pairs,'EXACT_ORDERED_LEAF_CHECKS',leaf_checks)
    print('MIXTURE_A_MOMENTS',moments(A),'MIXTURE_B_MOMENTS',moments(B))
    print('MIXTURE_A_REWARDS',reward('P',A),reward('Q',A))
    print('MIXTURE_B_REWARDS',reward('P',B),reward('Q',B))
    print('CONSTRAINED_FIBER_TRUE_MAX',F(3,8),F(1,3))
    print('INVALID_FACTOR_PRODUCT_VALUES',F(1,4),F(1,4))
    print('STRICT_OBSERVER_GAPS',F(1,8),F(1,12))
    print('GENERIC_MIXED_MOMENTS',m)
    print('FOUR_ATOM_WITNESS',witness)
    print('STAGE285B_CAUSAL_SPLIT_MOMENT_HULL_EXACT_PASS')


if __name__=='__main__':
    main()
