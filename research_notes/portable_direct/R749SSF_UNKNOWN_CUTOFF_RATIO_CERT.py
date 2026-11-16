#!/usr/bin/env python3
"""R749SSF exact certificate: unknown-cutoff identifiability of raw source ratios.
Frozen auxiliary pin a72226e2430ffa4786321ac86e7f0c599d5f0389.
Standard library only. Does not verify native X6 dynamics.
"""
from fractions import Fraction
from itertools import product
from math import comb
import json

W=(1,1,2,3,6)
M=K=2

def counts(limit):
    a=[0]*(limit+1);b=[0]*(limit+1);a[0]=1
    for j,w in enumerate(W):
        for v in range(w,limit+1):
            old=a[v-w];a[v]+=old
            b[v]+=b[v-w]+(old if j==0 else 0)
    C=[0]*(limit+2);T=[0]*(limit+2)
    for v in range(limit+1):
        C[v+1]=C[v]+a[v];T[v+1]=T[v]+b[v]
    return C,T

def residue_counts(q):
    C=T=0
    for t in product(*(range(6//w) for w in W)):
        s=sum(w*x for w,x in zip(W,t))
        L=(q-1-s)//6
        if L<0: continue
        m=comb(L+5,5)
        C+=m;T+=(L+t[0])*m
    return C,T

def diffs(values):
    out=[]
    row=values[:]
    while row:
        out.append(row[0]);row=[row[j+1]-row[j] for j in range(len(row)-1)]
    return out

def run():
    C,T=counts(320)
    for q in range(1,321):
        assert (C[q],T[q])==residue_counts(q),('residues',q)
    assert [(C[q],T[q]) for q in (5,6,7,8)]==[(25,25),(41,50),(65,91),(98,156)]
    def lo(q):return Fraction(T[q]-M,C[q]+K)
    def hi(q):return Fraction(T[q]+M,C[q]-K)
    def G(q):return (T[q+1]-M)*(C[q]-K)-(T[q]+M)*(C[q+1]+K)
    assert G(6)==-13
    for q in range(7,36):assert G(q)>0,q
    bases=range(36,42)
    coeff={}
    for base in bases:
        ds=diffs([G(base+6*j) for j in range(12)])
        assert ds[11]==0,(base,ds[11])
        assert all(t>0 for t in ds[:11]),(base,ds)
        coeff[str(base)]=ds[:11]
        # check interpolation on independent sample points beyond the fit domain
        for j in (12,15,20,30):
            assert sum(comb(j,i)*ds[i] for i in range(11))==G(base+6*j),(base,j)
    assert hi(6)==Fraction(4,3)
    assert lo(7)==Fraction(89,67)
    assert lo(8)==Fraction(77,50)>hi(6)
    def pairs(q):
        return {(Fraction(T[q]+e,C[q]+d)):(e,d)
            for e in range(-M,M+1) for d in range(-K,K+1)}
    for q in range(6,48):assert len(pairs(q))==25,('same_q',q)
    assert len(pairs(6))==len(pairs(7))==25
    assert not set(pairs(6)).intersection(pairs(7))
    # directly check exact rationals at the exceptional adjacent cutoffs.
    second6=sorted(pairs(6))[-2];second7=sorted(pairs(7))[1]
    assert second6 < lo(7) < hi(6) < second7
    for q in range(7,320):assert hi(q)<lo(q+1),q
    # Distinguish the raw ratio from the smooth-subtracted Y observer.
    def H(q):
        return (Fraction(1,6)+Fraction(1,2*q)-Fraction(115,36*q*q)
                +Fraction(115,6*q**3)-Fraction(16315,108*q**4))
    seen={};same_q=0
    for q in range(6,301):
        for e in range(-M,M+1):
            for d in range(-K,K+1):
                y=q**3*Fraction(T[q]+e,C[q]+d)-q**4*H(q)
                assert y not in seen,('Y finite collision',q,e,d,seen.get(y))
                seen[y]=(q,e,d)
                same_q+=1
    return {
        'unit':'R749SSF', 'status':'PASS', 'mathematical_review':'AUTHOR_EXACT_NOT_REVIEWED',
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'weights':list(W), 'error_budgets':{'numerator':M,'denominator':K},
        'raw_ratio_joint_unknown_cutoff_injective_for_all_q_ge':6,
        'sharp_at_q5':{'C5':C[5],'T5':T[5], 'pairs':[[-2,-2],[-1,-1]],'ratio':'1'},
        'population_q5_q8':{str(q):{'C':C[q],'T':T[q]} for q in range(5,9)},
        'gap_numerator_G6':G(6), 'gap_numerator_G7':G(7),
        'overlap_q6_q7_exact_set_intersection':0,
        'q6_second_largest_ratio':str(second6),
        'q7_second_smallest_ratio':str(second7),
        'certificate_method':'G(q) positive for 7..35, then exact degree-10 six-residue Newton binomial polynomials with positive coefficients at bases 36..41',
        'newton_binomial_coefficients_G_base36_to41':coeff,
        'cross_check_residue_counts_q': [1,320],
        'known_cutoff_injectivity_finite_checked_q':[6,47],
        'cross_check_interpolation_j':[12,15,20,30],
        'original_smooth_subtracted_Y_finite_exploration':{'q_from':6,'q_to':300,'error_triplets_checked':same_q,'exact_collisions':0,'infinite_case':'OPEN'},
        'scope':'raw numerator/denominator ratio observer; unknown q; not an infinite theorem for original Y observer or native BRC/X6'
    }

if __name__=='__main__':
    out=run()
    with open('R749SSF_UNKNOWN_CUTOFF_RATIO_RESULTS.json','w',encoding='utf-8') as f:
        json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
    print(out['status'],'bases=',len(out['newton_binomial_coefficients_G_base36_to41']),
          'Y_finite=',out['original_smooth_subtracted_Y_finite_exploration']['error_triplets_checked'])
