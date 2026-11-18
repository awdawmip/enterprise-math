"""Compose three fixed-Port V5 SHELL reads with actual V39 word transport.

Usage: python integration.py /path/to/check_port.py /path/to/enterprise-math-checkout
Place verify_bowtie.py beside this script. Only the three pinned original files
used by check_port.import_sources are required from the source checkout.
"""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import permutations, product
import json
from math import prod
from pathlib import Path

import verify_bowtie as bow


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def import_protocol(path):
    spec = spec_from_file_location("shell_port_checker", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_causally(orbit, fixed_axis, radial_sign):
    frame = bow.IDENTITY
    occurrences = Counter()
    checkpoint_frames = []
    observed, choices = [], []
    for tick, state in enumerate(orbit[:3]):
        # Programmed instrument: the choice needs only the sign observed now.
        y = radial_sign(state, fixed_axis)
        word = "ACB" if y > 0 else "ABC"
        observed.append(y)
        choices.append(word)
        for symbol in word:
            frame = bow.after(bow.BLOCK_FRAME[symbol], frame)
            occurrences.update(bow.RING_EXPANSION[symbol])
        if tick in (1, 2):
            checkpoint_frames.append(frame)
    return observed, choices, checkpoint_frames, occurrences


def decode(frames, calibrated_edge):
    r, t = [bow.FRAMES.index(f) for f in frames]
    last_bit = (t - r) % 3
    require(last_bit in (0, 1), "Third source bit is not identifiable")
    positive_count = r + last_bit
    observed_sign_product = (-1) ** (3 - positive_count)
    return calibrated_edge * observed_sign_product


def run(checker_path, root):
    port = import_protocol(checker_path)
    _, gauge = port.import_sources(root)
    expected_ledger = Counter({"A+": 3, "A-": 3, "B+": 3, "B-": 3})
    counts = Counter()
    law_counts = defaultdict(Counter)
    patterns = Counter()
    proof_rows = sha256()
    canonical = {}

    for axes in permutations(range(6), 3):
        for twist in sorted(gauge["TWISTS"]):
            weights = dict(zip(axes, twist))
            for signs in product((-1, 1), repeat=3):
                frame = tuple((axis + 1) * s for axis, s in zip(axes, signs))
                orbit = port.shell_trace(frame, weights, gauge)
                for j, fixed_axis in enumerate(axes):
                    ys, words, hs, ledger = read_causally(orbit, fixed_axis, port.radial_sign)
                    chi = weights[axes[(j + 1) % 3]]
                    answers = (prod(signs), decode(hs, chi))
                    require(answers[0] == answers[1], "Native initial product reconstruction")
                    require(ledger == expected_ledger, "Different matched directed transfer histogram")
                    require(prod(ys) * chi == answers[0], "Native sign calibration identity")
                    exponents = tuple(bow.FRAMES.index(h) for h in hs)
                    context = (axes, twist, fixed_axis)
                    law_counts[context][(exponents[-1], answers[0])] += 1
                    patterns[tuple(ys)] += 1
                    counts["native_input_histories"] += 1
                    counts["identical_directional_histogram_checks"] += 1
                    proof_rows.update(json.dumps(
                        [axes, twist, frame, fixed_axis, ys, words, hs, chi, *answers],
                        separators=(",", ":")).encode() + b"\n")
                    if axes == (0, 1, 2) and fixed_axis == 0:
                        canonical[(twist, tuple(ys))] = {
                            "axes_zero_based": axes, "fixed_axis_zero_based": fixed_axis,
                            "axis_edge_twist": twist, "signed_initial_tokens": frame,
                            "first_three_shell_radial_signs": ys, "words": words,
                            "h2_h3": hs, "h2_h3_exponents": exponents,
                            "opposite_edge_calibration": chi,
                            "initial_sign_product": answers[0],
                            "decoded_sign_product": answers[1], "ring_counts": dict(ledger)}

    target_contexts = 120 * 4 * 3
    require(len(law_counts) == target_contexts, "Missing orientation/twist/detector context")
    require(counts["native_input_histories"] == target_contexts * 8, "Coverage incomplete")
    require(set(patterns.values()) == {target_contexts} and len(patterns) == 8, "Unequal masks")
    for distribution in law_counts.values():
        score = sum(max(distribution[(h, 1)], distribution[(h, -1)]) for h in range(3))
        require(score == 7 and sum(distribution.values()) == 8, "One-terminal optimum")
    allneg = (-1, -1, -1)
    pos, neg = (1, 1, 1), (-1, -1, -1)
    # Same calibration and terminal frame, different intermediate frames/sign products.
    p, q = canonical[(allneg, pos)], canonical[(allneg, neg)]
    require(p["h2_h3"][1] == q["h2_h3"][1] and p["h2_h3"][0] != q["h2_h3"][0]
            and p["initial_sign_product"] == -q["initial_sign_product"], "Temporal witness")
    # Change gauge of an unobserved axis. The entire visible time series and
    # V39 frames agree; calibrating edge and desired initial product flip.
    r = p["signed_initial_tokens"]
    eps = (1, -1, 1, 1, 1, 1)
    r2 = gauge["gauge_frame"](r, eps)
    tw2 = gauge["gauge_alpha"](r, allneg, eps)
    q2 = canonical[(tuple(tw2), pos)]
    require(q2["signed_initial_tokens"] == tuple(r2) and p["h2_h3"] == q2["h2_h3"]
            and p["opposite_edge_calibration"] == -q2["opposite_edge_calibration"]
            and p["initial_sign_product"] == -q2["initial_sign_product"], "Gauge witness")
    o1 = port.shell_trace(r, dict(enumerate(allneg)), gauge)
    o2 = port.shell_trace(r2, dict(enumerate(tw2)), gauge)
    require([port.radial_sign(s, 0) for s in o1] == [port.radial_sign(s, 0) for s in o2],
            "Gauge pair differs outside the initial three ticks")
    return {"status": "PASS", "counts": dict(counts),
            "three_input_strings_per_calibrated_context": 8,
            "calibrated_contexts_with_7_of_8_one_frame_and_8_of_8_two_frames": len(law_counts),
            "three_sign_multiplicities": {"".join("+" if s > 0 else "-" for s in k): v
                                          for k, v in sorted(patterns.items())},
            "common_directed_ring_ledger": dict(expected_ledger), "net_current": [0, 0],
            "example_terminal_collision_resolved_at_second_checkpoint": [p, q],
            "example_calibration_necessity_even_with_all_port_times": [p, q2],
            "rows_sha256": proof_rows.hexdigest(),
            "source_blobs_checked_at_runtime": port.PINS,
            "macros_commit": "ed0b15b4ba948a21150969478d8a6941db76b11f",
            "scope": "Designed causal readout, V1/V5 at native source and V39 based-loop target; the physical signed three-force trigger has not been inferred."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("check_port", type=Path)
    parser.add_argument("source_root", type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.check_port, args.source_root), ensure_ascii=False, indent=2))
