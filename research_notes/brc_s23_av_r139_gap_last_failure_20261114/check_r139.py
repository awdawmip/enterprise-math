#!/usr/bin/env python3
"""R139: exact last infeasible Farey-gap coefficient and word-envelope checks.
No floating point. External tied S23 floor-word auxiliary model.
"""
from fractions import Fraction
from math import gcd
import json


def floor(x):
    return x.numerator // x.denominator if isinstance(x, Fraction) else x


def cells(m):
    fs = sorted({Fraction(a,b) for b in range(1,m+1) for a in range(b+1)})
    result=[]
    for left,right in zip(fs, fs[1:]):
        a,b=left.numerator,left.denominator
        c,d=right.numerator,right.denominator
        assert b*c-a*d == 1
        alpha=(left+right)/2
        cuts=[(Fraction(0),0,0),(Fraction(1),1,0)]
        for j in range(1,m+1):
            p=floor(j*alpha)+1
            cuts.append((p-j*alpha,p,j))
        cuts.sort()
        for (lv,p,j),(uv,q,k) in zip(cuts,cuts[1:]):
            assert lv<uv
            rho=(lv+uv)/2
            word=tuple(floor(rho+(i+1)*alpha)-floor(rho+i*alpha) for i in range(m))
            D=j*b*c-k*a*d+(q-p)*b*d
            assert D>=min(b,d)
            assert (D-j)%d==0 and (D-k)%b==0
            B=b*d-D
            result.append((a,b,c,d,p,j,q,k,D,B,word))
    return result


def feasible(g,K):
    a,b,c,d,p,j,q,k,D,B,w=g
    L=K-1
    h=((L+k)*a)%b
    return L+D>d*(b-h)


def fraction_feasible(g,K):
    a,b,c,d,p,j,q,k,D,B,w=g
    L=K-1
    lo=(L+k)*Fraction(a,b)-q
    hi=(L+j)*Fraction(c,d)-p
    return floor(lo)+1<hi


def word_count(records,K):
    return len({rec[-1] for rec in records if feasible(rec,K)})


def analyze(max_m=22):
    all_gaps=0
    crosschecks=0
    exact_lastbad=0
    tailchecks=0
    wordtest=0
    results=[]
    witnesses=[]
    for m in range(1,max_m+1):
        R=cells(m)
        all_gaps+=len(R)
        byword={}
        for g in R:
            byword.setdefault(g[-1],[]).append(g)
            B=g[-2]
            # new O(1) exact gap eventual threshold: K_gap=max(2, B+2)
            K_gap=max(2,B+2)
            # Direct tests around exact last bad and large coefficients.
            for K in sorted({2,3,4,5,K_gap,K_gap+1,K_gap+11,10**40+137,max(2,K_gap-1)}):
                assert feasible(g,K)==fraction_feasible(g,K), (m,g,K)
                crosschecks+=1
            if B>=1:
                assert not feasible(g,B+1) and feasible(g,B+2), (m,g,B)
                exact_lastbad+=1
            for K in (K_gap,K_gap+1,K_gap+7,10**40+137):
                assert feasible(g,K), (m,g,K)
                tailchecks+=1
        # Every word has a permanently feasible representation at K>=t_rep.
        t_rep=max(min(max(2,g[-2]+2) for g in gs) for gs in byword.values())
        t_gap=max(max(2,g[-2]+2) for g in R)
        t_last=2
        n_fails=0
        for K in range(2,t_rep+1):
            c=word_count(R,K)
            wordtest+=1
            if c<len(byword):
                t_last=K+1
                n_fails+=1
        assert t_last<=t_rep
        res={'m':m,'F':len(byword),'gaps':len(R),'all_gap_cutoff':t_gap,
             'representation_envelope':t_rep,'word_eventual':t_last,
             'incomplete_K_count':n_fails,'envelope_is_sharp':t_rep==t_last}
        results.append(res)
        if t_last<t_rep and len(witnesses)<8:
            ws=[(''.join(map(str,w)),min(max(2,g[-2]+2) for g in gs)) for w,gs in byword.items()]
            maxwords=[x for x in ws if x[1]==t_rep]
            witnesses.append({'m':m,'last_missing_K':t_last-1,'t_rep':t_rep,'bottleneck_words':maxwords[:3]})
    out={'marker':'R139_EXACT_LAST_BAD_GAP_PASS','arithmetic':'Python int and fractions.Fraction',
         'm_range':[1,max_m],
         'counts':{'gaps':all_gaps,'fraction_modular_checks':crosschecks,
                   'nontrivial_lastbad_checks':exact_lastbad,'tail_checks':tailchecks,
                   'word_coefficient_points':wordtest},
         'rows':results,'word_examples':witnesses}
    print(out['marker'])
    print('COUNTS',out['counts'])
    for x in results:
        print(x)
    with open('verification_r139.json','w',encoding='utf-8') as f:
        json.dump(out,f,indent=2,ensure_ascii=False)


if __name__=='__main__':
    analyze()
