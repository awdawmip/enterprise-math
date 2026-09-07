"""Independent, bounded audit of the weighted eight-positive classification.

No author checker, project observer, BRC implementation, or optimizer is imported.
Signed coefficients here are algebraic proof data, not physical branch weights.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path


AXES3 = tuple(combinations(range(6), 3))
BITS3 = tuple(product((0, 1), repeat=3))
HERE = Path(__file__).resolve().parent


def source_hashes():
    names = (
        "OWNER_WEIGHTED_TRADE_FRONTIER_20260907.md",
        "owner_weighted_trade_20260907_check.py",
        Path(__file__).name,
    )
    return {name: sha256((HERE / name).read_bytes()).hexdigest() for name in names}


def raw_tables(terms):
    """Direct literal fiber sums on all twenty raw triples, retaining zeros."""
    terms = tuple(terms)
    assert all(len(point) == 6 and all(type(v) is int for v in point)
               and type(weight) in (int, Fraction) for point, weight in terms)
    result = {}
    for axes in AXES3:
        table = Counter()
        for point, weight in terms:
            table[tuple(point[j] for j in axes)] += weight
        result[axes] = dict(table)
    return result


def raw_zero(terms):
    return all(value == 0 for table in raw_tables(terms).values()
               for value in table.values())


def rank_over_q(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    if not rows:
        return 0
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [entry / scale for entry in rows[rank]]
        for i in range(rank + 1, len(rows)):
            scale = rows[i][column]
            if scale:
                rows[i] = [a - scale * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def raw_incidence_rank(support):
    rows = []
    for axes in AXES3:
        addresses = [tuple(point[j] for j in axes) for point in support]
        for address in sorted(set(addresses)):
            rows.append([int(item == address) for item in addresses])
    return rank_over_q(rows)


def pair_balanced(a, b):
    return Counter(zip(a, b)) == Counter({pair: 2 for pair in product((0, 1), repeat=2)})


def audit_column_families():
    # Any two different representative columns can be put in this row order:
    # each pair occurs twice; row order and independent bit complements are free.
    first, second = tuple(row[0] for row in BITS3), tuple(row[1] for row in BITS3)
    candidates = tuple(column for column in product((0, 1), repeat=8)
                       if column[0] == 0 and sum(column) == 4
                       and pair_balanced(first, column)
                       and pair_balanced(second, column))
    assert len(candidates) == 9
    counts = Counter()
    cases = []
    for extra_count in range(5):  # two fixed + at most four = six physical axes
        for extras in combinations(candidates, extra_count):
            columns = (first, second) + extras
            if not all(pair_balanced(a, b) for a, b in combinations(columns, 2)):
                continue
            r = len(columns)
            short_rows = tuple(zip(*columns))
            if len(set(short_rows)) != 8:
                counts[f"r{r}:fewer_than_8_points"] += 1
                continue
            bases = tuple(axes for axes in combinations(range(r), 3)
                          if len({tuple(row[j] for j in axes) for row in short_rows}) == 8)
            assert bases  # independent exhaustive check of the all-once lemma
            basis = bases[0]
            labels = tuple(tuple(row[j] for j in basis) for row in short_rows)
            normals = []
            for column in columns:
                solutions = [normal for normal in BITS3 if any(normal)
                             and all(sum(a * b for a, b in zip(normal, label)) % 2 == value
                                     for label, value in zip(labels, column))]
                assert len(solutions) == 1
                normals.append(solutions[0])
            positives = tuple(tuple(row) + (0,) * (6 - r) for row in short_rows)
            positive_tables = raw_tables((point, 1) for point in positives)
            join = tuple(short + (0,) * (6 - r)
                         for short in product((0, 1), repeat=r)
                         if all(tuple((short + (0,) * (6 - r))[j] for j in axes) in table
                                for axes, table in positive_tables.items()))
            negatives = tuple(point for point in join if point not in positives)
            assert len(negatives) in (0, 8)
            if negatives:
                # Verify every original raw fiber, with no character/transform test.
                assert r == 4
                terms = tuple((point, 1) for point in positives) + tuple((point, -1) for point in negatives)
                assert raw_zero(terms)
                # A one-dimensional exact raw kernel rules out unequal amplitudes.
                assert raw_incidence_rank(positives + negatives) == 15
            counts[f"r{r}:distinct_8_points"] += 1
            counts[f"r{r}:negative_gate_{len(negatives)}"] += 1
            cases.append({"representative_axes": r, "all_once_triples": len(bases),
                          "normal_vectors": normals, "negative_gate": len(negatives)})
    return {"normalized_extra_columns": len(candidates),
            "counts": dict(sorted(counts.items())), "cases": cases}


def audit_physical_embeddings():
    cube4 = tuple(product((0, 1), repeat=4))
    count = 0
    for types in product(range(5), repeat=6):  # 4 is constant; 0..3 are bit types
        if not set(range(4)).issubset(types):
            continue
        terms = tuple((tuple(0 if kind == 4 else bits[kind] for kind in types),
                       (-1) ** sum(bits)) for bits in cube4)
        assert len({point for point, weight in terms}) == 16
        assert raw_zero(terms)
        count += 1
    assert count == 3360
    # Independent signed, nonadjacent level maps including duplicate/complement.
    def embed(bits):
        a, b, c, d = bits
        return (-9 + 5 * a, 7 - 11 * b, -3 + 17 * c,
                14 - 23 * d, 41 - 29 * a, -31)
    lam = Fraction(5, 13)
    terms = tuple((embed(bits), lam * (-1) ** sum(bits)) for bits in cube4)
    assert raw_zero(terms)
    assert raw_incidence_rank(tuple(point for point, _ in terms)) == 15
    # Unequal positive amplitude is detected by the unmodified raw observer.
    malformed = ((terms[0][0], terms[0][1] + Fraction(1, 13)),) + terms[1:]
    defects = raw_tables(malformed)
    assert sum(bool(value) for table in defects.values() for value in table.values()) == 20
    deleted = terms[1:]
    defect = sum(abs(value) for table in raw_tables(deleted).values() for value in table.values())
    assert defect == 20 * lam
    assert sum(abs(weight) for point, weight in deleted) / defect == Fraction(3, 4)
    return {"all_six_axis_type_assignments": count, "signed_level_embedding_raw_kernel_rank": 15,
            "single_amplitude_tamper_nonzero_raw_fibers": 20,
            "deleted_positive_raw_defect": str(defect), "deleted_ratio": "3/4"}


def audit_small_lemmas():
    pair_tables = tuple(a for a in range(5)
                        if all(value == 0 or value >= 2 for value in (a, 4 - a)))
    assert pair_tables == (0, 2, 4)
    counts = Counter()
    for chosen in combinations(range(8), 4):
        points = tuple(BITS3[i] for i in chosen)
        if not all(sum(point[j] for point in points) == 2 for j in range(3)):
            continue
        origin = points[0]
        differences = {tuple(a ^ b for a, b in zip(origin, point)) for point in points}
        assert len(differences) == 4
        assert all(tuple(a ^ b for a, b in zip(x, y)) in differences
                   for x, y in product(differences, repeat=2))
        # Closure checks the affine-plane assertion without the author's equation scan.
        counts["balanced_four_subsets"] += 1
    assert counts["balanced_four_subsets"] == 8
    return {"allowed_pair_count_parameter_a": pair_tables, **counts}


def run():
    initial_hashes = source_hashes()
    result = {"status": "PASS", "scope": "bounded independent combinatorial and exact raw-marginal audit",
              "source_hashes_sha256": initial_hashes,
              "small_lemmas": audit_small_lemmas(),
              "column_families": audit_column_families(),
              "physical_embeddings": audit_physical_embeddings(),
              "mathematical_proof": "See OWNER_WEIGHTED_TRADE_INDEPENDENT_AUDIT_20260907.md; enumeration is not a substitute.",
              "global_knowledge_sync": "main@4fa7d7d / GLOBAL_KNOWLEDGE_V1"}
    assert source_hashes() == initial_hashes, "audited source changed during run"
    return result


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
