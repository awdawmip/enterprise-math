#!/usr/bin/env python3
"""Exact finite sanity checks for the IID LR-fiber observer-preserving convexity theorem.

No numerical tolerances; every weight and operation uses fractions.Fraction.
Checks deliberately do not purport to exhaust all policies or prove the theorem.
"""
from __future__ import annotations
import json
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

N=4
SYMS=(0,1,2)
P=(F(1,2),F(1,3),F(1,6))
Q=(F(1,3),F(1,2),F(1,6))
LAMBDA=F(2,5)
assert sum(P)==sum(Q)==1 and all(z>0 for z in P+Q)

def x(h):
    return (len(h),h.count(0),h.count(1))

def advance(s,a):
    t,k0,k1=s
    return (t+1,k0+(a==0),k1+(a==1))

def path_weight(h,law):
    ans=F(1)
    for a in h: ans*=law[a]
    return ans

def actions(w0,w1,wc=None):
    if wc is None:
        den=w0+w1
        return (F(w0,den),F(w1,den),F(0))
    den=w0+w1+wc
    return (F(w0,den),F(w1,den),F(wc,den))

def history_policy(h,variant):
    # Distinguishes ordered paths with the same symbol histogram.
    v=sum((i+3)*(a+1) for i,a in enumerate(h))
    w0=1+(v+variant*3)%7
    w1=1+(v*2+len(h)+variant)%5
    wc=1+(v*3+2*variant+len(h))%6
    return actions(w0,w1,None if len(h)==N else wc)

def quotient_policy(s,variant):
    t,k0,k1=s
    v=(3*k0+5*k1+t*7+variant*11)
    w0=1+(v+variant)%5
    w1=1+(2*v+t+variant)%7
    wc=1+(3*v+variant)%6
    return actions(w0,w1,None if t==N else wc)

def simulate_history(policy,law):
    live={():F(1)}
    obs=defaultdict(F); occ=defaultdict(F); act=defaultdict(F)
    for t in range(N+1):
        nxt=defaultdict(F)
        for h,m in live.items():
            assert len(h)==t and m>=0
            st=x(h)
            probs=policy(h)
            assert sum(probs)==1 and (t<N or probs[2]==0)
            occ[st]+=m
            for d in (0,1):
                obs[(t,st,d)]+=m*probs[d]
                act[(st,d)]+=m*probs[d]
            act[(st,2)]+=m*probs[2]
            if t<N:
                for a in SYMS:
                    nxt[h+(a,)]+=m*probs[2]*law[a]
        live=nxt
    assert sum(obs.values())==1
    return dict(obs),dict(occ),dict(act)

def simulate_quotient(policy,law):
    live={(0,0,0):F(1)}
    obs=defaultdict(F);occ=defaultdict(F)
    for t in range(N+1):
        nxt=defaultdict(F)
        for st,m in live.items():
            assert st[0]==t
            probs=policy(st)
            assert sum(probs)==1 and (t<N or probs[2]==0)
            occ[st]+=m
            for d in (0,1): obs[(t,st,d)]+=m*probs[d]
            if t<N:
                for a in SYMS:
                    nxt[advance(st,a)]+=m*probs[2]*law[a]
        live=nxt
    assert sum(obs.values())==1
    return dict(obs),dict(occ)

def linear_mix(a,b):
    return {k:LAMBDA*a.get(k,F(0))+(1-LAMBDA)*b.get(k,F(0)) for k in a.keys()|b.keys()}

def law_ratio(s):
    t,k0,k1=s
    k2=t-k0-k1
    return (Q[0]/P[0])**k0*(Q[1]/P[1])**k1*(Q[2]/P[2])**k2

def build_markovized(pa,pb):
    _,occ_a,act_a=pa
    _,occ_b,act_b=pb
    occ=linear_mix(occ_a,occ_b)
    act=linear_mix(act_a,act_b)
    probs={}
    for st,m in occ.items():
        if m:
            z=tuple(act.get((st,j),F(0))/m for j in (0,1,2))
            assert sum(z)==1 and all(q>=0 for q in z)
            probs[st]=z
    def policy(st):
        return probs.get(st,(F(1),F(0),F(0)))
    return policy,probs,occ,act

