#!/usr/bin/env python3
"""Compare the new named BRC extension with the original X6 V1/V5 kernels.

Run: python check_native_embedding.py /path/to/enterprise-math
The input checkout only needs the three pinned experiment files below.
The two sibling check modules provide this contribution's typed extensions.
"""

from collections import Counter
from contextlib import redirect_stdout
from hashlib import sha1
from io import StringIO
from itertools import permutations, product
import json
from pathlib import Path
import runpy
import sys

import check_relation_updates as rel
import check_v39_relational_packets as packet


SOURCE_REVISION = "ef720decf4a35a276e509964250571a55421b9f8"
SCATTER = "experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py"
KERNEL = "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
GAUGE = "experiments/x6_signed_internal_q_correction_v5_20260906/check_signed_internal_q_correction.py"
PINS = {SCATTER: "cf5bc031b90b26d82216925d2768583db4e10f57",
        KERNEL: "300a96e3dc24bf6fff73743037a0347a8bc83176",
        GAUGE: "0104cf5cedd40831a94eec746394f977402ac36f"}


def import_sources(root):
    for path, expected in PINS.items():
        raw = (root / path).read_bytes()
        actual = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if actual != expected:
            raise ValueError("Source blob mismatch: " + path)
    with redirect_stdout(StringIO()):
        scatter = runpy.run_path(str(root / SCATTER))
        gauge = runpy.run_path(str(root / GAUGE))
    return scatter, gauge


def native_frame(carrier, axes):
    return tuple(t.sign * (axes[t.axis] + 1) for t in carrier.tokens)


def position(signed_axis, anchor):
    axis = abs(signed_axis) - 1
    sign = 1 if signed_axis > 0 else -1
    return tuple(c + sign * (i == axis) for i, c in enumerate(anchor))


def decode_packet_frames(frames):
    first = packet.FRAMES.index(frames[0])
    second = (packet.FRAMES.index(frames[1]) - first) % 3
    assert first in (0, 1) and second in (0, 1)
    return 1 - 2 * first, 1 - 2 * second


def check(root):
    scatter, gauge = import_sources(root)
    counters = Counter()
    sample = None
    for axes in permutations(range(6), 3):
        for signs, initial_a in product(rel.SIGNS, rel.TWISTS):
            carrier = rel.NamedTriadBRC.lift(signs)
            original = native_frame(carrier, axes)
            current = original
            a = initial_a
            shells = [signs]
            counters["six_axis_embedded_inputs"] += 1
            first_successor = None
            for tick in range(6):
                before_signs = carrier.read_signs()
                edge_by_axis = dict(zip(axes, a))
                departing = tuple(edge_by_axis[abs(t) - 1] for t in current)
                advanced = gauge["twisted_step"](current, departing)
                carrier = carrier.apply(a)
                assert advanced == native_frame(carrier, axes)
                assert tuple(t.source for t in carrier.tokens) == (
                    "source-0", "source-1", "source-2")
                a = tuple(-before_signs[i] * before_signs[(i + 1) % 3]
                          for i in range(3))
                current = advanced
                shells.append(carrier.read_signs())
                counters["original_v5_feedback_steps"] += 1
                if tick == 0:
                    first_successor = current
                if tick == 2:
                    assert current == tuple(-t for t in original)
                    assert a == initial_a
            assert current == original and a == initial_a
            assert len(carrier.history) == 6
            # This is finite-frame periodicity; ordered path history is retained.
            for anchor in ((0,) * 6, (3, -2, 1, 0, -4, 7)):
                mids = [scatter["midpoint_options"](position(u, anchor),
                                                    position(v, anchor))
                        for u, v in zip(original, first_successor)]
                assert set.intersection(*(set(pair) for pair in mids)) == {anchor}
                counters["original_brc_common_cell_checks"] += 1
            initial_r = rel.relations(signs, initial_a)
            for j in range(3):
                y = tuple(shells[t][j] for t in range(3))
                leaf = packet.relational_branch(y)
                q1, q2 = decode_packet_frames(leaf.frame_snapshots)
                recovered = [0] * 3
                recovered[(j - 1) % 3] = q1
                recovered[(j - 2) % 3] = -q1 * q2
                recovered[j] = q2
                assert tuple(recovered) == initial_r
                assert leaf.current == (0, 0)
                counters["feedback_to_v39_four_state_recoveries"] += 1
                single = packet.single_block_branch(y)
                single_q = packet.decode_single_block(single.frame_snapshots[1])
                assert single_q == (q1, q2)
                assert single.current == (0, 0)
                assert Counter(ring for _, ring in single.full_ring_history) == {
                    "A+": 1, "A-": 1, "B+": 1, "B-": 1}
                counters["single_intermediate_frame_recoveries"] += 1
                if sample is None and initial_r != (-1, -1, -1):
                    sample = {"axes": axes, "s": signs, "initial_twist": initial_a,
                              "detector": j, "readout": y, "r": initial_r,
                              "packet_words": [p.word for p in leaf.ordered_packets],
                              "frames": leaf.frame_snapshots,
                              "single_block_macros": [p.word for p in single.ordered_packets],
                              "single_observed_frame": single.frame_snapshots[1],
                              "generator_history": [e.generator for e in carrier.history]}
    assert counters == {"six_axis_embedded_inputs": 3840,
                        "original_v5_feedback_steps": 23040,
                        "original_brc_common_cell_checks": 7680,
                        "feedback_to_v39_four_state_recoveries": 11520,
                        "single_intermediate_frame_recoveries": 11520}
    return {"schema": "X6_NATIVE_RELATIONAL_FEEDBACK_EMBEDDING_CHECK_V1",
            "status": "PASS", "source_revision": SOURCE_REVISION,
            "original_kernel_blobs": PINS,
            "entrypoint": "check_native_embedding.py:check",
            "input_carrier": "120 ordered selections of three distinct X6 axes; 8 signed named frames; 4 V5 twists",
            "operation_semantics": "Original V5 tokenwise scatter, original signed-X6 shortest-path BRC midpoint operation, source-preserving feedback extension, R757/V39 packet composition",
            "observer_and_future_scope": "Six macro-event finite-state reversal/return; initial r through first three shell reads and either two relational packet boundaries or one intermediate S3 frame of a completed ABC-permutation block",
            "retained_provenance": "Named token slots, all six III scatter events, twist words, full directed ring words in both V39 controller variants",
            "residual_certificate": "Exact zero discrepancies against original kernels and zero r ambiguity; no native permission or physical time calibration inferred",
            "counts": dict(counters), "example": sample}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_native_embedding.py PATH_TO_ENTERPRISE_MATH")
    result = check(Path(sys.argv[1]).resolve())
    target = Path(__file__).with_name("native_embedding_results.json")
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], **result["counts"]}))
