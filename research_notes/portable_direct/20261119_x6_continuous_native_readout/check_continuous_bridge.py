#!/usr/bin/env python3
"""Compose the named X6 feedback carrier with the repeatable V39 reader.

Run beside the preceding feedback package, or pass that package/repository root.
All source events use the imported, source-pinned NamedTriadBRC extension.
Every packet appends its actual directed ring word to a carried network frame.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
import json
from pathlib import Path
import sys

import check_streaming_state as observer
import check_v39_stream_bridge as packet


def recover(q, axis):
    r = [0] * 3
    r[(axis - 1) % 3] = q[0]
    r[(axis - 2) % 3] = -q[0] * q[1]
    r[axis] = q[1]
    return tuple(r)


def run(kernel):
    counts = Counter()
    boundary_fibers = defaultdict(set)
    sample = None
    windows = 8
    last_sample = 3 * (windows - 1) + 2
    for signs, initial_twist, assignment in product(
            kernel.SIGNS, kernel.TWISTS, permutations(range(3))):
        current = kernel.NamedTriadBRC.lift(signs, assignment)
        twist = initial_twist
        shells = [current]
        twists = [twist]
        for _ in range(last_sample + 2):
            current, twist = observer.advance(current, twist, "ingress")
            shells.append(current)
            twists.append(twist)
            counts["named_source_events"] += 1
        counts["full_named_inputs"] += 1
        for axis, spacing in product(range(3), (1, 3)):
            phase, frame = 0, packet.E
            directed_history = ()
            for k in range(windows):
                start = spacing * k
                window_name = f"axis-{axis}:spacing-{spacing}:window-{k}"
                reads = []
                for event in range(start, start + 3):
                    token = next(t for t in shells[event].tokens if t.axis == axis)
                    reads.append(packet.NamedRead(
                        f"{token.source}:axis-{axis}:event-{event}", event, token.sign))
                leaf = packet.execute_window(window_name, reads, phase, frame)
                q = leaf.decoded_relation
                assert recover(q, axis) == kernel.relations(
                    shells[start].read_signs(), twists[start])
                phase, frame = leaf.final_phase, leaf.frame_after_macros[-1]
                directed_history += leaf.directed_history
                assert phase == int(q == (1, -1))
                assert Counter(x.direction for x in directed_history) == {
                    "A+": k + 1, "A-": k + 1, "B+": k + 1, "B-": k + 1}
                end = start + 2
                final_r = kernel.relations(shells[end].read_signs(), twists[end])
                final_y = shells[end].read_signs()[axis]
                assert q == (final_r[axis], final_r[(axis - 2) % 3])
                future_word = tuple(shells[t].read_signs()[axis]
                                    for t in range(end, end + 3))
                boundary_fibers[axis, final_r, final_y].add((frame, future_word))
                counts["decoded_source_windows"] += 1
                counts["source_to_network_sample_links"] += 3
                counts["directed_ring_occurrences"] += len(leaf.directed_history)
                if sample is None and phase == 1 and k > 0:
                    sample = {"axis": axis, "spacing": spacing,
                              "named_initial_assignment": assignment,
                              "source_window_start": start,
                              "reads": [{"name": x.name, "event": x.source_event,
                                         "sign": x.sign} for x in reads],
                              "relation_at_window_start": recover(q, axis),
                              "macro_word": leaf.macro_word,
                              "initial_network_frame": leaf.initial_frame,
                              "observed_frame": leaf.frame_after_macros[1],
                              "final_network_frame": frame,
                              "source_relation_at_last_sample": final_r,
                              "source_last_sign": final_y}
            assert len(directed_history) == 4 * windows
    assert len(boundary_fibers) == 24
    assert all(len(v) == 1 for v in boundary_fibers.values())
    assert counts == {"named_source_events": 4800, "full_named_inputs": 192,
                      "decoded_source_windows": 9216,
                      "source_to_network_sample_links": 27648,
                      "directed_ring_occurrences": 36864}
    return {
        "schema": "X6_CONTINUOUS_SOURCE_TO_V39_BRIDGE_CHECK_V1",
        "status": "PASS",
        "source_revision": observer.SOURCE_REVISION,
        "baseline_revision": "5806c80973d881009a755e8b5c922dab758a1032",
        "input_carrier": "192 named signed/twisted triad skeletons in a declared Heartbeat X6 three-axis embedding",
        "operation_semantics": "Actual NamedTriadBRC ingress-feedback scatters followed by source-indexed repeatable V39 macro composition",
        "observer_scope": "Three fixed-port consecutive source-event samples; disjoint or one-event sliding accepted windows; carried network frame initialized once at identity",
        "retained_provenance": "Full named source carrier, joint III paths and event order; actual sample source names/indices; every directed packet-ring occurrence",
        "timing_scope": "Logical accepted-window interface; complete windows are retained and serialized; no physical clock synchronization assumed",
        "residual_certificate": "Zero initial-window relation ambiguity, exact accumulated-frame carry, and eight source-sign/network boundary classes per fixed axis",
        "counts": dict(counts),
        "joint_sign_network_boundary_classes_per_axis": 8,
        "example": sample,
    }


if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_continuous_bridge.py [BASELINE_PACKAGE_OR_REPOSITORY]")
    kernel = observer.import_kernel(observer.kernel_path(
        sys.argv[1] if len(sys.argv) == 2 else None))
    result = run(kernel)
    Path(__file__).with_name("continuous_bridge_results.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], **result["counts"]}))
