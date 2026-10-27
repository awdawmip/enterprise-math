#!/usr/bin/env python3
"""Exact finite rational certificate for R1 N=3 delayed ternary observer theorem."""
from fractions import Fraction as F
from itertools import product, combinations
import json

A = (0, 1, 2)
third_P = {
    0: (F(1, 4), F(1, 4), F(1, 2)),
    1: (F(1, 12), F(3, 4), F(1, 6)),
    2: (F(1, 6), F(1, 2), F(1, 3)),
}
R = (F(2), F(1), F(1, 2))
third_Q = {i: tuple(third_P[i][j] * R[j] for j in A) for i in A}

def f(x):
    x = F(x)
    return str(x.numerator) + '/' + str(x.denominator)

def p(h):
    if len(h) == 0: return F(1)
    if len(h) == 1: return F(1,3)
    if len(h) == 2: return F(1,9)
    return F(1,9) * third_P[h[0]][h[2]]

def q(h):
    if len(h) < 3: return p(h)
    return R[h[2]] * p(h)

def z(h):
    if len(h) == 0: return (0, 'root')
    if len(h) in (1,2): return (len(h),h[0])
    return (3,h[2])

H={t:list(product(A,repeat=t)) for t in range(4)}
assert sum(len(H[t]) for t in range(4)) == 40
for i in A:
    assert sum(third_P[i]) == sum(third_Q[i]) == 1
    assert all(v > 0 for v in third_P[i] + third_Q[i])
for t in range(4):
    for h in H[t]:
        assert p(h)>0 and q(h)>0
        if t<3:
            assert sum(p(h+(a,)) for a in A) == p(h)
            assert sum(q(h+(a,)) for a in A) == q(h)
assert sum(p(h) for h in H[3]) == sum(q(h) for h in H[3]) == 1
# Ratio is constant on each state fiber.
ratios={}
for t in range(4):
    for h in H[t]:
        ratios.setdefault(z(h), set()).add(q(h)/p(h))
assert all(len(v)==1 for v in ratios.values())
assert [len(set(z(h) for h in H[t])) for t in range(4)] == [1,3,3,3]
# Exact strong lumpability under P,Q (labeled observed states).
for t in range(3):
    for h,g in combinations(H[t],2):
        if z(h) != z(g): continue
        for prob in (p,q):
            next_states=set(z(h+(a,)) for a in A)|set(z(g+(a,)) for a in A)
            for v in next_states:
                kh=sum(prob(h+(a,))/prob(h) for a in A if z(h+(a,))==v)
                kg=sum(prob(g+(a,))/prob(g) for a in A if z(g+(a,))==v)
                assert kh == kg
# The N=3 penultimate call profile distinguishes first-symbol types.
call={i: sum(third_P[i][j]*max(R[j]-F(1),F(0)) for j in A) for i in A}
assert call == {0:F(1,4),1:F(1,12),2:F(1,6)}

# Two full-history policies: continue at t=2 iff first symbol in selected group,
# decide D=1 at t=3 iff last symbol 0; otherwise terminate with D=0.
def witness(sel,prob):
    m=sum(prob((i,k)) for i,k in H[2] if i in sel)
    p31=sum(prob((i,k,j)) for i,k,j in H[3] if i in sel and j==0)
    return {"T2_D0": 1-m, "T3_D1":p31,"T3_D0":m-p31}
results=[]
thresholds=[(F(5,24),(0,)), (F(1,8),(0,2))]
for theta,sel in thresholds:
    xp,xq=witness(sel,p),witness(sel,q)
    m=xp['T3_D1']+xp['T3_D0']
    assert m==xq['T3_D1']+xq['T3_D0']
    contrast=xq['T3_D1']-xp['T3_D1']
    assert contrast==sum(p((i,k))*call[i] for i,k in H[2] if i in sel)
    results.append({"threshold":f(theta),"select_first_symbols":list(sel),"P":{key:f(val) for key,val in xp.items()},"Q":{key:f(val) for key,val in xq.items()},"m":f(m),"contrast_Q_minus_P":f(contrast)})
assert results[0]['m']=='1/3' and results[0]['contrast_Q_minus_P']=='1/12'
assert results[1]['m']=='2/3' and results[1]['contrast_Q_minus_P']=='5/36'
# Every pair of t=2 histories with differing first symbols is separated by
# one of the two threshold witnesses. This computes the pairwise Lagrange regret
# lower bound valid for ALL real continuation probabilities sharing a state.
cert=[]
for i,g in combinations(A,2):
    theta = F(5,24) if (i==0 or g==0) else F(1,8)
    high,low=(i,g) if call[i]>call[g] else (g,i)
    assert call[high] > theta > call[low]
    regret = min(F(1,9)*(call[high]-theta),F(1,9)*(theta-call[low]))
    assert regret>=F(1,216)
    cert.append({'first_symbols':[i,g], 'threshold':f(theta), 'worst_pairwise_gap_lower_bound':f(regret), 'pair_count':9})

payload={
'schema':'EM_R1_N3_DELAYED_OBSERVER_UNIQUENESS_RATIONAL_V1',
'classification':'AUTHOR_EXACT_FRACTION_CHECK_NOT_NATIVE_RESULT',
'prefix_counts_by_depth':[len(H[t]) for t in range(4)],
'quotient_states_by_depth':[len(set(z(h) for h in H[t])) for t in range(4)],
'P_final_rows':[[f(x) for x in third_P[i]] for i in A],
'Q_final_rows':[[f(x) for x in third_Q[i]] for i in A],
'likelihood_ratio_by_final_symbol':[f(x) for x in R],
'penultimate_A_at_lambda_1':[f(call[i]) for i in A],
'witnesses':results,
'forbidden_cross_type_merges':cert,
'number_of_cross_type_pairs':27,
'minimum_regret_certified':'1/216',
'coverage':'40 prefixes, 27 cross-first-type pairs, both laws, exact Fraction; general all-policy statement by mathematical proof',
'status':'PASS_EXACT_RATIONAL'}
print(json.dumps(payload,ensure_ascii=False,indent=2,sort_keys=True))
