from enterprise_math.closure_synergy_depth import synergy_chain, synergy_chain_report
from enterprise_math.closure_implication_bases import forward_chaining_trace


def test_k_way_direct_circuit_compiles_to_binary_rules_with_depth_k_minus_one():
    for arity in range(2, 7):
        report = synergy_chain_report(arity)
        assert report["raw_rooted_circuit_present"]
        assert report["iterative_max_premise_arity"] == 2
        assert report["raw_seed_derivation_rounds"] == arity - 1
        assert report["iterative_rule_count"] == arity - 1
        assert report["basis_sound"] and report["basis_complete"]


def test_missing_any_raw_antecedent_blocks_the_final_root():
    chain = synergy_chain(5)
    for missing in chain.antecedents:
        seed = frozenset(label for label in chain.antecedents if label != missing)
        final = forward_chaining_trace(seed, chain.rules)[-1]
        assert chain.root not in final


def test_full_raw_seed_reaches_root_only_after_helper_chain():
    chain = synergy_chain(5)
    trace = forward_chaining_trace(frozenset(chain.antecedents), chain.rules)
    assert len(trace) - 1 == 4
    assert chain.root not in trace[-2]
    assert chain.root in trace[-1]
