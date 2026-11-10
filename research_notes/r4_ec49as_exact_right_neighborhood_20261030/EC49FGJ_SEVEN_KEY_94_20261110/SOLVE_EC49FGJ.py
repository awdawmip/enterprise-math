#!/usr/bin/env python3
"""Reproduce fixed-allowlist MIP classifications (not standalone UNSAT proofs).
Needs sibling EC49FGF model, SciPy and NumPy. Frozen science remains unchanged.
"""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'EC49FGF_EXACT_16_CLASS_DUAL_20261110'))
from VERIFY_EC49FGF import build
j=json.load(open(Path(__file__).with_name('WITNESSES_EC49FGJ.json'),encoding='utf8'))
for p in j['profiles']:
    c,G,h,N,d=build({tuple(k) for k in p['allowed_keys']})
    ans=milp(c=c.astype(float),integrality=np.ones(len(c),dtype=np.int8),
       bounds=Bounds(0,1),
       constraints=LinearConstraint(G,np.full(len(h),-np.inf),h),
       options={'time_limit':75.,'mip_rel_gap':0.,'disp':False})
    print(p['profile_id'],'nodes',N,'discounts',d,'status',ans.status,
       'objective',ans.fun,'dual_bound',ans.mip_dual_bound,'gap',ans.mip_gap)
    assert ans.status==0 and round(ans.fun)==94 and round(ans.mip_dual_bound)==94
