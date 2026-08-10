from enterprise_math.p017_p018_p3_cubic_type3_bridge import (
    p3_cubic_type3_partition,
    p3_rough_triple_states,
)


def test_p3_cutoff_triple_least_factor_stays_below_p2_cubic_cutoff():
    for k in range(4, 61):
        data = p3_rough_triple_states(k)
        for a, b, c, value, offset in data["triple_states"]:
            assert data["p3_cutoff"] < a <= data["p2_cutoff"]
            assert a <= b <= c
            assert value == a * b * c == k * k + offset


def test_cubic_routing_partitions_triples_into_high_and_balanced_low_boxes():
    for k in range(4, 81):
        data = p3_cubic_type3_partition(k)
        assert data["all_triples_partitioned"] is True
        assert data["route_status"] == "BALANCED_TYPE_III_BOX_ISOLATED"
        H = data["cubic_horizon"]
        L = data["cubic_low_factor_floor"]
        U = data["upper"]
        for a, b, c, root, value, offset in data["cubic_high_unbalanced_triples"]:
            assert a < L
            assert root > H
            assert value == a * b * c == k * k + offset
        for a, b, c, root, value, offset in data["cubic_low_balanced_triples"]:
            assert L <= a <= b <= c
            assert root <= H
            assert c * L * L <= U
            assert value == a * b * c == k * k + offset
