from enterprise_math.p017_four_support_aggregate import (
    anchor_surviving_exact_four_support_hit,
    direct_anchor_surviving_four_support_mass,
    four_support_anchor_surviving_mass,
)


def test_historical_k58_negative_support_survives_corrected_scope() -> None:
    hit = anchor_surviving_exact_four_support_hit(58, [3, 5, 7, 11])
    assert hit is not None
    assert hit["state"] == 3465
    assert hit["cofactor"] == 3
    assert hit["cofactor_prime_factors"] == (3,)
    assert hit["anchor_surviving"] is True

    aggregate = four_support_anchor_surviving_mass(58)
    matches = [
        item
        for item in aggregate["contributions"]
        if item["support"] == (3, 5, 7, 11)
    ]
    assert len(matches) == 1
    assert matches[0]["tail"] == -2


def test_anchor_contaminated_hit_is_outside_transformed_large_region() -> None:
    # 271^2 < 73710 < 272^2 and
    # 73710 = 2 * 3^4 * 5 * 7 * 13.
    # The transverse support is {3,5,7,13}, but 2 is an anchor prime because
    # 2 | 272.  Supplement 02's large-region identity sums only anchor-surviving
    # states, so this hit must be rejected rather than misclassified as an exact
    # transformed four-support contribution.
    assert anchor_surviving_exact_four_support_hit(271, [3, 5, 7, 13]) is None


def test_support_reindexing_matches_direct_state_scan() -> None:
    for k in (20, 30, 40, 58, 80):
        by_support = four_support_anchor_surviving_mass(k)
        by_state = direct_anchor_surviving_four_support_mass(k)
        assert by_support["total_four_support_large_tail"] == by_state[
            "total_four_support_large_tail"
        ]

        support_rows = sorted(
            (
                int(item["state"]),
                tuple(item["support"]),
                int(item["tail"]),
            )
            for item in by_support["contributions"]
        )
        state_rows = sorted(
            (
                int(item["state"]),
                tuple(item["support"]),
                int(item["tail"]),
            )
            for item in by_state["contributions"]
            if int(item["support_product"]) > 2 * k
        )
        assert support_rows == state_rows
