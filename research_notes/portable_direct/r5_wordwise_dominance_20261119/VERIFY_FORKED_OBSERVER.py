#!/usr/bin/env python3
"""Check common-origin fork counterexample and the <=|Y| failure certificate."""
from itertools import product
from VERIFY_WORDWISE_DOMINANCE import transformation_monoid, bfs_certificate
import json


def fixed_witnesses(monoid, labels, x, Y):
    ys = [y for y in range(len(labels)) if Y & (1 << y)]
    return [y for y in ys if all(labels[f[x]] & ~labels[f[y]] == 0
                                  for f in monoid)]


def fork_failure_certificate(monoid, labels, x, Y):
    """For each losing candidate y choose one whole-word transformation."""
    ys = [y for y in range(len(labels)) if Y & (1 << y)]
    if fixed_witnesses(monoid, labels, x, Y):
        return None
    forks = []
    for y in ys:
        f = next(f for f in monoid if labels[f[x]] & ~labels[f[y]])
        if f not in forks:
            forks.append(f)
    assert 1 <= len(forks) <= len(ys)
    thresholds = tuple(labels[f[x]] for f in forks)
    before = all((labels[f[x]] & q) == q
                 for f, q in zip(forks, thresholds))
    after = any(all((labels[f[y]] & q) == q
                    for f, q in zip(forks, thresholds)) for y in ys)
    assert before and not after
    return len(forks)


def complete_three_state():
    n = 3
    action_set = list(product(range(n), repeat=n))
    checks = fixed_yes = fixed_no = wordwise_safe_but_fork_unsafe = 0
    for a in action_set:
        for b in action_set:
            monoid = transformation_monoid((a, b), n)
            for labels in product((0, 1), repeat=n):
                for Y in range(1, 1 << n):
                    for x in range(n):
                        if Y & (1 << x):
                            continue
                        fixed = bool(fixed_witnesses(monoid, labels, x, Y))
                        cert = fork_failure_certificate(monoid, labels, x, Y)
                        assert (cert is None) == fixed
                        checks += 1
                        fixed_yes += int(fixed)
                        fixed_no += int(not fixed)
                        if not fixed and bfs_certificate((a, b), labels, x, Y)[0]:
                            wordwise_safe_but_fork_unsafe += 1
    assert checks == 52488
    return dict(checks=checks, fixed_witness_yes=fixed_yes,
                fixed_witness_no=fixed_no,
                wordwise_safe_but_fork_unsafe=wordwise_safe_but_fork_unsafe)


def explicit_five_state():
    a = (3, 4, 3, 3, 4)
    b = (3, 3, 4, 3, 4)
    labels = (1, 1, 1, 1, 0)
    monoid = transformation_monoid((a, b), 5)
    Y = 6
    assert bfs_certificate((a, b), labels, 0, Y)[0]
    assert not fixed_witnesses(monoid, labels, 0, Y)
    assert fork_failure_certificate(monoid, labels, 0, Y) == 2
    before = all(labels[f[0]] & 1 for f in (a, b))
    after = any(all(labels[f[y]] & 1 for f in (a, b)) for y in (1, 2))
    assert before and not after
    return dict(initial_x=0, initial_Y=[1, 2],
                fork_words=["a", "b"], fork_size=2,
                joint_query={"a": 1, "b": 1},
                joint_query_before=True, joint_query_after=False)


if __name__ == "__main__":
    result = {
        "schema": "EM_R5_FORKED_OBSERVER_CHECK_V1",
        "result": "PASS",
        "complete_n3": complete_three_state(),
        "explicit_n5": explicit_five_state(),
        "inference": "bounded <=|Y| fork failures certify no common future witness; finite-Y necessity from intersection argument"
    }
    print(json.dumps(result, indent=2, sort_keys=True))
