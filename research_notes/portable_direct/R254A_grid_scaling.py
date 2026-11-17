#!/usr/bin/env python3
"""Exact 21-point characteristic-polynomial scaling experiment, R254A."""
from fractions import Fraction as F
from math import lcm, prod
import json,hashlib
from pathlib import Path

def setup(s):
 t=(1691*s-2615)/(2615*s-3539)
 a=[F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t]
 b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
 pi=[b[i]/(1-a[i]) for i in range(7)]
 z=sum(b[i]/(1-a[i])**2 for i in range(7))
 rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
 assert sum(pi)==sum(rho)==1
 return a,b,pi,rho

def ix(m):return [0]+[j+1 for j in range(6) if (m>>j)&1]
def mult(p,a):
 ans=[F(0)]*(len(p)+1)
 for j,v in enumerate(p):ans[j]-=v*a;ans[j+1]+=v
 return ans

def cp(a,b,idx):
 c=[F(1)]
 for i in idx:c=mult(c,a[i])
 for i in idx:
  rest=[F(1)]
  for j in idx:
   if i!=j:rest=mult(rest,a[j])
  for j,v in enumerate(rest):c[j]-=b[i]*v
 return c

def factors(q):
 vals={};p=2
 while p*p<=q:
  if q%p==0:
   n=0
   while q%p==0:n+=1;q//=p
   vals[p]=n
  p+=1
 if q>1:vals[q]=1
 return vals

def get(j):
 s=F(j,1000);a,b,pi,rho=setup(s)
 L=lcm(*((a[i]*(i==q)+(1-a[i])*pi[q]).denominator for i in range(7) for q in range(7)))
 J=lcm(*(((144,576,1440,4320,17280,86400,518400)[m.bit_count()]*rho[i]).denominator for m in range(63) for i in ix(m)))
 req={}
 for m in range(63):
  c=cp(a,b,ix(m));d=len(c)-1
  for j in range(1,d+1):
   for p,e in factors(c[d-j].denominator).items():req[p]=max(req.get(p,0),(e+j-1)//j)
 T=prod(p**v for p,v in req.items())
 return {'s':str(s),'T':T,'L':L,'J':J,'T_factors':req,'bit_ratio':round(T.bit_length()/L.bit_length(),4)}

if __name__=='__main__':
 rows=[]
 for j in range(390,411):
  row=get(j)
  assert row['L']%row['T']==0
  row['j']=j
  row['T_bits']=row['T'].bit_length()
  row['L_bits']=row['L'].bit_length()
  rows.append(row)
 assert len(rows)==21 and rows[10]['T']==299160
 result={'schema':'EM_R254A_21_POINT_SCALING_V1',
         'frozen_science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
         'parameter_grid':'j/1000 for j=390,...,410',
         'verified_count':len(rows),'all_T_divides_L':True,
         'minimum_T_bits':min(x['T_bits'] for x in rows),
         'maximum_T_bits':max(x['T_bits'] for x in rows),
         'minimum_L_bits':min(x['L_bits'] for x in rows),
         'maximum_L_bits':max(x['L_bits'] for x in rows),
         'algorithm':'for every mask c_m(x), T_min=product_p p^max_{m,j}ceil(v_p(den(c_{m,d-j}))/j)',
         'status':'EXACT_FINITE_FAMILY / NOT_REVIEWED',
         'rows':rows}
 raw=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
 out=Path(__file__).with_name('R254A_21_grid_scaling.json')
 out.write_text(raw,encoding='utf-8')
 print('PASS',len(rows),'anchors; T_min divides L at all 21; SHA256',hashlib.sha256(raw.encode()).hexdigest())
 print('bits',result['minimum_T_bits'],result['maximum_T_bits'],result['minimum_L_bits'],result['maximum_L_bits'])
