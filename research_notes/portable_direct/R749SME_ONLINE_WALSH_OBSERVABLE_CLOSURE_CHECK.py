#!/usr/bin/env python3
"""Exact five-mode finite-controller Walsh observable closure checker (R749SME).
Only the declared historical signed-Port controller is modeled, not native events.
"""
from fractions import Fraction as F
import json

D=3
N=1<<D
ONE=tuple(F(int(i==0)) for i in range(N))
MODES=['root','plus','minus','joint','fair']
VECTORS={'root':1,'plus':2,'minus':4,'joint':6,'fair':None}
EDGES={
  'root':{'plus':'plus','minus':'minus'},
  'plus':{'plus':'joint','minus':'joint'},
  'minus':{'plus':'joint','minus':'joint'},
  'joint':{'plus':'fair','minus':'fair'},
  'fair':{'plus':'fair','minus':'fair'}
}

def apply(v,word,sign):
    if v is None: return tuple(x/2 for x in word)
    return tuple(word[i]/2+F(sign,4)*word[i^v] for i in range(N))

def reduced_basis(rows):
    out=[]
    for row in rows:
        row=list(row)
        for pivot,vec in out:
            if row[pivot]:
                q=row[pivot]
                row=[a-q*b for a,b in zip(row,vec)]
        pivot=next((i for i,a in enumerate(row) if a),None)
        if pivot is None: continue
        q=row[pivot]
        row=[x/q for x in row]
        for k,(old_p,old) in enumerate(out):
            if old[pivot]:
                q=old[pivot]
                out[k]=(old_p,[x-q*y for x,y in zip(old,row)])
        out.append((pivot,row))
        out.sort(key=lambda x:x[0])
    return [tuple(v) for _,v in out]

spaces={m:[ONE] for m in MODES}
history=[]
for h in range(40):
    history.append({m:len(spaces[m]) for m in MODES})
    nxt={}
    for m in MODES:
        rows=[ONE]
        for a,sign in [('plus',1),('minus',-1)]:
            for v in spaces[EDGES[m][a]]:
                rows.append(apply(VECTORS[m],v,sign))
        nxt[m]=reduced_basis(rows)
    if all(len(nxt[m])==len(spaces[m]) for m in MODES):
        stabilized_at=h
        break
    spaces=nxt
else: raise AssertionError('no stabilization')

assert stabilized_at==3
assert [x['root'] for x in history]==[1,2,4,8]
assert {m:len(spaces[m]) for m in MODES}=={
  'root':8,'plus':4,'minus':4,'joint':2,'fair':1}
assert stabilized_at<=len(MODES)*(N-1)

print(json.dumps({
  'status':'PASS','arithmetic':'exact Fraction',
  'source_bits':D,'source_histories':N,'controller_states':len(MODES),
  'root_horizon_ranks':[x['root'] for x in history],
  'stabilized_horizon':stabilized_at,
  'fixed_point_state_ranks':{m:len(spaces[m]) for m in MODES},
  'minimal_root_affine_coordinates':len(spaces['root'])-1,
  'theoretical_global_iteration_bound':len(MODES)*(N-1)+1,
  'native_event_permission':'NOT_CHECKED'
},indent=2))
