#!/usr/bin/env python3
"""R022 pass-10 aggregation-semantics gate for recoalescence."""
import json


def aggregate(values, op, zero):
    out = zero
    for value in values:
        out = op(out, value)
    return out


def bool_union(a, b):
    return a | b


def nat_add(a, b):
    return a + b


def min_op(a, b):
    return min(a, b)


def duplicate_forgetting_examples():
    boolean_two = aggregate([{1}, {1}], bool_union, set())
    boolean_one = aggregate([{1}], bool_union, set())
    count_two = aggregate([1, 1], nat_add, 0)
    count_one = aggregate([1], nat_add, 0)
    min_two = aggregate([5, 5], min_op, float("inf"))
    min_one = aggregate([5], min_op, float("inf"))
    return {
        "boolean_support_duplicate_forget_exact": boolean_two == boolean_one,
        "natural_multiplicity_duplicate_forget_exact": count_two == count_one,
        "min_score_duplicate_forget_exact": min_two == min_one,
        "lesson": "forgetful duplicate recoalescence is exact exactly on reachable idempotent aggregate values",
    }


def coefficient_preserving_merge():
    explicit = aggregate([3, 3, 3, 3], nat_add, 0)
    grouped_value = 4 * 3
    return {
        "explicit_sum": explicit,
        "grouped_coefficient_value": grouped_value,
        "exact": explicit == grouped_value,
        "coefficient": 4,
        "lesson": "non-idempotent semantics can group equal residual values only if multiplicity/coefficient is retained",
    }


def zero_prune_examples():
    return {
        "natural_zero_prune_exact": aggregate([7, 0], nat_add, 0) == 7,
        "boolean_bottom_prune_exact": aggregate([{1}, set()], bool_union, set()) == {1},
        "min_infinity_prune_exact": aggregate([4, float("inf")], min_op, float("inf")) == 4,
        "lesson": "identity/bottom pruning is monoid-generic, unlike duplicate forgetting",
    }


def provenance_strengthening_kill():
    support_values = [{"ok"}, {"ok"}]
    support_merged = [{"ok"}]
    provenance_values = [{"h1"}, {"h2"}]
    provenance_merged_wrong = [{"h1"}]
    provenance_merged_exact = [{"h1", "h2"}]
    return {
        "support_merge_exact": aggregate(support_values, bool_union, set()) == aggregate(support_merged, bool_union, set()),
        "provenance_forget_exact": aggregate(provenance_values, bool_union, set()) == aggregate(provenance_merged_wrong, bool_union, set()),
        "provenance_union_token_exact": aggregate(provenance_values, bool_union, set()) == aggregate(provenance_merged_exact, bool_union, set()),
        "lesson": "two branches equal under support semantics need not be semantically equal after provenance is promoted to the observable",
    }


def algebraic_gate_table():
    return {
        "identity_prune": "valid in any commutative monoid when branch value is the identity",
        "forget_equal_duplicates": "requires idempotence s⊕s=s on reachable semantic values",
        "coefficient_group_equal_duplicates": "valid in commutative monoids with retained natural-number multiplicity action",
        "pairwise_collective_absorption": "requires idempotent order/semilattice structure; not monoid-generic",
        "frontier_set_cover": "requires the distributive/join-prime support regime from pass 7",
    }


def run_all():
    return {
        "duplicate_forgetting": duplicate_forgetting_examples(),
        "coefficient_merge": coefficient_preserving_merge(),
        "zero_prune": zero_prune_examples(),
        "provenance_kill": provenance_strengthening_kill(),
        "algebraic_gate": algebraic_gate_table(),
    }


def self_test():
    out = run_all()
    d = out["duplicate_forgetting"]
    assert d["boolean_support_duplicate_forget_exact"]
    assert not d["natural_multiplicity_duplicate_forget_exact"]
    assert d["min_score_duplicate_forget_exact"]
    assert out["coefficient_merge"]["exact"]
    z = out["zero_prune"]
    assert z["natural_zero_prune_exact"] and z["boolean_bottom_prune_exact"] and z["min_infinity_prune_exact"]
    p = out["provenance_kill"]
    assert p["support_merge_exact"]
    assert not p["provenance_forget_exact"]
    assert p["provenance_union_token_exact"]


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
