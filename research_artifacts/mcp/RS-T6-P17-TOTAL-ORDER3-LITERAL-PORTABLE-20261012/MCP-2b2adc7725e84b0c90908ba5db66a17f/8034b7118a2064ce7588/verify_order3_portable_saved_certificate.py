#!/usr/bin/env python3
"""Prepare a standalone order3 saved-certificate consumer; default is NOT_ADMITTED.

The separate rational math core comes from frozen own Source consumer096dcfb.
Parent EM-T6-B4F89F statically extracted it, made JSON float rejection explicit,
and removed only the old q2-1 exclusion / relabeled the order3 error. The new
canonical-input/control/portable CLI adapter has UNKNOWN native helper author,
in a directed shared-owner nonblind context. This is not native independence
or acceptance. No producer is imported. Verification only consumes saved trees.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
PORTABLE_SHA = "7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce"
PROSPECTIVE_INPUT_SHA = "c7a2624f7b9fbb9437b0b1756b323a879926ff138f82b816c6de60790a36371a"
SCOPE = "ALL_3264_LITERAL_RELAXED_TOTAL_ORDER3_PATTERNS"
ACTOR = "EM-T6-B4F89F"
SID = "MCP-2b2adc7725e84b0c90908ba5db66a17f"
SIDE_BUDGET = 2331
def reject_float(value):
    raise ValueError("Floating and nonfinite JSON forbidden")


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
    return raw, json.loads(raw.decode('utf-8'), object_pairs_hook=unique_object, parse_float=reject_float, parse_constant=reject_float)

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

def common_basis(portable, problem, max_radius):
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
        require(squared[i] > 2 * max_radius, 'One-nonpreferred uniform strict bound fails')
        orthogonal.append([Fraction(weighted[i][c]) -
                           sum(mu[i][k] * orthogonal[k][c] for k in range(i))
                           for c in range(16)])
        require(dot(orthogonal[i], orthogonal[i]) == squared[i], 'GS norm identity fails')
    require(squared == list(map(fraction, portable['gram_schmidt_squared'])),
            'Portable GS squared lengths mismatch')
    require(mu == [[fraction(v) for v in row] for row in portable['mu']],
            'Portable GS coefficients mismatch')
    return weights, coefficients, moduli, unweighted, weighted, mu, squared, orthogonal

def largest_prime_factor(value):
    require(value > 0, 'Nonpositive atom cofactor')
    largest, divisor = 1, 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            largest = divisor
            value //= divisor
        divisor += 1
    return max(largest, value)

def completion_from_saved_vector(derived, vector, positive, negative):
    """Recompute moments and necessary cuts of an existing local vector, without search."""
    remaining_positive = derived['positive_budget'] - positive
    remaining_negative = derived['negative_budget'] - negative
    require(min(remaining_positive, remaining_negative) >= 0, 'Negative survivor residual budget')
    positive_denominators = [17 * (17 * integer(q) + integer(r))
                             for q, r in derived['positive_atoms']]
    negative_denominators = [17 * (17 * integer(q) + integer(r))
                             for q, r in derived['negative_atoms']]
    moments = [Fraction(len(positive_denominators) - len(negative_denominators) + sum(vector))]
    for power in range(1, 7):
        moment = sum((Fraction(1, denominator ** power) for denominator in positive_denominators), Fraction(0))
        moment -= sum((Fraction(1, denominator ** power) for denominator in negative_denominators), Fraction(0))
        moment += sum((Fraction(value, (17 * j) ** power) for j, value in enumerate(vector, 1)), Fraction(0))
        require(moment.denominator % 17 != 0, 'Local mixed congruence leaves an uncanceled p17 pole')
        moments.append(moment)
    encode = lambda value: [str(value.numerator), str(value.denominator)]
    cuts = []
    for power, moment in enumerate(moments):
        lower = -Fraction(remaining_positive, 2 ** power)
        upper = Fraction(remaining_negative, 2 ** power)
        cuts.append({'k': power, 'M_k': encode(moment), 'lower': encode(lower),
                     'upper': encode(upper), 'passes': lower <= moment <= upper})
    return {'remaining_positive_budget': str(remaining_positive),
            'remaining_negative_budget': str(remaining_negative),
            'moments_M0_to_M6': list(map(encode, moments)),
            'necessary_completion_cuts': cuts,
            'status': 'OPEN_AFTER_NECESSARY_CUTS' if all(cut['passes'] for cut in cuts)
                      else 'EXCLUDED_BY_NAMED_NECESSARY_CUT',
            'local_survivor_retained': True,
            'completion_equations': 'sum_a t_a/a^k=-M_k for k=0..6; a>=2,17-free; separate (a-1)-weighted residual masses',
            'lower_prime_carrier_allowed_only_if_maximal_p17_admissible': derived['maximal_p17_admissible'],
            'full_collision_claim': False}

def consume_case(common, derived, ledger):
    """Check only saved nodes of one variable-radius tree, requiring both integer edges."""
    weights, coefficients, moduli, unweighted, weighted, mu, squared, orthogonal = common
    pattern_id = derived['pattern_id']
    require(ledger['pattern_id'] == pattern_id, 'Saved pattern ID mismatch')
    encoding = ledger.get('certificate_encoding')
    require(encoding in (None, 'COMPACT_INDEXED_TWO_CHOICE_TREE_V1'), 'Unknown certificate encoding')
    compact = encoding == 'COMPACT_INDEXED_TWO_CHOICE_TREE_V1'
    for key in ('positive_atoms', 'negative_atoms'):
        if not compact or key in ledger:
            require(ledger[key] == derived[key], 'Saved atom descriptors mismatch')
    radius = derived['radius_squared']
    positive_budget = derived['positive_budget']
    negative_budget = derived['negative_budget']
    targets = derived['targets']
    for key, expected in [('q0_positive_budget', positive_budget), ('q0_negative_budget', negative_budget),
                          ('radius_squared', radius), ('largest_vertical_prime', derived['largest_vertical_prime']),
                          ('positive_vertical_mass', derived['positive_fixed_mass']),
                          ('negative_vertical_mass', derived['negative_fixed_mass'])]:
        if not compact or key in ledger:
            require(integer(ledger[key]) == expected, 'Saved variable numeric input mismatch: ' + key)
    for key, expected in [('mixed_targets', targets), ('weights', weights), ('moduli', moduli)]:
        if not compact or key in ledger:
            require(list(map(integer, ledger[key])) == expected, 'Saved variable/common input mismatch: ' + key)
    if not compact or 'coefficients' in ledger:
        require([[integer(v) for v in row] for row in ledger['coefficients']] == coefficients,
                'Saved common coefficients mismatch')
    if not compact or 'maximal_p17_admissible' in ledger:
        require(type(ledger['maximal_p17_admissible']) is bool and
                ledger['maximal_p17_admissible'] == derived['maximal_p17_admissible'], 'Saved domain flag mismatch')
    require(ledger['literal_relaxed_outcome_even_if_outside_domain'] is True,
            'Outside-domain descriptors must retain their literal relaxed classification')
    particular = list(map(integer, ledger['particular_q0']))
    require(len(particular) == 16, 'Affine representative dimension mismatch')
    require(all(sum(a * b for a, b in zip(particular, row)) % modulus == target
                for row, modulus, target in zip(coefficients, moduli, targets)), 'Wrong affine mixed class')
    weighted_particular = [a * b for a, b in zip(particular, weights)]
    centers = [dot(weighted_particular, row) / diagonal for row, diagonal in zip(orthogonal, squared)]
    if not compact or 'affine_centers' in ledger:
        require(list(map(fraction, ledger['affine_centers'])) == centers, 'Target-specific affine centers mismatch')
    require(sum(center ** 2 * diagonal for center, diagonal in zip(centers, squared)) ==
            dot(weighted_particular, weighted_particular), 'Affine norm decomposition fails')
    nodes = {index(node['id']): node for node in ledger['nodes']}
    require(len(nodes) == len(ledger['nodes']) and len(nodes) <= 136,
            'Duplicate nodes or uniform one-nonpreferred node bound exceeded')
    root = index(ledger['root'])
    require(root in nodes, 'Saved root missing')
    seen, survivors = set(), []
    counters = {'nodes': 0, 'edges': 0, 'norm_pruned': 0, 'budget_pruned': 0,
                'full_leaves': 0, 'resource_stops': 0}

    def consume(node_id, coordinate, suffix, partial):
        require(node_id not in seen and node_id in nodes, 'Repeated or missing saved node')
        seen.add(node_id)
        node = nodes[node_id]
        counters['nodes'] += 1
        require(index(node['index']) == coordinate, 'Saved coordinate mismatch')
        if not compact or 'suffix' in node:
            require(list(map(integer, node['suffix'])) == suffix, 'Saved suffix mismatch')
        if not compact or 'partial_norm' in node:
            require(fraction(node['partial_norm']) == partial, 'Saved partial norm mismatch')
        require(partial <= radius, 'Pruned branch incorrectly continued')
        center = centers[coordinate] + sum(value * mu[higher][coordinate]
                                          for higher, value in enumerate(suffix, coordinate + 1))
        if not compact or 'center' in node:
            require(fraction(node['center']) == center, 'Saved center mismatch')
        quotient, remainder = divmod(center.numerator, center.denominator)
        if not compact or 'floor' in node:
            floor = node['floor']
            require(integer(floor['quotient']) == quotient and integer(floor['remainder']) == remainder and
                    integer(floor['denominator']) == center.denominator, 'Exact floor witness mismatch')
        edges = node['edges']
        require(len(edges) == 2 and sorted(integer(edge['z']) for edge in edges) ==
                [-quotient - 1, -quotient], 'Missing or repeated adjacent integer edge')
        for edge in edges:
            counters['edges'] += 1
            z = integer(edge['z'])
            norm = partial + squared[coordinate] * (z + center) ** 2
            if not compact or 'partial_norm' in edge:
                require(fraction(edge['partial_norm']) == norm, 'Saved edge norm mismatch')
            action = edge['action']
            if norm > radius:
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
            if not compact or 'vector' in edge:
                require(list(map(integer, edge['vector'])) == vector, 'Full vector mismatch')
            require(sum((value * weight) ** 2 for value, weight in zip(vector, weights)) == norm,
                    'Full vector norm mismatch')
            positive = sum(weight * max(value, 0) for value, weight in zip(vector, weights))
            negative = sum(weight * max(-value, 0) for value, weight in zip(vector, weights))
            require(all(sum(a * b for a, b in zip(vector, row)) % modulus == target
                        for row, modulus, target in zip(coefficients, moduli, targets)), 'Full mixed congruence mismatch')
            if 'positive_mass' in edge:
                require(integer(edge['positive_mass']) == positive, 'Reported positive mass mismatch')
            if 'negative_mass' in edge:
                require(integer(edge['negative_mass']) == negative, 'Reported negative mass mismatch')
            if 'mixed_residues' in edge:
                require(list(map(integer, edge['mixed_residues'])) == targets, 'Reported leaf residues mismatch')
            if 'weighted_norm' in edge:
                require(fraction(edge['weighted_norm']) == norm, 'Reported full-leaf weighted norm mismatch')
            for key, expected in [('positive_budget', positive_budget), ('negative_budget', negative_budget)]:
                if key in edge:
                    require(integer(edge[key]) == expected, 'Reported full-leaf budget mismatch: ' + key)
            feasible = positive <= positive_budget and negative <= negative_budget
            require(action == ('SURVIVOR' if feasible else 'BUDGET_PRUNED'), 'Leaf signed-budget classification mismatch')
            if feasible:
                survivors.append({'q0': list(map(str, vector)), 'q0_positive_mass': str(positive),
                                  'q0_negative_mass': str(negative),
                                  'total_positive_mass_with_atoms': str(positive + derived['positive_fixed_mass']),
                                  'total_negative_mass_with_atoms': str(negative + derived['negative_fixed_mass']),
                                  'mixed_residues': list(map(str, targets)),
                                  'full_H0_lower_prime_completion': 'OPEN_NOT_A_FULL_COLLISION',
                                  'completion': completion_from_saved_vector(derived, vector, positive, negative)})
            else:
                counters['budget_pruned'] += 1

    consume(root, 15, [], Fraction(0))
    require(seen == set(nodes) and counters['edges'] <= 272, 'Unreachable nodes or edge bound exceeded')
    require(ledger['survivors'] == survivors, 'Saved survivor list or exact completion obligations mismatch')
    require(type(ledger['complete_traversal']) is bool and
            ledger['complete_traversal'] == (counters['resource_stops'] == 0), 'Saved completion flag mismatch')
    require(type(ledger['resource_exhausted']) is bool and
            ledger['resource_exhausted'] == (counters['resource_stops'] > 0), 'Saved resource flag mismatch')
    if 'global_T6_complete' in ledger:
        require(ledger['global_T6_complete'] is False, 'A local order3 proof cannot close global T6')
    outcome = ledger['outcome']
    if outcome == 'EMPTY':
        require(not survivors and not counters['resource_stops'], 'Incomplete or surviving EMPTY claim')
    elif outcome == 'LOCAL_KERNEL':
        require(bool(survivors), 'Local kernel lacks independently verified survivor')
    elif outcome == 'RESOURCE_EXHAUSTED':
        require(counters['resource_stops'] > 0, 'Resource outcome lacks unresolved saved edge')
    else:
        raise ValueError('Unknown relaxed-class outcome; domain exclusion is not classification')
    for key, actual in [('node_count', counters['nodes']), ('edge_count', counters['edges']),
                        ('pruned_edges', counters['norm_pruned']), ('full_sphere_leaves', counters['full_leaves']),
                        ('budget_pruned', counters['budget_pruned'])]:
        if key in ledger:
            require(type(ledger[key]) is int and ledger[key] == actual, 'Reported case count mismatch: ' + key)
    return {'pattern_id': pattern_id, 'outcome': outcome,
            'maximal_p17_admissible': derived['maximal_p17_admissible'],
            'largest_vertical_prime': str(derived['largest_vertical_prime']),
            'q0_positive_budget': str(positive_budget), 'q0_negative_budget': str(negative_budget),
            'radius_squared': str(radius), 'counters': counters, 'survivors': survivors,
            'complete_saved_tree_consumed': counters['resource_stops'] == 0}


EXPECTED_COUNTS = {'q3_single': 16, 'q2_q1_same': 256, 'q2_q1_opposite': 256,
                   'q1_triple_same': 816, 'q1_triple_mixed': 1920}
COMPACT_ENCODING = 'COMPACT_INDEXED_TWO_CHOICE_TREE_V1'
EXPECTED_PRIOR_IDS = {'EM-DIRECT-E1F2B6', 'EM-DIRECT-FA0C27', 'EM-DIRECT-49ADE6',
                      'EM-DVR-C1A1D9', 'EM-DVR-4C90FB', 'EM-DVR-FBF223', 'EM-T6-B4F89F'}


def canonical_order3_descriptors():
    """Independent finite descriptor loops; invoked only for explicitly admitted saved-proof verification."""
    descriptors = {}
    def add(name, plus, minus, family):
        require(name not in descriptors, 'Duplicate independently canonicalized ID')
        descriptors[name] = (plus, minus, family)
    for residue in range(1, 17):
        add(f'q3-single-{residue:02}', [(3, residue)], [], 'q3_single')
    for order2_residue in range(1, 17):
        for order1_residue in range(1, 17):
            add(f'q3-q2q1-same-{order2_residue:02}-{order1_residue:02}',
                [(2, order2_residue), (1, order1_residue)], [], 'q2_q1_same')
            add(f'q3-q2q1-opposite-{order2_residue:02}-{order1_residue:02}',
                [(2, order2_residue)], [(1, order1_residue)], 'q2_q1_opposite')
    for a in range(1, 17):
        for b in range(a, 17):
            for c in range(b, 17):
                add(f'q3-q1triple-same-{a:02}-{b:02}-{c:02}',
                    [(1, a), (1, b), (1, c)], [], 'q1_triple_same')
            for c in range(1, 17):
                if c not in (a, b):
                    add(f'q3-q1triple-mixed-{a:02}-{b:02}-vs-{c:02}',
                        [(1, a), (1, b)], [(1, c)], 'q1_triple_mixed')
    require(len(descriptors) == 3264, 'Independent canonical descriptor family size mismatch')
    for family, expected in EXPECTED_COUNTS.items():
        require(sum(value[2] == family for value in descriptors.values()) == expected,
                'Independent canonical family count mismatch: ' + family)
    return descriptors


def repeated_prime_factors(value):
    require(type(value) is int and value > 0, 'Invalid cofactor')
    result, divisor = [], 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            result.append(divisor)
            value //= divisor
        divisor += 1
    if value > 1:
        result.append(value)
    return result


def input_atoms(value):
    require(type(value) is list, 'Prospective atom side must be a list')
    result = []
    for atom in value:
        require(type(atom) is list and len(atom) == 2 and all(type(v) is int for v in atom),
                'Prospective atom must use its pinned JSON integer schema')
        q, r = atom
        require(q in (1, 2, 3) and 1 <= r <= 16, 'Prospective atom outside order3 domain')
        result.append((q, r))
    return result


def derive_order3_inputs(prospective, portable_raw):
    """Recompute pinned input descriptors and static arithmetic, never produce a feasibility tree."""
    require(prospective['schema'] == 'T6_P17_TOTAL_ORDER3_LITERAL_FULL3264_PROSPECTIVE_INPUT_V1' and
            prospective['scientific_feasibility_executed'] is False and
            prospective['classifier_result_asserted'] is False, 'Prospective input cannot itself assert results')
    scope = prospective['scope']
    require(scope['literal_descriptor_count'] == 3264 and scope['maximal_p17_admissible_count'] == 1405 and
            scope['outside_domain_count'] == 1859 and scope['total_vertical_order'] == 3 and
            scope['overall_sign_quotient'] is True, 'Pinned descriptor scope mismatch')
    fixed = prospective['fixed_rule']
    weights = [17 * j - 1 for j in range(1, 17)]
    moduli = [17 ** k for k in range(1, 7)]
    require(fixed['prime'] == 17 and fixed['side_exponent_mass_limits'] == [2331, 2331] and
            fixed['q0_weights'] == weights and list(map(integer, fixed['mixed_moduli'])) == moduli,
            'Pinned fixed rule numeric fields mismatch')
    common = prospective['common_input']
    require(common['sha256'] == PORTABLE_SHA and common['bytes'] == len(portable_raw) and
            common['git_blob_sha1'] == hashlib.sha1(b'blob ' + str(len(portable_raw)).encode() + b'\0' + portable_raw).hexdigest(),
            'Prospective/common Source byte join mismatch')
    contribution = prospective['construction_contributions']
    require(contribution['driver_input_author'] == 'EM-DVR-4CF7AF' and
            contribution['root_direction_and_static_cost_author'] == 'EM-DVR-FBF223' and
            set(contribution['prior_scientific_contributor_ids']) == EXPECTED_PRIOR_IDS and
            len(contribution['prior_scientific_contributor_ids']) == 7 and
            contribution['subsequent_result_requires_genuinely_independent_nonauthor_review'] is True,
            'Root/Driver input authorship or subsequent review restriction changed')
    descriptors = canonical_order3_descriptors()
    rows = prospective['cases']
    require(len(rows) == 3264 and len({row['case_id'] for row in rows}) == 3264 and
            {row['case_id'] for row in rows} == set(descriptors), 'Pinned input ID closure mismatch')
    derived = {}
    for row in rows:
        name = row['case_id']
        plus, minus = input_atoms(row['positive_atoms']), input_atoms(row['negative_atoms'])
        expected_plus, expected_minus, family = descriptors[name]
        require(plus == expected_plus and minus == expected_minus and
                sum(q for q, _ in plus + minus) == 3 and not (set(plus) & set(minus)),
                'Primitive/sign-normalized descriptors mismatch: ' + name)
        cofactors = [17 * q + r for q, r in plus + minus]
        atom_data = [{'q': q, 'r': r, 'cofactor': 17 * q + r, 'denominator': 17 * (17 * q + r),
                      'exponent_mass': 17 * (17 * q + r) - 1,
                      'prime_factors': repeated_prime_factors(17 * q + r)} for q, r in plus + minus]
        require(row['atom_data'] == atom_data, 'Input atom arithmetic/factorization mismatch: ' + name)
        positive_mass = sum(17 * (17 * q + r) - 1 for q, r in plus)
        negative_mass = sum(17 * (17 * q + r) - 1 for q, r in minus)
        positive_budget, negative_budget = SIDE_BUDGET - positive_mass, SIDE_BUDGET - negative_mass
        require(min(positive_budget, negative_budget) >= 0, 'Negative fixed-atom residual budget')
        radius = positive_budget ** 2 + negative_budget ** 2
        targets = [(sum(pow(17 * q + r, -k, 17 ** k) for q, r in minus) -
                    sum(pow(17 * q + r, -k, 17 ** k) for q, r in plus)) % (17 ** k) for k in range(1, 7)]
        largest = max([17] + [largest_prime_factor(cofactor) for cofactor in cofactors])
        admissible = largest == 17
        require(list(map(integer, row['q0_side_budgets'])) == [positive_budget, negative_budget] and
                integer(row['radius_squared']) == radius and list(map(integer, row['mixed_rhs'])) == targets,
                'Input budgets/radius/mixed targets mismatch: ' + name)
        require(row['maximal_p17_domain'] == ('ADMISSIBLE' if admissible else 'OUTSIDE_DOMAIN'),
                'Input maximal-p17 domain flag mismatch: ' + name)
        derived[name] = {'pattern_id': name, 'positive_atoms': [[str(q), str(r)] for q, r in plus],
                         'negative_atoms': [[str(q), str(r)] for q, r in minus],
                         'positive_fixed_mass': positive_mass, 'negative_fixed_mass': negative_mass,
                         'positive_budget': positive_budget, 'negative_budget': negative_budget,
                         'radius_squared': radius, 'targets': targets, 'largest_vertical_prime': largest,
                         'maximal_p17_admissible': admissible, 'canonical_family': family}
    require(sum(row['maximal_p17_admissible'] for row in derived.values()) == 1405,
            'Independently derived admissible/outside partition mismatch')
    radii = [row['radius_squared'] for row in derived.values()]
    require(max(radii) == integer(prospective['static_cost']['max_radius_squared']) and
            min(radii) == integer(prospective['static_cost']['min_radius_squared']),
            'Prospective radius extrema mismatch')
    problem_view = {'weights': list(map(str, weights)), 'moduli': list(map(str, moduli)),
                    'coefficients': [[str(pow(j, -k, 17 ** k)) for j in range(1, 17)] for k in range(1, 7)]}
    return derived, problem_view


def join_observed_actual_context(context_raw, context, certificate):
    """Join actual saved metadata; do not create admission, identity or fresh liveness authority."""
    require(context.get('native_authorized') is True and context.get('scope') == SCOPE and
            context.get('researcher_id') == ACTOR and context.get('session_id') == SID,
            'NOT_ADMITTED: actual own order3 native context is required')
    require(context.get('total_vertical_order') == 3 and
            context.get('include_outside_domain_patterns') is True and
            context.get('excluded_replay_pattern_ids') == [],
            'Observed context must authorize the entire literal order3 family without exclusions')
    for key in ('task_id', 'publication_id', 'claim_id', 'execution_record_id', 'run_id'):
        require(type(context.get(key)) is str and bool(context[key]), 'Actual dynamic context field absent: ' + key)
    require(type(context.get('run_generation')) is int and context['run_generation'] > 0 and
            context.get('fenced_by_claim_id') is None, 'Actual run generation/fence metadata mismatch')
    require(context.get('global_goal_status') == 'OPEN' and
            context.get('native_mathematical_acceptance_granted') is False and
            context.get('platform_session_attested') is False, 'Actual acceptance/goal/provenance boundary changed')
    require(certificate['task_id'] == context['task_id'] and certificate['publication_id'] == context['publication_id'],
            'Certificate/dynamic Task/publication mismatch')
    expected = {key: context[key] for key in ('researcher_id', 'session_id', 'claim_id', 'execution_record_id',
                                            'run_id', 'run_generation')}
    require(certificate['own_actual_control'] == expected and
            certificate['control_evidence']['context_sha256'] == hashlib.sha256(context_raw).hexdigest(),
            'Saved certificate/actual observed context byte join mismatch')
    if 'native_authority_granted_by_local_code' in certificate['control_evidence']:
        require(certificate['control_evidence']['native_authority_granted_by_local_code'] is False,
                'Local code cannot grant native authority')
    return {'metadata_only_no_native_receipt_paths_opened': True,
            'observed_context_sha256': hashlib.sha256(context_raw).hexdigest(),
            'native_admission_or_acceptance_created_by_consumer': False}


def verify_order3_saved_certificate(portable, prospective, portable_raw, certificate):
    require(certificate['schema'] == 'T6_P17_TOTAL_ORDER3_COMPACT_CERTIFICATE_V1' and
            certificate['certificate_encoding'] == COMPACT_ENCODING,
            'Saved certificate must use the agreed complete order3 compact schema')
    require(certificate['new_pattern_count'] == 3264 and certificate['prime17_admissible_count'] == 1405 and
            certificate['outside_domain_count'] == 1859 and
            certificate['common_input_sha256'] == PORTABLE_SHA and
            certificate['order3_input_sha256'] == PROSPECTIVE_INPUT_SHA,
            'Saved certificate count/common/order3 input pins mismatch')
    require(certificate['global_T6_complete'] is False and certificate['q2_family_replayed'] is False and
            certificate['complete_traversal'] is True and certificate['resource_exhausted'] is False and
            certificate['outside_patterns_classified_not_skipped'] is True,
            'Resource/outside/replay/global scope cannot substitute for a complete classification')
    derived, problem_view = derive_order3_inputs(prospective, portable_raw)
    maximum = max(row['radius_squared'] for row in derived.values())
    common = common_basis(portable, problem_view, maximum)
    require(min(common[6]) == fraction(prospective['static_cost']['common_exact_GS_min']),
            'Independently reconstructed common GS minimum mismatch')
    records = certificate['case_ledgers']
    require(len(records) == 3264 and len({row['pattern_id'] for row in records}) == 3264 and
            {row['pattern_id'] for row in records} == set(derived), 'Saved 3264 complete ID closure mismatch')
    require(certificate['completed_pattern_ids'] == [row['pattern_id'] for row in records],
            'Saved completed-ID order differs from records')
    mandatory = {'certificate_encoding', 'pattern_id', 'outcome', 'particular_q0', 'root', 'nodes', 'survivors',
                 'complete_traversal', 'resource_exhausted', 'maximal_p17_admissible', 'largest_vertical_prime',
                 'positive_atoms', 'negative_atoms', 'positive_vertical_mass', 'negative_vertical_mass',
                 'q0_positive_budget', 'q0_negative_budget', 'radius_squared', 'mixed_targets',
                 'literal_relaxed_outcome_even_if_outside_domain'}
    summaries = []
    for record in records:
        require(mandatory <= set(record) and record['certificate_encoding'] == COMPACT_ENCODING and
                record['complete_traversal'] is True and record['resource_exhausted'] is False,
                'Saved compact tree must contain every mandatory scientific field and be complete')
        require(record['outcome'] in ('EMPTY', 'LOCAL_KERNEL'), 'Unclassified/resource outcome is not family completion')
        summary = consume_case(common, derived[record['pattern_id']], record)
        require(summary['complete_saved_tree_consumed'], 'Incomplete saved case cannot complete the family')
        summaries.append(summary)
    totals = {key: sum(row['counters'][key] for row in summaries)
              for key in ('nodes', 'edges', 'norm_pruned', 'budget_pruned', 'full_leaves', 'resource_stops')}
    require(totals['nodes'] <= 3264 * 136 and totals['edges'] <= 887808 and totals['resource_stops'] == 0,
            'Complete saved-tree uniform bounds/resource flags fail')
    classifications = {outcome: sum(row['outcome'] == outcome for row in summaries) for outcome in ('EMPTY', 'LOCAL_KERNEL')}
    for key, actual in [('total_node_count', totals['nodes']), ('total_edge_count', totals['edges']),
                        ('survivor_count', sum(len(row['survivors']) for row in summaries))]:
        require(type(certificate[key]) is int and certificate[key] == actual, 'Saved family total mismatch: ' + key)
    require(certificate['classification_counts'] == classifications, 'Saved family outcome totals mismatch')
    return {'status': 'PORTABLE_ORDER3_SAVED_CERTIFICATE_CHECK_PASS', 'pattern_count': 3264,
            'admissible_count': 1405, 'outside_literal_relaxed_count': 1859,
            'classification_counts': classifications, 'totals': totals, 'case_summaries': summaries,
            'all3264_saved_trees_complete': True, 'all3264_relaxed_classes_EMPTY': classifications['EMPTY'] == 3264,
            'no_workspace_verbose_or_old_q2_native_artifact_required': True,
            'no_q2_proof_tree_or_prior_ledger_math_consumed': True, 'q2_family_replayed': False,
            'native_helper_author_identity': 'UNKNOWN', 'nonblind_shared_owner': True,
            'prior_math_core_Source_sha256': '096dcfb3e0850c54743cf37153b1283bc2a703b9355b95fb2db6892491564995',
            'Parent_core_adaptation_author': ACTOR,
            'Parent_core_adaptation': 'Explicit float/nonfinite rejection; remove old q2-1-only exclusion; relabel order3 error',
            'new_adapter_author_native_identity': 'UNKNOWN',
            'Root_and_current_Driver_input_authors_preserved': prospective['construction_contributions'],
            'subsequent_genuinely_independent_nonauthor_review_required': True,
            'native_mathematical_acceptance_asserted': False, 'global_T6_complete': False,
            'scientific_search_or_producer_execution': False,
            'method': 'Independent canonical inputs/kernel/Gram; consume existing complete compact nodes only'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', action='store_true', help='Consume an actually admitted saved certificate; never generate one')
    parser.add_argument('--portable')
    parser.add_argument('--input')
    parser.add_argument('--certificate')
    parser.add_argument('--context')
    parser.add_argument('--output')
    args = parser.parse_args()
    if not args.verify:
        print(json.dumps({'status': 'NOT_ADMITTED_CODE_PREPARATION_ONLY',
                          'scientific_function_executed': False, 'native_acceptance_asserted': False,
                          'requires_explicit_verify_and_actual_saved_context': True}))
        return
    for name in ('portable', 'input', 'certificate', 'context', 'output'):
        require(getattr(args, name) is not None, 'Missing required --' + name + ' for saved-proof verification')
    portable_raw, portable = read_json(args.portable)
    prospective_raw, prospective = read_json(args.input)
    certificate_raw, certificate = read_json(args.certificate)
    context_raw, context = read_json(args.context)
    require(hashlib.sha256(portable_raw).hexdigest() == PORTABLE_SHA and
            hashlib.sha256(prospective_raw).hexdigest() == PROSPECTIVE_INPUT_SHA, 'Pinned Source inputs differ')
    control_join = join_observed_actual_context(context_raw, context, certificate)
    report = verify_order3_saved_certificate(portable, prospective, portable_raw, certificate)
    report['task_id'], report['publication_id'] = context['task_id'], context['publication_id']
    report['observed_context_join'] = control_join
    report['input_sha256'] = {name: hashlib.sha256(raw).hexdigest() for name, raw in
                              [('portable', portable_raw), ('order3_input', prospective_raw),
                               ('certificate', certificate_raw), ('context', context_raw)]}
    output = Path(args.output)
    require(not output.exists(), 'Refuse to replace an existing saved-proof verification')
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: report[key] for key in ('status', 'pattern_count', 'admissible_count',
                     'outside_literal_relaxed_count', 'classification_counts', 'totals', 'global_T6_complete')}, indent=2))


if __name__ == '__main__':
    main()
