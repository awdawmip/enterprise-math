#!/usr/bin/env python3
"""Exact finite certificate: 5-cycle source libraries, slack 2, Set_0(0/1).
Pure Python standard library; integer bitsets, exhaustive combinatorial checks.
Scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
from itertools import combinations
import json

K, S, J = 5, 2, 1
RAW = 1 << K
FULL = (1 << RAW) - 1
BELIEFS = [0x000000ff, 0x00003333, 0x00330033, 0x01040400,
           0x02080800, 0x54404000, 0xe8808000]
EXPECTED_TRANSITIONS = [(0, 0), (1, 1), (2, 2), (3, 4),
                        (3, 4), (5, 6), (5, 6)]
INVARIANT_CENTERS = [11, 15, 19, 21, 23, 27, 29, 31]


def bits(x, width):
    return [i for i in range(width) if x & (1 << i)]


def q(u):
    return sum(((u >> i) & 1) * ((u >> ((i + 1) % K)) & 1)
               for i in range(K))


def delta(r, u):
    missing = r & ~u
    e = r | (J & ~missing)
    return q(e) - q(e & ~missing)


def all_cover_masks():
    return [sum(1 << u for u in range(RAW)
                if (u & ~v) == 0 and q(v) - q(u) <= S)
            for v in range(RAW)]


def invariant_cover(v):
    mask = 0
    for t in range(RAW // 2):
        u = 2 * t
        if (u & ~v) == 0 and ((u | 1) & ~v) == 0 \
                and q(v) - q(u) <= S and q(v) - q(u | 1) <= S:
            mask |= 1 << t
    return mask


def main():
    assert len(set(BELIEFS)) == 7
    union = 0
    certificates = []
    for index, B in enumerate(BELIEFS):
        members = bits(B, RAW)
        assert members
        union |= B
        r = 0
        for u in members:
            r |= u
        assert all((u & ~r) == 0 for u in members)
        assert all(q(r) - q(u) <= S for u in members)
        assert all(delta(r, u) <= S for u in members)
        target_indices = []
        for b in (0, 1):
            image = 0
            for u in members:
                image |= 1 << ((u & ~1) | b)
            options = [j for j, C in enumerate(BELIEFS) if (C & image) == image]
            assert options
            target_indices.append(options[0])
        assert tuple(target_indices) == EXPECTED_TRANSITIONS[index]
        certificates.append({"state": index, "belief_hex": f"{B:08x}",
                             "source_center": r, "source_cost": 5 * K + q(r),
                             "raw_masks": members, "max_slack": max(q(r) - q(u) for u in members),
                             "set_0_to_0_state": target_indices[0],
                             "set_0_to_1_state": target_indices[1]})
    assert union == FULL

    # Static lower bound: every library used for a raw family can be replaced
    # by a canonical L(v). Every 6-tuple among 32 possible v must fail to cover.
    covers = all_cover_masks()
    static_checked = 0
    for centers in combinations(range(RAW), 6):
        static_checked += 1
        cover = 0
        for v in centers:
            cover |= covers[v]
        assert cover != FULL, centers
    assert static_checked == 906192

    # For a controller with both Set commands as self-loops, every represented
    # raw state belongs to a pair {2t,2t+1}; only odd OR centers are possible.
    candidates = [(v, invariant_cover(v)) for v in range(1, RAW, 2)]
    inv_full = (1 << (RAW // 2)) - 1
    invariant_checked = 0
    for chosen in combinations(candidates, 7):
        invariant_checked += 1
        cover = 0
        for _, mask in chosen:
            cover |= mask
        assert cover != inv_full
    assert invariant_checked == 11440
    witness_cover = 0
    for v in INVARIANT_CENTERS:
        witness_cover |= invariant_cover(v)
    assert witness_cover == inv_full

    evidence = {
        "status": "PASS_R5_K5_SINGLE_CONTROL_EXACT_7_VS_INVARIANT_8",
        "frozen_science_pin": "435e77af0d180eac32bd1f9c4c464bc4010b7551",
        "model": {"k": K, "slack": S, "commands": ["Set_0(0)", "Set_0(1)"],
                  "observer": "q(u)=sum cyclic u_i*u_(i+1)",
                  "genuine_source_library": "L(v), size 5k+q(v)"},
        "exact": {"static_minimum": 7, "dynamic_minimum": 7,
                  "self_loop_controller_minimum": 8,
                  "static_six_tuples_exhausted": static_checked,
                  "self_loop_seven_tuples_exhausted": invariant_checked},
        "states": certificates,
        "self_loop_eight_source_centers": INVARIANT_CENTERS,
        "proof_status": "FINITE_EXHAUSTIVE_CERTIFICATE_AND_EXPLICIT_CONSTRUCTION",
        "independent_review": "NOT_REVIEWED"
    }
    print(json.dumps(evidence, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
