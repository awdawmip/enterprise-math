#!/usr/bin/env python3
"""R662 exact S3 D3 four-cell X6 loop verifier: finite combinatorial residual only."""
from itertools import permutations, product
from collections import Counter
from json import dump
from pathlib import Path

G=list(permutations(range(3)))
e=(0,1,2)
rot=(1,2,0)
tau=(1,0,2)
tau2=(0,2,1)
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
def conjugate(x,g):return mul(mul(g,x),inv(g))
def class_id(x):
    if x==e:return 'identity'
    if mul(x,x)==e:return 'transposition'
    assert mul(x,mul(x,x))==e
    return 'three_cycle'
def square_hol(w):
    h=e
    for x in w:h=mul(x,h)
    return h

assert set(G)=={e,rot,(2,0,1),tau,tau2,(2,1,0)}
assert mul(rot,mul(rot,rot))==e
assert mul(tau,tau)==e
assert mul(tau,mul(rot,tau))==inv(rot)
vertex_tested=0
for sig in product(G,repeat=4):
    u=[mul(sig[(i+1)%4],inv(sig[i])) for i in range(4)]
    assert square_hol(u)==e
    vertex_tested+=1
classes=Counter()
for u in product(G,repeat=4):
    h=square_hol(u)
    classes[class_id(h)]+=1
    # Root frame stays identity; sequentially trivialize tree edges.
    f=[e]
    for i in range(3):f.append(mul(f[i],inv(u[i])))
    normalized=[mul(mul(f[(i+1)%4],u[i]),inv(f[i])) for i in range(4)]
    assert normalized[:3]==[e,e,e]
    assert normalized[3]==h
assert classes=={'identity':216,'transposition':648,'three_cycle':432}
vertex_defects=[e,rot,e,e]
cob=[mul(vertex_defects[(i+1)%4],inv(vertex_defects[i])) for i in range(4)]
assert cob==[rot,inv(rot),e,e] and square_hol(cob)==e
independent=[rot,e,e,e]
assert square_hol(independent)==rot
orbit_counts={}
for beta in range(5):
    reps=set()
    for v in product(G,repeat=beta):
        reps.add(min(tuple(conjugate(x,g) for x in v) for g in G))
    expected=(6**beta+3*2**beta+2*3**beta)//6
    assert len(reps)==expected
    orbit_counts[beta]=len(reps)
assert orbit_counts=={0:1,1:3,2:11,3:49,4:251}
assert class_id(tau)==class_id(tau2)=='transposition'
after0=mul(tau,tau); after1=mul(tau,tau2)
assert after0==e and class_id(after1)=='three_cycle'
chart=[(0,0,0,0,0,0),(1,0,0,0,0,0),(1,1,0,0,0,0),(0,1,0,0,0,0)]
for i in range(4):
    d=[chart[(i+1)%4][j]-chart[i][j] for j in range(6)]
    assert sum(abs(x) for x in d)==1
result={
 'marker':'R662_X6_FOUR_CELL_CYCLE_S3_COBBOUNDARY_GAUGE_PASS',
 'science_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'input':'Native-X6 4-cell signed one-axis-step adjacency; auxiliary independent S3 edge label',
 'vertex_assignments':vertex_tested,
 'edge_assignments':6**4,
 'cycle_class_counts':dict(classes),
 'orbit_counts':{str(k):v for k,v in orbit_counts.items()},
 'coboundary_loop':square_hol(cob),
 'independent_edge_loop':square_hol(independent),
 'class_update_before':[tau,tau2],
 'shared_update_left':tau,
 'class_update_after':[after0,after1],
 'review':'AUTHOR_SIDE_UNREVIEWED','native_H_scheduler':'NOT_INSTANTIATED'
}
p=Path(__file__).with_name('R662_EVIDENCE_RECOMPUTED.json')
p.write_text(__import__('json').dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(result['marker'],result['vertex_assignments'],result['edge_assignments'],orbit_counts)
