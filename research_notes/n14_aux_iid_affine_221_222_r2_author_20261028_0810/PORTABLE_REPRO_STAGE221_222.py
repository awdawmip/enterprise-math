#!/usr/bin/env python3
"""Portable exact independent rerun of author Stage221 and Stage222 auxiliary IID claims.
No external dependencies; all arithmetic Fraction/integer, complete ordered-word DFS.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

PN=(3,1,20); QN=(2,2,20); P=[F(x,24) for x in PN]; Q=[F(x,24) for x in QN]
S=(0,0,0); Z=(14,0,0)
STAGES={
221: dict(T=(6,2,2), U='Q', K=F(208781064,2258455),
 H=F(1164595201473697679395993,15464917737881091440640),
 AL=F(234533154377083721,657366253849018368),
 AR=F(234534888870523721,657366253849018368),
 VL=F(127935693438908681,13695130288521216),
 VR=F(127929012444860681,13695130288521216),
 z0=F(20613104997354313,51200000000000000),
 zs=F(36649221,200000000000),
 gap=F(22638313,6585654780), visits=46186),
222: dict(T=(7,3,1), U='P', K=F(588036024,6419795),
 H=F(410483428040280012261601,5494995559412316241920),
 AL=F(234534888870523721,657366253849018368),
 AR=F(234542079040923721,657366253849018368),
 VL=F(127929012444860681,13695130288521216),
 VR=F(127901570763740681,13695130288521216),
 z0=F(20622487197930313,51200000000000000),
 zs=-F(200284091,320000000000),
 gap=F(121200629,9360061110), visits=38956)
}

def nxt(s,j):return s[0]+1,s[1]+(j==0),s[2]+(j==1)

def check(stage,r):
  K=r['K'];T=r['T'];U=r['U']
  @lru_cache(None)
  def bell(s):
    opts={'P':K*F(2**(s[1]+s[2]),3**s[1]),'Q':K}
    if s[0]<14:opts['C']=1+sum(P[j]*bell(nxt(s,j))[0] for j in range(3))
    v=min(opts.values())
    return v,tuple(a for a,x in opts.items() if x==v),tuple(x-v for x in opts.values() if x>v)
  states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
  assert len(states)==680 and bell(S)[0]==r['H']
  ties={s:bell(s)[1] for s in states if len(bell(s)[1])>1}
  assert ties=={T:('P','C') if U=='P' else ('Q','C'),Z:('P','Q')}
  gaps=[x for s in states for x in bell(s)[2]]
  assert len(gaps)==1238 and min(gaps)==r['gap']
  def act(s,u,z):
    if s==T:return U if u else 'C'
    if s==Z:return 'P' if z else 'Q'
    opts=bell(s)[1];assert len(opts)==1
    return opts[0]
  def suffix(s,u,z):
    a=act(s,u,z)
    if a=='P':return F(0),F(1),F(0),F(0)
    if a=='Q':return F(1),F(0),F(0),F(0)
    c=[suffix(nxt(s,j),u,z) for j in range(3)]
    return tuple(F(i>=2)+sum((P if i%2==0 else Q)[j]*c[j][i] for j in range(3)) for i in range(4))
  def ordered(u,z):
    stack=[((),1,1,0,0)];total=[0]*4;visited=0
    while stack:
      w,p,q,a,b=stack.pop();visited+=1;n=len(w);choice=act((n,a,b),u,z)
      if choice=='C':
        for j in (0,1,2):stack.append((w+(j,),p*PN[j],q*QN[j],a+(j==0),b+(j==1)))
      else:
        factor=24**(14-n)
        total[0]+=(choice=='Q')*p*factor
        total[1]+=(choice=='P')*q*factor
        total[2]+=n*p*factor;total[3]+=n*q*factor
    return tuple(F(x,24**14) for x in total),visited
  O={};vis=0
  for u,z in product((0,1),repeat=2):
    f=suffix(S,u,z);g,n=ordered(u,z);assert f==g
    O[(u,z)]=f;vis+=n
  assert vis==r['visits']
  sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
  v=O[(0,0)];du=sub(O[(1,0)],v);dz=sub(O[(0,1)],v)
  assert sub(sub(O[(1,1)],O[(1,0)]),dz)==(F(0),)*4
  den=dz[0]-dz[1]
  z0=-(v[0]-v[1])/den;zs=-(du[0]-du[1])/den
  assert (z0,zs)==(r['z0'],r['zs']) and 0<z0<1 and 0<z0+zs<1
  def B(u):return tuple(v[i]+u*du[i]+(z0+zs*u)*dz[i] for i in range(4))
  left,right=B(F(0)),B(F(1))
  assert left[0]==left[1]==r['AL'] and right[0]==right[1]==r['AR']
  assert left[2]==r['VL'] and right[2]==r['VR']
  assert left[2]>left[3] and right[2]>right[3] and right[0]>left[0]
  assert left[2]+2*K*left[0]==right[2]+2*K*right[0]==r['H']
  assert right[2]-left[2]==-2*K*(right[0]-left[0])
  assert T[2]>Z[2] and Z[0]==14
  print(f'STAGE{stage}_PORTABLE_EXACT_PASS',vis)

for stage,row in STAGES.items():check(stage,row)
