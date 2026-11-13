#!/usr/bin/env python3
"""Exact author-side checker: rank-three (2+1)-block residual gauge orbits.

Runs over complete F_p^4 state populations for selected prime fields.
The theorem for all odd prime powers rests on the accompanying proof.
"""
from collections import Counter, deque
from itertools import product
import json
import random


def primitive_root(p):
    for g in range(2, p):
        if {pow(g, e, p) for e in range(1, p)} == set(range(1, p)):
            return g
    raise AssertionError(p)


def label(t, p):
    x0, x1, y0, y1 = t
    x = x0 != 0 or x1 != 0
    y = y0 != 0 or y1 != 0
    if not x and not y:
        return ('both_zero',)
    if x and not y:
        return ('only_upper',)
    if y and not x:
        return ('only_lower',)
    s = (y0*x0 + y1*x1) % p
    return ('both_nonzero_zero_pairing',) if s == 0 else ('paired_nonzero', s)


def neighbors(t, p, root, invroot):
    x0, x1, y0, y1 = t
    # U=[[1,1],[0,1]], L=[[1,0],[1,1]], D=diag(root,1)
    # Transform (X,Y) by (G X, Y G^-1); U,L,D generate GL_2(F_p).
    return (
        ((x0+x1)%p, x1, y0, (y1-y0)%p),
        (x0, (x0+x1)%p, (y0-y1)%p, y1),
        ((root*x0)%p, x1, (invroot*y0)%p, y1),
    )


def exhaust_full_group(p):
    root = primitive_root(p)
    invroot = pow(root, -1, p)
    unseen = set(product(range(p), repeat=4))
    expected_sizes = {
        ('both_zero',): 1,
        ('only_upper',): p*p-1,
        ('only_lower',): p*p-1,
        ('both_nonzero_zero_pairing',): (p*p-1)*(p-1),
    }
    expected_sizes.update({('paired_nonzero', s): p*(p*p-1) for s in range(1, p)})
    sizes = {}
    transitions = 0
    while unseen:
        first = next(iter(unseen))
        tag = label(first, p)
        todo = deque([first])
        unseen.remove(first)
        count = 0
        while todo:
            t = todo.popleft()
            assert label(t, p) == tag, (p, tag, t)
            count += 1
            for nxt in neighbors(t, p, root, invroot):
                transitions += 1
                if nxt in unseen:
                    unseen.remove(nxt)
                    todo.append(nxt)
        assert tag not in sizes, (p, tag, 'two orbits with same tag')
        sizes[tag] = count
    assert sizes == expected_sizes, (p, sizes, expected_sizes)
    assert sum(sizes.values()) == p**4
    assert len(sizes) == p+3
    return {'prime': p, 'root': root, 'states': p**4,
            'orbits': len(sizes), 'generator_transitions': transitions,
            'zero_pairing_nonzero_orbit_size': sizes[('both_nonzero_zero_pairing',)],
            'each_nonzero_pairing_orbit_size': p*(p*p-1)}


def exhaust_scalar_subgroup(p):
    root = primitive_root(p)
    unseen = set(product(range(p), repeat=4))
    orbit_sizes = Counter()
    while unseen:
        t = next(iter(unseen))
        seen = set()
        x0, x1, y0, y1 = t
        for e in range(p-1):
            a = pow(root, e, p)
            ia = pow(a, -1, p)
            seen.add(((a*x0)%p, (a*x1)%p, (ia*y0)%p, (ia*y1)%p))
        assert seen <= unseen
        orbit_sizes[len(seen)] += 1
        unseen.difference_update(seen)
    assert orbit_sizes[1] == 1
    assert orbit_sizes[p-1] == (p**4-1)//(p-1)
    assert sum(orbit_sizes.values()) == 1 + (p**4-1)//(p-1)
    return {'prime': p, 'scalar_effective_orbits': sum(orbit_sizes.values()),
            'nonzero_orbit_size': p-1}


