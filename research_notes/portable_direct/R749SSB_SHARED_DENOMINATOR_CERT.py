#!/usr/bin/env python3
"""Exact finite certificate: one common denominator-count error across all samples.
Positive labeled Walsh source model, frozen pin a72226e2430ffa4786321ac86e7f0c599d5f0389.
No third-party dependencies. Output is JSON with PASS iff all exact assertions pass.
"""
from fractions import Fraction as Q
from itertools import product
import json

W = (1, 1, 2, 3, 6)
J = (0, 1, 5)
P = tuple(Q(x, 36) for x in (455, -295, -25, 185, -25, -295))
S = tuple(tuple(P[(a+h)%6] for h in J) for a in range(6))
CUT = 1350
# Exact independent-count predecessor global bounds at PR #2546, R749SSA.
INDEPENDENT_THRESHOLDS = ((35,261,507),(53,267,513),(65,273,513))

nmax=CUT+max(J)
a=[0]*nmax
b=[0]*nmax
a[0]=1
for idx,w in enumerate(W):
    for n in range(w,nmax):
        b[n] += b[n-w]+(a[n-w] if idx==0 else 0)
        a[n] += a[n-w]
C=[0]*(nmax+1)
T=[0]*(nmax+1)
for n in range(nmax):
    C[n+1]=C[n]+a[n]
    T[n+1]=T[n]+b[n]

def H(q):
    return Q(1,6)+Q(1,2*q)-Q(115,36*q*q)+Q(115,6*q**3)-Q(16315,108*q**4)

H_scaled=[None]*(nmax+1)
for q in range(1,nmax+1): H_scaled[q]=q**4*H(q)

def y(q,e,d):
    assert C[q]+d>0
    return Q(q**3*(T[q]+e),C[q]+d)-H_scaled[q]

def ceil(fr): return -(-fr.numerator//fr.denominator)
def floor(fr):return fr.numerator//fr.denominator

def common_errors(r,K):
    return range(max(-K,1-C[r]),K+1)

def shared_failure(r,M,K):
    a=r%6
    qs=tuple(r+h for h in J)
    s=S[a]
    # Sufficient exact success via half the minimum inter-signature separation.
    rad=max(abs(y(q,e,d)-s[i]) for i,q in enumerate(qs)
            for d in common_errors(r,K) for e in set((-M,M)))
    if rad < Q(15,4):return None,'separation'
    for d in common_errors(r,K):
        for rival in range(6):
            if rival==a:continue
            for j in range(3):
                for ej in set((-M,M)):
                    v=y(qs[j],ej,d)
                    u=abs(v-s[j])
                    if abs(v-S[rival][j])>u:continue
                    errors=[None]*3
                    errors[j]=ej
                    for i,q in enumerate(qs):
                        if i==j:continue
                        L=max(s[i]-u,S[rival][i]-u)
                        U=min(s[i]+u,S[rival][i]+u)
                        low=max(-M,ceil((L+H_scaled[q])*Q(C[q]+d,q**3)-T[q]))
                        high=min(M,floor((U+H_scaled[q])*Q(C[q]+d,q**3)-T[q]))
                        if low>high:break
                        errors[i]=low
                    if all(e is not None for e in errors):
                        vals=tuple(y(q,e,d) for q,e in zip(qs,errors))
                        true=max(abs(vals[i]-s[i]) for i in range(3))
                        rival_dist=max(abs(vals[i]-S[rival][i]) for i in range(3))
                        assert rival_dist<=true
                        return {'r':r,'phase':a,'rival':rival,'common_denominator_error':d,
                                'numerator_errors':errors,'true_distance':str(true),
                                'rival_distance':str(rival_dist)},'exact'
    return None,'exact'

def naive_failure(r,M,K):
    qs=tuple(r+h for h in J)
    a=r%6
    for d in common_errors(r,K):
        samples=[tuple(y(q,e,d) for e in range(-M,M+1)) for q in qs]
        for vals in product(*samples):
            true=max(abs(vals[i]-S[a][i]) for i in range(3))
            if any(max(abs(vals[i]-S[b][i]) for i in range(3))<=true for b in range(6) if b!=a):
                return True
    return False

def main():
    outcomes=[]
    for K in range(3):
        for M in range(3):
            last=None;exacts=0
            for r in range(1,CUT):
                fail,mode=shared_failure(r,M,K)
                if mode=='exact':exacts+=1
                if fail is not None:last=fail
            N=1+(last['r'] if last else 0)
            assert N<=INDEPENDENT_THRESHOLDS[M][K]
            outcomes.append({'M':M,'K':K,'N_shared':N,'N_independent':INDEPENDENT_THRESHOLDS[M][K],
                             'last_failure':last,'finite_cutoffs_checked':CUT-1,
                             'exact_cases_after_separation_prune':exacts})
            print('M,K=',M,K,'N_shared=',N,'N_independent=',INDEPENDENT_THRESHOLDS[M][K],
                  'last=',last and last['r'],flush=True)
    direct=0
    for M in range(3):
        for K in range(3):
            for r in range(1,25):
                assert naive_failure(r,M,K)==(shared_failure(r,M,K)[0] is not None)
                direct+=1
    source_tests=0
    for r in range(1,25):
        ct=tt=0
        def rec(i,left,marked):
            nonlocal ct,tt
            if i==len(W):
                ct+=1;tt+=marked;return
            for k in range(left//W[i]+1):rec(i+1,left-k*W[i],k if i==0 else marked)
        rec(0,r-1,0)
        assert ct==C[r] and tt==T[r]
        source_tests+=1
    # Predecessor R749SSA independent-error tail (for r>=1350, M,K<=2).
    tail = Q(63374339249936,28025208984321)
    assert tail < Q(15,4)
    payload={'status':'PASS','unit':'R749SSB',
             'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
             'model':'W=(1,1,2,3,6), shifts=(0,1,5), unique nearest max-norm signature',
             'error_model':'one shared signed denominator count error d across three samples; independent signed integer numerator errors e_i',
             'M_and_K_inclusive':[0,1,2], 'cutoff_exclusive':CUT,
             'tail_source':'R749SSA PR#2546 independent-error certificate, tail r>=1350',
             'tail_bound_r_1350_for_budgets_up_to_2':str(tail),
             'min_signature_separation':'15/2',
             'exact_shared_end_coordinate_criterion':'fix common d and one signed numerator endpoint at maximizer coordinate; other e_i via exact integer intervals',
             'independent_direct_cube_checks':direct,
             'independent_source_recursions':source_tests,
             'results':outcomes}
    with open('R749SSB_SHARED_DENOMINATOR_RESULTS.json','w') as f:
        json.dump(payload,f,indent=2,ensure_ascii=False)
    print('PASS, independent direct cases',direct)
if __name__=='__main__':main()
