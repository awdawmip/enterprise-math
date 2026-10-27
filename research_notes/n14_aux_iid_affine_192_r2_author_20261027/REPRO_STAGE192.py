#!/usr/bin/env python3
"""Exact author-level Stage192 external N14 IID proof; full history DFS + suffix DP."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(48460834424347609212,295508725848336913)
L=F(48143893907559849832,295508725848336913)
H=F(75225538324811500070605605945717953,599560074353758700400961143177216)
X=(8,0,1);Z=(3,2,0) # Z is named Y in the accompanying Stage192 proof
alpha191=F(4019708522944196853791,11447745713044595933184)
V191=F(488968003499440699225081,45790982852178383732736)
x191=F(3031949890455107,6419704320000000)

@lru_cache(None)
def bell(s):
 n,a,b=s
 lr=F(2**(a+b),3**a)
 actions={'P':K*lr,'Q':L}
 if n<N:
  actions['C']=1+sum(P[i]*bell((n+1,a+(i==0),b+(i==1)))[0] for i in range(3))
 lo=min(actions.values())
 return lo,tuple(c for c,w in actions.items() if w==lo),{c:w-lo for c,w in actions.items() if w>lo}
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
ties={s:bell(s)[1] for s in states if len(bell(s)[1])>1}
gaps=[v for s in states for v in bell(s)[2].values()]
assert len(states)==680 and len(gaps)==1238 and ties=={X:('Q','C'),Z:('P','C')},ties
assert min(gaps)==F(380166467087574396707,9191503408786671341952)
assert bell((0,0,0))[0]==H
# Z denotes Y=(3,2,0) in the proof. Y -> X would decrease first-symbol count, and X -> Y decreases depth.
assert Z[0]<X[0] and Z[1]>X[1] # Y cannot precede X, X cannot precede Y

@lru_cache(None)
def policy_action(s):
 if s in (X,Z): return 'C'
 opts=bell(s)[1]
 assert len(opts)==1,(s,opts)
 return opts[0]

def cont(s,x,z):
 n,a,b=s
 ch=[dp((n+1,a+(i==0),b+(i==1)),x,z) for i in range(3)]
 return tuple(sum((P if j in (0,2) else Q)[i]*ch[i][j] for i in range(3))+(1 if j>=2 else 0) for j in range(4))

@lru_cache(None)
def dp(s,x,z):
 if s==X:
  base=cont(s,x,z)
  return tuple(F(x)*u+(1-F(x))*v for u,v in zip((F(1),F(0),F(0),F(0)),base))
 if s==Z:
  base=cont(s,x,z)
  return tuple(F(z)*u+(1-F(z))*v for u,v in zip((F(0),F(1),F(0),F(0)),base))
 ac=policy_action(s)
 if ac=='P':return F(0),F(1),F(0),F(0)
 if ac=='Q':return F(1),F(0),F(0),F(0)
 return cont(s,x,z)

corners={(x,z):dp((0,0,0),x,z) for x,z in product((0,1),repeat=2)}
B=corners[0,0]
DX=tuple(corners[1,0][j]-B[j] for j in range(4))
DZ=tuple(corners[0,1][j]-B[j] for j in range(4))
C=tuple(corners[1,1][j]-corners[1,0][j]-corners[0,1][j]+B[j] for j in range(4))
assert C==(F(0),)*4
# Whole ordered tree, integer branch weights: P=(3,1,20)/24, Q=(2,2,20)/24.
DEN=24**N

def dfs(x,z):
 sums=[0,0,0,0]
 visited=hits_X=hits_Z=ancestor_XZ=0
 def go(n,a,b,pwt,qwt,seenX):
  nonlocal visited,hits_X,hits_Z,ancestor_XZ
  visited+=1;s=(n,a,b)
  if s==X:hits_X+=1;seenX=True
  if s==Z:
   hits_Z+=1
   if seenX:ancestor_XZ+=1
  action= ('Q' if x else 'C') if s==X else ('P' if z else 'C') if s==Z else policy_action(s)
  if action=='C':
   assert n<N
   go(n+1,a+1,b,3*pwt,2*qwt,seenX)
   go(n+1,a,b+1,pwt,2*qwt,seenX)
   go(n+1,a,b,20*pwt,20*qwt,seenX)
  else:
   scale=24**(N-n)
   if action=='Q':sums[0]+=pwt*scale
   if action=='P':sums[1]+=qwt*scale
   sums[2]+=n*pwt*scale
   sums[3]+=n*qwt*scale
 go(0,0,0,1,1,False)
 return tuple(F(t,DEN) for t in sums),{'nodes':visited,'hits_X':hits_X,'hits_Z':hits_Z,'X_ancestor_Z':ancestor_XZ}
walks={};node_total=0
for x,z in product((0,1),repeat=2):
 got,stats=dfs(x,z)
 assert got==corners[x,z],(x,z,got,corners[x,z])
 assert stats['X_ancestor_Z']==0
 walks[f'{x}{z}']=stats;node_total+=stats['nodes']

# Error balance (B0-B1)+(DX0-DX1)*x+(DZ0-DZ1)*z=0
DB=B[0]-B[1];ax=DX[0]-DX[1];az=DZ[0]-DZ[1]
assert ax>0
x0=-DB/ax; xs=-az/ax
assert x0==x191,(x0,x191)
def obs(z):
 x=x0+xs*z
 return tuple(B[j]+DX[j]*x+DZ[j]*z for j in range(4))
start=obs(F(0)); end_try=obs(F(1))
assert start[0]==alpha191 and start[2]==V191,(start,alpha191,V191)
# Need positive alpha direction; if rate/coin constraints differ, theorem range follows exact sign.
alpha_speed=end_try[0]-start[0]
p_time_speed=end_try[2]-start[2]
gap0=start[2]-start[3]; gap_speed=end_try[2]-end_try[3]-gap0
max_z=F(1)
if xs>0:
 max_z=min(max_z,(F(1)-x0)/xs)
elif xs<0:
 max_z=min(max_z,-x0/xs)
assert max_z>0
for z in (F(0),max_z):
 x=x0+xs*z
 assert F(0)<=x<=1 and 0<=z<=1
 o=obs(z)
 assert o[0]==o[1]
 assert o[2]+K*o[1]+L*o[0]==H
 assert o[2]>o[3]
assert alpha_speed>0 and p_time_speed<0
assert -(p_time_speed/alpha_speed)==K+L
assert gap0>0 and gap0+gap_speed*max_z>0
alpha192=obs(max_z)[0];V192=obs(max_z)[2]
assert alpha192>alpha191 and V192<V191

fmt=lambda o:[str(u) for u in o]
cert={
 'stage':192,'scope':'EXTERNAL_IID_N14_AUTHOR_NOT_ADMITTED',
 'model':{'N':N,'P':fmt(P),'Q':fmt(Q)},
 'dual':{'K':str(K),'L':str(L),'H':str(H),'states':len(states),'strict_gaps':len(gaps),'min_positive_gap':str(min(gaps)),'ties':[{ 'state':list(s),'actions':list(a)} for s,a in ties.items()]},
 'corner_values':{f'{x}{z}':fmt(corners[x,z]) for x,z in product((0,1),repeat=2)},
 'B':fmt(B),'DX':fmt(DX),'DZ':fmt(DZ),'C':fmt(C),
 'ordered_tree':walks,'ordered_nodes_total':node_total,
 'balance':{'x0':str(x0),'dx_dz':str(xs),'z_end':str(max_z),'x_end':str(x0+xs*max_z),'alpha_slope':str(alpha_speed),'timeP_slope':str(p_time_speed),'time_gap0':str(gap0),'time_gap_slope':str(gap_speed)},
 'predecessor':{'alpha191':str(alpha191),'V191':str(V191),'x191':str(x191)},
 'theorem':{'delta_alpha':str(alpha192-alpha191),'alpha192':str(alpha192),'V192':str(V192),'value_slope':str(-(K+L)),'endpoint_tgap':str(obs(max_z)[2]-obs(max_z)[3])},
 'verification':{'dual':'EXACT_FRACTIONS','suffix_DP':'EXACT_FRACTIONS','unmerged_DFS':'INDEPENDENT_INTEGER_WEIGHTS','first_hit_ancestry':'CHECKED','math_acceptance':'NOT_ADMITTED'}
}
Path(__file__).with_name('certificate192.json').write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n')
print('BELL',len(states),'GAPS',len(gaps),'MIN_GAP',min(gaps),'TIES',ties)
print('CORNERS', {f'{x}{z}':fmt(corners[x,z]) for x,z in product((0,1),repeat=2)})
print('B',fmt(B),'DX',fmt(DX),'DZ',fmt(DZ),'C',fmt(C))
print('DFS_STATS',walks,'TOTAL_NODES',node_total)
print('x(z)=',x0,'+',xs,'*z','z_end',max_z,'x_end',x0+xs*max_z)
print('alpha(z)=',alpha191,'+',alpha_speed,'*z')
print('timeP(z)=',V191,'+',p_time_speed,'*z','gap',gap0,'+',gap_speed,'*z')
print('THEOREM_ALPHA192',alpha192,'V192',V192,'delta',alpha192-alpha191,'slope',-(K+L),'gap_end',obs(max_z)[2]-obs(max_z)[3])
print('STAGE192_AUTHOR_EXACT_FULL_REAL_PASS')
