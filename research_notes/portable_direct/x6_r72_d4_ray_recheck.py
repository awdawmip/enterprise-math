#!/usr/bin/env python3
"""Independent exact re-evaluation of the R71 cone bound; standard library only."""
import math,itertools,json
T=((1,0,0),(0,1,0),(0,0,1),(2,6,12),(6,24,60),
   (14,78,252),(4,18,48),(12,72,240),(8,54,192))
def cross(u,v):
 return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def norm(v):
 g=math.gcd(*v);v=tuple(x//g for x in v)
 if next(x for x in v if x)!=abs(next(x for x in v if x)):
  v=tuple(-x for x in v)
 return v
def q(v):
 return max(sum(max(0,x) for x in v),sum(max(0,-x) for x in v))
def sign_image(v):
 return [sum(a*b for a,b in zip(row,v)) for row in T]
lines=sorted({norm(v) for u,w in itertools.combinations(T,2) if any(v:=cross(u,w))})
rays=sorted(set(lines+[tuple(-x for x in r) for r in lines]))
sign=[sign_image(r) for r in rays]
conf=lambda u,v: all(x*y>=0 for x,y in zip(u,v))
triples=[(i,j,k) for i,j,k in itertools.combinations(range(len(rays)),3)
 if conf(sign[i],sign[j]) and conf(sign[i],sign[k]) and conf(sign[j],sign[k])]
maxtr=max(sum(q(rays[i]) for i in t) for t in triples)
result=dict(line_count=len(lines),oriented_count=len(rays),triples=len(triples),
 max_q_ray=max(map(q,rays)),max_q_triple_sum=maxtr,derived_threshold=maxtr-1)
assert result==dict(line_count=28,oriented_count=56,triples=212,max_q_ray=125,
 max_q_triple_sum=235,derived_threshold=234)
print(json.dumps(result,sort_keys=True))
