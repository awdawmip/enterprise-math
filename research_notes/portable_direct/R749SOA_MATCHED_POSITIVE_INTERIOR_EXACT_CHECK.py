#!/usr/bin/env python3
"""R749SOA exact rational arithmetic and finite corner audit.
The universal conclusion follows from the written analytic transport theorem,
not from finite sampling. Standard library only.
"""
from fractions import Fraction as F
from itertools import product
import json

OLD = F(1,4455)
OUTER = F(1,827)
INNER = F(1,1652)
BASE_GAP = F(1,110)


def house_bound(delta):
    assert F(0) <= delta < F(1,2)
    return delta/(F(1,2)-delta) + delta/2


def gap_bound(delta):
    return BASE_GAP - 3*house_bound(delta)


def center(t,s):
    h = min(t,s)
    out=[]
    for A,B in product((-1,1),repeat=2):
        out.append((1+t*A+s*B+h*A*B)/16)
    return tuple(out)


def audit():
    for N in (4455,1652,827,826):
        d=F(1,N)
        for t,s in ((F(1,2)-d,F(1,2)),(F(1,2)+d,F(1,2)),
                    (F(1,2),F(1,2)-d),(F(1,2),F(1,2)+d)):
            c = center(t,s)
            assert min(c)==(1-max(t,s))/16
            assert all(v>0 for v in c)
            assert sum(c)==F(1,4)
        assert gap_bound(d)>0 if N>=827 else gap_bound(d)<0
    assert gap_bound(OUTER)==F(1,227425)
    assert gap_bound(INNER)==F(4131,908600)
    assert gap_bound(INNER)>=F(1,220)
    assert gap_bound(F(1,826))<0
    assert OLD < INNER < OUTER
    assert (OUTER/OLD)**2 > 29
    return {
      'research_unit':'R749SOA',
      'scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'dependent_source':'R749SNG@74abff6fff03fb6defec95c6c505c69ea5b0832c',
      'kind':'EXACT_ANALYTIC_PROOF_WITH_RATIONAL_ARITHMETIC_AUDIT',
      'author_check':'PASS', 'independent_review':'NOT_REVIEWED',
      'old_radius':str(OLD), 'new_outer_radius':str(OUTER),
      'uniform_gap_outer':str(gap_bound(OUTER)),
      'inner_radius':str(INNER), 'uniform_gap_inner':str(gap_bound(INNER)),
      'minimum_gap_inner_at_least':'1/220',
      'ratio_outer_to_old_area':str((OUTER/OLD)**2),
      'area_outer':str(2*OUTER**2),
      'new_outer_radius_next_integer_826_fails_this_bound':str(gap_bound(F(1,826))),
      'coverage':'Analytic for all real points in closed L1 diamonds; four rational corner checks supplement proof',
      'unresolved':'Actual positive-gap phase boundary and exact 2D piecewise minimax radii'
    }


if __name__=='__main__':
    print(json.dumps(audit(),ensure_ascii=False,sort_keys=True,indent=2))
