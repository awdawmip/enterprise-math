#!/usr/bin/env python3
"""Exact dual-ray scan from Stage148. Candidate only, not Stage149 primal proof."""
from fractions import Fraction as F
N=14
P=(F(1,8),F(1,24),F(5,6))
K0=F(15834013488,41571575)
L0=F(15595845464,41571575)
B=(11,0,1)
T=(7,1,2)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def children(s):
    n,a,b=s
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def r(s):
    return F(2**(s[1]+s[2]),3**s[1])
def add(x,y):
    return tuple(a+b for a,b in zip(x,y))
def mul(t,x):
    return tuple(t*a for a in x)
def ev(x,K,L):
    return x[0]+x[1]*K+x[2]*L
H={};actions={};D={}
for s in reversed(S):
    d={"P":(F(0),r(s),F(0)),"Q":(F(0),F(0),F(1))}
    if s[0]<N:
        c=(F(1),F(0),F(0))
        for i,ch in enumerate(children(s)):
            c=add(c,mul(P[i],H[ch]))
        d["C"]=c
    smallest=min(ev(x,K0,L0) for x in d.values())
    opts=tuple(a for a,v in d.items() if ev(v,K0,L0)==smallest)
    chosen="Q" if s in (B,T) else opts[0]
    assert chosen in opts
    H[s]=d[chosen];actions[s]=chosen;D[s]=d
assert tuple(a for a in D[B] if ev(D[B][a],K0,L0)==min(ev(z,K0,L0) for z in D[B].values()))==("Q","C")
b_continue=D[B]["C"]
dK=1-b_continue[2]
dL=b_continue[1]
if dK+dL>0:
    dK,dL=-dK,-dL
assert (dK,dL)==(-F(43,1536),-F(7,288))
crossings=[]
for s,d in D.items():
    for name,coeff in d.items():
        if name==actions[s]:
            continue
        base=d[actions[s]]
        gap=ev(coeff,K0,L0)-ev(base,K0,L0)
        slope=(coeff[1]-base[1])*dK+(coeff[2]-base[2])*dL
        if gap==0:
            if s==B:assert slope==0
            if s==T:assert slope>0  # T Q-stop is strictly best after start
        elif slope<0:
            crossings.append((gap/(-slope),s,actions[s],name))
theta,s,a,b=min(crossings)
assert (theta,s,a,b)==(F(2007228070858752,11079947170025),(11,7,3),"C","P")
K1=K0+theta*dK
L1=L0+theta*dL
assert (K1,L1)==(F(100164600,266527),F(98815768,266527))
V={};ties=[];gaps=[]
for s in reversed(S):
    d={"P":K1*r(s),"Q":L1}
    if s[0]<N:
        d["C"]=1+sum((P[i]*V[ch] for i,ch in enumerate(children(s))),F())
    m=min(d.values())
    V[s]=m
    opt=tuple(a for a,z in d.items() if z==m)
    if len(opt)>1:ties.append((s,opt))
    gaps.extend(z-m for z in d.values() if z>m)
assert set(ties)=={(B,("Q","C")),((11,7,3),("P","C"))}
assert len(S)==680 and len(gaps)==1238
assert min(gaps)==F(2016649859,176854523904)
assert V[0,0,0]==F(2645762825003325844206337,9733658641089851031552)
print("PASS_STAGE149_DUAL_CANDIDATE_ONLY",K1,L1,ties)
