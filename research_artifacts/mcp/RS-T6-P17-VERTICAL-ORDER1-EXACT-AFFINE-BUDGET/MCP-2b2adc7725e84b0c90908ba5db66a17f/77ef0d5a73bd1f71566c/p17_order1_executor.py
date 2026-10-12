"""Exact p17 order1 classifier. Preparation does not execute this census.

No author checkers or native control tools are imported. Canonical native
authorization is external to this mathematical module. The explicit CLI guard
records actual control provenance; it cannot authenticate or grant authority.
"""
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import json
import time

P = 17
N = 16
BUDGET = 2331
TASK_ID = 'RS-T6-P17-VERTICAL-ORDER1-EXACT-AFFINE-BUDGET'
CERT_SHA256 = 'fdf0b060d47bccd5b2a5095dc4b72d13b68476f49494eb4435b0b50dd30c65f6'
BOUND_SHA256 = 'b2175e24af7ab3c3a582c28262503f69241ca00f3024ca9c77e75db615beb647'
HERE = Path(__file__).resolve().parent


class InvariantError(RuntimeError):
    """Certificate or implementation failure; never a mathematical rejection."""


def require(condition, message):
    if not condition:
        raise InvariantError(message)


def exact_int(value):
    require(type(value) is int, 'expected an exact integer, not bool/float')
    return value


def reject_float(_value):
    raise InvariantError('floating JSON data is forbidden')


def read_json(path, expected_sha=None):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    require(expected_sha is None or digest == expected_sha, 'input SHA256 mismatch')
    return json.loads(raw, parse_float=reject_float), digest


def pair(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def fraction_pair(value):
    require(type(value) is list and len(value) == 2, 'bad rational pair')
    numerator, denominator = map(exact_int, value)
    require(denominator > 0, 'nonpositive rational denominator')
    return Fraction(numerator, denominator)


def dot(left, right):
    require(len(left) == len(right), 'dot dimension mismatch')
    return sum(a * b for a, b in zip(left, right))


def determinant(matrix):
    a = [row[:] for row in matrix]
    dimension = len(a)
    require(dimension > 0 and all(len(row) == dimension for row in a), 'bad determinant matrix')
    sign, previous = 1, 1
    for k in range(dimension - 1):
        pivot = next((i for i in range(k, dimension) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k + 1, dimension):
            for j in range(k + 1, dimension):
                numerator = value * a[i][j] - a[i][k] * a[k][j]
                require(numerator % previous == 0, 'nonexact Bareiss division')
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = value
    return sign * a[-1][-1]


def gram_schmidt(rows):
    stars, norms, mu = [], [], []
    for row in rows:
        vector = list(map(Fraction, row))
        coefficients = []
        for star, norm in zip(stars, norms):
            coefficient = dot(row, star) / norm
            coefficients.append(coefficient)
            vector = [x - coefficient * y for x, y in zip(vector, star)]
        norm = dot(vector, vector)
        require(norm > 0, 'singular or nonpositive GS basis')
        stars.append(vector)
        norms.append(norm)
        mu.append(coefficients)
    return stars, norms, mu


def inverse_power(value, k, modulus):
    return pow(value ** k, -1, modulus)


def mixed_residues(vector, cofactor, prime=P, orders=6):
    """Final conditions use row-specific p^k, NOT the construction modulus."""
    result = []
    for k in range(1, orders + 1):
        modulus = prime ** k
        value = sum(u * inverse_power(s, k, modulus)
                    for s, u in enumerate(vector, 1))
        if cofactor is not None:
            value += inverse_power(cofactor, k, modulus)
        result.append(value % modulus)
    return result


def solve_unit_modular(matrix, target, prime, modulus):
    """Gauss elimination in Z/p^a; every selected pivot must be a unit."""
    n = len(matrix)
    require(len(target) == n and all(len(row) == n for row in matrix), 'bad modular system')
    a = [[value % modulus for value in row] + [target[i] % modulus]
         for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k] % prime != 0), None)
        require(pivot is not None, 'modular system lacks a unit pivot')
        a[k], a[pivot] = a[pivot], a[k]
        inverse = pow(a[k][k], -1, modulus)
        a[k] = [value * inverse % modulus for value in a[k]]
        for i in range(n):
            if i == k:
                continue
            factor = a[i][k]
            a[i] = [(x - factor * y) % modulus for x, y in zip(a[i], a[k])]
    solution = [a[i][-1] for i in range(n)]
    require(all((dot(row, solution) - rhs) % modulus == 0
                for row, rhs in zip(matrix, target)), 'modular solve invariant failure')
    return solution


