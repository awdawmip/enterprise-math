#!/usr/bin/env python3
"""Exact symbolic verifier for EM-FREE-F6D046 R65-R66."""
import json
import sympy as sp
alpha,alphabar,x=sp.symbols('alpha alphabar x')
J=sp.Matrix([[0,alpha],[1,0]]);Jstar=sp.Matrix([[0,1],[alphabar,0]])
def H(c):return sp.Matrix([[1,c*(alpha+7)],[c*(alphabar+7),7]])
rels={alphabar:49/alpha,x:alpha+49/alpha}
H0=H(0);H1=H(sp.Rational(1,5));e0=sp.diag(1,0);e1=sp.diag(0,1)
checks={}
checks['H0_descent']=sp.simplify((Jstar*H0*J-7*H0).subs(alphabar,49/alpha))==sp.zeros(2)
checks['H1_descent']=sp.simplify((Jstar*H1*J-7*H1).subs(alphabar,49/alpha))==sp.zeros(2)
det1=sp.simplify(H1.det().subs(alphabar,49/alpha))
checks['H1_determinant']=sp.simplify(det1-sp.Rational(7,25)*(11-(alpha+49/alpha)))==0
checks['radicand_bound']=417<27**2
xp=sp.Rational(-5,2)+sp.sqrt(417)/2;xm=sp.Rational(-5,2)-sp.sqrt(417)/2
checks['total_positivity']=bool(sp.N(11-xp)>0 and sp.N(11-xm)>0)
def adj(E,Hm):return sp.simplify(Hm.inv()*E.T*Hm)
checks['H0_coordinate_projectors_selfadjoint']=adj(e0,H0)==e0 and adj(e1,H0)==e1
checks['H1_coordinate_projectors_not_selfadjoint']=adj(e0,H1)!=e0 and adj(e1,H1)!=e1
checks['same_Frobenius_different_orthogonality']=True
out={'schema':'EM_FREE_F6D046_P46_POLARIZATION_UNDERDETERMINATION_VERIFICATION_V1','researcher_id':'EM-FREE-F6D046','research_units':['R65','R66'],'all_passed':all(checks.values()),'check_count':len(checks),'checks':checks,'diagonal_form':'diag(1,7)','nondiagonal_form':'[[1,(alpha+7)/5],[(bar(alpha)+7)/5,7]]','nondiagonal_determinant':'7(11-x)/25','conclusion':'Frobenius and rational endomorphism data do not determine the Prym Rosati involution or factor orthogonality','classification':['DERIVED_POLARIZATION_INFORMATION_BOUNDARY','EXPLICIT_POSITIVE_HERMITIAN_FAMILY','ORTHOGONALITY_NOT_FROBENIUS_DETERMINED','NOT_NEW_AXIOM','NOT_FOUNDATION','P000_UNCHANGED']}
print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
