"""Stage199 independent reproducible exact checker: external N14 IID only."""
from fractions import Fraction as F
from functools import cache
from itertools import product

P=(F(3,24),F(1,24),F(20,24))
Q=(F(2,24),F(2,24),F(20,24))
K=F(213288424,1523041); N=14
B=(7,0,1); Z=(14,0,0); root=(0,0,0)
def nxt(s,i):
    n,a,b=s
    return n+1,a+int(i==0),b+int(i==1)
@cache
def h(s):
    n,a,b=s
    costs={'P':K*F(2**(a+b),3**a),'Q':K}
    if n<N:
        costs['C']=1+sum(P[i]*h(nxt(s,i))[0] for i in range(3))
    m=min(costs.values())
    return m,tuple(c for c in ('P','Q','C') if c in costs and costs[c]==m),[v-m for v in costs.values() if v>m]
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(states)==680
assert h(root)[0]==F(13641932749948792109334011,125149469578557848027136)
assert {s:h(s)[1] for s in states if len(h(s)[1])>1}=={B:('Q','C'),Z:('P','Q')}
gaps=[v for s in states for v in h(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(2057512212551,276277395483648)
def act(s,u,z):
    if s==B: return 'Q' if u else 'C'
    if s==Z: return 'P' if z else 'Q'
    return h(s)[1][0]
@cache
def obs(s,u,z):
    a=act(s,u,z)
    if a=='P':return F(0),F(1),F(0),F(0)
    if a=='Q':return F(1),F(0),F(0),F(0)
    children=[obs(nxt(s,i),u,z) for i in range(3)]
    return tuple(sum((P if j%2==0 else Q)[i]*children[i][j] for i in range(3))+int(j>=2) for j in range(4))
def dfs(u,z):
    totals=[0]*4; count=0; hits=[0,0,0]
    def walk(s,mp,mq,seen_B=False):
        nonlocal count
        count+=1
        n=s[0]
        if s==B: hits[0]+=1;seen_B=True
        if s==Z: hits[1]+=1;hits[2]+=int(seen_B)
        a=act(s,u,z)
        if a=='C':
            for i,(pi,qi) in enumerate(zip((3,1,20),(2,2,20))):
                walk(nxt(s,i),mp*pi,mq*qi,seen_B)
        else:
            mul=24**(N-n)
            if a=='Q': totals[0]+=mp*mul
            else: totals[1]+=mq*mul
            totals[2]+=n*mp*mul
            totals[3]+=n*mq*mul
    walk(root,1,1)
    return tuple(F(x,24**N) for x in totals),count,tuple(hits)
corners={};node_counts=[]
for u,z in product((0,1),repeat=2):
    key=u,z
    corners[key]=obs(root,u,z)
    o,n,hits=dfs(u,z)
    assert o==corners[key]
    assert hits==(7,1,0)
    node_counts.append(n)
assert node_counts==[104410,104410,103087,103087]
O=corners[0,0]
DB=tuple(corners[1,0][i]-O[i] for i in range(4))
DZ=tuple(corners[0,1][i]-O[i] for i in range(4))
mixed=tuple(corners[1,1][i]-corners[1,0][i]-corners[0,1][i]+O[i] for i in range(4))
assert mixed==(F(0),)*4
assert DB==(F(256404203125,47552535724032),-F(4708046875,1114512556032),-F(2916052671875,17832200896512),-F(229709703125,835884417024))
assert DZ==(-F(6103515625,78364164096),F(6103515625,78364164096),F(0),F(0))
diff=lambda v:v[0]-v[1]
z0=-diff(O)/diff(DZ);zs=-diff(DB)/diff(DZ)
assert z0==F(1658052573537301,81920000000000000)
assert zs==F(790181343,12800000000)
assert 0<z0<z0+zs<1
def point(u):
    z=z0+zs*u
    return tuple(O[i]+DB[i]*u+DZ[i]*z for i in range(4))
left,right=point(F(0)),point(F(1))
assert left[0]==left[1]==F(1849166499307598953,5258930030792146944)
assert right[0]==right[1]==F(1852236949963598953,5258930030792146944)
assert left[2]==F(1152738710673976045,109561042308169728)
assert right[2]==F(1134822483057976045,109561042308169728)
assert right[0]-left[0]==F(166582609375,285315214344192)
assert left[2]>left[3] and right[2]>right[3]
assert all(v[2]+K*(v[0]+v[1])==h(root)[0] for v in (left,right))
assert left[2]-right[2]==2*K*(right[0]-left[0])
print("STAGE199_REFERENCE_FULL_REAL_PASS",sum(node_counts),"ordered DFS nodes")
