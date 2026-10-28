"""Exact checks for C42: nonuniform factor paths and balance conditions."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product, permutations
from math import comb, factorial
from time import perf_counter
import sys
import sympy as sp
from biased_paths import *


def exhaustive_small():
    cases=0;words=0
    weight_cases=[(Q(1),Q(1),Q(1)),(Q(1),Q(1),Q(2)),
                  (Q(1),Q(2),Q(3)),(Q(2,3),Q(4,5),Q(7,6))]
    count_cases=[(1,1,1),(2,1,1),(2,2,1),(2,2,2)]
    for ent in product((-1,0,1),repeat=3):
        d=skew(3,ent)
        for a in count_cases:
            for w in weight_cases:
                dist,info=state_distribution(a,d,w)
                other,n,_=direct_words(a,d,w)
                assert dist==other;cases+=1;words+=n
                # Rescaling all priorities leaves the path measure unchanged.
                assert exact_moments(a,d,tuple(7*x for x in w))==exact_moments(a,d,w)
    # Fractional curvature and four prime types.
    extra=[]
    for seed in range(9):
        a=(1+seed%2,1,1,1)
        d=skew(4,[Q((seed+2*i)%7-3,3) for i in range(6)])
        w=tuple(Q(seed+i+2,i+1) for i in range(4))
        dist,info=state_distribution(a,d,w);other,n,_=direct_words(a,d,w)
        assert dist==other;cases+=1;words+=n;extra.append(info)
    write('finite_distribution_checks.json',{'status':'PASS','cases':cases,
            'direct_weighted_words':words,'four_prime_cases':extra,
            'scope':'Exact full score probabilities, mean, variance, and uniform priority-scale invariance; no Monte Carlo.'})


def matrix_conditions():
    rows=[];checked=0
    for w in [(Q(1),)*4,(Q(1),Q(1),Q(2),Q(2)),
              (Q(1),Q(1),Q(2),Q(3)),(Q(1),Q(2),Q(3),Q(4))]:
        balanced=0
        for ent in product((-1,0,1),repeat=6):
            d=skew(4,ent);u=(1,2,1,2)
            c=balance_coefficients(u,d,w)['cubic']
            conditions=group_constraints(u,d,w)
            ok=all(x==0 for row in conditions.values() for x in row)
            assert (c==0)==ok
            balanced+=ok;checked+=1
        rows.append({'weights':w,'finite_curvatures_checked':729,'balanced_in_this_finite_grid':balanced})
    dims=[]
    for k in range(1,8):
        for g in range(1,k+1):
            # Contiguous nonempty groups; u stays strictly positive.
            w=tuple(Q(min(i+1,g)) for i in range(k))
            u=tuple(i+1 for i in range(k));edges=list(combinations(range(k),2))
            columns=[]
            for e in edges:
                d=skew(k,[int(x==e) for x in edges])
                vals=group_constraints(u,d,w)
                columns.append([x for row in vals.values() for x in row])
            A=sp.Matrix(len(set(w))*k,len(columns),lambda i,j:columns[j][i])
            nullity=len(columns)-int(A.rank())
            want=comb(k-g,2) if k-g>=2 else 0
            assert nullity==want
            dims.append({'types':k,'weight_classes':g,'nullity':nullity})
    # Verify the Gram kernel by exact Cauchy principal minors.
    minors=0
    for wp in [Q(1,3),Q(1),Q(5,2)]:
        rates=[Q(1,2),Q(1),Q(3,2),Q(5,2)]
        K=sp.Matrix([[kernel_cov(wp,x,y) for y in rates] for x in rates])
        for n in range(1,5):
            assert K[:n,:n].det()>0;minors+=1
    write('balance_classification.json',{'status':'PASS','finite_condition_checks':checked,
           'rows':rows,'dimension_checks':dims,'positive_gram_minors':minors})


def cycle_and_surviving_four():
    d=skew(3,[1,-1,1]);rows=[];full=[]
    for t in [1,2,3,4,10,100]:
        a=(t,)*3
        neutral=exact_moments(a,d,(Q(1),)*3)
        biased=exact_moments(a,d,(Q(1),Q(1),Q(2)))
        assert biased['variance']==Q(t*t,4)+Q(t*t*(t-1),90)
        row={'t':t,'uniform_variance':neutral['variance'],'every_step_bias_variance':biased['variance'],
             'mean_both':biased['mean'],'formula_only':t>4}
        if t<=4:
            hist,info=state_distribution(a,d,(Q(1),Q(1),Q(2)))
            full.append({'t':t,'distribution':hist,**info})
        rows.append(row)
    _,_,words=direct_words((1,1,1),d,(Q(1),Q(1),Q(2)))
    four=skew(4,[0,1,-1,-1,1,0]);w4=(Q(1),Q(1),Q(2),Q(2))
    coeff=balance_coefficients((1,1,1,1),four,w4)
    assert coeff['cubic']==0 and coeff['quadratic']==Q(14,45)
    four_rows=[]
    for t in [1,2]:
        hist,info=state_distribution((t,)*4,four,w4)
        other,n,_=direct_words((t,)*4,four,w4)
        assert hist==other and info['variance']==Q(14*t*t,45)
        four_rows.append({'t':t,'distribution':hist,**info})
    # Perturb one of a matched pair and the cubic contribution becomes positive.
    detuned=balance_coefficients((1,1,1,1),four,(Q(1),Q(11,10),Q(2),Q(2)))
    assert detuned['cubic']>0
    write('nonuniform_examples.json',{'status':'PASS','cycle_table':rows,'cycle_full_laws':full,
          'n30_word_weights':words,'four_prime_curvature':four,'four_weights':w4,
          'four_coefficients':coeff,'four_full_laws':four_rows,'four_detuned':detuned})


def first_choice_and_rotation():
    checked=0;hist_checks=0;rotation_checks=0;rows=[]
    for a in [(1,1,1),(2,2,2),(3,3,3),(1,2,3)]:
        # Kernel contains this multiplicity vector.
        u0,u1,u2=a
        d=skew(3,[Q(u2),-Q(u1),Q(u0)])
        assert all(sum(d[i][j]*a[j] for j in range(3))==0 for i in range(3))
        neutral,base=state_distribution(a,d,(Q(1),)*3)
        for w in [(Q(1),Q(1),Q(2)),(Q(5),Q(1,3),Q(7,2))]:
            biased,info=state_distribution(a,d,w,first_only=True)
            assert biased==neutral;hist_checks+=1
            other,n,_=direct_words(a,d,w,first_only=True)
            assert biased==other;checked+=n
        # Word score is unchanged by cyclic shift iff weighted row sums vanish.
        def gen(rem,word=()):
            if not any(rem):yield word;return
            for p,x in enumerate(rem):
                if x:
                    r=list(rem);r[p]-=1;yield from gen(tuple(r),word+(p,))
        def score(word):
            used=[0]*3;ans=Q(0)
            for p in word:
                ans+=sum(d[q][p]*used[q] for q in range(p));used[p]+=1
            return ans
        for word in gen(a):
            assert score(word)==score(word[1:]+word[:1]);rotation_checks+=1
        rows.append({'counts':a,'curvature':d,'full_score_support':base['score_support'],
                    'common_mean':base['mean'],'common_variance':base['variance']})
    # A deliberately unbalanced model shows why the premise matters.
    du=skew(3,[1,1,1]);a=(1,1,1)
    before,_=state_distribution(a,du,(Q(1),)*3)
    after,ai=state_distribution(a,du,(Q(1),Q(1),Q(2)),first_only=True)
    assert before!=after
    write('first_choice_invariance.json',{'status':'PASS','balanced_full_law_checks':hist_checks,
         'direct_weighted_words':checked,'cyclic_shift_checks':rotation_checks,'rows':rows,
         'unbalanced_witness':{'before':before,'after':after,'after_moments':ai}})


def weak_bias_and_calibration():
    s=sp.symbols('s',positive=True)
    C=sp.factor(2*(sp.Rational(1,3)+1/(3+2*s)-2/(3+s)-(sp.Rational(1,2)-1/(2+s))**2))
    want=s*s*(2*s*s+5*s+5)/(6*(s+2)**2*(s+3)*(2*s+3))
    assert sp.simplify(C-want)==0
    assert sp.limit(C/(s*s),s,0)==sp.Rational(5,216)
    # Equality to the independently computed finite variance coefficient.
    examples=[];cyc=skew(3,[1,-1,1])
    for sv in [Q(0),Q(1,100),Q(1,10),Q(1),Q(2),Q(-1,2)]:
        coef=balance_coefficients((1,1,1),cyc,(Q(1),Q(1),1+sv))
        c=Q(C.subs(s,sp.Rational(sv.numerator,sv.denominator)))
        assert coef['cubic']==c and coef['quadratic']==Q(1,4)-c
        examples.append({'relative_priority_bias':sv,'cubic_coefficient':c,
           'quadratic_coefficient':coef['quadratic'],
           'equal_extra_and_uniform_variance_t':None if not c else 1+1/(4*c)})
    # Two-type selection odds fix priorities up to a common positive scale.
    w=(Q(2,3),Q(4,5),Q(7,6),Q(11,5));odds={}
    for i,j in combinations(range(4),2):
        prob=theta(w[i],w[j]);odds[i,j]=prob/(1-prob)
    recovered=(Q(1),)+tuple(1/odds[0,j] for j in range(1,4))
    assert recovered==tuple(x/w[0] for x in w)
    for i,j,k in combinations(range(4),3):
        assert odds[i,j]*odds[j,k]==odds[i,k]
    # Context-dependent or cyclic odds reject a fixed-priority interpretation.
    bad={(0,1):Q(2),(1,2):Q(2),(0,2):Q(1,2)}
    assert bad[0,1]*bad[1,2]!=bad[0,2]
    # An unweighted row-sum repair does not generally balance the nonlinear law.
    write('weak_bias_and_identification.json',{'status':'PASS','symbolic_C':str(C),
        'C_over_s_squared_limit':'5/216','examples':examples,
        'relative_priorities_recovered':recovered,'original_normalized_priorities':tuple(x/w[0] for x in w),
        'pair_odds':odds,'incompatible_odds_example':bad,
        'scope':'Variance crossover exact; full critical triangular-array distribution not asserted.'})


def main():
    start=perf_counter()
    exhaustive_small();print('finite laws ok',flush=True)
    matrix_conditions();print('balance classes ok',flush=True)
    cycle_and_surviving_four();print('examples ok',flush=True)
    first_choice_and_rotation();print('first choice invariance ok',flush=True)
    weak_bias_and_calibration();print('weak bias and calibration ok',flush=True)
    write('execution.json',{'status':'PASS','elapsed_seconds':perf_counter()-start,'counter':dict(COUNTS),
        'python':sys.version,'sympy':sp.__version__,
        'arithmetic':'Fractions and SymPy exact rationals; all displayed decimals are derived views',
        'native_brc_git_blob':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
        'scope':'Five result files plus this execution record; finite checks complement self-contained general proofs.'})
    print(dict(COUNTS))

if __name__=='__main__':main()