def floor_ceiling_preference(center):
    """Integers bracketing -center, nearer first, lower integer at ties."""
    target = -Fraction(center)
    lower = target.numerator // target.denominator
    upper = lower if target.denominator == 1 else lower + 1
    if lower == upper:
        return lower, None
    if target - lower <= upper - target:
        return lower, upper
    return upper, lower


def prime_divisors_small(value):
    divisors, candidate = [], 2
    remaining = value
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            divisors.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1
    if remaining > 1:
        divisors.append(remaining)
    return divisors


@dataclass
class CertifiedBasis:
    unweighted: list
    weighted: list
    stars: list
    norms: list
    mu: list
    bounds: dict


def load_certified_basis(certificate_path, bound_path):
    certificate, _ = read_json(certificate_path, CERT_SHA256)
    bounds, _ = read_json(bound_path, BOUND_SHA256)
    require(certificate['prime'] == P, 'wrong prime')
    require(certificate['side_budget'] == BUDGET, 'wrong budget')
    unweighted = [[exact_int(x) for x in row] for row in certificate['unweighted_basis']]
    weighted = [[exact_int(x) for x in row] for row in certificate['weighted_basis']]
    require(len(unweighted) == len(weighted) == N, 'wrong basis dimension')
    require(all(len(row) == N for row in unweighted + weighted), 'wrong row dimension')
    require(weighted == [[u * (P * s - 1) for s, u in enumerate(row, 1)]
                         for row in unweighted], 'weighted/unweighted mismatch')
    require(abs(determinant(unweighted)) == P ** 21, 'wrong mixed-kernel index')
    require(all(mixed_residues(row, None) == [0] * 6 for row in unweighted), 'basis outside mixed kernel')
    minor = [[inverse_power(s, k, P) for s in range(1, 7)] for k in range(1, 7)]
    require(determinant(minor) % P != 0, 'nonunit six-column minor')
    stars, norms, mu = gram_schmidt(weighted)
    require(norms == [fraction_pair(x) for x in certificate['gram_schmidt_squared']], 'GS norm mismatch')
    require(min(norms) == fraction_pair(certificate['minimum_gram_schmidt_squared']), 'minimum GS mismatch')
    max_R2 = 2026 ** 2 + BUDGET ** 2
    require(all(norm > max_R2 for norm in norms), 'radius below one not proved')
    require(3 * min(norms) > 4 * max_R2, 'two-nonpreferred-choice bound not proved')
    require(bounds['actual_maximal_prime17_admissible_residues'] == [1,3,4,5,7,8,9,10,11,13,15,16], 'bad domain ledger')
    require(bounds['outside_maximal_prime17_residues'] == [2,6,12,14], 'bad excluded ledger')
    return CertifiedBasis(unweighted, weighted, stars, norms, mu, bounds)


def allowed_index_sets(basis, r):
    cost = P * (P + r) - 1
    R2 = (BUDGET - cost) ** 2 + BUDGET ** 2
    singles = [(i,) for i, norm in enumerate(basis.norms) if norm <= 4 * R2]
    pairs = [indices for indices in combinations(range(N), 2)
             if sum((basis.norms[i] for i in indices), Fraction()) <= 4 * R2]
    labels = [()] + singles + pairs
    saved = basis.bounds['classes'][r - 1]
    require(saved['r'] == r and saved['R2'] == R2 and saved['atom_cost'] == cost, 'class bound mismatch')
    require([i[0] for i in singles] == saved['weighted_farther_choice_singletons'], 'singleton bound mismatch')
    require([list(indices) for indices in pairs] == saved['weighted_farther_choice_pairs'], 'pair bound mismatch')
    require(len(labels) == saved['weighted_leaf_bound'], 'path count mismatch')
    return labels, cost, R2


