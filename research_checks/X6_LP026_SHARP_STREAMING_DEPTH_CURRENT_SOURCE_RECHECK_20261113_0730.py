#!/usr/bin/env python3
"""X6/LP026 regression for the §10 sharp online depth-side register.

Imports the real pinned coordinate/cover/signed-BRC modules.  Compares a
native signed-word dynamic program with a cover-plus-register program at
every layer and over the entire length-bounded endpoint ball.  This is a
test of the already-published auxiliary theorem, NOT a native Result,
CLAIM, independent Driver review, or a physical Heartbeat update law.

Source theorem:
research_notes/driver/2026-11-12_x6_finite_depth_signed_brc_cover_rotation_descent_and_minimum_memory.md#10
"""
from __future__ import annotations

from collections import defaultdict
from hashlib import sha1
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
COORD = ROOT / "experiments" / "x6_native_coordinate_completion_v7_20260905"
SIGNED = ROOT / "experiments" / "x6_signed_native_spatial_v16_20260905"
PINS = {
    COORD / "x6_coordinate.py": "dd6dd7e74b83be09bb7545ee92357eda445c6ca3",
    COORD / "x6_cover.py": "171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd",
    SIGNED / "signed_brc.py": "300a96e3dc24bf6fff73743037a0347a8bc83176",
}
for file, expected in PINS.items():
    raw = file.read_bytes()
    actual = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if actual != expected:
        raise AssertionError(("source pin mismatch", str(file), expected, actual))

sys.path[:0] = [str(COORD), str(SIGNED)]
from x6_coordinate import Coord6  # noqa: E402
from x6_cover import CoverState  # noqa: E402
from signed_brc import endpoint_multiplicity  # noqa: E402

NAX = 6
ZERO = (0,) * NAX
STEPS = tuple((i, d) for i in range(NAX) for d in (-1, +1))


def cover_of(z, modulus):
    h = min(z)
    r = tuple(x - h for x in z)
    return r, h % modulus


def encode(z, modulus, capacity):
    r, a = cover_of(z, modulus)
    h = min(z)
    q = (h - a) // modulus
    return r, a, q % capacity


def source_step(code, axis, direction, modulus, capacity):
    r, a, t = code
    source = CoverState(Coord6(r), a, modulus).step(axis, direction)
    v = tuple(x + (direction if j == axis else 0) for j, x in enumerate(r))
    carry = min(v)
    a_next = source.depth
    assert (a + carry - a_next) % modulus == 0
    lam = (a + carry - a_next) // modulus
    r_next = tuple(x - carry for x in v)
    assert source.coordinate.values == r_next, ("source mismatch", code, axis, direction)
    return source.coordinate.values, a_next, (t + lam) % capacity


def native_next(states):
    out = defaultdict(int)
    for z, count in states.items():
        for axis, direction in STEPS:
            zz = list(z)
            zz[axis] += direction
            out[tuple(zz)] += count
    return dict(out)


def coded_next(states, modulus, capacity):
    out = defaultdict(int)
    for code, count in states.items():
        for axis, direction in STEPS:
            out[source_step(code, axis, direction, modulus, capacity)] += count
    return dict(out)


def check(modulus, horizon):
    capacity = 1 + horizon // (3 * modulus)  # n=6: 1+floor(2H/(nm))
    native = {ZERO: 1}
    coded = {encode(ZERO, modulus, capacity): 1}
    ball_fibers = defaultdict(set)
    cross_length_code = {}
    transition_checks = 0
    source_brc_checks = 0
    for length in range(horizon + 1):
        assert sum(native.values()) == 12 ** length
        assert sum(coded.values()) == 12 ** length
        expected = defaultdict(int)
        for z, count in native.items():
            code = encode(z, modulus, capacity)
            expected[code] += count
            key = cover_of(z, modulus)
            ball_fibers[key].add(z)
            old = cross_length_code.setdefault(code, z)
            assert old == z, ("different endpoints share one bounded-horizon code", modulus, horizon, z, old)
            if length <= 4:
                assert endpoint_multiplicity(length, z) == count, (length, z)
                source_brc_checks += 1
        assert dict(expected) == coded, ("dynamic-program mismatch", modulus, horizon, length)
        if length < horizon:
            transition_checks += len(coded) * len(STEPS)
            native = native_next(native)
            coded = coded_next(coded, modulus, capacity)

    largest_fiber = max(map(len, ball_fibers.values()))
    assert largest_fiber == capacity, ("sharp information capacity mismatch", modulus, horizon, largest_fiber, capacity)
    return transition_checks, source_brc_checks, len(ball_fibers)


def main():
    transitions = 0
    brc = 0
    fibers = 0
    cases = 0
    for modulus in range(1, 7):
        for horizon in range(0, 7):
            t, b, f = check(modulus, horizon)
            transitions += t
            brc += b
            fibers += f
            cases += 1
    print("PASS_X6_LP026_SHARP_STREAMING_DEPTH_SOURCE_IMPORT")
    print("source_git_blob_sha1_pins", {str(k.relative_to(ROOT)): v for k, v in PINS.items()})
    print("moduli_1_to_6_horizons_0_to_6", cases)
    print("actual_source_CoverState_step_checks", transitions)
    print("actual_source_signed_BRC_comparisons", brc)
    print("cover_ball_fiber_groups_checked", fibers)


if __name__ == "__main__":
    main()
