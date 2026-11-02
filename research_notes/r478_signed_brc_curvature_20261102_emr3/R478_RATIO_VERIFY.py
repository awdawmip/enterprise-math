#!/usr/bin/env python3
"""Exact finite exhaustive regression for the R478 ratio-local PF3 characterization.
Independent integer determinant and Fraction normalized ratio evaluations; no floating point.
"""
from fractions import Fraction as F
from itertools import product
from hashlib import sha256
from pathlib import Path
import json

def get(a,j):return a[j] if 0<=j<len(a) else 0
def d2(a,j):return get(a,j)**2-get(a,j-1)*get(a,j+1)
def d3(a,j):
 x=get(a,j);u=get(a,j-1);v=get(a,j+1);w=get(a,j-2);t=get(a,j+2)
 return x**3-2*u*x*v+w*v**2+u*u*t-w*x*t

def q(a):
 n=len(a)-1;return [F(0)]+[F(a[j-1]*a[j+1],a[j]**2) for j in range(1,n)]+[F(0)]

checked=0; checks=0; pf3=0; strong=0; d=sha256(); classification=sha256()
for length in (3,4,5,6):
 for a in product((1,2,3,4),repeat=length):
  checked+=1
  qs=q(a);n=length-1
  for j in range(1,n):
   phi=F(1)-2*qs[j]+qs[j]**2*(qs[j-1]+qs[j+1]-qs[j-1]*qs[j+1])
   assert phi==F(d3(a,j),a[j]**3),(a,j,'ratio identity')
   checks+=1
  # Strict D2 local criterion matches q_j < 1, including boundary.
  assert all(d2(a,j)>0 for j in range(length))==all(x<1 for x in qs)
  local=all(d2(a,j)>0 and d3(a,j)>=0 for j in range(length))
  ratio=all(qs[j]<1 for j in range(length)) and all(
   F(1)-2*qs[j]+qs[j]**2*(qs[j-1]+qs[j+1]-qs[j-1]*qs[j+1])>=0
   for j in range(1,n))
  assert local==ratio,(a,'classification')
  if local:pf3+=1
  strong_case=all(x<=F(1,2) for x in qs)
  if strong_case:
   assert local
   strong+=1
  classification.update(bytes((length,int(local),int(strong_case))))
  for x in qs:
   classification.update(str(x).encode('ascii')+b';')

# Sharpness of the 1/2 universal threshold for n=2.
assert q((1,2,2))[1]==F(1,2) and d3((1,2,2),1)==0
assert q((1,2,F(21,10)))[1]==F(21,40) and d3((1,2,F(21,10)),1)<0
out={'schema':'R478_RATIO_LOCAL_CERT_V1','result':'R478_RATIO_EXACT_PASS','domain':'positive integer sequences lengths 3..6, every coefficient in {1,2,3,4}','sequences_checked':checked,'exact_normalized_minor_identities':checks,'pf3_local_pass':pf3,'q_at_most_half_sequences':strong,'classification_sha256':classification.hexdigest(),'sharpness_witness':{'boundary':[1,2,2],'failure':['1','2','21/10'],'q_failure':'21/40'},'arithmetic':'Fraction and unbounded Python integers; no floating point','note':'General-real identity is analytic; finite enumeration independently checks the stated finite domain.'}
Path('R478_RATIO_EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False),flush=True)
