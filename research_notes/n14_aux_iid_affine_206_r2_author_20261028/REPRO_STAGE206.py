"""Standalone Stage206 N14 external ternary-IID exact rational reproducer.
Reuses the Stage205 rational Bellman/ordered-positive-mass method; no X6 claim.
"""
from fractions import Fraction as F
from functools import cache
from itertools import product
N=14; P=(F(3,24),F(1,24),F(20,24)); Q=(F(2,24),F(2,24),F(20,24))
K=F(25155568056,213144883); H=F(1091477712445072832515830191,11676187772066443309350912)
W=(5,0,1); Z=(14,0,0); S=(0,0,0)
ss=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
def ch(s,j):return s[0]+1,s[1]+(j==0),s[2]+(j==1)
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
@cache
def bell(s):
    d={'P':K*lr(s),'Q':K}
    if s[0]<N:d['C']=1+sum(P[j]*bell(ch(s,j))[0] for j in range(3))
    m=min(d.values());return m,tuple(a for a in d if d[a]==m),tuple(v-m for v in d.values() if v>m)
assert len(ss)==680 and bell(S)[0]==H
assert {s:bell(s)[1] for s in ss if len(bell(s)[1])>1}=={W:('Q','C'),Z:('P','Q')}
gaps=[d for s in ss for d in bell(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(69107093,34529471046)
def act(s,u,z):
    if s==W:return 'Q' if u else 'C'
    if s==Z:return 'P' if z else 'Q'
    return bell(s)[1][0]
@cache
def dp(s,u,z):
    a=act(s,u,z)
    if a=='P':return F(0),F(1),F(0),F(0)
    if a=='Q':return F(1),F(0),F(0),F(0)
    cs=[dp(ch(s,j),u,z) for j in range(3)]
    return tuple(F(i>=2)+sum((P if i%2==0 else Q)[j]*cs[j][i] for j in range(3)) for i in range(4))
def ordered(u,z):
    totals=[0]*4;node=[0]
    def walk(s,p,q):
        node[0]+=1;a=act(s,u,z)
        if a=='C':
            for j in range(3):walk(ch(s,j),p*(3,1,20)[j],q*(2,2,20)[j])
        else:
            m=24**(N-s[0]); n=s[0]
            totals[0]+=int(a=='Q')*p*m;totals[1]+=int(a=='P')*q*m
            totals[2]+=n*p*m;totals[3]+=n*q*m
    walk(S,1,1)
    return tuple(F(t,24**N) for t in totals),node[0]
cs={};nodes=0
for u,z in product((0,1),repeat=2):
    v,n=ordered(u,z);assert v==dp(S,u,z);cs[u,z]=v;nodes+=n
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
O=cs[0,0];DT=sub(cs[1,0],O);DZ=sub(cs[0,1],O)
assert sub(sub(cs[1,1],cs[1,0]),DZ)==(F(0),)*4
err=lambda v:v[0]-v[1]
z0=-err(O)/err(DZ);zs=-err(DT)/err(DZ)
assert z0==F(106748677752881049,819200000000000000)
assert zs==F(894746757,12800000000)
assert 0<z0<z0+zs<1
v=lambda u:tuple(O[i]+u*DT[i]+(z0+zs*u)*DZ[i] for i in range(4))
a,b=v(F(0)),v(F(1));width=b[0]-a[0]
assert (a[0],a[2])==(F(1237831920550008115,3505953353861431296),F(2222034154437932573,219122084616339456))
assert (b[0],b[2])==(F(413520058350802705,1168651117953810432),F(2181785245548332573,219122084616339456))
assert width==F(666077759375,855945643032576) and a[0]==a[1] and b[0]==b[1]
assert a[2]>a[3] and b[2]>b[3]
assert a[2]+2*K*a[0]==b[2]+2*K*b[0]==H
assert nodes==313384
print('STAGE206_DERIVED_REFERENCE_EXACT_PASS',nodes,'width',width,'slope',2*K)
