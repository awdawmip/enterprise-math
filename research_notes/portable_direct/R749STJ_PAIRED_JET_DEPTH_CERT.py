#!/usr/bin/env python3
"""Exact paired-phase jet-depth classification, with rational linear algebra."""
import json
from pathlib import Path
from sympy import symbols, Rational as Q, factor, solve, linear_eq_to_matrix, cancel

e,d,E,D=symbols('e d E D')
a=[
 -Q(80,9)*(-81*D+81*d-10),
 Q(80,3)*(-2808*D-162*E+2700*d+162*e-107),
 -Q(40,81)*(-15398181*D-1609632*E+14208453*d+1539648*e+312038),
 Q(40,3)*(-56875743*D-8197308*E+50298219*d+7497468*e+3495995),
]
A,b=linear_eq_to_matrix(a,(e,d,E,D))
assert A.det()==77035520655360000
s=solve(a,(e,d,E,D),dict=True)[0]
expected={e:-Q(439960,3265191),d:-Q(658787,483732),E:Q(7355183,3265191),D:-Q(718507,483732)}
assert s==expected and s[E]>2
triple={e:-Q(6455,8748),d:-1,E:Q(12319,8748),D:-Q(91,81)}
assert all(-2<triple[z]<2 for z in (e,d,E,D))
assert all(cancel(a[i].subs(triple))==0 for i in range(3))
fourth=cancel(a[3].subs(triple))
assert fourth==Q(7002200,27)>0
out={'unit':'R749STJ','phase_pair':[1,5],'base_cutoffs':[73,77],'all_cutoffs':'q=73+6k, p=q+4 for integer k>=0','unconstrained_four_jet_solution':{str(k):str(s[k]) for k in (e,d,E,D)},'determinant':str(A.det()),'invalid_error':'E=7355183/3265191>2','legal_three_jet_solution':{str(k):str(triple[k]) for k in (e,d,E,D)},'first_nonzero_coefficient':str(fourth),'proof':'first three jet coefficients zero; unique solution of four-coefficient system violates E<=2','status':'AUTHOR_EXACT_NOT_REVIEWED','cross_reference':'R749STI phase pair (2,4): four-jet legal, five-jet impossible'}
fn=Path(__file__).with_name('R749STJ_PAIRED_JET_DEPTH_RESULTS.json')
fn.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS: (1,5) maximal legal jet order 3, (2,4) order 4 via R749STI')
print('det',A.det(),'fourth coefficient',fourth,'invalid E',s[E])
