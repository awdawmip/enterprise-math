"""Exact centered cross-moment families and two finite cover obstructions."""
import argparse
import importlib.util
import json
from itertools import permutations, product
from pathlib import Path

P = list(product(range(5), repeat=3))
PAIRS = ((0, 1), (0, 2), (1, 2))
TYPES = {(9, 557): 24000, (10, 744): 12000,
         (10, 768): 1500, (11, 944): 12000}
D = {tuple(v if i == j else 0 for i in range(3))
     for j in range(3) for v in (1, 4)}
F = {q for q in product(range(5), repeat=3)
     if sorted(min(a, 5-a) for a in q) == [0, 2, 2]}
E = F | {q for q in product(range(5), repeat=3)
         if sorted(min(a, 5-a) for a in q) == [0, 1, 2]}


def points(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask ^= bit


def moment(mask):
    coordinates = [P[i] for i in points(mask)]
    mu = tuple(sum(x[j] for x in coordinates) % 5 for j in range(3))
    q = tuple(sum(x[i]*x[j] for x in coordinates) % 5 for i, j in PAIRS)
    n = len(coordinates) % 5
    if n:
        q = tuple((a-pow(n, -1, 5)*mu[i]*mu[j]) % 5
                  for a, (i, j) in zip(q, PAIRS))
    return mu, q


def orbit(representative):
    oriented = {tuple(sorted(25*(P[x][perm[0]]*sign[0]*scale % 5)
                             + 5*(P[x][perm[1]]*sign[1]*scale % 5)
                             + P[x][perm[2]]*sign[2]*scale % 5
                             for x in representative))
                for perm in permutations(range(3))
                for sign in product((1, -1), repeat=3) for scale in (1, 2)}
    return {sum(1 << (25*((P[x][0]+a) % 5)+5*((P[x][1]+b) % 5)
                      +(P[x][2]+c) % 5) for x in row)
            for row in oriented for a, b, c in P}


def sumset(a, b):
    return {tuple((x+y) % 5 for x, y in zip(u, v)) for u in a for v in b}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('native_finite_menu',
                         args.previous/'fractional/proof/verify.py')
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    bad, pairs = native.observation_tables()
    source = json.loads((args.previous/'new_lower/class_representatives.json').read_text())
    families = {}
    checks = []
    for entry in source['families']:
        kind = entry['size'], entry['cost']
        if kind not in TYPES:
            continue
        family = set()
        for rep in entry['representatives']:
            assert native.native_class(sum(1 << p for p in rep), bad, pairs) == kind
            current = orbit(rep)
            assert not family & current
            family |= current
        assert len(family) == entry['count'] == TYPES[kind]
        target = E if kind[0] == 9 else F if kind[0] == 11 else D
        observed = set()
        for mask in family:
            mu, q = moment(mask)
            if kind[0] == 10:
                assert mu == (0, 0, 0)
            assert q in target
            observed.add(q)
        assert observed == target
        families[kind] = family
        checks.append({'type': list(kind), 'classes': len(family),
                       'representatives_native_checked': len(entry['representatives']),
                       'centered_cross_moment_values': len(target)})
    assert set(families) == set(TYPES)
    sums = {}
    for label, initial, expected in [('nine', E, [36, 102, 124, 125, 125]),
                                      ('eleven_944', F, [12, 60, 110, 124, 125])]:
        values = initial
        rows = []
        for k, count in enumerate(expected):
            assert len(values) == count
            rows.append({'ten_classes': k, 'reachable': count,
                         'zero_reachable': (0, 0, 0) in values})
            values = sumset(values, D)
        sums[label] = rows
    examples = json.loads(Path(__file__).with_name('counterexamples.json').read_text())
    examples_checked = []
    for name, exceptional, repetitions in [('twenty_nine', (9, 557), 2),
                                            ('forty_one', (11, 944), 3)]:
        example = examples[name]
        ids = example['points']
        assert len(ids) == len(set(ids)) == exceptional[0]+10*repetitions
        mask = sum(1 << p for p in ids)
        mu, q = moment(mask)
        assert q == (0, 0, 0)
        target = E if exceptional[0] == 9 else F
        for _ in range(repetitions):
            target = sumset(target, D)
        assert q not in target
        candidates = {t: sorted(m for m in rows if not m & ~mask)
                      for t, rows in families.items() if t[0] == 10 or t == exceptional}
        ten = set(candidates[(10, 744)]) | set(candidates[(10, 768)])
        # An independent finite-cover check of these small examples.
        nodes = 0
        def pack_tens(free, count):
            nonlocal nodes
            nodes += 1
            if count == 1:
                return free in ten
            p = next(points(free))
            return any(pack_tens(free ^ m, count-1) for m in ten
                       if m >> p & 1 and not m & ~free)
        assert not any(pack_tens(mask ^ m, repetitions) for m in candidates[exceptional])
        marginals = [[sum(P[p][j] == v for p in ids) for v in range(5)] for j in range(3)]
        if name == 'twenty_nine':
            assert all(sorted(row) == [5, 6, 6, 6, 6] for row in marginals)
        partial = example['explicit_partial_partition']
        partial_masks = [sum(1 << p for p in part) for part in partial]
        assert len(partial_masks) == repetitions
        assert partial_masks[0] in families[exceptional]
        assert all(m in families[(10, 744)] for m in partial_masks[1:])
        occupied = 0
        for m in partial_masks:
            assert not m & ~mask and not m & occupied
            occupied |= m
        remaining = mask ^ occupied
        assert remaining.bit_count() == 10
        assert sorted(points(remaining)) == example['unfilled_ten_points']
        assert all(sum(P[p][j] == v for p in points(remaining)) == 2
                   for j in range(3) for v in range(5))
        examples_checked.append({'example': name, 'points': len(ids), 'mu': mu,
                                 'centered_cross_moment': q, 'marginals': marginals,
                                 'candidate_counts': {str(t): len(v) for t, v in candidates.items()},
                                 'direct_cover_nodes': nodes, 'direct_cover_found': False})
    result = {'families': checks, 'native_representatives_checked': sum(x['representatives_native_checked'] for x in checks),
              'moment_classes_checked': sum(x['classes'] for x in checks),
              'sumset_tables': sums, 'examples': examples_checked,
              'scope': 'Exact finite observer identities and tail obstructions; no new global twelve-label lower bound.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
