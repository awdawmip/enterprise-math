#!/usr/bin/env python3
"""PREFIX-808: exact named-edge cut projection and signed histogram regression.
No third-party dependencies; Python >=3.9. Do not treat finite tests as theorem proof.
"""
from collections import defaultdict, Counter
from itertools import combinations, product
import json


def margin_of(x, edges, nr, nc):
    r, s = [0]*nr, [0]*nc
    for z,(i,j,k) in zip(x,edges):
        r[i]+=z; s[j]+=z
    return tuple(r),tuple(s)


def observer(x):
    return (sum(((e % 5)-2)*v for e,v in enumerate(x)),
            sum((((3*e+1) % 7)-3)*v for e,v in enumerate(x)))


def cut_test(edges, nr, nc, margins, chosen):
    """Chosen mapping edge-index->fixed integer, including selected and frozen edges.
    For remaining edges, verify integer transport feasibility via all directed cuts.
    """
    r=list(margins[0]); s=list(margins[1]); remaining=[]
    for e,(i,j,k) in enumerate(edges):
        if e in chosen:
            t=chosen[e]
            if t < 0 or t > k:
                return False
            r[i]-=t; s[j]-=t
        else:
            remaining.append((i,j,k))
    if min(r+s) < 0 or sum(r) != sum(s):
        return False
    for A in range(1<<nr):
        for B in range(1<<nc):
            lhs=sum(r[i] for i in range(nr) if (A>>i)&1)
            lhs-=sum(s[j] for j in range(nc) if (B>>j)&1)
            rhs=sum(k for i,j,k in remaining if ((A>>i)&1) and not ((B>>j)&1))
            if lhs > rhs:
                return False
    return True


def residual_histogram(edges,nr,nc,margins,chosen):
    """Independent exact enumeration of all completions after chosen values."""
    other=[e for e in range(len(edges)) if e not in chosen]
    ret=Counter()
    for values in product(*(range(edges[e][2]+1) for e in other)):
        x=[0]*len(edges)
        for e,v in chosen.items(): x[e]=v
        for e,v in zip(other, values): x[e]=v
        if margin_of(x, edges,nr,nc)==margins:
            ret[observer(x)] += 1
    return ret


