#!/usr/bin/env python3
"""Exact finite five-Port labelled-path BRC fiber classification, d<=250."""
from itertools import product
from fractions import Fraction as F
from math import isqrt
import json
from pathlib import Path
A=[[(4,0),(4,0),(0,0)],[(0,0),(-4,0),(4,0)],[(-5,3),(0,0),(-3,1)],[(-2,-2),(4,4),(2,2)],[(-2,0),(0,0),(5,2)]]
Q=(128,80,74,200,85)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def norm(a):return a[0]**2+a[1]**2
def circle(n):
 for x in range(-isqrt(n),isqrt(n)+1):
  y=isqrt(n-x*x)
  if y*y==n-x*x:
   yield(x,y)
   if y:yield(x,-y)
def brc(j,B,ref=None):
 p=[mul(A[j][k],B[k]) for k in range(3)]
 if ref:p.append(ref)
 v=(0,0)
 for a in p:
  for b in p:v=add(v,mul(a,(b[0],-b[1])))
 assert v[1]==0 and v[0]>=0
 return v[0]
def run():
 counts=[0,0,0,0]
 seen=set();phases=set();per_d=[]
 for d in range(1,251):
  z=list(circle(8*d*d));w=list(circle(5*d*d));v=list(circle(74*d*d));accepted=0
  for Z,W,V in product(z,w,v):
   counts[0]+=1
   C=add(mul((-5,3),Z),mul((-3,1),W))
   K=mul(sub(V,C),(1,1))
   if K[0]%4 or K[1]%4:continue
   counts[1]+=1
   B2=(K[0]//4,K[1]//4);B1=sub(Z,B2);B3=add(W,B2);B=(B1,B2,B3)
   if brc(3,B)!=200*d*d:continue
   counts[2]+=1
   if brc(4,B)!=85*d*d:continue
   counts[3]+=1;accepted+=1
   assert all(brc(j,B)==Q[j]*d*d for j in range(5))
   assert B1==mul((-2,0),B3) and norm(B3)==d*d
   assert B2 in (mul((0,2),B3),mul((0,-2),B3))
   seen.add(tuple(F(x,d) for t in B for x in t))
   phases.add((F(B3[0],d),F(B3[1],d)))
  per_d.append(accepted)
 independent={(F(x,d),F(y,d)) for d in range(1,251) for x,y in circle(d*d)}
 assert phases==independent and len(seen)==2*len(phases)
 # Source-labelled reference paths at common scale 1/4; each report is midpoint.
 references={}
 for name,ref in [('one',(4*8,0)),('imag',(0,4*8))]:
  bminus=((-2,0),(0,-2),(1,0));bplus=((-2,0),(0,2),(1,0))
  # B=b, d=4: reference numerator amplitude is 8*d.
  a=[F(brc(j,bminus,ref),64*4*4) for j in range(5)]
  b=[F(brc(j,bplus,ref),64*4*4) for j in range(5)]
  assert all(abs(x-y)<=2 for x,y in zip(a,b))
  references[name]=[str((x+y)/2) for x,y in zip(a,b)]
 assert counts==[2098944,1401344,5024,4640]
 assert len(seen)==632 and len(phases)==316
 result={'schema':'PREFIX325_COMPACT_EXACT_BRC_EVIDENCE_V1','denominator_max_inclusive':250,
 'Q0_times_64':Q,'candidate_triples_integral_port4_all5':counts,
 'distinct_states':len(seen),'distinct_unit_phases':len(phases),
 'per_denominator_all5_counts':per_d,
 'unit_phases':[[str(a),str(b)] for a,b in sorted(phases)],
 'reference_midpoints_at_scale_one_quarter':references,'checks':'PASS',
 'scope':'frozen-Q0 Gaussian rational states with common integer denominator <=250; not all complex states'}
 Path(__file__).with_name('RESULTS_PREFIX325_COMPACT.json').write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
 print('PASS PREFIX325',counts,len(seen),len(phases))
if __name__=='__main__':run()
