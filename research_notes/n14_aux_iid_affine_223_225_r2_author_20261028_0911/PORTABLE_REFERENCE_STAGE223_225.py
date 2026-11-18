#!/usr/bin/env python3
"""Portable exact independent rerun of author Stages223-225 auxiliary IID claims.
No external dependencies; all arithmetic Fraction/integer, complete ordered-word DFS.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

PN=(3,1,20); QN=(2,2,20); P=[F(x,24) for x in PN]; Q=[F(x,24) for x in QN]
S=(0,0,0); Z=(14,0,0)
STAGES={
223: dict(T=(12,6,4), U='Q', K=F(472392,5245),
 H=F(165229233763072546009,2244717448852930560),
 AL=F(234542079040923721,657366253849018368),
 AR=F(58635519760722649,164341563462254592),
 VL=F(127901570763740681,13695130288521216),
 VR=F(31975392689089889,3423782572130304),
 z0=F(20590441743370313,51200000000000000),
 zs=F(286071,409600000000000),
 gap=F(3955909,293652864), visits=33616),
224: dict(T=(6,3,1), U='P', K=F(450645768,5057815),
 H=F(631359661108760304999589,8658429425029616762880),
 AL=F(58635519760722649,164341563462254592),
 AR=F(58636490861202649,164341563462254592),
 VL=F(31975392689089889,3423782572130304),
 VR=F(31971787522945889,3423782572130304),
 z0=F(5147610444782297,12800000000000000),
 zs=-F(62448123,200000000000),
 gap=F(3955909,327746412), visits=30286),
225: dict(T=(5,2,2), U='Q', K=F(10693130948568,121783416983),
 H=F(3752369166154801283676185135,52119992580109135830319104),
 AL=F(58636490861202649,164341563462254592),
 AR=F(312728966121555653,876488338465357824),
 VL=F(31971787522945889,3423782572130304),
 VR=F(511537461689062799,54780521154084864),
 z0=F(5143613764910297,12800000000000000),
 zs=F(623779977367,8192000000000000),
 gap=F(3959345399,365350250949), visits=25996)
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

# Exact next Bellman dual candidate, not a primal claim.
K226=F(22581264879576,259377559703)
H226=F(7932877273030669030641345071,111006546064102353706942464)
@lru_cache(None)
def dual226(s):
    opts={'P':K226*F(2**(s[1]+s[2]),3**s[1]),'Q':K226}
    if s[0]<14:opts['C']=1+sum(P[j]*dual226(nxt(s,j))[0] for j in range(3))
    m=min(opts.values())
    return m,tuple(a for a,x in opts.items() if x==m),opts
assert dual226(S)[0]==H226
assert {s:dual226(s)[1] for s in [(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)] if len(dual226(s)[1])>1}=={(5,3,1):('P','C'),Z:('P','Q')}
assert H226==STAGES[225]['H']+2*STAGES[225]['AR']*(K226-STAGES[225]['K'])
print('STAGE226_DUAL_ONLY_PASS',K226)
