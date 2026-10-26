#!/usr/bin/env python3
"""Author-level exact-rational certificate for external N14 iid Stage156.

Only Python standard library. Two separate observer implementations:
(1) conditional Bellman suffix recursion on count states;
(2) literal ordered-prefix DFS with integer likelihood numerators.
No formal proof checker, native P000 transfer, or independent Driver claim.
"""
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
PINT=(3,1,20);QINT=(1,1,10)
G=(10,5,4);T=(14,0,0)
STATES=tuple((n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1))
assert len(STATES)==680
K155=F(5736,17)
ALPHA155=F(7319074367111079265,21035720123168587776)
V155=F(5285134557084071317,438244169232678912)


def ratio(a,b):return F(2)**(a+b)/F(3)**a

# Algebraic dual-ray scanner: H_s(t)=intercept+slope*t at K=L=k-t,
# with lexicographic minimizer by (value at t=0, right derivative).
def ray(k):
 @lru_cache(None)
 def visit(s):
  n,a,b=s
  acts={'P':(k*ratio(a,b),-ratio(a,b)),'Q':(k,F(-1))}
  if n<N:
   kids=[visit((n+1,a+1,b))[0],visit((n+1,a,b+1))[0],visit((n+1,a,b))[0]]
   acts['C']=(F(1)+sum(P[i]*kids[i][0] for i in range(3)),sum(P[i]*kids[i][1] for i in range(3)))
  winner=min(acts,key=lambda z:acts[z]);return acts[winner],winner,acts
 roots=[];ties=[];positive=0
 for s in STATES:
  val,act,acts=visit(s)
  for other,expr in acts.items():
   if other==act:continue
   d0,d1=expr[0]-val[0],expr[1]-val[1]
   assert d0>=0 and (d0!=0 or d1>=0),(s,act,other,d0,d1)
   if d0==0:ties.append((s,act,other,d1))
   else:
    positive+=1
    if d1<0:roots.append((d0/(-d1),s,other,act,d0,d1))
 assert roots
 roots.sort()
 return visit((0,0,0))[0],ties,positive,roots[0]

start_dual,ties155,_,first=ray(K155)
assert first[1]==G and first[2]=='Q' and first[3]=='C'
assert first[0]==F(7620096,5545247)
K156=K155-first[0]
assert K156==F(109612440,326191)

@lru_cache(None)
def bell(s):
 n,a,b=s
 acts={'P':K156*ratio(a,b),'Q':K156}
 if n<N:
  child=[bell((n+1,a+1,b))[0],bell((n+1,a,b+1))[0],bell((n+1,a,b))[0]]
  acts['C']=F(1)+sum(P[i]*child[i] for i in range(3))
 value=min(acts.values())
 minimizers=tuple(z for z,v in acts.items() if v==value)
 return value,minimizers,acts

TIES={s:bell(s)[1] for s in STATES if len(bell(s)[1])>1}
assert TIES=={G:('Q','C'),T:('P','Q')},TIES
GAPS=[v-bell(s)[0] for s in STATES for z,v in bell(s)[2].items() if v>bell(s)[0]]
assert len(GAPS)==1238 and min(GAPS)==F(4961,978573)
H=bell((0,0,0))[0]
assert H==F(8787882497416006214970643,35737825951544191746048)

# Conditional suffix observer on the count DAG. g=Prob(Q at G),
# x=Prob(P at T), with unique Bellman minimizers elsewhere.
@lru_cache(None)
def suffix(s,g,x):
 n,a,b=s
 def action(z):
  if z=='P':return (F(0),F(1),F(0),F(0))
  if z=='Q':return (F(1),F(0),F(0),F(0))
  kids=[suffix((n+1,a+1,b),g,x),suffix((n+1,a,b+1),g,x),suffix((n+1,a,b),g,x)]
  return (sum(P[i]*kids[i][0] for i in range(3)),sum(Q[i]*kids[i][1] for i in range(3)),
          F(1)+sum(P[i]*kids[i][2] for i in range(3)),F(1)+sum(Q[i]*kids[i][3] for i in range(3)))
 if s==G:
  a0,a1=action('C'),action('Q')
  return tuple((1-g)*a0[i]+g*a1[i] for i in range(4))
 if s==T:
  a0,a1=action('Q'),action('P')
  return tuple((1-x)*a0[i]+x*a1[i] for i in range(4))
 choices=bell(s)[1]
 assert len(choices)==1
 return action(choices[0])

