from enterprise_math.prime_brc_signed_support_nogo import (
    hit_support,
    large_modulus_signed_terms,
    signed_large_modulus_boundary_examples,
    support_injective_certificate,
    tail_core_static_support_nogo,
)


def test_exact_support_is_injective_for_moduli_up_to_k():
    for k in range(2, 60):
        seen = {}
        for d in range(1, k + 1):
            support = hit_support(k, d)
            assert len(support) >= 2
            assert support not in seen
            seen[support] = d
        support_injective_certificate(k, 1, k)


def test_tail_core_has_no_large_modulus_signed_sector():
    data = tail_core_static_support_nogo(31, 985)  # 985=5*197
    assert data["smooth_core"] == 5
    assert data["large_prime_tail"] == 197
    assert data["large_modulus_moduli"] == ()
    assert data["current_supports_pairwise_distinct"]
    assert large_modulus_signed_terms(31, 985) == ()


def test_smooth_sector_can_have_same_singleton_support_with_opposite_signs():
    data = signed_large_modulus_boundary_examples()
    smooth = data["smooth_witness"]
    assert smooth["support"] == (105,)
    assert (21, 1) in smooth["modulus_sign_pairs"]
    assert (105, -1) in smooth["modulus_sign_pairs"]
