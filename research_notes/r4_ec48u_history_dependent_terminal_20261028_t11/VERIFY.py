#!/usr/bin/env python3
from fractions import Fraction as F
from collections import defaultdict
from random import Random
import json
rng=Random(48021)
def positive_simplex(n):
    xs=[F(rng.randrange(1,8)) for _ in range(n)]
    return [v/sum(xs) for v in xs]
def random_fraction():
    return F(rng.randrange(1,8),8)
def exact_trial():
    n,ni,nm,nj=(rng.randrange(2,7),rng.randrange(1,4),rng.randrange(1,4),rng.randrange(2,5))
    ph,qh=positive_simplex(n),positive_simplex(n)
    s,u=[random_fraction() for _ in range(n)],[random_fraction() for _ in range(n)]
    bp,bq=[positive_simplex(ni) for _ in range(n)],[positive_simplex(ni) for _ in range(n)]
    mem=[positive_simplex(nm) for _ in range(n)]
    clone=[[[positive_simplex(nj) for m in range(nm)] for i in range(ni)] for h in range(n)]
    lr=[[ph[h]*bp[h][i]/(qh[h]*bq[h][i]) for i in range(ni)] for h in range(n)]
    keys=set((m,i,lr[h][i],j) for h in range(n) for m in range(nm) for i in range(ni) for j in range(nj))
    accept={key:random_fraction() for key in keys}
    finep,fineq=F(0),F(0)
    groups=defaultdict(lambda:[F(0),F(0)])
    for h in range(n):
        for i in range(ni):
            for m in range(nm):
                q=qh[h]*(1-s[h])*bq[h][i]*mem[h][m]
                p=ph[h]*(1-s[h])*bp[h][i]*mem[h][m]
                assert p==lr[h][i]*q
                a=sum((clone[h][i][m][j]*accept[m,i,lr[h][i],j] for j in range(nj)),F(0))
                finep+=p*a; fineq+=q*a
                groups[m,i,lr[h][i]][0]+=q
                groups[m,i,lr[h][i]][1]+=q*a
    oldp,oldq=F(0),F(0)
    for (m,i,L),(massQ,accQ) in groups.items():
        a=accQ/massQ
        assert F(0)<=a<=F(1)
        oldq+=massQ*a
        oldp+=L*massQ*a
    earlyp=sum((ph[h]*s[h]*u[h] for h in range(n)),F(0))
    earlyq=sum((qh[h]*s[h]*u[h] for h in range(n)),F(0))
    tp=sum((ph[h]*(2-s[h]) for h in range(n)),F(0))
    tq=sum((qh[h]*(2-s[h]) for h in range(n)),F(0))
    assert (earlyp+finep,earlyq+fineq,tp,tq)==(earlyp+oldp,earlyq+oldq,tp,tq)
    return any(sum(lr[h][i]==L for h in range(n))>1 for i in range(ni) for L in set(lr[h][i] for h in range(n)))
N=750
collisions=sum(exact_trial() for _ in range(N))
p=(F(3,4),F(1,4));q=(F(1,4),F(3,4));r1=(F(3,4),F(1,4))
p1=sum((p[h]*r1[h] for h in range(2)),F(0))
q1=sum((q[h]*r1[h] for h in range(2)),F(0))
assert (p1,q1)==(F(5,8),F(3,8)) and p1-q1==F(1,4)
assert sum(p)==sum(q)==1 and (p[0]/q[0],p[1]/q[1])==(3,F(1,3))
common=(F(1,2),F(1,2));rstrong=(F(3,4),F(1,4))
real=common[0]*rstrong[0]+common[1]*(1-rstrong[1])
assert real==F(3,4)
for numerator in range(9):
    u=F(numerator,8)
    simulated=common[0]*u+common[1]*(1-u)
    assert simulated==F(1,2)
report={
 "schema":"EM_EC48U_EXACT_V1","all_assertions":"PASS",
 "random_seed":48021,"source_neutral_positive_rational_trees_checked":N,
 "full_joint_lr_collision_trials":collisions,
 "four_coordinate_fiber_reconstructions":"PASS",
 "coarse_lr_counterexample":{"p_h":["3/4","1/4"],"q_h":["1/4","3/4"],"r_j1_given_h":["3/4","1/4"],"refined_accept_j1":[str(p1),str(q1)],"exact_support_gap":"1/4","old_coarse_lr":"1","old_full_history_lr":["3","1/3"]},
 "future_relation_counterexample":{"p_h":["1/2","1/2"],"q_h":["1/2","1/2"],"full_lr":["1","1"],"r_j1_given_h":["3/4","1/4"],"true_P_j_equals_h":"3/4","best_observable_fiber_sampler_P_j_equals_h":"1/2","joint_correlation_gap":"1/4"},
 "scope":"finite positive two-source trees, terminal-only acceptance; finite checks are not universal proof"
}
print(json.dumps(report,indent=2,sort_keys=True))