# Separate literal ordered DFS: 24^14 and 12^14 provide common
# integer denominators, even for leaves stopped at a shorter depth.
DP=24**N;DQ=12**N
POWERP=[24**(N-n) for n in range(N+1)]
POWERQ=[12**(N-n) for n in range(N+1)]
def ordered(g,x):
 hits={G:[0,0,0],T:[0,0,0]}
 accum=[0]*6
 nodes=0
 def dfs(n,a,b,p,q):
  nonlocal nodes
  nodes+=1
  s=(n,a,b)
  if s in hits:
   v=hits[s];v[0]+=1;v[1]+=p*POWERP[n];v[2]+=q*POWERQ[n]
  if s==G:act='Q' if g==1 else 'C'
  elif s==T:act='P' if x==1 else 'Q'
  else:
   choices=bell(s)[1]
   assert len(choices)==1
   act=choices[0]
  if act=='C':
   assert n<N
   dfs(n+1,a+1,b,p*PINT[0],q*QINT[0]);dfs(n+1,a,b+1,p*PINT[1],q*QINT[1]);dfs(n+1,a,b,p*PINT[2],q*QINT[2]);return
  pm=p*POWERP[n];qm=q*POWERQ[n]
  accum[0]+=pm;accum[1]+=qm
  if act=='Q':accum[2]+=pm
  else:accum[3]+=qm
  accum[4]+=n*pm;accum[5]+=n*qm
 dfs(0,0,0,1,1)
 assert accum[0]==DP and accum[1]==DQ
 result=(F(accum[2],DP),F(accum[3],DQ),F(accum[4],DP),F(accum[5],DQ))
 hit_readout={str(s):{'history_count':v[0],'P_mass':str(F(v[1],DP)),'Q_mass':str(F(v[2],DQ))} for s,v in hits.items()}
 return result,hit_readout,nodes

corners={};ordered_counts={};hitcert={}
for g,x in ((0,0),(1,0),(0,1),(1,1)):
 v,hits,nodes=ordered(g,x)
 assert v==suffix((0,0,0),F(g),F(x)),(g,x,v)
 corners[(g,x)]=v;ordered_counts[f'{g}{x}']=nodes
 hitcert[f'{g}{x}']=hits
assert all(hits[str(G)]['history_count']==300 and hits[str(T)]['history_count']==1 for hits in hitcert.values())
assert all(hits[str(G)]['P_mass']=='125/5435817984' and hits[str(G)]['Q_mass']=='125/2579890176' for hits in hitcert.values())
assert all(hits[str(T)]['P_mass']=='6103515625/78364164096' and hits[str(T)]['Q_mass']=='6103515625/78364164096' for hits in hitcert.values())
M00=corners[0,0];M10=corners[1,0];M01=corners[0,1];M11=corners[1,1]
dG=tuple(M10[i]-M00[i] for i in range(4))
dT=tuple(M01[i]-M00[i] for i in range(4))
mixed=tuple(M11[i]-M10[i]-M01[i]+M00[i] for i in range(4))
assert mixed==(F(0),)*4
# Given eP=eQ, x(g)=x0+x1*g. Both coefficients rational.
x0=(M00[1]-M00[0])/(dT[0]-dT[1]);x1=-(dG[0]-dG[1])/(dT[0]-dT[1])
assert x0==F(660133538249389,327680000000000000)
assert x1==F(3449577,327680000000000)
assert 0<x0<x0+x1<1

def M(g):
 x=x0+x1*g
 return tuple(M00[i]+g*dG[i]+x*dT[i] for i in range(4))

