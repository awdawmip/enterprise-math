#!/usr/bin/env python3
"""R022 pass-8 finite future-language/precision Galois and descent-monoid checks."""
from itertools import product
import json


def set_partitions(n):
    items = list(range(n))
    out = {}

    def rec(rest):
        if not rest:
            yield []
            return
        first = rest[0]
        for p in rec(rest[1:]):
            yield [{first}] + [set(b) for b in p]
            for i in range(len(p)):
                q = [set(b) for b in p]
                q[i].add(first)
                yield q

    for p in rec(items):
        canon = tuple(sorted(tuple(sorted(b)) for b in p))
        out[canon] = canon
    return list(out.values())


def relation(partition):
    return {(x, y) for block in partition for x in block for y in block}


def compose(f, g):
    """f after g."""
    return tuple(f[g[x]] for x in range(len(f)))


def kernel_for_language(n, observable, language):
    blocks = {}
    for x in range(n):
        signature = tuple(observable[f[x]] for f in language)
        blocks.setdefault(signature, []).append(x)
    return tuple(sorted(tuple(v) for v in blocks.values()))


def observation_safe(observable, partition, f):
    for block in partition:
        if len({observable[f[x]] for x in block}) > 1:
            return False
    return True


def safe_operations(n, observable, partition, functions):
    return tuple(f for f in functions if observation_safe(observable, partition, f))


def respects_partition(partition, f):
    rel = relation(partition)
    return all((f[x], f[y]) in rel for x, y in rel)


def meet_partition(left, right, n):
    def block_id(partition, x):
        for i, block in enumerate(partition):
            if x in block:
                return i
        raise AssertionError("missing state")

    groups = {}
    for x in range(n):
        key = (block_id(left, x), block_id(right, x))
        groups.setdefault(key, []).append(x)
    return tuple(sorted(tuple(v) for v in groups.values()))


def galois_exhaustive_model():
    n = 4
    observable = (0, 0, 1, 1)
    functions = [tuple(v) for v in product(range(n), repeat=n)]
    partitions = set_partitions(n)
    pool = [
        tuple(range(n)),
        (1, 2, 3, 0),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (3, 2, 1, 0),
        (1, 1, 2, 2),
    ]
    languages = [
        tuple(pool[i] for i in range(len(pool)) if (mask >> i) & 1)
        for mask in range(1 << len(pool))
    ]
    safe_cache = {
        partition: safe_operations(n, observable, partition, functions)
        for partition in partitions
    }

    galois_pairs = 0
    union_pairs = 0
    language_closures = 0
    equivalence_closures = 0
    single_extensions = 0

    for language in languages:
        kernel = kernel_for_language(n, observable, language)
        for partition in partitions:
            lhs = all(f in safe_cache[partition] for f in language)
            rhs = relation(partition) <= relation(kernel)
            assert lhs == rhs
            galois_pairs += 1

        language_closure = safe_cache[kernel]
        assert all(f in language_closure for f in language)
        assert safe_cache[kernel_for_language(n, observable, language_closure)] == language_closure
        language_closures += 1

        for f in pool:
            extended = tuple(dict.fromkeys(language + (f,)))
            assert kernel_for_language(n, observable, extended) == meet_partition(
                kernel,
                kernel_for_language(n, observable, (f,)),
                n,
            )
            single_extensions += 1

    for partition in partitions:
        equivalence_closure = kernel_for_language(n, observable, safe_cache[partition])
        assert relation(partition) <= relation(equivalence_closure)
        assert safe_cache[equivalence_closure] == safe_cache[partition]
        equivalence_closures += 1

    for left in languages:
        for right in languages:
            union = tuple(dict.fromkeys(left + right))
            assert kernel_for_language(n, observable, union) == meet_partition(
                kernel_for_language(n, observable, left),
                kernel_for_language(n, observable, right),
                n,
            )
            union_pairs += 1

    return {
        "states": n,
        "functions": len(functions),
        "equivalences": len(partitions),
        "language_pool": len(pool),
        "languages": len(languages),
        "galois_pairs_checked": galois_pairs,
        "language_union_pairs_checked": union_pairs,
        "language_closures_checked": language_closures,
        "equivalence_closures_checked": equivalence_closures,
        "single_operation_extensions_checked": single_extensions,
        "counterexample": False,
    }


def descent_monoid_model():
    n = 4
    functions = [tuple(v) for v in product(range(n), repeat=n)]
    partitions = set_partitions(n)
    identity = tuple(range(n))
    pair_checks = 0

    for partition in partitions:
        descending = [f for f in functions if respects_partition(partition, f)]
        descending_set = set(descending)
        assert identity in descending_set
        for f in descending:
            for g in descending:
                assert compose(f, g) in descending_set
                pair_checks += 1

    return {
        "states": n,
        "functions": len(functions),
        "equivalences": len(partitions),
        "composition_pairs_checked": pair_checks,
        "monoid": True,
    }


def _find_observation_safe_nonmonoid(n):
    functions = [tuple(v) for v in product(range(n), repeat=n)]
    partitions = set_partitions(n)
    for observable in product((0, 1), repeat=n):
        if len(set(observable)) < 2:
            continue
        for partition in partitions:
            safe = set(safe_operations(n, observable, partition, functions))
            for f in safe:
                for g in safe:
                    if compose(f, g) not in safe:
                        return True
    return False


def observation_safe_nonmonoid_kill():
    assert not _find_observation_safe_nonmonoid(2)

    n = 3
    observable = (0, 0, 1)
    partition = ((0, 2), (1,))
    functions = [tuple(v) for v in product(range(n), repeat=n)]
    f = (0, 2, 0)
    g = (0, 0, 1)
    fg = compose(f, g)
    safe = set(safe_operations(n, observable, partition, functions))
    assert f in safe and g in safe and fg not in safe

    return {
        "no_counterexample_states_2": True,
        "minimal_counterexample_states": 3,
        "observable": observable,
        "equivalence": partition,
        "f": f,
        "g": g,
        "composition": fg,
        "f_safe": True,
        "g_safe": True,
        "composition_safe": False,
        "lesson": "one-step observation safety is not compositionally closed; quotient descent is the monoid-strength condition",
    }


def incremental_refinement_witness():
    n = 4
    observable = (0, 0, 1, 1)
    identity = tuple(range(n))
    flip = (2, 1, 0, 3)
    old = kernel_for_language(n, observable, (identity,))
    new = kernel_for_language(n, observable, (identity, flip))
    by_new_observation = meet_partition(
        old,
        kernel_for_language(n, observable, (flip,)),
        n,
    )
    assert new == by_new_observation
    return {
        "old_kernel": old,
        "new_kernel": new,
        "local_split_law_holds": True,
        "lesson": "adding one future splits only old classes distinguished by the new observable",
    }


def run_all():
    return {
        "galois_exhaustive": galois_exhaustive_model(),
        "descent_monoid": descent_monoid_model(),
        "observation_safe_nonmonoid_kill": observation_safe_nonmonoid_kill(),
        "incremental_refinement": incremental_refinement_witness(),
    }


def self_test():
    out = run_all()
    g = out["galois_exhaustive"]
    assert g["galois_pairs_checked"] == 960
    assert g["language_union_pairs_checked"] == 4096
    assert not g["counterexample"]
    assert out["descent_monoid"]["monoid"]
    kill = out["observation_safe_nonmonoid_kill"]
    assert kill["minimal_counterexample_states"] == 3
    assert not kill["composition_safe"]
    assert out["incremental_refinement"]["local_split_law_holds"]


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
