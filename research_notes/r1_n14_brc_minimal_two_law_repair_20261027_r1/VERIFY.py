#!/usr/bin/env python3
"""Exact BRC ordered-branch minimal LR/SL/right-congruence repair checker.

External finite non-IID two-law probability model, not native P000 physics.
"""
import itertools
import json
from collections import defaultdict
from fractions import Fraction as F

A = (0, 1, 2)
N = 3
U = (F(1, 3),) * 3
KP = {
    0: (F(1, 4), F(1, 4), F(1, 2)),
    1: (F(1, 12), F(3, 4), F(1, 6)),
    2: (F(1, 6), F(1, 2), F(1, 3)),
}
R = (F(2), F(1), F(1, 2))
KQ = {i: tuple(KP[i][j]*R[j] for j in A) for i in A}
LEVEL = {t: tuple(itertools.product(A, repeat=t)) for t in range(N+1)}

def cond(h, law):
    return U if len(h)<2 else (KP if law=="P" else KQ)[h[0]]

def mass(h, law):
    p = F(1)
    for t,a in enumerate(h): p *= cond(h[:t], law)[a]
    return p

def x(h):
    t=len(h)
    if t==0: return (0,"root")
    if t==1: return (1,h[0])
    if t==2: return (2,"*")
    return (3,h[-1])

def lr(h): return mass(h,"Q")/mass(h,"P")

def aggregate(h,law,class_next):
    out=defaultdict(F)
    for a,w in zip(A,cond(h,law)):
        out[class_next[h+(a,)]]+=w
    return tuple(sorted(out.items()))

# Construct bottom-up the coarsest partition with labeled right congruence,
# LR constancy and strong lumpability for both P/Q.
classes={}
signatures={}
by_time={}
for t in range(N,-1,-1):
    sig_to_id={}
    by_time[t]=defaultdict(list)
    for h in LEVEL[t]:
        children=tuple(classes[h+(a,)] for a in A) if t<N else ()
        ps=aggregate(h,"P",classes) if t<N else ()
        qs=aggregate(h,"Q",classes) if t<N else ()
        sig=(x(h),lr(h),children,ps,qs)
        if sig not in sig_to_id: sig_to_id[sig]=len(sig_to_id)
        cid=sig_to_id[sig]
        classes[h]=(t,cid)
        signatures[h]=sig
        by_time[t][cid].append(h)

# Proof-condition exhaustiveness: every pair of histories of each class.
for t in range(N+1):
    for members in by_time[t].values():
        for h in members:
            for g in members:
                assert x(h)==x(g) and lr(h)==lr(g)
                if t<N:
                    assert all(classes[h+(a,)]==classes[g+(a,)] for a in A)
                    assert aggregate(h,"P",classes)==aggregate(g,"P",classes)
                    assert aggregate(h,"Q",classes)==aggregate(g,"Q",classes)
                    for dest,wp in aggregate(h,"P",classes):
                        r_child=lr(next(h+(a,) for a in A if classes[h+(a,)]==dest))
                        wq=dict(aggregate(h,"Q",classes))[dest]
                        assert lr(h)*wq==r_child*wp

# The strict refinement at time two is forced by the three pairwise-distinct
# probabilities to terminal class last-symbol 0; all same-first histories merge.
rowP={i:tuple(str(v) for v in KP[i]) for i in A}
rowQ={i:tuple(str(v) for v in KQ[i]) for i in A}
assert len({KP[i][0] for i in A})==3
assert sorted(len(m) for m in by_time[2].values())==[3,3,3]
assert sorted(len(m) for m in by_time[3].values())==[9,9,9]
assert [len(by_time[t]) for t in range(N+1)]==[1,3,3,3]

# Exact two-law Markovization test using a nontrivial full-history policy.
def actions(h):
    t=len(h)
    if t==0: return (F(0),F(0),F(1))
    if t==1:
        c=(F(1,2), F(2,3), F(1,3))[h[0]]
        d=F(h[0]+1,5)
    elif t==2:
        c=F(1+(h[0]+2*h[1])%4,5)
        d=F((h[0]+h[1])%3,4)
    else:
        c=F(0)
        d=F((h[0]+2*h[1]+h[2])%5,6)
    return ((1-c)*(1-d),(1-c)*d,c)

def outputs(law, action_fn):
    out=defaultdict(F)
    survival={():F(1)}
    for t in range(N+1):
        for h in LEVEL[t]:
            w=survival[h]*mass(h,law)
            a0,a1,c=action_fn(h)
            assert a0+a1+c==1 and (t<N or c==0)
            out[(t,classes[h],0)]+=w*a0
            out[(t,classes[h],1)]+=w*a1
            if t<N:
                for a in A: survival[h+(a,)]=survival[h]*c
    return {str(k):v for k,v in sorted(out.items())}

# Weight full-history actions by survival-mass under P (not unweighted mean).
survival={():F(1)}
den=defaultdict(F)
num=defaultdict(lambda: [F(0),F(0),F(0)])
for t in range(N+1):
    for h in LEVEL[t]:
        w=survival[h]*mass(h,"P")
        k=classes[h]
        den[k]+=w
        a=actions(h)
        for d in range(3): num[k][d]+=w*a[d]
        if t<N:
            for letter in A: survival[h+(letter,)]=survival[h]*a[2]
compressed={key:tuple(z/den[key] for z in values) for key,values in num.items()}
assert all(sum(v)==1 for v in compressed.values())
for law in ("P","Q"):
    assert outputs(law,actions)==outputs(law,lambda h:compressed[classes[h]])

# Verify law-independence of the compressed mixture at every time/state.
for t in range(N+1):
    for cls,members in by_time[t].items():
        if len(members)>1:
            wP=sum((mass(h,"P")*survival[h] for h in members),F(0))
            wQ=sum((mass(h,"Q")*survival[h] for h in members),F(0))
            assert wQ==lr(members[0])*wP

result={
    "schema":"EM_R1_N14_MINIMAL_PREDICTIVE_REPAIR_EXACT_V1",
    "status":"PASS_EXACT_FRACTION",
    "model":"strictly positive non-IID two-law 3-symbol 3-draw finite tree",
    "prefix_count":sum(map(len,LEVEL.values())),
    "old_x_time_profile":[1,3,1,3],
    "minimal_LR_SL_right_congruence_time_profile":[len(by_time[t]) for t in range(N+1)],
    "minimal_total_states":sum(len(by_time[t]) for t in range(N+1)),
    "full_ordered_history_states":sum(map(len,LEVEL.values())),
    "time2_class_to_first_symbol":{str(cid):by_time[2][cid][0][0] for cid in by_time[2]},
    "time2_conditional_P_rows":rowP,
    "time2_conditional_Q_rows":rowQ,
    "terminal_LR_by_last_symbol":{str(j):str(R[j]) for j in A},
    "full_policy_two_law_markovization":True,
    "verified_scope":"all 40 paths, all within-state ordered pairs, both law kernels, one nontrivial full-history policy; coarsest uniqueness supplied separately by mathematical proof"
}
print(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False))
