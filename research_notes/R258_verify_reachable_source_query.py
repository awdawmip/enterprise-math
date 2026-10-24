#!/usr/bin/env python3
"""Exact positive-BRC labelled-path observer: finite-control affine carrier x 00-query DFA.
Author-side auxiliary model ONLY; not native heartbeat update, R193 mapping or formal Result.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import product
from math import comb
import json

# Each branch is (next_nonspatial_control, six-axis linear holonomy sign, native-axis-1 offset).
# The sign flips both axes 1 and 2; remaining four axes fixed; P000 stays six spatial + one time.
EDGES = (
    ((2,-1,-1),(2,1,-1)),
    ((0,-1,-1),(0,1,-1)),
    ((1,1,1),(2,1,-1)),
)
# Automaton 0: has not seen 00, previous selector 1 or empty;
# 1: has not seen 00, previous selector 0; 2: has seen 00, absorbing.
DFA = ((1,0),(2,0),(2,2))

def advance(state, selector):
    q,sign,shift,query=state
    target,eta,b=EDGES[q][selector]
    return (target,eta*sign,eta*shift+b,DFA[query][selector])

def observer(state):return state[:3]

def run_word(word, source=0):
    state=(source,1,0,0)
    for a in word:state=advance(state,int(a))
    return state

def forward(max_depth,source=0):
    current={(source,1,0,0):1}
    for depth in range(max_depth+1):
        yield depth,current
        nxt=defaultdict(int)
        for st,v in current.items():
            for a in (0,1):nxt[advance(st,a)]+=v
        current=dict(nxt)

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def signature(states):
    result=defaultdict(lambda:[0,0,0])
    for (q,e,k,r),c in states.items():result[(q,e,k)][r]+=c
    return {o:tuple(v) for o,v in result.items()}

def main():
    selected=(0,1,2,3,4,5,6,7,8,12,24,48,64,96)
    recs={}
    exact_cases=0
    final_states=None
    for depth,states in forward(96):
        total=sum(states.values())
        no_00=sum(cnt for (q,e,k,r),cnt in states.items() if r!=2)
        yes_00=total-no_00
        assert total==1<<depth,(depth,'mass')
        assert no_00==fib(depth+2),(depth,'Fibonacci')
        assert all(c>0 and e in (-1,1) and abs(k)<=depth for (q,e,k,r),c in states.items())
        if depth<=12:
            direct=defaultdict(int)
            for bits in product((0,1),repeat=depth):
                word=''.join(map(str,bits))
                direct[run_word(word)]+=1
                exact_cases+=1
            assert dict(direct)==states,(depth,'all-paths')
        if depth in selected:
            sig=signature(states)
            mixed=sum((v[2]>0 and (v[0]>0 or v[1]>0)) for v in sig.values())
            triples=sum(all(v) for v in sig.values())
            recs[depth]={
                'all_paths':str(total),'yes_contains_00':str(yes_00),
                'no_contains_00':str(no_00),'product_atoms':len(states),
                'unmarked_affine_terminal_atoms':len(sig),
                'fibers_with_yes_and_no':mixed,'fibers_with_all_3_online_states':triples,
            }
        if depth==96:final_states=states
    # Two initially indistinguishable effects in a fiber, one satisfies query and one not.
    first=('000','101')
    pair=[run_word(w) for w in first]
    assert pair[0][:3]==pair[1][:3]==(0,1,-1)
    assert pair[0][3]==2 and pair[1][3]==0
    for suffix_len in range(30):
        a,b=(run_word(w+'1'*suffix_len) for w in first)
        assert a[:3]==b[:3] and a[3]==2 and b[3]==0
    # At depth seven, three pairwise future distinguishable DFA states share same exact observer atom.
    three=('1110101','1011010','0000000')
    triple=[run_word(w) for w in three]
    assert {st[:3] for st in triple}=={(2,-1,1)}
    assert [st[3] for st in triple]==[0,1,2]
    assert run_word(three[0]+'0')[:3]==run_word(three[1]+'0')[:3]
    assert [run_word(three[0]+'0')[3],run_word(three[1]+'0')[3]]==[1,2]
    # Moore automaton partition refinement: equal future accepted/rejected for all suffix words.
    part=[int(r==2) for r in range(3)]
    trace=[tuple(part)]
    while True:
        sig=[(part[r],part[DFA[r][0]],part[DFA[r][1]]) for r in range(3)]
        lab={};p=[]
        for s in sig:
            if s not in lab:lab[s]=len(lab)
            p.append(lab[s])
        trace.append(tuple(p))
        if len(set(p))==len(set(part)):
            break
        part=p
    assert len(set(part))==3 or len(set(p))==3
    report={
      'schema':'EM_R256_AUTHOR_EXACT_CHECK_V1',
      'model':'formal_positive_3control_2edge_X6_affine_then + deterministic_contains_00_provenance_DFA',
      'native_heartbeat_legal_update_verified':False,
      'actual_R193_source_observer_frozen':False,
      'python_exhaustive_source_word_checks':exact_cases,
      'depth_0_to_96_Fibonacci_and_positive_mass_checks':'PASS',
      'witness_first_mixed_fiber':{'depth':3,'words':list(first),'O':[0,1,-1],'query_states':[2,0]},
      'witness_three_future_distinguishable_states':{'depth':7,'words':list(three),'O':[2,-1,1],'query_states':[0,1,2]},
      'selected_depths':{str(k):v for k,v in recs.items()},
      'verification_limits':'All-path enumeration only through 12; all-depth claims follow induction/automata right congruence. No original Enterprise Math Python module executed.'
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()


# R258 extension: seven reachable product controls, with all-suffix Moore minimality.
# Reuse the exact R256 auxiliary forward() and EDGES/DFA data above.
# Author-side exact code: NOT an original enterprise_math package import.
def r258_check():
    from collections import deque
    initial=(0,0)
    def step(s,a):
        q,r=s
        return (EDGES[q][a][0],DFA[r][a])
    words={initial:''}
    todo=deque([initial])
    while todo:
        st=todo.popleft()
        for a in (0,1):
            t=step(st,a)
            if t not in words:
                words[t]=words[st]+str(a)
                todo.append(t)
    expected={(0,0),(2,1),(2,0),(1,2),(1,1),(0,2),(2,2)}
    assert set(words)==expected
    assert ({(q,r) for q in range(3) for r in range(3)}-expected)=={(0,1),(1,0)}
    transitions={(q,r):(step((q,r),0),step((q,r),1)) for (q,r) in expected}
    assert all(v in expected for ts in transitions.values() for v in ts)
    def output(s):return (s[0],int(s[1]==2))
    pairs=0
    ordered=sorted(expected)
    for i,st in enumerate(ordered):
        for t in ordered[i+1:]:
            assert output(st)!=output(t) or any(output(step(st,a))!=output(step(t,a)) for a in (0,1))
            pairs+=1
    assert pairs==21
    max_depth=96
    for depth, states in forward(max_depth):
        assert all((q,r) in expected for (q,eta,k,r) in states)
    witnesses=('1110101','1011010','0000000')
    end_states=[run_word(w) for w in witnesses]
    assert {s[:3] for s in end_states}=={(2,-1,1)}
    assert [s[3] for s in end_states]==[0,1,2]
    import json
    print(json.dumps({'R258':'PASS','reachable_product_controls':7,
      'unreachable':[[0,1],[1,0]], 'pairwise_future_distinguished':pairs,
      'joint_exact_model_depth_checked':max_depth,
      'control_model':'reachable finite Moore (q,g(r)), NOT effect-aware optimality',
      'native_source_module_executed':False,
      'R193_contract_verified':False},sort_keys=True))

if __name__=='__main__':
    r258_check()
