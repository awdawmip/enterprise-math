#!/usr/bin/env python3
"""EC46 exact BRC two-observation private-memory classifier verification.
All arithmetic uses integers or fractions. Does not simulate X6/heartbeat dynamics.
"""
from itertools import product, combinations
from fractions import Fraction
import json


def compositions(n, k):
    if k == 1:
        if n >= 1:
            yield (n,)
    else:
        for a in range(1, n-k+2):
            for rest in compositions(n-a, k-1):
                yield (a,) + rest


def score_assignment(a, b, assignment):
    r = len(a); y_count = len(a[0]); assert len(b) == r
    return sum(min(sum(a[h][y] for h in range(r) if assignment[h] == c),
                   sum(b[h][y] for h in range(r) if assignment[h] == c))
               for c in set(assignment) for y in range(y_count))


def best_partition(a, b, k):
    r = len(a)
    return min(score_assignment(a,b,t) for t in product(range(k),repeat=r))


def graph(a,b):
    r=len(a); y_count=len(a[0]); edges=[]
    for h,k in combinations(range(r),2):
        if any((a[h][y]-b[h][y])*(a[k][y]-b[k][y])<0 for y in range(y_count)):
            edges.append((h,k))
    return edges


def chromatic_number(r, edges):
    return next(k for k in range(1,r+1) if any(all(assignment[u]!=assignment[v] for u,v in edges)
                                             for assignment in product(range(k),repeat=r)))


def gap_from_abs(a,b,assignment):
    r=len(a); y_count=len(a[0])
    raw=0
    for c in set(assignment):
        for y in range(y_count):
            ds=[a[h][y]-b[h][y] for h in range(r) if assignment[h]==c]
            raw += sum(map(abs,ds)) - abs(sum(ds))
    assert raw % 2 == 0
    return raw//2


def test_model(a,b, brute=False):
    r=len(a)
    assert all(len(row)==len(a[0]) for row in a+b)
    full=sum(min(a[h][y],b[h][y]) for h in range(r) for y in range(len(a[0])))
    edges=graph(a,b)
    chi=chromatic_number(r,edges)
    opts=[best_partition(a,b,k) for k in range(1,r+1)]
    assert opts[-1] == full
    assert next(k for k,v in enumerate(opts,1) if v==full)==chi
    for k in range(1,r+1):
        for grouping in product(range(k),repeat=r):
            assert score_assignment(a,b,grouping)-full==gap_from_abs(a,b,grouping)
    if brute:
        # Independent direct encoding + decoding enumeration, no min-group shortcut.
        Y=len(a[0]); assert r<=3 and Y<=2
        for k in range(1,r+1):
            direct=min(sum(a[h][y]*(1-decoder[grouping[h]*Y+y])
                           +b[h][y]*decoder[grouping[h]*Y+y]
                           for h in range(r) for y in range(Y))
                       for grouping in product(range(k),repeat=r)
                       for decoder in product((0,1), repeat=k*Y))
            assert direct==opts[k-1]
    return chi, opts


def run():
    # Explicit EC46 witness. 52 microscopic branches under each hypothesis.
    A=((24,8),(12,4),(3,1))
    B=((1,3),(4,12),(8,24))
    assert sum(map(sum,A))==sum(map(sum,B))==52
    chi,opts=test_model(A,B,brute=True)
    assert opts==[26,21,16] and chi==3
    labels=['a','b','c']; signs=['+','-']
    conflicts=[[labels[u],labels[v]] for u,v in graph(A,B)]
    counts={'example_encoder_decoder_checks':sum(k**3*2**(2*k) for k in (1,2,3)),
            'example_partitions':sum(k**3 for k in (1,2,3)),
            'equal_total_root_dependent_models':0,
            'constant_terminal_kernel_models':0,
            'unequal_denominator_fraction_models':0,
            'independent_brute_force_models':0,
            'graph_chromatic_checks':0,
            'gap_identity_assignment_checks':0}
    # Product-form models: P(h,y)=u_h*p_y and Q(h,y)=v_h*q_y with all strictly positive.
    for M in range(3,7):
        root_dist=list(compositions(M,3))
        for u in root_dist:
            for v in root_dist:
                for L in range(2,6):
                    dists=list(compositions(L,2))
                    for p in dists:
                        for q in dists:
                            aa=tuple(tuple(u[h]*p[y] for y in range(2)) for h in range(3))
                            bb=tuple(tuple(v[h]*q[y] for y in range(2)) for h in range(3))
                            sampled=counts['constant_terminal_kernel_models']<64
                            test_model(aa,bb,brute=sampled)
                            counts['constant_terminal_kernel_models']+=1
                            counts['independent_brute_force_models']+=int(sampled)
                            counts['graph_chromatic_checks']+=1
                            counts['gap_identity_assignment_checks']+=1+8+27
    # General strictly positive integer joint source counts, unrelated conditional kernels.
    for T in range(6,10):
        dists=list(compositions(T,6))
        for flat_a in dists:
            aa=(flat_a[:2],flat_a[2:4],flat_a[4:6])
            for flat_b in dists:
                bb=(flat_b[:2],flat_b[2:4],flat_b[4:6])
                test_model(aa,bb)
                counts['equal_total_root_dependent_models']+=1
                counts['graph_chromatic_checks']+=1
                counts['gap_identity_assignment_checks']+=1+8+27
    # Unequal denominator P and Q: clear by using LCM; resulting integers have equal common denominator.
    for flat_a in compositions(7,6):
        for flat_b in compositions(8,6):
            aa=tuple(tuple(8*flat_a[2*h+y] for y in range(2)) for h in range(3))
            bb=tuple(tuple(7*flat_b[2*h+y] for y in range(2)) for h in range(3))
            assert sum(map(sum,aa))==sum(map(sum,bb))==56
            test_model(aa,bb)
            counts['unequal_denominator_fraction_models']+=1
            counts['graph_chromatic_checks']+=1
            counts['gap_identity_assignment_checks']+=1+8+27
    report={
      'schema':'EM_R4_EC46_EXACT_CHECK_V1',
      'arithmetic':'Python exact integers; arbitrary-rational denominators cross-multiplied',
      'scope':'finite two-observation BRC source populations; not X6 native dynamics',
      'example':{'source_counts_P':A,'source_counts_Q':B,'denominator_each':52,
                 'bayes_error_numerators_by_K':{'1':26,'2':21,'3':16},
                 'bayes_error_by_K':{'1':'1/2','2':'21/52','3':'4/13'},
                 'strict_improvements':{'1_to_2':'5/52','2_to_3':'5/52'},
                 'conflict_graph_edges':conflicts,'chromatic_number':3,
                 'four_observer_region_K_min':3,'decision_stage':2,
                 'time_coordinates':['stage-1 source-root observation','stage-2 terminal-source observation'],
                 'expected_decision_depth_each':'2'},
      'coverage':counts,
      'all_checks':'PASS',
      'universal_proof':'not a consequence of finite tests; see EC46 theorem paper'
    }
    return report

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