def particular_and_centers(basis, r):
    """Construction uses p^6; the complete coset uses the mixed p^k basis."""
    modulus = P ** 6
    matrix = [[inverse_power(s, k, modulus) for s in range(1, 7)]
              for k in range(1, 7)]
    target = [-inverse_power(P + r, k, modulus) % modulus for k in range(1, 7)]
    first = solve_unit_modular(matrix, target, P, modulus)
    particular = first + [0] * (N - 6)
    require(mixed_residues(particular, P + r) == [0] * 6, 'particular mixed residue failure')
    weighted = [u * (P * s - 1) for s, u in enumerate(particular, 1)]
    centers = [dot(weighted, star) / norm for star, norm in zip(basis.stars, basis.norms)]
    return particular, weighted, centers


def completion_metadata(vector, r, positive_mass, negative_mass):
    atom = P * (P + r)
    plus_left = BUDGET - (atom - 1) - positive_mass
    minus_left = BUDGET - negative_mass
    require(plus_left >= 0 and minus_left >= 0, 'negative survivor residual budget')
    moments = [Fraction(1 + sum(vector))]
    for k in range(1, 7):
        value = Fraction(1, atom ** k)
        value += sum((Fraction(u, (P * s) ** k) for s, u in enumerate(vector, 1)), Fraction())
        require(value.denominator % P != 0, 'uncanceled p17 pole in local survivor')
        moments.append(value)
    cuts = []
    for k, value in enumerate(moments):
        lower, upper = -Fraction(plus_left, 2 ** k), Fraction(minus_left, 2 ** k)
        cuts.append({'k': k, 'M_k': pair(value), 'necessary_lower': pair(lower),
                     'necessary_upper': pair(upper), 'passes': lower <= value <= upper})
    return {'remaining_positive_budget': plus_left, 'remaining_negative_budget': minus_left,
            'moments': [pair(value) for value in moments], 'necessary_completion_cuts': cuts,
            'completion_status': 'OPEN_AFTER_NECESSARY_CUTS' if all(cut['passes'] for cut in cuts)
                                 else 'EXCLUDED_BY_NAMED_NECESSARY_CUT',
            'local_survivor_retained': True,
            'unknown_completion_equations': 'sum_a t_a/a^k = -M_k, k=0..6, with separate residual masses and all17-free composite/integer denominators whose prime factors are at most13',
            'full_collision_or_global_T6_claim': False}


