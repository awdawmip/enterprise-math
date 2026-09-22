from collections import defaultdict
from math import gcd
import random
import pytest

from enterprise_math.group_ring_affine_character import (
    affine_correlation, affine_correlation_coefficients,
    affine_collision_from_order, affine_index_responses,
    compile_character_index, invert_affine_collision, jacobi_symbol,
)
from enterprise_math.group_ring_batch_response import compile_terminal_index


def histogram(n, a, length, intercept=1, slope=0):
    out = defaultdict(int)
    v = 1
    for x in range(length):
        out[v] += intercept+slope*x
        v = v*a % n
    return out


def observer(h, n, u):
    return sum(m*h.get(u*v % n,0) for v,m in h.items())


def explicit_order(n,a):
    v = 1
    for r in range(1,n+1):
        v = v*a % n
        if v == 1:
            return r
    raise AssertionError('unit order not found')


def test_ported_jacobi_matches_independent_sympy():
    from sympy.functions.combinatorial.numbers import jacobi_symbol as reference
    for n in range(1,100,2):
        for a in range(-40,80):
            assert jacobi_symbol(a,n) == int(reference(a,n))


def test_nonuniform_positive_counterexample():
    w = (2,1,1,2)
    def mass(a):
        h = defaultdict(int)
        for i,value in enumerate(w):
            h[pow(a,i,7)] += value
        return sum(x*x for x in h.values())
    assert explicit_order(7,6) == 2
    assert explicit_order(7,2) == 3
    assert sum(x*x for x in w) == 10
    assert mass(6) == mass(2) == 18


def test_zero_weight_hole_breaks_first_collision_detection():
    w = (1,0,1,0)
    h = defaultdict(int)
    for x,value in enumerate(w):
        h[pow(2,x,7)] += value
    assert explicit_order(7,2) == 3 < len(w)
    assert sum(x*x for x in h.values()) == sum(x*x for x in w) == 2


def test_general_monotone_weight_proof_identity():
    rng = random.Random(20260922)
    for _ in range(120):
        w = sorted(rng.randint(1,20) for _ in range(rng.randint(2,18)))
        corr = [sum(w[x]*w[x+d] for x in range(len(w)-d)) for d in range(len(w))]+[0]
        for d in range(len(w)-1):
            defect = w[0]*w[d]+sum((w[y-d]-w[y-d-1])*w[y]
                                   for y in range(d+1,len(w)))
            assert corr[d]-corr[d+1] == defect > 0
        masses = [corr[0]+2*sum(corr[d] for d in range(r,len(w),r))
                  for r in range(1,len(w)+1)]
        assert all(x>y for x,y in zip(masses,masses[1:]))
        assert masses[-1] == corr[0]


@pytest.mark.parametrize('intercept,slope',[(1,0),(1,1),(4,3),(1000,20)])
def test_affine_autocorrelation_cubic(intercept,slope):
    for L in range(1,35):
        for d in range(-L-2,L+3):
            k = abs(d)
            expected = sum((intercept+slope*x)*(intercept+slope*(x+k))
                           for x in range(max(0,L-k)))
            assert affine_correlation(L,d,intercept,slope) == expected
        c0,c1,c3 = affine_correlation_coefficients(L,intercept,slope)
        assert c0+c1*L+c3*L**3 == 0


def test_progression_collision_and_inversion():
    for L in range(1,32):
        for r in range(1,L+5):
            for intercept,slope in [(1,0),(1,1),(3,4)]:
                masses = [0]*r
                for x in range(L):
                    masses[x%r] += intercept+slope*x
                K = sum(x*x for x in masses)
                assert affine_collision_from_order(L,r,intercept,slope) == K
                inferred = invert_affine_collision(K,L,intercept,slope)
                if r < L:
                    assert inferred.order == r
                else:
                    assert inferred.order is None and inferred.lower_bound == L


def test_insufficient_mass_not_certified():
    assert invert_affine_collision(30,4,1,1).order is None
    with pytest.raises(ValueError):
        invert_affine_collision(29,4,1,1)
    with pytest.raises(ValueError):
        invert_affine_collision(31,4,1,1)
    with pytest.raises(ValueError):
        invert_affine_collision(276,4,1,1)


