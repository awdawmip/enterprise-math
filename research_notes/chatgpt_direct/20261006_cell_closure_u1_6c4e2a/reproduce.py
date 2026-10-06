#!/usr/bin/env python3
"""Compact same-author BRC replay of U1. No native force/heartbeat admission.

Run with sources/brc_weighted.py from the evidence package, or in the recorded
repository folder. The file is pinned by Git blob. Only unused imports are
removed. Full tagged diagnostics are in check_unit.py and the evidence archive.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import ast
import hashlib
import json
import sys
import types

root = Path(__file__).resolve().parent
source = root / 'sources/brc_weighted.py'
if not source.exists():
    source = root.parents[2] / 'src/enterprise_math/brc_weighted.py'
raw = source.read_bytes()
blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
assert blob == '3f205696709e847909958a153f8fe10d3f6b70f0'
tree = ast.parse(raw.decode())
assert [n.module for n in tree.body if isinstance(n,ast.ImportFrom) and n.level] == ['brc_logarithm','exact_arithmetic']
tree.body = [n for n in tree.body if not (isinstance(n,ast.ImportFrom) and n.level)]
m = types.ModuleType('pinned_u1_brc'); sys.modules[m.__name__] = m
exec(compile(tree,str(source),'exec'),m.__dict__)

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def total(states):
    value = m.CWM_ZERO
    for s in states:
        value = m.cwm_recoalesce(value,s)
    return value

lam = Q(1,48)
step = m.cwm_edge(lam)
steps = tuple(tuple(sign if k==j else 0 for k in range(6)) for j in range(6) for sign in (1,-1))
origin = (0,)*6
axis1 = steps[0]
layers = [{origin:m.CWM_ONE}]
for depth in range(1,9):
    nxt = {}
    for point,state in layers[-1].items():
        for delta in steps:
            target = add(point,delta)
            incoming = m.cwm_propagate(state,step)
            nxt[target] = m.cwm_recoalesce(nxt.get(target,m.CWM_ZERO),incoming)
    layers.append(nxt)

# Other-source arrivals: distinct signed ports remain distinct.
cross = {}
for j in range(6):
    for k,sign in enumerate((1,-1)):
        point = sub(steps[2*j+k],axis1)
        family = total(layer.get(point,m.CWM_ZERO) for layer in layers)
        cross[j,sign] = m.cwm_propagate(family,step)
C = total(cross.values())
# Self-return source remains a separate term; every neighbor has G(e1).
self_port = m.cwm_propagate(C,step)
full = {key:m.cwm_recoalesce(value,self_port) for key,value in cross.items()}
axis = [total([full[j,1],full[j,-1]]) for j in range(6)]
a,b = axis[0].total,axis[1].total
assert all(axis[j]==axis[1] for j in range(1,6))
T = total(axis).total
assert T == (1+12*lam)*C.total
D = a-5*b/2
tau = 2*D/3
loop = m.one_state_recurrent_cwm([m.cwm_propagate(step,step).total]*144)
assert loop.total_mass_stable
E = m.cwm_propagate(step,loop.depth(5)).total*loop.total_mass_closure
assert E == Q(1,47185920)
D_bounds = (D-(Q(1,2)+3*lam)*E,D+(1-3*lam)*E)
tau_bounds = (tau-(Q(1,3)+2*lam)*E,tau+(Q(2,3)-2*lam)*E)
a0 = total([cross[0,1],cross[0,-1]]).total
ratio_bounds = tuple((v+2*lam)/(1+12*lam)-Q(1,3) for v in
                    (a0/(C.total+E),(a0+E)/(C.total+E)))
assert D_bounds == (Q(19576426714339,1001929970810880),Q(3915291712967,200385994162176))
assert tau_bounds == (Q(19576426714339,1502894956216320),Q(3915291712967,300578991243264))
assert ratio_bounds == (Q(19576426714339,39711089792070),Q(3915291712967,7942217958414))

# A relaxed incidence certificate; not native signed triad validity.
triples = list(combinations(range(1,6),2))
usage = [Q(0)]*6
leg = m.cwm_propagate(axis[1],m.cwm_edge(Q(1,4)))
for j,k in triples:
    for i in (0,j,k):
        usage[i] += leg.total
assert usage == [5*b/2,b,b,b,b,b] and a-usage[0] == D
turned = m.cwm_propagate(axis[0],m.cwm_edge(tau/a))
kept = m.cwm_propagate(axis[0],m.cwm_edge(1-tau/a))
share = m.cwm_propagate(turned,m.cwm_edge(Q(1,5)))
repaired = [kept]+[m.cwm_recoalesce(axis[j],share) for j in range(1,6)]
assert [v.total for v in repaired] == [T/3]+[2*T/15]*5
assert total(repaired).total == T
repair_leg = m.cwm_propagate(total(axis),m.cwm_edge(Q(1,30)))
assert 10*repair_leg.total == T/3 and 4*repair_leg.total == 2*T/15

# Same coarse CWM/drive, different joint distinct-axis packet feasibility.
P = [(0,1)]*4+[(0,-1)]*2
QQ = [(0,1),(0,1),(1,1),(1,-1),(2,1),(2,-1)]
weight = m.cwm_edge(Q(1,2))
def coarse(labels):
    return (total(weight for _ in labels),tuple(
        total(weight for axis,s in labels if axis==j and s==1).total-
        total(weight for axis,s in labels if axis==j and s==-1).total for j in range(6)))
assert coarse(P)==coarse(QQ)
assert not any(len({P[i][0] for i in tri})==3 for tri in combinations(range(6),3))
cover = [(0,2,4),(1,3,5)]
assert sorted(i for tri in cover for i in tri)==list(range(6))
assert all(len({QQ[i][0] for i in tri})==3 for tri in cover)
print(json.dumps({'status':'EXACT_SAME_AUTHOR_REPLAY_NOT_NATIVE_DYNAMICS',
 'source_blob':blob,'lambda':str(lam),'D_bounds':list(map(str,D_bounds)),
 'tau_bounds':list(map(str,tau_bounds)),'tau_over_T_bounds':list(map(str,ratio_bounds)),
 'omitted_cross_path_budget_bound':str(E),'self_return_retained':True,
 'positions_solved':False,'prime_claim':False},indent=2))
