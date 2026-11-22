#!/usr/bin/env python3
"""Unit263 exact two-triad BRC + conditional SHELL/CLOSURE local-C12 check.
Python stdlib only. No native physical transition claim.
"""
import itertools
import json

CASES = [
    ("6,0", "LKJIHGMALKJIHGMdefghijklabAc", "LA", 6, 0),
    ("8,2", "LKJdefghimIHGFEDCBAcdefghimc", "dc", 8, 2),
]
ORIGINAL_FRAME = ((0, 1, 2), (1, -1, 1))


def rcan(frame):
    axes, signs = frame
    return (axes[1:] + axes[:1], tuple(-s for s in signs))


def local_move(frame, mode):
    # 0=SHELL, 1=CLOSURE
    return (frame, 1) if mode == 0 else (rcan(frame), 0)


def all_fiber_cycles():
    frames = [(a, s) for a in itertools.permutations(range(6), 3)
              for s in itertools.product((1, -1), repeat=3)]
    assert len(frames) == 960
    checks = 0
    for frame in frames:
        for m in (0, 1):
            state = (frame, m)
            for n in range(1, 13):
                state = local_move(*state)
                checks += 1
                assert (state == (frame, m)) == (n == 12), (frame, m, n)
    assert checks == 23040
    return checks


def replay(route, ingress, egress):
    pos = [0, 2]
    wind = [0, 0]
    counts = [0, 0]
    frames = [ORIGINAL_FRAME, ORIGINAL_FRAME]
    modes = [0, 0]
    for ch in route:
        t = 0 if ch.isupper() else 1
        dst = ord(ch) - ord("A" if t == 0 else "a")
        src = pos[t]
        assert dst != pos[1-t], (ch, src, dst, "occupied")
        if src == 12:
            assert dst == egress, (ch, src, dst, "wrong egress")
        elif dst == 12:
            assert src == ingress, (ch, src, dst, "wrong ingress")
        elif (dst-src) % 12 == 1:
            wind[t] += 1
        elif (src-dst) % 12 == 1:
            wind[t] -= 1
        else:
            raise AssertionError((ch, src, dst, "non-edge"))
        pos[t] = dst
        counts[t] += 1
        frames[t], modes[t] = local_move(frames[t], modes[t])
    assert pos == [0, 2] and wind == [-12, 12], (pos, wind)
    full_return = all(frames[k] == ORIGINAL_FRAME and modes[k] == 0
                      for k in (0, 1))
    return {
        "events": len(route),
        "counts": counts,
        "windings": wind,
        "local_mod12": [n % 12 for n in counts],
        "full_local_C12_return": full_return,
        "global_C12_return": len(route) % 12 == 0
    }


def main():
    checks = all_fiber_cycles()
    table = {}
    for name, witness, bounce, ingress, egress in CASES:
        table[name] = {}
        for loops in (0, 1, 4):
            route = bounce * loops + witness
            table[name][str(loops)] = replay(route, ingress, egress)
            assert (len(route), table[name][str(loops)]["full_local_C12_return"]) == (
                (28, False) if loops == 0 else (30, False) if loops == 1 else (36, True)
            )
    output = {
        "schema": "X6_TIME_UNIT263_LOCAL_C12_VS_C6_RETURN_CERT_V1",
        "all_frame_mode_step_assertions": checks,
        "full_local_fiber_states": 1920,
        "period_of_each": 12,
        "C12_orbits": 160,
        "cases": table,
        "source_execution": False,
        "status": "CONDITIONAL_EXACT_FINITE_EXECUTED_NOT_ADMITTED"
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
