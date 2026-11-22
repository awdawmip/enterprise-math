#!/usr/bin/env python3
"""T6 p17 vertical order6 split(1,5): exact global mixed q0 affine sphere check.

Reads the existing published q5 saturated-basis checker in the same directory,
retains every named vertical atom and q0 cofactor, and checks the full affine
sphere. This compact reproducer was derived from a standalone local exact
computation; that standalone version was executed and the results checked.
"""
import importlib.util
import json
from pathlib import Path
from fractions import Fraction

BASE=Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("p17_q5_exact_pinned",BASE)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
assert len(old.STATES[1])==16 and len(old.STATES[5])==30040
left=old.STATES[1];right=old.STATES[5]
max_R2=(2331-min(x[1] for x in left))**2+(2331-min(x[1] for x in right))**2
assert max_R2==4861576 and max_R2<old.Dmin

counts={"raw_pairs":0,"shared_vertical":0,"primitive_pairs":0,"nodes":0,"leaves":0,"survivors":0}
for pos in left:
    for neg in right:
        counts["raw_pairs"]+=1
        if set(pos[0])&set(neg[0]):
            counts["shared_vertical"]+=1
            continue
        counts["primitive_pairs"]+=1
        nodes,leaves,sol=old.ball_search(pos,neg)
        counts["nodes"]+=nodes
        counts["leaves"]+=leaves
        if sol is not None:
            counts["survivors"]+=1
            raise RuntimeError(f"Nonempty q0 candidate: {pos[0]} / {neg[0]} / {sol}")
assert counts=={"raw_pairs":480640,"shared_vertical":90937,"primitive_pairs":389703,"nodes":1293850,"leaves":1,"survivors":0}

# Independent direct modular check of the one sphere leaf (observed during
# the original exact enumeration), including full two-sided budget failure.
pos=((1,4),)
neg=((1,8),(2,3),(2,9))
u=(-20,5,-7,0,2,-12,6,1,2,3,-3,-1,-1,2,-2,3)
for j in range(1,7):
    mod=17**j
    residual=sum(x*pow(r,-j,mod) for r,x in enumerate(u,1))
    residual+=sum(pow(17*q+r,-j,mod) for q,r in pos)
    residual-=sum(pow(17*q+r,-j,mod) for q,r in neg)
    assert residual%mod==0
q0plus=sum((17*r-1)*max(x,0) for r,x in enumerate(u,1))
q0minus=sum((17*r-1)*max(-x,0) for r,x in enumerate(u,1))
posmass=sum(289*q+17*r-1 for q,r in pos)
negmass=sum(289*q+17*r-1 for q,r in neg)
sqnorm=sum(((17*r-1)*x)**2 for r,x in enumerate(u,1))
radius=(2331-posmass)**2+(2331-negmass)**2
assert (posmass,negmass,q0plus,q0minus)==(356,1782,3274,3371)
assert (sqnorm,radius)==(4162929,4202026)
assert posmass+q0plus==3630>2331
assert negmass+q0minus==5153>2331
result={"schema":"T6_P17_Q6_SPLIT1_5_EXACT_AFFINE_AUTHOR_V1",
        "split":[1,5], "counts":counts,
        "max_sphere_R_squared":max_R2,
        "one_sphere_leaf":{"positive_vertical":pos,"negative_vertical":neg,
                           "q0_signed":u,"weighted_sqnorm":sqnorm,
                           "leaf_radius_sq":radius,
                           "positive_total":3630,"negative_total":5153},
        "state":"AUTHOR_EXACT_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED"}
path=Path("T6_P17_Q6_SPLIT1_5_AUTHOR_EXACT_CERT_20261123.json")
path.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2,default=list))
