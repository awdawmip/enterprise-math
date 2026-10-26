#!/usr/bin/env python3
"""Self-contained exact Stage175 corrected off-diagonal reference checker.
Author's independently executed original and full logs are separate artifacts.
Uses exact Fractions; all three symbols have positive mass. No native claim.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(41521222013193063,181934251842254)
L=F(20701458469704504,90967125921127)
T=(8,2,0)
B=(6,3,3)
A=('P','Q','C')

def next_state(s,i):
    return (s[0]+1,s[1]+int(i==0),s[2]+int(i==1))

def ell(s):
    return F(2)**(s[1]+s[2])/F(3)**s[1]

@lru_cache(None)
def bell(s):
    options=[K*ell(s),L]
    if s[0]<N:
        options.append(1+sum((P[i]*bell(next_state(s,i))[0] for i in range(3)),F(0)))
    m=min(options)
    return m,tuple(a for a,v in zip(A,options) if v==m),options

strict={}
ties={}
gaps=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b)
            v,w,options=bell(s)
            (ties if len(w)>1 else strict)[s]=w if len(w)>1 else w[0]
            gaps.extend(x-v for x in options if x>v)
assert len(strict)+len(ties)==680
assert ties=={B:('Q','C'),T:('P','C')}
assert len(gaps)==1238
assert min(gaps)==F(152464420746873000396113,3337744988485269306998784)
H=bell((0,0,0))[0]
assert H==F(53122292194902540973485450586445,311451660365537449574670532608)

def act(s,t,b):
    if s==T:
        return 'P' if t else 'C'
    if s==B:
        return 'Q' if b else 'C'
    return strict[s]

def suffix(t,b):
    @lru_cache(None)
    def rec(s):
        a=act(s,t,b)
        if a=='P':return F(0),F(1),F(0),F(0)
        if a=='Q':return F(1),F(0),F(0),F(0)
        children=[rec(next_state(s,i)) for i in range(3)]
        return (
            sum((P[i]*children[i][0] for i in range(3)),F(0)),
            sum((Q[i]*children[i][1] for i in range(3)),F(0)),
            1+sum((P[i]*children[i][2] for i in range(3)),F(0)),
            1+sum((Q[i]*children[i][3] for i in range(3)),F(0)),
        )
    return rec((0,0,0))

def ordered_dfs(t,b):
    mass=defaultdict(int)
    first={T:[0,F(0),F(0)],B:[0,F(0),F(0)]}
    pn=(3,1,20)
    qn=(1,1,10)
    nodes=0
    def walk(n,a,c,p,q):
        nonlocal nodes
        nodes+=1
        s=(n,a,c)
        if s in first:
            v=first[s]
            v[0]+=1
            v[1]+=F(p,24**n)
            v[2]+=F(q,12**n)
        decision=act(s,t,b)
        if decision=='C':
            assert n<N
            for i in range(3):
                walk(n+1,a+int(i==0),c+int(i==1),p*pn[i],q*qn[i])
        else:
            mass[n,'ap']+=p
            mass[n,'aq']+=q
            mass[n,'tp']+=n*p
            mass[n,'tq']+=n*q
            if decision=='Q':mass[n,'ep']+=p
            else:mass[n,'eq']+=q
    walk(0,0,0,1,1)
    total=lambda label,den:sum((F(mass[n,label],den**n) for n in range(N+1)),F(0))
    assert total('ap',24)==total('aq',12)==1
    return (total('ep',24),total('eq',12),total('tp',24),total('tq',12)),first,nodes

corners={}
nodecounts=[]
first_hit=None
for t in (0,1):
    for b in (0,1):
        obs,first,nodes=ordered_dfs(t,b)
        assert obs==suffix(t,b)
        corners[t,b]=obs
        nodecounts.append(nodes)
        if first_hit is None:first_hit=first
        else:assert first_hit==first
assert nodecounts==[285916,282916,282052,279052]
assert first_hit[T]==[28,F(109375,746496),F(109375,1679616)]
assert first_hit[B]==[8,F(1,884736),F(1,373248)]
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
M00=corners[0,0]
dT=sub(corners[1,0],M00)
dB=sub(corners[0,1],M00)
assert sub(sub(corners[1,1],corners[1,0]),dB)==(F(0),)*4
D=lambda v:v[0]-v[1]
t0=-D(M00)/D(dT)
ts=-D(dB)/D(dT)
assert t0==F(3537410849994591,7720251392000000)
assert ts==F(102742439843,7720251392000000)
obs=lambda b:tuple(M00[i]+(t0+ts*b)*dT[i]+b*dB[i] for i in range(4))
left,right=obs(F(0)),obs(F(1))
assert 0<=t0<t0+ts<=1
assert left[0]==left[1]==F(10295869835213079092569,29500515812940089131008)
assert right[0]==right[1]==F(5147935054057228427975,14750257906470044565504)
assert left[2]==F(677877812657492293580503,59001031625880178262016)
assert right[2]==F(338938781942537717887145,29500515812940089131008)
assert left[2]>=left[3] and right[2]>=right[3]
assert all(m[2]+K*m[1]+L*m[0]==H for m in (left,right))
width=right[0]-left[0]
assert width==F(90967125921127,9833505270980029710336)>0
assert right[2]-left[2]==-(K+L)*width
print('STAGE175_CORRECTED_FULL_REAL_REFERENCE_PASS')
