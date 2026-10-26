#!/usr/bin/env python3
"""Stage159 author verifier: exact count Bellman + unmerged ordered DFS.
EXTERNAL finite iid N14 only; not a native P000/Driver proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict

N=14
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(580027221414,1887912013); L=F(566236422120,1887912013)
I=(9,5,4); J=(10,2,0)
acts='PQC'
def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,x):return(s[0]+1,s[1]+(x==0),s[2]+(x==1))
@lru_cache(None)
def value(s):
    v=[K*ratio(s),L]
    if s[0]<N:v.append(1+sum(P[x]*value(child(s,x))[0] for x in range(3)))
    return min(v),tuple(v)

strict={};gaps=[];ties={}
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=n,a,b; m,v=value(s);opt=[acts[x] for x,c in enumerate(v) if c==m]
            if len(opt)>1:ties[s]=opt
            else:strict[s]=opt[0]
            gaps += [c-m for c in v if c>m]
assert len(strict)+len(ties)==680
assert ties=={I:['Q','C'],J:['P','C']},ties
assert len(gaps)==1238 and min(gaps)==F(20367756,1887912013)

def move(s,i,j):
    if s==I:return 'Q' if i else 'C'
    if s==J:return 'P' if j else 'C'
    return strict[s]

def conditional(i,j):
    @lru_cache(None)
    def out(s):
        m=move(s,i,j)
        if m=='P':return F(0),F(1),F(0),F(0)
        if m=='Q':return F(1),F(0),F(0),F(0)
        z=[out(child(s,x)) for x in range(3)]
        return(sum(P[x]*z[x][0] for x in range(3)),
               sum(Q[x]*z[x][1] for x in range(3)),
               1+sum(P[x]*z[x][2] for x in range(3)),
               1+sum(Q[x]*z[x][3] for x in range(3)))
    return out((0,0,0))

def unmerged_dfs(i,j):
    pn=(3,1,20); qn=(1,1,10)
    counts=defaultdict(int); first={I:[0,F(0),F(0)],J:[0,F(0),F(0)]}
    nodes=0
    def visit(n,a,b,p,q):
        nonlocal nodes
        nodes+=1;s=n,a,b
        if s in first:
            first[s][0]+=1
            first[s][1]+=F(p,24**n);first[s][2]+=F(q,12**n)
        m=move(s,i,j)
        if m!='C':
            counts[n,'allp']+=p;counts[n,'allq']+=q
            counts[n,'tp']+=p*n;counts[n,'tq']+=q*n
            if m=='Q':counts[n,'ep']+=p
            else:counts[n,'eq']+=q
            return
        for x in range(3):visit(n+1,a+(x==0),b+(x==1),p*pn[x],q*qn[x])
    visit(0,0,0,1,1)
    def total(k,den):return sum((F(counts[n,k],den**n) for n in range(N+1)),F(0))
    assert total('allp',24)==total('allq',12)==1
    return (total('ep',24),total('eq',12),total('tp',24),total('tq',12)),first,nodes

corners={};first=None;visits={}
for i in range(2):
    for j in range(2):
        c=conditional(i,j);d,f,n=unmerged_dfs(i,j)
        assert c==d
        corners[i,j]=c;visits[f'{i}{j}']=n
        if first is None:first=f
        else:assert first==f
assert first[I]==[30,F(5,1811939328),F(5,859963392)]
assert first[J]==[45,F(1953125,11943936),F(1953125,26873856)]
base=corners[0,0]
def diff(x,y):return tuple(a-b for a,b in zip(x,y))
di=diff(corners[1,0],base);dj=diff(corners[0,1],base)
assert diff(diff(corners[1,1],corners[1,0]),diff(corners[0,1],base))==(0,0,0,0)
j0=-(base[0]-base[1])/(dj[0]-dj[1]);js=-(di[0]-di[1])/(dj[0]-dj[1])
assert j0==F(1036789387122389,4611571200000000)
assert js==F(163474367,1537190400000000)
assert 0<j0<1 and 0<j0+js<1
def at(i):return tuple(base[k]+i*di[k]+(j0+js*i)*dj[k] for k in range(4))
left=at(F(0));right=at(F(1));root=value((0,0,0))[0]
assert left[0]==left[1]==F(763167995878686618305,2192919042319171190784)
assert left[2]==F(3292184925194961698843,274114880289896398848)
assert right[0]==right[1]==F(381583997981821329445,1096459521159585595392)
assert right[2]==F(13168739674988914815857,1096459521159585595392)
assert left[2]>left[3] and right[2]>right[3]
for m in (left,right):assert m[2]+K*m[1]+L*m[0]==root
assert right[0]-left[0]==F(9439560065,243657671368796798976)
assert right[2]-left[2]==-(K+L)*(right[0]-left[0])
print('PASS: 680 Bellman states; 2 ties; 1238 positive gaps; min',min(gaps))
print('PASS: first hit',first,'ordered DFS node counts',visits)
print('PASS: four exact corners, zero mixed term; j(i)=',j0,'+',js,'*i')
print('PASS: alpha159',right[0],'V159',right[2], 'width',right[0]-left[0])
print('PASS: both exact endpoint dual equalities and strict time dominance')
