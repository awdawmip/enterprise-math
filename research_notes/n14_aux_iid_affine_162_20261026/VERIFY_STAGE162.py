#!/usr/bin/env python3
"""Stage162 author exact external ternary iid N14 checker, Fraction only.
Two structurally distinct evaluators: conditional suffix and raw ordered DFS.
This does not grant P000/native BRC or independent Driver acceptance.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json

N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(1776538556208,5886215131);L=F(5152927839848,17658645393)
R=(10,0,1);X=(7,3,3);ACTS='PQC';TIES={R:('Q','C'),X:('Q','C')}
fmt=lambda v: str(v.numerator)+('/'+str(v.denominator) if v.denominator!=1 else '')
def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
@lru_cache(None)
def bell(s):
    opts=[K*ratio(s),L]
    if s[0]<N:opts.append(1+sum(P[i]*bell(child(s,i))[0] for i in range(3)))
    return min(opts),tuple(opts)
strict={};ties={};gaps=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=n,a,b;v,opts=bell(s)
   wins=tuple(ACTS[i] for i,o in enumerate(opts) if o==v)
   if len(wins)>1:ties[s]=wins
   else:strict[s]=wins[0]
   gaps.extend(o-v for o in opts if o>v)
assert len(strict)+len(ties)==680
assert ties==TIES
assert len(gaps)==1238 and min(gaps)==F(1055356088281,183084835434624)
def action(s,r,x):
 if s==R:return 'Q' if r else 'C'
 if s==X:return 'Q' if x else 'C'
 return strict[s]
def suffix(r,x):
 @lru_cache(None)
 def out(s):
  a=action(s,r,x)
  if a=='P':return F(0),F(1),F(0),F(0)
  if a=='Q':return F(1),F(0),F(0),F(0)
  cs=[out(child(s,i)) for i in range(3)]
  return (sum(P[i]*cs[i][0] for i in range(3)),
          sum(Q[i]*cs[i][1] for i in range(3)),
          F(1)+sum(P[i]*cs[i][2] for i in range(3)),
          F(1)+sum(Q[i]*cs[i][3] for i in range(3)))
 return out((0,0,0))
def dfs(r,x):
 pn=(3,1,20);qn=(1,1,10);d=defaultdict(int)
 hits={R:[0,F(0),F(0)],X:[0,F(0),F(0)]}
 nodes=0
 def visit(n,a,b,p,q):
  nonlocal nodes
  nodes+=1;s=n,a,b
  if s in hits:
   h=hits[s];h[0]+=1;h[1]+=F(p,24**n);h[2]+=F(q,12**n)
  act=action(s,r,x)
  if act=='C':
   for i in range(3):visit(n+1,a+(i==0),b+(i==1),p*pn[i],q*qn[i])
   return
  d[n,'allp']+=p;d[n,'allq']+=q
  d[n,'tp']+=n*p;d[n,'tq']+=n*q
  if act=='P':d[n,'eq']+=q
  else:d[n,'ep']+=p
 visit(0,0,0,1,1)
 tot=lambda tag,base:sum((F(d[n,tag],base**n) for n in range(N+1)),F(0))
 assert tot('allp',24)==tot('allq',12)==1
 return (tot('ep',24),tot('eq',12),tot('tp',24),tot('tq',12)),hits,nodes
corners={};nodes={};hits=None
for r in (0,1):
 for x in (0,1):
  v=suffix(r,x);w,h,n=dfs(r,x)
  assert v==w,(r,x,v,w)
  corners[r,x]=v;nodes[f'{r}{x}']=n
  if hits is None:hits=h
  else:assert h==hits
assert sum(nodes.values())==1913008
assert hits[R]==[10,F(9765625,120932352),F(9765625,60466176)]
assert hits[X]==[56,F(35,5308416),F(35,2239488)]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0];dR=sub(corners[1,0],base);dX=sub(corners[0,1],base)
assert sub(sub(corners[1,1],corners[1,0]),dX)==(F(0),)*4
assert base==(F(608980370270800655,1752976676930715648),
 F(7002931380335,20061226008576),
 F(2600664590463380201,219122084616339456),
 F(153523688266399,13374150672384))
D=lambda v:v[0]-v[1]
D0,Dr,Dx=D(base),D(dR),D(dX)
assert D0==F(-8835332954136275,5258930030792146944)
assert Dr==F(225517578125,40122452017152)
assert Dx==F(126080896865,657366253849018368)
r0=-D0/Dr;slope=-Dx/Dr
assert r0==F(353413318165451,1182361600000000)
assert slope==F(-3602311339,105568000000000)
assert 0<r0+slope<r0<1
vec=lambda x:tuple(base[i]+(r0+slope*x)*dR[i]+x*dX[i] for i in range(4))
left=vec(F(0));right=vec(F(1))
A=F(440625016346358918245,1265046575011281764352)
B=F(2138967403739208846181,180720939287325966336)
AA=F(440625031179621048365,1265046575011281764352)
BB=F(2138966145833987829541,180720939287325966336)
width=F(29431075655,2510013045657305088)
assert left[0]==left[1]==A and left[2]==B
assert right[0]==right[1]==AA and right[2]==BB
assert right[0]-left[0]==width
assert K+L==F(10482543508472,17658645393)
assert right[2]-left[2]==-(K+L)*width
assert left[2]-left[3]==F(526231060559760430495,1265046575011281764352)
assert right[2]-right[3]==F(526240831439401052735,1265046575011281764352)
for v in (left,right):
 assert v[2]>v[3] and v[2]+K*v[1]+L*v[0]==bell((0,0,0))[0]
assert bell((0,0,0))[0]==F(211461038972875305263848856447,967349797503719726804631552)
cert={'status':'AUTHOR_EXACT_NOT_ADMITTED',
'model':{'N':N,'P':['1/8','1/24','5/6'],'Q':['1/12','1/12','5/6']},
'dual':{'K':fmt(K),'L':fmt(L),'Hroot':fmt(bell((0,0,0))[0]),'states':680,'positive_gaps':len(gaps),'min_gap':fmt(min(gaps)),
'ties':{str(k):list(v) for k,v in ties.items()}},
'first_hits':{str(k):{'count':v[0],'Pmass':fmt(v[1]),'Qmass':fmt(v[2])} for k,v in hits.items()},
'dfs_nodes':nodes,'corners':{f'{r}{x}':[fmt(z) for z in corners[r,x]] for (r,x) in corners},
'M00':[fmt(z) for z in base],'dR':[fmt(z) for z in dR],'dX':[fmt(z) for z in dX],'mixed':['0']*4,
'error':{'D0':fmt(D0),'Dr':fmt(Dr),'Dx':fmt(Dx),'r0':fmt(r0),'rSlope':fmt(slope),'r1':fmt(r0+slope)},
'left':{'alpha':fmt(A),'V':fmt(B),'time_gap':fmt(left[2]-left[3])},
'right':{'alpha':fmt(AA),'V':fmt(BB),'time_gap':fmt(right[2]-right[3])},
'width':fmt(width),'slope':fmt(K+L),'author_scope':'finite iid, all-real interval, strict right dual support sharpness'}
if __name__=='__main__':
 Path(__file__).with_name('certificate162.json').write_text(json.dumps(cert,indent=2)+'\n')
 print('STAGE162 PASS: states=680, gaps=1238, corner DFS nodes=1913008')
 print('alpha162',fmt(AA),'V162',fmt(BB),'width',fmt(width))
