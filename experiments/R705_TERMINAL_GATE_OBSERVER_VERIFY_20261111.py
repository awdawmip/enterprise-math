#!/usr/bin/env python3
"""Exact R705 X6 signed triad source and terminal-gate observer audit."""
import itertools
from collections import defaultdict, Counter
from math import factorial
import json

D=6
paths=[]
for axes in itertools.combinations(range(D),3):
    for ss in itertools.product((-1,1),repeat=3):
        sign=dict(zip(axes,ss))
        for order in itertools.permutations(axes):
            z=(0,)*D; ports=[]
            for axis in order:
                sigma=sign[axis];ports.append((z,axis,sigma))
                v=list(z);v[axis]+=sigma;z=tuple(v)
            paths.append((tuple(ports),z))
assert len(paths)==960
ends=defaultdict(set);terminal=defaultdict(set)
for p,(ports,end) in enumerate(paths):
    ends[end].add(p);terminal[ports[-1]].add(p)
assert len(ends)==160 and len(terminal)==480
group=defaultdict(list)
for port,ids in terminal.items():
    assert len(ids)==2
    assert len({paths[i][1] for i in ids})==1
    end=paths[next(iter(ids))][1];group[end].append(port)
assert len(group)==160 and all(len(v)==3 for v in group.values())
for end,v in group.items():
    assert len({p[1] for p in v})==3
    assert set().union(*(terminal[p] for p in v))==ends[end]
local={}
for r in range(4):
    classes=defaultdict(set)
    for mask in range(8):
        observation=(mask.bit_count(),tuple((mask>>i)&1 for i in range(r)))
        classes[observation].add(mask)
    assert len(classes)==2**r*(4-r)
    local[str(r)]={'classes':len(classes),'max_fiber':max(map(len,classes.values())),
      'fiber_histogram':dict(Counter(map(len,classes.values())))}
assert [local[str(i)]['classes'] for i in range(4)]==[4,6,8,8]
e=(1,1,1,0,0,0);pp=sorted(group[e],key=lambda p:p[1])
assert [p[1] for p in pp]==[0,1,2]
A={pp[0]};B={pp[1]}
assert sum(2 for p in A)==sum(2 for p in B)==2
assert sum(2 for p in A if p[1]==0)==2
assert sum(2 for p in B if p[1]==0)==0
def perm_point(z,g):
    v=[0]*D
    for i,x in enumerate(z):v[g[i]]=x
    return tuple(v)
for g in itertools.permutations(range(D)):
    eg=perm_point(e,g)
    for mask in range(8):
        allowed={pp[i] for i in range(3) if (mask>>i)&1}
        transformed={(perm_point(p[0],g),g[p[1]],p[2]) for p in allowed}
        assert transformed.issubset(set(group[eg]))
        assert 2*len(transformed)==2*mask.bit_count()
        for k in range(3):
            target=(perm_point(pp[k][0],g),g[pp[k][1]],pp[k][2])
            assert (pp[k] in allowed)==(target in transformed)
for r in (1,2):
    for subset in itertools.combinations(range(3),r):
        S=set(subset)
        assert any({g[i] for i in S}!=S for g in itertools.permutations(range(3)))
assert 2**413<6**160<=2**414
assert 4**160==2**320 and 8**160==2**480
evidence={'marker':'R705_TERMINAL_GATE_BRC_OBSERVER_LATTICE_EXACT_PASS',
'source_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
'scope':'static independent terminal Boolean Port gates',
'paths':len(paths),'endpoints':len(ends),'terminal_ports':len(terminal),
'classes_by_address_count':local,'global_optimal_bits':{'0':320,'1':414,'2':480,'3':480},
'covariance_cases':factorial(D)*8*3,
'witness':{'endpoint':[1,1,1,0,0,0],'A_last_axis':[0],
'B_last_axis':[1],'same_total_count':2,'named_axis_0_query':[2,0]},
'native_remaining':['Link/Port occupancy','V29 PASS/TRANSFER','V39 j','TRIADIC_CLOSURE_E']}
with open('R705_TERMINAL_GATE_BRC_OBSERVER_EVIDENCE_20261111.json','w') as f:json.dump(evidence,f,indent=2,sort_keys=True)
print(evidence['marker'],len(paths),len(ends),len(terminal),evidence['covariance_cases'])
