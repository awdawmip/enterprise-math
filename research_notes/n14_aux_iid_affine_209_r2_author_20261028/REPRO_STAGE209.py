"""External ternary IID N=14 Stage209 exact Bellman and unmerged ordered-history integer DFS."""
from fractions import Fraction as F
from functools import cache
from itertools import product
N=14;PN=(3,1,20);QN=(2,2,20)
P=tuple(F(x,24) for x in PN);Q=tuple(F(x,24) for x in QN)
K=F(134136,1231);H=F(366957863356152849587,4214676346292404224)
T=(10,4,3);Z=(14,0,0);S=(0,0,0)
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def nxt(s,j):return s[0]+1,s[1]+(j==0),s[2]+(j==1)
def rho(s):return F(2**(s[1]+s[2]),3**s[1])
@cache
def bell(s):
    ac={'P':K*rho(s),'Q':K}
    if s[0]<N:ac['C']=1+sum(P[j]*bell(nxt(s,j))[0] for j in range(3))
    best=min(ac.values());return best,tuple(a for a,x in ac.items() if x==best),tuple(x-best for x in ac.values() if x>best)
assert len(states)==680 and bell(S)[0]==H
assert {s:bell(s)[1] for s in states if len(bell(s)[1])>1}=={T:('Q','C'),Z:('P','Q')}
gaps=[g for s in states for g in bell(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(1547,177264)
def action(s,u,z):
    if s==T:return 'Q' if u else 'C'
    if s==Z:return 'P' if z else 'Q'
    return bell(s)[1][0]
@cache
def suffix(s,u,z):
    a=action(s,u,z)
    if a=='P':return F(0),F(1),F(0),F(0)
    if a=='Q':return F(1),F(0),F(0),F(0)
    cs=[suffix(nxt(s,j),u,z) for j in range(3)]
    return tuple(F(k>=2)+sum((P if k%2==0 else Q)[j]*cs[j][k] for j in range(3)) for k in range(4))
def ordered(u,z):
    mass=[0]*4;nodes=0
    def go(s,pm,qm):
        nonlocal nodes
        nodes+=1
        a=action(s,u,z)
        if a=='C':
            for j in range(3):go(nxt(s,j),pm*PN[j],qm*QN[j])
        else:
            v=24**(N-s[0]);n=s[0]
            mass[0]+=(a=='Q')*pm*v;mass[1]+=(a=='P')*qm*v
            mass[2]+=n*pm*v;mass[3]+=n*qm*v
    go(S,1,1)
    return tuple(F(x,24**N) for x in mass),nodes
corners={};nodes=0
for u,z in product((0,1),repeat=2):
    v,n=ordered(u,z);assert v==suffix(S,u,z)
    corners[u,z]=v;nodes+=n
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
O=corners[0,0];DT=sub(corners[1,0],O);DZ=sub(corners[0,1],O)
assert sub(sub(corners[1,1],corners[1,0]),DZ)==(F(0),)*4
err=lambda w:w[0]-w[1]
z0=-err(O)/err(DZ);zs=-err(DT)/err(DZ)
assert z0==F(215703723671345049,819200000000000000)
assert zs==F(6249221,3200000000000) and 0<z0<z0+zs<1
def balanced(u):return tuple(O[i]+u*DT[i]+(z0+zs*u)*DZ[i] for i in range(4))
A=balanced(F(0));B=balanced(F(1))
assert A[0]==A[1] and B[0]==B[1]
assert (A[0],A[2])==(F(1243660577111416115,3505953353861431296),F(2138786643677228573,219122084616339456))
assert (B[0],B[2])==(F(3730982047415656345,10517860061584293888),F(2138785208600876573,219122084616339456))
assert A[2]>A[3] and B[2]>B[3]
assert A[2]+2*K*A[0]==B[2]+2*K*B[0]==H
assert B[0]-A[0]==F(154336625,5135673858195456)
assert nodes==245752
print('STAGE209_REFERENCE_EXACT_PASS',nodes,'width',B[0]-A[0],'slope',2*K)
