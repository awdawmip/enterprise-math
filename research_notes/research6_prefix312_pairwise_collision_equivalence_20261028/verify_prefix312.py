#!/usr/bin/env python3
"""Exact tagged-source BRC proof check for all pair midpoints m=i*t*v.
Reads PREFIX311_RESULTS_{ten,eight}.json from the adjacent PREFIX311 folder.
T in {0,1,2,3}, all 4 C4 phases, 12 port matrices and every 10/8 menu.
Each witness has a=(1/2+i*t)v and b=(-1/2+i*t)v, difference v.
"""
import json
from fractions import Fraction as F
from pathlib import Path
import sys
SOURCE_DIR=Path(__file__).resolve().parents[1] / 'research6_prefix311_full_source_antipodal_polytope_20261028'
sys.path.insert(0,str(SOURCE_DIR))
from p311_full import E,S4,S7
from verify_prefix311_brc import Q,one,ii,mul,conj,op,row_paths,parse_v

def main():
    total=0; masses=0; ordered=0; q0_equal=0; ref_overlap=0; reference_diff_invariant=0
    for mode in ('ten','eight'):
      obj=json.loads((SOURCE_DIR/f'PREFIX311_RESULTS_{mode}.json').read_text())
      for result in obj['results']:
        M=(S4 if result['family']=='S4' else S7)[result['orbit']-1]
        omit=None if result['omit'] is None else int(result['omit'][-1])-1
        ports=E+M
        measured=[0,1]+[j+2 for j in range(3) if j!=omit]
        w=parse_v(result['witness_v'])
        for q0 in Q:
          q=tuple(map(F,q0));qpow=[one,q,mul(q,q)]
          v=[mul(w[j],conj(qpow[j])) for j in range(3)]
          reference_at_zero={}
          for t in range(4):
            positive=(F(1),F(2*t));negative=(F(-1),F(2*t))
            for j,row in enumerate(ports):
              base=row_paths(row,v,qpow)
              p=[mul(z,positive) for z in base]
              n=[mul(z,negative) for z in base]
              p0,c=op(p);n0,d=op(n);masses+=2;ordered+=c+d
              assert p0==n0
              q0_equal+=1
              if j in measured:
                for ref in (one,ii):
                  qp,c=op(p,ref);qn,d=op(n,ref)
                  masses+=2;ordered+=c+d
                  diff=qp-qn
                  assert abs(diff)<=2
                  ref_overlap+=1
                  key=(j,ref)
                  if t==0:reference_at_zero[key]=diff
                  else:
                    assert diff==reference_at_zero[key]
                    reference_diff_invariant+=1
            total+=1
    report=dict(model='exact tagged ordered BRC source pairs; midpoint m=i*t*v',t_values=[0,1,2,3],configurations_and_midpoints=total,q0_equalities=q0_equal,reference_overlap_checks=ref_overlap,reference_difference_invariance_checks=reference_diff_invariant,direct_brc_mass_evaluations=masses,tagged_ordered_source_pairs=ordered,result='PASS')
    (Path(__file__).resolve().parent/'PREFIX312_BRC_CHECK.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