def follow_unique_path(basis, r, label, particular, weighted_particular, centers, R2):
    nonpreferred = set(label)
    coefficients = [0] * N
    spent, steps = Fraction(), []
    for i in range(N - 1, -1, -1):
        center = centers[i] + sum((coefficients[j] * basis.mu[j][i]
                                  for j in range(i + 1, N)), Fraction())
        preferred, other = floor_ceiling_preference(center)
        chosen = other if i in nonpreferred else preferred
        if chosen is None:
            return {'nonpreferred_indices': list(label), 'status': 'NO_DISTINCT_NONPREFERRED_INTEGER',
                    'stopping_index': i, 'coordinate_decisions': len(steps) + 1,
                    'partial_norm_squared': pair(spent), 'steps': steps}
        coefficients[i] = chosen
        contribution = basis.norms[i] * (center + chosen) ** 2
        require(contribution >= 0, 'negative orthogonal contribution')
        if i in nonpreferred:
            require(contribution >= basis.norms[i] / 4, 'nonpreferred cost invariant failure')
        spent += contribution
        steps.append({'i': i, 'center': pair(center), 'preferred': preferred, 'other': other,
                      'chosen': chosen, 'nonpreferred': i in nonpreferred,
                      'contribution': pair(contribution), 'partial_norm_squared': pair(spent)})
        if spent > R2:
            return {'nonpreferred_indices': list(label), 'status': 'EXACT_NORM_PRUNED',
                    'stopping_index': i, 'coordinate_decisions': len(steps),
                    'partial_norm_squared': pair(spent), 'steps': steps}
    vector = [particular[s] + sum(coefficients[i] * basis.unweighted[i][s] for i in range(N))
              for s in range(N)]
    weighted = [(P * (s + 1) - 1) * u for s, u in enumerate(vector)]
    weighted_again = [weighted_particular[s] + sum(coefficients[i] * basis.weighted[i][s]
                                                 for i in range(N)) for s in range(N)]
    require(weighted == weighted_again, 'weighted reconstruction invariant failure')
    full_norm = sum(x * x for x in weighted)
    require(Fraction(full_norm) == spent and full_norm <= R2, 'GS/full norm invariant failure')
    residues = mixed_residues(vector, P + r)
    require(residues == [0] * 6, 'final mixed congruence invariant failure')
    positive = sum(max(x, 0) for x in weighted)
    negative = sum(max(-x, 0) for x in weighted)
    positive_budget = BUDGET - (P * (P + r) - 1)
    feasible = positive <= positive_budget and negative <= BUDGET
    result = {'nonpreferred_indices': list(label),
              'status': 'LOCAL_FEASIBLE' if feasible else 'SIGNED_BUDGET_REJECTED',
              'coordinate_decisions': len(steps), 'basis_coefficients': coefficients,
              'q0_vector': vector, 'weighted_norm_squared': full_norm,
              'positive_q0_mass': positive, 'negative_q0_mass': negative,
              'positive_q0_budget': positive_budget, 'negative_q0_budget': BUDGET,
              'mixed_congruence_residues': residues, 'steps': steps}
    if feasible:
        result['completion'] = completion_metadata(vector, r, positive, negative)
    return result


def classify_one_residue(basis, r):
    cofactor = P + r
    divisors = prime_divisors_small(cofactor)
    if any(prime > P for prime in divisors):
        return {'r': r, 'cofactor': cofactor, 'prime_divisors': divisors,
                'status': 'OUTSIDE_MAXIMAL_P17_DOMAIN', 'affine_paths_evaluated': 0,
                'relaxed_class_empty_claim': False}
    labels, cost, R2 = allowed_index_sets(basis, r)
    particular, weighted_particular, centers = particular_and_centers(basis, r)
    paths = [follow_unique_path(basis, r, label, particular, weighted_particular, centers, R2)
             for label in labels]
    survivors = [path for path in paths if path['status'] == 'LOCAL_FEASIBLE']
    keys = [tuple(path['q0_vector']) for path in survivors]
    require(len(set(keys)) == len(keys), 'duplicate feasible vector/path-label invariant failure')
    return {'r': r, 'cofactor': cofactor, 'prime_divisors': divisors,
            'status': 'COMPLETE_LOCAL_FEASIBLE_VECTOR_LIST' if survivors else 'EMPTY_BY_COMPLETE_EXACT_SEARCH',
            'q1_cost': cost, 'R2': R2, 'particular_q0': particular,
            'particular_mixed_residues': mixed_residues(particular, cofactor),
            'affine_h_coordinates': [pair(value) for value in centers],
            'allowed_nonpreferred_sets': [list(label) for label in labels],
            'affine_paths_evaluated': len(paths),
            'coordinate_decisions': sum(path['coordinate_decisions'] for path in paths),
            'paths': paths, 'local_survivor_count': len(survivors),
            'full_collision_or_global_T6_claim': False}


