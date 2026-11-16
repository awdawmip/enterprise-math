#!/usr/bin/env python3
"""Exact finite regression and constructive witnesses for support-trimmed PF3 criterion.

Arithmetic: Python arbitrary-precision signed integers. Input exhaustive over
all lists length 1..6 with entries 0,1,2,3; zero sequence handled separately.
For every rejected input the returned 2x2 or 3x3 minor is checked negative.
For every accepted input, all 1x1,2x2,3x3 minors of its 8x8 Toeplitz cut are
independently enumerated (the mathematical general result uses a proof, not
this finite cut). No randomness, floating point, or package dependencies.
"""
from itertools import combinations, product
from hashlib import sha256
import json


def get(a, k):
    return a[k] if 0 <= k < len(a) else 0


def det(rows):
    m = len(rows)
    if m == 1:
        return rows[0][0]
    if m == 2:
        return rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
    if m == 3:
        x, y, z = rows
        return (x[0] * (y[1]*z[2] - y[2]*z[1])
                -x[1] * (y[0]*z[2] - y[2]*z[0])
                +x[2] * (y[0]*z[1] - y[1]*z[0]))
    raise ValueError('Only 1..3 supported')


def toeplitz_minor(a, rr, cc):
    return det([[get(a, j-i) for j in cc] for i in rr])


def diagnose(a):
    support = [i for i, value in enumerate(a) if value > 0]
    if not support:
        return ('PF3', None)
    p, q = support[0], support[-1]
    for k in range(p+1, q):
        if a[k] == 0:
            t = p
            u = next(u for u in support if u > k)
            return ('gap', ((0, k-t), (k, u)))
    b = a[p:q+1]
    n = len(b)-1
    for j in range(1, n):
        d2 = b[j]*b[j]-b[j-1]*b[j+1]
        if d2 < 0:
            return ('d2_negative', ((0,1), (p+j, p+j+1)))
        if d2 == 0:
            # FIRST nonpositive D2: earlier D2 values are strictly positive.
            return ('d2_zero', ((0,1,2), (p+j,p+j+1,p+n+1)))
    for j in range(1, n):
        value = toeplitz_minor(b, (0,1,2), (j,j+1,j+2))
        if value < 0:
            return ('d3_negative', ((0,1,2), (p+j,p+j+1,p+j+2)))
    return ('PF3', None)


def check_all_minors_of_cut(a, N):
    tested=0
    for m in (1,2,3):
        for rr in combinations(range(N),m):
            for cc in combinations(range(N),m):
                v=toeplitz_minor(a,rr,cc)
                tested+=1
                if v < 0:
                    return False,tested,(rr,cc,v)
    return True,tested,None


def main():
    counters={k:0 for k in ('PF3','zero_sequence','gap','d2_negative','d2_zero','d3_negative')}
    certified=0
    accepted_cut_minors=0
    digest=sha256()
    examples={}
    N=8
    for L in range(1,7):
        for raw in product(range(4),repeat=L):
            a=list(raw)
            label,witness=diagnose(a)
            if not any(a):
                counters['zero_sequence']+=1
            counters[label]+=1
            if witness is not None:
                rr,cc=witness
                v=toeplitz_minor(a,rr,cc)
                assert v < 0, (a,label,rr,cc,v)
                # For first zero at j, the exact R474 identity is independently verified.
                if label=='d2_zero':
                    p=next(i for i,x in enumerate(a) if x)
                    q=max(i for i,x in enumerate(a) if x)
                    b=a[p:q+1]; j=cc[0]-p
                    dm=b[j-1]**2 - get(b,j-2)*b[j]
                    assert dm>0
                    assert v * b[j-1] == -b[-1]*b[j]*dm
                certified+=1
                examples.setdefault(label,{'a':a,'rows':rr,'columns':cc,'det':v})
            else:
                good, amount, neg=check_all_minors_of_cut(a,N)
                assert good,(a,neg)
                accepted_cut_minors+=amount
            digest.update(json.dumps([L,a,label,witness],separators=(',',':')).encode('ascii')+b'\n')
    assert counters['PF3']+certified==sum(4**L for L in range(1,7))
    check=[1,0,0,1]
    label,wit=diagnose(check)
    assert label=='gap' and toeplitz_minor(check,*wit)==-1
    out={
        'schema':'EM_PF3_ZERO_SUPPORT_CERTIFICATE_V1',
        'date':'2026-11-02',
        'input':'all length L=1..6 arrays over {0,1,2,3}, including zero arrays',
        'arithmetic':'exact signed integers, no floating point',
        'cut_dimension':N,
        'total_inputs':sum(4**L for L in range(1,7)),
        'classification':counters,
        'negative_witnesses_checked':certified,
        'all_minors_checked_for_accepted_on_8x8_cut':accepted_cut_minors,
        'classification_sha256':digest.hexdigest(),
        'example_by_failure':examples,
        'manual_gap_example':{'a':check,'rows':wit[0],'columns':wit[1],
                               'det':toeplitz_minor(check,*wit)},
        'status':'EXACT_FINITE_REGRESSION_PASS',
        'scope':'finite exact regression only; general theorem established by analytic argument'
    }
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
