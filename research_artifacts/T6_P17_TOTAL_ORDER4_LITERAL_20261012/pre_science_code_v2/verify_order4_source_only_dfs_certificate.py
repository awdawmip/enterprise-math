#!/usr/bin/env python3
"""Source-only full T6Q4DFS1 saved-proof verifier; default NOT_ADMITTED.

No producer import, search, census, native control, or remote operation.
Exact arithmetic functions below are transparently reused from separately built
Source q3 consumer ae2fad40...; new q4 input/wire/representative/tree adapter is
UNKNOWN native author, directed/shared-owner/nonblind construction, not native
independent review. Root FBF and Driver4CF input/codec authorship is preserved.
"""
import argparse
import base64
import hashlib
import json
import struct
from fractions import Fraction
from itertools import combinations_with_replacement, product
from pathlib import Path

PORTABLE_SHA = '7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce'
INPUT_SHA = '62dc2e5b6a3fceb129c25a0c19fc27dbe6ac195c6cdedecde7cfb1639789e16a'
SIDE_BUDGET = 2331
PRIME, DIMENSION, DEGREE, CASE_COUNT = 17, 16, 6, 30992
LOWER, MODULUS, HALF_MODULUS = 16901460, 24137569, 12068784
MAGIC = b'T6Q4DFS1'
HEADER_BYTES, MAX_PROOF_BYTES = 76, 1881352
INHERITED_EIGHT = ['EM-DIRECT-49ADE6','EM-DIRECT-E1F2B6','EM-DIRECT-FA0C27',
                  'EM-DVR-4C90FB','EM-DVR-C1A1D9','EM-DVR-FBF223',
                  'EM-T6-B4F89F','EM-DVR-4CF7AF']
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


def byte_pin(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}


def canonical_partitions(total, minimum=1):
    """Ascending partitions; descriptors only, never feasibility traversal."""
    if total == 0:
        yield ()
    for q in range(minimum, total + 1):
        for tail in canonical_partitions(total - q, q):
            yield (q,) + tail


def canonical_order4_descriptors():
    """Independent multiplicity/sign loops matching the frozen ordered input."""
    position = 0
    for partition in canonical_partitions(4):
        distinct_q = sorted(set(partition))
        multiset_options = [combinations_with_replacement(range(1, 17), partition.count(q))
                            for q in distinct_q]
        for residue_groups in product(*multiset_options):
            atoms = [(q, r) for q, residues in zip(distinct_q, residue_groups) for r in residues]
            support = sorted(set(atoms))
            for sign_tail in product((1, -1), repeat=len(support) - 1):
                signs = dict(zip(support, (1,) + sign_tail))
                plus = [atom for atom in atoms if signs[atom] == 1]
                minus = [atom for atom in atoms if signs[atom] == -1]
                yield position, 'q4-literal-' + format(position + 1, '05d'), partition, plus, minus
                position += 1


def json_atoms(value):
    require(type(value) is list, 'Atom side must be a list')
    result = []
    for pair in value:
        require(type(pair) is list and len(pair) == 2 and all(type(v) is int for v in pair),
                'Pinned q4 atoms require two JSON integers')
        q, r = pair
        require(1 <= q <= 4 and 1 <= r <= 16, 'Atom outside literal totalorder4 domain')
        result.append((q, r))
    return result


