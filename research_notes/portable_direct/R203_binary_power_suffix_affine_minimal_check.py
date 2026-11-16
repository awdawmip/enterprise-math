"""R203: exhaustive 7-orbit configurations for T_{2,2} in Aff(F_2^3).
No third-party dependencies; source is a finite certificate adjunct to the proof.
"""
from itertools import permutations, combinations
import json

def affine_consistent(state, target):
    """Determine if an affine map on F_2^3 maps seven input points to seven prescribed outputs."""
    shift = target[0]
    basis = None
    for ids in combinations(range(1, 7), 3):
        b = [state[i] for i in ids]
        independent = {b[0], b[1], b[2], b[0]^b[1], b[0]^b[2],
                       b[1]^b[2], b[0]^b[1]^b[2]}
        if len(independent) == 7:
            basis = ids
            break
    assert basis is not None
    linear = {0: 0}
    for mask in range(1, 8):
        x, y = 0, 0
        for j, i in enumerate(basis):
            if (mask >> j) & 1:
                x ^= state[i]
                y ^= target[i] ^ shift
        linear[x] = y
    assert len(linear) == 8
    return all((shift ^ linear[x]) == y for x, y in zip(state, target))

def run():
    counts = {"configurations": 0, "append0_affine_consistent": 0,
              "append1_affine_consistent": 0, "both_affine_consistent": 0}
    for six in permutations(range(1, 8), 6):
        state = (0,) + six
        _, p0, p1, p00, p01, p10, p11 = state
        append0 = (p0, p00, p10, p00, p10, p00, p10)
        append1 = (p1, p01, p11, p01, p11, p01, p11)
        ok0 = affine_consistent(state, append0)
        ok1 = affine_consistent(state, append1)
        counts["configurations"] += 1
        counts["append0_affine_consistent"] += int(ok0)
        counts["append1_affine_consistent"] += int(ok1)
        counts["both_affine_consistent"] += int(ok0 and ok1)
    assert counts == {"configurations": 5040, "append0_affine_consistent": 0,
                      "append1_affine_consistent": 0, "both_affine_consistent": 0}
    return {"status": "PASS", "method": "EXHAUSTIVE_7_STATE_AFFINE_CONSISTENCY_GF2",
            "counts": counts, "theorem": "orbit_min_dimension_F2_a2_L2_eq_4",
            "source_pin": "43ec6098b1330ae86d0a7863be336c5d97f6ef34"}

if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
