#!/usr/bin/env python3
"""Exact algebraic checks for EM-FREE-F6D046-R17.

The group-theoretic implications are proved in the accompanying theorem note;
this script verifies the displayed Weierstrass transform and invariants.
"""
import json
import sympy as sp

u,x=sp.symbols('u x')
A=u**4-24*u**2-48*u
transformed=sp.simplify((36*A/u**4).subs(u,-12/x))
a2=-6
a6=36
b2=4*a2
b4=0
b6=4*a6
b8=4*a2*a6
c4=b2**2-24*b4
disc=-b2**2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
j=sp.Rational(c4**3,disc)
checks={
  'weierstrass_transform':sp.simplify(transformed-(x**3-6*x**2+36))==0,
  'c4':c4==576,
  'discriminant':disc==-62208,
  'discriminant_factorization':sp.factorint(abs(disc))=={2:8,3:5},
  'j':j==-3072,
  'j_not_0_1728':j not in (0,1728),
}
out={
  'schema':'EM_FREE_F6D046_C46_BIELLIPTIC_NORMALIZER_VERIFICATION_V1',
  'researcher_id':'EM-FREE-F6D046',
  'research_unit':'EM-FREE-F6D046-R17-C46-BIELLIPTIC-NORMALIZER-RIGIDITY',
  'all_passed':all(checks.values()),
  'checks':checks,
  'theorem':'N_Aut(C46)(<sigma^2>)=<sigma>=C4',
  'proof_dependencies':[
    'R16 trivial exponent-colored PGL2 stabilizer',
    'Aut(E,O)={+1,-1} because j(E)=-3072',
    'kernel of descent through C46->E is <sigma^2>'
  ],
  'boundary':'Aut(C46)=C4 additionally follows once P46 geometric simplicity is independently validated.'
}
print(json.dumps(out,ensure_ascii=False,indent=2))
raise SystemExit(0 if out['all_passed'] else 1)