def derive_inputs(prospective, portable_raw):
    """Validate static descriptors, budgets and reciprocal targets only on --verify."""
    require(prospective['schema'] == 'T6_P17_TOTAL_ORDER4_LITERAL_FULL30992_FIXED_INPUT_V1',
            'Unknown q4 input schema')
    require(prospective['scientific_feasibility_executed'] is False and
            prospective['classifier_result_asserted'] is False, 'Static input asserts feasibility')
    scope = prospective['scope']
    require(scope['literal_descriptor_count'] == CASE_COUNT and
            scope['maximal_p17_admissible_count'] == 10212 and scope['outside_domain_count'] == 20780 and
            scope['total_vertical_order'] == 4 and scope['overall_sign_quotient'] is True and
            scope['all_literal_outside_systems_require_classification'] is True, 'Input scope changed')
    order = prospective['case_order']
    require(order['index_base'] == 0 and order['partition_sequence'] == [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]],
            'Canonical partition sequence changed')
    fixed = prospective['fixed_rule']
    weights = [17 * j - 1 for j in range(1, 17)]
    moduli = [17 ** k for k in range(1, 7)]
    require(fixed['prime'] == 17 and fixed['auxiliary_dimension'] == 16 and fixed['mixed_degree'] == 6 and
            fixed['side_exponent_mass_limits'] == [SIDE_BUDGET, SIDE_BUDGET] and
            fixed['q0_weights'] == weights and list(map(integer, fixed['mixed_moduli'])) == moduli,
            'Input fixed rule mismatch')
    reference = prospective['common_input']
    require(reference['repository'] == 'awdawmip/enterprise-math' and
            reference['source_commit'] == '953db05d78bd0f175a99d0406f850691d479ae26' and
            reference['path'] == 'research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/portable_input.json' and
            {k: reference[k] for k in ('bytes', 'sha256', 'git_blob_sha1')} == byte_pin(portable_raw),
            'Pinned common Source bytes mismatch')
    contribution = prospective['construction_contributions']
    require(contribution['root_direction_static_scope_and_canonical_codec'] == 'EM-DVR-FBF223' and
            contribution['driver_Task_input_interface_preparation'] == 'EM-DVR-4CF7AF' and
            contribution['helper_native_identity'] == 'UNKNOWN' and contribution['directed_nonblind'] is True and
            contribution['prior_scientific_contributor_ids'] == INHERITED_EIGHT and
            contribution['self_construction_checks_are_not_decisive_mathematical_review'] is True and
            contribution['subsequent_result_requires_genuine_separate_nonauthor_review'] is True,
            'Input authorship/exposure changed')
    atom_rows = []
    for q in range(1, 5):
        for r in range(1, 17):
            cofactor = 17 * q + r
            atom_rows.append({'q': q, 'r': r, 'cofactor': cofactor, 'denominator': 17 * cofactor,
                              'exponent_mass': 17 * cofactor - 1,
                              'prime_factors': repeated_prime_factors(cofactor),
                              'reciprocal_moments': [str(pow(cofactor, -k, 17 ** k)) for k in range(1, 7)]})
    require(prospective['atom_data'] == atom_rows, 'All64 atom arithmetic/factorizations mismatch')
    rows = prospective['cases']
    require(type(rows) is list and len(rows) == CASE_COUNT, 'Full30992 input required')
    derived, seen, quarter, admissible, ceilings, costs = [], set(), 0, 0, 0, []
    for position, name, partition, plus, minus in canonical_order4_descriptors():
        require(position < CASE_COUNT, 'Independent descriptors exceed30992')
        row = rows[position]
        require(type(row['case_index']) is int and row['case_index'] == position and
                row['case_id'] == name and name not in seen and row['order_partition'] == list(partition),
                'Ordered input case identity/partition mismatch at' + str(position))
        seen.add(name)
        require(json_atoms(row['positive_atoms']) == plus and json_atoms(row['negative_atoms']) == minus and
                sum(q for q, _ in plus + minus) == 4 and not (set(plus) & set(minus)),
                'Multiplicity/primitive/sign normalization mismatch at' + name)
        positive_mass = sum(17 * (17 * q + r) - 1 for q, r in plus)
        negative_mass = sum(17 * (17 * q + r) - 1 for q, r in minus)
        positive_budget, negative_budget = SIDE_BUDGET - positive_mass, SIDE_BUDGET - negative_mass
        require(min(positive_budget, negative_budget) >= 0, 'Negative signed residual budget')
        radius = positive_budget ** 2 + negative_budget ** 2
        targets = [(sum(pow(17 * q + r, -k, 17 ** k) for q, r in minus) -
                    sum(pow(17 * q + r, -k, 17 ** k) for q, r in plus)) % (17 ** k) for k in range(1, 7)]
        largest = max([17] + [largest_prime_factor(17 * q + r) for q, r in plus + minus])
        maximal = largest == 17
        is_quarter = 4 * radius < LOWER
        require(is_quarter or 2 * radius < LOWER, 'Ordinary strict2R2 bound fails')
        ceiling = 32 if is_quarter else 272
        require(list(map(integer, row['fixed_vertical_side_costs'])) == [positive_mass, negative_mass] and
                list(map(integer, row['q0_side_budgets'])) == [positive_budget, negative_budget] and
                integer(row['radius_squared']) == radius and list(map(integer, row['mixed_rhs'])) == targets and
                row['maximal_p17_domain'] == ('ADMISSIBLE' if maximal else 'OUTSIDE_DOMAIN') and
                row['strict_conservative_quarter_mask'] is is_quarter and
                type(row['conditional_coordinate_choice_ceiling']) is int and
                row['conditional_coordinate_choice_ceiling'] == ceiling,
                'Derived targets/budgets/domain/mask mismatch at' + name)
        derived.append({'pattern_id': name, 'case_index': position,
                        'positive_atoms': [[str(q), str(r)] for q, r in plus],
                        'negative_atoms': [[str(q), str(r)] for q, r in minus],
                        'positive_fixed_mass': positive_mass, 'negative_fixed_mass': negative_mass,
                        'positive_budget': positive_budget, 'negative_budget': negative_budget,
                        'radius_squared': radius, 'targets': targets,
                        'largest_vertical_prime': largest, 'maximal_p17_admissible': maximal,
                        'quarter': is_quarter, 'action_bound': ceiling})
        quarter += is_quarter; admissible += maximal; ceilings += ceiling
        costs.append(positive_mass + negative_mass)
    require(len(derived) == CASE_COUNT and admissible == 10212 and quarter == 4724 and ceilings == 7296064,
            'Independent30992 domain/mask/choice scope mismatch')
    static = prospective['static_arithmetic']
    require(static['quarter_mask_count'] == quarter and static['ordinary_mask_count'] == CASE_COUNT - quarter and
            static['conditional_full_family_coordinate_choice_ceiling'] == ceilings and
            integer(static['conservative_GS_lower']) == LOWER and
            integer(static['min_radius_squared']) == min(d['radius_squared'] for d in derived) and
            integer(static['max_radius_squared']) == max(d['radius_squared'] for d in derived) and
            list(map(integer, static['total_fixed_cost_range'])) == [min(costs), max(costs)],
            'Input static arithmetic summary mismatch')
    return derived, {'weights': list(map(str, weights)), 'moduli': list(map(str, moduli)),
                     'coefficients': [[str(pow(j, -k, 17 ** k)) for j in range(1, 17)] for k in range(1, 7)]}


