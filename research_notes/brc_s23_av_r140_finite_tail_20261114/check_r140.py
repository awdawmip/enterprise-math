#!/usr/bin/env python3
"""R140 exact finite word-level eventual-saturation certificate.
External tied-phase S23 observer only. Uses unbounded Python integers; no floats.
For m in [4, MAX_M], checks the entire remaining coefficient interval
[K_candidate(m), U_rep(m)-1] word by word; the known R139 gap cutoff
certifies all later coefficients. The R139B extremal-word lemma certifies failure
at K_ext-1 for m>=5; m=4 is exceptional, with exact threshold 4 rather than 3.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from math import gcd
from time import perf_counter


def farey_adjacent(n):
    a,b,c,d=0,1,1,n
    while True:
        assert b*c-a*d == 1
        yield a,b,c,d
        k=(n+b)//d
        a,b,c,d=c,d,k*c-a,k*d-b
        if a>=b:
            break


def word_and_gap_records(m):
    """Enumerate exact Farey open-slope cells and all m+1 intercept gaps."""
    result=defaultdict(list)
    gaps=0
    for a,b,c,d in farey_adjacent(m):
        A=a*d+b*c
        Q=2*b*d   # midpoint slope is A/Q (strictly inside Farey cell)
        cuts=[(0,0,0),(Q,1,0)]
        for j in range(1,m+1):
            p=(j*A)//Q+1
            cuts.append((p*Q-j*A,p,j))
        cuts.sort()
        assert all(x[0]<y[0] for x,y in zip(cuts,cuts[1:]))
        for (low,p,j),(high,q,k) in zip(cuts,cuts[1:]):
            # midpoint intercept rho=(low+high)/(2Q)
            x=low+high
            denom=2*Q
            prev=x//denom
            w=0
            for i in range(1,m+1):
                cur=(x+2*i*A)//denom
                w=(w<<1)|(cur-prev)
                prev=cur
            D=j*b*c-k*a*d+(q-p)*b*d
            B=b*d-D
            assert D>=min(b,d)
            # a,b,c,d,p,j,q,k,D,B. Every field is exact integer.
            result[w].append((a,b,c,d,p,j,q,k,D,B))
            gaps+=1
    return result,gaps


def modular_feasible(g,K):
    a,b,c,d,p,j,q,k,D,B=g
    L=K-1
    h=((L+k)*a)%b
    return L+D>d*(b-h)


def rational_interval_feasible(g,K):
    a,b,c,d,p,j,q,k,D,B=g
    L=K-1
    lo_num=(L+k)*a-q*b
    N=lo_num//b+1
    return N*d < (L+j)*c-p*d


def recover_witness(g,K):
    """Return exact theta in the Farey cell with correct intercept word."""
    a,b,c,d,p,j,q,k,D,B=g
    L=K-1
    N=((L+k)*a-q*b)//b+1
    lo=max(Fraction(a,b),Fraction(N+p,L+j))
    hi=min(Fraction(c,d),Fraction(N+q,L+k))
    assert lo<hi
    return (lo+hi)/2


def observe_word(theta,m,K):
    L=K-1
    a=theta.numerator;b=theta.denominator
    v=0
    prev=(L*a)//b
    for i in range(m):
        nxt=((L+i+1)*a)//b
        v=(v<<1)|(nxt-prev)
        prev=nxt
    return v


def target_F(m):
    phi=list(range(m+1))
    for q in range(2,m+1):
        if phi[q]==q:
            for j in range(q,m+1,q):phi[j]-=phi[j]//q
    return 1+sum((m+1-q)*phi[q] for q in range(1,m+1))


def verify(max_m=80):
    t0=perf_counter();rows=[]
    totals={'gaps':0,'words':0,'critical_words':0,'tested_word_coefficients':0,
            'tested_coefficient_values':0,'checked_witnesses':0,'predicates':0}
    for m in range(4,max_m+1):
        byword,gaps=word_and_gap_records(m)
        F=target_F(m)
        assert len(byword)==F,(m,'F mismatch',len(byword),F)
        total_gaps=sum(map(len,byword.values()))
        assert total_gaps==gaps
        K_lower=(m-2)*((m-1)//2)+1
        KE=4 if m==4 else K_lower
        envelope=max(min(max(2,g[-1]+2) for g in gs) for gs in byword.values())
        critical={w:gs for w,gs in byword.items() if min(max(2,g[-1]+2) for g in gs)>KE}
        # Exact last absence lower bound: m>=5 uses extremal two-one word;
        # m=4 has a separate missing word 1000 at K=3.
        extremal=(1<<(m-1))|1
        assert extremal in byword
        bad_word = (1<<(m-1)) if m==4 else extremal
        assert not any(modular_feasible(g,KE-1) for g in byword[bad_word]),(m,'lower bound')
        assert KE<=envelope,(m,'unexpected envelope')
        count=0; witness_count=0; mod_count=0
        for K in range(KE,envelope):
            for w,gs in critical.items():
                found=None
                for g in gs:
                    mod_count+=1
                    if modular_feasible(g,K):
                        found=g
                        break
                assert found is not None,('counterexample',m,K,w)
                count+=1
            # Independent rational interval + direct source formula checks,
            # including both ends and one reproducible interior coefficient.
            if K in {KE,KE+1,(KE+envelope)//2,envelope-1}:
                for w,gs in sorted(critical.items()):
                    g=next(g for g in gs if modular_feasible(g,K))
                    assert rational_interval_feasible(g,K)
                    t=recover_witness(g,K)
                    assert observe_word(t,m,K)==w, (m,K,w,g,t)
                    witness_count+=1
        # Conformance check: every gap obeys modular <=> rational endpoints
        # at the lower boundary and near its own last failure.
        for gs in byword.values():
            for g in gs:
                for K in {2,KE,max(2,g[-1]+1),max(2,g[-1]+2)}:
                    assert modular_feasible(g,K)==rational_interval_feasible(g,K),(m,K,g)
                    mod_count+=1
        totals['gaps']+=gaps;totals['words']+=F
        totals['critical_words']+=len(critical)
        totals['tested_word_coefficients']+=count
        totals['tested_coefficient_values']+=max(0,envelope-KE)
        totals['checked_witnesses']+=witness_count
        totals['predicates']+=mod_count
        row={'m':m,'F':F,'gap_records':gaps,'K_extremal_lower_bound':K_lower,
             'K_tail_candidate':KE,'U_rep':envelope,
             'K_eventual_exact_finite':KE,'critical_words':len(critical),
             'tested_word_coefficient_pairs':count,'checked_direct_witnesses':witness_count}
        rows.append(row)
        if m%10==0 or m==max_m:
            print('m',m,'F',F,'K',KE,'critical',len(critical),'checked',count,flush=True)
    report={'schema':'R140_EXACT_FINITE_TAIL_CERTIFICATE_V1',
            'marker':'R140_FINITE_EVENTUAL_TAIL_PASS',
            'domain':f'all integer m in [4,{max_m}], K_eventual(4)=4 and K_eventual(m)=(m-2)*floor((m-1)/2)+1 for 5<=m<={max_m}',
            'precision':'arbitrary-precision integer rational arithmetic, no floats',
            'proof_dependency':'R139B extremal-word last absence (m>=5), special m=4 gap counterexample, and R139 per-gap cutoff',
            'method':'Exhaustively check every critical word and coefficient K in [K_candidate,U_rep-1]; above U_rep one permanently available Farey gap per word; explicit missing word at K_candidate-1 establishes minimality',
            'totals':totals,'rows':rows,'elapsed_seconds_observed':round(perf_counter()-t0,3)}
    dest=f'/mnt/data/r140_verification_m{max_m}.json'
    with open(dest,'w',encoding='utf-8') as f:
        json.dump(report,f,ensure_ascii=False,indent=2)
    print(report['marker'],totals,'elapsed',report['elapsed_seconds_observed'],'output',dest)
    return report


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-m',type=int,default=80)
    args=ap.parse_args()
    verify(args.max_m)
