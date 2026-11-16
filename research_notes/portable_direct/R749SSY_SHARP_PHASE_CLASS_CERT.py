#!/usr/bin/env python3
"""R749SSY, exact phase-class one-read separation at q>=501.
Requires Python 3, SymPy. All comparisons and certificates are rational/integer.
The quasi-polynomial lemma follows from the explicit rational generating functions
proved in R749SST, and is restated in the companion paper.
"""
import json
import sympy as s

WEIGHTS = (1, 1, 2, 3, 6)
N = 501
THRESHOLDS = (s.Rational(-2), s.Rational(1203, 250), s.Rational(11))
EPSILON = s.Rational(1, 100)
PHASE_CLASS = (3, 0, 1, 2, 1, 0)
K = s.Symbol('k', integer=True, nonnegative=True)


def counts(max_q):
    base = [0] * max_q
    base[0] = 1
    for w in WEIGHTS[1:]:
        for n in range(w, max_q):
            base[n] += base[n-w]
    C, T = [0] * (max_q+1), [0] * (max_q+1)
    pc = pw = 0
    for q in range(1, max_q+1):
        n = q-1
        pc += base[n]
        pw += n*base[n]
        C[q] = C[q-1] + pc
        T[q] = T[q-1] + n*pc-pw
    return C, T


def S(x):
    return 18*x**4 + 54*x**3 - 345*x**2 + 2070*x - 16315


def Y(q, e, d, C, T):
    return s.Rational(q**3 * (T[q]+e), C[q]+d) - s.Rational(S(q), 108)


def main():
    C, T = counts(150)
    assert (C[6], T[6], C[12], T[12]) == (41, 50, 380, 881)
    phase = {}
    for r in range(6):
        base = 6+r
        cp = s.expand(s.interpolate([(i,C[base+6*i]) for i in range(6)], K))
        tp = s.expand(s.interpolate([(i,T[base+6*i]) for i in range(7)], K))
        assert s.degree(cp, K) == 5 and s.degree(tp, K) == 6
        for j in range(7, 15):
            assert cp.subs(K,j) == C[base+6*j]
            assert tp.subs(K,j) == T[base+6*j]
        phase[r] = (cp,tp)
    # GF denominators and numerator periods yield exact phase polynomials
    # for all q=6+r+6k, k>=0; see companion proof.
    guards=[]
    all_coefficients=[]
    for r in range(6):
        cls = PHASE_CLASS[r]
        base=6+r
        first=N+(r-N)%6
        shift=(first-base)//6
        cp,tp=phase[r]
        cp=s.expand(cp.subs(K,K+shift))
        tp=s.expand(tp.subs(K,K+shift))
        q=first+6*K
        for idx in (cls-1, cls):
            if not 0 <= idx < 3:
                continue
            if idx == cls:  # upper-side phase must be strictly below threshold
                e,d,sgn,target = 2,-2,-1,THRESHOLDS[idx]-EPSILON
                relation='upper_below'
            else:  # lower-side phase must be strictly above threshold
                e,d,sgn,target = -2,2,1,THRESHOLDS[idx]+EPSILON
                relation='lower_above'
            P=s.Poly(s.expand(sgn*(108*q**3*(tp+e)-(S(q)+108*target)*(cp+d))),K)
            coeff=P.all_coeffs()
            assert len(coeff)==6 and all(c>0 for c in coeff)
            all_coefficients.extend(coeff)
            guards.append(dict(residue=r,first_cutoff=first,threshold_index=idx,
                               relation=relation, polynomial_degree=P.degree(),
                               minimal_coefficient=str(min(coeff))))
    assert len(guards)==9 and len(all_coefficients)==54

    # Sharpness witness: q=500 (class 1) and p=501 (class 2) share y=483/100.
    C,T=counts(502)
    y=s.Rational(483,100)
    witness=[]
    for q,e in ((500,2),(501,-2)):
        d=s.cancel(q**3*s.Rational(T[q]+e,1)/(y+s.Rational(S(q),108))-C[q])
        assert -2<=d<=2
        assert Y(q,e,d,C,T)==y
        witness.append(dict(q=q,e=e,d=str(d),C=C[q],T=T[q]))
    out={
        'id':'R749SSY','status':'PASS',
        'input_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'domain':'integer q>=501; labeled source weights (1,1,2,3,6); real e,d in [-2,2]',
        'observable':'one scalar Y_q(e,d)',
        'limit_classes':{'0':[1,5],'1':[2,4],'2':[3],'3':[0]},
        'thresholds':list(map(str,THRESHOLDS)),
        'guaranteed_absolute_measurement_noise_strictly_below':str(EPSILON),
        'phase_guard_count':len(guards),
        'strictly_positive_polynomial_coefficient_count':len(all_coefficients),
        'minimum_coefficient':str(min(all_coefficients)),
        'guards':guards,
        'sharpness':{'y':str(y),'states':witness},
        'claim':'phase LIMIT CLASS identification with one noisy read; sharp integer lower cutoff 501',
        'status_of_review':'AUTHOR_EXACT_NOT_REVIEWED',
    }
    print(json.dumps(out,indent=2,ensure_ascii=False))


if __name__ == '__main__':
    main()
