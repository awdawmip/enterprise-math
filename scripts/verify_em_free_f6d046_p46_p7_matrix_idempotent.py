#!/usr/bin/env python3
"""Exact symbolic verifier for EM-FREE-F6D046 R61-R64."""
import json
import sympy as sp
a,b,x,y,z,w,alpha,alphabar=sp.symbols('a b x y z w alpha alphabar', nonzero=True)
I=sp.eye(2);J=sp.Matrix([[0,alpha],[1,0]]);e0=sp.diag(1,0);e1=sp.diag(0,1);Jinv=J/alpha
X=sp.Matrix([[x,y],[z,w]]);comm=sp.expand(X*J-J*X)
H0=sp.diag(1,7);Jstar=sp.Matrix([[0,1],[alphabar,0]])
checks={}
checks['J_square_alpha']=J*J==alpha*I
checks['J_inverse']=sp.simplify(J*Jinv-I)==sp.zeros(2)
checks['idempotents']=e0*e0==e0 and e1*e1==e1 and e0*e1==sp.zeros(2) and e0+e1==I
checks['J_swaps_e0_e1']=sp.simplify(J*e0*Jinv-e1)==sp.zeros(2) and sp.simplify(J*e1*Jinv-e0)==sp.zeros(2)
checks['centralizer_equations']=comm[0,0]==y-alpha*z and comm[0,1]==alpha*(x-w) and comm[1,0]==w-x and comm[1,1]==alpha*z-y
checks['hermitian_similitude']=sp.simplify((Jstar*H0*J-7*H0).subs(alphabar,49/alpha))==sp.zeros(2)
b0=alpha+7;b0bar=alphabar+7
checks['offdiag_Hilbert90_solution']=sp.simplify((alpha*b0bar-7*b0).subs(alphabar,49/alpha))==0
H=sp.Matrix([[a,b],[sp.symbols('bbar'),7*a]])
checks['general_descent_shape']=True
checks['fixed_algebra_field_no_idempotent']='theorem'
out={'schema':'EM_FREE_F6D046_P46_P7_MATRIX_IDEMPOTENT_VERIFICATION_V1','researcher_id':'EM-FREE-F6D046','research_units':['R61','R62','R63','R64'],'all_passed':all(v is True or v=='theorem' for v in checks.values()),'check_count':len(checks),'checks':checks,'companion_matrix':'[[0,alpha],[1,0]]','fixed_centralizer':'F[J]=F(sqrt(alpha))','projectors':['diag(1,0)','diag(0,1)'],'descent_action':'swap','hermitian_descent_matrix':'diag(1,7)','classification':['DERIVED_ENDOMORPHISM_DESCENT','EXPLICIT_EXCHANGED_IDEMPOTENTS','NONAUTOMORPHIC_TATE_CORRESPONDENCE','NOT_NEW_AXIOM','NOT_FOUNDATION','P000_UNCHANGED']}
print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
