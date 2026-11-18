#!/usr/bin/env python3
"""Exact two-source, non-IID, two-route, one shared tied-port counterexample."""
from fractions import Fraction as F

HALF = F(1, 2)
# P/S initial roots 0,1 have probabilities 1/2 each.
# Next symbol probabilities vary by preceding root: non-IID under both sources.
PZERO = {
    'P': (F(1, 4), F(3, 4)),
    'Q': (F(1, 3), F(2, 3)),
}


def ordered_paths(source, y):
    assert source in PZERO and F(0) <= y <= F(1)
    out = []
    # Fully enumerated source, first symbol, second symbol, and ordered port actions.
    for root in (0, 1):
        for second in (0, 1):
            p2 = PZERO[source][root] if second == 0 else 1 - PZERO[source][root]
            prefix = HALF * p2
            assert prefix > 0
            # Y is one shared source-blind constant, reused twice on a path.
            out.extend([
                (root, second, ('Y1_0',), prefix*(1-y), 'A'),
                (root, second, ('Y1_1','Y2_0'), prefix*y*(1-y), 'B'),
                (root, second, ('Y1_1','Y2_1'), prefix*y*y, 'C'),
            ])
    assert len(out) == 12
    assert sum(p for _,_,_,p,_ in out) == 1
    return out


def observe(source,y):
    paths=ordered_paths(source,y)
    # One binary terminal observable, common to both sources.
    reward=sum(p for r,s,h,p,t in paths if (r==0 and t=='B') or (r==1 and t=='C'))
    law={r:tuple(sum(p for rr,s,h,p,t in paths if rr==r and t==tt)
                 for tt in ('A','B','C')) for r in (0,1)}
    return reward,law


def main():
    assert PZERO['P'] != PZERO['Q']
    for source in PZERO:
        assert all(0 < p < 1 for p in PZERO[source])
        assert PZERO[source][0] != PZERO[source][1]
    checked=0
    for iy in range(17):
        y=F(iy,16)
        for source in PZERO:
            reward,law=observe(source,y)
            assert reward == y/2
            for r in (0,1):
                assert law[r] == (HALF*(1-y),HALF*y*(1-y),HALF*y*y)
                assert sum(law[r]) == HALF
            checked+=1
    # True global value, unique fixed shared-port optimiser y=1.
    true_reward=observe('P',F(1))[0]
    assert true_reward==HALF
    assert observe('Q',F(1))[0]==HALF
    # Invalid independent-route cones: choose y_0=1/2 for route 0 and y_1=1 for route 1.
    # These are each implementable on their *own* route, but not by one shared y.
    w0=w1=HALF
    y0,y1=HALF,F(1)
    z0,v0=w0*y0,w0*y0*y0
    z1,v1=w1*y1,w1*y1*y1
    assert z0==F(1,4) and v0==F(1,8)
    assert z1==HALF and v1==HALF
    assert z0*z0==w0*v0 and z1*z1==w1*v1
    relaxed_reward=z0-v0+v1
    assert relaxed_reward==F(5,8)
    assert relaxed_reward-true_reward==F(1,8)
    assert z0/w0 != z1/w1 and v0/w0 != v1/w1
    # Algebraic conic bound: z0-v0 <= z0 - z0^2/w0 <= w0/4=1/8.
    # And v1 <= w1=1/2, so the independent-cone upper bound is exactly 5/8.
    for iz in range(9):
        z=F(iz,16)
        assert 0 <= z <= w0
        lower_v=z*z/w0
        assert z-lower_v<=w0/4
    # Joint hull witnesses (common ex-ante mixture Y=0 or Y=1 with weight 1/2).
    m1,m2=HALF,HALF
    assert m1*m1<=m2<=m1
    assert all((HALF*m1,HALF*m2)==(F(1,4),F(1,4)) for _ in (0,1))
    joint_mixture_reward=(observe('P',F(0))[0]+observe('P',F(1))[0])/2
    assert joint_mixture_reward==F(1,4)
    print('POSITIVE_NONIID_TRANSITIONS',PZERO)
    print('ORDERED_PREFIXES',4,'LEAVES_PER_SOURCE',12)
    print('EXACT_REPLAYS_SOURCE_POLICY_PAIRS',checked)
    print('TRUE_SHARED_PORT_MAX_REWARD',true_reward,'MIN_LOSS',1-true_reward)
    print('INDEPENDENT_ROUTE_CONE_MAX_REWARD',relaxed_reward,'MIN_LOSS',1-relaxed_reward)
    print('STRICT_GAP',relaxed_reward-true_reward)
    print('MISSING_CROSS_ROUTE_MOMENTS', 'z0/w0 = z1/w1; v0/w0 = v1/w1')
    print('EXACT_JOINT_HULL', 'shared m1,m2: 0<=m1<=1,m1^2<=m2<=m1; z_i=w_i*m1, v_i=w_i*m2')
    print('STAGE284B_SHARED_PORT_CONIC_COMPATIBILITY_EXACT_PASS')

if __name__=='__main__':
    main()
