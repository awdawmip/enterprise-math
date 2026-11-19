"""Audit a local ternary comparison law on all three-port directed graphs."""
import argparse
from collections import Counter, deque
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import permutations, product
import json
from math import prod
from pathlib import Path
import runpy


LABELS = range(3)
ARCS = tuple(permutations(LABELS, 2))
IDENTITY = (1, 0, 0, 0, 1, 0, 0, 0, 1)
RECORD = (1, 0, 0, 0, 1, 0, 1, 2, 1)
TRIPLES = tuple(product(LABELS, repeat=3))


def reflection(source, receiver):
    if source == receiver:
        return receiver
    return next(value for value in LABELS if value not in (source, receiver))


def binary_gates():
    perms = tuple(permutations(LABELS))
    eligible = []
    for rows in product(perms, repeat=3):
        if all(rows[phi[x]][phi[y]] == phi[rows[x][y]] for phi in perms for x, y in product(LABELS, repeat=2)):
            eligible.append(rows)
    assert len(eligible) == 2
    assert tuple(tuple(reflection(i, j) for j in LABELS) for i in LABELS) in eligible
    return {'source_preserving_bijections_tested': len(perms) ** 3, 'equivariant_tables': eligible}


def step(matrix, source, target):
    result = list(matrix)
    result[3 * target:3 * target + 3] = [
        (2 * matrix[3 * source + j] - matrix[3 * target + j]) % 3 for j in LABELS
    ]
    return tuple(result)


def reachability(edges):
    reach = [[i == j or (i, j) in edges for j in LABELS] for i in LABELS]
    for k in LABELS:
        for i, j in product(LABELS, repeat=2):
            reach[i][j] |= reach[i][k] and reach[k][j]
    return reach


def predicted_order(reach):
    blocks = {tuple(j for j in LABELS if reach[i][j] and reach[j][i]) for i in LABELS}
    order = 1
    for block in blocks:
        n = len(block)
        upstream = sum(i not in block and reach[i][block[0]] for i in LABELS)
        gl = prod(3 ** n - 3 ** j for j in range(n))
        order *= gl * 3 ** (n * (upstream - 1)) if upstream else gl // (3 ** n - 1)
    return order


def distances(edges):
    distance = {IDENTITY: 0}
    todo = deque([IDENTITY])
    while todo:
        matrix = todo.popleft()
        for i, j in edges:
            other = step(matrix, i, j)
            if other not in distance:
                distance[other] = distance[matrix] + 1
                todo.append(other)
    return distance


def determinant(m):
    a, b, c, d, e, f, g, h, i = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def all_graphs():
    records = []
    for mask in range(64):
        edges = tuple(edge for bit, edge in enumerate(ARCS) if mask & (1 << bit))
        reach = reachability(edges)
        dist = distances(edges)
        assert len(dist) == predicted_order(reach)
        assert (RECORD in dist) == (reach[0][2] and reach[1][2])
        for m in dist:
            assert all(sum(m[3*i:3*i+3]) % 3 == 1 for i in LABELS)
            assert all(reach[j][i] or m[3*i+j] == 0 for i, j in product(LABELS, repeat=2))
        records.append({'mask': mask, 'group_order': len(dist), 'record_distance': dist.get(RECORD)})
    full = {m for m in product(LABELS, repeat=9)
            if determinant(m) % 3 and all(sum(m[3*i:3*i+3]) % 3 == 1 for i in LABELS)}
    assert set(dist) == full and len(full) == 432
    levels = Counter(dist.values())
    assert [levels[i] for i in range(7)] == [1, 6, 27, 84, 151, 126, 37]
    outcomes = Counter(r['record_distance'] for r in records)
    assert outcomes == {None: 32, 2: 16, 4: 16}
    return {'arc_mask_order': ARCS, 'graphs': records, 'full_group_depth_counts': dict(levels),
            'record_distances': {'unreachable': outcomes[None], 'two': outcomes[2], 'four': outcomes[4]}}


