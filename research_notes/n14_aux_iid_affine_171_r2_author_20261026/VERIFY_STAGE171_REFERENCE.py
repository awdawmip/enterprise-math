#!/usr/bin/env python3
"""Stage171 exact author checker for the frozen external N14 ternary IID model.
All arithmetic is Fraction-exact. No native P000 claim, Session, or Driver review.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K,L=F(378837,1529),F(1128472,4587)
R,U=(10,0,1),(12,4,3)
A=('P','Q','C')
def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))
@lru_cache(None)
def bell(s):
    opts=[K*ratio(s),L]
    if s[0]<N:
        opts.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
    m=min(opts)
    return m,tuple(a for a,v in zip(A,opts) if v==m),opts
ties,gaps={},[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b);v,w,opts=bell(s)
            if len(w)>1:ties[s]=w
            gaps.extend(x-v for x in opts if x>v)
assert ties=={R:('Q','C'),U:('Q','C')},ties
assert len(gaps)==1238 and min(gaps)==F(3442966771823,94671649898496)
H=bell((0,0,0))[0]
assert H==F(332293501648867121767,1807757198084800512)
def action(s,r,u):
    if s==R:return 'Q' if r else 'C'
    if s==U:return 'Q' if u else 'C'
    return bell(s)[1][0]
def suffix(r,u):
    @lru_cache(None)
    def rec(s):
        ac=action(s,r,u)
        if ac=='P':return F(0),F(1),F(0),F(0)
        if ac=='Q':return F(1),F(0),F(0),F(0)
        assert s[0]<N
        x=[rec(child(s,i)) for i in range(3)]
        return (sum((P[i]*x[i][0] for i in range(3)),F(0)),
                sum((Q[i]*x[i][1] for i in range(3)),F(0)),
                1+sum((P[i]*x[i][2] for i in range(3)),F(0)),
                1+sum((Q[i]*x[i][3] for i in range(3)),F(0)))
    return rec((0,0,0))
def ordered_dfs(r,u):
    acc=defaultdict(int);hits={R:[0,F(0),F(0)],U:[0,F(0),F(0)]}
    nodes=0
    def rec(n,a,b,p,q):
        nonlocal nodes
        nodes+=1
        s=(n,a,b)
        if s in hits:
            h=hits[s];h[0]+=1
            h[1]+=F(p,24**n);h[2]+=F(q,12**n)
        ac=action(s,r,u)
        if ac=='C':
            assert n<N
            for i,(pi,qi) in enumerate(((3,1),(1,1),(20,10))):
                rec(n+1,a+(i==0),b+(i==1),p*pi,q*qi)
        else:
            acc[n,'ap']+=p;acc[n,'aq']+=q
            acc[n,'tp']+=n*p;acc[n,'tq']+=n*q
            if ac=='P':acc[n,'eq']+=q
            else:acc[n,'ep']+=p
    rec(0,0,0,1,1)
    mass=lambda key,den:sum((F(acc[n,key],den**n) for n in range(N+1)),F(0))
    assert mass('ap',24)==mass('aq',12)==1
    return (mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes
corners={};first=None;node_counts={}
for r in(0,1):
    for u in(0,1):
        v=suffix(r,u);w,h,n=ordered_dfs(r,u)
        assert v==w,(r,u,v,w)
        corners[r,u]=v;node_counts[r,u]=n
        if first is None:first=h
        else:assert first==h
assert first[R][0]==10 and first[U][0]==5170
assert first[R][1]==F(9765625,120932352)
assert first[R][2]==F(9765625,60466176)
assert first[U][1]==F(8078125,220150628352)
assert first[U][2]==F(8078125,139314069504)
assert sum(node_counts.values())==1222924,node_counts
sub=lambda v,w:tuple(x-y for x,y in zip(v,w))
base=corners[0,0]
dR=sub(corners[1,0],base)
dU=sub(corners[0,1],base)
assert sub(sub(corners[1,1],corners[1,0]),dU)==(F(0),)*4
D=lambda v:v[0]-v[1]
r0=-D(base)/D(dR)
rs=-D(dU)/D(dR)
assert r0==F(1284898704522779,1689088000000000)
assert rs==-F(641597,3694880000)
assert 0<=r0<=1 and 0<=r0+rs<=1
M=lambda u:tuple(base[i]+(r0+rs*u)*dR[i]+u*dU[i] for i in range(4))
v0,v1=M(F(0)),M(F(1))
a170=F(126062165849964145105,361441878574651932672)
V170=F(4191196473918241372757,361441878574651932672)
a171=F(882435274780741015735,2530093150022563528704)
V171=F(4191188444229937372757,361441878574651932672)
assert v0[0]==v0[1]==a170 and v0[2]==V170
assert v1[0]==v1[1]==a171 and v1[2]==V171
assert v0[2]-v0[3]==F(134198175358476229825,361441878574651932672)
assert v1[2]-v1[3]==F(939402695545477608775,2530093150022563528704)
assert all(v[2]>=v[3] and v[2]+K*v[1]+L*v[0]==H for v in (v0,v1))
assert a171-a170==F(12351453125,274532676868767744)>0
assert V171-V170==-(K+L)*(a171-a170)
print('STAGE171_AUTHOR_EXACT_FULL_REAL_PASS')
print('states=680 gaps=1238 tie-states=',ties)
print('ordered_DFS_nodes=',node_counts,'total=',sum(node_counts.values()))
print('balance_r0=',r0,'slope=',rs)
print('alpha171=',a171,'V171=',V171,'width=',a171-a170,'slope=',K+L)
