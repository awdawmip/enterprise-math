"""Exact N14 ternary-IID external auxiliary model, Stage205 author verifier.
Finite rational Bellman enumeration and separate full ordered-history DFS. This
is NOT a native P000/X6 Result, Source CLAIM, or mathematical admission.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from json import dump
N=14
P=(F(3,24),F(1,24),F(20,24))
Q=(F(2,24),F(2,24),F(20,24))
K=F(16200,137)
H=F(175689269891985199711,1876232849527406592)
T=(12,3,1); Z=(14,0,0); S=(0,0,0)
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
@lru_cache(None)
def bell(s):
    c={'P':K*lr(s),'Q':K}
    if s[0]<N:c['C']=1+sum(P[i]*bell(child(s,i))[0] for i in range(3))
    v=min(c.values());return v,tuple(a for a in c if c[a]==v),tuple(val-v for val in c.values() if val>v)
assert len(states)==680
assert bell(S)[0]==H
assert {s:bell(s)[1] for s in states if len(bell(s)[1])>1}=={T:('P','C'),Z:('P','Q')}
gaps=[d for s in states for d in bell(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(69107093,19635830784)
def action(s,u,z):
    if s==T:return 'P' if u else 'C'
    if s==Z:return 'P' if z else 'Q'
    return bell(s)[1][0]
@lru_cache(None)
def dp(s,u,z):
    a=action(s,u,z)
    if a=='P':return F(0),F(1),F(0),F(0)
    if a=='Q':return F(1),F(0),F(0),F(0)
    cs=[dp(child(s,i),u,z) for i in range(3)]
    return tuple(F(j>=2)+sum((P if j%2==0 else Q)[i]*cs[i][j] for i in range(3)) for j in range(4))
def dfs(u,z):
    sums=[0,0,0,0];nodes=0;joint=0;reached_t=0;reached_z=0
    def visit(s,p,q,seen_t=False):
        nonlocal nodes,joint,reached_t,reached_z
        nodes+=1
        if s==T:seen_t=True;reached_t+=1
        if s==Z:reached_z+=1;joint+=int(seen_t)
        a=action(s,u,z)
        if a=='C':
            for i in range(3):visit(child(s,i),p*(3,1,20)[i],q*(2,2,20)[i],seen_t)
        else:
            m=24**(N-s[0]); n=s[0]
            sums[0]+=int(a=='Q')*p*m
            sums[1]+=int(a=='P')*q*m
            sums[2]+=n*p*m
            sums[3]+=n*q*m
    visit(S,1,1)
    return tuple(F(x,24**N) for x in sums),nodes,joint,reached_t,reached_z
cs={};total=0;stats={}
for u,z in product((0,1),repeat=2):
    d=dp(S,u,z)
    h,n,j,ct,cz=dfs(u,z)
    assert d==h,(u,z,d,h)
    assert j==0,(u,z,j)
    cs[(u,z)]=d;total+=n
    stats[str((u,z))]={'nodes':n,'t_histories':ct,'z_histories':cz,'joint':j}
O=cs[0,0]
DT=tuple(cs[1,0][j]-O[j] for j in range(4))
DZ=tuple(cs[0,1][j]-O[j] for j in range(4))
M=tuple(cs[1,1][j]-cs[1,0][j]-cs[0,1][j]+O[j] for j in range(4))
assert M==(F(0),)*4
err=lambda a:a[0]-a[1]
assert err(DZ)!=0
z0=-err(O)/err(DZ)
zs=-err(DT)/err(DZ)
def balance(u):
    z=z0+zs*u
    return tuple(O[j]+DT[j]*u+DZ[j]*z for j in range(4))
A=balance(F(0));B=balance(F(1))
width=B[0]-A[0]
print('k=',K,'H=',H)
print('corners',cs)
print('delta_T',DT,'delta_Z',DZ,'mixed',M)
print('z(u)=',z0,'+',zs,'u')
print('balanced0=',A,'balanced1=',B,'width=',width)
print('time gaps tP-tQ at endpoints=',A[2]-A[3],B[2]-B[3])
print('total_nodes=',total,'stats=',stats)
print('all_coin_feasible=',0<=z0<=1,0<=z0+zs<=1)
print('tP_dominance=',A[2]>=A[3],B[2]>=B[3])
print('Lagrangian0,1',A[2]+K*(A[0]+A[1]),B[2]+K*(B[0]+B[1]))
print('alpha204=',F(1237582032550008115,3505953353861431296),'V204=',F(2225727754437932573,219122084616339456))
assert 0<=z0<=1 and 0<=z0+zs<=1
assert A[0]==A[1] and B[0]==B[1]
assert A[2]>A[3] and B[2]>B[3]
assert width==F(5083984375,71328803586048)
assert A[0]==F(1237582032550008115,3505953353861431296)
assert A[2]==F(2225727754437932573,219122084616339456)
assert B[0]==F(1237831920550008115,3505953353861431296)
assert B[2]==F(2222034154437932573,219122084616339456)
assert A[2]+K*(A[0]+A[1])==B[2]+K*(B[0]+B[1])==H
assert total==329164
print('STAGE205_AUTHOR_EXACT_FULL_REAL_PASS',total)