def test_parity_witness_and_nonrecursive_gain():
    p = compile_character_index(7,3,11,range(7))
    assert p.mode == 'PARITY_PROGRESSION'
    assert p.search_span == 6
    assert p.index.order == 6
    assert p.index._logs[3] == 1
    assert jacobi_symbol(3,7) == -1
    assert jacobi_symbol(3*3,7) == 1
    for u,e in p.index._logs.items():
        assert jacobi_symbol(u,7) == (-1)**e


def test_character_zero_and_same_sign_not_membership():
    p = compile_character_index(21,4,50,(1,4,16,5,2))
    assert p.mode == 'CHARACTER_ZERO_EXCLUSION'
    assert set(p.rejected_states) == {2}
    assert jacobi_symbol(5,21) == jacobi_symbol(4,21) == 1
    assert 5 not in p.index._logs
    assert affine_index_responses(p.index,20,(2,5),2,1) == (0,0)


@pytest.mark.parametrize('n,a',[(7,3),(15,2),(15,7),(21,2),(9,2),(16,3),(5,4),(3,1)])
def test_character_all_lengths_and_weighted_observers(n,a):
    states = tuple(range(n))
    for span in range(1,16):
        filtered = compile_character_index(n,a,span,iter(states))
        raw = compile_terminal_index(n,a,span,states)
        assert filtered.status == raw.status == 'COMPLETE'
        r = explicit_order(n,a)
        if filtered.index.order is not None:
            assert filtered.index.order == r
        for L in range(1,span+1):
            h = histogram(n,a,L,2,3)
            expected = tuple(observer(h,n,u) for u in states)
            assert affine_index_responses(filtered.index,L,states,2,3) == expected
            assert affine_index_responses(raw.index,L,states,2,3) == expected
        # Existing unweighted windows and dyadic cuts remain valid after lifting.
        requests = [(span,u) for u in states]
        assert filtered.index.windows(requests) == raw.index.windows(requests)
        m = span.bit_length()-1
        assert filtered.index.cuts(m,range(m+1),states) == raw.index.cuts(m,range(m+1),states)


def test_odd_horizon_off_by_one():
    p = compile_character_index(17,3,15,(1,3,6))
    assert p.index.order == 16  # certified via a^2, even though beyond master horizon
    assert p.index._logs[3] == 1
    assert p.index._logs[6] == 15  # inferred from inverse exponent1 and proven period16
    assert p.index.windows([(15,6)]) == (14,)


def test_budget_failure_is_unknown():
    for use in (False,True):
        p = compile_character_index(10007,5,1000,(1,2,3),use_character=use,
                                    max_baby_steps=10,max_scan_steps=0)
        assert p.status == 'BUDGET_EXHAUSTED' and p.index is None
        assert p.executed_scans == 0


def test_duplicate_empty_nonunit_and_identity_inputs():
    for n,a,states in [(7,3,()),(15,2,(0,3,5)),(7,1,(1,1,2)),(7,3,(3,3,1))]:
        p = compile_character_index(n,a,12,iter(states))
        h = histogram(n,a,10,5,2)
        assert affine_index_responses(p.index,10,states,5,2) == tuple(observer(h,n,u) for u in states)


def test_domain_is_immutable_and_bounded():
    p = compile_character_index(7,3,7,(1,3))
    with pytest.raises(TypeError):
        p.index._logs[2] = 1
    with pytest.raises(ValueError):
        affine_index_responses(p.index,8,(1,))
    with pytest.raises(ValueError):
        affine_index_responses(p.index,6,(2,))


@pytest.mark.parametrize('args',[(2,1,10,(1,)),(7,0,10,(1,)),(15,3,10,(1,)),
                                 (7,3,0,(1,)),(7,3,10,(7,)),(7,3,10,(True,))])
def test_bad_compiler_inputs(args):
    with pytest.raises(ValueError):
        compile_character_index(*args)


@pytest.mark.parametrize('args',[(0,0,1,1),(4,0,0,1),(4,0,1,-1),(4,True,1,1)])
def test_bad_weight_inputs(args):
    with pytest.raises(ValueError):
        affine_correlation(*args)
