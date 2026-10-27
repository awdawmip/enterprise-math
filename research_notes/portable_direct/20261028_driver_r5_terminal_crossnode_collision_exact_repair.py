#!/usr/bin/env python3
"""Nonblind exact R5 collision audit. Not a native Driver review."""
from fractions import Fraction as F
from itertools import product
import json

alpha, beta = F(1,10), F(3,4)
lam = (F(20), F(10), F(-2), F(3))
roots = {'A':(F(1,2),F(1,2)), 'B':(F(1,2),F(3,2))}
q = {'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
r = {'AU':F(1),'AV':F(1,4),'BU':F(1),'BV':F(2)}
eps = {'AU':alpha,'AV':F(0),'BU':beta,'BV':F(0)}

def stop(mass, lr, t, declaration):
    return (mass*lr if declaration=='Q' else F(0),
            mass if declaration=='P' else F(0),mass*lr*t,mass*t)

def add(*vals):
    return tuple(sum(v[i] for v in vals) for i in range(4))

def score(v):
    return sum(lam[i]*v[i] for i in range(4))

terminal = {(n,j):r[n]*(1+eps[n]*(2*j-1)) for n in r for j in (0,1)}
classes={}
for key, ratio in terminal.items():classes.setdefault(ratio,[]).append(key)
assert len(classes)==5 and classes[F(1,4)]==[('AV',0),('AV',1),('BU',0)]
assert set(classes.keys())=={F(1,4),F(9,10),F(11,10),F(7,4),F(2)}

# All terminal histories at the same (t,R) use ONE deterministic action.
vectors=set(); best=None; best_policy=None
for topA,topB,shared,gateAV,gateBV in product('PQC',repeat=5):
    for labels in product('PQ',repeat=len(classes)):
        terminal_action=dict(zip(classes,labels))
        vals={}
        for n in q:
            gate={'AU':shared,'BU':shared,'AV':gateAV,'BV':gateBV}[n]
            if gate!='C': vals[n]=stop(q[n],r[n],2,gate)
            else: vals[n]=add(*[stop(q[n]/2,terminal[(n,j)],3,terminal_action[terminal[(n,j)]]) for j in (0,1)])
        a=stop(*roots['A'],1,topA) if topA!='C' else add(vals['AU'],vals['AV'])
        b=stop(*roots['B'],1,topB) if topB!='C' else add(vals['BU'],vals['BV'])
        v=add(a,b)
        vectors.add(v)
        cost=score(v)
        if best is None or cost<best:
            best=cost; best_policy=(topA,topB,shared,gateAV,gateBV,labels)

def node_cost(n,action):
    if action in 'PQ':return score(stop(q[n],r[n],2,action))
    return sum(min(score(stop(q[n]/2,terminal[(n,j)],3,a)) for a in 'PQ') for j in (0,1))

full_by_root={}
for root in roots:
    stop_costs=[score(stop(*roots[root],1,a)) for a in 'PQ']
    nodes_cost=sum(min(node_cost(n,act) for act in 'PQC') for n in q if n.startswith(root))
    full_by_root[root]=min(*stop_costs,nodes_cost)
full=sum(full_by_root.values())
assert full==F(233,24),(full,full_by_root)
assert best==F(79,8),(best,best_policy)
assert best-full==F(1,6)
q_av=F(1,3); q_bu0=F(1,8)
prob_Q=q_av/(q_av+q_bu0)
assert prob_Q==F(8,11)
old=add(stop(q_av,F(1,4),3,'Q'),stop(q_bu0,F(1,4),3,'P'))
new=tuple(prob_Q*stop(q_av+q_bu0,F(1,4),3,'Q')[i]+(1-prob_Q)*stop(q_av+q_bu0,F(1,4),3,'P')[i] for i in range(4))
assert old==new
out={'audit':'NONBLIND_UNREVIEWED_NOT_ADMITTED','alpha':str(alpha),'beta':str(beta),
     'terminal_ratio_classes':{str(v):[list(k) for k in ks] for v,ks in sorted(classes.items())},
     'valid_seedless_deterministic_points':len(vectors),'seedless_min':str(best),
     'full_history_min':str(full),'support_gap':str(best-full),
     'full_root_minima':{k:str(v) for k,v in full_by_root.items()},
     'example_terminal_common_Q_probability':str(prob_Q),
     'terminal_repair_old_observation':[str(x) for x in old],
     'terminal_repair_new_observation':[str(x) for x in new]}
print(json.dumps(out,ensure_ascii=False,indent=2))
