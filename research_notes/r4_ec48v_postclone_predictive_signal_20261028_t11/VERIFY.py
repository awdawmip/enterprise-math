#!/usr/bin/env python3
"""EC48V: exact finite positive source-neutral clone / sequential stopping certificate.
Python standard-library fractions only. No float arithmetic and no external API.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

ZERO, ONE = F(0), F(1)
C = F(1, 8)
H = ('A', 'B')
J = (0, 1)
Z = (0, 1)
w = {'A': F(1, 2), 'B': F(1, 2)}
r = {('A', 1): F(3, 4), ('B', 1): F(1, 4)}
r[('A', 0)], r[('B', 0)] = ONE-r[('A', 1)], ONE-r[('B', 1)]
pz = {('A', 1): F(3, 4), ('B', 1): F(1, 2)}
qz = {('A', 1): F(1, 4), ('B', 1): F(1, 2)}
for h in H:
    pz[(h, 0)], qz[(h, 0)] = ONE-pz[(h, 1)], ONE-qz[(h, 1)]

LEAVES = []
for h, j, z in product(H, J, Z):
    p = w[h] * r[(h,j)] * pz[(h,z)]
    q = w[h] * r[(h,j)] * qz[(h,z)]
    assert p > 0 and q > 0
    L = p / q
    assert L == pz[(h,z)] / qz[(h,z)]
    LEAVES.append((h,j,z,p,q,L))
assert sum((x[3] for x in LEAVES), ZERO) == ONE
assert sum((x[4] for x in LEAVES), ZERO) == ONE
assert all(sum((w[h]*r[(h,j)] for h in H), ZERO) == F(1,2) for j in J)


def key(leaf, mode):
    h,j,z,p,q,L=leaf
    if mode=='old': return (z,L)
    if mode=='refined-erased': return (z,L)
    if mode=='refined-retained': return (j,z,L)
    if mode=='full': return (h,j,z)
    raise ValueError(mode)


def group(leaf, mode):
    h,j,z,p,q,L=leaf
    if mode=='old': return '*'
    if mode=='full': return (h,j)
    return j


def vec(early, terminal, mode):
    # Early action is S0 (stop+reject), S1 (stop+accept), C (continue).
    a,b,tp,tq=ZERO,ZERO,ONE,ONE
    for x in LEAVES:
        h,j,z,p,q,L=x
        act=early[group(x,mode)]
        if act=='C':
            tp+=p; tq+=q
            accepted=terminal[key(x,mode)]
        else: accepted=(act=='S1')
        if accepted:
            a+=p; b+=q
    return a,b,tp,tq


def val(v, cost=C):
    return v[0]-v[1]-cost*(v[2]+v[3])


def exhaustive(mode, cost=C):
    groups=sorted({group(x,mode) for x in LEAVES},key=str)
    keys=sorted({key(x,mode) for x in LEAVES},key=str)
    optimum=None; winner=None; count=0
    for acts in product(('S0','S1','C'), repeat=len(groups)):
        early=dict(zip(groups,acts))
        for accept in product((False, True), repeat=len(keys)):
            terminal=dict(zip(keys,accept))
            v=vec(early, terminal, mode)
            value=val(v,cost)
            count+=1
            if optimum is None or value>optimum:
                optimum, winner=value,(early,terminal,v)
    return optimum,winner,count


def analytical_gains():
    G={j:sum((w[h]*r[(h,j)]*max(ZERO,pz[(h,z)]-qz[(h,z)]) for h in H for z in Z),ZERO) for j in J}
    W={j:sum((w[h]*r[(h,j)] for h in H),ZERO) for j in J}
    return G,W


def opt_from_gains(G,W,cost):
    refined = -2*cost+sum((max(ZERO,G[j]-2*cost*W[j]) for j in G),ZERO)
    old = -2*cost+max(ZERO,sum(G.values(),ZERO)-2*cost)
    return old, refined


G,W=analytical_gains()
assert G=={0:F(1,16),1:F(3,16)}
assert W=={0:F(1,2),1:F(1,2)}
old_formula, ref_formula=opt_from_gains(G,W,C)
assert (old_formula,ref_formula)==(-F(1,4),-F(3,16))
exh={}
for mode in ('old','refined-erased','refined-retained','full'):
    best,winning,count=exhaustive(mode)
    exh[mode]={'optimal':str(best),'count':count,'witness_vec':list(map(str,winning[2]))}
    expect={'old':-F(1,4),'refined-erased':-F(3,16),'refined-retained':-F(3,16),'full':-F(1,8)}[mode]
    assert best==expect,(mode,best,expect)

# Explicit refined witness: stop J=0 (reject), continue J=1, accept if LR>1.
explicit=vec({0:'S0',1:'C'}, {key(x,'refined-erased'):(x[5]>ONE) for x in LEAVES}, 'refined-erased')
assert explicit==(F(9,32),F(3,32),F(3,2),F(3,2))
assert val(explicit)==-F(3,16)

# Exact parametric value-of-information equality/strictness on seeded positive models.
# Each Q/P weight h is identical at the decision epoch; source distinction arises at future Z.
rng=Random(48022)
trials=500
strict_trials=0
for t in range(trials):
    n_h=2+rng.randrange(3)
    n_j=2+rng.randrange(3)
    # Each row of integer weights is normalized into positive rational probabilities.
    def norm(a):
        s=sum(a)
        return [F(x,s) for x in a]
    ww=norm([rng.randint(1,9) for _ in range(n_h)])
    rr=[norm([rng.randint(1,9) for _ in range(n_j)]) for _ in range(n_h)]
    zzp=[norm([rng.randint(1,9) for _ in range(2)]) for _ in range(n_h)]
    zzq=[norm([rng.randint(1,9) for _ in range(2)]) for _ in range(n_h)]
    gm={j:sum((ww[h]*rr[h][j]*max(ZERO,zzp[h][z]-zzq[h][z]) for h in range(n_h) for z in range(2)),ZERO) for j in range(n_j)}
    wm={j:sum((ww[h]*rr[h][j] for h in range(n_h)),ZERO) for j in range(n_j)}
    cost=F(rng.randrange(1,30),100)
    old,ref=opt_from_gains(gm,wm,cost)
    assert ref>=old
    # Verify the independent mixed-sign characterization.
    b=[gm[j]-2*cost*wm[j] for j in range(n_j)]
    assert (ref>old)==(max(b)>ZERO and min(b)<ZERO)
    if ref>old:strict_trials+=1

report={
  'schema':'EM_EC48V_EXACT_CERTIFICATE_V1',
  'date':'2026-10-28',
  'scope':'Auxiliary finite strictly positive dual-source BRC; one middle stop/continue decision; full controlled-history LR at each stage; terminal acceptance; no native X6 claim.',
  'terminal_leaf_count':len(LEAVES),
  'source_mass_checks':{'P':'1','Q':'1','strict_positive':True},
  'j_weights':{str(j):str(W[j]) for j in J},
  'j_positive_accept_gains':{str(j):str(G[j]) for j in J},
  'cost':'1/8',
  'old_one_state_maximum':str(old_formula),
  'refined_one_state_maximum':str(ref_formula),
  'strict_support_gap':str(ref_formula-old_formula),
  'explicit_refined_vector':list(map(str,explicit)),
  'exhaustive_deterministic_controllers':exh,
  'randomized_model_checks':trials,
  'randomized_strict_gap_cases':strict_trials,
  'source_neutral_kernel':'r(J|H) identical under P,Q',
  'all_assertions':'PASS',
}
print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
