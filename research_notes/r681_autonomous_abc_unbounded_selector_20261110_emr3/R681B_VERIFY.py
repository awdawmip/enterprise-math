#!/usr/bin/env python3
"""R681B: integer check of field-C3 covariant priority scheduler."""
from itertools import product,combinations
W=(-1,-2,-3,0)
def rot(v):return (v[2],v[0],v[1])+tuple(v[3:])
def choose(q,w):
    v=[i for i in range(3) if q[i]==min(q)]
    assert len({w[i] for i in v})==len(v)
    return max(v,key=lambda i:w[i])
def step(q,w):
    i=choose(q,w); a=list(q);a[i]+=1
    return tuple(a),i
checks=0
for q in product(range(9),repeat=3):
 for k in range(3):
    w=W
    for _ in range(k):w=rot(w)
    nq,i=step(q,w)
    nr,j=step(rot(q),rot(w))
    assert j==(i+1)%3 and nr==rot(nq)
    checks+=1
for k in range(3):
    w=W
    for _ in range(k):w=rot(w)
    q=(0,0,0)
    for t in range(300):
      q,i=step(q,w)
      assert i==(k+t)%3
      assert q==tuple((t+1)//3+(1 if (j-k)%3 < (t+1)%3 else 0) for j in range(3))
MCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
def c(s):
    out=[]
    for m in MCH:
      if any((a in s)+(b in s)!=1 for a,b in m):out.append(0)
      else:out.append(1 if sum(b in s for a,b in m)%2==0 else -1)
    return tuple(out)
assert tuple(x-y for x,y in zip(c((0,1,4)),c((1,3,5))))==(1,0,-1,0)
M=[[0]*4 for _ in range(4)];M[0][1]=M[1][2]=1
B=(-4,-3,-2,10)
u=[B[i]+sum(M[i][j]-M[j][i] for j in range(4)) for i in range(4)]
def score(s,t):
    a,b=c(s),c(t)
    return sum(u[i]*b[i] for i in range(4))+sum(a[i]*(M[i][j]-M[j][i])*b[j] for i in range(4) for j in range(4))
s=(1,4,5); N=[t for t in combinations(range(6),3) if len(set(t)&set(s))==2]
mx=max(score(s,t) for t in N)
win={t for t in N if score(s,t)==mx}
assert {(0,1,4),(1,3,5)}.issubset(win)
print({'C3_equivariance_checks':checks,'rotated_schedule_events':900,'C3_context_orbit_minimum':3})
print('R681B_TYPED_C3_COVARIANT_PRIORITY_SCHEDULER_EXACT_PASS')
