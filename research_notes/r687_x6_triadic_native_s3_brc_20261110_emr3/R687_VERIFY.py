#!/usr/bin/env python3
"""R687 exact checker: X6 signed-axis triadic candidate, S3 holonomy and BRC."""
import json
from itertools import combinations, permutations, product
from math import factorial
from collections import Counter
from fractions import Fraction
from pathlib import Path

N=6
TRIADS=tuple(combinations(range(6),3))
ID=(0,1,2)
TABLE={
 (0,0):(0,1,2), (1,0):(0,1,3), (2,0):(0,1,4),
 (0,1):(0,2,3), (1,1):(1,2,3), (2,1):(0,1,3),
}
def triad(z):
    return TABLE[(sum(z[i] for i in (0,2,4))%3,
                  sum(z[i] for i in (1,3,5))%2)]
def edge(z,axis,sign):
    v=list(z); v[axis]+=sign
    return tuple(v)
def adjacent(s,t):
    return len(set(s)&set(t))==2
def frame_move(frame,s,t):
    assert adjacent(s,t) and set(frame)==set(s)
    dropped=next(iter(set(s)-set(t)))
    added=next(iter(set(t)-set(s)))
    return tuple(added if a==dropped else a for a in frame)
def permutation_product(q,p):
    return tuple(q[i] for i in p)
def holonomy(path):
    zs=(0,)*N
    f=triad(zs)
    assert f==ID
    for axis,sgn in path:
        ns=edge(zs,axis,sgn)
        f=frame_move(f,triad(zs),triad(ns))
        zs=ns
    assert zs==(0,)*N and triad(zs)==ID
    return f
PLUS=((0,1),(1,1),(0,-1),(1,-1))
MINUS=((0,-1),(1,1),(0,1),(1,-1))
def sigma_action_tuple(x,sigma):
    out=[None]*N
    for old,new in enumerate(sigma): out[new]=x[old]
    return tuple(out)
def sigma_labels(labels,sigma):
    return tuple(sigma[i] for i in labels)
def closure_candidate(labels,q,incidence):
    """E*: positive equal three distinct native-axis quanta plus a directed 3-cycle."""
    if len(labels)!=3 or len(set(labels))!=3 or q<=0:
        return False
    if not all(0<=a<N for a in labels):
        return False
    cycle={(labels[i],labels[(i+1)%3]) for i in range(3)}
    return len(incidence)==3 and set(incidence)==cycle
def make_incidence(frame):
    return tuple((frame[i],frame[(i+1)%3]) for i in range(3))
def all_partitions_abc():
    A=('A1','A2'); B=('B1','B2'); C=('C1','C2')
    out=[]
    for b in B:
        for c in C:
            other_b=next(x for x in B if x!=b)
            other_c=next(x for x in C if x!=c)
            out.append(frozenset((
                frozenset((A[0],b,c)),
                frozenset((A[1],other_b,other_c))
            )))
    return out
