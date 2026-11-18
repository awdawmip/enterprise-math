"""Standalone external IID N=14 Stage208 exact Bellman, suffix DP and full ordered integer-mass DFS."""
from fractions import Fraction as F
from functools import cache
from itertools import product
N=14;PN=(3,1,20);QN=(2,2,20)
P=tuple(F(x,24) for x in PN);Q=tuple(F(x,24) for x in QN)
K=F(19224,175);H=F(168140201472112396231,1917318240392970240)
T=(11,3,1);Z=(14,0,0);S=(0,0,0)
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def child(s,j):return s[0]+1,s[1]+(j==0),s[2]+(j==1)
def rho(s):return F(2**(s[1]+s[2]),3**s[1])
@cache
def bell(s):
    ac={'P':K*rho(s),'Q':K}
    if s[0]<N:ac['C']=1+sum(P[j]*bell(child(s,j))[0] for j in range(3))
    b=min(ac.values())
    return b,tuple(a for a,x in ac.items() if x==b),tuple(x-b for x in ac.values() if x>b)
assert len(states)==680 and bell(S)[0]==H
assert {s:bell(s)[1] for s in states if len(bell(s)[1])>1}=={T:('P','C'),Z:('P','Q')}
gaps=[g for s in states for g in bell(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(3757,340200)
def action(s,u,z):
    if s==T:return 'P' if u else 'C'
    if s==Z:return 'P' if z else 'Q'
    return bell(s)[1][0]
@cache
def suffix(s,u,z):
    a=action(s,u,z)
    if a=='P':return F(0),F(1),F(0),F(0)
    if a=='Q':return F(1),F(0),F(0),F(0)
    cs=[suffix(child(s,j),u,z) for j in range(3)]
    return tuple(F(k>=2)+sum((P if k%2==0 else Q)[j]*cs[j][k] for j in range(3)) for k in range(4))
def ordered(u,z):
    acc=[0]*4;nodes=0
    def go(s,pm,qm):
        nonlocal nodes
        nodes+=1
        a=action(s,u,z)
        if a=='C':
            for j in range(3):go(child(s,j),pm*PN[j],qm*QN[j])
        else:
            factor=24**(N-s[0]);n=s[0]
            acc[0]+=(a=='Q')*pm*factor
            acc[1]+=(a=='P')*qm*factor
            acc[2]+=n*pm*factor
            acc[3]+=n*qm*factor
    go(S,1,1)
    return tuple(F(v,24**N) for v in acc),nodes
corners={};nodes=0
for u,z in product((0,1),repeat=2):
    v,n=ordered(u,z);assert v==suffix(S,u,z)
    corners[u,z]=v;nodes+=n
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
O=corners[0,0];dt=sub(corners[1,0],O);dz=sub(corners[0,1],O)
assert sub(sub(corners[1,1],corners[1,0]),dz)==(F(0),)*4
err=lambda v:v[0]-v[1]
z0=-err(O)/err(dz);zs=-err(dt)/err(dz)
assert z0==F(220020301271345049,819200000000000000)
assert zs==-F(2697861,512000000) and 0<z0+zs<z0<1
def b(u):return tuple(O[i]+u*dt[i]+(z0+zs*u)*dz[i] for i in range(4))
A=b(F(0));B=b(F(1))
assert A[0]==A[1] and B[0]==B[1]
assert (A[0],A[2])==(F(1243470457111416115,3505953353861431296),F(2141397262877228573,219122084616339456))
assert (B[0],B[2])==(F(1243660577111416115,3505953353861431296),F(2138786643677228573,219122084616339456))
assert A[2]>A[3] and B[2]>B[3]
assert A[2]+2*K*A[0]==B[2]+2*K*B[0]==H
assert B[0]-A[0]==F(46416015625,855945643032576)
assert nodes==277216
print('STAGE208_REFERENCE_EXACT_PASS',nodes,'width',B[0]-A[0],'slope',2*K)
