#!/usr/bin/env python3
"""R749SPQ: exact full optimal-center dimension + strict octahedral containment.
Requires the frozen companion R749SPP_WALSH_3D_OPTIMAL_CENTER_OCTAHEDRON_CERT.py
in the same directory. Only standard-library exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import R749SPP_WALSH_3D_OPTIMAL_CENTER_OCTAHEDRON_CERT as c

def run():
    vv=set()
    for inds in combinations(range(16),5):
        y=c.bareiss(inds)
        if y is not None and all(c.dot(a,y)>=b for a,b in zip(c.A,c.B)):
            vv.add(y)
    assert len(vv)==50
    w_plus=(F(1),F(0),F(0),F(9),F(4))
    z_plus=(F(1),F(0),F(0),F(4),F(9))
    critical=(w_plus, tuple(-q if i>=3 else q for i,q in enumerate(w_plus)),
              z_plus, tuple(-q if i>=3 else q for i,q in enumerate(z_plus)))
    for y in critical:
        assert all(c.dot(a,y)>=b for a,b in zip(c.A,c.B))
        assert c.risk_numerator(y,(F(0),)*5)==144
    # All calibrated minimax centers must have w=z=0: source laws with 4th/5th
    # Walsh moments +/-9/10 force center moments w=z=0 by TV >= |moment difference|/2.
    q=(F(-1),F(1),F(-2),F(0),F(0))
    assert sum(abs(i) for i in q[:3])==4>2  # Q scaled by 10: outside the R749SPP octahedron.
    assert all(F(10)+bit[0]+F(5)*bit[1]+c.dot(row,q)>=0
               for bit,row in zip(c.C,c.A))
    excess=[c.risk_numerator(y,q)-144 for y in vv]
    assert max(excess)==0
    print(json.dumps({
        'status':'PASS', 'research_unit':'R749SPQ',
        'frozen_science_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'fiber':'t=1/10,s=1/2', 'rho_and_rho_cal':'9/20',
        'source_vertices':len(vv),
        'all_optimal_calibrated_centers_have':'w=z=0',
        'exact_affine_dimension_of_full_calibrated_optimal_center_set':3,
        'four_sign_witness_sources_scaled_10':[list(map(str,y)) for y in critical],
        'outside_octahedron_scaled_10':list(map(str,q)),
        'outside_center_is_feasible':True,
        'outside_center_max_excess_times_320':str(max(excess)),
        'outside_center_tight_source_vertices':sum(t==0 for t in excess),
        'outside_center_l1_huv_scaled_10':'4 > 2 (R749SPP octahedron radius)',
        'dependency':'R749SPP_WALSH_3D_OPTIMAL_CENTER_OCTAHEDRON_CERT.py',
        'review_status':'AUTHOR_EXACT_NOT_REVIEWED',
    },sort_keys=True,indent=2))

if __name__=='__main__':run()
