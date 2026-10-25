#!/usr/bin/env python3
"""Exact auxiliary-BRC Newton-pole certificate. Python integer arithmetic only.

All-grade claims follow from the note's formal recurrence and symbolic
coefficient extraction, not from this finite regression sweep. No native X6.
"""
from __future__ import annotations
from math import comb
from fractions import Fraction
import json
from pathlib import Path

D_MAX = 120
DIRECT_GRADE = 34
DIRECT_SHIFT = 5

def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def mul_y(a, exponent):
    out = a[:]
    for _ in range(exponent):
        nxt = [0] * (len(out) + 1)
        for k, value in enumerate(out):
            nxt[k] += value
            nxt[k + 1] -= value
        out = nxt
    return out

def add_into(out, term, shift=0, multiplier=1):
    for k, value in enumerate(term):
        out[k + shift] += multiplier * value

def make_numerator_polynomials(last):
    p = []
    checked = []
    for d in range(last + 1):
        c, r = divmod(d, 3)
        n = [choose(6, d), -(choose(6, d - 1) + choose(8, d - 1)), choose(8, d - 2)]
        out = [0] * (d + c + 3)
        add_into(out, mul_y(n, c))
        if d >= 1:
            add_into(out, mul_y(p[d-1], c - (d-1)//3), shift=1, multiplier=2)
        if d >= 2:
            add_into(out, mul_y(p[d-2], c + 1 - (d-2)//3), shift=1)
        if d >= 3:
            add_into(out, p[d-3], shift=3)
        while len(out) > 1 and out[-1] == 0:
            out.pop()
        assert len(out) - 1 <= (0 if d == 0 else d + c - 1)
        p.append(out)
        A = sum(out)
        B = -sum(i * value for i, value in enumerate(out))
        predicted_A = [1, 2*c + 6, 2*c*c + 14*c + 14][r]
        assert A == predicted_A, ('leading pole', d, A, predicted_A)
        if c >= 1:
            F = Fraction(A * (2*d+c+1), 2) + B
            f_num, den = (
                (8*c**3+72*c*c+91*c-87,6),
                (2*c**4+28*c**3+85*c*c-22*c-72,3),
                (4*c**5+80*c**4+435*c**3+430*c*c-619*c+195,15)
            )[r]
            assert (F*den == f_num), ('second pole', d, F, f_num, den)
            assert F > 0, ('second-positive', d, F)
        checked.append((d,c,r,A,B))
    return p, checked

def numerator_coefficient(p, d, j):
    c=d//3
    return sum(value*choose(j-k+c, c) for k,value in enumerate(p[d]) if j >= k)

def e_rows(last):
    rows=[]
    for n in range(last+1):
        row=[0]*(n+1)
        if n==0: row[0]=1
        if n>=1:
            for j,value in enumerate(rows[n-1]):
                row[j]+=value;row[j+1]+=value
        if n>=4:
            for j,value in enumerate(rows[n-4]): row[j+2]-=2*value
        if n>=6:
            for j,value in enumerate(rows[n-6]): row[j+3]+=value
        if n==2:row[1]-=1
        rows.append(row)
    return rows

def direct_crosschecks(p):
    rows=e_rows(3*DIRECT_GRADE+DIRECT_SHIFT+6)
    total=0
    for d in range(DIRECT_GRADE+1):
        for w in range(DIRECT_SHIFT+1):
            j=d+w
            b=2*j+6
            values=[rows[b+k][j]-(rows[b+k][j-1] if j else 0) for k in range(w+1)]
            difference=sum((-1)**(w-k)*choose(w,k)*v for k,v in enumerate(values))
            via_numerator=numerator_coefficient(p,d,j)
            assert difference==via_numerator,(d,j,difference,via_numerator)
            total+=1
    return total

if __name__ == '__main__':
    polys, checked=make_numerator_polynomials(D_MAX)
    cross=direct_crosschecks(polys)
    report={
      'schema':'EM_R4_EC21_ALL_DIAGONALS_POLE_CERTIFICATE_V1',
      'scientific_status':'AUTHOR_DERIVATION_UNREVIEWED',
      'model':'E(x,u)=(1-ux^2)/(1-(1+u)x+2u^2x^4-u^3x^6)',
      'theorem':'Every q_d(d+w) is polynomial in w of exact degree floor(d/3), with explicit positive highest and second-highest coefficients',
      'uniform_formula':'A_(3c+r)=[1,2c+6,2c^2+14c+14][r]; second numerator F_r(c), c>=1, in research note',
      'proof_mechanism':'Exact rational recurrence for [t^d]H(z,t), and singular expansion at z=1; arbitrary d formulas are symbolic, not a numerical extrapolation',
      'polynomial_numerators_checked_d':D_MAX,
      'direct_E_row_crosschecks':cross,
      'direct_grades_through':DIRECT_GRADE,
      'direct_shifts_through':DIRECT_SHIFT,
      'all_grade_unimodality':'OPEN',
      'native_X6':'NOT_EXECUTED',
      'independent_driver':'NOT_REVIEWED',
      'samples':[{'d':d,'pole_order':c+1,'leading_pole_A':A,'subleading_pole_B':B} for d,c,r,A,B in checked if d in (0,1,2,3,4,5,6,7,8,14,15,16,20,35,60,90,120)],
    }
    path=Path(__file__).with_name('R4_EC21_report.json')
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'all_poly_d':D_MAX,'direct_crosschecks':cross,'sample_d120':report['samples'][-1]},ensure_ascii=False))
