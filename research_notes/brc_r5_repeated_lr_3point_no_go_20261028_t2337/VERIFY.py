#!/usr/bin/env python3
"""Exact Fraction regression for the symmetric-three-signature repeated-LR no-go theorem.

The all-real statement is proved in RESEARCH.md, not inferred from this finite run.
No third-party dependencies.  Python 3.10+.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

R = F(3, 2)
L, H = F(1, 2), F(5, 2)
ARR = (F(1, 4), F(1, 4))
O_Q, O_LR = F(1, 2), F(1, 2)
P = (F(1, 8), F(1, 4))
Z = (F(13, 27), F(1, 3))
Q = tuple(1 - 2*p for p in P)


def kernel(t):
    assert 0 < t < F(1, 2)
    return (t, 1 - 2*t, t)


def check_model(p=P, z=Z):
    assert sum(ARR) + O_Q == 1
    assert R*sum(ARR) + O_Q*O_LR == 1
    for v in p + z:
        probs = kernel(v)
        assert sum(probs) == 1
        assert sum(x*y for x,y in zip((L,R,H), probs)) == R
        assert sum(x*y/R for x,y in zip((L,R,H), probs)) == 1
        assert all(x*y/R > 0 for x,y in zip((L,R,H), probs))


def coeffs(p=P,z=Z):
    return tuple((p_i+(1-2*p_i)*z_i)/(2-2*p_i) for p_i,z_i in zip(p,z))


def hinge(x,y,s):
    return min(x*s, y)


def deficit(x,y):
    v=2*hinge(x,y,R)-hinge(x,y,L)-hinge(x,y,H)
    assert v>=0
    return v


def actions(p,z,x,y,beta):
    d=deficit(x,y)
    q=1-2*p
    return (F(0), beta-p*d, (1+q)*beta-p*d-q*z*d)


def support_gap(p,z,x,y,beta):
    a=actions(p[0],z[0],x,y,beta)
    b=actions(p[1],z[1],x,y,beta)
    v_full=ARR[0]*min(a)+ARR[1]*min(b)
    v_lr=min(ARR[0]*a[i]+ARR[1]*b[i] for i in range(3))
    return v_lr-v_full


def source_events(m,p,z,alpha,gamma,source):
    q=1-2*p
    # Each tuple: source, time, likelihood ratio, Q mass
    return [(source,1,R,m*(1-alpha)),
            (source,2,L,m*alpha*p),(source,2,H,m*alpha*p),
            (source,2,R,m*alpha*q*(1-gamma)),
            (source,3,L,m*alpha*q*gamma*z),
            (source,3,H,m*alpha*q*gamma*z),
            (source,3,R,m*alpha*q*gamma*(1-2*z))]


def events(alphas,gammas):
    e=[('O',1,O_LR,O_Q)]
    for idx in range(2):
        e+=source_events(ARR[idx],P[idx],Z[idx],alphas[idx],gammas[idx],('A','B')[idx])
    assert sum(m for _,_,_,m in e)==1
    assert sum(s*m for _,_,s,m in e)==1
    return e


def observed(e,declare_p):
    return (sum(s*m*(1-declare_p[i]) for i,(_,_,s,m) in enumerate(e)),
            sum(m*declare_p[i] for i,(_,_,_,m) in enumerate(e)),
            sum(t*s*m for _,t,s,m in e),
            sum(t*m for _,t,_,m in e))


def flatten_exact(full_events, full_decisions):
    q_tail=sum(m for source,t,s,m in full_events if source!='O' and s==L)
    q_tail_H=sum(m for source,t,s,m in full_events if source!='O' and s==H)
    assert q_tail==q_tail_H
    # time increment in Q only for A/B, relative to the universal time-1 base.
    excess=sum((t-1)*m for source,t,s,m in full_events)
    kA,kB=coeffs()
    assert kA==kB==F(5,18)
    dmax=sum(ARR[i]*(1+Q[i]) for i in range(2))
    alpha=excess/dmax
    assert 0<=alpha<=1
    replica=events((alpha,alpha),(F(1),F(1)))
    qtail_lr=sum(m for src,t,s,m in replica if src!='O' and s==L)
    assert qtail_lr==kA*excess and qtail_lr>=q_tail
    theta=q_tail/qtail_lr if qtail_lr else F(0)
    # The arbitrary full-history decision rule is first Q-mass averaged by
    # terminal signature; the more-informative LR experiment is then garbled.
    masses={s:F(0) for s in (L,R,H)}
    chosen={s:F(0) for s in (L,R,H)}
    for i,(src,t,s,m) in enumerate(full_events):
        if src=='O':continue
        masses[s]+=m
        chosen[s]+=m*full_decisions[i]
    rules={s:(chosen[s]/masses[s] if masses[s] else F(0)) for s in (L,R,H)}
    converted={L:theta*rules[L]+(1-theta)*rules[R],
               H:theta*rules[H]+(1-theta)*rules[R],R:rules[R]}
    lr_rules=[full_decisions[0] if src=='O' else converted[s]
              for src,t,s,m in replica]
    assert all(0<=u<=1 for u in lr_rules)
    return replica,lr_rules,alpha,theta,qtail_lr,q_tail


def randfrac(rng):
    den=rng.randrange(2,49)
    return F(rng.randrange(den+1),den)


def main():
    check_model()
    assert P[0]!=P[1] and Z[0]!=Z[1]
    assert all(z>=p for p,z in zip(P,Z))
    assert coeffs()==(F(5,18),F(5,18))
    print('Strictly positive P/Q kernels: PASS')
    print('q_*= (3/4, 1/2), p=(1/8,1/4), z=(13/27,1/3), k=(5/18,5/18)')
    n=0
    for a,b,c in product(range(-3,4),range(-3,4),range(-16,17)):
        x,y,beta=F(a,2),F(b,2),F(c,12)
        assert support_gap(P,Z,x,y,beta)==0
        n+=1
    print(f'Exact signed Bellman support checks: {n} / {n} PASS')
    # Perturb only the second-level B kernel to break the common threshold.
    alternate=(Z[0],F(1,4))
    beta=F(19,72)
    assert support_gap(P,alternate,F(1),R,beta)==F(1,192)
    print('Independent perturbation strict support gap: 1/192 PASS')
    # Source-specific behavioral policy and terminal decisions.
    full_e=events((F(1),F(1,2)),(F(0),F(1,2)))
    full_rules=[F(1) if s==H else F(0) for src,t,s,m in full_e]
    got=observed(full_e,full_rules)
    assert got==(F(157,192),F(7,96),F(103,64),F(45,32)),got
    lr_e,lr_rules,alpha,theta,UL,UF=flatten_exact(full_e,full_rules)
    assert alpha==F(1,2) and theta==F(42,65)
    assert UF==F(7,96) and UL==F(65,576)
    assert observed(lr_e,lr_rules)==got
    print(f'Explicit full policy: O={got} ; LR alpha={alpha}, gamma=1, tail-garble theta={theta} PASS')
    rng=Random(20261028)
    for _ in range(1000):
        full_e=events((randfrac(rng),randfrac(rng)),
                      (randfrac(rng),randfrac(rng)))
        full_rules=[randfrac(rng) for i in range(len(full_e))]
        lr_e,lr_rules,*_ =flatten_exact(full_e,full_rules)
        assert observed(full_e,full_rules)==observed(lr_e,lr_rules)
    print('Exact full-policy to unseeded-LR constructive matching: 1000 / 1000 PASS')
    # Exhaustive classification of finite rational parameter grids,
    # using all breakpoints: each cell is an interval of affine functions.
    pars=[F(1,12),F(1,8),F(1,6),F(1,4),F(1,3),F(5,12)]
    total=0
    for pA,pB,zA,zB in product(pars,repeat=4):
        pp=(pA,pB); zz=(zA,zB)
        cA,cB=coeffs(pp,zz)
        same=((zA>=pA and zB>=pB and cA==cB)
              or (zA<pA and zB<pB and pA==pB and zA==zB))
        # For a hinge with D=1, action signs change only at its
        # pairwise affine intersections; testing the open intervals
        # gives an exact finite decision procedure for this fixed grid tuple.
        lines=[actions(pp[h],zz[h],F(1),R,F(0)) for h in range(2)]
        slopes=((F(0),F(1),1+(1-2*pA)),
                (F(0),F(1),1+(1-2*pB)))
        pts={F(-2),F(2)}
        for idx in range(2):
            v=lines[idx];s=slopes[idx]
            for i in range(3):
                for j in range(i+1,3):
                    if s[i]!=s[j]:pts.add((v[j]-v[i])/(s[i]-s[j]))
        bb=sorted(pts)
        tests=bb+[(bb[i]+bb[i+1])/2 for i in range(len(bb)-1)]
        ok=all(support_gap(pp,zz,F(1),R,b)==0 for b in tests)
        assert ok==same,(pp,zz,same,ok,tests)
        total+=1
    print(f'Exact three-action breakpoint classification checks: {total} / {total} PASS')
    print('PASS_EXACT_R5_REPEATED_LR_SYMMETRIC_THREE_SIGNATURE_NO_GO')

if __name__=='__main__':main()
