#!/usr/bin/env python3
"""R022 third-pass Residual Certificate Algebra finite-state oracle.

This is generic/non-cryptographic. It models Boolean final-support semantics
over a finite residual language and tests exact branch-configuration rewrites.
"""
from collections import Counter
from itertools import combinations
import json


def signature_atoms(signature, language):
    return frozenset((u, y) for u in language for y in signature.get(u, ()))


def configuration_join(configuration, signatures, language):
    out = set()
    for branch in configuration:
        out.update(signature_atoms(signatures[branch], language))
    return frozenset(out)


def residual_join_certificate(lhs, rhs, signatures, language):
    return configuration_join(lhs, signatures, language) == configuration_join(rhs, signatures, language)


def minimum_existing_bases(configuration, signatures, language):
    configuration = tuple(configuration)
    target = configuration_join(configuration, signatures, language)
    for k in range(len(configuration) + 1):
        good = []
        for sub in combinations(configuration, k):
            if configuration_join(sub, signatures, language) == target:
                good.append(sub)
        if good:
            return good
    return []


def pairwise_dominated(configuration, branch, signatures, language):
    b = signature_atoms(signatures[branch], language)
    return any(branch != other and b <= signature_atoms(signatures[other], language) for other in configuration)


def removable_by_coalition(configuration, branch, signatures, language):
    lhs = tuple(configuration)
    rhs = tuple(x for x in lhs if x != branch)
    return residual_join_certificate(lhs, rhs, signatures, language)


def rjc_special_cases():
    signatures = {
        "a": {"u": {"ok"}},
        "b": {"u": {"ok"}},
        "dead": {"u": set()},
        "extra": {"u": {"other"}},
    }
    return {
        "rcc_as_idempotence": residual_join_certificate(("a", "b"), ("a",), signatures, ("u",)),
        "ncc_as_bottom_elimination": residual_join_certificate(("a", "dead"), ("a",), signatures, ("u",)),
        "wrong_nonempty_prune_rejected": not residual_join_certificate(("a", "extra"), ("a",), signatures, ("u",)),
        "congruence_under_configuration_union": residual_join_certificate(("a", "b", "extra"), ("a", "extra"), signatures, ("u",)),
    }


def collective_dominance_counterexample():
    signatures = {
        "A": {"u": {1, 2}},
        "B": {"u": {1, 3}},
        "C": {"u": {2, 3}},
    }
    config = ("A", "B", "C")
    return {
        "pairwise_dominated": {b: pairwise_dominated(config, b, signatures, ("u",)) for b in config},
        "collectively_removable": {b: removable_by_coalition(config, b, signatures, ("u",)) for b in config},
        "minimum_bases": [list(x) for x in minimum_existing_bases(config, signatures, ("u",))],
        "target_atoms": sorted(configuration_join(config, signatures, ("u",))),
    }


def antichain_greedy_trap():
    sets = {
        "S0": {0},
        "S1": {1, 2},
        "S2": {1, 3},
        "S3": {1, 4},
        "S4": {2, 3},
        "S5": {2, 4},
    }
    signatures = {k: {"u": v} for k, v in sets.items()}
    config = tuple(sets)
    target = configuration_join(config, signatures, ("u",))
    irredundant = []
    for k in range(1, len(config) + 1):
        for sub in combinations(config, k):
            if configuration_join(sub, signatures, ("u",)) != target:
                continue
            if all(configuration_join(tuple(x for x in sub if x != b), signatures, ("u",)) != target for b in sub):
                irredundant.append(sub)
    sizes = sorted(set(map(len, irredundant)))
    min_size = min(sizes)
    return {
        "pairwise_incomparable": all(not (sets[a] <= sets[b] or sets[b] <= sets[a]) for i, a in enumerate(config) for b in config[i + 1:]),
        "irredundant_basis_sizes": sizes,
        "minimum_bases": [list(x) for x in irredundant if len(x) == min_size],
        "larger_irredundant_examples": [list(x) for x in irredundant if len(x) > min_size][:2],
        "bad_greedy_removal_sequence": ["S4", "S5"],
        "bad_greedy_terminal_basis": ["S0", "S1", "S2", "S3"],
        "good_removal_sequence": ["S1", "S3", "S4"],
        "good_terminal_basis": ["S0", "S2", "S5"],
    }


