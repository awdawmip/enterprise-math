from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations, product
from types import MappingProxyType

import pytest

from enterprise_math.group_ring_sparse_identifiability import (
    SparseCollisionCodebook, collision_spectrum, compile_sparse_codebook,
    period_closures, sparse_ruler, structural_alias, verify_codebook,
)
from enterprise_math.group_ring_support_certificates import (
    SupportCertificate, certify_runs, certify_support, support_runs, high_band_identifiable,
    verify_support_certificate, support_mark_lower_bound, order_from_certified_support,
    certify_readout_margin, verify_readout_margin, decode_bounded_readout,
)


def make_book(H, support, profiles):
    profiles = tuple(tuple(w) for w in profiles)
    codes = tuple(zip(*(collision_spectrum(support, w, H) for w in profiles)))
    book = SparseCollisionCodebook(H, tuple(support), profiles, codes,
                                  MappingProxyType({c: i+1 for i, c in enumerate(codes)}))
    verify_codebook(book)
    return book


@pytest.fixture
def scalar_book():
    return make_book(6, (0, 1, 2, 3, 6), ((47, 14, 65, 1, 66),))


@pytest.fixture
def binary_book():
    return compile_sparse_codebook(12, alphabet='binary').codebook


def test_high_band_matches_unchanged_closure_all_small_supports():
    for H in range(1, 9):
        for bits in range(1, 1 << (H+1)):
            support = tuple(x for x in range(H+1) if bits >> x & 1)
            out = certify_support(support, H)
            cert = out.certificate
            assert out.status == 'COMPLETE'
            assert verify_support_certificate(cert)
            labels = period_closures(support, H)
            expected = labels == tuple(range(1, H+1))+(0,)
            assert (cert.status == 'IDENTIFYING') == expected
            assert high_band_identifiable(support, H) == expected
            if not expected:
                a, b = cert.alias
                assert labels[a-1] == labels[b-1]
            else:
                assert len(support) >= support_mark_lower_bound(H)


def test_exact_third_boundary_and_missing_compulsory_witness():
    out = certify_support((0, 4, 5, 6), 6).certificate
    assert out.missing_lag == 3
    assert out.alias == (3, 6)
    assert verify_support_certificate(out)
    out = certify_support((0, 1, 5, 7, 9), 9).certificate
    assert out.status == 'IDENTIFYING'  # Missing lag 3 is permitted at H/3.


def test_above_horizon_alias_is_not_reported_as_exact_order():
    out = certify_support((0, 1), 7).certificate
    assert out.status == 'ALIASED'
    a, b = out.alias
    assert b == 8
    assert verify_support_certificate(out)


def test_compact_large_horizon_is_never_expanded():
    H = 10**30+2
    b = (H+2)//3
    out = certify_runs(((0, b), (H-b, H)), H)
    assert out.status == 'COMPLETE'
    assert out.required_run_pairs == 3
    assert len(out.certificate.cover) <= 2
    assert verify_support_certificate(out.certificate)


def test_all_complete_block_rulers_have_positive_certificate():
    for H in range(1, 257):
        out = certify_support(sparse_ruler(H), H)
        assert out.certificate.status == 'IDENTIFYING'
        assert verify_support_certificate(out.certificate)


def test_runs_merge_exactly_and_do_not_fill_holes():
    assert support_runs((0, 1, 2, 4, 5, 8), 9) == ((0, 2), (4, 5), (8, 8))
    cert = certify_support((0, 4, 5, 6), 6).certificate
    assert cert.runs == ((0, 0), (4, 6))


@pytest.mark.parametrize('runs,H', [
    ((), 4), (((0, 1), (2, 4)), 4), (((0, 3), (3, 4)), 4),
    (((3, 4), (0, 1)), 4), (((0, 5),), 4), (((0, True),), 4),
    (((-1, 1),), 4), (((0, 0),), 0), (((0, 1, 2),), 4),
])
def test_reject_invalid_compact_supports(runs, H):
    with pytest.raises((ValueError, TypeError)):
        certify_runs(runs, H)


def test_budget_exhaustion_is_not_a_negative_certificate():
    out = certify_support((0, 1, 5, 7, 9), 9, max_run_pairs=1)
    assert out.status == 'BUDGET_EXHAUSTED'
    assert out.certificate is None
    assert out.evaluated_run_pairs == 0


def test_reject_forged_positive_cover():
    cert = certify_support((0, 1, 5, 7, 9), 9).certificate
    with pytest.raises(ValueError):
        verify_support_certificate(replace(cert, cover=cert.cover[:-1]))
    with pytest.raises(ValueError):
        verify_support_certificate(replace(cert, cover=((20, 21),)))
    with pytest.raises(ValueError):
        verify_support_certificate(replace(cert, alias=(3, 6)))


def test_reject_forged_negative_alias():
    cert = certify_support((0, 4, 5, 6), 6).certificate
    with pytest.raises(ValueError):
        verify_support_certificate(replace(cert, alias=(3, 7)))
    with pytest.raises(ValueError):
        verify_support_certificate(replace(cert, missing_lag=4, alias=(4, 7)))
    with pytest.raises(ValueError):
        verify_support_certificate(replace(cert, status='BUDGET_EXHAUSTED'))


