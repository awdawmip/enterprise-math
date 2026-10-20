#!/usr/bin/env python3
"""Second-pass generic BRC certificate/exactness audit for R022.

Non-cryptographic finite-state models only.
"""
from dataclasses import dataclass
from itertools import product
from typing import FrozenSet, Tuple

LowLocal = Tuple[int, int]
Upper = Tuple[int, ...]
Branch = Tuple[LowLocal, ...]


@dataclass(frozen=True)
class ContextScopedNCC:
    depth: int
    connector_states_before: FrozenSet[int]
    low_local: LowLocal
    upper_local: int


def transition(states: FrozenSet[int], low: LowLocal, high: int) -> FrozenSet[int]:
    """Small nondeterministic connector with a one-bit hidden carry state."""
    a, b = low
    out = set()
    for carry in states:
        if a == high:
            if b == 0:
                out.add(carry)
            else:
                out.add(carry)
                out.add(1 - carry)
        elif b == carry:
            out.add(1 - carry)
    return frozenset(out)


def run(branch: Branch, upper: Upper):
    states = frozenset({0})
    trace = [states]
    for depth, (low, high) in enumerate(zip(branch, upper)):
        states = transition(states, low, high)
        trace.append(states)
        if not states:
            return False, depth, tuple(trace)
    return True, len(branch), tuple(trace)


def certificate(branch: Branch, upper: Upper):
    ok, depth, trace = run(branch, upper)
    if ok:
        return None
    return ContextScopedNCC(depth, trace[depth], branch[depth], upper[depth])


def certificate_applies(branch: Branch, upper: Upper, cert: ContextScopedNCC) -> bool:
    ok, depth, trace = run(branch, upper)
    if len(trace) <= cert.depth:
        return False
    return (
        trace[cert.depth] == cert.connector_states_before
        and branch[cert.depth] == cert.low_local
        and upper[cert.depth] == cert.upper_local
    )


def find_context_invalidation_witness(n: int = 5):
    base_upper = (0, 1, 0, 1, 1)
    branches = list(product(list(product([0, 1], [0, 1])), repeat=n))
    for branch in branches:
        cert = certificate(branch, base_upper)
        if cert is None or cert.depth < 2:
            continue
        mutated = list(base_upper)
        mutated[cert.depth] ^= 1
        mutated = tuple(mutated)
        ok2, _, _ = run(branch, mutated)
        if ok2:
            return {
                "branch": branch,
                "failure_depth": cert.depth,
                "base_upper": base_upper,
                "mutated_upper": mutated,
                "context_omission_would_false_prune": True,
            }
    raise AssertionError("expected context invalidation witness")


def find_reusable_ncc(n: int = 5):
    upper = (0, 1, 0, 1, 1)
    branches = list(product(list(product([0, 1], [0, 1])), repeat=n))
    best = None
    for branch in branches:
        cert = certificate(branch, upper)
        if cert is None or cert.depth < 1:
            continue
        matched = []
        for candidate in branches:
            if certificate_applies(candidate, upper, cert):
                matched.append(candidate)
        sound = all(run(candidate, upper)[0] is False and run(candidate, upper)[1] == cert.depth
                    for candidate in matched)
        if sound and (best is None or (cert.depth, len(matched)) > (best[0].depth, best[1])):
            best = (cert, len(matched))
    assert best is not None
    cert, count = best
    return {
        "failure_depth": cert.depth,
        "certified_branches": count,
        "dependency_footprint": {
            "connector_states_before": tuple(sorted(cert.connector_states_before)),
            "low_local": cert.low_local,
            "upper_local": cert.upper_local,
        },
        "sound": True,
    }


def budget_truncation_kill():
    """A width cap without an exact certificate destroys final support."""
    branches = ("a", "b")
    final_support = {"a": frozenset({0}), "b": frozenset({1})}
    exact = set().union(*(final_support[b] for b in branches))
    retained = branches[:1]
    truncated = set().union(*(final_support[b] for b in retained))
    return {
        "exact_support": tuple(sorted(exact)),
        "truncated_support": tuple(sorted(truncated)),
        "lost_results": tuple(sorted(exact - truncated)),
        "exact_without_prune_certificate": exact == truncated,
    }


def exactness_strata():
    """Semantic classes mined from the source architecture."""
    return {
        "exact_local_reduction": (
            "connector exact-state duplicate elimination under fixed context",
            "context-scoped no-completion prefix certificate reuse",
        ),
        "completeness_neutral_structure": (
            "forward/backward decomposition before truncation",
            "thread-level parallelism",
        ),
        "not_exact_without_extra_certificate": (
            "width/condition autobalancing truncation",
            "best-path/score pruning",
            "timeout kill and fixed k->k-1 rollback",
        ),
    }


def run_all():
    return {
        "context_scoped_ncc": find_reusable_ncc(),
        "context_invalidation_kill": find_context_invalidation_witness(),
        "budget_truncation_kill": budget_truncation_kill(),
        "exactness_strata": exactness_strata(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_all(), indent=2, default=list))
