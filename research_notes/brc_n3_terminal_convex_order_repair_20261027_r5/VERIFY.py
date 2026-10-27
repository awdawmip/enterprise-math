"""Exact finite two-measure N=3 BRC terminal-repair certificate.

All numerical claims use fractions.Fraction; no floating-point computation.
This is an external finite probability tree, not native Heartbeat dynamics.
"""
from fractions import Fraction as F
from itertools import combinations, product

ONE, ZERO = F(1), F(0)
R = lambda a, b=1: F(a, b)

ROOT = {'a': (R(1,2), R(1,2)), 'b': (R(1,2), R(3,2))}  # (Q, LR)
STEP2 = {
    'a': [('ax', R(1,3), ONE), ('aw', R(2,3), R(1,4))],
    'b': [('by', R(1,2), ONE), ('bv', R(1,2), R(2))],
}
TERMINAL = {
    'ax': [(R(1,2),R(1,4)), (ONE,R(1,2)), (R(3,2),R(1,4))],
    'aw': [(R(1,8),R(1,2)), (R(3,8),R(1,2))],
    'by': [(R(1,2),R(1,3)), (ONE,R(1,3)), (R(3,2),R(1,3))],
    'bv': [(R(3,2),R(1,2)), (R(5,2),R(1,2))],
}

# The ordered observer vector is (P(decide Q), Q(decide P), E_P tau, E_Q tau).
def observe(policy):
    p_decide_p, q_decide_p = ZERO, ZERO
    ep_tau, eq_tau = ONE, ONE
    measure = {}
    for name, (q1, l1) in ROOT.items():
        p1 = q1*l1
        c1 = policy['c1'][l1]
        # Early-stopping decisions are "Q" throughout this certificate.
        ep_tau += p1*c1
        eq_tau += q1*c1
        for node, qprob, l2 in STEP2[name]:
            q2 = q1*qprob*c1
            p2 = l2*q2
            c2 = policy['c2'][l2] if policy.get('lr_only', True) else policy['c2'][node]
            ep_tau += p2*c2
            eq_tau += q2*c2
            for l3, k3 in TERMINAL[node]:
                q3 = q2*c2*k3
                g = policy['g3'].get(l3, ZERO)
                p_decide_p += l3*q3*g
                q_decide_p += q3*g
                measure[l3] = measure.get(l3, ZERO) + q3
    return (ONE-p_decide_p, q_decide_p, ep_tau, eq_tau), measure

# Full-history action at the collision: ax continues, by stops.
F_FULL = {'c1': {R(1,2):R(1,2), R(3,2):R(1,2)},
          'c2': {'ax':ONE,'aw':ZERO,'by':ZERO,'bv':ZERO},
          'g3': {R(1,2):ZERO, ONE:ONE, R(3,2):ZERO}, 'lr_only':False}

# Seedless likelihood-ratio policy: one continuation action at L_2 = 1.
C_LR = {'c1': {R(1,2):R(1,2), R(3,2):R(1,2)},
        'c2': {R(1,4):ZERO, ONE:R(2,5), R(2):ZERO},
        'g3': {R(1,2):R(1,6), ONE:ONE, R(3,2):R(1,6)}}


def bounded_two_moment_solver(y, mass, a, b):
    """Find exact rational g in [0,1]^m with sum(mass*g)=a, sum(y*mass*g)=b.
    Searches all vertex types: at most two non-bound decisions. Exponential in m.
    """
    m = len(y)
    for nf in range(min(2,m)+1):
        for free in combinations(range(m), nf):
            fixed = [j for j in range(m) if j not in free]
            for vals in product((ZERO, ONE), repeat=len(fixed)):
                g = [None]*m
                for j,v in zip(fixed, vals):g[j]=v
                a_left = a - sum((mass[j]*g[j] for j in fixed), ZERO)
                b_left = b - sum((y[j]*mass[j]*g[j] for j in fixed), ZERO)
                if nf == 0:
                    if a_left == b_left == 0: return tuple(g)
                elif nf == 1:
                    j = free[0]
                    t = a_left/mass[j]
                    if ZERO <= t <= ONE and y[j]*mass[j]*t == b_left:
                        g[j] = t
                        return tuple(g)
                else:
                    j,k = free
                    det = mass[j]*mass[k]*(y[k]-y[j])
                    assert det != 0
                    gj = (a_left*mass[k]*y[k]-b_left*mass[k])/det
                    gk = (b_left*mass[j]-a_left*mass[j]*y[j])/det
                    if ZERO <= gj <= ONE and ZERO <= gk <= ONE:
                        g[j],g[k] = gj,gk
                        return tuple(g)
    return None