start=M(F(0));finish=M(F(1))
assert start[0]==start[1]==ALPHA155 and start[2]==V155
assert finish[0]==finish[1]==F(7319074368089652265,21035720123168587776)
assert finish[2]==F(5285134543382516317,438244169232678912)
assert finish[0]>start[0]
assert start[2]>start[3] and finish[2]>finish[3]
assert all(p[2]+K156*(p[0]+p[1])==H for p in (start,finish))
ALPHA156=finish[0];V156=finish[2]
WIDTH=ALPHA156-ALPHA155
assert WIDTH==F(40773875,876488338465357824)
assert V155-V156==2*K156*WIDTH

# Next exact ray closure from the saturated g=1 face.
_,ties156,_,next_root=ray(K156)
assert next_root[1:4]==((10,2,0),'P','C')
assert next_root[0]==F(63783344160,3434465039)
K157=K156-next_root[0]
assert K157==F(3342600,10529)

cert={
 'schema':'EM_N14_STAGE156_AUTHOR_EXACT_RATIONAL_V1',
 'evidence_class':'AUTHOR_EXACT_COMPUTATION_ASSISTED_NO_INDEPENDENT_REVIEW',
 'model':{'horizon':14,'P':['1/8','1/24','5/6'],'Q':['1/12','1/12','5/6'],'scope':'external finite iid ordered-history randomized policies'},
 'stage155_input':{'alpha':str(ALPHA155),'V':str(V155),'K=L':str(K155)},
 'scan155_to_156':{'t':str(first[0]),'new_state':str(first[1]),'tie':f'{first[2]}/{first[3]}','K156=L156':str(K156)},
 'stage156_bellman':{'states':len(STATES),'dual_root':str(H),'ties':{str(s):list(v) for s,v in TIES.items()},'strict_positive_gaps':len(GAPS),'min_positive_gap':str(min(GAPS)),'negative_gaps':0},
 'first_hits':hitcert['00'],
 'corners':{f'{a}{b}':list(map(str,v)) for (a,b),v in corners.items()},
 'dG':list(map(str,dG)),'dT':list(map(str,dT)),'mixed':list(map(str,mixed)),
 'equalization':{'x0':str(x0),'dx_dg':str(x1),'g_range':['0','1'],'x_endpoints':[str(x0),str(x0+x1)]},
 'endpoints':{'alpha155':str(ALPHA155),'V155':str(V155),'alpha156':str(ALPHA156),'V156':str(V156),'alpha_width':str(WIDTH),'slope':str(2*K156),'tP_minus_tQ':[str(start[2]-start[3]),str(finish[2]-finish[3])],'dual_equal_both':True},
 'ordered_dfs_nodes':ordered_counts,
 'stage157_dual_only':{'ray_t':str(next_root[0]),'K=L':str(K157),'new_state':str(next_root[1]),'tie':f'{next_root[2]}/{next_root[3]}','status':'candidate_not_primal_proof'},
 'limitations':['not independent Research Driver review','not native P000 mapping','not formal theorem admission']
}

if __name__=='__main__':
 path=Path(__file__).parent/'certificate156.json'
 path.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print('PASS: 680 states; 1238 positive gaps; 2 ties; 4 ordered DFS corners crosschecked')
 print('first closure from Stage155:',first[0],G,'K156=L156',K156)
 print('dual root',H,'minimum positive gap',min(GAPS))
 print('first-hits',json.dumps(hitcert['00'],sort_keys=True))
 print('M00',tuple(map(str,M00)))
 print('dG',tuple(map(str,dG)),'dT',tuple(map(str,dT)),'mixed',mixed)
 print('x(g)=',x0,'+',x1,'*g')
 print('alpha156',ALPHA156,'V156',V156,'width',WIDTH,'slope',2*K156)
 print('tP-tQ endpoints',start[2]-start[3],finish[2]-finish[3])
 print('ordered node counts',ordered_counts)
 print('Stage157 candidate ray',next_root[0],'K=L',K157,'state',next_root[1])
 print('certificate',path)
