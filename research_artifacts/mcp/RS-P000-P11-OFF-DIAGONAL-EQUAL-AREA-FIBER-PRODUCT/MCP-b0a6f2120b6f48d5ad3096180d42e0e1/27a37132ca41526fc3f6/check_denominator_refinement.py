#!/usr/bin/env python3
"""Predeclared exact integer-gcd regression; no new point search."""
from fractions import Fraction
from math import gcd
import json
from pathlib import Path

def numerators(p,q,r,s):
    n=[]
    for a in (41,29,1):
        n.extend([132*q*q-p*p-a*p*q,132*q*q-p*p+a*p*q])
    for a in (r,s):
        n.extend([132*q*q-a*p,132*q*q+a*p])
    for a in (47,37,23):
        n.extend([132*q*q+p*p-a*p*q,132*q*q+p*p+a*p*q])
    return n

def formula(p,q,r,s):
    n=numerators(p,q,r,s)
    actual=gcd(*n)
    v2=(p & -p).bit_length()-1
    expected=gcd(p,33)*(2 if p%2 else 8 if v2==2 else 4)
    assert actual==expected,(p,q,r,s,actual,expected)
    assert (2*p*q)%actual==0
    D=(2*p*q)//actual
    closed=(p*q//gcd(p,132))*(2 if v2>=3 else 1)
    assert D==closed
    assert gcd(*(a//actual for a in n))==1
    return actual,D

def main():
    b=Path(__file__).parent
    old=json.loads((b/'offdiag_checks.json').read_text())
    points=[]
    for row in old['rows']:
        d=Fraction(row['d']);p,q=d.numerator,d.denominator
        r,s=Fraction(row['mu'])*q,Fraction(row['nu'])*q
        assert r.denominator==s.denominator==1
        g,D=formula(p,q,int(r),int(s))
        assert D==row['D']
        points.append({'n':row['n'],'numerator_gcd':g,'D_matches':True})
    count=0;cases={'p_odd':0,'v2_p_eq_2':0,'v2_p_ge_3':0}
    for p in range(1,33):
        for q in range(1,16,2):
            if gcd(p,q)!=1 or p%4==2:
                continue
            samples=[(0,0),(4,8)] if p%2 else [(1,1),(3,5)]
            for r,s in samples:
                formula(p,q,r,s);count+=1
                key='p_odd' if p%2 else 'v2_p_eq_2' if p%8 else 'v2_p_ge_3'
                cases[key]+=1
    out={'schema':'P11_DENOMINATOR_REFINEMENT_REGRESSION_V1','all_checks_passed':True,
         'old_point_checks':points,'artificial_integer_gcd_cases':count,
         'case_counts':cases,'artificial_cases_are_curve_points':False,
         'finite_testing_is_global_proof':False}
    (b/'denominator_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
