#!/usr/bin/env python3
"""Stage190 exact external IID N14 proof: rational Bellman plus independently unmerged path DFS.

Input uses known Stage190 dual as unreviewed candidate; script verifies all finite claims.
This is an author certificate, not native X6 or independent Source admission.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));N=14
K=F(219205722106707916,1293441907677519)
L=F(72144743665153672,431147302559173)
H=F(27408936515658794949498678792123439,212566265355324633731370212917248)
X=(8,0,1);Y=(4,2,0)
alpha189=F(28110010813253777166137,80134219991312171532288)
V189=F(3460429309624219796220367,320536879965248686129152)
x189=F(11602917512839349,44937930240000000)
@lru_cache(None)
def bell(s):
 n,a,b=s;ell=F(2**(a+b),3**a)
 opts={'P':K*ell,'Q':L}
 if n<N:opts['C']=1+sum(P[i]*bell((n+1,a+(i==0),b+(i==1)))[0] for i in range(3))
 m=min(opts.values())
 return m,tuple(act for act,v in opts.items() if v==m),tuple(v-m for act,v in opts.items() if v>m)
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
ties=[(s,bell(s)[1]) for s in states if len(bell(s)[1])>1]
gaps=[v for s in states for v in bell(s)[2]]
assert len(states)==680 and len(gaps)==1238 and dict(ties)=={X:('Q','C'),Y:('P','C')},ties
assert min(gaps)==F(8957179515094375931,362080953867613958784)
assert bell((0,0,0))[0]==H
# Four-symbol counts need not be compressed into a generic BRC shadow. Here exact IID likelihood
# ratio is a sufficient statistic for local Bellman action costs only; the independent DFS
# separately retains all ordered histories and both positive model masses.
assert X[0]>Y[0] and X[1]<Y[1]
# X cannot lead backwards in depth to Y; Y cannot lead to X because a cannot decrease.
@lru_cache(None)
def default_action(s):
 if s in (X,Y):return 'C'
 a=bell(s)[1];assert len(a)==1,(s,a)
 return a[0]
@lru_cache(None)
def outcome(s,xc,yc):
 if s==X:
  v=continuation(s,xc,yc)
  return tuple(F(xc)*u+(1-F(xc))*w for u,w in zip((F(1),F(0),F(0),F(0)),v))
 if s==Y:
  v=continuation(s,xc,yc)
  return tuple(F(yc)*u+(1-F(yc))*w for u,w in zip((F(0),F(1),F(0),F(0)),v))
 ac=default_action(s)
 if ac=='P':return (F(0),F(1),F(0),F(0))
 if ac=='Q':return (F(1),F(0),F(0),F(0))
 return continuation(s,xc,yc)
def continuation(s,xc,yc):
 n,a,b=s
 v=[outcome((n+1,a+(i==0),b+(i==1)),xc,yc) for i in range(3)]
 return tuple(sum((P if j in (0,2) else Q)[i]*v[i][j] for i in range(3))+(1 if j>=2 else 0) for j in range(4))
corners={(x,y):outcome((0,0,0),x,y) for x,y in product((0,1),repeat=2)}
B=corners[0,0];DX=tuple(corners[1,0][j]-B[j] for j in range(4))
DY=tuple(corners[0,1][j]-B[j] for j in range(4))
C=tuple(corners[1,1][j]-corners[1,0][j]-corners[0,1][j]+B[j] for j in range(4))
assert C==(F(0),)*4,C
DEN=24**N
def dfs(xc,yc):
 visited=hitsX=hitsY=y_ancestor_of_x=x_ancestor_of_y=0
 sums=[0]*4
 def rec(n,a,b,pwt,qwt,seenX,seenY):
  nonlocal visited,hitsX,hitsY,y_ancestor_of_x,x_ancestor_of_y
  visited+=1;s=(n,a,b)
  if s==X:
   hitsX+=1
   if seenY:y_ancestor_of_x+=1
   seenX=True
  if s==Y:
   hitsY+=1
   if seenX:x_ancestor_of_y+=1
   seenY=True
  ac=('Q' if xc else 'C') if s==X else ('P' if yc else 'C') if s==Y else default_action(s)
  if ac=='C':
   assert n<N
   rec(n+1,a+1,b,3*pwt,2*qwt,seenX,seenY)
   rec(n+1,a,b+1,pwt,2*qwt,seenX,seenY)
   rec(n+1,a,b,20*pwt,20*qwt,seenX,seenY)
  else:
   w=24**(N-n)
   if ac=='Q':sums[0]+=pwt*w
   if ac=='P':sums[1]+=qwt*w
   sums[2]+=n*pwt*w;sums[3]+=n*qwt*w
 rec(0,0,0,1,1,False,False)
 return tuple(F(v,DEN) for v in sums),dict(nodes=visited,hits_X=hitsX,hits_Y=hitsY,Y_ancestor_of_X=y_ancestor_of_x,X_ancestor_of_Y=x_ancestor_of_y)
walks={};node_total=0
for x,y in product((0,1),repeat=2):
 z,w=dfs(x,y)
 assert z==corners[x,y],(x,y,z,corners[x,y])
 assert w['Y_ancestor_of_X']==w['X_ancestor_of_Y']==0
 walks[f'{x}{y}']=w;node_total+=w['nodes']
# Balance eP=eQ with x as function of y; independent tie cones imply affine exact family.
DB=B[0]-B[1];dX=DX[0]-DX[1];dY=DY[0]-DY[1]
assert dX>0 and dY<0,(DB,dX,dY)
x0=-DB/dX;xslope=-dY/dX
def x_bal(y):return x0+xslope*y
def O(y):
 x=x_bal(y)
 return tuple(B[j]+DX[j]*x+DY[j]*y for j in range(4))
assert x0==x189 and O(F(0))[0]==alpha189 and O(F(0))[2]==V189,(x0,O(F(0)),x189,alpha189,V189)
assert xslope>0
# End when either coin saturates: x<=1, y<=1
end=min(F(1),(F(1)-x0)/xslope)
assert end>0
for y in (F(0),end):
 assert 0<=x_bal(y)<=1
 o=O(y)
 assert o[0]==o[1] and o[2]>o[3]
 assert o[2]+K*o[1]+L*o[0]==H
alpha_slope=O(F(1))[0]-O(F(0))[0]
vp_slope=O(F(1))[2]-O(F(0))[2]
gap0=O(F(0))[2]-O(F(0))[3]
gap_slope=(O(F(1))[2]-O(F(1))[3])-gap0
assert alpha_slope>0 and vp_slope<0
assert gap0>0 and gap0+gap_slope*end>0
assert -(vp_slope/alpha_slope)==K+L
alpha_new=O(end)[0];v_new=O(end)[2]
assert alpha_new>alpha189 and v_new<V189
print('ROOT',H,'STATES',len(states),'GAPS',len(gaps),'MIN_GAP',min(gaps),'TIES',ties)
print('FOUR_CORNERS',{f'{x}{y}':[str(t) for t in corners[x,y]] for x,y in product((0,1),repeat=2)})
print('B',[str(t) for t in B]);print('DX',[str(t) for t in DX]);print('DY',[str(t) for t in DY]);print('MIXED',[str(t) for t in C])
print('DFS',walks,'NODE_TOTAL',node_total)
print('x(y)=',x0,'+',xslope,'*y','END_y=',end,'END_x=',x_bal(end))
print('alpha(y)=',alpha189,'+',alpha_slope,'*y')
print('tP(y)=',V189,'+',vp_slope,'*y')
print('tP-tQ=',gap0,'+',gap_slope,'*y')
print('STAGE190_ALPHA_END',alpha_new,'V_END',v_new,'DELTA',alpha_new-alpha189,'SLOPE',K+L)
cert={'stage':190,'status':'AUTHOR_EXACT_CANDIDATE','model':'external_ternary_iid_N14',
 'read_sources':{'stage189': 'EM_STAGE189_AUTHOR_EXACT_PORTABLE_20261027.tar.xz','stage190_dual':'certificate190_dual.json'},
 'P':list(map(str,P)),'Q':list(map(str,Q)),'N':N,'K':str(K),'L':str(L),'H':str(H),
 'states':len(states),'strict_positive_action_gaps':len(gaps),'min_positive_action_gap':str(min(gaps)),
 'ties':[{'state':list(s),'actions':list(a)} for s,a in ties],
 'corners':{f'{x}{y}':list(map(str,corners[x,y])) for x,y in product((0,1),repeat=2)},
 'B':list(map(str,B)),'DX':list(map(str,DX)),'DY':list(map(str,DY)),'C':list(map(str,C)),
 'walks':walks,'dfs_nodes':node_total,'x0':str(x0),'xslope':str(xslope),'y_end':str(end),'x_end':str(x_bal(end)),
 'alpha189':str(alpha189),'V189':str(V189),'alpha_slope':str(alpha_slope),'tP_slope':str(vp_slope),'tP_minus_tQ_0':str(gap0),'tP_minus_tQ_slope':str(gap_slope),
 'alpha190':str(alpha_new),'V190':str(v_new),'delta_alpha':str(alpha_new-alpha189), 'support_line_slope':str(K+L),
 'test_status':'EXACT_LOCAL_PASS','native_admission':False}
Path(__file__).with_name('certificate190.json').write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
print('STAGE190_AUTHOR_EXACT_FULL_REAL_PASS')
