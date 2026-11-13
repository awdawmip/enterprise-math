"""Standalone rational Bellman/ordered-integer-DFS reproduction of external N14 Stage216."""
from fractions import Fraction as F
from functools import cache
from itertools import product
N=14;PN=(3,1,20);QN=(2,2,20)
P=tuple(F(x,24) for x in PN);Q=tuple(F(x,24) for x in QN)
K=F(908057789003279736,9275758227422879)
H=F(10060422269700525971327026167740407,127032717449378935977323595300864)
W=(1,0,1);Z=(14,0,0);S=(0,0,0)
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def nxt(s,j):return s[0]+1,s[1]+int(j==0),s[2]+int(j==1)
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
@cache
def val(s):
    av={'P':K*ratio(s),'Q':K}
    if s[0]<N:av['C']=1+sum(P[j]*val(nxt(s,j))[0] for j in range(3))
    best=min(av.values())
    return best,tuple(k for k,v in av.items() if v==best),tuple(v-best for v in av.values() if v>best)
assert val(S)[0]==H and len(states)==680
assert {s:val(s)[1] for s in states if len(val(s)[1])>1}=={W:('Q','C'),Z:('P','Q')}
gaps=[g for s in states for g in val(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(3387232024158932057,432769775858641842624)
def decide(s,u,z):
    if s==W:return 'Q' if u else 'C'
    if s==Z:return 'P' if z else 'Q'
    return val(s)[1][0]
@cache
def suffix(s,u,z):
    a=decide(s,u,z)
    if a=='P':return F(0),F(1),F(0),F(0)
    if a=='Q':return F(1),F(0),F(0),F(0)
    children=[suffix(nxt(s,j),u,z) for j in range(3)]
    return tuple(F(i>=2)+sum((P if i%2==0 else Q)[j]*children[j][i] for j in range(3)) for i in range(4))
def ordered(u,z):
    nums=[0,0,0,0];nodes=0
    def go(s,pm,qm):
        nonlocal nodes
        nodes+=1
        a=decide(s,u,z)
        if a=='C':
            for j in range(3):go(nxt(s,j),pm*PN[j],qm*QN[j])
        else:
            factor=24**(N-s[0]);n=s[0]
            nums[0]+=int(a=='Q')*pm*factor
            nums[1]+=int(a=='P')*qm*factor
            nums[2]+=n*pm*factor
            nums[3]+=n*qm*factor
    go(S,1,1)
    return tuple(F(v,24**N) for v in nums),nodes
corners={};nodes=0
for u,z in product((0,1),repeat=2):
    v,n=ordered(u,z)
    assert v==suffix(S,u,z)
    corners[u,z]=v;nodes+=n
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
O=corners[0,0];dw=sub(corners[1,0],O);dz=sub(corners[0,1],O)
assert sub(sub(corners[1,1],corners[1,0]),dz)==(F(0),)*4
err=lambda t:t[0]-t[1]
z0=-err(O)/err(dz);zs=-err(dw)/err(dz)
assert z0==F(305483250299541629,819200000000000000)
assert zs==F(50430503829405343,1638400000000000000)
assert 0<z0<z0+zs<1

def balanced(u):return tuple(O[i]+u*dw[i]+(z0+zs*u)*dz[i] for i in range(4))
A=balanced(F(0));B=balanced(F(1))
assert A[0]==A[1] and B[0]==B[1]
assert (A[0],A[2])==(F(3747711513430661245,10517860061584293888),F(2066603386919928833,219122084616339456))
assert (B[0],B[2])==(F(7504698785088745369,21035720123168587776),F(4095371032631387677,438244169232678912))
assert B[0]-A[0]==F(9275758227422879,21035720123168587776)
assert A[2]>A[3] and B[2]>B[3]
assert A[2]+2*K*A[0]==B[2]+2*K*B[0]==H
assert nodes==86830
print('STAGE216_REFERENCE_EXACT_PASS',nodes,'width',B[0]-A[0],'slope',2*K)
