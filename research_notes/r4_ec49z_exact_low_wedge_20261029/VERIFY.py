#!/usr/bin/env python3
"""EC49Z exact low-discrimination section certificate.

All arithmetic uses Python's Fraction (no float rounding). Checks the full
18-leaf positive source laws, a fixed causal/unseeded 3-history prefix and
selected exact points on two policy families; the all-real theorem is proved
in PROOF.md (not extrapolated from these checks).
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

W = range(3)
U = range(2)
Z = range(3)
C = range(4)  # A0, A1, B0, B1
SIGMA = (1, 0, -1)
ETA = F(1, 200)
B = F(1, 16)
DELTA0 = F(17, 288)
DELTA_STAR = F(59, 576)  # EC49X independent global optimum
COST1 = F(43, 48)
COST2 = F(7, 8)

# Each row is a conditional distribution of the first paid action given W.
# The leftover is STOP. W2 may stop with probability 3/8.
X = (
    (F(1), F(0), F(0), F(0)),
    (F(0), F(1), F(0), F(0)),
    (F(0), F(9, 16), F(1, 16), F(0)),
)


def signal(w, u):
    return F(1, 2) + (2 * u - 1) * ETA * SIGMA[w]


def joint(source, w, u, z):
    p = F(1, 9) if source == 'Q' else (F(1, 6) if w == z else F(1, 12))
    return p * signal(w, u)


def is_pure_diagonal_paid(c, z):
    return (c, z) in ((0, 0), (2, 2))


def is_pure_off_diagonal_paid(c, z):
    return (c == 0 and z != 0) or (c == 2 and z != 2)


def accept_prob(c, z, strength, blend):
    """Blend low/high endpoints at a common fixed delta.

    blend=1 -> low policy: accept pure diagonal with strength.
    blend=0 -> high policy: accept all, reject pure offdiagonal with strength.
    Crucially, blending happens in each terminal Bernoulli probability,
    with no ex-ante seed persistent across decisions.
    """
    low = strength if is_pure_diagonal_paid(c, z) else F(0)
    high = F(1) - (strength if is_pure_off_diagonal_paid(c, z) else F(0))
    return blend * low + (1 - blend) * high


def global_high_prob(c, z, strength):
    """Reject all z absent from a paid code's W support with strength.

    A0 supports {0}, A1 supports {1,2}, B0 supports {2}. All
    these rejected atoms have exact source likelihood ratio 3/4.
    """
    off_support = is_pure_off_diagonal_paid(c, z) or (c == 1 and z == 0)
    return F(1) - (strength if off_support else F(0))


def evaluate_global_high(strength):
    assert 0 <= strength <= 1
    mass = {}
    for source in ('P','Q'):
        stopping = sum(F(1,3)*(1-sum(X[w])) for w in W)
        paid = sum(X[w][c]*joint(source,w,u,z)*global_high_prob(c,z,strength)
                   for w,c,u,z in product(W,C,U,Z))
        mass[source] = stopping+paid
    return mass['P'],mass['Q']


def evaluate(strength, blend):
    assert 0 <= strength <= 1 and 0 <= blend <= 1
    p = {}
    for source in ('P', 'Q'):
        # STOP acceptance is strength-independent for endpoint mixing:
        # low STOP=0, high STOP=1.
        stopping = sum(F(1, 3) * (1-sum(X[w])) * (1-blend) for w in W)
        paying = sum(
            X[w][c] * joint(source, w, u, z) * accept_prob(c, z, strength, blend)
            for w, c, u, z in product(W, C, U, Z)
        )
        p[source] = stopping + paying
    c1 = sum(F(1, 3) * X[w][c] * (1 if c < 2 else 2) for w, c in product(W, C))
    c2 = sum(F(1, 3) * X[w][c] for w, c in product(W, C))
    return p['P'], p['Q'], c1, c2


def check():
    assert all(sum(X[w]) <= 1 for w in W)
    assert all(signal(w, u)>0 for w,u in product(W,U))
    for source in ('P', 'Q'):
        leaves = [joint(source, w, u, z) for w, u, z in product(W,U,Z)]
        assert len(leaves)==18 and min(leaves)>0 and sum(leaves)==1
        assert all(sum(joint(source,w,u,z) for u,z in product(U,Z))==F(1,3) for w in W)

    pairs=[]
    for d in (F(0), F(1, 36), F(1, 18), DELTA0):
        strength=d/DELTA0
        for blend in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            a,b,c1,c2=evaluate(strength,blend)
            assert c1==COST1 and c2==COST2
            assert a-b==d
            assert a==blend*(3*d)+(1-blend)*(1-3*d)
            assert b==a-d
            assert 3*d <= a <= 1-3*d
            pairs.append({'delta':str(d),'blend':str(blend),'alpha':str(a),'beta':str(b)})
    upper_global=[]
    for d in (F(0), F(1,18), F(1,16), F(1,12), DELTA_STAR):
        a,b = evaluate_global_high(d/DELTA_STAR)
        assert a==1-3*d and b==1-4*d and a-b==d
        upper_global.append({'delta':str(d),'alpha':str(a),'beta':str(b)})
    assert evaluate_global_high(F(1)) == (F(133,192), F(85,144))
    # Pure codes A0 and B0 carry paid prefix mass exactly 17/16.
    puremass=sum(X[w][c] for w,c in ((0,0),(2,2)))
    assert puremass==F(17,16) and puremass/18==DELTA0
    assert all(X[w][0]==0 for w in (1,2))
    assert all(X[w][2]==0 for w in (0,1))
    a,b,c1,c2=evaluate(F(1),F(1))
    assert (a,b)==(F(17,96),F(17,144))
    a,b,c1,c2=evaluate(F(1),F(0))
    assert (a,b)==(F(79,96),F(55,72))
    assert a-b==DELTA0
    report={
        'schema':'EC49Z_EXACT_BEHAVIORAL_WEDGE_V1',
        'status':'AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED',
        'source_laws':'EC49Y: 18 strictly positive rational (w,u,z) leaves per P/Q',
        'eta':'1/200','stage_costs':{'C1':'43/48','C2':'7/8'},
        'theorem':{'delta_domain':'0 <= delta <= 17/288',
                   'exact_alpha_section':'[3*delta, 1-3*delta]',
                   'beta':'alpha-delta',
                   'lower_boundary_saturation_impossible_beyond_threshold':'For delta > 17/288, alpha=3delta is impossible',
                   'upper_boundary_all_the_way':'alpha=1-3delta attained for 0<=delta<=59/576'},
        'fixed_prefix':[[str(v) for v in row] for row in X],
        'strength':'delta/(17/288)',
        'policy_interpolation':'terminal-state fresh coins, no persistent shared seed',
        'checks':{'positive_leaf_checks_per_source':18,'exact_section_points':len(pairs),'global_upper_points':len(upper_global),
                  'pure_paid_prefix_mass':'17/16', 'all_assertions_passed':True},
        'sample_points':pairs,'global_upper_samples':upper_global,
        'scope':'Exact single submaximal sector, not complete fixed-cost acceptance image or native signed BRC'
    }
    folder=Path(__file__).resolve().parent
    (folder/'EXACT_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
    print('EC49Z FRACTION PASS; section points',len(pairs),'; lower sharpness threshold',DELTA0, '; upper reaches',DELTA_STAR,'; sample δ=1/18: alpha in',[F(1,6),F(5,6)])

if __name__=='__main__':
    check()
