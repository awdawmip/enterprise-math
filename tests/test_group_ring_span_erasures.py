from dataclasses import replace
from itertools import combinations
from math import gcd

import pytest

from enterprise_math.group_ring_span_erasures import (
    certify_span_erasures, verify_span_erasure_certificate, target_closures,
    interval_period_threshold, full_interval_threshold, minimum_erasure_span,
    robust_tail_parameters, robust_tail_support, translated_lag_witness,
    robust_tail_order,
)
from enterprise_math.group_ring_support_design import certify_mark_erasures
from enterprise_math.group_ring_sparse_identifiability import period_closures


def signature(s, r):
    return tuple((i,j) for i,x in enumerate(s) for j,y in enumerate(s)
                 if i < j and (y-x) % r == 0)


def identifiable(s, H, A):
    limit = max(H,A)+2
    rows = {r: signature(s,r) for r in range(1,limit)}
    return all(rows[r] != rows[t] for r in range(1,H+1)
               for t in range(1,limit) if t != r)


def brute_loss(s, H, A, protected=()):
    allowed = tuple(x for x in s if x not in protected)
    for k in range(len(allowed)+1):
        for removed in combinations(allowed,k):
            remain = tuple(x for x in s if x not in removed)
            if not identifiable(remain,H,A):
                return k
    return None


@pytest.mark.parametrize('H,A,s', [
    (3,4,(0,1,2,3,4)), (6,8,tuple(range(9))),
    (3,8,(0,2,5,8)), (6,6,(0,4,5,6)),
    (2,6,(0,1,3,6)), (1,1,(0,)), (4,3,(0,1,2,3)),
])
def test_general_erasure_certificate_matches_independent_partitions(H,A,s):
    out = certify_span_erasures(s,H,A)
    assert out.status == 'COMPLETE'
    c = out.certificate
    assert c.minimum_deletions == brute_loss(s,H,A)
    assert verify_span_erasure_certificate(c)
    rem = tuple(x for x in s if x not in c.erased_marks)
    assert signature(rem,c.witness_period) == signature(rem,c.alias_period)


def test_prime_three_is_really_needed_not_only_parity():
    # For r=1, delete position1: remaining 0,3,6 have closure3, not an even closure.
    s=(0,1,3,6)
    out=certify_span_erasures(s,1,6).certificate
    assert out.minimum_deletions == 1
    assert out.witness_period == 1 and out.alias_period == 3
    assert out.erased_marks == (1,)


@pytest.mark.parametrize('protected', [(),(0,), (0,6), (0,1,2,3,6)])
def test_protected_general_cut_and_old_fixed_span_agree(protected):
    s=(0,1,2,3,6)
    new=certify_span_erasures(s,6,6,protected=protected).certificate
    old=certify_mark_erasures(s,6,protected=protected).certificate
    assert new.minimum_deletions == old.minimum_deletions
    assert new.minimum_deletions == brute_loss(s,6,6,protected)


def test_full_interval_threshold_and_witness():
    for H in range(1,12):
        for A in range(H,H+7):
            c=certify_span_erasures(tuple(range(A+1)),H,A).certificate
            assert c.minimum_deletions == full_interval_threshold(A,H)
            assert c.alias_period == 2*c.witness_period


@pytest.mark.parametrize('H,e,A', [
    (1,0,1),(1,4,9),(2,1,3),(3,1,4),(6,2,8),(6,3,9),
    (6,4,12),(10,1,11),(10,5,15),(10,6,18),(10,9,27),
])
def test_exact_minimum_span(H,e,A):
    out=minimum_erasure_span(H,e)
    assert out.status=='COMPLETE' and out.minimum_span==A
    assert full_interval_threshold(A,H)>e
    assert full_interval_threshold(A-1,H)<=e
    assert interval_period_threshold(A-1,out.limiting_period)<=e


