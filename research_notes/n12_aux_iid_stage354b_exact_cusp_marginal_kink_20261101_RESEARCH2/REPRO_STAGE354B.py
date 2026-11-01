#!/usr/bin/env python3
"""Exact Fraction certificate for Stage354-B restricted-arc phase-transition slopes.
Requires the immutable Stage351 right-arc checker; its module-level root,
16-tag, curvature, and sign assertions are executed on import.
"""
from fractions import Fraction as F
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import os,sys
assert __debug__
prior=os.environ.get('EM_STAGE351B_CHECKER')
if prior is None:
    prior=Path(__file__).resolve().parent.parent/'n12_aux_iid_stage351b_exact_cusp_onset_20261101_RESEARCH2'/'REPRO_STAGE351B.py'
sp=spec_from_file_location('stage351_exact_source',str(prior))
assert sp and sp.loader and Path(prior).is_file()
m=module_from_spec(sp)
sys.modules[sp.name]=m
sp.loader.exec_module(m)
I=m.I
# Every endpoint is a certified rational isolator of the actual algebraic point.
X0=I(m.xs0,m.xs1);Y0=I(m.star_ylo,m.star_yhi)
Xc=I(m.xc_lo,m.xc_hi);Yc=I(m.yc_lo,m.yc_hi)
zero=m.phi_prime_interval(X0,Y0,False)
left=m.phi_prime_interval(Xc,Yc,False)
right=m.phi_prime_interval(Xc,Yc,True)
# Interval subtraction produces outward rational enclosure of exact differences.
value_jump=zero-left
source_tag_jump=right-left
reallocation=right-zero
assert F('0.08273') < value_jump.lo <= value_jump.hi < F('0.08274')
assert F('0.11665') < source_tag_jump.lo <= source_tag_jump.hi < F('0.11666')
assert F('0.03392') < reallocation.lo <= reallocation.hi < F('0.03393')
# Algebraic identity: the only switching source word is (y,3/4,k=2):
# Delta c_y = (21/256)*B2'(y_c), with B2'(y)=y(2-3y).
rx,ry,yp,bx,by,bp,cx,cy,cp=m.arc_terms(Xc,Yc,False)
exact_tag_jump_enclosure=I(F(21,256))*Yc*(2-3*Yc)*yp/bp
assert source_tag_jump.lo < exact_tag_jump_enclosure.hi
assert exact_tag_jump_enclosure.lo < source_tag_jump.hi
assert F('0.11665') < exact_tag_jump_enclosure.lo
assert exact_tag_jump_enclosure.hi < F('0.11666')
# H(E)=old-endpoint cost - cusp-split cost.
# On (E_cusp, 0.0022] its derivative is phi'_+(E)-phi'_-(E-E_cusp).
# Stage351 brackets the FULL relevant post-cusp and near-star rectangles.
assert m.R.lo-m.L.hi > F(3,100)
assert m.sc_lo>0 and m.sc_hi < m.E_MAX < 2*m.sc_lo
print('STAGE354B_RESTRICTED_CUSP_PHASE_TRANSITION_FRACTION_PASS')
print('optimized_value_slope_jump: 0.08273 < J < 0.08274')
print('unoptimized_source_tag_jump: 0.11665 < U < 0.11666')
print('reallocation_slope_advantage: 0.03392 < A < 0.03393')
print('source_tag_jump_identity: U = (21/256)*B2prime(y_cusp)*Y1prime(x_cusp)/bprime(x_cusp)')
print('strict_gap_all_post_cusp_budgets: old_minus_split > (3/100)*(E-E_cusp)')
print('value_shape: strictly_concave_each_piece; upward_kink; neither_global_convex_nor_concave')
print('scope: original 16-word labels; right r1=0 arc only; portable author; unreviewed')
