"""R174 exact signed-rational port-family moment algebra and four independent witnesses.
Typed mathematical candidate; no native BRC amplitude execution or physics.
"""
from fractions import Fraction
import json


DIM = 6
ZERO = (Fraction(0),) * DIM
E = (0, 1)
M = (0, -1)


def path_sig(word):
    displacement = [0] * DIM
    integral = [0] * DIM
    for axis, sign in word:
        displacement[axis] += sign
        for j in range(DIM):
            integral[j] += displacement[j]
    return len(word), tuple(displacement), tuple(integral)


def sig(family):
    out = {}
    for i, j, coeff, path in family:
        record = out.setdefault((i, j), [Fraction(0), Fraction(0),
                                          [Fraction(0)] * DIM, [Fraction(0)] * DIM])
        n, d, c = path_sig(path)
        record[0] += coeff
        record[1] += coeff * n
        record[2] = [x + coeff * y for x, y in zip(record[2], d)]
        record[3] = [x + coeff * y for x, y in zip(record[3], c)]
    return {k: (a, l, tuple(b), tuple(c)) for k, (a, l, b, c) in out.items()}


def serial(left, right):
    return [(i, k, w * z, p + q)
            for i, j, w, p in left
            for jj, k, z, q in right if j == jj]


def summary_serial(left, right):
    a, b = sig(left), sig(right)
    out = {}
    for (i, j), (aa, ll, dd, cc) in a.items():
        for (jj, k), (bb, mm, ee, ff) in b.items():
            if j != jj:
                continue
            rec = out.setdefault((i, k), [Fraction(0), Fraction(0),
                                            [Fraction(0)] * DIM, [Fraction(0)] * DIM])
            rec[0] += aa * bb
            rec[1] += ll * bb + aa * mm
            rec[2] = [x + di * bb + aa * ei for x, di, ei in zip(rec[2], dd, ee)]
            rec[3] = [x + ci * bb + aa * fi + di * mm
                      for x, ci, fi, di in zip(rec[3], cc, ff, dd)]
    return {k: (a, l, tuple(d), tuple(c)) for k, (a, l, d, c) in out.items()}


def branch(c, path):
    return (0, 0, Fraction(c), tuple(path))


def main():
    witnesses = {
        "A": [branch(1, ())],
        "L": [branch(1, (E, M)), branch(1, (M, E)), branch(-2, ())],
        "B": [branch(1, (E, E)), branch(-2, (E, M)), branch(1, (M, E))],
        "C": [branch(1, (E, M)), branch(-1, (M, E))]
    }
    expected = {"A": (1, 0, 0, 0), "L": (0, 4, 0, 0),
                "B": (0, 0, 2, 0), "C": (0, 0, 0, 2)}
    identity = [branch(1, ())]
    probe_contexts = {
        "A": ([branch(1, (E, M))], identity),
        "L": ([branch(1, (E,))], identity),
        "B": (identity, [branch(1, (E,))]),
        "C": (identity, identity)
    }
    witness_observations = {}
    for name, family in witnesses.items():
        a, l, d, c = sig(family)[(0, 0)]
        assert (a, l, d[0], c[0]) == expected[name]
        assert d[1:] == ZERO[1:] and c[1:] == ZERO[1:]
        x, y = probe_contexts[name]
        observation = sig(serial(serial(x, family), y))[(0, 0)][3]
        assert observation[0] == expected[name][{"A": 0, "L": 1, "B": 2, "C": 3}[name]]
        assert observation[1:] == ZERO[1:]
        witness_observations[name] = str(observation[0])

    alphabet = [(i, z) for i in (0, 1, 5) for z in (-1, 1)]
    families = []
    for t in range(32):
        group = []
        for z in range(4):
            source, destination = (t + z) % 2, (t + z // 2) % 2
            coeff = Fraction(((-1) ** (t + z)) * (z + 1), z % 3 + 1)
            path = tuple(alphabet[(2 * t + 3 * z + k) % len(alphabet)]
                         for k in range((t + z) % 4))
            group.append((source, destination, coeff, path))
        families.append(group)

    count = 0
    blank = (Fraction(0), Fraction(0), ZERO, ZERO)
    for f in families:
        for g in families:
            raw = sig(serial(f, g))
            summary = summary_serial(f, g)
            for port in set(raw) | set(summary):
                assert raw.get(port, blank) == summary.get(port, blank), port
            count += 1

    result = {
        "marker": "R174_SIGNED_PORT_MOMENT_CONTEXT_EXACT_PASS",
        "all_exact_fraction": True,
        "native_spatial_axes": DIM,
        "ports": 2,
        "families": len(families),
        "raw_vs_summary_serial_pairs": count,
        "separating_witnesses": witness_observations,
        "witness_signature_coordinates": {
            k: list(v) for k, v in expected.items()
        },
        "source_scope": "proposed signed-rational BRC-style port/path extension",
        "native_brc_kernel_executed": False,
        "mathematics": "AUTHOR_PROVED; INDEPENDENT_REVIEW_NOT_RUN"
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
