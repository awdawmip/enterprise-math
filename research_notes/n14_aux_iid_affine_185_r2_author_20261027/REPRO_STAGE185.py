"""Independent exact reproduction of the Stage185 external N14 full-history certificate.
The only state quotient is the sufficient IID count statistic; the DFS stays ordered.
"""
from fractions import Fraction as F
from functools import lru_cache
N=14; P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=L=F(11700648,62533); S=(9,0,1); Z=(14,0,0)
A=('P','Q','C')
def nxt(x,i):return (x[0]+1,x[1]+(i==0),x[2]+(i==1))
def ell(x):return F(2)**(x[1]+x[2])/F(3)**x[1]
@lru_cache(None)
def bell(x):
    v=[K*ell(x),L]
    if x[0]<N:v.append(1+sum(P[i]*bell(nxt(x,i))[0] for i in range(3)))
    m=min(v);return m,tuple(a for a,t in zip(A,v) if t==m),v
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
ties={x:bell(x)[1] for x in states if len(bell(x)[1])>1}
gaps=[z-bell(x)[0] for x in states for z in bell(x)[2] if z>bell(x)[0]]
assert len(states)==680 and ties=={S:('Q','C'),Z:('P','Q')}
assert len(gaps)==1238 and min(gaps)==F(3713241817841,107552181583872)
H=F(60828835377977479173913,428198791166048600064)
assert bell((0,0,0))[0]==H
def action(x,s,z):
    if x==S:return 'Q' if s else 'C'
    if x==Z:return 'P' if z else 'Q'
    return bell(x)[1][0]
def dp(s,z):
    @lru_cache(None)
    def f(x):
        a=action(x,s,z)
        if a=='P':return (F(0),F(1),F(0),F(0))
        if a=='Q':return (F(1),F(0),F(0),F(0))
        y=[f(nxt(x,i)) for i in range(3)]
        return (sum(P[i]*y[i][0] for i in range(3)),sum(Q[i]*y[i][1] for i in range(3)),1+sum(P[i]*y[i][2] for i in range(3)),1+sum(Q[i]*y[i][3] for i in range(3)))
    return f((0,0,0))
def ordered(s,z):
    sums=[F(0)]*4;mass=[F(0)]*2;hits={S:[0,F(0),F(0)],Z:[0,F(0),F(0)]};nodes=0
    def walk(x,p,q):
        nonlocal nodes
        nodes+=1;n=x[0]
        if x in hits:
            hits[x][0]+=1;hits[x][1]+=p;hits[x][2]+=q
        act=action(x,s,z)
        if act=='C':
            for i in range(3):walk(nxt(x,i),p*P[i],q*Q[i])
        else:
            mass[0]+=p;mass[1]+=q
            sums[2]+=n*p;sums[3]+=n*q
            if act=='Q':sums[0]+=p
            else:sums[1]+=q
    walk((0,0,0),F(1),F(1));assert mass==[1,1]
    return tuple(sums),hits,nodes
corners={};nodes={};hits=None
for s in (0,1):
 for z in (0,1):
    v=dp(s,z);w,h,n=ordered(s,z)
    assert v==w,(s,z,v,w)
    corners[s,z]=v;nodes[s,z]=n
    if hits is None:hits=h
    else:assert hits==h
assert hits[S][0]==9 and hits[Z][0]==1
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0];dS=sub(corners[1,0],base);dZ=sub(corners[0,1],base)
assert sub(sub(corners[1,1],corners[1,0]),dZ)==(F(0),)*4
diff=lambda a:a[0]-a[1]
s0=-diff(base)/diff(dS);sz=-diff(dZ)/diff(dS)
zmax=(1-s0)/sz
assert s0==F(36748691781079349,37833811200000000)
assert sz==F(128000000,5911533)
assert zmax==F(1085119418920651,819200000000000000)
assert 0<s0<1 and 0<zmax<1
v=lambda z:tuple(base[i]+(s0+sz*z)*dS[i]+z*dZ[i] for i in range(4))
a,b=v(0),v(zmax)
assert a[0]==a[1]==F(6302854731325816791787,17990936586642819907584)
assert a[2]==F(49268185437698746127021,4497734146660704976896)
assert b[0]==b[1]==F(3684877789469437643,10517860061584293888)
assert b[2]==F(2399458174541646935,219122084616339456)
assert b[0]-a[0]==F(67855772623365068983,6908519649270842844512256)
assert all(v[2]>=v[3] for v in (a,b))
assert all(v[2]+K*v[1]+L*v[0]==H for v in (a,b))
assert b[0]>a[0] and b[2]<a[2]
assert b[2]-a[2]==-(K+L)*(b[0]-a[0])
assert sum(nodes.values())==829864
print('PASS STAGE185', 'ordered_nodes',sum(nodes.values()),'hits',hits,
      's0',s0,'sz',sz,'zmax',zmax,'alpha185',b[0],'V185',b[2],
      'width',b[0]-a[0],'slope',K+L)
