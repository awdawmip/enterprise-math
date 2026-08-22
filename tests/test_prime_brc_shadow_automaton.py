from enterprise_math.prime_brc_shadow_automaton import (
    carry_to_support,
    minimal_state_certificate,
    shadow_refinement_path,
    shadow_refinement_state,
    support_to_carry,
)


def test_sum_detail_bijection_has_exactly_four_states():
    cert = minimal_state_certificate()
    assert cert["required_state_count"] == 4
    assert cert["realized_state_count"] == 4
    for support in cert["support_patterns"]:
        assert carry_to_support(*support_to_carry(*support)) == support


def test_k8_q13_dyadic_shadow_path_is_11_to_01_to_00():
    # Edge multipliers are 5 (lower) and 6 (upper). Scale 2 selects upper;
    # scale 4 divides neither, so the support then dies.
    path = shadow_refinement_path(8, 5, (2, 2))
    assert tuple(item["support"] for item in path["records"]) == (
        (1, 1),
        (0, 1),
        (0, 0),
    )


def test_refinement_is_path_flat_on_factor_reordering():
    # k=21,p=13 gives an edge whose lower/upper multipliers are 13,14.
    a = shadow_refinement_path(21, 13, (2, 7))
    b = shadow_refinement_path(21, 13, (7, 2))
    assert a["cumulative_scale"] == b["cumulative_scale"] == 14
    assert a["final_support"] == b["final_support"]
    assert a["final_support"] == shadow_refinement_state(21, 13, 14)["support"]


def test_no_side_resurrection_dense():
    for k in range(8, 80):
        for p in range(k // 2 + 1, k):
            try:
                state = shadow_refinement_state(k, p, 1)
            except ValueError:
                continue
            assert state["support"] == (1, 1)
            for factors in ((2,), (3,), (2, 3), (3, 2), (2, 2, 3)):
                path = shadow_refinement_path(k, p, factors)
                supports = [tuple(item["support"]) for item in path["records"]]
                for prev, nxt in zip(supports, supports[1:]):
                    assert nxt[0] <= prev[0]
                    assert nxt[1] <= prev[1]
