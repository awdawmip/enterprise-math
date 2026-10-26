#!/usr/bin/env python3
"""Exact reproducible Stage173 author-side external N14 proof checker."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=L=F(451080,1909)
R=(10,0,1);Z=(14,0,0);A=('P','Q','C')
def fmt(x):return str(x)
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return(s[0]+1,s[1]+int(i==0),s[2]+int(i==1))
@lru_cache(None)
def bell(s):
    v=[K*ell(s),L]
    if s[0]<N:v.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F()))
    m=min(v)
    return m,tuple(a for a,x in zip(A,v) if x==m),v
ties={};gaps=[]
for n in range(N+1):
  for a in range(n+1):
    for b in range(n-a+1):
      s=(n,a,b);m,w,v=bell(s)
      if len(w)>1:ties[s]=w
      gaps += [x-m for x in v if x>m]
assert ties=={R:('Q','C'),Z:('P','Q')}
assert len(gaps)==1238 and min(gaps)==F(8039,309258)
H=bell((0,0,0))[0]
assert H==F(9224707194483683711431,52288007441574002688)
def action(s,r,z):
    if s==R:return 'Q' if r else 'C'
    if s==Z:return 'Q' if z else 'P'
    return bell(s)[1][0]
def suffix(r,z):
  @lru_cache(None)
  def rec(s):
    c=action(s,r,z)
    if c=='P':return (F(0),F(1),F(0),F(0))
    if c=='Q':return (F(1),F(0),F(0),F(0))
    v=[rec(child(s,i)) for i in range(3)]
    return (sum((P[i]*v[i][0] for i in range(3)),F()),
            sum((Q[i]*v[i][1] for i in range(3)),F()),
            1+sum((P[i]*v[i][2] for i in range(3)),F()),
            1+sum((Q[i]*v[i][3] for i in range(3)),F()))
  return rec((0,0,0))
def dfs(r,z):
    acc=defaultdict(int);hits={R:[0,F(0),F(0)],Z:[0,F(0),F(0)]};nodes=0
    def walk(n,a,b,p,q):
        nonlocal nodes
        nodes+=1;s=(n,a,b)
        if s in hits:
            hits[s][0]+=1;hits[s][1]+=F(p,24**n);hits[s][2]+=F(q,12**n)
        ac=action(s,r,z)
        if ac=='C':
            assert n<N
            for i in range(3):
                pn=(3,1,20)[i];qn=(1,1,10)[i]
                walk(n+1,a+(i==0),b+(i==1),p*pn,q*qn)
        else:
            acc[n,'ap']+=p;acc[n,'aq']+=q
            acc[n,'tp']+=n*p;acc[n,'tq']+=n*q
            if ac=='P':acc[n,'eq']+=q
            else:acc[n,'ep']+=p
    walk(0,0,0,1,1)
    m=lambda tag,den:sum((F(acc[n,tag],den**n) for n in range(N+1)),F())
    assert m('ap',24)==m('aq',12)==1
    return (m('ep',24),m('eq',12),m('tp',24),m('tq',12)),hits,nodes
corners={};hs=None;nodes=[]
for r in (0,1):
 for z in (0,1):
    v=suffix(r,z);w,h,n=dfs(r,z)
    assert v==w
    corners[r,z]=v;nodes.append(n)
    if hs is None:hs=h
    else:assert hs==h
assert hs[R][0]==10 and hs[Z][0]==1
assert sum(nodes)==1144144
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
B=corners[0,0];dR=sub(corners[1,0],B);dZ=sub(corners[0,1],B)
assert sub(sub(corners[1,1],corners[1,0]),dZ)==(F(0),)*4
assert dR==(F(4521484375,1486016741376),
            -F(3232421875,1253826625536),
            -F(61181640625,557256278016),
            -F(20751953125,104485552128))
assert dZ==(F(6103515625,78364164096),-F(6103515625,78364164096),F(),F())
D=lambda v:v[0]-v[1]
r0=-D(B)/D(dR);rs=-D(dZ)/D(dR)
assert r0==F(420842109150005409,14779520000000000) and rs==-F(640000,23093)
zlo=(1-r0)/rs
assert zlo==F(406062589150005409,409600000000000000) and 0<zlo<1
assert 0<r0+rs<1 and r0+rs*zlo==1
vec=lambda z:tuple(B[i]+(r0+rs*z)*dR[i]+z*dZ[i] for i in range(4))
a=vec(F(1));b=vec(zlo)
alpha172=F(220608887064170557255,632523287505640882176)
V172=F(1047792388565411809841,90360469643662983168)
alpha173=F(611493515114730101,1752976676930715648)
V173=F(1267557322258081771,109561042308169728)
width=F(750324145848852691,13493830133453672153088)
assert a[0]==a[1]==alpha172 and a[2]==V172
assert b[0]==b[1]==alpha173 and b[2]==V173
assert b[0]-a[0]==width>0 and b[2]<a[2]
assert a[2]-a[3]>0 and b[2]-b[3]>0
assert all(v[2]+K*v[1]+L*v[0]==H for v in (a,b))
assert b[2]-a[2]==-(K+L)*width
print("STAGE173_AUTHOR_EXACT_FULL_REAL_PASS")
print("width",fmt(width),"alpha173",fmt(alpha173),"V173",fmt(V173))
print("r(z)=",fmt(r0),"+",fmt(rs),"*z ; z_min=",fmt(zlo))
print("ties",ties,"positive_gaps",len(gaps),"nodes",nodes)
