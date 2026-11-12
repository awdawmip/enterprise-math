from itertools import permutations, product
import json
frames=[(a,s) for a in permutations(range(6),3) for s in product((-1,1),repeat=3)]
def rot(f):
 a,s=f
 return (a[1:]+a[:1],tuple(-v for v in s))
checks=0
for f in frames:
 orbit=set()
 x=f
 for _ in range(6):
  orbit.add(x)
  x=rot(x)
 assert len(orbit)==6
 for slot in range(3):
  for axis in set(range(6))-set(f[0]):
   for sign in (-1,1):
    a=list(f[0]);s=list(f[1])
    a[slot]=axis;s[slot]=sign
    assert (tuple(a),tuple(s)) not in orbit
    checks+=1
assert checks==17280
print(json.dumps({"status":"PASS","frames":960,"candidate_one_axis_replacements":17280,"V1R_reachable_replacements":0,"native_coupled_permission_proved":False},sort_keys=True))
