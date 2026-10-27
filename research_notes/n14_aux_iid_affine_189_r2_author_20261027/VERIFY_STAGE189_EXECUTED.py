#!/usr/bin/env python3
"""Stage189 N14 external ternary IID author exact certificate (rational, ordered-history DFS)."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6)); N=14
K=F(241967493,1388612); L=F(59424392,347153)
H=F(209137371682549614928313,1584768521683668566016)
X=(8,0,1); T=(13,6,4)
alpha188=F(9370003598922725167379,26711406663770723844096)
V188=F(1153476444134184737662789,106845626655082895376384)
@lru_cache(None)
def bell(s):
 n,a,b=s; ell=F(2**(a+b),3**a)
 opts=[('P',K*ell),('Q',L)]
 if n<N:opts.append(('C',1+sum(P[i]*bell((n+1,a+(i==0),b+(i==1)))[0] for i in range(3))))
 m=min(v for _,v in opts)
 return m,tuple(action for action,v in opts if v==m),{action:v-m for action,v in opts if v>m}
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
ties=[(s,bell(s)[1]) for s in states if len(bell(s)[1])>1]
gaps=[v for s in states for v in bell(s)[2].values()]
assert len(states)==680 and len(gaps)==1238 and len(ties)==2 and dict(ties)=={X:('Q','C'),T:('Q','C')}, ties
assert min(gaps)==F(66370340952961,3582466457075712) and bell((0,0,0))[0]==H
# A path from X to T would require six first symbols and three second symbols in five further draws.
assert T[0]-X[0]==5 and T[1]-X[1]==6 and T[2]-X[2]==3
assert T[1]-X[1] > T[0]-X[0]
@lru_cache(None)
def default_action(s):
 if s in (X,T):return 'C'
 a=bell(s)[1];assert len(a)==1
 return a[0]
@lru_cache(None)
def outcome(s, xc,tc):
 if s==X:
  vC=continuation(s,xc,tc)
  return tuple(F(xc)*u+(1-F(xc))*v for u,v in zip((F(1),F(0),F(0),F(0)),vC))
 if s==T:
  vC=continuation(s,xc,tc)
  return tuple(F(tc)*v+(1-F(tc))*u for u,v in zip((F(1),F(0),F(0),F(0)),vC))
 ac=default_action(s)
 if ac=='P':return (F(0),F(1),F(0),F(0))
 if ac=='Q':return (F(1),F(0),F(0),F(0))
 return continuation(s,xc,tc)
def continuation(s,xc,tc):
 n,a,b=s;v=[outcome((n+1,a+(i==0),b+(i==1)),xc,tc) for i in range(3)]
 return tuple(sum((P if j in(0,2) else Q)[i]*v[i][j] for i in range(3))+(1 if j>=2 else 0) for j in range(4))
corners={(x,t):outcome((0,0,0),x,t) for x,t in product((0,1),repeat=2)}
B=corners[0,0]; DX=tuple(corners[1,0][i]-B[i] for i in range(4)); DT=tuple(corners[0,1][i]-B[i] for i in range(4)); C=tuple(corners[1,1][i]-corners[1,0][i]-corners[0,1][i]+B[i] for i in range(4))
assert C==(F(0),)*4
# independent ordered-history tree weights; totals scaled by 24^14
DEN=24**N

def dfs(xc,tc):
 visited=hitsX=hitsT=ancestral_XT=0
 sums=[0]*4
 def rec(n,a,b,pwt,qwt,seenX):
  nonlocal visited,hitsX,hitsT,ancestral_XT
  visited+=1;s=(n,a,b)
  if s==X:hitsX+=1;seenX=True
  if s==T:
   hitsT+=1
   if seenX:ancestral_XT+=1
  ac=('Q' if xc else 'C') if s==X else (('C' if tc else 'Q') if s==T else default_action(s))
  if ac!='C':
   scale=24**(N-n)
   if ac=='Q':sums[0]+=pwt*scale
   if ac=='P':sums[1]+=qwt*scale
   sums[2]+=n*pwt*scale;sums[3]+=n*qwt*scale
  else:
   assert n<N
   rec(n+1,a+1,b,3*pwt,2*qwt,seenX)
   rec(n+1,a,b+1,pwt,2*qwt,seenX)
   rec(n+1,a,b,20*pwt,20*qwt,seenX)
 rec(0,0,0,1,1,False)
 return tuple(F(x,DEN) for x in sums),dict(nodes=visited,hits_X=hitsX,hits_T=hitsT,X_ancestor_of_T=ancestral_XT)
walks={};total_nodes=0
for x,t in product((0,1),repeat=2):
 z,w=dfs(x,t);assert z==corners[x,t],(x,t,z,corners[x,t]);assert w['X_ancestor_of_T']==0
 walks[f'{x}{t}']=w;total_nodes+=w['nodes']
# Error equality x(t) = - (dB+dT*t)/dX.
DB=B[0]-B[1];dX=DX[0]-DX[1];dT=DT[0]-DT[1]
assert dX>0 and dT<0
x0=-DB/dX;xslope=-dT/dX

def x_bal(t):return x0+xslope*t
def O(t):
 x=x_bal(t)
 return tuple(B[i]+DX[i]*x+DT[i]*t for i in range(4))
assert 0<x0<1 and xslope>0
assert O(F(0))[0]==alpha188 and O(F(0))[2]==V188,(O(F(0)),alpha188,V188)
# Continuation until another probability hits boundary: x reaches 0 or t reaches 1.
t_to_one=(F(1)-x0)/xslope
endpoint=min(F(1),t_to_one)
assert endpoint>0
for t in (F(0),endpoint):
 assert F(0)<=x_bal(t)<=1
 o=O(t);assert o[0]==o[1] and o[2]>=o[3]
 assert o[2]+K*o[1]+L*o[0]==H
alpha_slope=O(F(1))[0]-O(F(0))[0]
v_slope=O(F(1))[2]-O(F(0))[2]
tgap0=O(F(0))[2]-O(F(0))[3]
tgap_slope=O(F(1))[2]-O(F(1))[3]-tgap0
assert alpha_slope>0 and v_slope<0
alpha_new=O(endpoint)[0];v_new=O(endpoint)[2]
assert alpha_new>alpha188 and v_new<V188
assert tgap0>0 and tgap0+tgap_slope*endpoint>0
assert -(v_slope/alpha_slope)==K+L
# Strict sharpness: complete-history minimizers at X and T reduce to effective independent coins because no ancestry.
# Equality on the support for alpha > alpha_new would imply common error alpha and x,x(t) in legal [0,1].
# With alpha(t) increasing, largest legal t is endpoint.  Hence contradiction.
# Stage190 dual candidate: choose active tie at newly saturated coin, retain any interior tie.

def fmt(v):return str(v)
print('ROOT',H,'BELL',len(states),'GAPS',len(gaps),'MIN_GAP',min(gaps),'TIES',ties)
print('FOUR_CORNER', {f'{x}{t}':[fmt(u) for u in corners[x,t]] for x,t in product((0,1),repeat=2)})
print('B',[fmt(v) for v in B]);print('DX',[fmt(v) for v in DX]);print('DT',[fmt(v) for v in DT]);print('C',[fmt(v) for v in C]);print('DFS',walks,'NODE_TOTAL',total_nodes)
print('X(t)=',x0,' + ',xslope,'*t','T_END',endpoint,'x_end',x_bal(endpoint))
print('ALPHA(t)=',alpha188,' + ',alpha_slope,'*t')
print('TP(t)=',V188,' + ',v_slope,'*t','GAP(t)=',tgap0,' + ',tgap_slope,'*t')
print('ST189_PROVED','alpha',alpha_new,'V',v_new,'delta',alpha_new-alpha188,'slope',-(K+L),'tgap_end',O(endpoint)[2]-O(endpoint)[3])
CERT={'stage':189,'model':'external_ternary_iid_N14','source_Stage188':'EM_STAGE188_AUTHOR_EXACT_PORTABLE_20261027.zip','P':[str(u) for u in P],'Q':[str(u) for u in Q],'N':N,'K':str(K),'L':str(L),'H':str(H),'ties':[list(s) for s,a in ties],'states':len(states),'positive_gaps':len(gaps),'minimum_positive_gap':str(min(gaps)),'four_corners':{f'{x}{t}':[str(u) for u in corners[x,t]] for x,t in product((0,1),repeat=2)},'B':[str(v) for v in B],'DX':[str(v) for v in DX],'DT':[str(v) for v in DT],'C':[str(v) for v in C],'walks':walks,'dfs_nodes':total_nodes,'x0':str(x0),'xslope':str(xslope),'t_end':str(endpoint),'x_end':str(x_bal(endpoint)),'alpha188':str(alpha188),'V188':str(V188),'alpha_slope':str(alpha_slope),'timeP_slope':str(v_slope),'time_gap0':str(tgap0),'time_gap_slope':str(tgap_slope),'alpha189':str(alpha_new),'V189':str(v_new),'delta_alpha':str(alpha_new-alpha188),'timegap_end':str(O(endpoint)[2]-O(endpoint)[3]),'test_status':'PASS'}
Path(__file__).with_name('certificate189.json').write_text(json.dumps(CERT,ensure_ascii=False,indent=2)+'\n')
print('STAGE189_AUTHOR_EXACT_FULL_REAL_PASS')
