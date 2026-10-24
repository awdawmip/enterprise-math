#!/usr/bin/env python3
"""C289 exact author verification for 125 uniformly stable auxiliary roots.
Place beside pinned C275_STANDALONE_EXACT_REPLAY.py,
C284_187_EXACT_DYADIC_BRACKETS.json, C285_EXACT_UNIFORM_DERIVATIVE.py,
C288_ISOLATING_BOXES_EXACT.py. All deciding inequalities use Fraction.
"""
from fractions import Fraction as R
from itertools import combinations
import json
import hashlib
import C275_STANDALONE_EXACT_REPLAY as s
import C285_EXACT_UNIFORM_DERIVATIVE as c285
import C288_ISOLATING_BOXES_EXACT as c288

EPS=R(1,2**28)

def verify():
    paths,mult=c288.build_paths()  # verifies frozen C284 record digest
    weights,_=s.floor_fixed_masses()
    Q=s.Q
    min_margin=None
    min_info=None
    tight_low=None
    tight_high=None
    max_inf=R(0)
    max_l1=R(0)
    deriv_lower_min=None
    for i,p in enumerate(paths):
        k=p['k']; a,b=R(k,4096),R(k+1,4096)
        w,h,d=p['w'],p['h'],p['d']
        v0=tuple(x+a*z for x,z in zip(w,d))
        v1=tuple(x+b*z for x,z in zip(w,d))
        assert s.valid(v0) and s.valid(v1)
        lo=s.original_F(v0,weights)
        hi=s.original_F(v1,weights)
        left=(Q-lo)/Q
        right=(hi-Q)/Q
        assert left>EPS and right>EPS,(i,'margin')
        for side,x in (('low',left),('high',right)):
            if min_margin is None or x<min_margin:
                min_margin=x
                min_info=(i,side,p['wid'],k)
        if tight_low is None or left<tight_low[0]:tight_low=(left,i)
        if tight_high is None or right<tight_high[0]:tight_high=(right,i)
        lower=c285.derivative_lower(w,h,a,b,weights)
        assert 56*lower>Q,(i,'whole interval derivative')
        if deriv_lower_min is None or lower<deriv_lower_min:
            deriv_lower_min=lower
        max_inf=max(max_inf,max(abs(x) for x in d))
        max_l1=max(max_l1,sum(abs(x) for x in d))
    assert len(paths)==125
    assert min_info[:2]==(67,'low')
    assert tight_low[1]==67 and tight_high[1]==69
    assert max_inf==R(15359,1020000)
    assert 56*max_inf==R(107513,127500)<1
    assert max_l1==R(25437513,1103011000)<R(1,40)
    assert deriv_lower_min>R(Q,56)
    gap_min=None
    pairs=0
    for i,j in combinations(range(125),2):
        x,y=paths[i]['box'],paths[j]['box']
        gap=max(max(R(0),lo-hi2,lo2-hi)
                for (lo,hi),(lo2,hi2) in zip(x,y))
        assert gap>R(1,2**23)
        gap_min=gap if gap_min is None or gap<gap_min else gap_min
        pairs+=1
    assert pairs==7750
    assert gap_min==R(518383,3360752136192)
    result={
       'schema':'EM_C289_LEVEL_STABILITY_AUTHOR_EXACT_V1',
       'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
       'n_paths':125,
       'exact_endpoint_comparisons':250,
       'whole_interval_derivative_proofs':125,
       'separated_box_pairs':7750,
       'uniform_relative_level_halfwidth':'1/268435456',
       'minimum_endpoint_margin_strict':'min(abs(F(end)-Q)/Q)>2^-28',
       'bottleneck_path_index':min_info[0],
       'bottleneck_side':min_info[1],
       'bottleneck_witness_id':min_info[2],
       'bottleneck_k':min_info[3],
       'bottleneck_fraction_sha256':hashlib.sha256(
           f'{min_margin.numerator}/{min_margin.denominator}'.encode()).hexdigest(),
       'minimum_margin_float_display_only':format(float(min_margin),'.15g'),
       'max_direction_linf':str(max_inf),
       'max_direction_l1':str(max_l1),
       'normalized_coordinate_sensitivity_strict_upper':'107513/127500',
       'min_interbox_gap':str(gap_min),
       'formal_source_admission':False,
       'native_x6_or_signed_brc_promotion':False
    }
    with open('C289_AUTHOR_EXACT_AUDIT_20261025.json','w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print('C289_UNIFORM_LEVEL_STABILITY_EXACT_PASS 125 paths 250 endpoint margins 7750 pairs')
    print('minimum-margin display:',float(min_margin),
          'witness:',min_info,'max direction linf:',max_inf)
    return result

if __name__=='__main__':
    verify()
