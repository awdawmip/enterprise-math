#!/usr/bin/env python3
"""Stage111 exact Fraction certificate, external ternary iid N=14. Author code."""
from fractions import Fraction as F
p=(F(1,8),F(1,24),F(5,6));q=(F(1,12),F(1,12),F(5,6))
states=[(n,a,b) for n in range(14,-1,-1) for a in range(n+1) for b in range(n-a+1)]
A=(10,3,0);T=(4,0,2)
K=F(328788597439629,341261245318)
def L(k):return -F(185064,635)+F(21376,17145)*k
def ch(z):
 n,a,b=z
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(z):return F(2**(z[1]+z[2]),3**z[1])
def bell(k):
 val={};opts={};gap={}
 for z in states:
  costs={'P':k*ratio(z),'Q':L(k)}
  if z[0]<14:costs['C']=1+sum((p[j]*val[c] for j,c in enumerate(ch(z))),F(0))
  best=min(costs.values());val[z]=best
  opts[z]=tuple(a for a,c in costs.items() if c==best)
  gap[z]={a:c-best for a,c in costs.items()}
 return val,opts,gap
h,options,gap=bell(K)
assert len(states)==680
assert {z for z,ops in options.items() if len(ops)>1}=={A,T}
assert sum(t>0 for row in gap.values() for t in row.values())==1238
assert not any(t<0 for row in gap.values() for t in row.values())
assert min(t for row in gap.values() for t in row.values() if t>0)==F(67830632993,3071351207862)
base={z:('C' if z in (A,T) else options[z][0]) for z in states}
a0=F(13084102571183753507,37682150988866125824)
v0=F(1934432098641265410385,150728603955464503296)
u0=F(159869038712303,211315200000000)
assert h[0,0,0]==v0+(K+L(K))*a0
# Exact first-hit positive rational branch weights. Neither tie state can follow the other.
assert T[2]>A[2] and A[0]>T[0]
hit={(0,0,0):1};pm={(0,0,0):F(1)};qm={(0,0,0):F(1)}
for z in reversed(states):
 if z not in hit or base[z]!='C':continue
 for j,c in enumerate(ch(z)):
  hit[c]=hit.get(c,0)+hit[z]
  pm[c]=pm.get(c,F(0))+pm[z]*p[j]
  qm[c]=qm.get(c,F(0))+qm[z]*q[j]
assert (hit[A],pm[A],qm[A])==(120,F(390625,5971968),F(390625,20155392))
assert (hit[T],pm[T],qm[T])==(6,F(25,3456),F(25,864))
suffix={}
for z in states:
 if base[z]=='P':suffix[z]=(F(0),F(1),F(0),F(0),1)
 elif base[z]=='Q':suffix[z]=(F(1),F(0),F(0),F(0),1)
 else:
  ss=[suffix[t] for t in ch(z)]
  suffix[z]=(sum((p[j]*ss[j][0] for j in range(3)),F(0)),
             sum((q[j]*ss[j][1] for j in range(3)),F(0)),
             1+sum((p[j]*ss[j][2] for j in range(3)),F(0)),
             1+sum((q[j]*ss[j][3] for j in range(3)),F(0)),
             sum(s[4] for s in ss))
assert suffix[A]==(F(635,165888),F(10201,10368),F(7711,6912),F(1069,864),21)
assert suffix[T]==(F(97026796793,97844723712),F(23538461,15479341056),F(21341487367,12230590464),F(1826080831,1289945088),1555)
x=-pm[A]*suffix[A][0]; y=qm[A]*(1-suffix[A][1])
zp=pm[T]*(1-suffix[T][0]);zq=-qm[T]*suffix[T][1]
du=(zp-zq)/(y-x); eta=x*du+zp
assert du==F(16351264081,88048000000)
assert eta==F(609395080925,43613600681558016)
assert 0<u0 and u0+du==F(199112072506703,211315200000000)<1
def moments(u,w):
 vals={}
 for z in states:
  actions={'P':u,'C':1-u} if z==A else {'Q':w,'C':1-w} if z==T else {base[z]:F(1)}
  row=[F(0)]*4
  for ac,weight in actions.items():
   if ac=='P':m=(F(0),F(1),F(0),F(0))
   elif ac=='Q':m=(F(1),F(0),F(0),F(0))
   else:
    cs=[vals[t] for t in ch(z)]
    m=(sum((p[j]*cs[j][0] for j in range(3)),F(0)),
       sum((q[j]*cs[j][1] for j in range(3)),F(0)),
       1+sum((p[j]*cs[j][2] for j in range(3)),F(0)),
       1+sum((q[j]*cs[j][3] for j in range(3)),F(0)))
   for j in range(4):row[j]+=weight*m[j]
  vals[z]=tuple(row)
 return vals[0,0,0]
for w in (F(0),F(1,2),F(1)):
 eP,eQ,tP,tQ=moments(u0+du*w,w)
 assert eP==eQ==a0+eta*w
 assert tP==v0-(K+L(K))*eta*w and tP>tQ
 assert tP+K*eQ+L(K)*eP==h[0,0,0]
assert a0+eta==F(13084629088533672707,37682150988866125824)
assert v0-(K+L(K))*eta==F(1930486964443856499985,150728603955464503296)
assert moments(u0+du,F(1))[3]==F(114606239754171547805,9420537747216531456)
# Dual-only next breakpoint: affine fixed-action differences.
policy={z:('C' if z==A else 'Q' if z==T else options[z][0]) for z in states}
def fixed_gap(k):
 v={};ret={}
 for z in states:
  c={'P':k*ratio(z),'Q':L(k)}
  if z[0]<14:c['C']=1+sum((p[j]*v[t] for j,t in enumerate(ch(z))),F(0))
  v[z]=c[policy[z]]
  ret[z]={ac:cost-v[z] for ac,cost in c.items()}
 return ret
g0=fixed_gap(K);g1=fixed_gap(K-F(1))
roots=[(K-g0[z][ac]/(g0[z][ac]-g1[z][ac]),z,ac)
       for z in states for ac in g0[z]
       if g0[z][ac]>0 and g0[z][ac]>g1[z][ac]]
assert len(roots)==849
k2,z2,ac2=max(roots)
assert (k2,z2,ac2)==(F(50591871,53872),(14,7,4),'Q')
assert all(g>=0 for row in fixed_gap(k2).values() for g in row.values())
assert {z for z,ops in bell(k2)[1].items() if len(ops)>1}=={A,z2}
print('PASS_STAGE111_AUTHOR_EXACT',a0+eta,v0-(K+L(K))*eta,'STAGE112_DUAL_ONLY',k2,L(k2))
