#!/usr/bin/env python3
"""Exact dual/primal certificates for external ternary IID stages 231--233.

No floating point, data-driven optimization, or native X6 interpretation.
Two independent implementations: rational count-state suffix DP and unmerged
ordered-history DFS carrying separate positive integer P/Q branch masses.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json

N, DEN = 14, 24
PN, QN = (3,1,20), (2,2,20)
P, Q = tuple(F(k,DEN) for k in PN), tuple(F(k,DEN) for k in QN)
ROOT=(0,0,0); Z=(14,0,0)
STATES=tuple((n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1))
assert len(STATES)==680
S=lambda x:f"{x.numerator}/{x.denominator}"
next_state=lambda s,j:(s[0]+1,s[1]+(j==0),s[2]+(j==1))

CONFIG=(
 (231,F(33912,479),F(33912,479),((10,1,0),Z),(('C','P'),('P','Q')),
  F(14503202310215,40122452017152),F(7243830309143,835884417024),
  F(109004146840315,300082505711616),F(631291740495223,75020626427904),
  F(5990704895603323,100097158938624),15652),
 (232,F(3736,55),F(41652,605),((10,1,0),(12,1,1)),(('C','P'),('C','Q')),
  F(109004146840315,300082505711616),F(631291740495223,75020626427904),
  F(7270819537255,20008983232512),F(21002077276133,2501122904064),
  F(91814076904081,1580343975936),15052),
 (233,F(7768,115),F(342,5),((9,1,0),(12,1,1)),(('C','P'),('C','Q')),
  F(7270819537255,20008983232512),F(21002077276133,2501122904064),
  F(1160041464109745,3183518045011968),F(3286774073290327,397939755626496),
  F(34724256851041,600791924736),14266),
)

def verify(config):
 (stage,lp,lq,ties,choices,alphaL,valueL,alphaR,valueR,H,expected_nodes)=config
 assert lp>0 and lq>0
 @lru_cache(None)
 def opt(s):
  n,a,b=s
  acts={'P':lq*F(2**(a+b),3**a),'Q':lp}
  if n<N:acts['C']=1+sum(P[j]*opt(next_state(s,j))[0] for j in range(3))
  best=min(acts.values())
  return best,tuple(k for k,v in acts.items() if v==best),acts
 opt(ROOT)
 tie_map={s:opt(s)[1] for s in STATES if len(opt(s)[1])>1}
 assert set(tie_map)==set(ties),(stage,tie_map)
 for t,acts in zip(ties,choices):assert set(acts)==set(tie_map[t])
 gaps=[v-opt(s)[0] for s in STATES for v in opt(s)[2].values() if v>opt(s)[0]]
 assert len(gaps)==1238 and min(gaps)>0
 assert opt(ROOT)[0]==H
 def action(s,bits):
  for idx,t in enumerate(ties):
   if s==t:return choices[idx][bits[idx]]
  w=opt(s)[1]
  assert len(w)==1,(stage,s,w)
  return w[0]
 @lru_cache(None)
 def suffix(s,bits):
  a=action(s,bits)
  if a!='C':return F(a=='Q'),F(a=='P'),F(0),F(0)
  kids=[suffix(next_state(s,j),bits) for j in range(3)]
  return tuple(F(k>=2)+sum((P if k%2==0 else Q)[j]*kids[j][k] for j in range(3)) for k in range(4))
 def dfs(bits):
  stack=[(0,0,0,1,1)];mass=[0]*4;visits=0
  while stack:
   n,a,b,p,q=stack.pop();visits+=1
   act=action((n,a,b),bits)
   if act=='C':
    for j in range(3):stack.append((n+1,a+(j==0),b+(j==1),p*PN[j],q*QN[j]))
   else:
    mul=DEN**(N-n)
    mass[1 if act=='P' else 0]+=(q if act=='P' else p)*mul
    mass[2]+=n*p*mul; mass[3]+=n*q*mul
  return tuple(F(x,DEN**N) for x in mass),visits
 corners={};nodes={}
 for bits in product((0,1),repeat=2):
  v=suffix(ROOT,bits);w,count=dfs(bits)
  assert v==w
  assert v[2]+lp*v[0]+lq*v[1]==H
  assert v[2]>v[3]
  corners[bits]=v;nodes[bits]=count
 assert sum(nodes.values())==expected_nodes
 mixed=tuple(corners[1,1][i]-corners[1,0][i]-corners[0,1][i]+corners[0,0][i] for i in range(4))
 if stage==231:assert mixed==(F(0),)*4
 else: assert mixed!=(F(0),)*4
 vertices=[]
 for bits,v in corners.items():
  if v[0]==v[1]:vertices.append((v[0],(bits,),(F(1),),v))
 for a,b in combinations(corners,2):
  v,w=corners[a],corners[b]
  d1=v[0]-v[1];d2=w[0]-w[1]
  if d1*d2>=0:continue
  weight=-d2/(d1-d2)
  assert 0<weight<1
  obs=tuple(weight*v[i]+(1-weight)*w[i] for i in range(4))
  assert obs[0]==obs[1]
  vertices.append((obs[0],(a,b),(weight,1-weight),obs))
 assert len(vertices)==3
 lo=min(vertices,key=lambda x:x[0]);hi=max(vertices,key=lambda x:x[0])
 assert lo[0]==alphaL and hi[0]==alphaR and lo[3][2]==valueL and hi[3][2]==valueR
 assert alphaR>alphaL and all(v[3][2]>v[3][3] for v in vertices)
 assert valueL+(lp+lq)*alphaL==H==valueR+(lp+lq)*alphaR
 if stage==231:
  o=corners[0,0];du=tuple(corners[1,0][i]-o[i] for i in range(4))
  dz=tuple(corners[0,1][i]-o[i] for i in range(4))
  z0=-(o[0]-o[1])/(dz[0]-dz[1]);zs=-(du[0]-du[1])/(dz[0]-dz[1])
  umax=(1-z0)/zs
  assert z0==F(550325289029,625000000000) and zs==F(2513,20000)
  assert 0<umax<1 and z0+zs>1
  assert umax==F(10667815853,11218750000)
 else:z0=zs=umax=None
 return {
  'stage':stage,'model':{'N':N,'P':list(PN),'Q':list(QN),'denominator':DEN},
  'penalty_eP':S(lp),'penalty_eQ':S(lq),'H':S(H),'slope':S(-(lp+lq)),
  'tied_states':[list(s) for s in ties],'choices_u0_u1':[list(x) for x in choices],
  'all_Bellman_states':len(STATES),'strict_positive_gaps':len(gaps),'minimum_strict_gap':S(min(gaps)),
  'corner_observations':{''.join(map(str,bits)):[S(v) for v in obs] for bits,obs in corners.items()},
  'dfs_nodes':{''.join(map(str,bits)):nodes[bits] for bits in corners},'total_dfs_nodes':sum(nodes.values()),
  'interaction_coefficient':[S(x) for x in mixed],
  'balanced_face_vertices':[
    {'alpha':S(v[0]),'policies':[''.join(map(str,b)) for b in v[1]],'weights':[S(w) for w in v[2]],
     'observations':[S(x) for x in v[3]]} for v in sorted(vertices,key=lambda v:v[0])],
  'alpha_left':S(alphaL),'alpha_right':S(alphaR),'delta':S(alphaR-alphaL),
  'V_left':S(valueL),'V_right':S(valueR),
  'tP_minus_tQ_left':S(lo[3][2]-lo[3][3]),'tP_minus_tQ_right':S(hi[3][2]-hi[3][3]),
  'z0_stage231':S(z0) if z0 is not None else None,
  'zs_stage231':S(zs) if zs is not None else None,
  'u_max_stage231':S(umax) if umax is not None else None,
  'classification':'AUTHOR_EXACT_UNREVIEWED_EXTERNAL_AUXILIARY',
  'verification':'Fraction Bellman 680 + Fraction suffix DP + independent ordered integer-mass DFS + all balanced edge vertices'
 }

def main():
 reports=[verify(c) for c in CONFIG]
 for i in range(2):
  assert reports[i]['alpha_right']==reports[i+1]['alpha_left']
  assert reports[i]['V_right']==reports[i+1]['V_left']
  assert F(reports[i]['slope'])<F(reports[i+1]['slope'])
 root=Path(__file__).resolve().parent
 (root/'certificate231_233.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
 for r in reports:
  print('STAGE',r['stage'],'PASS','nodes',r['total_dfs_nodes'],'alphaR',r['alpha_right'],
        'Vright',r['V_right'],'mixed',r['interaction_coefficient'])
 print('STAGE231_233_EXACT_PASS',sum(r['total_dfs_nodes'] for r in reports),
       'states_each',680,'gaps_each',1238,'balanced_vertices_each',3)

if __name__=='__main__':main()
