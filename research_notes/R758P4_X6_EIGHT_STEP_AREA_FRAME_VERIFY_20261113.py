#!/usr/bin/env python3
"""R758P4 exhaustive exact 8-step area/frame test (candidate transport only)."""
from collections import Counter, defaultdict
from itertools import permutations
import json

E=(0,1,2); R=(1,2,0); R2=(2,0,1)
T=((1,0,2),(0,2,1),(2,1,0))

def mul(p,q):
    return tuple(p[q[i]] for i in range(3))

def h(w):
    f=E
    for axis,sgn in w:
        f=mul(T[axis],f)
    return f

def q(w):
    return sum((1 if i%2==0 else -1)*axis for i,(axis,sgn) in enumerate(w))%3

def area(w):
    x=[0,0,0]; a=[0,0,0]
    for axis,sgn in w:
        if axis==1:
            a[0]+=x[0]*sgn
        elif axis==2:
            a[1]+=x[0]*sgn
            a[2]+=x[1]*sgn
        x[axis]+=sgn
    assert x==[0,0,0]
    return tuple(a)

def make(s):
    return tuple((int(tok[1]),1 if tok[0]=="+" else -1) for tok in s.split())

w0=make("+0 +1 -0 -1 +0 +2 -0 -2")
w2=make("+0 +1 -0 -1 +2 -0 -2 +0")
assert area(w0)==area(w2)==(1,1,0)
assert q(w0)==0 and q(w2)==2
assert h(w0)==E and h(w2)==R2

pool=((0,1),(0,1),(0,-1),(0,-1),(1,1),(1,-1),(2,1),(2,-1))
fibers=defaultdict(Counter)
for word in set(permutations(pool)):
    a=area(word)
    k=q(word)
    assert h(word)==(E,R,R2)[k]
    fibers[a][k]+=1

assert sum(sum(f.values()) for f in fibers.values())==10080
assert len(fibers)==75
support=Counter(len(f) for f in fibers.values())
assert support=={1:17,2:44,3:14}
assert [fibers[(1,1,0)][k] for k in range(3)]==[48,96,96]
assert [fibers[(0,0,-1)][k] for k in range(3)]==[16,192,192]
totals=[sum(f[k] for f in fibers.values()) for k in range(3)]
assert totals==[3744,3168,3168]

c1=make("+0 +1 -0 -1")
c2=make("+1 -0 -1 +0")
assert area(c1)==area(c2)==(1,0,0)
assert {q(c1),q(c2)}=={1,2}
for u in ((),c1,c2):
    for v in ((),c1,c2):
        assert q(u+v)==(q(u)+q(v))%3

print(json.dumps({
 "status":"PASS", "words":10080, "area_vectors":75,
 "area_fibers_by_frame_support":dict(sorted(support.items())),
 "frames":{"e":totals[0],"r":totals[1],"r2":totals[2]},
 "area_1_1_0_frames":{"e":48,"r":96,"r2":96},
 "witness_area":list(area(w0)),"witness_q":[q(w0),q(w2)],
 "max_repair_bits":2}, sort_keys=True, indent=2))
