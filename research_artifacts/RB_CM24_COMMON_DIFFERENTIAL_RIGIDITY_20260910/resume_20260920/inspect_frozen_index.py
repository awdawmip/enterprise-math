"""Consume the stored complete index; do not execute its generating programs."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
base=ROOT/'research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908'
rr=json.loads((base/'squareclass_rr_certificate.json').read_bytes())
ex=json.loads((base/'empty_fiber_obstruction_certificate.json').read_bytes())
actual=json.loads((HERE/'INDEX_APPLICATION.json').read_bytes())
rows4=rr['patterns']['4+2+0+0']['rows'];rows222=rr['patterns']['2+2+2+0']['rows']
assert len(rows4)==45 and len(rows222)==90
for rows,pattern in [(rows4,[4,2]),(rows222,[2,2,2])]:
    for row in rows:
        labels=row['fixed_parameter_representative']
        assert len(labels)==6
        assert sorted([labels.count(j) for j in range(4) if labels.count(j)],reverse=True)==pattern
        assert row['compatible_geometric_twist_table_size']==16
assert len(ex['excluded_components'])==45
assert all(len(row['excluded_geometric_twists'])==4 for row in ex['excluded_components'])
matches=[(i,r) for i,r in enumerate(rows4) if r['fixed_parameter_representative']==[0,3,3,0,0,0]]
assert len(matches)==1
i,r=matches[0]
assert r['infinity_empty_representative']==[1,2,2,1,1,1]
assert actual['accepted_map_match']=={'row_index_zero_based':i,'row':r}
assert actual['counts_consumed']==ex['counts']
print(json.dumps({'status':'PASS_FROZEN_DATA_INTAKE','rows_read':135,'exclusion_masks_read':45,
                  'accepted_row_index_zero_based':i,'regenerated_assignments':False,
                  'RR_ODE_parameter_systems_solved_by_this_program':0}))
