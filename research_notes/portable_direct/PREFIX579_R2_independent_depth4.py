#!/usr/bin/env python3
"""PREFIX579 independent finite-depth exact 96 native ports: integer moments degrees 0..4."""
import json
from fractions import Fraction as F
from math import comb
from PREFIX579_R2_native_kernel import edge,ACTIONS
weights={'A5':(1,0,0),'S':(1,1,0),'D':(1,-1,0),'K':(0,0,1),
'A5+K':(1,0,1),'A5-K':(1,0,-1),'A5+2K':(1,0,2),'D+K':(1,-1,1),
'S+K':(1,1,1),'A6':(0,1,0)}
edges=[]
for i in range(96):
  row=[]
  for action in ACTIONS:
    j,w=edge(i,action)
    row.append((j,w[4],w[5],w[6]))
  assert len(row)==6
  edges.append(row)
def cumulant4(moment):
  mu,m2,m3,m4=moment[1:]
  return m4-4*m3*mu-3*m2*m2+12*m2*mu*mu-6*mu**4
cur={name:[[1]*96]+[[0]*96 for j in range(4)] for name in weights}
results=[]
for depth in range(129):
  if depth in (1,2,4,8,16,32,64,128):
    c={}
    for name,arr in cur.items():
      assert all(m==6**depth for m in arr[0])
      mom=[F(sum(vec),96*6**depth) for vec in arr]
      c[name]=cumulant4(mom)
    assert c['A5']==c['A6']
    results.append({'depth':depth,'fourth_rate_display':{k:'%.12f'%float(v/depth) for k,v in c.items()},
       'fourth_A5_exact':str(c['A5']),'fourth_K_exact':str(c['K'])})
  if depth==128:break
  for name,(a,b,c) in weights.items():
    old=cur[name]
    new=[[0]*96 for j in range(5)]
    for i,row in enumerate(edges):
      for j,r5,r6,g in row:
        q=a*r5+b*r6+c*g
        powers=(1,q,q*q,q**3,q**4)
        for k in range(5):
          new[k][i]+=sum(comb(k,l)*powers[k-l]*old[l][j] for l in range(k+1))
    cur[name]=new
print(json.dumps({'status':'ALL_ASSERTIONS_PASS','method':'exact integer 96-port moments 0..4',
  'source':'PREFIX565/566 frozen source kernel reconstructed by PREFIX578','results':results},indent=2))
