# Portable adaptation of the published Stage167 checker, with the exact Stage168 constants and two Bernoulli tie actions.
# The distinct locally executed author program and its log are in the Stage168 downloadable evidence ZIP; GitHub storage is not remote execution.
#!/usr/bin/env python3
"""Exact Stage168 model-side verifier. Author-side; external N14 IID only."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(2152236456,8362241)
L=F(2125312232,8362241)
R=(10,0,1)
X=(9,2,0)
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
assert ties=={R:('Q','C'),X:('P','C')}
assert len(strict)+len(ties)==680
assert len(gaps)==1238
assert min(gaps)==F(199132488595033,16180247553933312)
assert bell((0,0,0))[0]==F(58026151900459658728236701,305391946664037178146816)
def action(s,r,x):
    if s==R: return 'Q' if r else 'C'
    if s==X: return 'P' if x else 'C'
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
assert counts=={(0,0):367237,(0,1):365077,(1,0):366997,(1,1):364837}
assert first_hits[R]==[10,F(9765625,120932352),F(9765625,60466176)]
assert first_hits[X]==[36,F(78125,497664),F(78125,1119744)]
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
assert r0==F(3362167312954741,11823616000000000)
assert rs==F(5475969,11546500)
r1=r0+rs
assert r1==F(8969559568954741,11823616000000000)
assert 0<r0<r1<1
M=lambda x:tuple(base[i]+(r0+rs*x)*dR[i]+x*dX[i] for i in range(4))
left=M(F(0));right=M(F(1))
a166=F(881276478829564219615,2530093150022563528704)
v166=F(4275865622441272343957,361441878574651932672)
a167=F(882432475025404219615,2530093150022563528704)
v167=F(4191390146637112343957,361441878574651932672)
width=F(653300078125,1429857692024832)
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
