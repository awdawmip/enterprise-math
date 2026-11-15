#!/usr/bin/env python3
"""Check the first six members of the exact infinite switch-only Q family."""
from VERIFY_R5_N5_SWITCH_ONLY import point_coordinates, optimal_family, all_edges
import json

rows=[]
for m in range(6):
    gaps = (3, 2, 2, 3) + (5,)*m
    families=[]
    for mask in range(4):
        x=point_coordinates(gaps, 0, 3, mask)
        j,f=optimal_family(x, 3+m)
        assert j == 4
        families.append(f)
    f0,fa,fb,fab=families
    prefix=tuple(range(5,5+m))
    assert list(map(len, families)) == [1,4,4,8]
    assert fa & fb == f0
    assert fab-fa-fb == {(1,2,3)+prefix}
    assert all_edges(fab) == all_edges(fa) | all_edges(fb)
    rows.append({'m':m, 'n':5+m, 'K':3+m, 'J':4,
                 'optimizer_counts':[1,4,4,8],
                 'Q_witness':[1,2,3]+list(prefix),
                 'joint_neutral_edges':0})
print(json.dumps({'status':'PASS_R5_SWITCH_ONLY_INFINITE_FAMILY_SIX_FINITE_CHECKS',
                  'm_checked':list(range(6)), 'rows':rows,
                  'unbounded_proof':'See UNBOUNDED_SWITCH_ONLY_Q_FAMILY.md; finite tests are not that proof',
                  'review':'NOT_REVIEWED'}, indent=2, sort_keys=True))
