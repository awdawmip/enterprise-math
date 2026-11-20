"""R60: exhaustive exact finite 0/1 positive-BRC branch enumeration.
No physical evolution, amplitude cancellation or external analytic propagation.
"""
from itertools import permutations
from collections import defaultdict
import json

def matmul(A,B):
    p=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(p)) for j in range(p)] for i in range(p)]

def trace_prefix(S):
    p=len(S); power=S; out=[]
    for _ in range(p):
        out.append(sum(power[i][i] for i in range(p)))
        power=matmul(power,S)
    return tuple(out)

def flat_to_mat(bits,p):
    return [list(bits[i*p:(i+1)*p]) for i in range(p)]

def relabel(bits,p,permutation):
    return tuple(bits[permutation[i]*p+permutation[j]] for i in range(p) for j in range(p))

def orbit(bits,p):
    return {relabel(bits,p,perm) for perm in permutations(range(p))}

def total_and_degree_signature(S):
    p=len(S)
    C=[[1-S[i][j] for j in range(p)] for i in range(p)]
    m=sum(map(sum,C))
    out=tuple(sorted(map(sum,C)))
    indeg=tuple(sorted(sum(C[i][j] for i in range(p)) for j in range(p)))
    return (m,trace_prefix(S),out,indeg)

def marked_positive_mass(S):
    # Two independent AB successes: (i,j) and (i,i), with a shared label i.
    return sum(sum(S[i][j] for j in range(len(S)))*S[i][i] for i in range(len(S)))

def positive_pattern_mass(template,S):
    p=len(S)
    edges=[(i,j) for i in range(p) for j in range(p) if template[i][j]==1]
    return sum(all(S[perm[i]][perm[j]] for i,j in edges)
               for perm in permutations(range(p)))

def check(p):
    permutations_list=list(permutations(range(p)))
    seen={}; signature_collisions=0; min_signature_counterexample=None
    graph_count=0; orbit_representatives=set()
    for mask in range(1<<(p*p)):
        bits=tuple((mask>>a)&1 for a in range(p*p))
        S=flat_to_mat(bits,p)
        signature=total_and_degree_signature(S)
        key=min(relabel(bits,p,perm) for perm in permutations_list)
        graph_count+=1
        orbit_representatives.add(key)
        if signature in seen and seen[signature][0]!=key:
            signature_collisions+=1
            if min_signature_counterexample is None:
                min_signature_counterexample=(seen[signature][1],bits)
        else:
            seen.setdefault(signature,(key,bits))
        for perm in permutations_list:
            assert len(relabel(bits,p,perm))==p*p
        assert positive_pattern_mass(S,S)>0
    return {'p':p,'labelled_graphs':graph_count,
            'simultaneous_relabel_orbits':len(orbit_representatives),
            'signature_collisions':signature_collisions,
            'first_collision_found':min_signature_counterexample is not None}

def main():
    results=[check(p) for p in range(1,4)]
    A=[[1,0,0],[1,0,1],[1,1,1]]
    B=[[0,1,0],[1,1,0],[1,1,1]]
    p=3
    assert total_and_degree_signature(A)==total_and_degree_signature(B)
    assert trace_prefix(A)==(2,4,5)
    assert orbit(tuple(sum(A,[])),p).isdisjoint(orbit(tuple(sum(B,[])),p))
    assert marked_positive_mass(A)==4 and marked_positive_mass(B)==5
    assert positive_pattern_mass(A,A)>0 and positive_pattern_mass(A,B)==0
    for p in range(1,4):
        bits_by_edges=defaultdict(list)
        for mask in range(1<<(p*p)):
            bits=tuple((mask>>a)&1 for a in range(p*p))
            bits_by_edges[sum(bits)].append(bits)
        for m,members in bits_by_edges.items():
            reps={min(orbit(bits,p)) for bits in members}
            for F in reps:
                matF=flat_to_mat(F,p)
                for G in reps:
                    value=positive_pattern_mass(matF,flat_to_mat(G,p))
                    assert (value>0)==(F==G), (p,m,F,G,value)
    data={'schema':'ENTERPRISE_MATH_X6_R60_POSITIVE_BRC_GRAPH_TOMOGRAPHY_V1',
          'status':'PASS','arithmetic':'integer positive branch counts',
          'sizes':results,'witness':{
            'p':3,'success_A':A,'success_B':B,
            'blocked_edges_A':[[0,1],[0,2],[1,1]],
            'blocked_edges_B':[[0,0],[0,2],[1,2]],
            'forbidden_edge_count':3,'trace_prefix':[2,4,5],
            'characteristic_polynomial':'lambda^3-2lambda^2+1',
            'blocked_out_degree_sorted':[0,1,2],
            'blocked_in_degree_sorted':[0,1,2],
            'marked_positive_two_trial_A':4,
            'marked_positive_two_trial_B':5,
            'spanning_pattern_mass_on_A_positive':True,
            'spanning_pattern_mass_on_B_zero':True},
          'model':'conditional typed positive-BRC 0/1 success events with stable simultaneous Port labels across reset replicates; no physical/native time claim',
          'verification':'p=1..3 exhaustive labelled binary relation enumeration and orbit class tests; symbolic general proof of positive template completeness'}
    print(json.dumps(data,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
