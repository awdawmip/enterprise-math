#!/usr/bin/env python3
"""Exact Stage167 model-side verifier. Author-side; external N14 IID only."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(51166022460516,192153882113)
L=F(150858479252536,576461646339)
R=(10,0,1)
X=(5,1,2)
A=('P','Q','C')
def ell(s): return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i): return (s[0]+1,s[1]+(i==0),s[2]+(i==1))
@lru_cache(None)
def bell(s):
    vals=[K*ell(s),L]
    if s[0]<N:
        vals.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
    m=min(vals)
    return m,tuple(a for a,v in zip(A,vals) if v==m),vals
strict={}
ties={}
gaps=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b); m,w,vals=bell(s)
            if len(w)>1: ties[s]=w
            else: strict[s]=w[0]
            gaps.extend(v-m for v in vals if v>m)
assert ties=={R:('Q','C'),X:('Q','C')}
assert len(strict)+len(ties)==680
assert len(gaps)==1238
assert min(gaps)==F(172366798507207447,5163915757745737728)
assert bell((0,0,0))[0]==F(12362030636126506094814337691297,63157738823584353992721825792)
def action(s,r,x):
    if s==R: return 'Q' if r else 'C'
    if s==X: return 'Q' if x else 'C'
    return strict[s]
def suffix(r,x):
    @lru_cache(None)
    def rec(s):
        z=action(s,r,x)
        if z=='P':return (F(0),F(1),F(0),F(0))
        if z=='Q':return (F(1),F(0),F(0),F(0))
        v=[rec(child(s,i)) for i in range(3)]
        return (sum((P[i]*v[i][0] for i in range(3)),F(0)),
                sum((Q[i]*v[i][1] for i in range(3)),F(0)),
                1+sum((P[i]*v[i][2] for i in range(3)),F(0)),
                1+sum((Q[i]*v[i][3] for i in range(3)),F(0)))
    return rec((0,0,0))
def ordered_dfs(r,x):
    # Integer-weight, unmerged ordered paths; different algorithm from suffix.
    pn=(3,1,20); qn=(1,1,10)
    acc=defaultdict(int)
    hits={R:[0,F(0),F(0)],X:[0,F(0),F(0)]}
    nodes=0
    def walk(n,a,b,p,q):
        nonlocal nodes
        nodes+=1
        s=(n,a,b)
        if s in hits:
            h=hits[s]
            h[0]+=1
            h[1]+=F(p,24**n)
            h[2]+=F(q,12**n)
        z=action(s,r,x)
        if z=='C':
            for i in range(3):
                walk(n+1,a+(i==0),b+(i==1),p*pn[i],q*qn[i])
        else:
            acc[n,'ap']+=p;acc[n,'aq']+=q
            acc[n,'tp']+=n*p;acc[n,'tq']+=n*q
            if z=='P': acc[n,'eq']+=q
            else: acc[n,'ep']+=p
    walk(0,0,0,1,1)
    mass=lambda k,b:sum((F(acc[n,k],b**n) for n in range(N+1)),F(0))
    assert mass('ap',24)==mass('aq',12)==1
    return (mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes
corners={}
counts={}
first_hits=None
for r in (0,1):
    for x in (0,1):
        v=suffix(r,x)
        w,h,n=ordered_dfs(r,x)
        assert v==w
        corners[r,x]=v
        counts[(r,x)]=n
        if first_hits is None:first_hits=h
        else:assert h==first_hits
assert counts=={(0,0):387997,(0,1):367237,(1,0):387757,(1,1):366997}
assert first_hits[R]==[10,F(9765625,120932352),F(9765625,60466176)]
assert first_hits[X]==[20,F(125,41472),F(125,15552)]
# The R and X prefix cones cannot contain each other: X already has one zero.
assert X[0]<R[0] and X[1]>R[1]
sub=lambda a,b:tuple(ai-bi for ai,bi in zip(a,b))
base=corners[0,0]
dR=sub(corners[1,0],base)
dX=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),dX)
assert mixed==(F(0),)*4
D=lambda v:v[0]-v[1]
Dr=D(dR);assert Dr
r0=-D(base)/Dr
rs=-D(dX)/Dr
assert r0==F(3629376130799541,11823616000000000)
assert rs==-F(167005511153,7389760000000)
r1=r0+rs
assert r1==F(3362167312954741,11823616000000000)
assert 0<r1<r0<1
M=lambda x:tuple(base[i]+(r0+rs*x)*dR[i]+x*dX[i] for i in range(4))
left=M(F(0));right=M(F(1))
a166=F(881262643750052083615,2530093150022563528704)
v166=F(4276909130601160631957,361441878574651932672)
a167=F(881276478829564219615,2530093150022563528704)
v167=F(4275865622441272343957,361441878574651932672)
width=F(24019235264125,4392522829900283904)
H=bell((0,0,0))[0]
assert left[0]==left[1]==a166
assert right[0]==right[1]==a167
assert left[2]==v166 and right[2]==v167
assert a167-a166==width
assert left[2]>left[3] and right[2]>right[3]
assert all(z[2]+K*z[1]+L*z[0]==H for z in (left,right))
assert right[2]-left[2]==-(K+L)*width
print('STAGE167_AUTHOR_EXACT_PASS')
print('states=680 strict_gaps=1238 ordered_dfs_nodes=',sum(counts.values()))
print('mixed=',mixed,'r0=',r0,'r1=',r1)
print('alpha167=',a167,'V167=',v167,'eta=',width,'slope=',K+L)
