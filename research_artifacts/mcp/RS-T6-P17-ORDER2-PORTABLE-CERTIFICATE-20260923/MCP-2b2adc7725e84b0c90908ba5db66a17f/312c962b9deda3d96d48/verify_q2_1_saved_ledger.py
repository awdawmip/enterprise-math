#!/usr/bin/env python3
"""Consume a saved q2-1 proof ledger; never generate a feasibility search.

Call only after parent supplies actual own claim/open/run evidence.
The control-evidence argument is preserved by hash, not treated as native
authority conferred by this checker. Native helper identity stays UNKNOWN.

Scientific integers are decimal strings; fractions are [numerator,denominator]
strings. Indices/IDs alone may be JSON integers. Ledger contract:
  pattern_id='q2-1', outcome='EMPTY'|'LOCAL_KERNEL'|'RESOURCE_EXHAUSTED',
  particular_q0:16 strings, affine_centers:16 fractions, root:integer ID,
  nodes:[{id,index,suffix:[z_(index+1),...,z_15],partial_norm,center,
    floor:{quotient,remainder,denominator},edges:[
      {z,partial_norm,action:'NORM_PRUNED'|'CHILD'|'BUDGET_PRUNED'|
         'SURVIVOR'|'RESOURCE_STOP', child:ID if CHILD,
         vector:16 strings if full leaf}]}].
Both integers -floor(center)-1 and -floor(center) are required at every node.
Only nodes already in the ledger are visited. A CHILD must be an explicitly
saved node; this code never chooses or constructs missing feasibility nodes.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

PORTABLE_SHA = '7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce'
TASK_ID = 'RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923'
RADIUS = 8450730
POSITIVE = 1737
NEGATIVE = 2331


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value):
    require(isinstance(value, str), 'Scientific integer must be a decimal string')
    require(value and (value.isdecimal() or value[0] == '-' and value[1:].isdecimal()),
            'Invalid exact integer encoding')
    return int(value)


def fraction(value):
    require(isinstance(value, list) and len(value) == 2, 'Invalid fraction')
    numerator, denominator = map(integer, value)
    require(denominator > 0, 'Fraction denominator must be positive')
    return Fraction(numerator, denominator)


def index(value):
    require(type(value) is int, 'Index or node ID must be a JSON integer')
    return value


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'Duplicate JSON key')
        result[key] = value
    return result


def read_json(path):
    raw = Path(path).read_bytes()
    return raw, json.loads(raw.decode('utf-8'), object_pairs_hook=unique_object)


def dot(left, right):
    require(len(left) == len(right), 'Dot-product dimension mismatch')
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def determinant(matrix):
    """Bareiss elimination with every division checked exact."""
    n = len(matrix)
    work = [list(row) for row in matrix]
    require(all(len(row) == n for row in work), 'Determinant matrix not square')
    previous, sign = 1, 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if work[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            work[k], work[pivot_row] = work[pivot_row], work[k]
            sign = -sign
        pivot = work[k][k]
        for r in range(k + 1, n):
            for c in range(k + 1, n):
                numerator = work[r][c] * pivot - work[r][k] * work[k][c]
                quotient, remainder = divmod(numerator, previous)
                require(remainder == 0, 'Nonexact Bareiss division')
                work[r][c] = quotient
            work[r][k] = 0
        previous = pivot
    return sign * work[-1][-1]


def common_basis(portable, problem):
    weights = [17 * j - 1 for j in range(1, 17)]
    require(list(map(integer, portable['weights'])) == weights, 'Portable weights mismatch')
    require(list(map(integer, problem['weights'])) == weights, 'Problem weights mismatch')
    moduli = [17 ** k for k in range(1, 7)]
    require(list(map(integer, problem['moduli'])) == moduli, 'Mixed moduli mismatch')
    coefficients = [[pow(j, -k, 17 ** k) for j in range(1, 17)] for k in range(1, 7)]
    require([[integer(v) for v in row] for row in problem['coefficients']] == coefficients,
            'Reciprocal coefficient mismatch')
    unweighted = [[integer(v) for v in row] for row in portable['unweighted_basis']]
    weighted = [[integer(v) for v in row] for row in portable['weighted_basis']]
    require(len(unweighted) == len(weighted) == 16 and
            all(len(row) == 16 for row in unweighted + weighted), 'Basis dimension mismatch')
    require(abs(determinant(unweighted)) == 17 ** 21, 'Kernel index mismatch')
    require(determinant([row[:6] for row in coefficients]) % 17 != 0,
            'Mixed-map unit minor missing')
    for row, scaled in zip(unweighted, weighted):
        require(scaled == [value * weight for value, weight in zip(row, weights)],
                'Weighted basis mismatch')
        require(all(sum(a * b for a, b in zip(row, coefficient)) % modulus == 0
                    for coefficient, modulus in zip(coefficients, moduli)),
                'Basis outside mixed kernel')
    gram = [[dot(a, b) for b in weighted] for a in weighted]
    mu = [[Fraction(0) for _ in range(16)] for _ in range(16)]
    squared = []
    orthogonal = []
    for i in range(16):
        for j in range(i):
            mu[i][j] = (gram[i][j] - sum(mu[i][k] * mu[j][k] * squared[k]
                                      for k in range(j))) / squared[j]
        mu[i][i] = Fraction(1)
        squared.append(gram[i][i] - sum(mu[i][k] ** 2 * squared[k] for k in range(i)))
        require(squared[i] > RADIUS, 'Two-choice strict bound fails')
        orthogonal.append([Fraction(weighted[i][c]) -
                           sum(mu[i][k] * orthogonal[k][c] for k in range(i))
                           for c in range(16)])
        require(dot(orthogonal[i], orthogonal[i]) == squared[i], 'GS norm identity fails')
    require(squared == list(map(fraction, portable['gram_schmidt_squared'])),
            'Portable GS squared lengths mismatch')
    require(mu == [[fraction(v) for v in row] for row in portable['mu']],
            'Portable GS coefficients mismatch')
    return weights, coefficients, moduli, unweighted, weighted, mu, squared, orthogonal


def verify(portable, problem, ledger):
    require(ledger['pattern_id'] == 'q2-1', 'Outside authorized one-pattern scope')
    cases = [case for case in problem['cases'] if case['id'] == 'q2-1']
    require(len(cases) == 1, 'Missing or duplicate q2-1 descriptor')
    case = cases[0]
    require(case['positive_atoms'] == [['2', '1']] and case['negative_atoms'] == [],
            'Fixed atom mismatch')
    require(integer(case['q0_positive_budget']) == POSITIVE and
            integer(case['q0_negative_budget']) == NEGATIVE and
            integer(case['radius_squared']) == RADIUS, 'Budget or sphere mismatch')
    require(17 * 35 - 1 == 594 and 2331 - 594 == POSITIVE and
            POSITIVE ** 2 + NEGATIVE ** 2 == RADIUS, 'Fixed mass arithmetic fails')
    weights, coefficients, moduli, unweighted, weighted, mu, squared, orthogonal = common_basis(portable, problem)
    targets = [(-pow(35, -k, 17 ** k)) % (17 ** k) for k in range(1, 7)]
    require(list(map(integer, case['mixed_targets'])) == targets, 'Mixed target mismatch')
    particular = list(map(integer, ledger['particular_q0']))
    require(len(particular) == 16, 'Affine representative dimension mismatch')
    require(all(sum(a * b for a, b in zip(particular, coefficient)) % modulus == target
                for coefficient, modulus, target in zip(coefficients, moduli, targets)),
            'Affine representative outside q2-1 coset')
    weighted_particular = [a * b for a, b in zip(particular, weights)]
    centers = [dot(weighted_particular, row) / diagonal
               for row, diagonal in zip(orthogonal, squared)]
    require(list(map(fraction, ledger['affine_centers'])) == centers, 'q2 affine centers mismatch')
    require(sum(center ** 2 * diagonal for center, diagonal in zip(centers, squared)) ==
            dot(weighted_particular, weighted_particular), 'Affine norm decomposition fails')
    nodes = {index(node['id']): node for node in ledger['nodes']}
    require(len(nodes) == len(ledger['nodes']) and len(nodes) <= 131071,
            'Duplicate IDs or impossible tree bound')
    root = index(ledger['root'])
    require(root in nodes, 'Root missing')
    seen, survivors = set(), []
    counters = {'nodes': 0, 'edges': 0, 'norm_pruned': 0, 'budget_pruned': 0,
                'full_leaves': 0, 'resource_stops': 0}

    def consume(node_id, coordinate, suffix, partial):
        require(node_id not in seen and node_id in nodes, 'Repeated or missing saved node')
        seen.add(node_id)
        node = nodes[node_id]
        counters['nodes'] += 1
        require(index(node['index']) == coordinate, 'Saved coordinate mismatch')
        require(list(map(integer, node['suffix'])) == suffix, 'Saved suffix mismatch')
        require(fraction(node['partial_norm']) == partial, 'Saved partial norm mismatch')
        require(partial <= RADIUS, 'Pruned branch incorrectly continued')
        center = centers[coordinate] + sum(coefficient * mu[higher][coordinate]
                                          for higher, coefficient in enumerate(suffix, coordinate + 1))
        require(fraction(node['center']) == center, 'Saved center mismatch')
        quotient, remainder = divmod(center.numerator, center.denominator)
        floor = node['floor']
        require(integer(floor['quotient']) == quotient and
                integer(floor['remainder']) == remainder and
                integer(floor['denominator']) == center.denominator, 'Floor witness mismatch')
        edges = node['edges']
        require(len(edges) == 2 and sorted(integer(edge['z']) for edge in edges) ==
                [-quotient - 1, -quotient], 'Missing or duplicated feasible integer choice')
        for edge in edges:
            counters['edges'] += 1
            z = integer(edge['z'])
            norm = partial + squared[coordinate] * (z + center) ** 2
            require(fraction(edge['partial_norm']) == norm, 'Edge partial norm mismatch')
            action = edge['action']
            if norm > RADIUS:
                require(action == 'NORM_PRUNED', 'Exact norm prune not respected')
                counters['norm_pruned'] += 1
                continue
            if action == 'RESOURCE_STOP':
                counters['resource_stops'] += 1
                continue
            if coordinate:
                require(action == 'CHILD', 'Feasible partial branch omitted')
                consume(index(edge['child']), coordinate - 1, [z] + suffix, norm)
                continue
            counters['full_leaves'] += 1
            z_vector = [z] + suffix
            vector = [particular[c] + sum(z_vector[r] * unweighted[r][c] for r in range(16))
                      for c in range(16)]
            require(list(map(integer, edge['vector'])) == vector, 'Full leaf vector mismatch')
            require(sum((value * weight) ** 2 for value, weight in zip(vector, weights)) == norm,
                    'Full leaf norm mismatch')
            positive = sum(weight * max(value, 0) for value, weight in zip(vector, weights))
            negative = sum(weight * max(-value, 0) for value, weight in zip(vector, weights))
            feasible = positive <= POSITIVE and negative <= NEGATIVE
            require(action == ('SURVIVOR' if feasible else 'BUDGET_PRUNED'),
                    'Leaf signed-budget classification mismatch')
            require(all(sum(a * b for a, b in zip(vector, coefficient)) % modulus == target
                        for coefficient, modulus, target in zip(coefficients, moduli, targets)),
                    'Full leaf mixed congruence mismatch')
            if feasible:
                survivors.append({'q0_vector': list(map(str, vector)),
                                  'positive_q0_mass': str(positive), 'negative_q0_mass': str(negative),
                                  'positive_mass_with_fixed_atom': str(positive + 594),
                                  'remaining_H0_and_lower_prime_completion': 'OPEN'})
            else:
                counters['budget_pruned'] += 1

    consume(root, 15, [], Fraction(0))
    require(seen == set(nodes), 'Unreachable saved nodes')
    outcome = ledger['outcome']
    if outcome == 'EMPTY':
        require(not survivors and not counters['resource_stops'], 'Incomplete or surviving EMPTY claim')
    elif outcome == 'LOCAL_KERNEL':
        require(bool(survivors), 'Local kernel without verified survivor')
    elif outcome == 'RESOURCE_EXHAUSTED':
        require(counters['resource_stops'] > 0, 'Resource outcome without saved unresolved edge')
    else:
        raise ValueError('Unknown outcome')
    return {'status': 'INDEPENDENT_SAVED_LEDGER_PASS', 'pattern_id': 'q2-1',
            'outcome': outcome, 'counters': counters, 'survivors': survivors,
            'all_272_patterns_classified': False, 'global_T6_complete': False,
            'native_helper_identity': 'UNKNOWN', 'native_authority_asserted_by_checker': False,
            'method': 'Saved complete two-choice proof consumption; independent exact Gram/LDL and affine identities; no feasibility search generation'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--portable', required=True)
    parser.add_argument('--problem', required=True)
    parser.add_argument('--ledger', required=True)
    parser.add_argument('--control-evidence', required=True,
                        help='Actual parent-supplied own claim/open/run evidence; hash preserved only')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    portable_raw, portable = read_json(args.portable)
    require(hashlib.sha256(portable_raw).hexdigest() == PORTABLE_SHA, 'Portable Source pin mismatch')
    problem_raw, problem = read_json(args.problem)
    require(problem['common_basis_sha256'] == PORTABLE_SHA, 'Problem common-basis pin mismatch')
    ledger_raw, ledger = read_json(args.ledger)
    control_raw = Path(args.control_evidence).read_bytes()
    require(bool(control_raw), 'Actual control evidence missing')
    report = verify(portable, problem, ledger)
    report['task_id'] = TASK_ID
    report['input_sha256'] = {name: hashlib.sha256(raw).hexdigest() for name, raw in
                             [('portable', portable_raw), ('problem', problem_raw),
                              ('ledger', ledger_raw), ('control_evidence', control_raw)]}
    output = Path(args.output)
    require(not output.exists(), 'Refuse to overwrite an existing verification report')
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
