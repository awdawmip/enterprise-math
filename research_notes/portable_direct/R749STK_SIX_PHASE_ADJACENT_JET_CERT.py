#!/usr/bin/env python3
"""R749STK: exact six-residue adjacent six-step cutoff jet classification.

Reproduce: python R749STK_SIX_PHASE_ADJACENT_JET_CERT.py
Requires: Python 3 and SymPy. Only exact integer/rational operations.
"""
import json
from math import factorial
from pathlib import Path
import sympy as s

N = s.Symbol('N')
e, d, E, D = s.symbols('e d E D')
W = (1, 1, 2, 3, 6)
VARIABLES = (e, d, E, D)


def convolution(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def block(weights):
    a = [1]
    for w in weights:
        a = convolution(a, [int(k % w == 0) for k in range(7-w)])
    return a


# Rational generating functions: C(z) = QC(z)/(1-z^6)^6,
# T(z) = QT(z)/(1-z^6)^7; coefficient of z^(n-1) is C_n/T_n.
QC = block((*W, 1))
QT = convolution([0, 1], block((1, 1, 1, 1, 2, 3, 6)))


def falling(t, m):
    return s.prod(t-i for i in range(m))/factorial(m)


def quasi(r):
    c = s.expand(sum(a*falling((N-1-i)/6+5, 5)
                     for i, a in enumerate(QC) if (r-1-i) % 6 == 0))
    t = s.expand(sum(a*falling((N-1-i)/6+6, 6)
                     for i, a in enumerate(QT) if (r-1-i) % 6 == 0))
    return c, t


POLYNOMIAL_PART = {-4:s.Rational(18,108), -3:s.Rational(54,108),
                   -2:s.Rational(-345,108), -1:s.Rational(2070,108),
                    0:s.Rational(-16315,108)}


def universal_jet(residue, ee, dd, last_order=5):
    """Y_n(ee,dd)=sum a_k n^-k, k=0..last_order, exact."""
    c,t=quasi(residue)
    cp,tp=s.Poly(c,N),s.Poly(t,N)
    K=last_order+4
    aa=[cp.nth(5-i) if i<=5 else s.Integer(0) for i in range(K+1)]
    bb=[tp.nth(6-i) if i<=6 else s.Integer(0) for i in range(K+1)]
    aa[5]+=dd
    bb[6]+=ee
    rr=[]
    for k in range(K+1):
        rr.append(s.expand((bb[k]-sum(aa[i]*rr[k-i] for i in range(1,k+1)))/aa[0]))
    assert all(rr[k+4]==POLYNOMIAL_PART[k] for k in (-4,-3,-2,-1))
    return [s.factor(rr[k+4]-POLYNOMIAL_PART.get(k,0)) for k in range(last_order+1)]


def shift_jet(a,q):
    """Convert n^-1 expansion to x=(6j)^-1, n=q+6j=x^-1+q."""
    return [s.expand(a[0] if k==0 else
           sum(a[h]*s.binomial(-h,k-h)*q**(k-h) for h in range(1,k+1)))
            for k in range(len(a))]


def independent_integer_counts(max_n=240):
    parts=[0]*(max_n+1)
    parts[0]=1
    for w in W:
        for i in range(w,max_n+1):
            parts[i]+=parts[i-w]
    C=[0]*(max_n+1)
    T=[0]*(max_n+1)
    for n in range(1,max_n+1):
        C[n]=C[n-1]+parts[n-1]
        T[n]=T[n-1]+C[n-1]
    for r in range(6):
        c,t=quasi(r)
        for n in range(29,max_n+1):
            if n%6==r:
                assert c.subs(N,n)==C[n]
                assert t.subs(N,n)==T[n]
    return {'n_min':29,'n_max':max_n,'residues':6}


def run():
    check=independent_integer_counts()
    phase_records=[]
    for r in range(6):
        q=78 if r==0 else 72+r
        p=q+6
        left=shift_jet(universal_jet(r,e,d),q)
        right=shift_jet(universal_jet(r,E,D),p)
        assert left[0]==right[0]
        coeffs=[s.factor(left[k]-right[k]) for k in range(1,6)]
        A,b=s.linear_eq_to_matrix(coeffs[:4],VARIABLES)
        assert A.det()==180295624949760000
        unique=s.solve(coeffs[:4],VARIABLES,dict=True)
        assert len(unique)==1
        bad=unique[0]
        assert all(s.cancel(z.subs(bad))==0 for z in coeffs[:4])
        assert bad[E]>2
        # One universal rational gauge d=D=-1 gives three-jet equality.
        witness=s.solve(coeffs[:3]+[D+1],VARIABLES,dict=True)
        assert len(witness)==1
        good=witness[0]
        assert all(-2<good[t]<2 for t in VARIABLES)
        assert all(s.cancel(z.subs(good))==0 for z in coeffs[:3])
        first=s.factor(coeffs[3].subs(good))
        assert first>0
        phase_records.append({
          'r':r,'q':q,'p':p,'common_limit':str(left[0]),
          'three_jet_witness':{str(v):str(good[v]) for v in VARIABLES},
          'first_nonzero_order':4,'fourth_difference_coefficient':str(first),
          'four_linear_equation_determinant':str(A.det()),
          'unique_unconstrained_four_jet':{str(v):str(bad[v]) for v in VARIABLES},
          'unconstrained_E_excess_over_2':str(bad[E]-2)})
    output={
      'unit':'R749STK',
      'frozen_source_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'domain':'q=b_r+6k, p=q+6, k>=0, b_r=(78,73,74,75,76,77); four fixed nuisance parameters in [-2,2]',
      'observations':'Y_{q+6j}(e,d) and Y_{p+6j}(E,D)',
      'jet_variable':'x=1/(6j)',
      'claim':'In each of six residue classes, maximal legal common asymptotic jet depth for adjacent six-step cutoffs is exactly three',
      'integer_quasipolynomial_crosscheck':check,
      'certificate':phase_records,
      'evidence_status':'AUTHOR_EXACT_NOT_REVIEWED',
      'next':'Classify arbitrary positive cutoff gap 6h and analyze finite-noise residual detectability'
    }
    path=Path(__file__).with_name('R749STK_SIX_PHASE_ADJACENT_JET_RESULTS.json')
    path.write_text(json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True)+'\n', encoding='utf-8')
    print('PASS six residues, 6/6 legal three-jet, 6/6 forbidden four-jet, integer recurrence crosscheck 29..240')
    for row in phase_records:
        print(row['r'],row['q'],row['p'],row['fourth_difference_coefficient'],row['unique_unconstrained_four_jet']['E'])
    print('results:',path.name,'bytes:',path.stat().st_size)
    return output


if __name__ == '__main__':
    run()
