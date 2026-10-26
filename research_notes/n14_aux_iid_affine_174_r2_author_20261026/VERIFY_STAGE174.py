#!/usr/bin/env python3
"""Exact Stage174 external N14 ternary IID primal/dual author verifier.
Independent computational observers: Fraction suffix DP and unmerged
ordered-history DFS with integer branch masses. Not a native P000 theorem.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=L=F(16044588,70019)
T=(8,2,0);Z=(14,0,0)
A=('P','Q','C')
EXPECTED={T:('P','C'),Z:('P','Q')}
def fmt(x):return str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return(s[0]+1,s[1]+int(i==0),s[2]+int(i==1))

@lru_cache(None)
def bell(s):
    opts=[K*ell(s),L]
    if s[0]<N:opts.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
    m=min(opts)
    return m,tuple(a for a,v in zip(A,opts) if v==m),opts

strict={};ties={};gaps=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b);m,w,opts=bell(s)
            (ties if len(w)>1 else strict)[s]=w if len(w)>1 else w[0]
            gaps.extend(v-m for v in opts if v>m)
H=bell((0,0,0))[0]
assert len(strict)+len(ties)==680 and ties==EXPECTED
assert len(gaps)==1238
assert min(gaps)==F(39435024594685,1926840855822336)
assert H==F(2630296570966281555483145,15342709242751472369664)

def action(s,t,z):
    if s==T:return 'P' if t else 'C'
    if s==Z:return 'Q' if z else 'P'
    return strict[s]

def suffix(t,z):
    @lru_cache(None)
    def rec(s):
        ac=action(s,t,z)
        if ac=='P':return(F(0),F(1),F(0),F(0))
        if ac=='Q':return(F(1),F(0),F(0),F(0))
        v=[rec(child(s,i)) for i in range(3)]
        return(sum((P[i]*v[i][0] for i in range(3)),F(0)),
               sum((Q[i]*v[i][1] for i in range(3)),F(0)),
               1+sum((P[i]*v[i][2] for i in range(3)),F(0)),
               1+sum((Q[i]*v[i][3] for i in range(3)),F(0)))
    return rec((0,0,0))

def ordered_dfs(t,z):
    pn=(3,1,20);qn=(1,1,10)
    acc=defaultdict(int)
    hits={T:[0,F(0),F(0)],Z:[0,F(0),F(0)]}
    nodes=0
    def walk(n,a,b,p,q):
        nonlocal nodes
        nodes+=1;s=(n,a,b)
        if s in hits:
            h=hits[s];h[0]+=1;h[1]+=F(p,24**n);h[2]+=F(q,12**n)
        ac=action(s,t,z)
        if ac=='C':
            assert n<N
            for i in range(3):walk(n+1,a+(i==0),b+(i==1),p*pn[i],q*qn[i])
        else:
            acc[n,'ap']+=p;acc[n,'aq']+=q;acc[n,'tp']+=n*p;acc[n,'tq']+=n*q
            if ac=='P':acc[n,'eq']+=q
            else:acc[n,'ep']+=p
    walk(0,0,0,1,1)
    mass=lambda tag,den:sum((F(acc[n,tag],den**n) for n in range(N+1)),F(0))
    assert mass('ap',24)==mass('aq',12)==1
    return(mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes

corners={};nodecounts={};hits0=None
for t in (0,1):
    for z in (0,1):
        a=suffix(t,z);b,h,n=ordered_dfs(t,z)
        assert a==b,(t,z,a,b)
        corners[t,z]=a;nodecounts[f'{t}{z}']=n
        if hits0 is None:hits0=h
        else:assert hits0==h
assert hits0[T][0]==28 and hits0[Z][0]==1
assert T[1]==2 and Z[1]==Z[2]==0
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0]
dT=sub(corners[1,0],base)
dZ=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),dZ)
assert mixed==(F(0),)*4
D=lambda v:v[0]-v[1]
D0,Dt,Dz=map(D,(base,dT,dZ))
z0=-D0/Dz;zs=-Dt/Dz
z=lambda t:z0+zs*t
vec=lambda t:tuple(base[i]+t*dT[i]+z(t)*dZ[i] for i in range(4))
assert z0==F(406062589150005409,409600000000000000)
assert zs==F(1884827,100000000)
t0=F(0);t1=F(3537410849994591,7720251392000000)
assert z(t1)==1 and z(t0)>0 and t1<1
left,right=vec(t0),vec(t1)
alpha173=F(611493515114730101,1752976676930715648)
V173=F(1267557322258081771,109561042308169728)
alpha174=F(10295869835213079092569,29500515812940089131008)
V174=F(677877812657492293580503,59001031625880178262016)
width=F(27520663367307918581,157336084335680475365376)
checks={
 'stage173_endpoint':left[0]==left[1]==alpha173 and left[2]==V173,
 'stage174_endpoint':right[0]==right[1]==alpha174 and right[2]==V174,
 'strict_width':right[0]-left[0]==width and width>0,
 'balanced_both':left[0]==left[1] and right[0]==right[1],
 'timeP_dominates':left[2]>=left[3] and right[2]>=right[3],
 'dual_tight':all(v[2]+K*v[1]+L*v[0]==H for v in (left,right)),
 'alpha_grows':right[0]>left[0],
 'time_falls':right[2]<left[2],
 'slope':right[2]-left[2]==-(K+L)*width,
 'legal_coins':0<z0<1 and 0<t1<1,
 'disjoint_first_hits':mixed==(F(0),)*4,
}
for k,v in checks.items():print('CHECK',k,v)
print('TIES',ties,'POSITIVE_GAPS',len(gaps),'H',fmt(H))
print('HITS',{str(k):list(map(fmt,v)) for k,v in hits0.items()})
print('NODES',nodecounts,'TOTAL',sum(nodecounts.values()))
print('BALANCE',fmt(z0),fmt(zs),'LEGAL_T',[fmt(t0),fmt(t1)])
print('LEFT',[fmt(v) for v in left],'RIGHT',[fmt(v) for v in right])
print('WIDTH',fmt(width),'SLOPE',fmt(K+L))
assert all(checks.values())
print('STAGE174_AUTHOR_EXACT_FULL_REAL_PASS')
