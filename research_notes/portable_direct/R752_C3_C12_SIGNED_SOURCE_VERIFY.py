from itertools import permutations, product
import json
frames=[(a,s) for a in permutations(range(6),3) for s in product((-1,1),repeat=3)]
def rotate(f):
 a,s=f
 return (a[1:]+a[:1],tuple(-v for v in s))
def step(st):
 f,m=st
 return (f,"CLOSURE") if m=="SHELL" else (rotate(f),"SHELL")
def stepn(st,n):
 for _ in range(n):st=step(st)
 return st
def ports(f):return tuple(zip(f[0],f[1]))
def cycle(p):return p[1:]+p[:1]
def support(p):return frozenset(p)
count={str(n):0 for n in (1,2,4,8,12)}
signed_source_preserved={str(n):0 for n in (2,4,8,12)}
for f in frames:
 p=ports(f)
 for n in (1,2,4,8,12):
  q=ports(stepn((f,"SHELL"),n)[0])
  if n==4 and q==cycle(cycle(p)):count[str(n)]+=1
  elif n==8 and q==cycle(p):count[str(n)]+=1
  elif n==12 and q==p:count[str(n)]+=1
  elif n in (1,2):count[str(n)]+=int(q==cycle(p))
  if n in (2,4,8,12) and support(q)==support(p):
   signed_source_preserved[str(n)]+=1
assert count=={"1":0,"2":0,"4":240,"8":240,"12":960},count
assert signed_source_preserved=={"2":0,"4":240,"8":240,"12":960},signed_source_preserved
print(json.dumps({"status":"PASS","frames":960,"R748_shift_compatibility_counts":count,"signed_source_preserved":signed_source_preserved,"homogeneous_sign_frames":240,"native_event_permission":False},sort_keys=True))
