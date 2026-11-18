"""Verify the one-port parity theorem against the original X6 V1 and V5 kernels.

Usage: python check_port.py PATH_TO_ENTERPRISE_MATH_CHECKOUT
The three imported source files must match the listed immutable Git blobs.
"""
from collections import Counter, defaultdict
from contextlib import redirect_stdout
from hashlib import sha1
from io import StringIO
from itertools import permutations, product
from math import prod
from pathlib import Path
import json
import runpy
import sys

SCATTER = "experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py"
KERNEL = "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
GAUGE = "experiments/x6_signed_internal_q_correction_v5_20260906/check_signed_internal_q_correction.py"
PINS = {
    SCATTER: "cf5bc031b90b26d82216925d2768583db4e10f57",
    KERNEL: "300a96e3dc24bf6fff73743037a0347a8bc83176",
    GAUGE: "0104cf5cedd40831a94eec746394f977402ac36f",
}


def check(condition, message):
    if not condition:
        raise ValueError(message)


def import_sources(root):
    for path, expected in PINS.items():
        buf = (root / path).read_bytes()
        digest = sha1(b"blob " + str(len(buf)).encode() + b"\0" + buf).hexdigest()
        check(digest == expected, "Wrong source version: " + path)
    with redirect_stdout(StringIO()):
        scatter = runpy.run_path(str(root / SCATTER))
        gauge = runpy.run_path(str(root / GAUGE))
    return scatter, gauge


def shell_trace(frame, weights, gauge):
    # The twist belongs to the AXIS edge. Slots are named tokens and move.
    orbit = []
    for _ in range(6):
        orbit.append(frame)
        departing_edges = tuple(weights[abs(token)-1] for token in frame)
        frame = gauge["twisted_step"](frame, departing_edges)
    check(frame == orbit[0], "Six shell updates must close")
    return orbit


def radial_sign(frame, axis):
    return next((1 if token > 0 else -1) for token in frame if abs(token) == axis+1)


def position(token, pivot):
    axis = abs(token)-1
    return tuple(x + (1 if token > 0 else -1) * (i == axis) for i, x in enumerate(pivot))


def experiment(root):
    scatter, gauge = import_sources(root)
    counts = Counter()
    length_fibres = defaultdict(set)
    twists = sorted(gauge["TWISTS"])
    anchors = [(0,)*6, (3,-2,1,0,-4,7)]
    seen_example = None
    for axes in permutations(range(6), 3):
        for twist in twists:
            weights = dict(zip(axes, twist))
            for signs in product((-1,1), repeat=3):
                frame = tuple((axis+1)*sign for axis, sign in zip(axes, signs))
                orbit = shell_trace(frame, weights, gauge)
                parity = prod(signs)
                counts["frames_with_twist"] += 1
                for tick, state in enumerate(orbit):
                    current_parity = prod(radial_sign(state,k) for k in axes)
                    check(current_parity == (-1)**tick*parity, "Parity clock")
                    counts["phase_parity_checks"] += 1
                for pivot in anchors:
                    options = [scatter["midpoint_options"](position(a,pivot),position(b,pivot))
                               for a,b in zip(orbit[0],orbit[1])]
                    common = set.intersection(*(set(pair) for pair in options))
                    check(common == {pivot}, "Incorrect common Cell")
                    counts["joint_midpoint_checks"] += 1
                if twist == (-1,)*3:
                    q = scatter["q_triad"](axes)
                    for initial, advanced in zip(frame, orbit[1]):
                        check(scatter["act"](q,position(initial,anchors[0])) == position(advanced,anchors[0]),
                              "V1 scatter and V5 tokenwise step disagree")
                for j, detector in enumerate(axes):
                    trace = [radial_sign(st,detector) for st in orbit]
                    opposite = weights[axes[(j+1)%3]]
                    check(prod(trace[:3])*opposite == parity, "Opposite edge calibration")
                    check(trace[3:] == [-s for s in trace[:3]], "Half-period reversal")
                    counts["fixed_port_histories"] += 1
                    for h in range(13):
                        nplus = sum(trace[t%6] == 1 for t in range(h))
                        length_fibres[axes,twist,j,h,nplus].add(parity)
                    # Reverse an unobserved axis, keeping the detector fixed.
                    invisible = axes[(j+1)%3]
                    eps = tuple(-1 if axis == invisible else 1 for axis in range(6))
                    frame2 = gauge["gauge_frame"](frame,eps)
                    twist2 = gauge["gauge_alpha"](frame,twist,eps)
                    orbit2 = shell_trace(frame2,dict(zip(axes,twist2)),gauge)
                    visible = tuple(axis for axis in axes if axis != invisible)
                    check(prod(radial_sign(frame2,k) for k in axes) == -parity, "Parity failed to flip")
                    check(all(radial_sign(u,k)==radial_sign(v,k) for u,v in zip(orbit,orbit2)
                              for k in visible), "Two-detector gauge witness failed")
                    check(all(gauge["passage"](u) == gauge["passage"](v) for u,v in zip(orbit,orbit2)),
                          "Unsigned passage failed to agree")
                    counts["two_port_gauge_counterpairs"] += 1
                    if axes == (0,1,2) and detector == 0 and twist == (-1,)*3 and signs == (1,)*3:
                        seen_example = {"twist":twist,"initial":frame,"conjugate_twist":twist2,
                                        "conjugate_initial":frame2,"one_port":trace}
    for (*_,h,nplus),possible in length_fibres.items():
        check(len(possible) == (1 if h%6==3 else 2), "Consecutive-window criterion")
    counts["consecutive_window_output_fibres"] = len(length_fibres)
    # All time masks in one period, independently test both distribution and
    # single-run recovery criteria against a complete 8-sign truth table.
    for weights in twists:
        for mask in range(64):
            coeffs = []
            intercept = None
            samples = {}
            for bits in product((0,1), repeat=3):
                frame = tuple((i+1)*(2*b-1) for i,b in enumerate(bits))
                orbit = shell_trace(frame,dict(enumerate(weights)),gauge)
                score = sum(radial_sign(orbit[t],0)>0 for t in range(6) if mask>>t&1)
                samples[bits] = score
            intercept = samples[(0,0,0)]
            for i in range(3):
                unit = tuple(int(i==k) for k in range(3))
                coeffs.append(samples[unit]-intercept)
            hist = [Counter(),Counter()]
            for bits, score in samples.items():
                check(score == intercept+sum(x*y for x,y in zip(bits,coeffs)), "Affine score")
                hist[sum(bits)%2][score] += 1
            disjoint = not (hist[0].keys() & hist[1].keys())
            equal = hist[0] == hist[1]
            triple_zero = any(sum(d*s for d,s in zip(coeffs,signs)) == 0
                              for signs in product((-1,1),repeat=3))
            check(equal == (0 in coeffs), "Law identification criterion")
            check(disjoint == (0 not in coeffs and not triple_zero), "Single-shot criterion")
            counts["one_period_mask_twist_checks"] += 1
    return {"status":"PASS","source_blobs":PINS,"counts":dict(sorted(counts.items())),
            "canonical_example":seen_example,"exact_consecutive_lengths_mod_6":[3]}


if __name__ == "__main__":
    print(json.dumps(experiment(Path(sys.argv[1]).resolve()),ensure_ascii=False,indent=2))
