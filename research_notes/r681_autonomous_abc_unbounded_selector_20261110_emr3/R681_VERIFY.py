#!/usr/bin/env python3
"""R681 exact model-local affine-envelope certificate; Python 3 stdlib only."""
from itertools import combinations,permutations
from fractions import Fraction
T=tuple(combinations(range(6),3))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
PASS=((0,1),(1,2),(2,0))
BIAS=((-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),(2,4,3,-10),(3,2,4,-10),(4,3,2,-10))
PHASE=((),(0,),(0,1))
w0=(-1,1,-2,-1);w=(-1,-2,-3,0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def code(s,m):
    if any((a in s)+(b in s)!=1 for a,b in m):return 0
    return 1 if sum(b in s for a,b in m)%2==0 else -1
C={s:tuple(code(s,m) for m in MATCH) for s in T}
N={s:tuple(t for t in T if len(set(s)&set(t))==2) for s in T}
assert len(set(C.values()))==20 and all(len(v)==9 for v in N.values())
def state(bias,p,n):
    M=[[0]*4 for _ in range(4)]
    for a,b in PASS:M[a][b]=n
    u=list(bias)
    for e in p:
        a,b=PASS[e];M[a][b]+=1;u[a]+=1;u[b]-=1
    return u,M
def score(u,M,s,t):
    return dot(u,C[t])+sum(C[s][i]*(M[i][j]-M[j][i])*C[t][j] for i in range(4) for j in range(4))
def line(b,p,s,t):
    u,M=state(b,p,0);v,Q=state(b,p,1)
    z=score(u,M,s,t)
    return score(v,Q,s,t)-z,z
def cross(wv=None,K=1):
    R=Fraction(0)
    for b in BIAS:
      for p in PHASE:
       for s in T:
        D={t:line(b,p,s,t) for t in N[s]}
        for a,c in combinations(N[s],2):
         m=K*(D[a][0]-D[c][0])
         z=K*(D[c][1]-D[a][1])
         if wv is not None:z+=dot(wv,C[c])-dot(wv,C[a])
         if m:R=max(R,Fraction(z,m))
    return R,(R.numerator+R.denominator-1)//R.denominator+1
Rp,bound=cross()
assert (Rp,bound)==(19,20)
def ties(b,p,n,wv=None,K=1):
    u,M=state(b,p,n);out=[]
    for s in T:
        D={t:K*score(u,M,s,t)+(dot(wv,C[t]) if wv else 0) for t in N[s]}
        maxv=max(D.values());best=[t for t in N[s] if D[t]==maxv]
        if len(best)>1:out.append((s,best,maxv))
    return out
P=set()
for b in BIAS:
 for p in PHASE:
  for n in range(bound+1):
   for s,win,v in ties(b,p,n):
    P.update(tuple(sorted(x)) for x in combinations(win,2))
assert len(P)==44
def shell(k):
 def rec(i,r,acc):
  if i==4:
   if r==0:yield tuple(acc)
   return
  for a in range(r+1):
   for val in ((0,) if a==0 else (-a,a)):
    yield from rec(i+1,r-a,acc+[val])
 yield from rec(0,k,[])
counts=[]
for k in range(7):
 W=list(shell(k))
 good=[v for v in W if all(dot(v,C[a])!=dot(v,C[b]) for a,b in P)]
 counts.append((len(W),len(good)))
 if k==6:mins=good
assert counts==[(1,0),(8,0),(32,0),(88,0),(192,0),(360,0),(608,28)]
assert w in mins
def min_pos(m,z):
 if m==0:return z if z>0 else None
 if m>0:return m*max(0,(-z)//m+1)+z
 if z<=0:return None
 return z+m*((z-1)//(-m))
K=1;wit=None
for b in BIAS:
 for p in PHASE:
  for s in T:
   D={t:line(b,p,s,t) for t in N[s]}
   for a,c in permutations(N[s],2):
    rr=dot(w,C[c])-dot(w,C[a])
    if rr<=0:continue
    gap=min_pos(D[a][0]-D[c][0],D[a][1]-D[c][1])
    if gap is None:continue
    k=rr//gap+1
    if k>K:K=k;wit=(b,p,s,a,c,gap,rr)
assert K==10 and wit==((-4,-3,-2,10),(),(0,1,3),(1,3,4),(1,2,3),1,9)
Rq,lim=cross(w0,7);assert Rq==Fraction(137,7) and lim==21
collisions=[]
for b in BIAS:
 for p in PHASE:
  matches=[(n,s,win) for n in range(lim+1) for s,win,v in ties(b,p,n,w0,7)]
  assert len(matches)==1,(b,p,matches)
  n,s,win=matches[0];collisions.append((b,p,n,s,win))
assert len(collisions)==18
assert min(3*n+len(p) for b,p,n,s,win in collisions)==31
for b in BIAS:
 for p in PHASE:
  for n in range(max(bound,lim)+1):
   assert not ties(b,p,n,w,K)
   u,M=state(b,p,n)
   for s in T:
    pscore={t:score(u,M,s,t) for t in N[s]}
    winner=max(N[s],key=lambda t:K*pscore[t]+dot(w,C[t]))
    assert pscore[winner]==max(pscore.values())
q=[0,0,0]
for i in range(300):
 e=min(range(3),key=lambda t:(q[t],t));assert e==i%3;q[e]+=1
print({'primary_crossing':str(Rp),'primary_pairs':len(P),'L1_shells':counts,
       'new_w':w,'K':K,'K9_witness':wit,'old_crossing':str(Rq),
       'old_ties':len(collisions),'first_event':31})
print('R681_AFFINE_ABC_GLOBAL_STRICT_SELECTOR_EXACT_PASS')
