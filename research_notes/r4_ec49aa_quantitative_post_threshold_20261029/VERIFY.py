#!/usr/bin/env python3
"""EC49AA: exact rational bound constants and a post-threshold behavioral witness.

No floating-point arithmetic is used; universal inequality is in PROOF.md.
This program verifies the finite source and the explicit causal policy.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

W=range(3); U=range(2); Z=range(3); C=range(4)
ETA=F(1,200)
X=((F(1),F(0),F(0),F(0)),
   (F(0),F(1),F(0),F(0)),
   (F(0),F(9,16),F(1,16),F(0)))
D0=F(17,288)
D_TARGET=F(1,16)
TAU_STAR=F(9,32)*F(99,101)
T_RATIO=F(101,99)
LOWER=F(3)*D_TARGET+3*TAU_STAR*(D_TARGET-D0)
UPPER=F(9,46)
EXTRA=F(2,23)


def t(w,u):
    return F(1,2)+(2*u-1)*ETA*(1-w)


def mass(source,w,u,z):
    joint=F(1,9) if source=='Q' else (F(1,6) if w==z else F(1,12))
    return joint*t(w,u)


def a_paid(c,u,z):
    # no persistent seed: a single fresh Bernoulli at (c,u,z)
    if (c,z) in ((0,0),(2,2)):
        return F(1)
    if (c,z)==(1,1):
        return EXTRA
    return F(0)


def main():
    assert 0<ETA<F(1,2)
    assert min(t(w,u) for w,u in product(W,U))==F(99,200)
    assert max(t(w,u) for w,u in product(W,U))==F(101,200)
    assert TAU_STAR==F(891,3232)
    assert 2*TAU_STAR*T_RATIO==F(9,16)
    assert 0 < D_TARGET-D0 == F(1,288)
    assert LOWER==F(19689,103424)
    assert F(3,16)<LOWER<UPPER<F(1)-3*D_TARGET
    assert all(sum(X[w])<=1 for w in W)

    # Original two-source 18-leaf strictly positive model.
    for source in ('P','Q'):
        leaves=[mass(source,w,u,z) for w,u,z in product(W,U,Z)]
        assert len(leaves)==18 and all(x>0 for x in leaves)
        assert sum(leaves)==1
        for w in W:
            assert sum(mass(source,w,u,z) for u,z in product(U,Z))==F(1,3)

    b=sum(X[w][c] for w in W for c in (2,3))
    paid=sum(X[w][c] for w,c in product(W,C))
    stop=3-paid
    c1=(paid+b)/3
    c2=paid/3 # every paid prefix buys S
    assert b==F(1,16)
    assert paid==F(21,8)
    assert stop==F(3,8)
    assert (c1,c2)==(F(43,48),F(7,8))

    result={}
    for source in ('P','Q'):
        accepted=sum(X[w][c]*mass(source,w,u,z)*a_paid(c,u,z)
                     for w,c,u,z in product(W,C,U,Z))
        # The stopped histories are rejected; there is no no-S branch.
        result[source]=accepted
    alpha,beta=result['P'],result['Q']
    assert (alpha,beta)==(UPPER,F(49,368))
    assert alpha-beta==D_TARGET
    assert alpha-3*D_TARGET==F(3,368)
    assert D0<F(1,16)<F(59,576)
    # Direct aggregate check of A1 z1 weight (before acceptance thinning).
    p_a1_z1=sum(X[w][1]*mass('P',w,u,1) for w,u in product(W,U))
    q_a1_z1=sum(X[w][1]*mass('Q',w,u,1) for w,u in product(W,U))
    assert (p_a1_z1,q_a1_z1)==(F(41,192),F(25,144))
    assert EXTRA*(p_a1_z1-q_a1_z1)==F(1,288)

    report={
       'schema':'EC49AA_POST_THRESHOLD_QUANTITATIVE_BOUND_V1',
       'status':'AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED',
       'source_laws':{'P':'1/6 when w=z, 1/12 otherwise; times t_w(u)',
                      'Q':'1/9 for every w,z; times t_w(u)',
                      't_w(u)':'1/2 + (2u-1)*(1-w)/200',
                      'leaves_per_source':18},
       'bounds':{'delta':'1/16','pure_threshold':'17/288',
                 'tau_limit':str(TAU_STAR),'t_max_over_min':str(T_RATIO),
                 'universal_alpha_lower':str(LOWER),
                 'witness_alpha_upper':str(UPPER),
                 'witness_beta':str(beta),
                 'global_tradeoff':'alpha >= 3*delta + (2673/3232)*max(0,delta-17/288)'},
       'witness':{'prefix_x':[[str(v) for v in row] for row in X],
                  's':'always buy S', 'terminal_rule':'accept (A0,z0) or (B0,z2) with probability 1, (A1,z1) with probability 2/23, else 0',
                  'stage_cost_P_Q':{'C1':'43/48','C2':'7/8'},
                  'alpha':str(alpha),'beta':str(beta),'delta':str(alpha-beta)},
       'checks':{'exact_positive_source_leaves_per_source':18,
                 'normalization':True, 'costs':True, 'acceptance_pair':True,
                 'threshold_identity':True,'all_assertions_passed':True},
       'proof_scope':'Universal all-real bound by analytical near-pure cylinder lemma; computation only checks the explicit exact witness and constant identities.',
       'open':'Exact global alpha_min at delta=1/16 remains unresolved.'
    }
    output=Path(__file__).with_name('EXACT_REPORT.json')
    output.write_text(json.dumps(report,sort_keys=True,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('EC49AA Fraction PASS', 'tau*=',TAU_STAR,'lower=',LOWER,'upper=',UPPER,
          '(alpha,beta)=',(alpha,beta),'delta=',alpha-beta)

if __name__=='__main__':
    main()
