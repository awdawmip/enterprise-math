"""Exact finite checks for the fixed-source p-primary defect calculus."""
import argparse
from itertools import combinations, product
import json
from pathlib import Path


def valuation(a, p, k):
    if not a:
        return k
    exponent = 0
    while a % p == 0:
        a //= p
        exponent += 1
    return exponent


def smith_log_order(rows, p, k):
    """log_p of the span size via row/column elimination over Z/p^k."""
    q = p**k
    mat = [[entry % q for entry in row] for row in rows]
    total = 0
    while mat and mat[0]:
        depth, i, j = min((valuation(x, p, k), i, j)
                          for i, row in enumerate(mat) for j, x in enumerate(row))
        if depth == k:
            break
        mat[0], mat[i] = mat[i], mat[0]
        for row in mat:
            row[0], row[j] = row[j], row[0]
        d = p**depth
        inv = pow(mat[0][0] // d, -1, q)
        first = [inv * x % q for x in mat[0]]
        # Clear the first column. Further column operations on the pivot row
        # leave this lower-right block unchanged.
        mat = [[(x - row[0] // d * y) % q for x, y in zip(row[1:], first[1:])]
               for row in mat[1:]]
        total += k - depth
    return total


def row_membership(columns, b, p, k):
    """Is b B in Row A? Columns are pairs of observation and target tuples."""
    if not columns:
        return True
    rows = list(zip(*(u for u, _ in columns)))
    target = [sum(x*y for x, y in zip(b, v)) for _, v in columns]
    return smith_log_order(rows, p, k) == smith_log_order([*rows, target], p, k)


def combined_span(columns, q, s, t):
    span = {(0,)*(s+t)}
    for u, v in columns:
        col = u + v
        span = {tuple((x+c*y) % q for x, y in zip(z, col))
                for z in span for c in range(q)}
    return span


def fibers(span, s):
    result = {}
    for z in span:
        result.setdefault(z[:s], set()).add(z[s:])
    return result


def submask(left, right):
    return left & right == left


def minimal(family):
    result = []
    for m in sorted(set(family), key=lambda a: (a.bit_count(), a)):
        if not any(submask(c, m) for c in result):
            result.append(m)
    return tuple(result)


def small_system(columns, s, t, p, k):
    """Independent row Smith, column spans, obstruction antichains and joins."""
    q, n = p**k, len(columns)
    targets = list(product(range(q), repeat=t))
    masks = range(1 << n)
    obs, spaces = {}, {}
    for h in masks:
        sel = [col for j, col in enumerate(columns) if h & (1 << j)]
        spans = combined_span(sel, q, s, t)
        spaces[h] = fibers(spans, s)
        vertical = spaces[h][(0,)*s]
        answer = []
        for b in targets:
            good = all(sum(x*y for x, y in zip(b, v)) % q == 0 for v in vertical)
            assert good == row_membership(sel, b, p, k)
            answer.append(good)
        obs[h] = tuple(answer)

    for h, g in product(masks, repeat=2):
        left, right = spaces[h], spaces[g]
        common = left.keys() & right.keys()
        differences = {tuple((x-y) % q for x, y in zip(v, w)) for u in common
                       for v in left[u] for w in right[u]}
        assert differences == spaces[h | g][(0,)*s]

    increment_checks = 0
    for h in masks:
        before = spaces[h][(0,)*s]
        for i, (u, v) in enumerate(columns):
            after = spaces[h | (1 << i)][(0,)*s]
            depth = next(j for j in range(k+1)
                         if tuple(p**j*x % q for x in u) in spaces[h])
            base = tuple(p**depth*x % q for x in u)
            w = next(iter(spaces[h][base]))
            residual = tuple((p**depth*x-y) % q for x, y in zip(v, w))
            assert after == {tuple((x+c*y) % q for x, y in zip(z,residual))
                             for z in before for c in range(q)}
            level_sizes = []
            for j in range(k+1):
                bj = {tuple(p**j*x % q for x in z) for z in before}
                aj = {tuple(p**j*x % q for x in z) for z in after}
                quotient_size = len(aj)//len(bj)
                order = next(p**l for l in range(k+1)
                             if tuple(p**(j+l)*x % q for x in residual) in bj)
                assert quotient_size == order
                level_sizes.append(quotient_size)
            assert all(a//b in (1,p) and a%b == 0
                       for a,b in zip(level_sizes,level_sizes[1:]))
            increment_checks += 1

    circuits = [minimal(h for h in masks if not obs[h][j]) for j in range(len(targets))]
    assert all(c.bit_count() <= s+1 for family in circuits for c in family)
    signatures = {}
    for h in masks:
        reduced = tuple(minimal(c & ~h for c in family) for family in circuits)
        table = tuple(obs[h | u] for u in masks)
        assert table == tuple(tuple(not any(submask(c, u) for c in family)
                                    for family in reduced) for u in masks)
        signatures[h] = reduced
    essential = 0
    for family in circuits:
        for c in family:
            essential |= c
    for h, g in combinations(masks, 2):
        assert (signatures[h] == signatures[g]) == all(obs[h|u] == obs[g|u] for u in masks)
        if (h ^ g) & essential:
            i = ((h ^ g) & essential) & -((h ^ g) & essential)
            assert any(obs[u] != obs[u|i] for u in masks if not u&i)
        else:
            assert obs[h] == obs[g]
    return {'prime': p, 'length': k, 'columns': n, 'targets': len(targets),
            'smith_tests': len(masks)*len(targets), 'join_tests': len(masks)**2,
            'hide_only_classes': len(set(signatures.values())),
            'hide_and_reveal_classes': 1 << essential.bit_count(),
            'single_column_filtered_updates': increment_checks,
            'max_minimal_obstruction': max((c.bit_count() for f in circuits for c in f), default=0)}


def graph_family(p, k, s):
    q = p**k
    # The single named probe (e_i,c) creates the cyclic ideal (c-lambda_i).
    # Use Smith order on actual selected coordinate columns, not the formula.
    labels = list(product(range(q), repeat=s))
    eye = [tuple(int(i == j) for j in range(s)) for i in range(s)]
    signatures = set()
    for label in labels:
        graph = [(unit, (value,)) for unit, value in zip(eye, label)]
        signature = []
        for i, c in product(range(s), range(q)):
            cols = [*graph, (eye[i], (c,))]
            A = list(zip(*(u for u, _ in cols)))
            B = [v[0] for _, v in cols]
            delta = smith_log_order([*A, B], p, k) - smith_log_order(A, p, k)
            assert delta == k - valuation((c - label[i]) % q, p, k)
            signature.append(delta)
        signatures.add(tuple(signature))
    assert len(signatures) == q**s
    return {'prime': p, 'length': k, 'observation_rows': s, 'distinct_safe_histories': len(signatures),
            'single_probe_smith_checks':len(labels)*s*q}


def compute():
    low = [small_system([((1,), (0,)), ((1,), (1,)), ((1,), (0,))], 1, 1, p, k)
           for p, k in [(2, 1), (2, 2), (2, 3), (3, 2), (5, 2)]]
    low += [small_system([((1, 0), (0, 1)), ((0, 1), (0, 0)),
                          ((1, 1), (1, 1)), ((2, 2), (2, 0))], 2, 2, 2, 2)]
    # Each n=2 binary scalar system; all masks, all futures, all named targets.
    cols = list(product([(0,), (1,)], repeat=2))
    binary = [small_system(list(pair), 1, 1, 2, 1) for pair in product(cols, repeat=2)]
    graphs = [graph_family(p,k,s) for p,k,s in [(2,2,2),(2,3,2),(2,4,2),(3,2,2),
              (3,3,1),(3,4,1),(5,2,2),(5,3,1),(5,4,1)]]
    return {'fixed_examples':low, 'exhaustive_two_column_binary_systems':len(binary),
            'binary_join_tests':sum(r['join_tests'] for r in binary),
            'graph_families':graphs, 'total_graph_probe_checks':sum(r['single_probe_smith_checks'] for r in graphs)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', type=Path)
    args = parser.parse_args()
    data = compute()
    if args.verify:
        if data != json.loads(args.verify.read_text()):
            raise SystemExit('certificate mismatch')
        print('PASS')
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))
