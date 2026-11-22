"""PREFIX-1000: independent scalar norm certificate for the frozen Stage46 X6 BRC 12-port candidate.
Frozen P000: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
C[incoming,outgoing] = (1 - 6*int(incoming == outgoing))/6.
Arithmetic in integers; final mass numerator / 36**n.
"""
from collections import defaultdict
from math import comb
from fractions import Fraction
import json
from pathlib import Path

D = 6


def collisions(max_m):
    a = [1] * (max_m + 1)
    for d in range(2, D + 1):
        a = [sum(comb(m,r)**2 * a[m-r] for r in range(m+1)) for m in range(max_m+1)]
    return a


def scalar_components(n, a):
    if n == 1:
        return 0, 30
    if n == 2:
        return 900, 180
    t = n - 2
    positive = (6*(t*t - 2*t - 1)*a[t+1]
                -432*t*(t-2)*a[t]
                +7776*(t-1)**2*a[t-1])
    negative = 216*a[t] - 6*a[t+1]
    assert positive >= 0 and negative > 0
    return positive, negative


def exact_direct(nmax=7, initial_axis=0):
    """Independent signed Cell/incoming-port BRC numerator DP with at most one negative step."""
    zero = (0,)*D
    state = {(zero, D + initial_axis, 0): 1}
    totals = {}
    for n in range(1,nmax+1):
        nxt = defaultdict(int)
        for (cell,incoming,neg), amp in state.items():
            for outgoing in range(2*D):
                minus = outgoing >= D
                if minus and neg:
                    continue
                j = outgoing % D
                k = list(cell)
                k[j] += -1 if minus else 1
                incoming_next = j if minus else D+j
                nxt[(tuple(k),incoming_next,neg+int(minus))] += amp * (1-6*int(incoming==outgoing))
        state = dict(nxt)
        plus = sum(v*v for (k,h,c),v in state.items() if c==1 and h>=D)
        minus = sum(v*v for (k,h,c),v in state.items() if c==1 and h<D)
        totals[n] = (plus,minus)
    return totals


def evaluate():
    N=70
    a=collisions(N)
    expected={1:30,2:1080,3:2700,4:48960,5:1087020,
              6:24222240,7:561368520,8:13634006400,
              9:346180688460,10:9140285567520}
    direct=exact_direct(7)
    samples={}
    for n in range(1,N+1):
        p,m=scalar_components(n,a)
        if n in direct:
            assert (p,m)==direct[n], (n,(p,m),direct[n])
        if n in expected:
            assert p+m==expected[n], (n,p+m,expected[n])
        if n<=10 or n in (16,24,40,60,70):
            samples[str(n)]={'positive_numerator':str(p),
                             'negative_numerator':str(m),
                             'total_numerator':str(p+m),
                             'positive_mass':f'{Fraction(p,36**n)}',
                             'first_negative_flux':f'{Fraction(m,36**n)}'}
    return {'schema':'PREFIX1000_R6_POSITIVE_TERMINAL_SCALAR_CERTIFICATE_V1',
            'model':'Stage46 signed BRC C=J/6-I, X6 Cell and terminal directed port',
            'frozen_p000':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'arithmetic':'exact Python integers, probability mass numerator / 36**n',
            'scalar_range':[1,N],
            'independent_direct_range':[1,7],
            'prior_prefix997_expected_range':[1,10],
            'direct_all_passed':True,
            'prior_all_passed':True,
            'samples':samples}


if __name__=='__main__':
    result=evaluate()
    with (Path(__file__).parent / 'PREFIX1000_R6_EXACT_RESULTS.json').open('w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
    print('PASS: scalar n=1..70; direct BRC 1..7; prior 1..10')
    for n in ('3','4','5','8','24'):
        print(n,result['samples'][n]['positive_numerator'],result['samples'][n]['negative_numerator'])
