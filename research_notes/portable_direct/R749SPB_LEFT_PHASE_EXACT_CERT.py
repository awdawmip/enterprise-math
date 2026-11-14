#!/usr/bin/env python3
"""R749SPB: exact left-hand Walsh zero-gap phase certificate.
Requires R749SPA_WALSH_REPAIRED_SEGMENT_EXACT_CERT.py from the same frozen
research artifact set; standard-library Python and exact rational arithmetic.
"""
from fractions import Fraction as F
import json
import R749SPA_WALSH_REPAIRED_SEGMENT_EXACT_CERT as prior

def main():
    s=F(3,5)
    endpoints=[F(0),F(2,15)]
    signs=[]
    pair=[]
    for t in endpoints:
        a=prior.law(t,s,0,t,t,1-t,s)
        b=prior.law(t,s,0,-t,-t,t-1,-s)
        assert min(a)>=0 and min(b)>=0 and sum(a)==sum(b)==1
        assert prior.tv(a,b)==1-t
        signs.append(tuple((x>y)-(x<y) for x,y in zip(a,b)))
        pair.append({'t':str(t),'source_pair_TV':str(prior.tv(a,b))})
    assert all(x*y>=0 for a,b in zip(signs[0],signs[1]) for x,y in [(a,b)])
    prior.rad=lambda t:(1-t)/2
    upper=prior.certify(F(0),F(2,15),F(0),F(0))
    assert upper['max_risk_excess']=='0'
    return {'status':'PASS','research_id':'R749SPB',
            'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'model':'original 16-atom compatible Walsh fiber; s=3/5, real 0<=t<=2/15',
            'theorem_left':'rho=rho_cal=(1-t)/2',
            'center_left':'p(t,3/5,0,0,0,0,0)',
            'source_pair_lower':{'endpoints':pair,'sign_consistency':True,
                                 'all_real_t_source_TV':'1-t'},
            'upper':upper,'seam_t':'2/15',
            'seam_radius':'13/30',
            'full_combined_result':'zero gap for every real t in [0,2/5] at s=3/5; rho=(1-t)/2 on [0,2/15], and (18/5-t)/8 on [2/15,2/5]',
            'radius_slope_left':'-1/2','radius_slope_right':'-1/8',
            'basis':'R749SPA two right-hand piece certificates at the same frozen model',
            'review_status':'AUTHOR_EXACT_NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
