#!/usr/bin/env python3
"""PREFIX-308: provenance-labelled Gaussian-integer BRC frame verification.
Every Q is an ordered source-path-pair sum; all amplitudes use denominator 8.
This is an auxiliary BRC register, NOT native X6/physical detector simulation.
"""
import json
from itertools import product
from pathlib import Path

Z=(0,0); U=(1,0); I=(0,1)
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def times(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def star(a):return (a[0],-a[1])
def sc(a,n):return (a[0]*n,a[1]*n)
def summable(seq):
 s=Z
 for z in seq:s=plus(s,z)
 return s
def sq(a):return a[0]*a[0]+a[1]*a[1]
def mass(paths,counts):
 # Source pairs remain ordered and source-labelled through the observer.
 v=summable(times(star(x),y) for _,x in paths for _,y in paths)
 counts['ordered_pairs']+=len(paths)**2
 counts['mass_reads']+=1
 assert v[1]==0 and v[0]>=0
 return v[0]
def rows_for(M,q):
 q2=times(q,q)
 return [(sc(U,4),sc(q,4),Z),(Z,(-4,0),sc(q,4))]+[
 tuple(times(tuple(M[j][k]),(U,q,q2)[k]) for k in range(3)) for j in range(3)]
def run():
 source=Path(__file__).resolve().parents[1]/'research6_prefix299_rank2_left_orbits_20261027'/'RESULTS_PREFIX299.json'
 obj=json.loads(source.read_text(encoding='utf-8'))
 alphabet=(Z,U,(-1,0),I,(0,-1),(1,1))
 counts={'configs':0,'input_cases':0,'mass_reads':0,'ordered_pairs':0,'gram_entries':0,'reconstructions':0}
 row_norms=[]
 for family,case in obj['cases'].items():
  assert family in ('S4','S7')
  for orbit,M in enumerate(case['all_orbits'],1):
   norms=sorted(sum(sq(tuple(z)) for z in row) for row in M)
   assert norms in ([33,38,54],[33,44,48],[33,46,46])
   assert sum(norms)==125
   row_norms.append(norms)
   for q in (U,I,(-1,0),(0,-1)):
    rows=rows_for(M,q)
    for k in range(3):
     for l in range(3):
      v=summable(times(star(row[k]),row[l]) for row in rows)
      assert v==(((64-case['S'][k]),0) if k==l else Z),(family,orbit,q,k,l,v)
      counts['gram_entries']+=1
    counts['configs']+=1
    for a in product(alphabet,repeat=3):
     readout=[]
     for row in rows:
      paths=[(f'source_{k}',times(row[k],a[k])) for k in range(3)]
      Q0=mass(paths,counts)
      Q1=mass(paths+[('reference_1',(8,0))],counts)
      Qi=mass(paths+[('reference_i',(0,8))],counts)
      assert (Q1-Q0-64)%16==0 and (Qi-Q0-64)%16==0
      y=((Q1-Q0-64)//16,(Qi-Q0-64)//16)
      assert Q0==sq(y)
      readout.append(y)
     for k in range(3):
      rec=summable(times(star(row[k]),readout[j]) for j,row in enumerate(rows))
      assert rec==sc(a[k],64-case['S'][k]),(family,orbit,q,a,k)
     counts['input_cases']+=1
     counts['reconstructions']+=1
 assert counts['configs']==48 and counts['input_cases']==10368
 assert counts['gram_entries']==432 and counts['mass_reads']==155520
 assert len(row_norms)==12 and all(v[0]==33 for v in row_norms)
 # Rigorous bounds use Gram and row-norm certificates, not error samples.
 return {'schema':'ENTERPRISE_MATH_PREFIX308_FRAME_CERTIFICATE_V1',
  'source_prefix299_blob':'b6acffe158f014469235f5428d2889ff43b62810',
  'scope':'all Q(i)^3; 12 exact S4/S7 matrices; 4 C4 source phases',
  'eight_extra_references':{'selected_ports':'E,C and two R; omit an R with norm^2=33/64',
                            'gram_lower_numerator_over_64':29,
                            'error_bound_sq_numerator':512,'error_bound_sq_denominator':29},
  'ten_extra_references':{'selected_ports':'E,C,R1,R2,R3',
                            'gram_lower_numerator_over_64':62,
                            'error_bound_sq_numerator':320,'error_bound_sq_denominator':31},
  'counts':counts,'row_norm_multisets':row_norms,
  'proof_note':'Infinite-input and all-continuous-noise bounds follow from Hermitian Gram Loewner inequalities; finite BRC run checks kernel semantics only.',
  'native_admission':'AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED'}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