def validate_control_context(path):
    context, digest = read_json(path)
    require(context.get('task_id') == TASK_ID, 'wrong actual child Task context')
    for field in ['publication_id', 'claim_id', 'execution_record_id', 'run_id', 'researcher_id']:
        require(type(context.get(field)) is str and bool(context[field]), 'missing actual context field: ' + field)
    require(context.get('root_verified_current_native_authorization') is True,
            'Root must verify actual current publication/claim/run before execution')
    require(context.get('execution_authorized') is True, 'execution context is not authorized')
    evidence = context.get('receipt_evidence')
    require(type(evidence) is list and len(evidence) >= 3,
            'publication, claim and run receipt evidence is required')
    public_evidence = []
    for item in evidence:
        require(type(item) is dict, 'receipt evidence must be a file/hash descriptor')
        require(item.get('kind') in ['TASK_PUBLICATION', 'CLAIM', 'RUN'], 'unknown receipt evidence kind')
        require(type(item.get('path')) is str and type(item.get('sha256')) is str,
                'receipt evidence requires an exact local path and SHA256')
        raw = Path(item['path']).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == item['sha256'], 'actual receipt file/hash mismatch')
        public_evidence.append({key: item[key] for key in ['kind', 'path', 'sha256']})
    require({item['kind'] for item in public_evidence} == {'TASK_PUBLICATION', 'CLAIM', 'RUN'},
            'all three actual native receipt kinds are required')
    # Do not serialize arbitrary extra context fields or private capabilities.
    public_context = {field: context[field] for field in
                      ['task_id', 'publication_id', 'claim_id', 'execution_record_id',
                       'run_id', 'researcher_id', 'root_verified_current_native_authorization',
                       'execution_authorized']}
    public_context['receipt_evidence'] = public_evidence
    return public_context, digest


def run_authorized(certificate_path, bound_path, context_path):
    context, context_digest = validate_control_context(context_path)
    started = time.monotonic()
    basis = load_certified_basis(certificate_path, bound_path)
    rows = [classify_one_residue(basis, r) for r in range(1, 17)]
    require([row['r'] for row in rows if row['status'] == 'OUTSIDE_MAXIMAL_P17_DOMAIN'] == [2,6,12,14],
            'wrong domain classification')
    path_count = sum(row['affine_paths_evaluated'] for row in rows)
    decisions = sum(row.get('coordinate_decisions', 0) for row in rows)
    require(path_count == 299 and decisions <= 4784, 'precommitted resource bound exceeded')
    return {'schema': 'T6_P17_ORDER1_EXACT_SIXTEEN_ROW_CLASSIFICATION_V1',
            'status': 'COMPLETE_DOMAIN_AND_AFFINE_CLASSIFICATION',
            'task_execution_context': context, 'control_context_sha256': context_digest,
            'context_authentication_boundary': 'Actual native authorization checked externally by Root; this local file is recorded provenance, not authority.',
            'certificate_sha256': CERT_SHA256, 'branch_bound_sha256': BOUND_SHA256,
            'executor_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds': time.monotonic() - started,
            'rows': rows, 'affine_paths_evaluated': path_count, 'coordinate_decisions': decisions,
            'local_survivor_count': sum(row.get('local_survivor_count', 0) for row in rows),
            'p17_higher_orders_claim': False, 'global_T6_completion_claim': False,
            'p19_campaign_replayed': False, 'author_checkers_imported_or_executed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, default=HERE/'inputs/p17_q0_certificate.json')
    parser.add_argument('--branch-bounds', type=Path, default=HERE/'inputs/P17_ORDER1_BRANCH_BOUND_RESULTS.json')
    parser.add_argument('--execute-order1', action='store_true')
    parser.add_argument('--actual-control-context', type=Path)
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    if not arguments.execute_order1:
        print(json.dumps({'status': 'PREPARATION_ONLY_NO_AFFINE_CENSUS',
                          'task_id_proposed_not_authority': TASK_ID,
                          'certificate_sha256': CERT_SHA256, 'branch_bound_sha256': BOUND_SHA256,
                          'requires_actual_publication_claim_run': True}))
        return
    require(arguments.actual_control_context is not None and arguments.output is not None,
            'actual control context and explicit new output path are required')
    require(not arguments.output.exists(), 'refuse to overwrite existing execution evidence')
    result = run_authorized(arguments.certificate, arguments.branch_bounds, arguments.actual_control_context)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    with arguments.output.open('x') as destination:
        json.dump(result, destination, indent=2)
        destination.write('\n')
    print(json.dumps({'status': result['status'], 'output': str(arguments.output),
                      'affine_paths_evaluated': result['affine_paths_evaluated'],
                      'local_survivor_count': result['local_survivor_count'],
                      'global_T6_completion_claim': False}))


if __name__ == '__main__':
    main()
