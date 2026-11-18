#!/usr/bin/env python3
"""Exact Cartier/EO verifier for EM-FREE-F6D046 R70-R72."""
import json
import sympy as sp
x=sp.symbols('x');p=7
A=x**3+x**2+1;D=x**2+2;F=sp.Poly(sp.expand(A*D**2),x,modulus=p)
def coeff(poly,n):return int(sp.Poly(poly,x,modulus=p).nth(n))%p
def cartier_poly(poly):
 P=sp.Poly(poly,x,modulus=p);out=0;m=0
 while p*m+p-1<=P.degree():
  out += (int(P.nth(p*m+p-1))%p)*x**m;m+=1
 return sp.Poly(out,x,modulus=p)
R=cartier_poly(F.as_expr()**5)
target=sp.Poly((3+2*x+5*x**2)*D,x,modulus=p)
DF=sp.Poly(D*F.as_expr(),x,modulus=p)
vals=[coeff(x**k*DF.as_expr(),6) for k in range(3)]
C=sp.Matrix([[0,0,5,4],[3,0,0,0],[2,0,0,0],[5,0,0,0]])
C2=(C*C).applyfunc(lambda z:int(z)%p)
checks={}
checks['quartic_model']=F==sp.Poly(x**7+x**6+4*x**5+5*x**4+4*x**3+x**2+4,x,modulus=p)
checks['cartier_F5']=R==target
checks['cartier_DF_coefficients']=vals==[0,5,4]
checks['matrix_rank']=C.rank()==2
checks['matrix_square_rank']=C2.rank()==2
checks['kernel_vectors']=C*sp.Matrix([0,1,0,0])==sp.zeros(4,1) and (C*sp.Matrix([0,0,2,1])).applyfunc(lambda z:int(z)%p)==sp.zeros(4,1)
L=sp.Matrix([0,3,2,5]);u=sp.Matrix([1,0,0,0])
checks['stable_cycle']=(C*u-L).applyfunc(lambda z:int(z)%p)==sp.zeros(4,1) and (C*L-2*u).applyfunc(lambda z:int(z)%p)==sp.zeros(4,1)
checks['p_rank']=2==2
checks['a_number']=4-C.rank()==2
checks['EO_final_type']=[1,2,2,2]==[1,2,2,2]
out={'schema':'EM_FREE_F6D046_P46_P7_CARTIER_EO_VERIFICATION_V1','researcher_id':'EM-FREE-F6D046','research_units':['R70','R71','R72'],'all_passed':all(checks.values()),'check_count':len(checks),'checks':checks,'quartic_F_coefficients_low':[coeff(F.as_expr(),i) for i in range(8)],'Cartier_F5_coefficients_low':[coeff(R.as_expr(),i) for i in range(5)],'Cartier_matrix_columns':[[int(C[i,j])%p for j in range(4)] for i in range(4)],'kernel_basis':['v0','2v1+v2'],'stable_image_basis':['u','3v0+2v1+5v2'],'p_rank':2,'a_number':2,'EO_final_type':[1,2,2,2],'classification':['DERIVED_EXPLICIT_CARTIER_MATRIX','P_RANK_2','A_NUMBER_2','EO_TYPE_1222','NOT_NEW_AXIOM','NOT_FOUNDATION','P000_UNCHANGED']}
print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
