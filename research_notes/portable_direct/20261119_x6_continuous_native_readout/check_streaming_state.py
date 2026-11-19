#!/usr/bin/env python3
"""Exact finite BRC checks for minimal continuing X6 feedback observers.

Run beside the preserved baseline package, or pass its package directory,
repository root, or exact check_relation_updates.py path.
The source carrier retains named III branches; this program tests explicitly
scoped observation quotients, never a deletion of the original BRC history.
"""

from collections import Counter, defaultdict
import hashlib
import importlib.util
from itertools import permutations, product
import json
from pathlib import Path
import sys


KERNEL_SHA256 = "83175b298bb8d18b43e2936043cf42f73efb476fa8b6581d4c9cdcd147af2ee0"
SOURCE_REVISION = "ef720decf4a35a276e509964250571a55421b9f8"
LAWS = ("persistent", "ingress", "egress", "stationary")


def import_kernel(path):
    path = Path(path).resolve()
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != KERNEL_SHA256:
        raise ValueError(f"BRC source mismatch: {digest}")
    spec = importlib.util.spec_from_file_location("x6_relation_brc", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def kernel_path(argument=None):
    baseline = "20261119_x6_native_relational_feedback"
    if argument is None:
        return Path(__file__).resolve().parent.parent / baseline / "check_relation_updates.py"
    path = Path(argument)
    if path.is_file():
        return path
    direct = path / "check_relation_updates.py"
    if direct.is_file():
        return direct
    return path / "research_notes" / "portable_direct" / baseline / "check_relation_updates.py"


def key(carrier, twist):
    return (carrier.read_signs(), tuple(twist),
            tuple(token.axis for token in carrier.tokens))


def names(state):
    out = [None] * 3
    for source, axis in enumerate(state[2]):
        out[axis] = source
    return tuple(out)


def relation(state):
    s, a, _ = state
    return tuple(s[i] * a[i] * s[(i + 1) % 3] for i in range(3))


def changes(r, law):
    if law == "persistent":
        return (1, 1, 1)
    offset = {"ingress": 0, "egress": -1, "stationary": 1}[law]
    return tuple(-r[(i + offset) % 3] for i in range(3))


def advance(carrier, twist, law):
    state = key(carrier, twist)
    change = changes(relation(state), law)
    output = carrier.apply(twist)
    next_twist = tuple(twist[i] * change[i] for i in range(3))
    assert output.sources == carrier.sources
    assert len(output.history) == len(carrier.history) + 1
    assert tuple(branch.source for branch in output.history[-1].joint_branches) == (
        tuple(token.source for token in carrier.tokens))
    assert all(branch.branch_name == "INNER" and branch.multiplicity == 1
               for branch in output.history[-1].joint_branches)
    return output, next_twist


def colors(signatures):
    palette = {}
    return {state: palette.setdefault(signature, len(palette))
            for state, signature in signatures.items()}


def stable_partition(states, transitions, output):
    current = colors({state: output(state) for state in states})
    counts = [len(set(current.values()))]
    while True:
        refined = colors({state: (output(state), tuple(
            current[transitions[law][state]] for law in LAWS)) for state in states})
        counts.append(len(set(refined.values())))
        if refined == current:
            return current, counts
        current = refined


def verify_partition(partition, quotient):
    forward, reverse = defaultdict(set), defaultdict(set)
    for state, color in partition.items():
        image = quotient(state)
        forward[color].add(image)
        reverse[image].add(color)
    assert all(len(x) == 1 for x in forward.values())
    assert all(len(x) == 1 for x in reverse.values())


def run(kernel):
    states = tuple((s, a, axes) for s, a, axes in
                   product(kernel.SIGNS, kernel.TWISTS, permutations(range(3))))
    assert len(states) == 192 and len(set(states)) == 192
    transitions = {law: {} for law in LAWS}
    traces = {}
    transition_checks = 0
    for state in states:
        s, a, axes = state
        carrier = kernel.NamedTriadBRC.lift(s, axes)
        assert key(carrier, a) == state
        r = relation(state)
        p = names(state)
        for law in LAWS:
            after, twist = advance(carrier, a, law)
            target = key(after, twist)
            assert target in states
            transitions[law][state] = target
            d = changes(r, law)
            assert relation(target) == tuple(d[i] * r[(i - 1) % 3] for i in range(3))
            assert names(target) == tuple(p[(i - 1) % 3] for i in range(3))
            for j in range(3):
                assert target[0][j] == s[j] * r[(j - 1) % 3]
            transition_checks += 1
        current, twist = carrier, a
        trace = []
        for t in range(61):
            trace.append(key(current, twist))
            if t < 60:
                current, twist = advance(current, twist, "ingress")
        assert all(trace[t + 6] == trace[t] for t in range(55))
        assert len(current.history) == 60
        traces[state] = trace

    observer_rows = []
    gauge_checks = sampling_checks = stride_checks = 0
    for j in range(3):
        types = {
            "raw_sign": (lambda state: state[0][j],
                         lambda state: (state[0][j], relation(state)), 8, 24),
            "adjacent_product": (lambda state: relation(state)[(j - 1) % 3],
                                 relation, 4, 48),
            "named_raw_sign": (lambda state: (names(state)[j], state[0][j]),
                               lambda state: (names(state), state[0][j], relation(state)),
                               48, 4),
        }
        for label, (output, quotient, expected, fiber_size) in types.items():
            partition, refinements = stable_partition(states, transitions, output)
            assert len(set(partition.values())) == expected
            assert set(Counter(partition.values()).values()) == {fiber_size}
            verify_partition(partition, quotient)
            observer_rows.append({"axis": j, "observer": label,
                                  "stable_states": expected,
                                  "fixed_width_bits": (expected - 1).bit_length(),
                                  "skeletons_per_fiber": fiber_size,
                                  "partition_refinement_counts": refinements})

        for state in states:
            s, a, axes = state
            for epsilon in kernel.SIGNS:
                if epsilon[j] != 1:
                    continue
                target = (tuple(epsilon[i] * s[i] for i in range(3)),
                          kernel.edge_gauge(a, epsilon), axes)
                assert target[0][j] == s[j]
                assert relation(target) == relation(state)
                assert names(target) == names(state)
                assert all(traces[target][t][0][j] == traces[state][t][0][j]
                           for t in range(7))
                gauge_checks += 1
            y = [sample[0][j] for sample in traces[state]]
            assert all(y[t + 3] == -y[t] for t in range(58))
            assert all(y[t] == (-1) ** (t // 3) * y[t % 3] for t in range(61))
            u = (y[0], relation(state))
            assert u[1][(j - 1) % 3] == y[0] * y[1]
            assert u[1][(j - 2) % 3] == -y[0] * y[2]
            assert u[1][j] == y[1] * y[2]

        for mask in range(64):
            offsets = tuple(t for t in range(6) if mask & (1 << t))
            m = len({t % 3 for t in offsets})
            fibers = defaultdict(set)
            for state in states:
                word = tuple(traces[state][t][0][j] for t in offsets)
                fibers[word].add(relation(state))
            assert len(fibers) == 2 ** m
            expected = 4 if m == 0 else 2 ** (3 - m)
            assert {len(fiber) for fiber in fibers.values()} == {expected}
            sampling_checks += 1
        for stride in range(1, 13):
            for length in (1, 2, 3, 6):
                fibers = defaultdict(set)
                for state in states:
                    word = tuple(traces[state][k * stride][0][j] for k in range(length))
                    fibers[word].add(relation(state))
                expected = 4 if stride % 3 == 0 else (4, 2, 1)[min(length, 3) - 1]
                assert {len(fiber) for fiber in fibers.values()} == {expected}
                stride_checks += 1

    left = ((1, 1, 1), (-1, 1, 1), (0, 1, 2))
    right = ((1, -1, 1), (1, -1, 1), (0, 1, 2))
    assert relation(left) == relation(right) == (-1, 1, 1)
    assert all(traces[left][t][0][0] == traces[right][t][0][0] for t in range(61))
    assert left[0][1] != right[0][1]

    return {
        "schema": "X6_STREAMING_OBSERVER_MINIMALITY_CHECK_V1",
        "status": "PASS",
        "source_revision": SOURCE_REVISION,
        "baseline_package_commit": "5806c80973d881009a755e8b5c922dab758a1032",
        "brc_kernel_sha256": KERNEL_SHA256,
        "entrypoint": "check_streaming_state.py:run -> NamedTriadBRC.apply",
        "input_carrier": "192 current signed/twisted named triad skeletons in a fixed X6 embedding; original sources and ordered III paths retained",
        "operation_semantics": "Four declared source-derived local twist updates, each using an actual named III BRC scatter; repeated ingress feedback for sampling",
        "observer_and_future_scope": "Fixed-axis raw signs, adjacent products, or current source-name/sign pairs; arbitrary finite known compositions of the four actions",
        "residual_certificate": "Exact stable-fiber equality to 4-, 8-, and 48-state observers; explicit off-axis counterexample; no native permission or physical clock calibration inferred",
        "counts": {"internal_skeletons": len(states),
                   "source_preserving_action_transitions": transition_checks,
                   "retained_ingress_event_steps": len(states) * 60,
                   "gauge_fiber_checks": gauge_checks,
                   "sampling_subset_cases": sampling_checks,
                   "stride_and_length_cases": stride_checks},
        "observer_partitions": observer_rows,
        "sampling_theorem": {"sufficient_and_necessary": "all three known event-offset residues modulo 3 are represented",
                             "equal_stride": "three samples suffice iff stride is not divisible by 3",
                             "proof_scope": "arbitrary finite or infinite sample sets by y[n]=(-1)^(n//3)*w[n%3]"},
        "off_axis_witness": {"left": left, "right": right,
                             "fixed_axis": 0, "distinguishing_axis": 1},
        "source_name_scope": "At each shell only the current source name at the fixed port is read; three future names recover the six assignments",
    }


if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_streaming_state.py [BASELINE_PACKAGE_OR_REPO_OR_KERNEL]")
    result = run(import_kernel(kernel_path(sys.argv[1] if len(sys.argv) == 2 else None)))
    target = Path(__file__).with_name("streaming_state_results.json")
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "counts": result["counts"],
                      "output": target.name}, ensure_ascii=False))