def language_extension_kill():
    signatures = {
        "x": {"short": {"ok"}, "long": {"x-only"}},
        "y": {"short": {"ok"}, "long": {"y-only"}},
    }
    return {
        "exact_on_short_language": residual_join_certificate(("x",), ("y",), signatures, ("short",)),
        "exact_after_language_extension": residual_join_certificate(("x",), ("y",), signatures, ("short", "long")),
    }


def multiplicity_kill():
    signatures = {"p": {"u": {"ok"}}, "q": {"u": {"ok"}}}
    before = Counter({"ok": 2})
    after = Counter({"ok": 1})
    return {
        "support_merge_exact": residual_join_certificate(("p", "q"), ("p",), signatures, ("u",)),
        "multiplicity_before": dict(before),
        "multiplicity_after": dict(after),
        "multiplicity_preserved": before == after,
    }


def free_union_token_width_kill():
    signatures = {
        "A": {"u": {1, 2}},
        "B": {"u": {1, 3}},
        "C": {"u": {2, 3}},
    }
    existing = minimum_existing_bases(("A", "B", "C"), signatures, ("u",))
    target = configuration_join(("A", "B", "C"), signatures, ("u",))
    with_synth = dict(signatures)
    with_synth["UNION"] = {"u": {y for _, y in target}}
    return {
        "existing_token_min_width": len(existing[0]),
        "free_synthesized_union_token_width": len(minimum_existing_bases(("UNION",), with_synth, ("u",))[0]),
        "union_token_explicit_atom_count": len(target),
        "warning": "width=1 is vacuous if arbitrary exact union tokens/denotations are synthesized without charging their representation",
    }


def set_cover_reduction_witness():
    sets = {
        "S0": {1, 2, 3},
        "S1": {1, 4},
        "S2": {2, 5},
        "S3": {4, 5},
    }
    signatures = {k: {"only": v} for k, v in sets.items()}
    bases = minimum_existing_bases(tuple(sets), signatures, ("only",))
    return {
        "universe": sorted(set().union(*sets.values())),
        "minimum_cover_size": len(bases[0]),
        "minimum_exact_branch_bases": [list(x) for x in bases],
        "reduction": "singleton residual language; final outcomes are Set-Cover universe elements; branch signatures are the input subsets",
    }


def run_all():
    return {
        "rjc_special_cases": rjc_special_cases(),
        "collective_dominance": collective_dominance_counterexample(),
        "antichain_greedy_trap": antichain_greedy_trap(),
        "language_extension_kill": language_extension_kill(),
        "multiplicity_kill": multiplicity_kill(),
        "free_union_token_width_kill": free_union_token_width_kill(),
        "set_cover_reduction_witness": set_cover_reduction_witness(),
    }


def self_test():
    out = run_all()
    s = out["rjc_special_cases"]
    assert s["rcc_as_idempotence"] and s["ncc_as_bottom_elimination"]
    assert s["wrong_nonempty_prune_rejected"] and s["congruence_under_configuration_union"]
    d = out["collective_dominance"]
    assert not any(d["pairwise_dominated"].values())
    assert all(d["collectively_removable"].values())
    assert len(d["minimum_bases"]) == 3 and all(len(b) == 2 for b in d["minimum_bases"])
    g = out["antichain_greedy_trap"]
    assert g["pairwise_incomparable"] and g["irredundant_basis_sizes"] == [3, 4]
    l = out["language_extension_kill"]
    assert l["exact_on_short_language"] and not l["exact_after_language_extension"]
    m = out["multiplicity_kill"]
    assert m["support_merge_exact"] and not m["multiplicity_preserved"]
    f = out["free_union_token_width_kill"]
    assert f["existing_token_min_width"] == 2 and f["free_synthesized_union_token_width"] == 1
    c = out["set_cover_reduction_witness"]
    assert c["minimum_cover_size"] == 2 and c["minimum_exact_branch_bases"] == [["S0", "S3"]]


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
