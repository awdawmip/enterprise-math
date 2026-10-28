"""Exact, labelled-source ordered-pair BRC certificate for PREFIX-310.

Input: second columns of 12 representatives from PREFIX-299, Git blob
b6acffe158f014469235f5428d2889ff43b62810.  No randomness or floating point.
Run: python verify_prefix310.py
"""
import json

COLS = {
    "S4": [
        [(0, 0), (4, 0), (0, -4)], [(0, 0), (4, 0), (0, 4)],
        [(0, 0), (4, 0), (0, -4)], [(0, 0), (4, 0), (0, 4)],
        [(0, 0), (0, 0), (4, 4)], [(0, 0), (0, 0), (4, 4)],
    ],
    "S7": [
        [(4, 0), (0, 0), (-4, 0)], [(4, 0), (-4, 0), (0, 0)],
        [(0, 0), (4, 4), (0, 0)], [(0, 0), (4, 4), (0, 0)],
        [(0, 4), (0, -4), (0, 0)], [(0, 4), (0, -4), (0, 0)],
    ],
}
PHASES = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def mul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]

def conj(x):
    return x[0], -x[1]

def run():
    c = dict(configurations=0, axis_configurations=0,
             diagonal_configurations=0, diagonal_port_omission_configurations=0,
             base_pairs_equal=0, reference_intervals_overlap=0,
             direct_brc_mass_evaluations=0, ordered_labelled_source_path_pairs=0,
             max_reference_mass_numerator_difference=0)
    def brc(paths):
        pairs = [mul(x, conj(y)) for x in paths for y in paths]
        c["direct_brc_mass_evaluations"] += 1
        c["ordered_labelled_source_path_pairs"] += len(pairs)
        re, im = sum(z[0] for z in pairs), sum(z[1] for z in pairs)
        assert im == 0 and re >= 0
        return re
    def measured(col, p, sign, reference=None):
        z = mul(col, (sign * p[0], sign * p[1]))
        paths = [(0, 0), z, (0, 0)]  # three source labels, including zero paths
        if reference is not None:
            paths.append(reference)  # independent reference source label
        return brc(paths)
    def check(cols, p, selected):
        for col in cols:
            assert measured(col, p, 1) == measured(col, p, -1)
            c["base_pairs_equal"] += 1
        for j in selected:
            for reference in [(8, 0), (0, 8)]:
                plus = measured(cols[j], p, 1, reference)
                minus = measured(cols[j], p, -1, reference)
                d = abs(plus - minus)
                expected = 32 * abs(mul(cols[j], p)[0 if reference[0] else 1])
                assert d == expected and d <= 128
                c["reference_intervals_overlap"] += 1
                c["max_reference_mass_numerator_difference"] = max(
                    c["max_reference_mass_numerator_difference"], d)
    classification = []
    for family, orbits in COLS.items():
        for orbit, col in enumerate(orbits, 1):
            diagonal = [j for j, z in enumerate(col) if abs(z[0]) == abs(z[1]) == 4]
            assert len(diagonal) <= 1
            if diagonal:
                assert all(z == (0, 0) for j, z in enumerate(col) if j != diagonal[0])
            else:
                assert all(z in {(0,0),(4,0),(-4,0),(0,4),(0,-4)} for z in col)
            classification.append([family, orbit, "DIAGONAL" if diagonal else "AXIS"])
            for q in PHASES:
                cols = [mul((4, 0), q), (-4, 0)] + [mul(z, q) for z in col]
                c["configurations"] += 1
                c["diagonal_configurations" if diagonal else "axis_configurations"] += 1
                check(cols, (1, 0) if diagonal else (1, 1), range(5))
                if diagonal:
                    # Leave the diagonal Port's free Q0, remove only its Q1/Qi.
                    omit = 2 + diagonal[0]
                    check(cols, (1, 1), [j for j in range(5) if j != omit])
                    c["diagonal_port_omission_configurations"] += 1
    assert c == dict(configurations=48, axis_configurations=32,
                     diagonal_configurations=16, diagonal_port_omission_configurations=16,
                     base_pairs_equal=320, reference_intervals_overlap=608,
                     direct_brc_mass_evaluations=1856,
                     ordered_labelled_source_path_pairs=25216,
                     max_reference_mass_numerator_difference=128), c
    return {"status": "PASS", "counts": c, "classification": classification}

if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