def main():
    leaves = []
    for root,(q1,l1) in ROOT.items():
        assert q1 > 0 and l1 > 0
        trans=STEP2[root]
        assert sum((p for _,p,_ in trans),ZERO)==ONE
        assert sum((p*r for _,p,r in trans),ZERO)==q1*l1/q1
        for node,qp,l2 in trans:
            kern=TERMINAL[node]
            assert sum((p for _,p in kern),ZERO)==ONE
            assert sum((p*l for l,p in kern),ZERO)==l2
            for l3,k3 in kern:
                assert qp*k3 > 0 and l3>0
                leaves.append((node,l3,q1*qp*k3))
    assert len(leaves)==10
    assert sum((q for _,_,q in leaves),ZERO)==ONE
    assert sum((y*q for _,y,q in leaves),ZERO)==ONE
    of, u = observe(F_FULL)
    oc, v = observe(C_LR)
    expected = (R(23,24),R(1,24),R(19,12),R(19,12))
    assert of==oc==expected
    y=(R(1,2),ONE,R(3,2))
    assert tuple(u.get(yi,ZERO) for yi in y)==(R(1,48),R(1,24),R(1,48))
    assert tuple(v.get(yi,ZERO) for yi in y)==(R(1,40),R(1,30),R(1,40))
    d = tuple(v[yi]-u[yi] for yi in y)
    assert d==(R(1,240),-R(1,120),R(1,240))
    assert sum(d)==0 and sum(yi*di for yi,di in zip(y,d))==0
    dm2=sum((yi*yi*di for yi,di in zip(y,d)),ZERO)
    assert dm2==R(1,480)
    b_arrival=R(5,24)
    assert -dm2/b_arrival==-R(1,100)  # C_2 = weighted Cov(z, E_K Y^2)
    # Convex order for ternary identical mass & mean: positive second-moment delta.
    assert dm2 > 0
    # Exact terminal repair: target g_full selects only the y=1 bin.
    a,b=R(1,24),R(1,24)
    sol=bounded_two_moment_solver(y,[v[yi] for yi in y],a,b)
    assert sol == (R(5,6),ZERO,R(5,6))  # lexical first vertex; a second valid repair is (1/6,1,1/6)
    assert sum(v[yi]*sol[j] for j,yi in enumerate(y)) == a
    assert sum(yi*v[yi]*sol[j] for j,yi in enumerate(y)) == b
    # The particular target requires two fractional bins, not just one.
    assert len([z for z in sol if 0<z<1])==2
    assert u[y[1]]>v[y[1]]
    assert v[y[0]]==v[y[2]]
    assert a>v[y[1]]
    # If at most one endpoint is fractional then E[Y*g]=E[g] implies both
    # endpoint decisions equal and hence must both be bound values; neither works.
    print('LEAVES 10; POSITIVE_NORM_AND_LR_MEANS PASS')
    print('O_FULL = O_SEEDLESS =', tuple(str(z) for z in of))
    print('TERMINAL_U =', tuple(str(u[yi]) for yi in y))
    print('TERMINAL_V =', tuple(str(v[yi]) for yi in y))
    print('DELTA_V_MINUS_U =', tuple(str(z) for z in d))
    print('DELTA_M2 =', dm2)
    print('COV_Z_M2 =', -dm2/b_arrival)
    print('EXACT_REPAIR_G3_SOLVER =', tuple(str(z) for z in sol))
    print('EXACT_REPAIR_G3_AUTHORED =', tuple(str(C_LR['g3'][yi]) for yi in y))
    print('FRACTIONAL_G3_ACTIONS_REQUIRED = 2')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__': main()
