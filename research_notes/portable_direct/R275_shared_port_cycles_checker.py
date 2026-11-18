#!/usr/bin/env python3
"""Exact rational checks for R275 shared-Port cycle feedback (Python stdlib only)."""
from fractions import Fraction as F
import json

P = 13

def vp(x):
    x = F(x)
    if x == 0:
        return None
    n, d = abs(x.numerator), x.denominator
    z = 0
    while n % P == 0:
        n //= P
        z += 1
    while d % P == 0:
        d //= P
        z -= 1
    return z

def residue(x):
    x = F(x)
    assert vp(x) is not None and vp(x) >= 0
    n, d = x.numerator, x.denominator
    while n % P == 0 and d % P == 0:
        n //= P
        d //= P
    return (n * pow(d, -1, P)) % P

def determinant(matrix):
    a = [[F(v) for v in row] for row in matrix]
    n = len(a)
    det = F(1)
    for i in range(n):
        j = next((j for j in range(i, n) if a[j][i]), None)
        if j is None:
            return F(0)
        if j != i:
            a[j], a[i] = a[i], a[j]
            det = -det
        pivot = a[i][i]
        det *= pivot
        for j in range(i+1, n):
            factor = a[j][i] / pivot
            for h in range(i+1, n):
                a[j][h] -= factor * a[i][h]
            a[j][i] = F(0)
    return det

def inverse_entry00(w):
    n = len(w)
    a = [[F(int(i == j)) - w[i][j] for j in range(n)] for i in range(n)]
    return determinant([row[1:] for row in a[1:]]) / determinant(a)

def three_port(a,b,c,d,e,f):
    return [[F(0),a,c],[b,F(0),e],[d,f,F(0)]]

def row_strict(w):
    return all(sum(row) < 1 for row in w)

records=[]
for t in range(1, 9):
    pow13 = P ** t
    a=c=F(1,4)
    b=d=F(2,1+pow13)
    results={}
    for label, e in [('bouquet', F(0)),('fixed_cross',F(1,8)),
                     ('depth_t_cross',F(pow13,4*(1+pow13)))]:
        f=e
        w=three_port(a,b,c,d,e,f)
        assert row_strict(w)
        D=1-a*b-c*d-e*f-a*e*d-c*f*b
        assert determinant([[int(i==j)-w[i][j] for j in range(3)]
                            for i in range(3)]) == D
        got=inverse_entry00(w)
        assert got == (1-e*f)/D
        if label=='bouquet':
            assert D == F(pow13,1+pow13)
            assert vp(got)==-t and residue(pow13*got)==1
        elif label=='fixed_cross':
            assert D == F(9*(7*pow13-1),64*(1+pow13))
            assert got == F(7*(1+pow13),7*pow13-1)
            assert vp(got)==0 and residue(got)==6
        else:
            assert D == F(3*pow13*(4+5*pow13),16*(1+pow13)**2)
            assert vp(got)==-t and residue(pow13*got)==10
        results[label]={'v13_determinant':vp(D),'v13_star00':vp(got),
                        'mod13_normalized':residue(pow13*got)
                          if label!='fixed_cross' else residue(got)}
    Q=F(1,2*(1+pow13))
    assert vp(1/(1-Q)) == 0
    records.append({'t':t,'cases':results})

# Exact insufficient-quotient witness with the same original hub star.
a=c=F(1,4)
prior_a=three_port(a,F(1,4),c,F(1,2),F(0),F(0))
prior_b=three_port(a,F(1,2),c,F(1,4),F(0),F(0))
assert row_strict(prior_a) and row_strict(prior_b)
assert inverse_entry00(prior_a) == inverse_entry00(prior_b) == F(16,13)
prior_a[0][1] += F(1,8)
prior_b[0][1] += F(1,8)
assert row_strict(prior_a) and row_strict(prior_b)
assert inverse_entry00(prior_a) == F(32,25)
assert inverse_entry00(prior_b) == F(4,3)

print(json.dumps({'status':'PASS','prime':P,'checked_t_range':[1,8],
                  'cases_per_t':3,'exact_independent_determinant_checks':24,
                  'witness':{'baseline':'16/13','after_edge_addition_A':'32/25',
                             'after_edge_addition_B':'4/3'},'cases':records},
                 ensure_ascii=False,sort_keys=True,indent=2))
