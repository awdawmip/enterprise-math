#!/usr/bin/env python3
"""R643 exact integer verifier for a proposed PF10 count-changing V27 extension."""
from itertools import combinations
from collections import Counter
T=tuple(combinations(range(6),3))
N={s:tuple(t for t in T if len(set(s)&set(t))==2) for s in T}
M=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),
   ((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
def code(m,s):
    z=set(s);b=[]
    for a,c in m:
        if (a in z)+(c in z)!=1:return 0
        b.append(c in z)
    return 1 if sum(b)%2==0 else -1
C={s:tuple(code(m,s) for m in M) for s in T}
assert len(C)==len(set(C.values()))==20 and sum(map(len,N.values()))==180
U=(-2,-4,-3,10)
O=((0,1,-1,0),(-1,0,1,0),(1,-1,0,0),(0,0,0,0))
def a(s,t):return sum(C[s][i]*O[i][j]*C[t][j] for i in range(4) for j in range(4))
def v(t):return sum(U[i]*C[t][i] for i in range(4))
def phi(s,t,n):return v(t)+(n+1)*a(s,t)
def wins(s,n):
    mx=max(phi(s,t,n) for t in N[s])
    return tuple(t for t in N[s] if phi(s,t,n)==mx)
L=((0,1,2),(1,2,3),(2,3,4),(0,3,4),(0,3,5),(0,2,5))
margin=[]
for i,s in enumerate(L):
    w=L[(i+1)%6]
    assert wins(s,0)==(w,) and a(s,w)==max(a(s,t) for t in N[s])==1
    margin.append(min(phi(s,w,0)-phi(s,t,0) for t in N[s] if t!=w))
assert margin==[4,1,1,4,1,1]
ties={}
for n in range(14):
    d={''.join(map(str,s)):len(wins(s,n)) for s in T if len(wins(s,n))>1}
    if d:ties[n]=d
assert ties=={1:{'015':2},2:{'124':2,'134':2},3:{'045':2,'345':2},
              4:{'125':2},11:{'245':2},12:{'135':2},13:{'014':2}}
stable={}
for s in T:
    w=wins(s,14);assert len(w)==1
    stable[s]=w[0]
    assert a(s,w[0])==max(a(s,t) for t in N[s])
    assert min(phi(s,w[0],14)-phi(s,t,14) for t in N[s] if t!=w[0])>=1
assert all(wins(L[n%6],n)==(L[(n+1)%6],) for n in range(120))
# Source-defined shared-axis slot transfer, six-step transposition.
z={k:i for i,k in enumerate(L[0])}
for n in range(12):
    s=L[n%6];t=L[(n+1)%6];q=set(s)&set(t)
    leave=next(iter(set(s)-q));enter=next(iter(set(t)-q))
    z={**{k:z[k] for k in q}, enter:z[leave]}
    if n==5:assert tuple(z[k] for k in L[0])==(2,1,0)
assert tuple(z[k] for k in L[0])==(0,1,2)
P=tuple(combinations(range(4),2))
def obs(x):
    m=[x[8+i*4:12+i*4] for i in range(4)]
    return tuple(x[i]-x[i+4] for i in range(4))+tuple(m[i][j]-m[j][i] for i,j in P)
K=[]
for i in range(4):
    x=[0]*24;x[i]=x[i+4]=1;K.append(x)
for i,j in P:
    x=[0]*24;x[8+4*i+j]=x[8+4*j+i]=1;K.append(x)
for i in range(4):
    x=[0]*24;x[8+5*i]=1;K.append(x)
assert len(K)==14 and all(obs(x)==(0,)*10 for x in K)
def unsafe(x):
    y=list(x);y[0]+=x[8];return y
assert obs(unsafe(K[10]))==(1,)+(0,)*9
x=list((0,0,0,10)+(2,4,3,0))
x.extend(int((i,j) in {(0,1),(1,2),(2,0)}) for i in range(4) for j in range(4))
y=x.copy();y[8]+=2
assert obs(x)==obs(y) and obs(unsafe(y))[0]-obs(unsafe(x))[0]==2
def next_from(z,s):
    u=z[:4];om=[[0]*4 for _ in range(4)]
    for (i,j),b in zip(P,z[4:]):om[i][j]=b;om[j][i]=-b
    ss={t:sum(u[i]*C[t][i] for i in range(4))+sum(C[s][i]*om[i][j]*C[t][j] for i in range(4) for j in range(4)) for t in N[s]}
    return tuple(t for t in N[s] if ss[t]==max(ss.values()))
assert next_from(obs(unsafe(x)),(0,1,3))==((0,1,2),)
assert next_from(obs(unsafe(y)),(0,1,3))==((0,3,5),)
for n in range(151):
    for s in T:
        if n>=14: assert wins(s,n)==(stable[s],)
print('R643_PF10_COUNT_EVOLVING_EXACT_PASS',
      'triads',len(T),'edges',sum(map(len,N.values())),
      'critical_n',sorted(ties),'stabilization_n',14,
      'crosschecks',151*len(T))
