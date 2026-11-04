#!/usr/bin/env python3
"""Exact reachable KMP x first-source horizon quotient certificate; Python standard library."""
import itertools
import json
from collections import deque
ALPHABET='aAbBcCdDeE'
GATES=('aab','aba')
def step(gate,state,letter):
    q,tag=state
    text=gate[:q]+letter
    k=next(k for k in range(len(gate),-1,-1) if text.endswith(gate[:k]))
    if tag=='N':
        if letter in 'bB': tag='B'
        elif letter in 'cC': tag='C'
    return k,tag
def machine(gate):
    initial=(0,'N'); path={initial:''}; todo=deque([initial])
    while todo:
        st=todo.popleft()
        for x in ALPHABET:
            dest=step(gate,st,x)
            if dest not in path:
                path[dest]=path[st]+x;todo.append(dest)
    return sorted(path),path
def output(gate,st,observer):
    q,tag=st
    if observer=='q_firstB':return q,tag=='B'
    if observer=='accept_firstB':return q==len(gate),tag=='B'
    if observer=='firstB':return tag=='B'
    if observer=='accept':return q==len(gate)
    if observer=='q_fulltag':return st
    raise ValueError(observer)
def signatures(gate,states,observer,H):
    s={st:(output(gate,st,observer),) for st in states}
    def partition(x):
        groups={}
        for st in states: groups.setdefault(x[st],[]).append(st)
        return [sorted(v) for v in groups.values()]
    history=[partition(s)]
    for _ in range(H):
        s={st:(output(gate,st,observer),tuple(s[step(gate,st,ch)] for ch in ALPHABET)) for st in states}
        history.append(partition(s))
    return history
def witness(gate,s,t,observer,max_len=7):
    if output(gate,s,observer)!=output(gate,t,observer):return ''
    todo=deque([(s,t,'')]);seen={(s,t)}
    while todo:
        a,b,w=todo.popleft()
        if len(w)==max_len:continue
        for x in ALPHABET:
            aa,bb=step(gate,a,x),step(gate,b,x)
            if output(gate,aa,observer)!=output(gate,bb,observer):return w+x
            if (aa,bb) not in seen:seen.add((aa,bb));todo.append((aa,bb,w+x))
    return None
def run():
    data={}
    for g in GATES:
        states,paths=machine(g)
        assert len(states)=={'aab':11,'aba':10}[g]
        assert all(step(g,s,ch) in set(states) for s in states for ch in ALPHABET)
        result={'states':[str(s) for s in states],'reachability':{str(s):paths[s] for s in states}}
        for obs in ('q_fulltag','q_firstB','accept_firstB','firstB','accept'):
            parts=signatures(g,states,obs,7)
            sizes=[len(p) for p in parts]
            assert sizes[-1]==sizes[-2],(g,obs,sizes)
            checked=0
            for s,t in itertools.combinations(states,2):
                first=next((h for h,p in enumerate(parts) if any((s in c)!=(t in c) for c in p)),None)
                w=witness(g,s,t,obs,7)
                if first is None: assert w is None
                else: assert w is not None and len(w)==first,(g,obs,s,t,first,w)
                checked+=1
            result[obs]={'horizon_counts':sizes,'pairs_checked':checked}
        data[g]=result
    data['status']='ALL_CHECKS_PASS'
    return data
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
