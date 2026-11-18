#!/usr/bin/env python3
"""Fixed seven-key native-prefix MILP for the EC49FGL 98-edge case.
Run next to the published sibling EC49FGF_EXACT_16_CLASS_DUAL_20261110.
Solver result only proves a fixed-inventory conditional optimum.
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'EC49FGF_EXACT_16_CLASS_DUAL_20261110'))
from VERIFY_EC49FGF import model

K = {(2,1,1), (3,0,1), (3,1,1), (4,2,1), (5,4,1), (6,3,1), (6,4,1)}
c, G, h, stats = model(K)
ans = milp(c.astype(float), integrality=np.ones(len(c), dtype=np.int8),
           bounds=Bounds(0,1),
           constraints=LinearConstraint(G, np.full(len(h), -np.inf), h),
           options={'mip_rel_gap':0.0, 'time_limit':120})
report = {'key_inventory':sorted(K), 'stats':stats, 'solver':'SciPy/HiGHS',
          'status':int(ans.status), 'objective':float(ans.fun) if ans.fun is not None else None,
          'dual_bound':float(ans.mip_dual_bound) if getattr(ans,'mip_dual_bound',None) is not None else None,
          'gap':float(ans.mip_gap) if getattr(ans,'mip_gap',None) is not None else None}
print(json.dumps(report, indent=2))
assert ans.status == 0 and abs(ans.fun-98)<1e-6 and abs(ans.mip_dual_bound-98)<1e-6 and ans.mip_gap == 0, ans.message
print('PASS fixed-key solver-backed optimum 98, no portable exact UNSAT certificate')
