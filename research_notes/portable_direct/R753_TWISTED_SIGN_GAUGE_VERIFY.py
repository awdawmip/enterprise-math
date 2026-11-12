from itertools import permutations,product
import json
frames=[(a,s) for a in permutations(range(6),3) for s in product((-1,1),repeat=3)]
def rot2(f):
 a,s=f
 return (a[2:]+a[:2],s)
def ports(f):return tuple(zip(f[0],f[1]))
def cyc2(p):return p[2:]+p[:2]
def gauge(p):
 # source signs s_i, target after C^2 has s_(i+2); desired has s_i
 s=[v for _,v in p]
 return tuple(s[i]*s[(i+2)%3] for i in range(3))
def apply(p,g):return tuple((a,s*e) for (a,s),e in zip(p,g))
n=0;even=0;ident=0;triple=0
for f in frames:
 p=ports(f);g=gauge(p)
 assert g[0]*g[1]*g[2]==1
 q=apply(cyc2(p),g)
 assert q==ports(rot2(f))
 even+=1
 ident+=g==(1,1,1)
 r=q
 for _ in range(2):
  r=apply(cyc2(r),gauge(r))
 assert r==p
 triple+=1
 n+=1
assert n==960 and ident==240 and triple==960
print(json.dumps({"status":"PASS","frames":n,"even_gauge_products":even,"identity_gauge":ident,"nontrivial_gauge":n-ident,"three_step_return":triple,"native_event_permission":False},sort_keys=True))
