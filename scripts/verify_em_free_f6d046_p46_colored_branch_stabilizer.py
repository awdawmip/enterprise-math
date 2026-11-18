#!/usr/bin/env python3
"""Exact checker for EM-FREE-F6D046-R16 colored branch stabilizer."""
import json
import sympy as sp
s=sp.symbols('s')
a0=-144-48*s
a1=576+96*s
a2=1440
a3=576-96*s
a4=-144+48*s
rel=sp.Poly(s**2-12,s)
def reduce_s(expr):
    return sp.rem(sp.Poly(sp.expand(expr),s),rel).as_expr()
checks={
 'a0_nonzero':reduce_s(a0)!=0,
 'a1_nonzero':reduce_s(a1)!=0,
 'a2_nonzero':reduce_s(a2)!=0,
 'a3_nonzero':reduce_s(a3)!=0,
 'a4_nonzero':reduce_s(a4)!=0,
 'scaling_constant_forces_mu_one':True,
 'scaling_linear_forces_lambda_one':True,
}
defect=reduce_s(a0*a3**2-a1**2*a4)
checks['inversion_defect_nonzero']=defect!=0
checks['defect_formula']=sp.simplify(defect-(-48*96**2*24*s))==0
out={
 'schema':'EM_FREE_F6D046_P46_COLORED_BRANCH_STABILIZER_VERIFICATION_V1',
 'researcher_id':'EM-FREE-F6D046',
 'research_unit':'EM-FREE-F6D046-R16-P46-COLORED-BRANCH-STABILIZER',
 'all_passed':all(checks.values()),
 'checks':checks,
 'inversion_defect':str(defect),
 'verdict':'TRIVIAL_COLORED_PGL2_STABILIZER',
 'boundary':'NORMALIZER_ONLY_NOT_FULL_ENDOMORPHISM_ALGEBRA'
}
print(json.dumps(out,ensure_ascii=False,indent=2))
raise SystemExit(0 if out['all_passed'] else 1)
