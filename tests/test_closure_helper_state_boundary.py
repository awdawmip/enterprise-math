from enterprise_math.closure_helper_state_boundary import (
    helper_state_tradeoff,
    pure_nontrivial_circuits,
)


def test_fixed_raw_alphabet_has_only_the_k_ary_nontrivial_circuit():
    for arity in range(2, 7):
        circuits = pure_nontrivial_circuits(arity)
        assert len(circuits) == 1
        circuit = circuits[0]
        assert len(circuit.premise) == arity
        assert circuit.root == "z"


def test_binary_compilation_pays_helpers_and_depth_but_preserves_raw_projection():
    for arity in range(2, 7):
        report = helper_state_tradeoff(arity)
        assert report.fixed_alphabet_required_premise_arity == arity
        assert report.helper_label_count == max(0, arity - 2)
        assert report.compiled_max_premise_arity == 2
        assert report.compiled_depth == arity - 1
        assert report.raw_projection_verified


def test_five_way_fixture_exposes_three_resource_axes():
    report = helper_state_tradeoff(5)
    assert (
        report.fixed_alphabet_required_premise_arity,
        report.helper_label_count,
        report.compiled_max_premise_arity,
        report.compiled_depth,
    ) == (5, 3, 2, 4)
