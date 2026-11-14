"""SciPy/HiGHS 0-1 native-prefix tree crosscheck for EC49EXG.
This reported MIP optimum is separate from the exact integer trie lower-bound proof.
Requires NumPy/SciPy; VERIFY_EC49EXG.py is standard-library only.
"""
import json
from collections import defaultdict
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
from VERIFY_EC49EXG import O,T,K,W,fiber,steps

parent=[-1];children=[{}];terminal=defaultdict(list);node_word={}
for h in range(2,9):
    for word,st,s in fiber(h,K[h]):
        v=0
        for t in st:
            if t not in children[v]:
                children[v][t]=len(parent);parent.append(v);children.append({})
            v=children[v][t]
        c=4*(h-2)+T.index(s);terminal[c].append(v);node_word[v]=word
N=len(parent);assert N==23887 and len(terminal)==28
baseline=set()
for w in W[2]:
    v=0
    for t in steps(w):
        v=children[v][t];baseline.add(v)
assert len(baseline)==28
row=[];col=[];val=[];lower=[];upper=[]
for v in range(1,N):
    r=len(lower);row.extend((r,r));col.extend((v,parent[v]));val.extend((1.,-1.))
    lower.append(-np.inf);upper.append(0.)
for color in range(28):
    r=len(lower)
    for v in set(terminal[color]):row.append(r);col.append(v);val.append(1.)
    lower.append(1.);upper.append(np.inf)
A=coo_matrix((val,(row,col)),shape=(len(lower),N)).tocsr()
cost=np.ones(N);cost[0]=0.;cost[list(baseline)]=0.
lo=np.zeros(N);hi=np.ones(N);lo[0]=1.;lo[list(baseline)]=1.
result=milp(c=cost,integrality=np.ones(N),bounds=Bounds(lo,hi),
    constraints=LinearConstraint(A,lower,upper),
    options={'mip_rel_gap':0.,'time_limit':180.})
assert result.status==0 and result.mip_gap==0
assert int(round(result.fun))==int(round(result.mip_dual_bound))==116
selected={}
for color in range(28):
    choices=[node_word[v] for v in terminal[color] if result.x[v]>.5]
    assert len(choices)==1
    selected[f'h{color//4+2}_T{color%4}']=choices[0]
paid=set()
for word in selected.values():
    st=steps(word);paid.update(st[:i] for i in range(1,len(st)+1))
assert len(paid)==144
print(json.dumps({'status':'PASS','solver':'SciPy-HiGHS_MILP','trie_nodes':N,
    'colors':28,'objective_extra':116,'baseline':28,'E':144,
    'reported_dual_bound':144,'reported_gap':0,'witness':selected},indent=2))
