#!/usr/bin/env python3
"""Readable exact Stage184 verifier; external N14 IID, rational DP + unmerged DFS.
Companion executed original and its logs are in EM_STAGE184_AUTHOR_EXACT_PORTABLE_20261027.zip.
No floating arithmetic; positive P and Q branch measures are never canceled.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict

N=14
P=(F(1,8), F(1,24), F(5,6))
Q=(F(1,12), F(1,12), F(5,6))
K=F(321331011187179,1679273916694)
L=F(480139895871848,2518910875041)
S=(9,0,1); T=(6,2,0)
A=('P','Q','C')
def ell(x): return F(2)**(x[1]+x[2])/F(3)**x[1]
def child(x,i): return x[0]+1,x[1]+int(i==0),x[2]+int(i==1)

@lru_cache(None)
def bell(x):
    cost=[K*ell(x),L]
    if x[0]<N:
        cost.append(1+sum((P[i]*bell(child(x,i))[0] for i in range(3)),F(0)))
    m=min(cost)
    return m,tuple(a for a,c in zip(A,cost) if c==m),tuple(cost)

gaps=[];ties={};strict={}
for n in range(15):
    for a in range(n+1):
        for b in range(n-a+1):
            x=(n,a,b);v,actions,values=bell(x)
            if len(actions)>1:ties[x]=actions
            else:strict[x]=actions[0]
            gaps.extend(w-v for w in values if w>v)
assert len(ties)+len(strict)==680
assert ties=={S:('Q','C'),T:('P','C')}
assert len(gaps)==1238
assert min(gaps)==F(7747768995607,181361583002952)
H=bell((0,0,0))[0]
assert H==F(1816035087448322622333240298837,12544295497767083269983043584)
def chosen(x,s,t):
    if x==S:return 'Q' if s else 'C'
    if x==T:return 'P' if t else 'C'
    return strict[x]
def dp(s,t):
    @lru_cache(None)
    def rec(x):
        act=chosen(x,s,t)
        if act=='P':return F(0),F(1),F(0),F(0)
        if act=='Q':return F(1),F(0),F(0),F(0)
        z=[rec(child(x,i)) for i in range(3)]
        return (sum((P[i]*z[i][0] for i in range(3)),F(0)),
                sum((Q[i]*z[i][1] for i in range(3)),F(0)),
                1+sum((P[i]*z[i][2] for i in range(3)),F(0)),
                1+sum((Q[i]*z[i][3] for i in range(3)),F(0)))
    return rec((0,0,0))
def dfs(s,t):
    # Exact positive weights: P symbols (3,1,20)/24; Q symbols (1,1,10)/12.
    count=defaultdict(int);hits={S:[0,F(0),F(0)],T:[0,F(0),F(0)]}
    nodes=0
    def walk(n,a,b,p,q):
        nonlocal nodes
        nodes+=1;st=(n,a,b)
        if st in hits:
            h=hits[st];h[0]+=1;h[1]+=F(p,24**n);h[2]+=F(q,12**n)
        act=chosen(st,s,t)
        if act=='C':
            assert n<14
            for i,(pn,qn) in enumerate(zip((3,1,20),(1,1,10))):
                walk(n+1,a+int(i==0),b+int(i==1),p*pn,q*qn)
        else:
            for tag,val in (('ap',p),('aq',q),('tp',n*p),('tq',n*q)):
                count[n,tag]+=val
            count[n,'eq' if act=='P' else 'ep']+=q if act=='P' else p
    walk(0,0,0,1,1)
    mass=lambda name,den:sum((F(count[n,name],den**n) for n in range(N+1)),F(0))
    assert mass('ap',24)==mass('aq',12)==1
    return (mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes

corners={};dfs_nodes={};first=None
for s in (0,1):
    for t in (0,1):
        v,h,n=dfs(s,t)
        assert v==dp(s,t),(s,t,v,dp(s,t))
        corners[s,t]=v;dfs_nodes[s,t]=n
        if first is None:first=h
        else:assert first==h
assert dfs_nodes=={(0,0):215152,(0,1):207682,(1,0):214720,(1,1):207250}
assert first[S]==[9,F(390625,4478976),F(390625,2239488)]
assert first[T]==[15,F(3125,27648),F(3125,62208)]

minus=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0];ds=minus(corners[1,0],base);dt=minus(corners[0,1],base)
assert minus(minus(corners[1,1],corners[1,0]),dt)==(F(0),)*4
D=lambda x:x[0]-x[1]
s0=-D(base)/D(ds); st=-D(dt)/D(ds)
assert s0==F(21925676597479349,37833811200000000)
assert st==F(12352512653,31528176000)
assert 0<=s0<=1 and 0<=s0+st<=1
vec=lambda t:tuple(base[i]+(s0+st*t)*ds[i]+t*dt[i] for i in range(4))
left=vec(F(0));right=vec(F(1))
assert left[0]==left[1]==F(6293786652175669191787,17990936586642819907584)
assert left[2]==F(50134108209086100977021,4497734146660704976896)
assert right[0]==right[1]==F(6302854731325816791787,17990936586642819907584)
assert right[2]==F(49268185437698746127021,4497734146660704976896)
assert left[2]-left[3]==F(166070625793116812795,562216768332588122112)
assert right[2]-right[3]==F(149857900062857106545,562216768332588122112)
assert right[0]>left[0] and right[2]<left[2]
assert right[0]-left[0]==F(2623865494834375,5205710817894334464)
assert K+L==F(1924272825305233,5037821750082)
assert all(v[2]+K*v[1]+L*v[0]==H for v in (left,right))
assert right[2]-left[2]==-(K+L)*(right[0]-left[0])
print('STAGE184_AUTHOR_EXACT_FULL_REAL_PASS')