def test_general_large_loss_quotient_blocks():
    for H in range(1,26):
        for e in range(H,45):
            ans=minimum_erasure_span(H,e)
            E=e+1
            expected=e+max(r*((E+r-1)//r) for r in range(1,H+1))
            assert ans.minimum_span==expected
    out=minimum_erasure_span(20,100,max_blocks=0)
    assert out.status=='BUDGET_EXHAUSTED' and out.minimum_span is None


def test_huge_symbolic_span_and_tail_have_no_population_expansion():
    H=10**60
    ans=minimum_erasure_span(H,3)
    assert ans.minimum_span==H+3 and ans.evaluated_blocks==0
    p=robust_tail_parameters(H,3)
    assert p.span==H+3 and p.mark_upper_bound < H
    with pytest.raises(ValueError,match='max_marks'):
        robust_tail_support(H,3,max_marks=1000)


@pytest.mark.parametrize('H,e', [(3,1),(6,1),(6,2),(9,2),(10,3),(17,2),(30,5)])
def test_robust_sparse_construction_and_disjoint_witnesses(H,e):
    p=robust_tail_parameters(H,e)
    s=robust_tail_support(H,e)
    assert max(s)==H+e and len(s)<=p.mark_upper_bound
    assert minimum_erasure_span(H,e).minimum_span==p.span
    for d in range(H//3+1,H+1):
        pairs=translated_lag_witness(p,d)
        assert len(pairs)==e+1
        assert all(y-x==d and x in s and y in s for x,y in pairs)
        assert len({x for pair in pairs for x in pair})==2*(e+1)
    c=certify_span_erasures(s,H,p.span).certificate
    assert c.minimum_deletions==e+1


def test_construction_matches_old_tail_when_no_loss():
    from enterprise_math.group_ring_support_design import tail_ruler
    for H in range(1,101):
        assert robust_tail_support(H,0)==tail_ruler(H)


def test_small_all_erasure_patterns_without_protected_endpoints():
    for H,e in [(3,1),(6,2),(9,2)]:
        s=robust_tail_support(H,e)
        for count in range(e+1):
            for erased in combinations(s,count):
                keep=tuple(x for x in s if x not in erased)
                assert target_closures(keep,H,H+e)==tuple(range(1,H+1))


def test_above_H_is_not_a_single_observation_partition():
    # H=3, A=4: order4 and order5 are both above-H but have different collisions.
    s=(0,1,2,3,4)
    assert signature(s,4)!=signature(s,5)
    ans=robust_tail_order(17,4,3,1) # order4, visible collision at 0,4
    assert ans.status=='ORDER_ABOVE_HORIZON' and ans.order is None


def test_larger_span_can_bypass_old_highband_need():
    # r=3 need not occur as a lag if6 and9 are retained and the target stops at3.
    s=(0,1,5,7,9)
    ds={y-x for x in s for y in s if y>x}
    assert 3 not in ds and target_closures(s,3,9)==(1,2,3)
    assert certify_span_erasures(s,3,9).certificate.minimum_deletions>=1


def test_actual_modular_powers_after_erasures():
    H,e=6,2
    s=robust_tail_support(H,e)
    for n in range(2,31):
        for a in range(1,n):
            if gcd(a,n)!=1:continue
            z=a%n;r=1
            while z!=1:z=z*a%n;r+=1
            for erased in [(),(s[0],),(s[-1],),(s[0],s[-1])]:
                ans=robust_tail_order(n,a,H,e,erased=erased)
                if r<=H:assert ans.order==r
                else:assert ans.status=='ORDER_ABOVE_HORIZON'


def test_budgets_and_forgery_are_not_success():
    s=robust_tail_support(12,2)
    out=certify_span_erasures(s,12,14,max_mark_visits=1)
    assert out.status=='BUDGET_EXHAUSTED' and out.certificate is None
    out=certify_span_erasures(s,12,14,max_sieve_span=1)
    assert out.status=='BUDGET_EXHAUSTED' and out.certificate is None
    c=certify_span_erasures(s,12,14).certificate
    with pytest.raises(ValueError):verify_span_erasure_certificate(replace(c,minimum_deletions=100))
    with pytest.raises(ValueError):verify_span_erasure_certificate(replace(c,erased_marks=()))
    with pytest.raises(ValueError):verify_span_erasure_certificate(replace(c,minimum_deletions=True))
    with pytest.raises(ValueError):translated_lag_witness(replace(robust_tail_parameters(12,2),blocks=9),12)


@pytest.mark.parametrize('args', [(0,0),(5,-1),(True,0),(5,True),(5,2)])
def test_invalid_construction_inputs(args):
    with pytest.raises(ValueError):robust_tail_parameters(*args)


def test_invalid_domains_and_loss_inputs():
    with pytest.raises(ValueError):certify_span_erasures((0,0,3),3,4)
    with pytest.raises(ValueError):certify_span_erasures((0,4),3,3)
    with pytest.raises(ValueError):certify_span_erasures((0,3),3,4,protected=(1,))
    with pytest.raises(ValueError):robust_tail_order(7,2,3,1,erased=(0,1))
    with pytest.raises(ValueError):robust_tail_order(7,2,3,1,erased=(90,))
    with pytest.raises(ValueError):robust_tail_order(8,2,3,1)
    with pytest.raises(ValueError):robust_tail_parameters(6,1,width=0)
    with pytest.raises(ValueError):robust_tail_parameters(6,1,width=10)


def test_required_boundary_and_mark_bound_at_optimal_span():
    from enterprise_math.group_ring_span_erasures import robust_mark_lower_bound
    for H in range(1,40):
        for e in range(H//3+1):
            s=robust_tail_support(H,e)
            assert len(s)>=robust_mark_lower_bound(H,e)
            assert (set(range(e+1))|set(range(H,H+e+1))).issubset(s)
    with pytest.raises(ValueError):robust_mark_lower_bound(6,4)