def same_dist(a,b):
    return all(a.get(k,F(0))==b.get(k,F(0)) for k in a.keys()|b.keys())

def marginal_observer(out):
    co=defaultdict(F)
    for (t,(tt,k0,k1),d),m in out.items():
        assert t==tt
        co[(t,k0%2,d)]+=m
    return dict(co)

# Exhaust all 121 ordered histories for P/Q LR constancy on count-state fibers.
fibers=defaultdict(set); prefix_count=0
for t in range(N+1):
    for h in product(SYMS,repeat=t):
        prefix_count+=1
        p=path_weight(h,P);q=path_weight(h,Q)
        assert p>0 and q>0
        fibers[x(h)].add(q/p)
        assert q/p==law_ratio(x(h))
assert prefix_count==121 and all(len(v)==1 for v in fibers.values())

# Strong lumpability on every prefix: x's next-state P/Q law is history-independent.
for st in fibers:
    if st[0]==N: continue
    for law in (P,Q):
        next_law=defaultdict(F)
        for a in SYMS:next_law[advance(st,a)]+=law[a]
        assert sum(next_law.values())==1

checks=[]
for label,pair in (
    ('two_full_history_policies', (lambda h: history_policy(h,1),lambda h:history_policy(h,2))),
    ('two_quotient_policies', (lambda h:quotient_policy(x(h),1),lambda h:quotient_policy(x(h),2))),
):
    ap=simulate_history(pair[0],P);bp=simulate_history(pair[1],P)
    aq=simulate_history(pair[0],Q);bq=simulate_history(pair[1],Q)
    policy,probs,occ,act=build_markovized(ap,bp)
    targetp=linear_mix(ap[0],bp[0]);targetq=linear_mix(aq[0],bq[0])
    cp,occ_cp=simulate_quotient(policy,P)
    cq,occ_cq=simulate_quotient(policy,Q)
    assert same_dist(cp,targetp) and same_dist(cq,targetq)
    assert same_dist(marginal_observer(cp),marginal_observer(targetp))
    assert same_dist(marginal_observer(cq),marginal_observer(targetq))
    # Q occupancy is likelihood-factor of P occupancy, even with history-dependent stopping.
    for st in occ:
        assert occ_cq.get(st,F(0))==law_ratio(st)*occ_cp.get(st,F(0))
        assert occ.get(st,F(0))==occ_cp.get(st,F(0))
    checks.append({'type':label,'full_observer_equal_P':True,'full_observer_equal_Q':True,
                   'coarse_observer_equal_PQ':True,
                   'positive_occupancy_states':len(probs),
                   'sample_state_2_1_1_kernel':[str(z) for z in probs[(2,1,1)]],
                   'P_T4_D1':str(sum(v for (t,s,d),v in cp.items() if t==4 and d==1)),
                   'Q_T4_D1':str(sum(v for (t,s,d),v in cq.items() if t==4 and d==1))})

result={
 'schema':'EM_R1_IID_LR_FIBER_CONVEXITY_EXACT_CHECK_V1',
 'status':'PASS_EXACT_FINITE_INSTANCES',
 'model':{'N':N,'alphabet':SYMS,'P':[str(z) for z in P],'Q':[str(z) for z in Q],
          'compression':'x(h)=(t,count_0,count_1)','lambda':str(LAMBDA)},
 'prefix_count':prefix_count,'compressed_state_count':len(fibers),
 'all_LR_fibers_constant':True,'strong_lumpability_by_IID_and_recursive_x':True,
 'checks':checks,
 'proof_scope':'Finite checks of two chosen pairs of strategies; all-horizon convexity and universal Markovization rely on separate mathematical proof.'
}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
