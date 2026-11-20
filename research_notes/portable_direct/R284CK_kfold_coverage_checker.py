#!/usr/bin/env python3
"""R284CK: exact finite proof checker for k-fold coverage of 64 frozen Port arcs.

No third-party packages; t=2*rho is integral at every critical radius.
Fourfold observation coordinate y4=4*y represents rational open-cell midpoints.
"""
import hashlib
import json
from itertools import product

P = 17179869143
D = (1120832, 6, 13, 1651128)
Z = (0, 390139, 394465, 1497639)
SELECT = (0, 1, 2, 4, 5, 6)
FROZEN_SHA = "b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4"
THRESHOLD_SHA = "332263f243b45d5f99a45ae6febaf15b0a9a9f4826bc275a76acb7288ec76601"


def determinant(lower, top):
    u1, a11, x, y, u2, w, a22, z, u3, g, h, r = lower
    t, s = 6 - a11, 13 - a22
    u = t * s - x * w
    v = -r * u - z * (t * h + x * g) - y * (w * h + s * g)
    p1, p2 = s * u1 + x * u2, t * u2 + w * u1
    q1 = -r * p1 - u1 * z * h + x * z * u3 + y * (u2 * h + s * u3)
    q2 = -r * p2 + t * z * u3 + u1 * z * g + y * (w * u3 - u2 * g)
    q3 = u * u3 + p1 * g + p2 * h
    k = (u * D[3] + v, p1 * D[3] + q1, p2 * D[3] + q2, q3)
    base = D[0] * k[0] - Z[1] * k[1] - Z[2] * k[2] - Z[3] * k[3] - sum(k)
    return base - sum(k[j] for j in range(4) if top & (1 << j))


def lower_state(key, fill):
    state = [fill] * 12
    for j, pos in enumerate(SELECT):
        state[pos] = 1 + ((key >> (5-j)) & 1)
    return state


def arc_data():
    arcs = []
    for key in range(64):
        a = determinant(lower_state(key, 2), 15)
        w = determinant(lower_state(key, 1), 0) - a
        assert 0 < w < P // 2
        arcs.append((a % P, w))
    return arcs


def direct_mask(arcs, y4, t):
    """Exact membership at y=y4/4, with expansion rho=t/2."""
    bits = 0
    for key, (a, w) in enumerate(arcs):
        if w + t >= P:
            bits |= 1 << key
            continue
        delta = (y4 - 4*a) % (4*P)
        if delta <= 4*w + 2*t or delta >= 4*P - 2*t:
            bits |= 1 << key
    return bits


def open_cells(arcs, t):
    """Return exact cell (left,right,count) in doubled-coordinate circle.

    Count is obtained by event sweep; direct_mask checks it independently.
    """
    events = []
    full = 0
    for key, (a, w) in enumerate(arcs):
        if w + t >= P:
            full |= 1 << key
        else:
            events.append(((2*a-t) % (2*P), key, 1))
            events.append(((2*(a+w)+t) % (2*P), key, -1))
    events.sort()
    if not events:
        return [(0, 2*P, 64)]
    first = next((x for x, _, _ in events if x > 0), 2*P)
    # The midpoint of (0,first) has exact fourfold coordinate y4=first.
    state = direct_mask(arcs, first, t)
    cells = [(0, first, state.bit_count())]
    j = 0
    while j < len(events) and events[j][0] == 0:
        j += 1  # initial state already is to the right of the zero cut
    while j < len(events):
        x = events[j][0]
        while j < len(events) and events[j][0] == x:
            _, key, direction = events[j]
            if direction == 1:
                state |= 1 << key
            else:
                state &= ~(1 << key)
            j += 1
        next_pos = events[j][0] if j < len(events) else 2*P
        if next_pos > x:
            cells.append((x, next_pos, state.bit_count()))
    return cells


def kinetic_breakpoints(arcs):
    saturation = [P-w for a, w in arcs]
    collisions = []
    for i, (a, w) in enumerate(arcs):
        for j, (b, v) in enumerate(arcs):
            t = (b-a-w) % P
            if 0 < t < min(saturation[i], saturation[j]):
                collisions.append((t, i, j))
    assert len(collisions) == len(set(t for t, _, _ in collisions)) == 3955
    assert len(set(saturation)) == 64
    assert not set(saturation).intersection(t for t, _, _ in collisions)
    return saturation, collisions


def codeword_sha256():
    digest = hashlib.sha256()
    for upper in product((1, 2), repeat=4):
        top = sum((v-1) << j for j, v in enumerate(upper))
        for lower in product((1, 2), repeat=12):
            word = determinant(lower, top) % P
            digest.update(word.to_bytes(8, "big"))
    return digest.hexdigest()


def main():
    arcs = arc_data()
    assert codeword_sha256() == FROZEN_SHA
    saturation, collisions = kinetic_breakpoints(arcs)
    times = [0] + sorted(set(saturation) | {t for t, _, _ in collisions})
    assert len(times) == 4020
    thresholds = {}
    complete_cell_checks = 0
    min_sequence = []
    for t in times:
        cells = open_cells(arcs, t)
        counts = []
        for left, right, count in cells:
            exact = direct_mask(arcs, left+right, t).bit_count()
            assert exact == count, (t, left, right, exact, count)
            counts.append(exact)
            complete_cell_checks += 1
        lo, hi = min(counts), max(counts)
        min_sequence.append(lo)
        for k in range(1, 65):
            if k not in thresholds and lo >= k:
                thresholds[k] = t
    assert complete_cell_checks == 510300
    assert min_sequence == sorted(min_sequence)
    assert len(thresholds) == len(set(thresholds.values())) == 64
    assert hashlib.sha256(" ".join(str(thresholds[k]) for k in range(1,65)).encode()).hexdigest() == THRESHOLD_SHA
    witness_checks = 0
    witnesses = []
    for k in range(1, 65):
        t = thresholds[k]
        before = open_cells(arcs, t-1)
        after = open_cells(arcs, t)
        deficient = min(before, key=lambda x: x[2])
        assert deficient[2] < k
        y4 = deficient[0]+deficient[1]
        assert direct_mask(arcs, y4, t-1).bit_count() == deficient[2]
        witness_checks += 1
        for left, right, count in after:
            assert count >= k
            assert direct_mask(arcs, left+right, t).bit_count() == count
            witness_checks += 1
        witnesses.append({"k":k, "t2rho":t, "min_before":deficient[2], "witness_y4":y4})
    assert witness_checks == 8062
    mean_numerator = sum(w for a,w in arcs)
    assert mean_numerator == 24072341088
    print(json.dumps({
        "schema":"R284CK_KFOLD_COVERAGE_V1",
        "frozen_sha256":FROZEN_SHA,
        "arc_sha256":hashlib.sha256(b"".join(
            a.to_bytes(5,"little")+w.to_bytes(5,"little") for a,w in arcs)).hexdigest(),
        "p":P,
        "active_crossings":len(collisions),
        "saturations":len(saturation),
        "breakpoints":len(times)-1,
        "direct_open_cell_checks":complete_cell_checks,
        "threshold_witness_checks":witness_checks,
        "min_max_at_zero":(min(x[2] for x in open_cells(arcs,0)),
                           max(x[2] for x in open_cells(arcs,0))),
        "uniform_mean_at_zero":[mean_numerator,P],
        "thresholds":witnesses,
        "proof_status":"AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED"
    }, indent=2))


if __name__ == "__main__":
    main()
