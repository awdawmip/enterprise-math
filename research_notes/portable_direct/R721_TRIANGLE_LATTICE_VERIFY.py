"""R721 exact finite certificate: triangle-source pair ledger vs positive BRC source.

Model: six labeled native axis candidates, 20 triple-source bits, 15 pair counts.
Arithmetic: exact finite integer incidence, not native physical propagation.
Run: python R721_TRIANGLE_LATTICE_VERIFY.py (Python 3 standard library).
"""
from collections import Counter
from itertools import combinations, permutations
import json
from pathlib import Path

V = tuple(range(6))
EDGES = tuple(combinations(V, 2))
TRIPLES = tuple(combinations(V, 3))
EDGE_POS = {p: k for k, p in enumerate(EDGES)}
TRIPLE_MASKS = tuple(sum(1 << EDGE_POS[e] for e in combinations(t, 2)) for t in TRIPLES)
assert len(EDGES) == 15 and len(TRIPLES) == 20


def residue_ok(mask):
    deg = [0] * 6
    for k, (a, b) in enumerate(EDGES):
        if mask & (1 << k):
            deg[a] += 1
            deg[b] += 1
    return all(d % 2 == 0 for d in deg) and mask.bit_count() % 3 == 0


def positive_triangle_packings():
    """Exhaust 2**20 Boolean source states; keep exactly edge-disjoint triples."""
    packings = Counter()
    for state in range(1 << len(TRIPLES)):
        ledger = 0
        for k, bit in enumerate(TRIPLE_MASKS):
            if state & (1 << k):
                if ledger & bit:
                    break
                ledger |= bit
        else:
            packings[ledger] += 1
    return packings


def six_cycles():
    """Enumerate the 60 undirected Hamiltonian cycles in K6."""
    cycles = set()
    for p in permutations((1, 2, 3, 4, 5)):
        if p[0] > p[-1]:
            continue
        path = (0,) + p + (0,)
        mask = 0
        for a, b in zip(path, path[1:]):
            mask |= 1 << EDGE_POS[tuple(sorted((a, b)))]
        cycles.add(mask)
    assert len(cycles) == 60
    return cycles


def signed_witness():
    """The six-cycle equals 015 + 123 + 345 - 135 as pair ledgers."""
    witness = {(0, 1, 5): 1, (1, 2, 3): 1, (3, 4, 5): 1, (1, 3, 5): -1}
    ledger = [sum(coeff * (set(e) <= set(t)) for t, coeff in witness.items()) for e in EDGES]
    cycle = {(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)}
    assert ledger == [int(e in cycle) for e in EDGES]
    assert residue_ok(sum(1 << EDGE_POS[e] for e in cycle))
    return witness, cycle


def main():
    valid = {m for m in range(1 << len(EDGES)) if residue_ok(m)}
    packings = positive_triangle_packings()
    assert set(packings) <= valid
    cycles = six_cycles()
    assert valid - set(packings) == cycles
    witness, cycle = signed_witness()

    for perm in permutations(range(6)):
        relabeled = {tuple(sorted(perm[i] for i in t)): c for t, c in witness.items()}
        target = {tuple(sorted((perm[a], perm[b]))) for a, b in cycle}
        for e in EDGES:
            assert sum(c * (set(e) <= set(t)) for t, c in relabeled.items()) == int(e in target)

    result = {
        "schema": "R721_BRC_TRIANGLE_LATTICE_V1",
        "pair_edge_patterns_tested": 2**15,
        "Boolean_source_states_tested": 2**20,
        "integer_lattice_compatible_simple_ledgers": len(valid),
        "integer_lattice_compatible_by_edges": {
            str(k): v for k, v in sorted(Counter(m.bit_count() for m in valid).items())
        },
        "nonnegative_triangle_representable_simple_ledgers": len(packings),
        "positive_ledger_by_edges": {
            str(k): v for k, v in sorted(Counter(m.bit_count() for m in packings).items())
        },
        "nonnegative_representation_multiplicity": {
            str(k): v for k, v in sorted(Counter(packings.values()).items())
        },
        "false_positives_for_positive_cone": len(valid - set(packings)),
        "false_positive_exact_family": "ALL_60_UNDIRECTED_HAMILTONIAN_CYCLES_K6",
        "S6_signed_witness_permutations_checked": 720,
        "lattice_index_n6": 96,
        "lattice_quotient_n6": "Z/6 x (Z/2)^4",
        "logical_scope": "full integer lattice iff parity+total-mod3 for all n>=5; positive/Boolean necessity only",
        "status": "EXACT_PASS",
    }
    expected = json.loads(Path(__file__).with_name("R721_TRIANGLE_LATTICE_EVIDENCE.json").read_text())
    assert result == expected, (result, expected)
    print("R721_BRC_TRIANGLE_LATTICE_EXACT_PASS")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
