#!/usr/bin/env python3
"""Exact verifier for EM-FREE-F6D046 R56-R57."""
import json
import sympy as sp
p=7
def mul(x,y):return ((x[0]*y[0]+5*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def inv(x):
 n=(x[0]*x[0]-5*x[1]*x[1])%p;ni=pow(n,-1,p)
 return (x[0]*ni%p,-x[1]*ni%p)
def div(x,y):return mul(x,inv(y))
def sq(x):return mul(x,x)
r=(0,1);a0=(1,2);a1=(5,6);a2=r;a3=(2,6);a4=(6,2)
checks={}
checks['r_square_5']=sq(r)==(5,0)
checks['all_coefficients_nonzero']=all(a!=(0,0) for a in [a0,a1,a2,a3,a4])
lam=div(a0,a4);c=div(a1,a3)
checks['lambda_5r']=lam==(0,5)
checks['c_2plus4r']=c==(2,4)
checks['c_square_2r']=sq(c)==(0,2)
checks['inversion_contradiction']=sq(c)!=lam
t=sp.symbols('t')
A=t**4+3*t**3+3*t**2+3*t+4;D=t**2+5*t+3
checks['A_factorization']=sp.Poly(A-(t-1)*(t**3+4*t**2+3),t,modulus=7).is_zero
checks['D_irreducible']=bool(sp.Poly(D,t,modulus=7).is_irreducible)
checks['cubic_A_irreducible']=bool(sp.Poly(t**3+4*t**2+3,t,modulus=7).is_irreducible)
checks['j_generic_mod7']=(-3072)%7==1 and 1 not in (0,1728%7)
out={'schema':'EM_FREE_F6D046_P46_P7_BRANCH_NORMALIZER_VERIFICATION_V1','researcher_id':'EM-FREE-F6D046','research_units':['R56','R57'],'all_passed':all(checks.values()),'check_count':len(checks),'checks':checks,'normalized_A_polynomial_coefficients_pairs':[a0,a1,a2,a3,a4],'colored_PGL2_stabilizer':'TRIVIAL','bielliptic_normalizer':'C4','boundary':'full special-fiber automorphism group remains open outside the normalizer','classification':['DERIVED_P7_BRANCH_RIGIDITY','EXACT_NORMALIZER_THEOREM','NONAUTOMORPHIC_ISOGENY_SPLITTING','NOT_NEW_AXIOM','NOT_FOUNDATION','P000_UNCHANGED']}
print(json.dumps(out,ensure_ascii=False,indent=2))
raise SystemExit(0 if out['all_passed'] else 1)
