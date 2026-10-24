#!/usr/bin/env python3
"""R254 independent compact exact-integer BRC fiber-and-DAG reproducer.
Uses declared three-control/two-edge auxiliary model, not enterprise_math import.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb
import json

edges={0:((2,-1,-1),(2,1,-1)),
       1:((0,-1,-1),(0,1,-1)),
       2:((1,1,1),(2,1,-1))}

def move(state,selector):
    q,eps,p=state
    target,eta,b=edges[q][selector]
    neweps=eps*eta
    return target,neweps,p-neweps*b

def counted_step(hist):
    out=Counter()
    for state,c in hist.items():
        for i in (0,1):out[move(state,i)]+=c
    return out

def ordered_state(start,word):
    state=(start,1,0)
    for i in word:state=move(state,i)
    return state

class SharedExpression:
    def __init__(self,start):
        self.nodes=[('unit',)]
        self.rows=[{start:0}]
    def step(self):
        terms={q:[] for q in edges}
        for q,old in self.rows[-1].items():
            for i,(dst,_,_) in enumerate(edges[q]):
                term=len(self.nodes)
                self.nodes.append(('append',old,q,i))
                terms[dst].append(term)
        new={}
        for dst,arr in terms.items():
            if arr:
                num=len(self.nodes)
                self.nodes.append(('sum',tuple(arr)))
                new[dst]=num
        self.rows.append(new)
    @lru_cache(None)
    def words(self,node):
        a=self.nodes[node]
        if a[0]=='unit':return ((),)
        if a[0]=='append':return tuple(w+((a[2],a[3]),) for w in self.words(a[1]))
        return tuple(w for ch in a[1] for w in self.words(ch))


def run():
    h={i:Counter({(i,1,0):1}) for i in (0,1)}
    chosen=(3,12,24,48,64,96)
    sample=[]
    for m in range(97):
        for src,dist in h.items():
            assert sum(dist.values())==2**m
            marginal=Counter()
            for (q,eps,p),v in dist.items():marginal[p]+=v
            assert marginal==Counter({p:comb(m,(m+p)//2) for p in range(-m,m+1,2)})
            central=comb(m,m//2)
            maximum=max(dist.values())
            assert (central+5)//6<=maximum<=central
            if m<=12:
                exact=Counter(ordered_state(src,w) for w in product((0,1),repeat=m))
                assert exact==dist
            if src==0 and m in chosen:
                sample.append((m,str(maximum),(maximum-1).bit_length()))
        if m<96:h={src:counted_step(dist) for src,dist in h.items()}
    dag_check=[]
    for start in (0,1):
        d=SharedExpression(start)
        for m in range(65):
            assert len(d.nodes)<=1+9*m
            if m<=11:
                obs=Counter()
                for target,node in d.rows[m].items():
                    for labeled in d.words(node):
                        q=start;selectors=[]
                        for source,i in labeled:
                            assert source==q
                            q=edges[q][i][0]
                            selectors.append(i)
                        assert q==target
                        obs[ordered_state(start,selectors)]+=1
                assert obs==Counter(ordered_state(start,w) for w in product((0,1),repeat=m))
            if m==64:dag_check.append((start,len(d.nodes)))
            if m<64:d.step()
    assert ordered_state(0,(0,0,0))==ordered_state(0,(1,0,1))==(0,1,1)
    return {'status':'PASS','horizons':'0..96','selected':[list(i) for i in sample],
            'dag_nodes_at_64':dag_check,'source_effect':'SIX_AXIS_FORMAL_AFFINE',
            'native_import_executed':False}

if __name__=='__main__':print(json.dumps(run(),sort_keys=True))
