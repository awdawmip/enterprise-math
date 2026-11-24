#!/usr/bin/env python3
"""Check 12 finite members of a proven gap-at-least-3 infinite Q family."""
from VERIFY_R5_N5_SWITCH_ONLY import point_coordinates, optimal_family, all_edges
import json

rows=[]
for separator in (3, 5):
    for m in range(6):
        gaps = (3, 2, 2, 3) + (separator,)*m
        families=[]
        for mask in range(4):
            x=point_coordinates(gaps, 0, 3, mask)
            j,f=optimal_family(x, 3+m)
            assert j == 4
            families.append(f)
        f0,fa,fb,fab=families
        suffix=tuple(range(5,5+m))
        assert list(map(len, families)) == [1,4,4,8]
        assert fa & fb == f0
        assert fab-fa-fb == {(1,2,3)+suffix}
        assert all_edges(fab) == all_edges(fa) | all_edges(fb)
        rows.append({'separator_gap':separator, 'm':m, 'n':5+m, 'K':3+m,
                     'J':4, 'optimizer_counts':[1,4,4,8],
                     'Q_witness':[1,2,3]+list(suffix), 'joint_neutral_edges':0})
print(json.dumps({'status':'PASS_R5_SWITCH_ONLY_UNBOUNDED_FAMILY_TWELVE_FINITE_CHECKS',
                  'separators_checked':[3,5], 'm_checked':list(range(6)),
                  'rows':rows,
                  'unbounded_proof':'See UNBOUNDED_SWITCH_ONLY_Q_FAMILY.md; finite tests are not that proof',
                  'review':'NOT_REVIEWED'}, indent=2, sort_keys=True))
