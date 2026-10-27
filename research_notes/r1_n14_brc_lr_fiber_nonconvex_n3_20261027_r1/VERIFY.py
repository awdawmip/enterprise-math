#!/usr/bin/env python3
"""Exact finite BRC-style ordered-path verification: LR-fiber nonconvexity at N=3."""
from fractions import Fraction as F
from collections import defaultdict
import itertools
import json

A = (0, 1, 2)
U = (F(1, 3),) * 3
R = (F(2), F(1), F(1, 2))
K_P = {
    0: (F(1, 4), F(1, 4), F(1, 2)),
    1: (F(1, 12), F(3, 4), F(1, 6)),
    2: (F(1, 6), F(1, 2), F(1, 3)),
}
K_Q = {i: tuple(R[j]*K_P[i][j] for j in A) for i in A}


def path_mass(h, law):
    if not h: return F(1)
    m = U[h[0]]
    if len(h) >= 2: m *= U[h[1]]
    if len(h) >= 3: m *= (K_P if law == "P" else K_Q)[h[0]][h[2]]
    return m


def x(h):
    if len(h) == 0: return (0, '*')
    if len(h) == 1: return (1, h[0])
    if len(h) == 2: return (2, '*')
    if len(h) == 3: return (3, h[2])
    raise ValueError('horizon 3')


def o(h): return x(h)[1]


def terminal(policy, law):
    # policy = {'c1': three continue probabilities, 'c2': prob continue from
    # the single time-2 state, 'd3': prob decide 1 at terminal x(3,j)}.
    ans = defaultdict(F)
    for i in A:
        m1 = path_mass((i,), law)
        c1 = policy['c1'][i]
        ans[(1, str(o((i,))), 0)] += m1*(1-c1)
        for a in A:
            m2 = m1*U[a]*c1
            ans[(2, '*', 0)] += m2*(1-policy['c2'])
            for j in A:
                m3 = m2*policy['c2']*(K_P if law == 'P' else K_Q)[i][j]
                d = policy['d3'][j]
                ans[(3, str(j), 1)] += m3*d
                ans[(3, str(j), 0)] += m3*(1-d)
    return dict(ans)


def rat(f):
    f=F(f)
    return str(f.numerator) if f.denominator == 1 else f'{f.numerator}/{f.denominator}'


def fmt(dist):
    return {f'T={k[0]},o={k[1]},D={k[2]}':rat(v) for k,v in sorted(dist.items()) if v}


def weighted_mix(a,b):
    return {k:(a.get(k,F(0))+b.get(k,F(0)))/2 for k in (a.keys()|b.keys())}


def check():
    paths=[h for n in range(4) for h in itertools.product(A,repeat=n)]
    assert len(paths)==40
    for i in A:
        for k in (K_P[i], K_Q[i]):
            assert all(v>0 for v in k) and sum(k)==1
    for h in paths:
        mP,mQ=path_mass(h,'P'),path_mass(h,'Q')
        assert mP>0 and mQ>0
        if len(h)<3: assert mQ/mP==1
        else: assert mQ/mP==R[h[-1]]
        if len(h)<3:
            assert sum(path_mass(h+(a,), 'P') for a in A)==mP
            assert sum(path_mass(h+(a,), 'Q') for a in A)==mQ
    # Assert recursive-updatability: child state depends only on parent x and symbol.
    for depth in range(3):
        groups=defaultdict(list)
        for h in itertools.product(A,repeat=depth): groups[x(h)].append(h)
        for hs in groups.values():
            for a in A:
                assert len({x(h+(a,)) for h in hs})==1
    # Strong LR-fiber constancy on ALL states, not only on observed states.
    for depth in range(4):
        groups=defaultdict(list)
        for h in itertools.product(A,repeat=depth): groups[x(h)].append(h)
        for hs in groups.values():
            assert len({path_mass(h,'Q')/path_mass(h,'P') for h in hs})==1
    pA={'c1':(F(1),F(0),F(0)), 'c2':F(1),'d3':(F(1),)*3}
    pB={'c1':(F(0),F(1),F(0)), 'c2':F(0),'d3':(F(1),)*3}
    # Any midpoint realization is forced by time-1 observable i and total T=3.
    pForced={'c1':(F(1,2),F(1,2),F(0)), 'c2':F(1,2), 'd3':(F(1),)*3}
    results={}
    for law in ('P','Q'):
        a,b=terminal(pA,law),terminal(pB,law)
        target=weighted_mix(a,b)
        forced=terminal(pForced,law)
        assert sum(target.values())==1
        assert sum(forced.values())==1
        assert all(target.get((1,str(i),0),0)==forced.get((1,str(i),0),0) for i in A)
        assert target.get((2,'*',0),0)==forced.get((2,'*',0),0)==F(1,6)
        assert sum(v for k,v in target.items() if k[0]==3)==F(1,6)
        assert sum(v for k,v in forced.items() if k[0]==3)==F(1,6)
        gap=target.get((3,'0',1),0)-forced.get((3,'0',1),0)
        assert gap == (F(1,72) if law=='P' else F(1,36))
        results[law]={
            'A':fmt(a),'B':fmt(b),'midpoint':fmt(target),
            'forced_quotient':fmt(forced),'j0_D1_gap':rat(gap),
            'required_t1_continuations':['1/2','1/2','0'],
            'required_t2_continuation':'1/2'
        }
    assert K_P[0]!=K_P[1] and K_Q[0]!=K_Q[1]
    # Predecessor kernel rank/TVD reuse (time-one x labels, not time-one LR classes).
    tvQ=sum(abs(K_Q[0][j]-K_Q[1][j]) for j in A)/2
    assert tvQ==F(1,2)
    result={
        'schema':'EM_R1_LR_FIBER_N3_EXACT_V1',
        'status':'AUTHOR_EXACT_FINITE_WITNESS',
        'horizon':3,'alphabet':[0,1,2],'ordered_prefix_count':len(paths),
        'positive_and_normalized':True,'state_update_deterministic':True,
        'likelihood_ratio_constant_on_every_x_fiber':True,
        'source_laws_distinct':True,
        'time1_PQ':['1/3','1/3','1/3'],
        'time2_PQ':['1/3','1/3','1/3'],
        'time3_P':{str(i):[rat(z) for z in K_P[i]] for i in A},
        'time3_Q':{str(i):[rat(z) for z in K_Q[i]] for i in A},
        'time3_Q_over_P_by_last_symbol':[rat(z) for z in R],
        'time2_predecessor_Q_TV':rat(tvQ),
        'counterexample':results,
        'proof_scope':'Excluded midpoint by forced t1+t2 actions; N<=2 convexity is mathematical proof, not finite computation'
    }
    return result

if __name__ == '__main__':
    print(json.dumps(check(),indent=2,ensure_ascii=False,sort_keys=True))
