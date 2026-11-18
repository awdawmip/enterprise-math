#!/usr/bin/env python3
"""R749STE exact five-read separation for (602,604).
Frozen five-labeled-source auxiliary model @a72226e2430ffa4786321ac86e7f0c599d5f0389.
AUTHOR_EXACT_NOT_REVIEWED; all calculations exact symbolic integer/rational.
"""
import hashlib
import json
from pathlib import Path
import sympy as sp

Q, P = 602, 604
WEIGHTS = (1, 1, 2, 3, 6)
MAX_N = P + 24
coeff = [0]*(MAX_N+1)
coeff[0] = 1
for wt in WEIGHTS:
    for k in range(wt, MAX_N+1):
        coeff[k] += coeff[k-wt]
C, T = [0]*(MAX_N+1), [0]*(MAX_N+1)
for n in range(1, MAX_N+1):
    C[n] = C[n-1] + coeff[n-1]
    T[n] = T[n-1] + C[n-1]
assert (C[602],T[602],C[604],T[604]) == (
    19230175073,1938941614326,19548563534,1977560635876)
assert C[608] == 20197991618 and T[608] == 2056723726251

e,d = sp.symbols('e d')
S = lambda n: 18*n**4+54*n**3-345*n**2+2070*n-16315
u, w, t = [], [], []
for j in range(5):
    a, b = Q+6*j, P+6*j
    tj = C[a]+d
    alpha = sp.Rational(a**3,b**3)
    beta = sp.Rational(S(b)-S(a),108*b**3)
    uj = sp.expand(alpha*(T[a]+e)+beta*tj)
    wj = sp.expand(C[b]*uj-T[b]*tj)
    t.append(tj);u.append(uj);w.append(wj)
A = sp.expand(w[0]*t[1]-w[1]*t[0])
B = sp.expand(u[1]*t[0]-u[0]*t[1])
polys = {}
for j in (2,3,4):
    # First two observation equalities imply A=B*D, even if B=0.
    # Each later equality implies the polynomial numerator below is zero.
    raw = sp.expand(A*(u[j]*t[0]-u[0]*t[j])-
                    (w[0]*t[j]-w[j]*t[0])*B)
    quotient, rem = sp.div(sp.Poly(raw,e,d),sp.Poly(t[0],e,d))
    assert rem.is_zero
    assert sp.expand(quotient.as_expr()*t[0]-raw)==0
    numerator = sp.together(quotient.as_expr()).as_numer_denom()[0]
    poly = sp.Poly(numerator,e,d).primitive()[1]
    assert poly.total_degree()<=3
    polys[j] = poly.as_expr()

def prim_res(f,g,variable,survivor):
    return sp.Poly(sp.resultant(f,g,variable),survivor).primitive()[1]

rd23 = prim_res(polys[2],polys[3],e,d)
rd24 = prim_res(polys[2],polys[4],e,d)
gd = sp.gcd(rd23,rd24)
a_d=423323687089090985675
b_d=894099074786485299705326337578
expected_gd=sp.Poly((d+C[602])*(d+C[608])*(a_d*d-b_d),d)
assert gd==expected_gd
assert b_d>2*a_d and C[602]>2 and C[608]>2
assert sp.gcd(sp.quo(rd23,gd),sp.quo(rd24,gd)).degree()==0

re23 = prim_res(polys[2],polys[3],d,e)
re24 = prim_res(polys[2],polys[4],d,e)
ge = sp.gcd(re23,re24)
a_e=16278056426515699712159090150
b_e=10813151975078948797440159426145393125049
expected_ge=sp.Poly((e+T[602])*(e+T[608])*(a_e*e-b_e),e)
assert ge.primitive()[1]==expected_ge.primitive()[1]
assert b_e>2*a_e and T[602]>2 and T[608]>2
assert sp.gcd(sp.quo(re23,ge),sp.quo(re24,ge)).degree()==0

record={
 'unit':'R749STE','status':'PASS','evidence':'AUTHOR_EXACT_NOT_REVIEWED',
 'source':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'predecessor':'R749STD; Draft PR #2619@749399f2ced6038e5941706e3d144880260708d2',
 'q':Q,'p':P,'weights':list(WEIGHTS),'reads':5,
 'first_four_collide_via_predecessor':True,
 'fifth_separates_all_allowed_error_states':True,
 'error_domain':'e,d,E,D in [-2,2]',
 'counts':{str(x):{'C':C[x],'T':T[x]} for x in (602,604,608)},
 'polynomial_total_degrees':{str(j):sp.Poly(polys[j],e,d).total_degree() for j in (2,3,4)},
 'resultants_in_e_degrees':{'P2_P3':rd23.degree(),'P2_P4':rd24.degree()},
 'resultants_in_d_degrees':{'P2_P3':re23.degree(),'P2_P4':re24.degree()},
 'resultant_gcd_d':str(gd.as_expr()),
 'resultant_gcd_e_primitive':str(ge.as_expr()),
 'exact_d_common_root_candidates':[str(-C[602]),str(-C[608]),str(sp.Rational(b_d,a_d))],
 'exact_e_common_root_candidates':[str(-T[602]),str(-T[608]),str(sp.Rational(b_e,a_e))],
 'no_gcd_roots_in_closed_minus2_plus2':True,
 'resultant_bit_sizes':{
  'd23':max(abs(int(x)).bit_length() for x in rd23.all_coeffs()),
  'd24':max(abs(int(x)).bit_length() for x in rd24.all_coeffs()),
  'e23':max(abs(int(x)).bit_length() for x in re23.all_coeffs()),
  'e24':max(abs(int(x)).bit_length() for x in re24.all_coeffs())},
 'proof_kernel':'SymPy exact QQ/ZZ polynomial resultants and Euclidean GCD; integer/rational only',
 'pair_optimal_exact_read_count':5,
 'global_horizon_from_predecessor_bounds':'5 <= m_* <= 11, unchanged',
 'next':'Seek five-read collisions for another cutoff pair or global upper bound below eleven; quantify finite-range noise separation.'
}
out=Path(__file__).with_name('R749STE_FIVE_READ_PAIR_SEPARATION_RESULTS.json')
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS R749STE 602 vs 604: five reads separate all [-2,2]^4 real states')
print('gcd_d:',sp.factor(gd.as_expr()))
print('gcd_e:',sp.factor(ge.as_expr()))
print('resultant degrees:',record['resultants_in_e_degrees'],record['resultants_in_d_degrees'])
print('results_sha256:',hashlib.sha256(out.read_bytes()).hexdigest())
