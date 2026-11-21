"""PREFIX-999 | frozen P000 V5; Stage46 12-port BRC signed-amplitude flux."""
from collections import defaultdict
from fractions import Fraction
from math import comb
import json

D = 6

def collisions(limit):
    a = [1] * (limit + 1)
    for d in range(2, D + 1):
        a = [sum(comb(m, r)**2 * a[m-r] for r in range(m+1))
             for m in range(limit+1)]
    return a

def direct_brc(limit=7):
    state = {((0,)*D, D, 0): 1}
    rows = {}
    for n in range(1, limit+1):
        nxt = defaultdict(int)
        for (cell, incoming, negatives), amp in state.items():
            for outgoing in range(2*D):
                neg = int(outgoing >= D)
                if negatives + neg > 1:
                    continue
                j = outgoing % D
                target = list(cell)
                target[j] += 1 - 2*neg
                new_incoming = j if neg else D+j
                nxt[(tuple(target), new_incoming, negatives+neg)] += amp * (
                    1 - 6*int(incoming == outgoing))
        state = nxt
        outer = sum(v*v for (cell, h, neg), v in state.items() if neg == 0)
        exit_ = sum(v*v for (cell, h, neg), v in state.items()
                    if neg == 1 and h < D)
        rows[n] = (outer, exit_)
    return rows

def frac(x):
    return f'{x.numerator}/{x.denominator}'

def run():
    limit = 60
    A = collisions(limit)
    M = {0: Fraction(1)}
    for n in range(1, limit+2):
        M[n] = Fraction(A[n-1], 6*36**(n-1))
    rows = direct_brc()
    for n, (outer, exit_) in rows.items():
        assert M[n] == Fraction(outer, 36**n)
        assert M[n-1]-M[n] == Fraction(exit_, 36**n)
    for n in range(2, limit+1):
        assert M[n-1]-M[n] == Fraction(
            216*A[n-2]-6*A[n-1], 36**n)
    assert sum((M[n-1]-M[n] for n in range(1,limit+1)), Fraction(0)) == 1-M[limit]
    ns = (1,2,3,4,5,6,7,8,10,12,24,40,60)
    return {'record':'PREFIX999_R6_EXACT_RESULTS',
            'source':'enterprise-math P000 V5@f42f2906d77f24085c123f3ccfe9667d41caa96d; Stage46 local BRC',
            'observer':'signed Cell displacement plus terminal directed port; square after coherent sum',
            'recurrence':'A_1(m)=1; A_d(m)=sum_r binom(m,r)^2 A_(d-1)(m-r)',
            'law':'F_n=M_(n-1)-M_n; M_0=1; M_n=A_6(n-1)/(6*36^(n-1))',
            'direct_BRC_checked_n':list(rows),
            'direct_BRC_integer_numerators':{str(n):{'outer':str(v[0]),'exit':str(v[1])}
                                             for n,v in rows.items()},
            'scalar_checked_n':'1..60',
            'samples':{str(n):{'M_outer':frac(M[n]),'F_first_exit':frac(M[n-1]-M[n]),
                               'F_over_M':frac((M[n-1]-M[n])/M[n])} for n in ns},
            'sum_first_exit_1_to_60':frac(1-M[60]),
            'survival_after_60':frac(M[60]),
            'asymptotic_F_n':'45/(16*pi^(5/2))*n^(-7/2)',
            'moment_threshold':'E[T^p]<infinity iff 0<=p<5/2',
            'status':'AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED'}

if __name__ == '__main__':
    result = run()
    with open('PREFIX999_R6_EXACT_RESULTS.json','w',encoding='utf-8') as file:
        json.dump(result,file,ensure_ascii=False,indent=2)
        file.write('\n')
    print('PASS exact BRC n=1..7, scalar recurrence n=1..60')
