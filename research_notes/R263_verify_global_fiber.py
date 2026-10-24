#!/usr/bin/env python3
"""Author-side exact combinatorial checker for the formal R260/R262 BRC toy model.
No claim of running native enterprise_math modules or native heartbeat dynamics.
"""
from collections import defaultdict
from itertools import product
from math import ceil
import json

EDGES = {0: ((2,-1,-1),(2,+1,-1)), 1:((0,-1,-1),(0,+1,-1)), 2:((1,+1,+1),(2,+1,-1))}
DELTA = ((1,0),(2,0),(2,2))
TARGET = ((0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2))

def transition(q,r,eps,k,a):
    t,eta,b=EDGES[q][a]
    return (t,DELTA[r][a],eta*eps,eta*k+b)

def all_words_witnesses(m):
    examples={}
    for bits in product((0,1),repeat=m):
        q=r=k=0; eps=1
        for a in bits: q,r,eps,k=transition(q,r,eps,k,a)
        key=(eps,k,q,r)
        if key not in examples: examples[key]=''.join(map(str,bits))
    fibers=defaultdict(dict)
    for (eps,k,q,r),word in examples.items(): fibers[(eps,k)][(q,r)]=word
    full=sorted((g,w) for g,w in fibers.items() if set(w)==set(TARGET))
    maxsz=max(map(len,fibers.values()))
    return full, maxsz, fibers

def compose_effect(e1,e2):
    eps,k=e1;eta,b=e2
    return eta*eps,eta*k+b

def evaluate(word):
    state=(0,0,1,0)
    for ch in word: state=transition(*state,int(ch))
    return state

def main():
    max_by_depth={}
    bases={}
    for m in range(11):
        full,best,fibers=all_words_witnesses(m)
        max_by_depth[m]=best
        if 8<=m<=10:
            assert full,(m,best)
            g,words=sorted(full,key=lambda x:(abs(x[0][1]),x[0]))[0]
            assert set(words)==set(TARGET)
            assert all(evaluate(w)==(q,r,*g) for (q,r),w in words.items())
            bases[m]={'effect':g,'witnesses':{f'{q},{r}':words[q,r] for q,r in TARGET}}
    assert all(max_by_depth[m]<=6 for m in range(8))
    assert max_by_depth[8]==7
    mass_table={}
    for m,record in bases.items():
        g=tuple(record['effect'])
        d=defaultdict(int)
        for word in product((0,1),repeat=m):
            q=r=k=0; eps=1
            for a in word:q,r,eps,k=transition(q,r,eps,k,a)
            if (eps,k)==g:d[(q,r)]+=1
        assert set(d)==set(TARGET) and all(v>0 for v in d.values())
        mass_table[m]=[d[x] for x in TARGET]
    assert mass_table=={8:[1,6,1,9,1,1,16],9:[1,19,2,20,3,1,28],10:[2,38,3,29,4,1,49]}
    reset='101'; assert evaluate(reset)==(0,0,1,-1)
    # finite stress of constructive universal statements, never replaces algebraic proof.
    for m in range(8,181):
        j=8+(m-8)%3; h=(m-j)//3
        expected_effect=(bases[j]['effect'][0],bases[j]['effect'][1]-h*bases[j]['effect'][0])
        for target,baseword in bases[j]['witnesses'].items():
            result=evaluate(reset*h+baseword)
            assert result[:2]==tuple(map(int,target.split(','))),(m,target,result)
            assert result[2:]==expected_effect,(m,target,result,expected_effect)
    data={
      'schema':'EM_R263_AUTHOR_GLOBAL_SEVENFIBER_EXACT_V1',
      'scope':'formal R260/R262 positive binary choice six-slot affine toy BRC, nonnative',
      'target_states':TARGET,
      'max_joint_states_inside_one_effect_fiber_by_depth_0_to_10':max_by_depth,
      'first_full_fiber_depth':8,
      'three_base_fibers':bases,
      'fiber_multiplicity_vectors':mass_table,
      'common_reset_word':'101',
      'common_reset_effect':(1,-1),
      'universal_effect_formula':'m=j+3h, j in {8,9,10}; (eps_j,k_j - eps_j*h)',
      'finite_stress_to_length':180,
      'status':'PASS',
      'not_proven_by_computation':['universality for arbitrary length (proved by prefix-composition algebra)','native P000 heartbeat update correspondence','R193 actual source/time-port','native Source module execution','formal Result/Driver admission'],
    }
    print(json.dumps(data,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
