"""Exact rational audit for a calibrated two-direction clock comparison graph."""
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations, product
import json


def lab_table():
    def decimal(x):
        return Decimal(x.numerator) / Decimal(x.denominator)
    # MHz, the four displayed centres in Botermann et al., Table I.
    freq = tuple(map(F, ('777210326.98','384225534.98','546455143.0','546474960.7')))
    err = tuple(map(F, ('1.25','1.6','.43','.43')))
    p, a = freq[0]/freq[2], freq[1]/freq[3]
    with localcontext() as ctx:
        ctx.prec=45
        eps = decimal(p*a).sqrt()-1
        assert Decimal('1.47e-9') < eps < Decimal('1.48e-9')
        sigma = sum(decimal((u/v)**2) for u,v in zip(err,freq)).sqrt()/2
        return {'frequency_MHz_parallel_antiparallel_rest1_rest2':list(map(str,freq)),
                'one_sigma_MHz':list(map(str,err)), 'epsilon_from_displayed_centres':format(eps,'.12E'),
                'first_order_independent_sigma_log_scale':format(sigma,'.12E'),
                'directional_beta_conditional':format(decimal((p-a)/(p+a)),'.12f'),
                'Bothwell_slope_relative_deviation_nominal':str(F(98,109)-1),
                'Bothwell_relative_one_sigma_given_nominal_slope':str(F(23,109))}


def potentials(n, edges):
    graph = defaultdict(list)
    for u,v,p,a in edges:
        graph[u].append((v,p,a))
        graph[v].append((u,1/p,1/a))
    state = {}
    for root in range(n):
        if root in state:
            continue
        state[root]=(F(1),F(1))
        queue=[root]
        while queue:
            u=queue.pop()
            for v,p,a in graph[u]:
                dst=(state[u][0]*p,state[u][1]*a)
                if v in state and state[v]!=dst:
                    return None
                if v not in state:
                    state[v]=dst
                    queue.append(v)
    return state


def square_class(x):
    # Positive rational, sparse prime vectors mod 2.
    v=x.numerator*x.denominator
    primes=set()
    p=2
    while p*p<=v:
        while v%p==0:
            primes.symmetric_difference_update((p,))
            v//=p
        p+=1
    if v!=1:
        primes.add(v)
    return frozenset(primes)


def degree(edges):
    pivots={}
    for _,_,p,a in edges:
        vec=set(square_class(p*a))
        while vec:
            pivot=max(vec)
            if pivot not in pivots:
                pivots[pivot]=vec
                break
            vec=vec^pivots[pivot]
    return 2**len(pivots)


def scalar_cycles(n, edges):
    graph=defaultdict(list)
    for eid,(u,v,r) in enumerate(edges):
        graph[u].append((v,eid,r))
        graph[v].append((u,eid,1/r))
    def visit(root,u,seen,used,ratio):
        for v,eid,r in graph[u]:
            if eid in used:
                continue
            if v==root:
                yield len(used)+1,ratio*r
            elif v>root and v not in seen:
                yield from visit(root,v,seen|{v},used|{eid},ratio*r)
    for root in range(n):
        yield from visit(root,root,{root},set(),F(1))


def worst(n, edges):
    # Store kappa = radicand ** (1/order), exactly.
    best,order=F(1),1
    for count,ratio in scalar_cycles(n,edges):
        r=max(ratio,1/ratio)
        if r**order > best**count:
            best,order=r,count
    return best,order


def bounds_feasible(n, edges, kappa):
    # Both directed upper bounds on the ratio potential[v]/potential[u].
    arcs=[]
    for u,v,r in edges:
        arcs.extend(((u,v,kappa*r),(v,u,kappa/r)))
    upper=[F(1)]*n
    for _ in range(n):
        changed=False
        for u,v,bound in arcs:
            candidate=upper[u]*bound
            if candidate<upper[v]:
                upper[v]=candidate
                changed=True
        if not changed:
            return True
    return False


def synthetic():
    E=[(0,1,F(6),F(3,2)),(1,2,F(1),F(4,9)),(0,2,F(6),F(2,3))]
    assert degree(E)==1 and potentials(3,E)=={0:(1,1),1:(6,F(3,2)),2:(6,F(2,3))}
    factor=F(16,15)
    distorted=E[:-1]+[(0,2,6*factor,F(2,3)/factor)]
    assert [p*a for _,_,p,a in distorted]==[p*a for _,_,p,a in E]
    assert potentials(3,distorted) is None
    for i in range(3):
        assert potentials(3,distorted[:i]+distorted[i+1:]) is not None
    row=[(u,v,p) for u,v,p,_ in distorted]
    assert worst(3,row)==(factor,3)
    sq=[(0,1,F(2),F(1)),(1,2,F(3),F(1)),(0,2,F(6),F(1))]
    assert potentials(3,sq) is not None and degree(sq)==4
    parallel=[(0,1,F(1)),(0,1,F(4)),(0,1,F(1,4))]
    assert bounds_feasible(2,parallel[:2],F(2)) and bounds_feasible(2,[parallel[0],parallel[2]],F(2))
    assert not bounds_feasible(2,parallel,F(2)) and bounds_feasible(2,parallel,F(4))
    assert worst(2,parallel)==(16,2)
    # All signed exponent labels -1,0,1 on every edge of K4, two independent algorithms.
    pairs=list(combinations(range(4),2))
    trials=0
    for labels in product((-1,0,1),repeat=len(pairs)):
        es=[(u,v,F(2)**x) for (u,v),x in zip(pairs,labels)]
        r,k=worst(4,es)
        for cap in (F(1),F(5,4),F(3,2),F(2)):
            assert (cap**k>=r)==bounds_feasible(4,es,cap)
            trials+=1
    # Hamming distance from the neutral report, node rates independently 1 or 2,
    # global gauge fixed at vertex zero.  The cut witness also lives in Q.
    weights=[]
    for state in product((F(1),F(2)),repeat=3):
        c=(F(1),)+state
        if len(set(c))<2:
            continue
        weights.append(sum(c[v]!=c[u] for u,v in pairs))
    assert min(weights)==3
    return {'calibrated_triangle_UV':{str(k):list(map(str,v)) for k,v in potentials(3,E).items()},
            'reciprocal_drift_same_product':str(factor),'triangle_min_multiplicative_repair':'(16/15)^(1/3)',
            'real_but_not_rational_node_factor_example':{'square_classes':['2','3','6'],'minimal_degree':degree(sq)},
            'parallel_ratios':['1','4','1/4'],'parallel_optimum':4,
            'K4_crosschecks_cycle_vs_difference_constraints':trials,'K4_minimum_cut':min(weights)}


if __name__=='__main__':
    print(json.dumps({'published_tables':lab_table(),'conditional_graph':synthetic()},indent=2,sort_keys=True))
