#!/usr/bin/env python3
"""R749SOC exact polytope/endpoint directional transport certificate.
Requires R749SOB_SHARP_REFERENCE_TRANSPORT_EXACT_CHECK.py in the same directory.
Python standard library, Fraction only.
"""
from fractions import Fraction as Q
from itertools import combinations
import json
from R749SOB_SHARP_REFERENCE_TRANSPORT_EXACT_CHECK import ROWS, RHS, solve_exact, chi, tv_to_reference

def vertices():
    out=set()
    for ids in combinations(range(16),5):
        y=solve_exact(ids)
        if y is not None and all(sum((a*b for a,b in zip(row,y)),Q(0)) >= bound for row,bound in zip(ROWS,RHS)):
            out.add(y)
    assert len(out)==17 and max(map(tv_to_reference,out))==Q(15,32)
    return out

def directional_slope(y,c,mask,sign):
    # Equivalent to TV(c*(r0-mu)+sign*chi_mask/16) for |direction|_1=1.
    return sum((abs(c*sum(((int(j==0)-y[j])*ROWS[x][j] for j in range(5)),Q(0))+2*sign*chi(mask,x)) for x in range(16)),Q(0))/64

def main():
    d=Q(1,339)
    cmax=1/(Q(1,2)-d)
    vs=vertices()
    endpoints=[]
    for c in (Q(2),cmax):
        outcomes={}
        for mask in (3,12):
            for sign in (-1,1):
                extreme=max(directional_slope(y,c,mask,sign) for y in vs)
                assert extreme <= c*Q(15,32)+Q(1,16)
                outcomes[f'mask_{mask}_sign_{sign}']=str(extreme)
        endpoints.append({'c':str(c),'bound':str(c*Q(15,32)+Q(1,16)),'extrema':outcomes})
    H0=d*cmax+d/2
    H2=d*(cmax*Q(15,32)+Q(1,16))+d*cmax*(d+H0)
    gap=Q(1,110)-3*H2
    assert gap == Q(43323,5646650680) >0
    assert 2<=cmax and d*cmax<=1
    return {
      'unit':'R749SOC', 'result':'PASS',
      'frozen_source':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'scope':'auxiliary 16-state Walsh model, every real (t,s) in closed L1 diamond; author proof / NOT_REVIEWED',
      'base_polytope_vertices':len(vs),'base_max_TV':'15/32',
      'directional_checks':{'endpoint_count':2,'directions_per_endpoint':4,'vertices_per_direction':len(vs),'all_exact':True,'endpoint_table':endpoints},
      'diamond':{'L1_radius':str(d),'area':str(2*d*d),
          'area_ratio_vs_R749SOA':str(Q(827,339)**2),
          'area_ratio_vs_R749SOB':str(Q(481,339)**2),
          'old_H_at_boundary':str(H0),'directional_H_at_boundary':str(H2),
          'positive_gap_uniform_bound':str(gap)},
      'derivation':'Convex in base vertex, direction L1 ball, and coefficient c in [2,1/(1/2-d)]; reverse transport coupled to old Hausdorff witness.'
    }

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