def inverse_mod_unit_matrix(matrix, modulus):
    """Independently invert via unit-pivot modular row elimination."""
    n = len(matrix)
    require(n == 6 and all(len(row) == n for row in matrix), 'Canonical A dimension mismatch')
    work = [[x % modulus for x in row] + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if work[i][col] % 17), None)
        require(pivot is not None, 'Canonical A lacks unit pivot')
        work[col], work[pivot] = work[pivot], work[col]
        unit = pow(work[col][col], -1, modulus)
        work[col] = [(v * unit) % modulus for v in work[col]]
        for i in range(n):
            if i != col:
                factor = work[i][col]
                work[i] = [(a - factor * b) % modulus for a, b in zip(work[i], work[col])]
    inverse = [row[n:] for row in work]
    for left, right in ((matrix, inverse), (inverse, matrix)):
        require(all(sum(left[i][k] * right[k][j] for k in range(n)) % modulus == int(i == j)
                    for i in range(n) for j in range(n)), 'Canonical A inverse identity fails')
    return inverse


def prepare_common(portable, problem):
    # Exact reused core: requesting max_radius=LOWER/2 proves D_i>LOWER.
    common = common_basis(portable, problem, LOWER // 2)
    weights, coefficients, moduli, rows, weighted, mu, squared, orthogonal = common
    require(min(squared) > LOWER, 'Exact Dmin conservative lower bound fails')
    for i in range(16):
        for j in range(16):
            require(dot(weighted[i], weighted[j]) == sum(mu[i][k] * mu[j][k] * squared[k] for k in range(16)),
                    'Full triangular Gram factorization fails')
            if i != j:
                require(dot(orthogonal[i], orthogonal[j]) == 0, 'GS orthogonality fails')
    # These precise modulo17^k least-nonnegative entry lifts are part of T6Q4DFS1.
    matrix = [[pow(j, -k, 17 ** k) for j in range(1, 7)] for k in range(1, 7)]
    inverse = inverse_mod_unit_matrix(matrix, MODULUS)
    return common, matrix, inverse


def canonical_particular(targets, matrix, inverse, coefficients, moduli):
    require(len(targets) == 6 and all(type(t) is int and 0 <= t < m for t, m in zip(targets, moduli)),
            'Canonical target lifts are not least nonnegative mixed residues')
    y = [sum(a * t for a, t in zip(row, targets)) % MODULUS for row in inverse]
    require(all(sum(a * b for a, b in zip(row, y)) % MODULUS == t for row, t in zip(matrix, targets)),
            'Canonical A*y target identity fails')
    particular = [((v + HALF_MODULUS) % MODULUS) - HALF_MODULUS for v in y] + [0] * 10
    require(all(sum(a * b for a, b in zip(row, particular)) % m == t
                for row, m, t in zip(coefficients, moduli, targets)), 'Canonical particular mixed congruence fails')
    return particular


def encode_uleb(value):
    require(type(value) is int and value >= 0, 'ULEB value invalid')
    result = bytearray()
    while True:
        low = value & 127
        value >>= 7
        result.append(low | (128 if value else 0))
        if not value:
            return bytes(result)


class CaseActions:
    def __init__(self, count, packed):
        self.count, self.packed, self.position = count, packed, 0

    def take(self):
        require(self.position < self.count, 'Missing complete child/candidate action')
        action = (self.packed[self.position // 4] >> (2 * (self.position % 4))) & 3
        self.position += 1
        return action

    def finish(self):
        require(self.position == self.count, 'Unconsumed/duplicate/trailing actions inside case')


class WireReader:
    def __init__(self, raw, common_sha, input_sha, case_count):
        require(type(raw) is bytes and len(raw) <= MAX_PROOF_BYTES, 'Proof binary size exceeds conditional fullfamily ceiling')
        require(len(raw) >= HEADER_BYTES and raw[:8] == MAGIC, 'Bad or incomplete T6Q4DFS1 header')
        require(raw[8:40] == bytes.fromhex(common_sha) and raw[40:72] == bytes.fromhex(input_sha),
                'Wire common/input full-byte SHA header mismatch')
        require(struct.unpack('<I', raw[72:76])[0] == case_count, 'Wrong complete case count/header variant')
        self.raw, self.offset, self.case_count, self.records = raw, HEADER_BYTES, case_count, 0

    def next_case(self, bound):
        require(self.records < self.case_count, 'Duplicate/excess case record')
        start, value, shift = self.offset, 0, 0
        while True:
            require(self.offset < len(self.raw), 'Unfinished/missing case ULEB record')
            require(self.offset - start < 2, 'Overlong/excessive ULEB action count')
            byte = self.raw[self.offset]; self.offset += 1
            value |= (byte & 127) << shift
            if not byte & 128:
                break
            shift += 7
        require(self.raw[start:self.offset] == encode_uleb(value), 'Noncanonical overlong ULEB')
        require(2 <= value <= bound and value % 2 == 0, 'Action count outside independently proved mask bound')
        length = (value + 3) // 4
        require(self.offset + length <= len(self.raw), 'Unfinished packed case action record')
        packed = self.raw[self.offset:self.offset + length]; self.offset += length
        used = value % 4
        require(not used or packed[-1] >> (2 * used) == 0, 'Nonzero tail padding bits')
        self.records += 1
        return CaseActions(value, packed)

    def finish(self):
        require(self.records == self.case_count and self.offset == len(self.raw),
                'Missing/duplicate records or trailing bytes; partial prefix is not fullproof')


def consume_saved_case(common, matrix, inverse, derived, actions, progress):
    """Consume saved actions only; every child exists solely because its next symbol is C."""
    weights, coefficients, moduli, rows, weighted, mu, squared, orthogonal = common
    radius = derived['radius_squared']
    require(all(d > (4 if derived['quarter'] else 2) * radius for d in squared),
            'Per-case strict quarter/ordinary GS bound fails')
    particular = canonical_particular(derived['targets'], matrix, inverse, coefficients, moduli)
    weighted_particular = [a * w for a, w in zip(particular, weights)]
    base_centers = [dot(weighted_particular, star) / d for star, d in zip(orthogonal, squared)]
    choices = [0] * 16
    statistics = {'nodes': 0, 'actions': 0, 'N': 0, 'C': 0, 'B': 0, 'S': 0, 'full_leaves': 0}
    witnesses = []

    def visit(i, partial_norm):
        statistics['nodes'] += 1
        center = base_centers[i] + sum(choices[j] * mu[j][i] for j in range(i + 1, 16))
        floor = center.numerator // center.denominator
        for z in (-floor - 1, -floor):
            choices[i] = z
            norm = partial_norm + squared[i] * (z + center) ** 2
            action = actions.take(); statistics['actions'] += 1
            if norm > radius:
                require(action == 0, 'False N/C/B/S: strict exact sphere prune required')
                statistics['N'] += 1
                continue
            if i > 0:
                require(action == 1, 'False action/missing live internal child')
                statistics['C'] += 1
                visit(i - 1, norm)
                continue
            statistics['full_leaves'] += 1
            vector = [particular[c] + sum(choices[j] * rows[j][c] for j in range(16)) for c in range(16)]
            require(sum((w * v) ** 2 for w, v in zip(weights, vector)) == norm, 'Leaf weighted norm/GS identity fails')
            residues = [sum(a * v for a, v in zip(row, vector)) % m for row, m in zip(coefficients, moduli)]
            require(residues == derived['targets'], 'Leaf six original mixed congruences fail')
            positive = sum(w * max(v, 0) for w, v in zip(weights, vector))
            negative = sum(w * max(-v, 0) for w, v in zip(weights, vector))
            budget_pass = positive <= derived['positive_budget'] and negative <= derived['negative_budget']
            require(action == (3 if budget_pass else 2), 'False B/S signed budget action; equality must survive')
            statistics['S' if budget_pass else 'B'] += 1
            if budget_pass:
                witness = {'pattern_id': derived['pattern_id'], 'case_index': derived['case_index'],
                           'q0_vector': list(map(str, vector)), 'basis_coordinates': list(map(str, choices)),
                           'positive_mass': str(positive), 'negative_mass': str(negative),
                           'positive_budget': str(derived['positive_budget']), 'negative_budget': str(derived['negative_budget']),
                           'mixed_residues': list(map(str, residues)), 'weighted_norm': str(norm.numerator),
                           'maximal_p17_admissible': derived['maximal_p17_admissible'],
                           'literal_relaxed_LOCAL_KERNEL_even_if_outside_domain': True,
                           'completion': completion_from_saved_vector(derived, vector, positive, negative),
                           'H0_lower_prime_completion_status': 'OPEN_NOT_DECIDED_BY_LOCAL_KERNEL',
                           'global_collision_or_T6_complete': False}
                witnesses.append(witness)
                if progress.get('first_verified_local_witness') is None:
                    progress['first_verified_local_witness'] = witness
        choices[i] = 0

    visit(15, Fraction(0))
    actions.finish()
    require(statistics['actions'] == actions.count and statistics['actions'] <= derived['action_bound'],
            'Complete action count/bound mismatch')
    return {'case_index': derived['case_index'], 'pattern_id': derived['pattern_id'],
            'classification': 'LOCAL_KERNEL' if witnesses else 'EMPTY',
            'maximal_p17_admissible': derived['maximal_p17_admissible'], 'quarter': derived['quarter'],
            'complete_saved_tree': True, 'statistics': statistics, 'witnesses': witnesses}


def safe_member_path(value):
    require(type(value) is str and value and '\\' not in value and not value.startswith('/'), 'Unsafe Source member path')
    parts = value.split('/')
    require(all(part not in ('', '.', '..') for part in parts), 'Unsafe Source member path component')
    return value


def canonical_base64(value):
    require(type(value) is str and value.isascii(), 'Source chunk base64 must be ASCII')
    require(not any(c.isspace() for c in value), 'Source chunk base64 must be canonical without whitespace')
    raw = base64.b64decode(value, validate=True)
    require(base64.b64encode(raw).decode('ascii') == value, 'Noncanonical Source chunk base64 padding')
    return raw


def load_saved_proof(proof_path, manifest_path, expected_sha=None):
    """Read binary or explicit complete manifest/carriers; never open local verbose cases."""
    if proof_path:
        raw = Path(proof_path).read_bytes()
        evidence = {'encoding': 'raw-T6Q4DFS1-binary', 'path': str(proof_path), 'pin': byte_pin(raw)}
    else:
        manifest_raw, manifest = read_json(manifest_path)
        manifest_fields = {'schema', 'proof_encoding', 'scope_status', 'raw_bytes', 'raw_sha256',
                           'raw_git_blob_sha1', 'compression', 'encoded_bytes', 'encoded_sha256',
                           'base64_characters', 'part_count', 'parts', 'common_sha256', 'ordered_input_sha256', 'case_count'}
        require(set(manifest) == manifest_fields and
                manifest['schema'] == 'T6_Q4_BINARY_PROOF_LOSSLESS_SOURCE_MANIFEST_V1' and
                manifest['proof_encoding'] == 'T6Q4DFS1' and manifest['scope_status'] == 'UNVERIFIED_BY_BYTE_PACKER' and
                manifest['compression'] == 'none', 'Unknown Source proof manifest/encoding; byte codec is not math acceptance')
        require(type(manifest['raw_bytes']) is int and HEADER_BYTES <= manifest['raw_bytes'] <= MAX_PROOF_BYTES,
                'Invalid whole Source binary byte count')
        require(type(manifest['encoded_bytes']) is int and manifest['encoded_bytes'] == manifest['raw_bytes'] and
                manifest['encoded_sha256'] == manifest['raw_sha256'], 'Unsupported compression/encoded byte substitution')
        require(manifest['common_sha256'] == PORTABLE_SHA and manifest['ordered_input_sha256'] == INPUT_SHA and
                type(manifest['case_count']) is int and manifest['case_count'] == CASE_COUNT, 'Source manifest input/count pins mismatch')
        expected_characters = 4 * ((manifest['raw_bytes'] + 2) // 3)
        require(type(manifest['base64_characters']) is int and manifest['base64_characters'] == expected_characters and
                expected_characters <= 2508472, 'Whole Source base64 length ceiling mismatch')
        rows = manifest['parts']
        expected_parts = (expected_characters + 899999) // 900000
        require(type(rows) is list and type(manifest['part_count']) is int and
                len(rows) == manifest['part_count'] == expected_parts <= 3, 'Invalid complete Source part inventory')
        seen, pieces, offset, carrier_pins = set(), [], 0, []
        base = Path(manifest_path).resolve().parent
        for idx, row in enumerate(rows):
            require(set(row) == {'path', 'bytes', 'sha256', 'git_blob_sha1', 'base64_offset', 'base64_characters'} and
                    type(row['base64_offset']) is int and row['base64_offset'] == offset,
                    'Source part order/offset gap or overlap')
            relative = safe_member_path(row['path'])
            require(relative not in seen and relative != Path(manifest_path).name, 'Duplicate/self-referential Source chunk')
            seen.add(relative)
            path = base / relative
            require(not path.is_symlink() and path.resolve().is_relative_to(base), 'Source chunk escapes manifest directory')
            carrier_raw, carrier = read_json(path)
            require(set(carrier) == {'schema', 'part_index', 'part_count', 'raw_sha256', 'payload_base64'} and
                    carrier['schema'] == 'T6_Q4_BINARY_PROOF_LOSSLESS_SOURCE_PART_V1' and
                    type(carrier['part_index']) is int and carrier['part_index'] == idx and
                    type(carrier['part_count']) is int and carrier['part_count'] == len(rows) and
                    carrier['raw_sha256'] == manifest['raw_sha256'],
                    'Source carrier schema/index/offset mismatch')
            require(len(carrier_raw) < 1048576 and byte_pin(carrier_raw) == {k: row[k] for k in ('bytes', 'sha256', 'git_blob_sha1')},
                    'Source chunk carrier full-byte/SHA/Gitblob mismatch')
            payload = carrier['payload_base64']
            require(type(payload) is str and payload.isascii() and
                    type(row['base64_characters']) is int and
                    len(payload) == row['base64_characters'] == min(900000, expected_characters - offset),
                    'Source part base64 character count/chunk bound mismatch')
            require(not any(c.isspace() for c in payload), 'Source part base64 whitespace forbidden')
            pieces.append(payload); offset += len(payload)
            require(offset <= expected_characters, 'Source part total exceeds whole encoded proof')
            carrier_pins.append({'path': relative, 'carrier': byte_pin(carrier_raw),
                                 'base64_offset': row['base64_offset'], 'base64_characters': len(payload)})
        require(offset == expected_characters, 'Incomplete whole Source base64 inventory')
        raw = canonical_base64(''.join(pieces))
        require(len(raw) == manifest['raw_bytes'] and hashlib.sha256(raw).hexdigest() == manifest['raw_sha256'] and
                byte_pin(raw)['git_blob_sha1'] == manifest['raw_git_blob_sha1'], 'Whole Source binary reassembly mismatch')
        evidence = {'encoding': 'T6Q4DFS1/none/base64', 'manifest_path': str(manifest_path),
                    'manifest_pin': byte_pin(manifest_raw), 'part_count': len(rows), 'parts': carrier_pins,
                    'whole_binary_pin': byte_pin(raw), 'byte_packer_scope_not_mathematical_acceptance': True}
    require(len(raw) <= MAX_PROOF_BYTES, 'Whole proof size exceeds conditional wire ceiling')
    if expected_sha:
        require(hashlib.sha256(raw).hexdigest() == expected_sha, 'External expected complete proof SHA mismatch')
    return raw, evidence


def observed_context(context_path, input_raw, proof_raw):
    if not context_path:
        return {'provided': False, 'native_authorization_or_acceptance_created_by_verifier': False}
    raw, context = read_json(context_path)
    require(type(context) is dict, 'Context metadata must be an object')
    if 'total_vertical_order' in context:
        require(type(context['total_vertical_order']) is int and context['total_vertical_order'] == 4, 'Context totalorder mismatch')
    if 'global_goal_status' in context:
        require(context['global_goal_status'] == 'OPEN', 'Context global Goal must remain OPEN')
    for key in ('prior_q2_scientific_replayed', 'prior_q3_scientific_replayed', 'global_T6_complete', 'native_mathematical_acceptance_granted'):
        if key in context:
            require(context[key] is False, 'Context asserts forbidden replay/global or native acceptance: ' + key)
    if 'order4_input_descriptor' in context:
        descriptor = context['order4_input_descriptor']
        require(descriptor['bytes'] == len(input_raw) and descriptor['sha256'] == hashlib.sha256(input_raw).hexdigest(),
                'Observed context q4 input byte pin mismatch')
    if 'proof_sha256' in context:
        require(context['proof_sha256'] == hashlib.sha256(proof_raw).hexdigest(), 'Observed context complete proof SHA mismatch')
    return {'provided': True, 'context_pin': byte_pin(raw),
            'observed_binding_fields': {k: context[k] for k in ('task_id', 'publication_id', 'researcher_id', 'session_id',
                                                               'claim_id', 'execution_record_id', 'run_id', 'run_generation') if k in context},
            'context_is_metadata_only_not_authenticated_by_mathematical_verifier': True,
            'native_authorization_or_acceptance_created_by_verifier': False}


def verify_full_saved_proof(portable_raw, portable, input_raw, prospective, proof_raw, context_observation, proof_evidence, progress):
    require(byte_pin(portable_raw)['sha256'] == PORTABLE_SHA and len(portable_raw) == 32208, 'Exact common input bytes differ')
    require(byte_pin(input_raw)['sha256'] == INPUT_SHA and len(input_raw) == 13084243, 'Exact full ordered q4 input bytes differ')
    wire = WireReader(proof_raw, PORTABLE_SHA, INPUT_SHA, CASE_COUNT)
    derived, problem = derive_inputs(prospective, portable_raw)
    common, matrix, inverse = prepare_common(portable, problem)
    totals = {'nodes': 0, 'actions': 0, 'N': 0, 'C': 0, 'B': 0, 'S': 0, 'full_leaves': 0}
    classifications = {'EMPTY': 0, 'LOCAL_KERNEL': 0}
    summaries = []
    for row in derived:
        progress['currently_consuming_case_index'] = row['case_index']
        actions = wire.next_case(row['action_bound'])
        summary = consume_saved_case(common, matrix, inverse, row, actions, progress)
        for key in totals:
            totals[key] += summary['statistics'][key]
        classifications[summary['classification']] += 1
        summaries.append(summary)
        progress['complete_case_prefix_count'] = len(summaries)
    wire.finish()
    require(totals['actions'] <= 7296064 and totals['actions'] == 2 * totals['nodes'], 'Full conditional action ceiling/node relation fails')
    return {'schema': 'T6_Q4_FULL_SOURCE_ONLY_EXACT_SAVED_DFS_VERIFICATION_REPORT_V1',
            'status': 'COMPLETE_T6Q4DFS1_LITERAL_CLASSIFICATION_PASS',
            'all30992_saved_case_trees_complete': True, 'case_count': CASE_COUNT,
            'admissible_count': 10212, 'outside_literal_relaxed_count': 20780,
            'quarter_count': 4724, 'ordinary_count': 26268,
            'classification_counts': classifications, 'totals': totals,
            'case_summaries': summaries,
            'common_math': {'full_mixed_kernel_index': str(17 ** 21), 'dimension': 16,
                            'GS_min_squared': [str(min(common[6]).numerator), str(min(common[6]).denominator)],
                            'strict_GS_conservative_lower': str(LOWER),
                            'canonical_A_entry_lifts_and_both_inverse_identities_checked': True,
                            'all_per_case_target_budget_domain_and_strict_mask_preconditions_checked': True},
            'input_pins': {'portable': byte_pin(portable_raw), 'order4_input': byte_pin(input_raw), 'whole_proof': byte_pin(proof_raw)},
            'Source_proof_evidence': proof_evidence, 'observed_optional_context': context_observation,
            'first_verified_local_witness': progress.get('first_verified_local_witness'),
            'native_helper_identity': 'UNKNOWN', 'directed_shared_owner_nonblind_construction': True,
            'inherited_eight_known_native_authors': INHERITED_EIGHT,
            'Root_direction_static_and_canonical_codec_author': 'EM-DVR-FBF223',
            'Driver_input_and_Task_interface_author': 'EM-DVR-4CF7AF',
            'arithmetic_core_reuse_source_consumer_sha256': 'ae2fad40e958984a256e79e7d137287b9a0b18b2c8b606d0ad932435ea4206f8',
            'consumer_is_new_construction_author_not_F9_native_reviewer': True,
            'genuine_separate_nonauthor_result_review_required': True,
            'scientific_search_or_producer_executed': False, 'lower_order_proof_replayed': False,
            'native_or_remote_Source_operation': False, 'native_mathematical_acceptance_created': False,
            'global_T6_complete': False, 'global_goal_status': 'OPEN',
            'H0_lower_prime_completion_decided': False}


def synthetic_wire_self_test():
    """Wire only: no portable/input loads, matrices, GS, representatives, or real cases."""
    sha1, sha2 = '11' * 32, '22' * 32
    header = MAGIC + bytes.fromhex(sha1) + bytes.fromhex(sha2) + struct.pack('<I', 1)
    valid = header + encode_uleb(6) + bytes((0xE4, 0x04))  # N,C,B,S,N,C; two zero tail pairs.
    wire = WireReader(valid, sha1, sha2, 1)
    actions = wire.next_case(32)
    require([actions.take() for _ in range(6)] == [0, 1, 2, 3, 0, 1], 'LSB-first four-symbol decode failed')
    actions.finish(); wire.finish()
    rejected = []

    def must_reject(name, run):
        try:
            run()
        except (ValueError, KeyError, TypeError):
            rejected.append(name)
        else:
            raise ValueError('Synthetic invalid wire unexpectedly accepted: ' + name)

    def parse_complete(raw, bound=32):
        reader = WireReader(raw, sha1, sha2, 1)
        current = reader.next_case(bound)
        for _ in range(current.count):
            current.take()
        current.finish(); reader.finish()

    must_reject('bad_magic', lambda: parse_complete(b'BADMAGIC' + valid[8:]))
    must_reject('wrong_common_hash', lambda: parse_complete(valid[:8] + bytes(32) + valid[40:]))
    must_reject('wrong_input_hash', lambda: parse_complete(valid[:40] + bytes(32) + valid[72:]))
    must_reject('wrong_uint32_count', lambda: parse_complete(valid[:72] + struct.pack('<I', 2) + valid[76:]))
    must_reject('alternate_dimension_header', lambda: parse_complete(valid[:72] + bytes((16, 1)) + valid[76:]))
    must_reject('overlong_uleb', lambda: parse_complete(header + bytes((0x86, 0x00, 0xE4, 0x04))))
    must_reject('excessive_uleb', lambda: parse_complete(header + bytes((0x80, 0x80, 0x01))))
    must_reject('quarter_count_bound', lambda: parse_complete(header + encode_uleb(34) + bytes(9)))
    must_reject('ordinary_count_bound', lambda: parse_complete(header + encode_uleb(274) + bytes(69), 272))
    must_reject('zero_count', lambda: parse_complete(header + b'\0'))
    must_reject('odd_count', lambda: parse_complete(header + encode_uleb(3) + b'\0'))
    must_reject('nonzero_padding', lambda: parse_complete(valid[:-1] + bytes((0x44,))))
    must_reject('missing_record', lambda: parse_complete(header))
    must_reject('truncated_payload', lambda: parse_complete(valid[:-1]))
    must_reject('unfinished_uleb', lambda: parse_complete(header + bytes((0x86,))))
    must_reject('trailing_binary', lambda: parse_complete(valid + b'\0'))
    def missing_child():
        current = WireReader(header + encode_uleb(2) + b'\x04', sha1, sha2, 1).next_case(32)
        current.take(); current.take(); current.take()
    must_reject('missing_required_child_action', missing_child)
    def unconsumed_actions():
        current = WireReader(valid, sha1, sha2, 1).next_case(32)
        current.take(); current.finish()
    must_reject('duplicate_or_unconsumed_actions', unconsumed_actions)
    def false_symbol():
        current = WireReader(header + encode_uleb(2) + b'\0', sha1, sha2, 1).next_case(32)
        require(current.take() == 1, 'Synthetic expected C replaced by N')
    must_reject('false_expected_action_symbol', false_symbol)
    return {'status': 'SYNTHETIC_WIRE_ONLY_PASS', 'valid_lsb_action_streams': 1, 'rejection_checks': rejected,
            'real_input_or_common_loaded': False, 'canonical_family_derived': False,
            'matrix_GS_or_representative_executed': False, 'real_case_feasibility_or_fullproof_verified': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', action='store_true', help='Consume an explicit complete saved q4 proof; never produce/search')
    parser.add_argument('--synthetic-wire-self-test', action='store_true', help='Only synthetic format/rejection checks, no real math')
    parser.add_argument('--portable', type=Path)
    parser.add_argument('--input', type=Path)
    proof_group = parser.add_mutually_exclusive_group()
    proof_group.add_argument('--proof', type=Path, help='Complete raw T6Q4DFS1 binary')
    proof_group.add_argument('--proof-source-manifest', '--proof-manifest', dest='proof_manifest', type=Path,
                             help='Complete Source manifest and independently pinned base64 carriers')
    parser.add_argument('--expected-proof-sha256', help='Optional external complete raw binary SHA256 pin')
    parser.add_argument('--context', type=Path, help='Optional observed actual context metadata; does not authorize science')
    parser.add_argument('--output', type=Path, help='New exclusive report path')
    args = parser.parse_args()
    if args.synthetic_wire_self_test:
        require(not args.verify and not any((args.portable, args.input, args.proof, args.proof_manifest, args.context)),
                'Synthetic wire mode cannot accept scientific inputs')
        report = synthetic_wire_self_test()
        if args.output:
            with args.output.open('x', encoding='utf-8') as handle:
                json.dump(report, handle, indent=2); handle.write('\n')
        print(json.dumps(report)); return 0
    if not args.verify:
        print(json.dumps({'status': 'NOT_ADMITTED', 'science_or_proof_consumption_executed': False,
                          'native_authorization': False, 'native_helper_identity': 'UNKNOWN'}))
        return 0
    if not args.portable or not args.input or not (args.proof or args.proof_manifest) or not args.output:
        parser.error('--verify requires --portable --input --proof or --proof-source-manifest and a new --output')
    require(not args.output.exists(), 'Output already exists; preserve prior report bytes')
    progress = {'complete_case_prefix_count': 0, 'currently_consuming_case_index': None, 'first_verified_local_witness': None}
    try:
        portable_raw, portable = read_json(args.portable)
        input_raw, prospective = read_json(args.input)
        proof_raw, proof_evidence = load_saved_proof(args.proof, args.proof_manifest, args.expected_proof_sha256)
        context_observation = observed_context(args.context, input_raw, proof_raw)
        report = verify_full_saved_proof(portable_raw, portable, input_raw, prospective, proof_raw,
                                        context_observation, proof_evidence, progress)
        exit_code = 0
    except (ValueError, KeyError, TypeError, OSError, IndexError, OverflowError) as error:
        report = {'schema': 'T6_Q4_FULL_SOURCE_ONLY_EXACT_SAVED_DFS_VERIFICATION_REPORT_V1',
                  'status': 'REJECTED_INCOMPLETE_OR_INVALID_FULL_PROOF', 'error': str(error),
                  'all30992_saved_case_trees_complete': False, 'progress': progress,
                  'native_helper_identity': 'UNKNOWN', 'directed_shared_owner_nonblind_construction': True,
                  'native_mathematical_acceptance_created': False, 'global_T6_complete': False,
                  'global_goal_status': 'OPEN', 'H0_lower_prime_completion_decided': False,
                  'scientific_search_or_producer_executed': False}
        exit_code = 1
    with args.output.open('x', encoding='utf-8') as handle:
        json.dump(report, handle, indent=2, ensure_ascii=False); handle.write('\n')
    print(json.dumps({k: report[k] for k in ('status', 'classification_counts', 'totals', 'error', 'global_T6_complete') if k in report}))
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
