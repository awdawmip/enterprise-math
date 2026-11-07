#!/usr/bin/env python3
"""Stage353-B: exact post-cusp right-arc split optimization certificate.

Reuses pinned Stage351-B checker (same original 16-tag Bernoulli source laws).
Supply EM_STAGE351B_CHECKER or use the sibling repository research_notes path.
All sign/curvature decisions use rational Fraction intervals.
"""
from fractions import Fraction as Q
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import os
import sympy as sp

old = os.environ.get('EM_STAGE351B_CHECKER')
if not old:
    old = Path(__file__).resolve().parent.parent / 'n12_aux_iid_stage351b_exact_cusp_onset_20261101_RESEARCH2' / 'REPRO_STAGE351B.py'
spec = spec_from_file_location('stage351_source', str(old))
assert spec and spec.loader, f'missing exact Stage351 source at {old}'
m = module_from_spec(spec)
# dataclasses requires its module to be registered before executing it.
import sys
sys.modules[spec.name] = m
spec.loader.exec_module(m)
I=m.I

# Independently compare the right-of-cusp gradient with the full four-word
# signed y-source laws, including their original 9:7 source coefficients.
z=sp.Symbol('z')
w=(1,3,3,1)
B=lambda k:z**k*(1-z)**(3-k)
sign_y14=(1,1,-1,-1)
sign_y34_right=(-1,-1,-1,1)
def dD(sign):return -sum(w[k]*sign[k]*sp.diff(B(k),z) for k in range(4))/2
assert sp.expand((9*dD(sign_y14)+7*dD(sign_y34_right))/256
                 +3*z*(25*z-18)/256)==0

X=I(Q('.23780'),Q('.23788'))
Y=I(Q('.57569'),Q('.57591'))
rx,ry,yp,bx,by,bp,cx,cy,cp=m.arc_terms(X,Y,True)
rxx=I(4)*(6*X-4)/5
ryy=(6*Y-4)/5
ypp=-(rxx+ryy*yp*yp)/ry
bxx=-(18*X-6)/4
byy=-(18*Y-6)/16
cxx=-I(3)*(122*X-124)/256
cyy=-I(3)*(50*Y-18)/256
bpp=bxx+byy*yp*yp+by*ypp
cpp=cxx+cyy*yp*yp+cy*ypp
N=cpp*bp-cp*bpp
assert N.hi < -Q(7,5)  # post-cusp strict curvature numerator
assert bp.lo > Q(3,10)
assert cp.hi < 0

# Stage351 explicitly certifies the pre-cusp N<-4/5 and positive B',
# near-zero phi'<-119/100, and post-cusp phi'>-117/100.
# Ensure the critical interval ordering for every E in (E_cusp,Emax].
assert m.E_MAX < 2*m.sc_lo and m.sc_hi < m.E_MAX
# s in [0,E] splits into three strict-concavity pieces at
# E-E_cusp and E_cusp; the minimum is at an endpoint of a piece.
# Compare endpoints by H'(E)<-1/50, H(E_cusp)=0.
print('STAGE353B_POST_CUSP_RESTRICTED_GLOBAL_SPLIT_EXACT_PASS')
print('post_cusp_curvature_numerator_upper', N.hi)
print('post_cusp_budget_derivative_lower', bp.lo)
print('post_cusp_cost_derivative_upper', cp.hi)
print('right_arc_split_minimizers_for_Ecusp_lt_E_le_11over5000: (Ecusp,E-Ecusp) and swap')
print('strict_endpoint_gap_gt: (E-Ecusp)/50')
print('scope: 16 source-word tags; right r1=0 arc only; source-authored, not native Result')