def exhaustive_family(nr,nc,maxcap,selection):
    num_edges=nr*nc
    totals=Counter()
    for capacities in product(range(maxcap+1),repeat=num_edges):
        edges=[(e//nc,e%nc,capacities[e]) for e in range(num_edges)]
        fibers=defaultdict(list)
        for x in product(*(range(k+1) for k in capacities)):
            fibers[margin_of(x,edges,nr,nc)].append(x)
            totals['all_tables']+=1
        totals['capacity_patterns']+=1
        for margins,tables in fibers.items():
            totals['margin_fibers']+=1
            for T in selection(num_edges):
                fcases=[{}]
                # Also test frozen-source fibers for 2x2 with a selected pair.
                if nr==2 and nc==2 and len(T)==2:
                    for f in range(num_edges):
                        if f not in T:
                            for val in set(x[f] for x in tables):
                                fcases.append({f:val})
                for frozen in fcases:
                    selected_tables=[x for x in tables if all(x[e]==v for e,v in frozen.items())]
                    totals['subfibers']+=1
                    truth=defaultdict(Counter)
                    for x in selected_tables:
                        truth[tuple(x[e] for e in T)][observer(x)]+=1
                    predicted=defaultdict(Counter)
                    for assignment in product(*(range(capacities[e]+1) for e in T)):
                        chosen=dict(frozen)
                        chosen.update(zip(T,assignment))
                        yes=cut_test(edges,nr,nc,margins,chosen)
                        exists=assignment in truth
                        totals['candidate_vectors']+=1
                        assert yes==exists,(nr,nc,capacities,margins,T,frozen,assignment,yes,exists)
                        if yes:
                            h=residual_histogram(edges,nr,nc,margins,chosen)
                            assert h==truth[assignment],(nr,nc,capacities,margins,T,frozen,assignment,h,truth[assignment])
                            totals['histogram_checks']+=1
                            predicted[assignment]=h
                            totals['feasible_vectors']+=1
                        else:
                            totals['excluded_vectors']+=1
                    assert predicted==truth,(nr,nc,capacities,margins,T,frozen)
                    totals['subfiber_checks']+=1
    return totals


def selections(nr,nc):
    if (nr,nc)==(2,2):
        return lambda E: list(combinations(range(E),2))+list(combinations(range(E),3))
    if (nr,nc)==(2,3):
        return lambda E: list(combinations(range(E),2))+list(combinations(range(E),3))
    if (nr,nc)==(3,3):
        return lambda E: [(0,4),(2,6)]
    raise ValueError('unknown family')


def run():
    families={}
    for nr,nc,maxcap in [(2,2,2),(2,3,1),(3,3,1)]:
        result=exhaustive_family(nr,nc,maxcap,selections(nr,nc))
        families[f'{nr}x{nc}_maxcap{maxcap}']=dict(result)
    # Named parallel edges: two distinct 0->0 sources, no forced merging.
    def named_parallel_test():
        edge_shapes=[(0,0,1),(0,0,1),(0,1,1),(1,0,1),(1,1,1)]
        fibers=defaultdict(list)
        for x in product(range(2),repeat=5):
            fibers[margin_of(x,edge_shapes,2,2)].append(x)
        checked=0
        for margins,tables in fibers.items():
            for T in combinations(range(5),2):
                truth={tuple(x[e] for e in T) for x in tables}
                for t in product(range(2),repeat=2):
                    chosen=dict(zip(T,t));yes=cut_test(edge_shapes,2,2,margins,chosen)
                    assert yes==(t in truth)
                    if yes:
                        assert residual_histogram(edge_shapes,2,2,margins,chosen)==Counter(observer(x) for x in tables if tuple(x[e] for e in T)==t)
                    checked+=1
        return {'margin_fibers':len(fibers),'selected_vector_checks':checked,'tables':32}
    parallel=named_parallel_test()
    # Coupling counterexample: marginal intervals both {0,1}; joint only {(1,0),(0,1)}.
    edge_grid=[(0,0,1),(0,1,1),(1,0,1),(1,1,1)]
    candidate_margins=((1,1),(1,1))
    joint={t for t in product(range(2),repeat=2) if cut_test(edge_grid,2,2,candidate_margins,{0:t[0],1:t[1]})}
    assert joint=={(1,0),(0,1)}
    out={'schema':'PREFIX808_R6_EXACT_MULTI_EDGE_CUT_PROJECTION_V1',
         'source_frontier':'PREFIX-807','scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'model':'FINITE_NAMED_BIPARTITE_INTEGER_CAPACITY_TRANSPORT_AUXILIARY',
         'families':families,'named_parallel':parallel,
         'coupling_counterexample':{'margins':[[1,1],[1,1]],'selected_edges':[0,1],
                                    'marginal_ranges':[[0,1],[0,1]],'attainable_pairs':sorted(map(list,joint)),
                                    'unattainable_pairs':[[0,0],[1,1]],
                                    'joint_laurent_polynomial':'z1 + z2'},
         'status':'ALL_EXACT_ASSERTIONS_PASSED',
         'proof_scope':'all finite named bipartite multigraphs, integral capacities and vertex demands',
         'regression_scope':'all capacity patterns and feasible margins of specified finite grids; all indicated T and F cases',
         'admission':'AUTHOR_PROVED_NOT_INDEPENDENTLY_REVIEWED'}
    out['totals']={k:sum(v.get(k,0) for v in families.values()) for k in ['capacity_patterns','margin_fibers','all_tables','subfibers','candidate_vectors','feasible_vectors','excluded_vectors','histogram_checks','subfiber_checks']}
    out['totals']['parallel_selected_vector_checks']=parallel['selected_vector_checks']
    return out


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2,ensure_ascii=False))