def test_scalar_margin_and_midpoint_boundary(scalar_book):
    cert = certify_readout_margin(scalar_book, normalized=False)
    assert cert.minimum_gap == 226
    assert set(cert.critical_pair) == {3, 6}
    assert cert.executed_pair_checks == 6
    assert verify_readout_margin(scalar_book, cert)
    mid = (17417+17191)//2
    got = decode_bounded_readout(scalar_book, (mid,), 113, normalized=False)
    assert got.status == 'AMBIGUOUS' and got.candidates == (3, 6)
    got = decode_bounded_readout(scalar_book, (mid,), 112, normalized=False)
    assert got.status == 'INCONSISTENT'
    for r, row in enumerate(scalar_book.codes, 1):
        for sign in (-1, 1):
            got = decode_bounded_readout(scalar_book, (row[0]+sign*112,), 112,
                                         normalized=False)
            assert got.candidates == (r,)


def test_normalized_margin_is_invariant_under_weight_scaling(scalar_book):
    scaled = make_book(scalar_book.horizon, scalar_book.support,
                      (tuple(10*x for x in scalar_book.profiles[0]),))
    a = certify_readout_margin(scalar_book)
    b = certify_readout_margin(scaled)
    assert a.minimum_gap == b.minimum_gap == F(226, 193**2)
    assert certify_readout_margin(scaled, normalized=False).minimum_gap == 22600


def test_normalized_scalar_packing_bound(scalar_book):
    cert = certify_readout_margin(scalar_book)
    baseline = scalar_book.codes[-1][0]
    scale = sum(scalar_book.profiles[0])**2
    assert cert.minimum_gap <= (1-F(baseline, scale))/scalar_book.horizon
    assert (1-F(baseline, scale))/scalar_book.horizon <= F(
        len(scalar_book.support)-1, len(scalar_book.support)*scalar_book.horizon)


def test_erasure_margin_matches_every_erased_subset(binary_book):
    codes = binary_book.codes
    t = len(binary_book.profiles)
    for erased_count in range(min(3, t)):
        cert = certify_readout_margin(binary_book, normalized=False,
                                       erased_channels=erased_count)
        want = min(max(abs(codes[i][j]-codes[k][j]) for j in range(t) if j not in E)
                   for i, k in combinations(range(len(codes)), 2)
                   for E in combinations(range(t), erased_count))
        assert cert.minimum_gap == want
        assert verify_readout_margin(binary_book, cert)


def test_multichannel_noise_and_erasures_at_exact_boundary(binary_book):
    cert = certify_readout_margin(binary_book, normalized=False, erased_channels=1)
    a, b = cert.critical_pair
    values = tuple(F(x+y, 2) for x, y in zip(binary_book.codes[a-1], binary_book.codes[b-1]))
    out = decode_bounded_readout(binary_book, values, cert.minimum_gap/2,
                                 normalized=False, erased=cert.critical_erased)
    assert out.status == 'AMBIGUOUS'
    assert a in out.candidates and b in out.candidates


def test_exact_noisy_decoder_preserves_above_horizon(scalar_book):
    out = decode_bounded_readout(scalar_book, scalar_book.codes[-1], 0, normalized=False)
    assert out.status == 'ORDER_ABOVE_HORIZON_CONDITIONAL'
    assert out.order is None and out.lower_bound == 7


def test_margin_budget_has_no_fake_gap(binary_book):
    out = certify_readout_margin(binary_book, max_pair_checks=0)
    assert out.status == 'BUDGET_EXHAUSTED'
    assert out.minimum_gap is None and out.executed_pair_checks == 0


def test_reject_forged_margin_and_forged_codebook(scalar_book):
    cert = certify_readout_margin(scalar_book)
    with pytest.raises(ValueError):
        verify_readout_margin(scalar_book, replace(cert, minimum_gap=cert.minimum_gap+1))
    bad = replace(scalar_book, codes=((0,),)+scalar_book.codes[1:])
    with pytest.raises(ValueError):
        certify_readout_margin(bad)
    with pytest.raises(ValueError):
        decode_bounded_readout(bad, (0,), 0)


@pytest.mark.parametrize('epsilon', [-1, 0.01, True, float('nan')])
def test_no_floats_or_invalid_error_bounds(scalar_book, epsilon):
    with pytest.raises(ValueError):
        decode_bounded_readout(scalar_book, (1,), epsilon)


def test_invalid_noise_dimensions_and_unmarked_corruption(scalar_book):
    for values, erased in [((0, 1), ()), ((0,), (0,)), ((0,), (2,)), ((0,), (True,))]:
        with pytest.raises(ValueError):
            decode_bounded_readout(scalar_book, values, 0, erased=erased)
    with pytest.raises(ValueError):
        certify_readout_margin(scalar_book, erased_channels=1)
    with pytest.raises(ValueError):
        decode_bounded_readout(scalar_book, (0.1,), 0)


def test_custom_support_order_executes_original_gcd_backend():
    S = (0, 1, 5, 7, 9)
    cert = certify_support(S, 9).certificate
    assert order_from_certified_support(7, 2, S, cert).order == 3
    assert order_from_certified_support(7, 3, S, cert).order == 6
    out = order_from_certified_support(101, 2, S, cert)
    assert out.status == 'ORDER_ABOVE_HORIZON' and out.lower_bound == 10
    with pytest.raises(ValueError):
        order_from_certified_support(7, 3, (0, 1, 4, 7, 9), cert)
    with pytest.raises(ValueError):
        order_from_certified_support(7, 2, (0, 4, 5, 6),
            certify_support((0, 4, 5, 6), 6).certificate)


def test_boolean_highband_has_no_horizon_array():
    assert high_band_identifiable((0, 10**100), 10**100) is False
