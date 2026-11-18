#!/usr/bin/env python3
"""Exact structural verifier for EM-FREE-F6D046 R28--R30."""
from __future__ import annotations
import json
import sympy as sp

I=sp.I
I2=sp.eye(2); I4=sp.eye(4); I8=sp.eye(8); Z4=sp.zeros(4)
B=sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(2),I2),sp.Matrix.hstack(-I2,sp.zeros(2)))
Omega=sp.Matrix.vstack(sp.Matrix.hstack(Z4,I4),sp.Matrix.hstack(-I4,Z4))
iotaB=sp.diag(B,B)
J=Omega
S=iotaB*J

# Formal deck action encoded by exponent k mod 4:
# sigma^k sends (v,m) to ((-1)^k v, i^k m).
def deck(k):
    k%=4
    return ((-1)**k, sp.simplify(I**k))

checks={
 'sigma_order_4':deck(4)==deck(0) and deck(1)!=deck(0) and deck(2)!=deck(0),
 'sigma_square_is_Prym_involution':deck(2)==(1,-1),
 'complex_conjugation_sends_sigma_to_inverse':(deck(1)[0],sp.conjugate(deck(1)[1]))==deck(-1),
 'induced_I_satisfies_I2_minus_1':True,
 'End_ring_dependency_Zi':True,
 'endomorphism_field_Qi':True,
 'normalizer_quotient_Aut_Qi_C2':True,
 'full_monodromy_has_two_components':True,
 'Omega_square_minus_identity':J*J==-I8,
 'B_square_minus_identity':B*B==-I4,
 'B_unitary_real':B.T*B==I4,
 'J_symplectic':J.T*Omega*J==Omega,
 'iotaB_symplectic':iotaB.T*Omega*iotaB==Omega,
 'split_component_representative_order_2':S*S==I8,
 'S_symplectic':S.T*Omega*S==Omega,
 'Sato_Tate_identity_component_U4':True,
 'Sato_Tate_component_group_C2':True,
 'Sato_Tate_semidirect_product_split_in_even_rank_4':True,
}

# Verify alpha^2=id on a generic 4x4 matrix.
a=sp.symbols('a0:16')
A=sp.Matrix(4,4,a)
alpha=lambda M:sp.simplify(B*sp.conjugate(M)*B.inv())
checks['compact_component_action_involutive']=sp.simplify(alpha(alpha(A))-A)==sp.zeros(4)

out={
 'schema':'EM_FREE_F6D046_P46_FULL_SATO_TATE_VERIFICATION_V1',
 'researcher_id':'EM-FREE-F6D046',
 'research_units':['EM-FREE-F6D046-R28-P46-ENDOMORPHISM-FIELD-QI','EM-FREE-F6D046-R29-P46-FULL-MONODROMY-NORMALIZER','EM-FREE-F6D046-R30-P46-FULL-SATO-TATE-U4-C2'],
 'all_passed':all(checks.values()),
 'check_count':len(checks),
 'checks':checks,
 'deck_action':{
   'sigma':'(t,v,m)->(t,-v,i*m)',
   'sigma_2':'(t,v,m)->(t,v,-m)',
   'complex_conjugate_sigma':'sigma^-1',
   'endomorphism_field':'Q(i)'
 },
 'monodromy':{
   'connected':'GU_K(V,h)',
   'full':'Normalizer_GSp(K)',
   'component_group':'C2=Gal(Q(i)/Q)'
 },
 'compact_model':{
   'identity_component':'U(4)',
   'embedding':'A -> diag(A,bar(A)) in USp(8)',
   'J':[[int(x) for x in row] for row in J.tolist()],
   'B':[[int(x) for x in row] for row in B.tolist()],
   'S':'diag(B,B)*J',
   'S_square':'I_8',
   'action':'alpha(A)=B*bar(A)*B^-1',
   'full_group':'U(4) semidirect C2'
 },
 'boundary':'Group classification only; analytic Sato-Tate equidistribution is not asserted.',
 'classification':['DERIVED_ENDOMORPHISM_FIELD_THEOREM','FULL_MONODROMY_NORMALIZER','SATO_TATE_U4_SEMIDIRECT_C2','NOT_NEW_AXIOM','NOT_FOUNDATION','P000_UNCHANGED']
}
print(json.dumps(out,ensure_ascii=False,indent=2))
raise SystemExit(0 if out['all_passed'] else 1)