def check_commutator_matrix(p, trials=120):
    rng = random.Random(20261028+p)
    for _ in range(trials):
        a,b = rng.sample(range(p), 2)
        B = [[rng.randrange(p) for _ in range(3)] for _ in range(3)]
        A = [a,a,b]
        K = [[(B[i][j]*A[j]-A[i]*B[i][j])%p for j in range(3)]
             for i in range(3)]
        upper = ((b-a)*B[0][2]%p,(b-a)*B[1][2]%p)
        lower = ((a-b)*B[2][0]%p,(a-b)*B[2][1]%p)
        assert K == [[0,0,upper[0]],[0,0,upper[1]],[lower[0],lower[1],0]]
        s = (upper[0]*lower[0]+upper[1]*lower[1])%p
        K2trace = sum(K[i][j]*K[j][i] for i in range(3) for j in range(3))%p
        assert K2trace == (2*s)%p
    return {'prime':p,'random_exact_commutator_trials':trials}



def rank_mod(rows, p):
    M = [row[:] for row in rows]
    if not M:
        return 0
    m, n = len(M), len(M[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank,m) if M[i][col] % p), None)
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        inv = pow(M[rank][col] % p, -1, p)
        M[rank] = [(x*inv)%p for x in M[rank]]
        for j in range(m):
            if j != rank and M[j][col] % p:
                c = M[j][col] % p
                M[j] = [(x-c*y)%p for x,y in zip(M[j],M[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def mul3(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(3))%p
             for j in range(3)] for i in range(3)]


def bracket(A,B,p):
    AB,BA = mul3(A,B,p),mul3(B,A,p)
    return [[(AB[i][j]-BA[i][j])%p for j in range(3)] for i in range(3)]


def check_burnside(p):
    A=[[0,0,0],[0,0,0],[0,0,1]]
    hist=Counter()
    total_fixed=0
    order=0
    for a,b,c,d in product(range(p),repeat=4):
        if (a*d-b*c)%p==0:
            continue
        G=[[a,b,0],[c,d,0],[0,0,1]]
        columns=[]
        for i,j in product(range(3),repeat=2):
            E=[[0]*3 for _ in range(3)]
            E[i][j]=1
            delta=bracket(bracket(E,A,p),G,p)
            columns.append([delta[x][y] for x,y in product(range(3),repeat=2)])
        rho=rank_mod([[columns[k][z] for k in range(9)] for z in range(9)],p)
        assert rho<=4
        hist[rho]+=1
        total_fixed += p**(9-rho-5)
        order+=1
    assert order==(p*p-1)*(p*p-p)
    assert total_fixed==order*(p+3), (p,total_fixed,order)
    return {'prime':p, 'effective_GL2_group_order':order,
            'fixed_point_sum':total_fixed, 'burnside_orbits':total_fixed//order,
            'double_commutator_rank_histogram':dict(sorted(hist.items()))}


def main():
    cases = [exhaust_full_group(p) for p in (3,5,7,11,13,19)]
    scalar = [exhaust_scalar_subgroup(p) for p in (3,5,7,13)]
    matrices = [check_commutator_matrix(p) for p in (3,5,7,13,19,373)]
    burnside = [check_burnside(p) for p in (3,5,7)]
    p=373
    result = {
       'status':'PASS',
       'proof_scope':'all odd prime powers via algebraic proof; script tests prime fields only',
       'exhaustive_full_gauge':cases,
       'exhaustive_scalar_effective_subgroup':scalar,
       'commutator_checks':matrices,
       'rank_independent_burnside_map_checks':burnside,
       'p373_theorem_predictions': {
          'total_marked_K':p**4,
          'full_GL2_effective_orbits':p+3,
          'scalar_only_effective_orbits':1+(p**4-1)//(p-1),
          'source_fiber_for_fixed_K':p**5,
          'scalar_zero_pairing_collapses_four_distinct_full_gauge_orbits':True,
       },
       'admission':'AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE'
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
