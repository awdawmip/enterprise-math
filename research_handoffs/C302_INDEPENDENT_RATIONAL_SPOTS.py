#!/usr/bin/env python3
"""C302 second implementation: nine exact rational identity spot checks.
Not a 125-path independent mathematical review; author-level cross-check.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter,defaultdict
from math import gcd,lcm
import json
import C298_SHARED_DENOMINATOR_EXACT as base
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as src

SAMPLE=(0,8,24,28,40,63,64,96,124)

def main():
 rows=json.loads(Path('C302_125_SCALAR_NORMALIZATION_CERTIFICATE.json').read_text())['rows']
 br=json.loads(Path('C293_125_REFINED_BRACKETS.json').read_text())['records']
 paths,_=c288.build_paths();W,_=src.floor_fixed_masses()
 for i in SAMPLE:
  path=paths[i]; k=int(br[i][1]); lo=F(k,2**24);hi=F(k+1,2**24);t=(lo+hi)/2
  terms=base.make_terms(path,lo,hi,W)
  counts=Counter();den_values=[]; occ=defaultdict(set)
  for j,(c,factors) in enumerate(terms):
   v=c.denominator; local=Counter()
   for n,d in factors:
    d_content,q=base.primitive_factor(d)
    v*=d_content;local[q]+=1;occ[q].add(j)
   den_values.append(v)
   for q,e in local.items():counts[q]=max(counts[q],e)
  s=lcm(*den_values); L=int(rows[i]['certified_common_scalar_divisor_decimal'])
  assert s%L==0
  cancel=[q for q in counts if len(q)==2 and occ[q] in ({75,77},{76,78})]
  assert len(cancel)==2
  D=F(s)
  for q,e in counts.items():D*=base.poly_eval(q,t)**e
  At=F(0)
  for (c,factors),d in zip(terms,den_values):
   m=s//d*c.numerator
   local=Counter(base.primitive_factor(dn)[1] for n,dn in factors)
   term=F(m)
   for n,dn in factors:
    term*=base.poly_eval(n,t)
   # Structural integrality of all coefficients after dividing by L.
   monomial_content=abs(m)
   for n,dn in factors:monomial_content*=gcd(*n)
   assert monomial_content%L==0
   for q,e in counts.items():
    if e>local[q]:term*=base.poly_eval(q,t)**(e-local[q])
   At+=term
  v=tuple(w+t*d for w,d in zip(path['w'],path['d']))
  assert src.valid(v)
  f=src.original_F(v,W)/src.Q
  assert At==D*f
  Q=base.poly_eval(cancel[0],t)*base.poly_eval(cancel[1],t)
  Ared=At/Q;Dred=D/Q
  assert Dred>0 and Ared/L==(Dred/L)*f
  # Integer-polynomial membership at dyadic t:
  r=Ared/L * 2**(25*rows[i]['degree'])
  assert r.denominator==1,(i,r.denominator)
  print('C302_INDEPENDENT_SPOT',i,'Lbits',L.bit_length(),'dyadic_degree',rows[i]['degree'],'PASS',flush=True)
 print('C302_INDEPENDENT_RATIONAL_SPOTS_9_PASS')
if __name__=='__main__':main()