def verify():
    checks=0
    for a in range(3):
        for b in range(2):
            z=[0]*6;z[0]=a;z[1]=b;z=tuple(z)
            s=triad(z)
            assert len(s)==3 and len(set(s))==3
            for axis,sign in product(range(N),(-1,1)):
                v=edge(z,axis,sign);t=triad(v)
                assert adjacent(s,t),(a,b,axis,sign,s,t)
                assert frame_move(frame_move(s,s,t),t,s)==s
                for F in permutations(s):
                    G=frame_move(F,s,t)
                    assert frame_move(G,t,s)==F
                    assert closure_candidate(F,1,make_incidence(F))
                    assert closure_candidate(G,1,make_incidence(G))
                    checks+=1
    cov=0
    generators=[]
    for k in range(N-1):
        sig=list(range(N));sig[k],sig[k+1]=sig[k+1],sig[k]
        generators.append(tuple(sig))
    for sigma in generators:
        for a,b in product(range(3),range(2)):
            z=(a,b,0,0,0,0)
            for axis,sign in product(range(N),(-1,1)):
                v=edge(z,axis,sign)
                assert sigma_action_tuple(edge(z,axis,sign),sigma)==edge(sigma_action_tuple(z,sigma),sigma[axis],sign)
                for F in permutations(triad(z)):
                    source_move=frame_move(F,triad(z),triad(v))
                    transformed_move=frame_move(sigma_labels(F,sigma),sigma_labels(triad(z),sigma),sigma_labels(triad(v),sigma))
                    assert transformed_move==sigma_labels(source_move,sigma)
                    cov+=1
    g=holonomy(PLUS);h=holonomy(MINUS)
    assert g==(2,0,1) and h==(0,2,1)
    assert permutation_product(g,g)!=ID
    assert permutation_product(g,permutation_product(g,g))==ID
    assert permutation_product(h,h)==ID
    assert permutation_product(g,h)!=permutation_product(h,g)
    generations={ID:1}
    series=[]
    for k in range(1,4):
        q=Counter()
        for F,n in generations.items():
            for gen in (g,h):q[permutation_product(gen,F)]+=n
        generations=dict(q)
        series.append({''.join(map(str,key)):val for key,val in sorted(q.items())})
    assert [len(x) for x in series]==[2,4,6]
    assert sorted(generations.values())==[1,1,1,1,2,2]
    assert sum(generations.values())==8
    parts=all_partitions_abc()
    assert len(set(parts))==4
    partition_counts={}
    for m in range(1,5):
        B=tuple(f'B{i}' for i in range(m))
        C=tuple(f'C{i}' for i in range(m))
        partitions=set()
        for pi in permutations(B):
            for tau in permutations(C):
                decomposition=frozenset(frozenset((f'A{i}',pi[i],tau[i])) for i in range(m))
                partitions.add(decomposition)
        assert len(partitions)==factorial(m)**2
        partition_counts[m]=len(partitions)
    assert closure_candidate((0,1,2),1,make_incidence((0,1,2)))
    assert closure_candidate((0,1,3),1,make_incidence((0,1,3)))
    ev={
      'schema':'R687_X6_TRIADIC_NATIVE_BRIDGE_V1',
      'native_spatial_scope':'X6 torsor over Z^6; relative chart at chosen Cell anchor',
      'source_task':'RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142',
      'frozen_task_source':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'previous_auxiliary_proof':'R686 author branch 1e25c6319dc0205d1f8ac58755ceca9f259effdf',
      'lookup_table':{f'{a},{b}':list(TABLE[a,b]) for a,b in sorted(TABLE)},
      'all_native_axis_edges_checked':6*12,
      'frame_cases_checked':checks,
      's6_generator_covariance_cases_checked':cov,
      'loop_plus':[list(x) for x in PLUS],
      'loop_minus':[list(x) for x in MINUS],
      'loop_plus_holonomy':list(g),'loop_minus_holonomy':list(h),
      'based_holonomy_subgroup_order':6,
      'equal_time_12_step_BRC_support':series[-1],
      'eight_branch_exact_weights':{k:f'{v}/8' for k,v in series[-1].items()},
      'distinct_labeled_six_force_triad_partitions':4,
      'equal_axis_class_m_labeled_partitions':{str(k):v for k,v in partition_counts.items()},
      'typed_closure_status':'EXPLICIT_CANDIDATE_E_STAR_NOT_CANONICAL_P000_DERIVATION',
      'arithmetic':'integer modular arithmetic; rational BRC weights',
      'scope':'Exact periodic 3x2 lookup and its S6 transported family; not an empirical X6 force dynamics',
      'pass_marker':'R687_X6_TRIADIC_S3_NATIVE_BRC_EXACT_PASS'
    }
    dest=Path(__file__).with_name('R687_EVIDENCE.json')
    dest.write_text(json.dumps(ev,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
    print(ev['pass_marker'])
    print('frame checks',checks,'rotation generator checks',cov,'loop holonomies',g,h)
    print('t=12 fiber',series[-1])
if __name__=='__main__':verify()
