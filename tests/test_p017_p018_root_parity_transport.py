from enterprise_math.p017_p018_root_parity_transport import root_parity_transport


def test_root_p3_to_p2_parity_defect_transport_is_exact() -> None:
    for k in (4, 5, 10, 17, 31, 100, 203, 500, 1000):
        data = root_parity_transport(k)
        assert data["transport_identity"]
        assert data["d2_parity_defect"] == 2 * data["prime_count_from_d2"]
        assert data["d2_parity_defect"] == (
            data["d3_parity_defect"]
            - 2 * data["squarefree_triple_count"]
            - data["repeated_triple_count"]
        )
        assert data["repeated_triple_count"] <= data["repeated_triple_capacity_bound"]
        assert data["status"] == "ROOT_P3_TO_P2_PARITY_DEFECT_TRANSPORT"


def test_repeated_root_p3_triple_columns_are_single_use() -> None:
    for k in (31, 100, 203, 500, 1000):
        data = root_parity_transport(k)
        seen = set()
        for p, value, offset in data["repeated_triple_rows"]:
            assert p not in seen
            seen.add(p)
            assert data["p3_cutoff"] < p <= data["p2_cutoff"]
            assert value == k * k + offset
            assert value % (p * p) == 0
