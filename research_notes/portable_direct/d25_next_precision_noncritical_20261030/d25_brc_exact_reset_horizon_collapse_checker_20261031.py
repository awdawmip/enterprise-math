#!/usr/bin/env python3
"""Exact BRC integer rank-one reset factorization and full-refresh boundary check."""
import json
from itertools import product
from math import comb, factorial
from pathlib import Path

Z=(1,-1,-1,1)


def count(w,T,J,word):
    v=tuple(w)
    for y in word:
        v0=tuple(v[k]*J[k][y] for k in range(len(w)))
        v=tuple(sum(v0[k]*T[k][j] for k in range(len(w))) for j in range(len(w)))
    return sum(v)


def model(m,d,c=0):
    n=2*m-1;p=n+1
    w=tuple(comb(n,2*k) for k in range(m));W=sum(w);S=c+d*W
    T=tuple(tuple(c*(i==j)+d*w[j] for j in range(m)) for i in range(m))
    J=lambda h:tuple(tuple(p+h[k]*z for z in Z) for k in range(m))
    JA=J(tuple(2*k for k in range(m)))
    JB=J(tuple(n-2*k for k in range(m)))
    assert all(x>0 for row in T for x in row)
    return w,T,JA,JB,W,S


def main():
    full_checks=0;cases=[]
    for m in range(2,7):
        for d in (1,2,5):
            w,T,A,B,W,S=model(m,d,0)
            assert all(T[i]==T[0] for i in range(m))
            first_A=tuple(sum(w[k]*A[k][y] for k in range(m)) for y in range(4))
            first_B=tuple(sum(w[k]*B[k][y] for k in range(m)) for y in range(4))
            assert first_A==first_B
            for word in ([(0,)*t for t in range(0,2*m+1)] if m>3 else
                         [u for t in range(0,2*m+1) for u in product(range(4),repeat=t)]):
                a=count(w,T,A,word)
                b=count(w,T,B,word)
                fact=(S*d**(len(word)-1)) if word else 1
                if word:
                    fact*=__import__('math').prod(first_A[y] for y in word)
                else:
                    fact=W
                assert a==b==fact,(m,d,word,a,b,fact)
                full_checks+=1
            cases.append({"m":m,"d":d,"same_initial":list(w) if m==2 else "verified",
                          "identical_first_step_emission":list(first_A) if m==2 else "verified",
                          "full_words":m<=3,"rank_one":True})
    # Separate sharp general length-2 witness when the initial w and reset r differ.
    w=(1,1);r=(1,2);T=((1,2),(1,2));
    JA=((4,2,2,4),(5,1,1,5))
    JB=((5,1,1,5),(4,2,2,4))
    for word in product(range(4),repeat=1):
        assert count(w,T,JA,word)==count(w,T,JB,word)
    l1=0;mass_a=mass_b=0
    for word in product(range(4),repeat=2):
        a=count(w,T,JA,word);b=count(w,T,JB,word)
        assert a-b==3*(6+3*Z[word[0]])*Z[word[1]]
        l1+=abs(a-b);mass_a+=a;mass_b+=b
    assert count(w,T,JA,(0,0))==378
    assert count(w,T,JB,(0,0))==351
    assert (l1,mass_a,mass_b)==(288,2592,2592)
    # Arbitrarily fast-but-not-rank-one integer mixing retains N-length strict split.
    fast=[]
    for m in (2,3,4):
        d=100;c=1;n=2*m-1
        w,T,A,B,W,S=model(m,d,c)
        word=(0,)*n
        gap=count(w,T,A,word)-count(w,T,B,word)
        assert gap==-S*factorial(n)
        fast.append({"m":m,"d":d,"c":c,"spectral_ratio_num":c,
                     "spectral_ratio_den":S,"first_split_all_zero_gap":gap})
    doc={"status":"PASS","scope":"AUTHOR_EXACT_INTEGER_AUXILIARY_BRC_ONLY",
         "rankone_configurations":len(cases),"checked_words_and_witnesses":full_checks,
         "exhaustive_rankone_range":"m=2,3; d=1,2,5; words |u|<=2m; m=4,5,6 targeted all-zero words to length 2m",
         "rankone_cases":cases,"two_step_sharp_nonstationary_witness":{
             "initial_weights":[1,1],"reset_weights":[1,2],
             "T":[list(x) for x in ((1,2),(1,2))],
             "two_step_00":{"A":378,"B":351},"L1":l1,"mass_each":mass_a},
         "near_rankone_positive_cases":fast,
         "proof_scope":"general positive integer rank-one reset factorization and two-step criterion; symbolic finite-difference sharp nonzero-c family from preceding theorem",
         "admission":"UNREVIEWED_NOT_ADMITTED_NOT_NATIVE"}
    dest=Path(__file__).with_name('d25_brc_exact_reset_horizon_collapse_author_check_20261031.json')
    dest.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS',len(cases),'rankone configurations',full_checks,'word/witness checks; exact sharp two-step and near-rankone cases')
    print('m2 nonstationary witness L1',l1,'mass',mass_a,'00',[count((1,1),((1,2),(1,2)),J,(0,0)) for J in (JA,JB)])

if __name__=='__main__':
    main()
