from dataclasses import replace
from itertools import combinations
from math import gcd, isqrt
from random import Random

import pytest

from enterprise_math.group_ring_support_design import (
    tail_ruler_parameters, tail_ruler, tail_ruler_order,
    prune_identifying_support, verify_support_reduction,
    certify_mark_erasures, verify_mark_erasure_certificate,
    _destroy_lag,
)
from enterprise_math.group_ring_support_certificates import high_band_identifiable
from enterprise_math.group_ring_sparse_identifiability import (
    period_closures, sparse_ruler,
)


def simple_band(s,H):
    D={y-x for x in s for y in s if x<y}
    return all(d in D for d in range(H//3+1,H+1))


def brute_erasure(s,H,protected=()):
    allowed=[x for x in s if x not in protected]
    for e in range(len(allowed)+1):
        for erased in combinations(allowed,e):
            if not simple_band(set(s)-set(erased),H):
                return e
    return None


@pytest.mark.parametrize('H',[1,2,3,4,5,6,9,10,15,24,100,4096,65536])
def test_construction_and_integer_mark_bound(H):
    p=tail_ruler_parameters(H);s=tail_ruler(H)
    assert simple_band(s,H)
    root=isqrt(4*p.compulsory_count)
    expected=root+(root*root<4*p.compulsory_count)
    assert p.mark_upper_bound==expected
    assert len(s)<=expected
    assert s[0]==0 and s[-1]==H


def test_symbolic_large_horizon_does_not_expand():
    p=tail_ruler_parameters(10**60+37)
    assert p.width*p.blocks>=p.compulsory_count
    assert p.mark_upper_bound>10**20
    with pytest.raises(ValueError,match='max_marks'):
        tail_ruler(p.horizon,max_marks=1000)


def test_tail_need_not_cover_all_differences():
    s=(0,1,6,8,10)
    assert high_band_identifiable(s,10)
    assert 3 not in {y-x for x in s for y in s if x<y}
    assert period_closures(s,10)==tuple(range(1,11))+(0,)


def test_safe_pruning_h10_and_h15():
    assert prune_identifying_support(tail_ruler(10),10).support==(0,1,6,8,10)
    assert prune_identifying_support(tail_ruler(15),15).support==(0,1,2,9,12,15)


def test_every_order_of_deletion_keeps_coverage_and_local_minimality():
    rng=Random(445)
    for H in range(1,50):
        initial=sparse_ruler(H);scan=list(initial);rng.shuffle(scan)
        out=prune_identifying_support(initial,H,order=scan)
        assert verify_support_reduction(out)
        assert simple_band(out.support,H)
        for x in out.support:
            assert not simple_band(set(out.support)-{x},H)


def test_protected_deletion_is_honored():
    out=prune_identifying_support(tuple(range(12)),11,protected=(4,5,6))
    assert set((4,5,6)).issubset(out.support)
    assert verify_support_reduction(out)


def test_pruning_cap_and_invalid_input():
    assert prune_identifying_support((0,1,4,6),6,max_pairs=0).status=='BUDGET_EXHAUSTED'
    with pytest.raises(ValueError):prune_identifying_support((0,6),6)
    with pytest.raises(ValueError):prune_identifying_support((0,1,4,6),6,order=(0,1))
    with pytest.raises(ValueError):prune_identifying_support((0,1,4,6),6,protected=(True,))


def test_forged_pruning_witness_rejected():
    out=prune_identifying_support(tail_ruler(10),10)
    with pytest.raises(ValueError):verify_support_reduction(replace(out,support=(0,1,10)))
    with pytest.raises(ValueError):verify_support_reduction(replace(out,essential_lags=()))
    with pytest.raises(ValueError):verify_support_reduction(replace(out,removed=(0,)))


def test_two_representations_share_the_same_failure():
    s=(0,1,2,3,6)
    assert high_band_identifiable(s,6)
    edges=[(x,x+3) for x in s if x+3 in s]
    assert edges==[(0,3),(3,6)]
    assert _destroy_lag(edges,3,{0,6})==(3,)
    assert not simple_band(set(s)-{3},6)


def test_no_unprotected_support_tolerates_one_arbitrary_mark_loss():
    for H in range(1,60):
        cert=certify_mark_erasures(tail_ruler(H),H).certificate
        assert cert.minimum_deletions==1 and cert.witness_lag==H
        assert set(cert.erased_marks).issubset((0,H))
        assert verify_mark_erasure_certificate(cert)


def test_endpoints_only_full_support_has_exact_one_failure_tolerance():
    for H in range(3,60):
        cert=certify_mark_erasures(tuple(range(H+1)),H,protected=(0,H)).certificate
        assert cert.minimum_deletions==2
        assert cert.witness_lag==H-1 and cert.erased_marks==(1,H-1)


def test_all_protected_or_identifying_core_is_immune():
    s=tail_ruler(10)
    for full in [s,tuple(range(11))]:
        cert=certify_mark_erasures(full,10,protected=s).certificate
        assert cert.minimum_deletions is None
        assert cert.witness_lag is None and cert.erased_marks==()
        assert verify_mark_erasure_certificate(cert)


def test_already_bad_support_returns_zero_not_infinite():
    out=certify_mark_erasures((0,6),6,protected=(0,6))
    assert out.status=='COMPLETE' and out.certificate.minimum_deletions==0
    assert verify_mark_erasure_certificate(out.certificate)


def test_forged_erasure_claim_and_cap_refused():
    out=certify_mark_erasures(tuple(range(11)),10,protected=(0,10))
    with pytest.raises(ValueError):
        verify_mark_erasure_certificate(replace(out.certificate,minimum_deletions=3))
    limited=certify_mark_erasures(tuple(range(11)),10,max_pairs=2)
    assert limited.status=='BUDGET_EXHAUSTED' and limited.certificate is None
    with pytest.raises(ValueError):verify_mark_erasure_certificate(out.certificate,max_pairs=2)


def test_all_small_supports_and_protected_choices_match_exhaustive_deletion():
    for H in range(1,7):
        for bits in range(1,1<<(H+1)):
            s=tuple(i for i in range(H+1) if bits>>i&1)
            for p in [(),tuple(x for x in (0,H) if x in s),s[::2],s]:
                cert=certify_mark_erasures(s,H,protected=p).certificate
                assert cert.minimum_deletions==brute_erasure(s,H,p)


def test_tail_order_real_modular_cases():
    for n in range(2,30):
        for a in range(1,n):
            if gcd(n,a)>1:continue
            r=1;z=a%n
            while z!=1:z=z*a%n;r+=1
            for H in [1,2,r,max(1,r-1),r+1,2*r+1]:
                ans=tail_ruler_order(n,a,H)
                assert ans.order==(r if r<=H else None)


@pytest.mark.parametrize('bad',[True,0,-1,2.0,'12'])
def test_construction_bad_horizon(bad):
    with pytest.raises(ValueError):tail_ruler_parameters(bad)


def test_deletion_preserves_identification_not_original_mass():
    from enterprise_math.group_ring_sparse_identifiability import collision_spectrum
    dense=tuple(range(11));small=(0,1,6,8,10)
    assert high_band_identifiable(dense,10) and high_band_identifiable(small,10)
    assert collision_spectrum(dense,(1,)*len(dense),10)[0]==121
    assert collision_spectrum(small,(1,)*len(small),10)[0]==25

def test_inclusion_minimal_is_not_global_minimum():
    greedy=prune_identifying_support(tail_ruler(19),19)
    better=(0,1,2,9,13,16,19)
    assert verify_support_reduction(greedy) and len(greedy.support)==8
    assert high_band_identifiable(better,19) and len(better)==7