def prepared_endpoints():
    group = distances(ARCS)
    def evaluate(m, x):
        return tuple(sum(m[3*i+j] * x[j] for j in LABELS) % 3 for i in LABELS)
    ready = [m for m in group if all(evaluate(m, (j, a, a)) == (j, a, j)
                                     for j, a in product(LABELS, repeat=2))]
    keep_j = [m for m in ready if m[:3] == IDENTITY[:3]]
    keep_both = [m for m in keep_j if m[:6] == IDENTITY[:6]]
    assert (len(ready), len(keep_j), len(keep_both)) == (18, 6, 2)
    distances_read_only = distances(((0, 2), (1, 2)))
    costs = {str(m[-3:]): distances_read_only[m] for m in keep_both}
    assert costs == {'(1, 2, 1)': 2, '(1, 1, 2)': 3}
    return {'all_linear_ready_extensions': len(ready), 'keep_source': len(keep_j),
            'keep_source_and_reference': costs}


def nonlinear(x):
    j, a, r = x
    return (a, j, r) if len(set(x)) == 3 else x


def nonlinearity():
    images = [nonlinear(x) for x in TRIPLES]
    assert len(set(images)) == 27
    for phi in permutations(LABELS):
        for x in TRIPLES:
            assert nonlinear(tuple(phi[i] for i in x)) == tuple(phi[i] for i in nonlinear(x))
    for i in LABELS:
        standard = tuple(int(i == j) for j in LABELS)
        assert nonlinear(standard) == standard
    assert nonlinear((0, 1, 2)) == (1, 0, 2)
    return {'equivariant_permutations': 6**4 * 24, 'linear_local_group': 432, 'index': 72,
            'nonlinear_witness_moved_triples': sum(x != y for x, y in zip(TRIPLES, images))}


def positive_writes(repo):
    previous = Path(__file__).resolve().parents[1] / 'fiftieth' / 'calibration_check.py'
    adapter = runpy.run_path(str(previous))
    brc = adapter['load'](repo)
    data = (repo / 'research_tasks' / 'RS-EULER-RR-01-LOCAL-COUPLING-20261011.md').read_bytes()
    book = sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    assert book == '83e85caf3c313b10486b346a7b4290129385ab6b'
    offsets = {(j, (b,)): Fraction(1 + 3 * int(b == j), 18) for j, b in product(LABELS, repeat=2)}
    old_costs = Counter()
    old = adapter['finite_kernel'](brc, old_costs, offsets)
    assert old['best_score'] == '2/3'
    rows, counts = [], Counter()
    for sheet in (-1, 1):
        output = Counter()
        for j, a, r in TRIPLES:
            w = brc.cwm_edge(offsets[j, ((r-a) % 3,)] / 3)
            start = w.total
            state = (j, a, r)
            for source_index in (0, 1):
                voter = state[source_index]
                intended = reflection(voter, state[2])
                turns = (sheet * (intended - state[2])) % 3
                for _ in range(turns or 1):
                    state = (state[0], state[1], (state[2] + sheet * bool(turns)) % 3)
                    w = brc.cwm_propagate(w, brc.CWM_ONE)
                    counts['contact' if turns else 'hold'] += 1
                assert state == (j, a, intended) and w.total == start
            assert state == (j, a, (r+j-a) % 3)
            output[j, state[2]] += w.total
            if sheet == 1:
                rows.append([j, a, r, reflection(j, r), state[2]])
        assert [[str(3 * output[j, y]) for y in LABELS] for j in LABELS] == old['channel_by_source']
    assert counts == {'contact': 108, 'hold': 36}
    return {'taskbook_git_blob': book, 'public_pins': adapter['PINS'],
            'benchmark_adapter_sha256': sha256(previous.read_bytes()).hexdigest(),
            'rows_j_a_receiver_initial_middle_final': rows, 'two_sheet_positive_primitive_calls': dict(counts),
            'one_sheet_original_E_calls': dict(old_costs), 'original_positive_channel': old['channel_by_source'],
            'optimal_single_record_score': old['best_score']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path, required=True)
    args = parser.parse_args()
    result = {'binary_tables': binary_gates(), 'directed_graphs': all_graphs(),
              'equivariant_boundary': nonlinearity(), 'prepared_extensions': prepared_endpoints(), 'source_integration': positive_writes(args.repo)}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
