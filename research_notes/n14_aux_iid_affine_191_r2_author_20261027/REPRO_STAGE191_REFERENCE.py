#!/usr/bin/env python3
"""Stage191 N14 external IID exact rational reference verifier.
This source is a standalone reference; original executed source/logs are in
EM_STAGE191_AUTHOR_EXACT_PORTABLE_20261027.tar.xz (SHA256 in PROOF).
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

P=(F(1,8), F(1,24), F(5,6))
Q=(F(1,12), F(1,12), F(5,6))
N=14
K=F(610519409541,3646579780)
L=F(30208318184,182328989)
H=F(531209309176160736181221937,4161698766215586030551040)
X=(8,0,1); Z=(10,5,2)
a0=F(28137949158459611576537,80134219991312171532288)
v0=F(3422790017676192400495567,320536879965248686129152)
x0_expected=F(21216994209825749,44937930240000000)
delta_expected=F(569778090625,4347559678348099584)
a1_expected=F(4019708522944196853791,11447745713044595933184)
v1_expected=F(488968003499440699225081,45790982852178383732736)

def successor(s,i):
    n,a,b=s
    return n+1,a+(i==0),b+(i==1)

@lru_cache(None)
def bell(s):
    n,a,b=s
    d={'P':K*F(2**(a+b),3**a), 'Q':L}
    if n<N:
        d['C']=1+sum(P[i]*bell(successor(s,i))[0] for i in range(3))
    m=min(d.values())
    return m,tuple(t for t,v in d.items() if v==m),tuple(v-m for v in d.values() if v>m)

states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
ties={s:bell(s)[1] for s in states if len(bell(s)[1])>1}
gaps=[g for s in states for g in bell(s)[2]]
assert len(states)==680 and len(gaps)==1238
assert ties=={X:('Q','C'),Z:('P','C')}
assert min(gaps)==F(8957179515094375931,451573216820267581440)
assert bell((0,0,0))[0]==H
assert Z[0]-X[0] < Z[1]-X[1] # disjoint tie first-hit cones

@lru_cache(None)
def action(s):
    if s in (X,Z): return 'C'
    acts=bell(s)[1]
    assert len(acts)==1,(s,acts)
    return acts[0]

@lru_cache(None)
def suffix(s,x,z):
    if s==X:
        q=(F(1),F(0),F(0),F(0))
        v=continuation(s,x,z)
        return tuple(F(x)*q[j]+(1-F(x))*v[j] for j in range(4))
    if s==Z:
        p=(F(0),F(1),F(0),F(0))
        v=continuation(s,x,z)
        return tuple(F(z)*p[j]+(1-F(z))*v[j] for j in range(4))
    a=action(s)
    if a=='P': return F(0),F(1),F(0),F(0)
    if a=='Q': return F(1),F(0),F(0),F(0)
    return continuation(s,x,z)

def continuation(s,x,z):
    v=[suffix(successor(s,i),x,z) for i in range(3)]
    return tuple(sum((P if j in(0,2) else Q)[i]*v[i][j] for i in range(3))
                 +(j>=2) for j in range(4))

corner={(x,z):suffix((0,0,0),x,z) for x,z in product((0,1),repeat=2)}
B=corner[0,0]
DX=tuple(corner[1,0][j]-B[j] for j in range(4))
DZ=tuple(corner[0,1][j]-B[j] for j in range(4))
C=tuple(corner[1,1][j]-corner[1,0][j]-corner[0,1][j]+B[j]
        for j in range(4))
assert C==(F(0),)*4

# Completely separate ordered-history tree, integer P/Q numerator weights;
# do not merge histories by their count state.
def ordered_dfs(x,z):
    total=[0,0,0,0]
    nodes=hitX=hitZ=ancestry=0
    denom=24**N
    def go(s,wp,wq,seenX):
        nonlocal nodes,hitX,hitZ,ancestry
        nodes+=1
        n,a,b=s
        if s==X: hitX+=1;seenX=True
        if s==Z:
            hitZ+=1
            if seenX: ancestry+=1
        if s==X: act='Q' if x else 'C'
        elif s==Z: act='P' if z else 'C'
        else: act=action(s)
        if act!='C':
            scale=24**(N-n)
            if act=='Q': total[0]+=wp*scale
            if act=='P': total[1]+=wq*scale
            total[2]+=n*wp*scale
            total[3]+=n*wq*scale
        else:
            assert n<N
            for i,(pi,qi) in enumerate(((3,2),(1,2),(20,20))):
                go(successor(s,i),wp*pi,wq*qi,seenX)
    go((0,0,0),1,1,False)
    return tuple(F(u,denom) for u in total),(nodes,hitX,hitZ,ancestry)

num_nodes=0
for x,z in product((0,1),repeat=2):
    vector,stats=ordered_dfs(x,z)
    assert vector==corner[x,z] and stats[1:]==(8,640,0)
    num_nodes+=stats[0]
assert num_nodes==697144

dB=B[0]-B[1]
dX=DX[0]-DX[1]
dZ=DZ[0]-DZ[1]
assert dX>0
x0=-dB/dX
slope=-dZ/dX
assert x0==x0_expected and slope==F(577693,3900862000)
def balanced(z):
    x=x0+slope*z
    return tuple(B[j]+x*DX[j]+z*DZ[j] for j in range(4))
start=balanced(F(0)); end=balanced(F(1))
assert start[0]==start[1]==a0 and start[2]==v0
assert end[0]==end[1]==a1_expected and end[2]==v1_expected
assert 0<x0<x0+slope<1
for o in (start,end):
    assert o[2]>o[3] and o[2]+K*o[1]+L*o[0]==H
assert end[0]-start[0]==delta_expected
assert -(end[2]-start[2])/(end[0]-start[0]) == K+L
print("STAGE191_REFERENCE_EXACT_PASS",
      "states",len(states),"strict_gaps",len(gaps),"DFS_nodes",num_nodes,
      "alpha191",end[0],"V191",end[2],"slope",-(K+L))
