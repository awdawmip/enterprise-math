#!/usr/bin/env python3
"""R749STO: exact rational single-read fiber classification.
Auxiliary scalar model frozen at a72226e2430ffa4786321ac86e7f0c599d5f0389.
Requires Python 3 + SymPy. No floating-point inputs or mesh search.
"""
import hashlib
import json
from fractions import Fraction
from math import prod
from pathlib import Path
import sympy as s

W = (1, 1, 2, 3, 6)
j = s.Symbol('j', integer=True)
LIMIT = 8000
part = [0]*(LIMIT+1)
part[0] = 1
for w in W:
    for n in range(w,LIMIT+1):
        part[n] += part[n-w]
C=[0]*(LIMIT+1);T=[0]*(LIMIT+1)
for n in range(1,LIMIT+1):
    C[n]=C[n-1]+part[n-1]
    T[n]=T[n-1]+C[n-1]

def S(n):
    return 18*n**4 + 54*n**3 - 345*n**2 + 2070*n - 16315

def y(n,e,d):
    return s.Rational(n**3*(T[n]+e), C[n]+d) - s.Rational(S(n),108)

def poly_ct(q):
    """Within one residue mod 6, C and T have degrees <=5, <=6.
    This follows from the rational generating functions specified in the note.
    Interpolation is exact because the degree bounds are known a priori.
    """
    cp=s.Poly(s.interpolate([(k,C[q+6*k]) for k in range(6)],j),j)
    tp=s.Poly(s.interpolate([(k,T[q+6*k]) for k in range(7)],j),j)
    for k in range(7,12):
        assert cp.eval(k)==C[q+6*k]
        assert tp.eval(k)==T[q+6*k]
    return cp.as_expr(),tp.as_expr()

def certificates(q,p):
    cq,tq=poly_ct(q);cp,tp=poly_ct(p)
    n=q+6*j;m=p+6*j
    # The two extreme differences, with strictly positive denominators:
    # A = 108*(C_n+2)*(C_m-2)*[Y_n(-2,+2)-Y_m(+2,-2)]
    # B = 108*(C_n-2)*(C_m+2)*[Y_n(+2,-2)-Y_m(-2,+2)]
    a=s.Poly(s.expand(108*(n**3*(tq-2)*(cp-2) - m**3*(tp+2)*(cq+2))
                     -(S(n)-S(m))*(cq+2)*(cp-2)),j)
    b=s.Poly(s.expand(108*(n**3*(tq+2)*(cp+2) - m**3*(tp-2)*(cq-2))
                     -(S(n)-S(m))*(cq-2)*(cp+2)),j)
    assert a.degree()==b.degree()==9
    for k in (0,1,5,9):
        n0=q+6*k;m0=p+6*k
        assert a.eval(k)==108*(C[n0]+2)*(C[m0]-2)*(y(n0,-2,2)-y(m0,2,-2))
        assert b.eval(k)==108*(C[n0]-2)*(C[m0]+2)*(y(n0,2,-2)-y(m0,-2,2))
    return a,b

def positive_coeffs(poly):
    return all(c>0 for c in poly.all_coeffs())

def serialize(poly):
    return [str(c) for c in reversed(poly.all_coeffs())]

def run():
    A1,B1=certificates(73,265)
    assert positive_coeffs(-A1) and positive_coeffs(B1)
    A2,B2=certificates(77,7859)
    first=[s.Rational(A2.eval(k),108*(C[77+6*k]+2)*(C[7859+6*k]-2)) for k in range(23)]
    assert all(z>0 for z in first)
    delta=min(first)
    assert delta==first[22]
    assert delta==s.Rational(2781963755899710066647,603273189896095648315920)
    # The power-basis coefficients furnish a universal certificate for ALL t>=0.
    down=s.Poly(-A2.as_expr().subs(j,j+23),j)
    up=s.Poly(B2.as_expr().subs(j,j+23),j)
    assert positive_coeffs(down) and positive_coeffs(up)
    assert A2.eval(22)>0>A2.eval(23)
    result={
      'unit':'R749STO',
      'source_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'evidence':'AUTHOR_EXACT_NOT_REVIEWED',
      'method':'exact integer counting; degree-certified quasi-polynomial interpolation; rational coefficient signs',
      'model_weights':W,
      'pair_73_265':{
          'all_j':'j >= 0: one-read exact collision exists for at least one legal nuisance quadruple for each j',
          'negative_A_coefficients':serialize(-A1),
          'positive_B_coefficients':serialize(B1)},
      'pair_77_7859':{
          'j_0_to_22':'every legal nuisance quadruple yields strictly positive first-read difference',
          'j_23_on':'one-read exact collision exists for at least one legal nuisance quadruple for each integer j >= 23',
          'minimum_gap_first_23':str(delta),
          'minimum_gap_at_j':22,
          'finite_23_positive_A':True,
          'negative_A_shift_23_coefficients':serialize(down),
          'positive_B_shift_23_coefficients':serialize(up),
          'noise_if_each_readout_error_le_eta':'uniform early separation when 2*eta < minimum_gap_first_23'},
      'scope':'Independent nuisance parameters may vary with the chosen index j. No simultaneous multi-index collision is asserted.',
      'prior_two_read':'R749STN: for 73,265 two-read H(j)>0 at j>=37; for 77,7859 at j>=1.',
      'integer_count_checks':{'dynamic_program_max_n':LIMIT,'interpolation_off-grid_per_pair':10,
                              'extreme_numerator_crosschecks_per_pair':4}
    }
    content=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    out=Path(__file__).with_name('R749STO_ONE_READ_FIBER_PHASE_RESULTS.json')
    out.write_text(content,encoding='utf-8')
    print('PASS: 40 infinite-halfline coefficients, 23 finite signs; 4 exact numerator crosschecks per pair')
    print('delta',delta,'numerator degrees',A1.degree(),B1.degree(),A2.degree(),B2.degree())
    print('sha256(json)=',hashlib.sha256(content.encode()).hexdigest())
if __name__=='__main__': run()
