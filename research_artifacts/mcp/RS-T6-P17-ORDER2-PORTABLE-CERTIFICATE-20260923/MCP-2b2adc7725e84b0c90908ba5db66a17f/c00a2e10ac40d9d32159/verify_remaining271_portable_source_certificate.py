#!/usr/bin/env python3
"""Standalone portable Source certificate consumer; no feasibility generation.

Default inputs are compact certificate, common portable/problem, actual observed
control metadata, and three prior q2-1 Source artifacts (ledger, review pack,
checkpoint). No local case, verbose batch, tar archive or native publication
receipt is opened. Optional --diagnostic-root audits saved verbose bytes.
The q2-1 tree is not mathematically reconsumed. This consumes saved proof only.
"""

import argparse
import base64
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path

PORTABLE_SHA = '7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce'
TASK_ID = 'RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923'
PUBLICATION_ID = 'TP2-33BFE7DD84657DAB803C'
SIDE_BUDGET = 2331
PROBLEM_SHA = "a16356adfd5c1763ed0c0426b381d89f70f0c51736335687578f1b9a5c63db0d"
PRIOR_SOURCE = "c406e50f16d8e1d3ba359f3291299170d7940bad"
PRIOR_LEDGER_SHA = "0cacbc773fc6f4bb995f36ad127aa07fd7cfa5bf6e79195a2b78db3549da016c"
PRIOR_REVIEW_PACK_SHA = "0a564c8b5fa6727e4d298064523af8a2b087515782cb76cb385de60761a71644"
PRIOR_RECEIPT_SHA = "0d1a941e3e3f45a4ca8f48884453b8b117824b518434ed978df5f3af7a888ae5"


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


def derive_case(case):
    """Static input derivation only; no representative or branch is produced."""
    positive = [[integer(q), integer(r)] for q, r in case['positive_atoms']]
    negative = [[integer(q), integer(r)] for q, r in case['negative_atoms']]
    require(all(q in (1, 2) and 1 <= r <= 16 for q, r in positive + negative),
            'Atom outside order2 descriptors')
    require(sum(q for q, _ in positive + negative) == 2, 'Vertical order mismatch')
    if len(positive) == 1 and positive[0][0] == 2 and not negative:
        expected_id = f'q2-{positive[0][1]}'
    elif len(positive) == 2 and all(q == 1 for q, _ in positive) and not negative:
        a, b = positive[0][1], positive[1][1]
        require(a <= b, 'Same-side unordered pair not normalized')
        expected_id = f'same-q1-{a}-{b}'
    elif len(positive) == len(negative) == 1 and positive[0][0] == negative[0][0] == 1:
        a, b = positive[0][1], negative[0][1]
        require(a < b, 'Opposite pair cancels or is not normalized up to sign')
        expected_id = f'opposite-q1-{a}-{b}'
    else:
        raise ValueError('Not one of the original primitive order2 descriptor classes')
    require(case['id'] == expected_id, 'Pattern ID does not identify the atoms')
    positive_cofactors = [17 * q + r for q, r in positive]
    negative_cofactors = [17 * q + r for q, r in negative]
    positive_mass = sum(17 * s - 1 for s in positive_cofactors)
    negative_mass = sum(17 * s - 1 for s in negative_cofactors)
    positive_budget = SIDE_BUDGET - positive_mass
    negative_budget = SIDE_BUDGET - negative_mass
    require(positive_budget >= 0 and negative_budget >= 0, 'Fixed atoms exhaust a side')
    radius = positive_budget ** 2 + negative_budget ** 2
    targets = [(-sum(pow(s, -k, 17 ** k) for s in positive_cofactors) +
                sum(pow(s, -k, 17 ** k) for s in negative_cofactors)) % (17 ** k)
               for k in range(1, 7)]
    require(integer(case['q0_positive_budget']) == positive_budget and
            integer(case['q0_negative_budget']) == negative_budget and
            integer(case['radius_squared']) == radius, 'Descriptor side budgets or radius mismatch')
    require(list(map(integer, case['mixed_targets'])) == targets, 'Descriptor mixed targets mismatch')
    largest = max([17] + [largest_prime_factor(s) for s in positive_cofactors + negative_cofactors])
    return {'pattern_id': expected_id, 'positive_atoms': case['positive_atoms'],
            'negative_atoms': case['negative_atoms'], 'positive_fixed_mass': positive_mass,
            'negative_fixed_mass': negative_mass, 'positive_budget': positive_budget,
            'negative_budget': negative_budget, 'radius_squared': radius, 'targets': targets,
            'maximal_p17_admissible': largest == 17, 'largest_vertical_prime': largest}


def derive_all_cases(problem):
    require(len(problem['cases']) == 272, 'Original family must have 272 descriptors')
    cases = {}
    for case in problem['cases']:
        derived = derive_case(case)
        require(derived['pattern_id'] not in cases, 'Duplicate original pattern ID')
        cases[derived['pattern_id']] = derived
    expected = ({f'q2-{r}' for r in range(1, 17)} |
                {f'same-q1-{a}-{b}' for a in range(1, 17) for b in range(a, 17)} |
                {f'opposite-q1-{a}-{b}' for a in range(1, 17) for b in range(a + 1, 17)})
    require(set(cases) == expected, 'Original descriptor family incomplete')
    require(problem['case_counts'] == {'q2_single': 16, 'same_q1_pair': 136,
                                     'opposite_q1_pair_up_to_sign': 120, 'total': 272},
            'Original family count metadata mismatch')
    return cases


PRIOR_CHECKPOINT_SHA = '5b325ffc9a744d353e8c57a89bd7b462398b21c5f4e6b62738987502b20b28b8'
PRIOR_CONTRIBUTOR_IDS = ['EM-DIRECT-49ADE6', 'EM-DIRECT-E1F2B6', 'EM-DIRECT-FA0C27', 'EM-DVR-4C90FB', 'EM-DVR-C1A1D9', 'EM-DVR-FBF223', 'EM-T6-B4F89F']
EXPECTED_PRIOR_OUTPUT_PINS = {'q2_1_exact_executor.py': {'sha256': '401462459bcbb2c72ba9da858f17918545c08157db60b34dcda2b86eadd203e6', 'git_blob_sha1': '388ea199ffd89c15dfceb35c2149009dd4b1b2da'}, 'Q2_1_COMPLETE_NEW_LEDGER.json': {'sha256': '0cacbc773fc6f4bb995f36ad127aa07fd7cfa5bf6e79195a2b78db3549da016c', 'git_blob_sha1': '758102d8c9fed37d9014555105891ec3d927bb18'}, 'Q2_1_EXACT_AFFINE_INPUT.json': {'sha256': '8f0ea88c45a54fb01ab8524bd9cc3147c9ffcb96d02dee535472c7fd994ec179', 'git_blob_sha1': '3cb703610e211f49cc2bc797ee416bb990fa2d78'}, 'Q2_1_COMPLETE_COVERAGE_ARGUMENT.md': {'sha256': 'fa7732952eec580dfc954760b1e0c00c9f2df79bfa46f6739555bbb9707603c7', 'git_blob_sha1': 'f195f257b890e499e2942b91929e20c9e86f0615'}, 'RETURN.md': {'sha256': '8212d10d92841e23bf8efda5e9ef95db6f23a04652c0ed58a2353aca8fbd5187', 'git_blob_sha1': '921c2719d08e452e6c340d9466434c5e7575d141'}, 'CONTRIBUTION_AND_EXPOSURE_DISCLOSURE.md': {'sha256': '6d639c43d5720fd3dc2c274349ce60e06fca38216025c8040ea235deb883815e', 'git_blob_sha1': 'e7942c08c67c2ce639c1bf34b785078963251d2e'}, 'OWN_NATIVE_CONTROL_EVIDENCE_PACKED.json': {'sha256': '41f1e8cdb077d711639b6da207ce48f6effddec120be7da1f9abb9bc5a0303c2', 'git_blob_sha1': '33c90764487708600f6e34a32b474d7169ac935c'}, 'INDEPENDENT_REVIEW_EVIDENCE_PACKED.json': {'sha256': '0a564c8b5fa6727e4d298064523af8a2b087515782cb76cb385de60761a71644', 'git_blob_sha1': '43418a5351789512e24b1eed939e34695491ed4a'}, 'verify_q2_1_saved_ledger.py': {'sha256': '1003b2334a54ae080a6ef4e87271b6176527f3e55b26030d2726e565f05b2d8c', 'git_blob_sha1': '50732f6272c614766c304a302a361ccc26d3e146'}}

def git_blob(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()


def verify_prior_source_input(ledger_path, review_pack_path, checkpoint_path):
    """Join only published prior Source artifacts; do not consume the old tree."""
    ledger_raw, ledger = read_json(ledger_path)
    pack_raw, pack = read_json(review_pack_path)
    checkpoint_raw, checkpoint = read_json(checkpoint_path)
    require(hashlib.sha256(ledger_raw).hexdigest() == PRIOR_LEDGER_SHA, 'Prior Source ledger pin mismatch')
    require(hashlib.sha256(pack_raw).hexdigest() == PRIOR_REVIEW_PACK_SHA, 'Prior Source review pack pin mismatch')
    require(hashlib.sha256(checkpoint_raw).hexdigest() == PRIOR_CHECKPOINT_SHA, 'Prior Source checkpoint pin mismatch')
    require(checkpoint['schema'] == 'ENTERPRISE_MATH_MCP_EXECUTION_CHECKPOINT_V1' and
            checkpoint['task_id'] == TASK_ID and checkpoint['publication_id'] == PUBLICATION_ID and
            checkpoint['researcher_id'] == 'EM-T6-B4F89F' and
            checkpoint['session_id'] == 'MCP-2b2adc7725e84b0c90908ba5db66a17f' and
            checkpoint['executor_role'] == 'RESEARCHER', 'Prior checkpoint identity/Task/pub mismatch')
    require(checkpoint['contributor_ids'] == PRIOR_CONTRIBUTOR_IDS, 'Prior seven contribution identities changed')
    require(checkpoint['verification'] == 'AUTHOR_REPORTED_SOURCE_BYTES_ONLY_NOT_MATHEMATICAL_ACCEPTANCE',
            'Prior checkpoint byte custody promoted to acceptance')
    prefix = ('research_artifacts/mcp/' + TASK_ID +
              '/MCP-2b2adc7725e84b0c90908ba5db66a17f/312c962b9deda3d96d48/')
    rows = checkpoint['output_manifest']
    require(len(rows) == 9 and len({row['path'] for row in rows}) == 9, 'Prior output manifest closure mismatch')
    manifest = {}
    for row in rows:
        name = Path(row['path']).name
        require(name in EXPECTED_PRIOR_OUTPUT_PINS and row['path'] == prefix + name,
                'Unexpected prior Source output path')
        expected = EXPECTED_PRIOR_OUTPUT_PINS[name]
        require(row['sha256'] == 'sha256:' + expected['sha256'] and
                row['git_blob_sha1'] == 'sha1:' + expected['git_blob_sha1'], 'Prior Source output manifest pin mismatch')
        manifest[name] = row
    require(set(manifest) == set(EXPECTED_PRIOR_OUTPUT_PINS), 'Prior Source outputs missing')
    for name, raw in [('Q2_1_COMPLETE_NEW_LEDGER.json', ledger_raw),
                      ('INDEPENDENT_REVIEW_EVIDENCE_PACKED.json', pack_raw)]:
        require(hashlib.sha256(raw).hexdigest() == EXPECTED_PRIOR_OUTPUT_PINS[name]['sha256'] and
                git_blob(raw) == EXPECTED_PRIOR_OUTPUT_PINS[name]['git_blob_sha1'],
                'Provided prior Source bytes differ from checkpoint SHA/Git-blob')
    require(pack['codec'] == 'gzip+base64-utf8-json' and pack['file_count'] == 8, 'Prior pack shape mismatch')
    decoded = gzip.decompress(base64.b64decode(pack['payload'], validate=True))
    require(len(decoded) == pack['original_bytes'] and
            hashlib.sha256(decoded).hexdigest() == pack['original_sha256'], 'Prior decoded review pack byte pin mismatch')
    packed = json.loads(decoded.decode('utf-8'), object_pairs_hook=unique_object)['files']
    members = {row['path']: row for row in packed}
    pack_manifest = {row['path']: row for row in pack['files']}
    require(len(packed) == len(members) == len(pack['files']) == len(pack_manifest) == 8 and
            set(members) == set(pack_manifest), 'Prior eight-member review closure mismatch')
    for name, row in members.items():
        path = Path(name)
        require(not path.is_absolute() and '..' not in path.parts, 'Unsafe prior packed review path')
        content = row['content'].encode('utf-8')
        expected = pack_manifest[name]
        require(len(content) == expected['bytes'] and hashlib.sha256(content).hexdigest() == expected['sha256'] and
                git_blob(content) == expected['git_blob_sha1'], 'Prior packed member byte/SHA/Git-blob mismatch')
    name = 'independent-check/INDEPENDENT_Q2_1_LEDGER_VERIFICATION_RECEIPT.json'
    independent_raw = members[name]['content'].encode('utf-8')
    require(hashlib.sha256(independent_raw).hexdigest() == PRIOR_RECEIPT_SHA, 'Prior scientific receipt pin mismatch')
    independent = json.loads(independent_raw.decode('utf-8'), object_pairs_hook=unique_object)
    require(independent['status'] == 'INDEPENDENT_SAVED_LEDGER_PASS' and
            independent['pattern_id'] == 'q2-1' and independent['outcome'] == 'EMPTY' and
            independent['native_helper_identity'] == 'UNKNOWN' and
            independent['native_authority_asserted_by_checker'] is False, 'Prior independent receipt scope/provenance mismatch')
    require(ledger['pattern_id'] == 'q2-1' and ledger['outcome'] == 'EMPTY' and
            ledger['completed_pattern_ids'] == ['q2-1'] and ledger['complete_traversal'] is True,
            'Prior Source-completed unit metadata mismatch')
    return {'pattern_id': 'q2-1', 'outcome': 'EMPTY', 'source_commit': PRIOR_SOURCE,
            'source_input_only_no_tree_reconsumption': True, 'prior_checkpoint_manifest_outputs_checked': 9,
            'prior_review_pack_members_byte_verified': 8, 'contributor_ids': PRIOR_CONTRIBUTOR_IDS,
            'input_sha256': {'ledger': hashlib.sha256(ledger_raw).hexdigest(),
                             'independent_review_pack': hashlib.sha256(pack_raw).hexdigest(),
                             'Source_checkpoint': hashlib.sha256(checkpoint_raw).hexdigest()},
            'native_acceptance_created_by_checker': False}


def compact_projection(verbose):
    """Canonical complete scientific projection of a saved verbose record; no search."""
    keys = ('pattern_id', 'outcome', 'particular_q0', 'root', 'survivors',
            'complete_traversal', 'resource_exhausted', 'maximal_p17_admissible',
            'largest_vertical_prime', 'positive_atoms', 'negative_atoms',
            'positive_vertical_mass', 'negative_vertical_mass', 'q0_positive_budget',
            'q0_negative_budget', 'radius_squared', 'mixed_targets',
            'literal_relaxed_outcome_even_if_outside_domain')
    result = {key: verbose[key] for key in keys}
    result['certificate_encoding'] = 'COMPACT_INDEXED_TWO_CHOICE_TREE_V1'
    result['nodes'] = []
    for node in verbose['nodes']:
        projected = {'id': node['id'], 'index': node['index'], 'edges': []}
        require(len(node['edges']) == 2, 'Cannot project an incomplete saved node')
        for edge in node['edges']:
            action = edge['action']
            require(action in ('CHILD', 'NORM_PRUNED', 'BUDGET_PRUNED', 'SURVIVOR'),
                    'Unknown complete-certificate edge action')
            saved = {'z': edge['z'], 'action': action}
            if action == 'CHILD':
                saved['child'] = edge['child']
            elif action in ('BUDGET_PRUNED', 'SURVIVOR'):
                for key in ('vector', 'positive_mass', 'negative_mass', 'mixed_residues',
                            'weighted_norm', 'positive_budget', 'negative_budget'):
                    saved[key] = edge[key]
            projected['edges'].append(saved)
        result['nodes'].append(projected)
    return result


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
    require(pattern_id != 'q2-1', 'Completed q2-1 must not be replayed')
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
        require(ledger['global_T6_complete'] is False, 'A local order2 proof cannot close global T6')
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


def verify_batch(portable, problem, batch, diagnostic_root=None):
    require(batch['task_id'] == TASK_ID and batch['publication_id'] == PUBLICATION_ID,
            'Saved batch task/publication scope mismatch')
    require(batch['new_pattern_count'] == 271 and batch['prime17_admissible_count'] == 153 and
            batch['outside_domain_count'] == 118 and batch['outside_patterns_classified_not_skipped'] is True,
            'Saved batch coverage/domain metadata mismatch')
    for key in ('global_T6_complete', 'family_hard_target_complete', 'p19_replayed', 'q2_1_replayed'):
        require(batch[key] is False, 'Saved batch scope claim mismatch: ' + key)
    require(batch['family_integration_and_Driver_review_required'] is True,
            'Saved local classification lacks required integration/review distinction')
    prior = batch['prior_q2_1']
    require(prior['pattern_id'] == 'q2-1' and prior['source_commit'] == PRIOR_SOURCE and
            prior['ledger_sha256'] == PRIOR_LEDGER_SHA and prior['input_only'] is True and
            prior['replayed'] is False and prior['nodes_copied_into_new_payload'] is False and
            prior['counts_included_in_new_compute_totals'] is False,
            'Source-completed q2-1 must remain a pinned input outside new computation')
    derived = derive_all_cases(problem)
    remaining = {name: case for name, case in derived.items() if name != 'q2-1'}
    require(len(remaining) == 271, 'Remaining original ID count mismatch')
    maximum = max(case['radius_squared'] for case in derived.values())
    common = common_basis(portable, problem, maximum)
    require(sum(case['maximal_p17_admissible'] for case in remaining.values()) == 153,
            'Remaining domain accounting mismatch')
    require(len(batch['case_ledgers']) == 271, 'Saved batch does not contain exactly 271 new records')
    ledgers = {record['pattern_id']: record for record in batch['case_ledgers']}
    require(len(ledgers) == 271 and set(ledgers) == set(remaining), 'Saved new pattern IDs missing, duplicated, or replayed')
    require(batch['completed_pattern_ids'] == [record['pattern_id'] for record in batch['case_ledgers']],
            'Saved completed-ID list differs from its complete records')
    manifest_rows = batch['case_artifact_manifest']
    manifest = {row['pattern_id']: row for row in manifest_rows}
    require(len(manifest_rows) == len(manifest) == 271 and set(manifest) == set(remaining),
            'Individual saved-case manifest incomplete')
    require(batch['certificate_encoding'] == 'COMPACT_INDEXED_TWO_CHOICE_TREE_V1', 'Portable input is not the complete compact encoding')
    require(all(record.get('certificate_encoding') == 'COMPACT_INDEXED_TWO_CHOICE_TREE_V1'
                for record in batch['case_ledgers']), 'Portable record lacks complete compact encoding marker')
    for name, row in manifest.items():
        relative = Path(row['path'])
        require(not relative.is_absolute() and '..' not in relative.parts and
                relative.as_posix() == f'cases/{name}.json', 'Unsafe diagnostic reference path')
        require(type(row['bytes']) is int and row['bytes'] > 0 and
                isinstance(row['sha256'], str) and len(row['sha256']) == 64 and
                isinstance(row['git_blob_sha1'], str) and len(row['git_blob_sha1']) == 40,
                'Invalid diagnostic-only original byte reference')
    individual_pins = []
    if diagnostic_root is not None:
        for name, row in manifest.items():
            relative = Path(row['path'])
            require(not relative.is_absolute() and '..' not in relative.parts and
                    relative.as_posix() == f'cases/{name}.json', 'Unsafe or unexpected individual case path')
            raw, record = read_json(Path(diagnostic_root) / relative)
            digest = hashlib.sha256(raw).hexdigest()
            blob = hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()
            require(row['bytes'] == len(raw) and row['sha256'] == digest and row['git_blob_sha1'] == blob,
                    'Individual case byte/SHA256/Git-blob pin mismatch')
            if ledgers[name].get('certificate_encoding') == 'COMPACT_INDEXED_TWO_CHOICE_TREE_V1':
                require(compact_projection(record) == ledgers[name], 'Compact case differs from canonical saved verbose projection')
            else:
                require(record == ledgers[name], 'Individual saved case differs from embedded batch record')
            individual_pins.append({'pattern_id': name, 'path': row['path'], 'bytes': len(raw),
                                    'sha256': digest, 'git_blob_sha1': blob})
    summaries = [consume_case(common, remaining[record['pattern_id']], record) for record in batch['case_ledgers']]
    totals = {key: sum(summary['counters'][key] for summary in summaries)
              for key in ('nodes', 'edges', 'norm_pruned', 'budget_pruned', 'full_leaves', 'resource_stops')}
    require(totals['edges'] <= 73712, 'Uniform 271-case edge bound exceeded')
    complete = all(summary['complete_saved_tree_consumed'] for summary in summaries)
    require(batch['complete_traversal'] is complete and batch['resource_exhausted'] is (not complete),
            'Saved batch completion/resource metadata mismatch')
    for key, actual in [('total_node_count', totals['nodes']), ('total_edge_count', totals['edges']),
                        ('survivor_count', sum(len(summary['survivors']) for summary in summaries))]:
        require(type(batch[key]) is int and batch[key] == actual, 'Saved batch total mismatch: ' + key)
    require(batch['classification_counts'] ==
            {outcome: sum(summary['outcome'] == outcome for summary in summaries)
             for outcome in ('EMPTY', 'LOCAL_KERNEL')}, 'Saved classification totals mismatch')
    return {'status': 'INDEPENDENT_PORTABLE_SOURCE_REMAINING271_PROOF_PASS', 'new_pattern_count': 271,
            'source_completed_pattern_input_only': ['q2-1'],
            'new_completed_pattern_ids': [summary['pattern_id'] for summary in summaries if summary['complete_saved_tree_consumed']],
            'new_resource_incomplete_pattern_ids': [summary['pattern_id'] for summary in summaries if not summary['complete_saved_tree_consumed']],
            'new_domain_counts': {'maximal_p17_admissible': 153, 'outside_maximal_p17_domain': 118},
            'literal_relaxed_classification_required_for_outside_cases': True,
            'all_remaining271_saved_trees_complete': complete,
            'all_original272_relaxed_classes_complete_with_prior_input': complete,
            'all_original272_relaxed_classes_EMPTY_with_prior_input': complete and all(s['outcome'] == 'EMPTY' for s in summaries),
            'totals': totals, 'case_summaries': summaries, 'individual_case_file_pins': individual_pins,
            'diagnostic_root_used': diagnostic_root is not None,
            'local_cases_or_verbose_originals_required_for_scientific_proof': False,
            'diagnostic_projection_byte_audit_performed_by_this_invocation': diagnostic_root is not None,
            'uniform_static_bounds': {'nodes_per_case': 136, 'edges_per_case': 272, 'new_edges_total': 73712,
                                      'max_original_radius_squared': str(maximum)},
            'global_T6_complete': False, 'native_helper_identity': 'UNKNOWN',
            'native_authority_or_acceptance_asserted_by_checker': False,
            'method': 'Saved proof consumption only; common independent exact Gram/LDL and full mixed-kernel validation once; variable-case centers and complete two-choice trees; no feasibility generation'}


def verify_observed_control_metadata(control, batch, raw):
    """Join the existing observed context as metadata; create no execution authority."""
    require(control['task_id'] == TASK_ID and control['publication_id'] == PUBLICATION_ID and
            control['researcher_id'] == 'EM-T6-B4F89F' and
            control['session_id'] == 'MCP-2b2adc7725e84b0c90908ba5db66a17f' and
            control['activity_id'] == 'RA-B6662BE3C64EEFC2AA156A87', 'Observed control identity/scope mismatch')
    require(control['scope'] == 'ALL_REMAINING_271_LITERAL_RELAXED_ORDER2_PATTERNS' and
            control['excluded_replay_pattern_ids'] == ['q2-1'] and control['include_outside_domain_patterns'] is True and
            control['prior_q2_1_replayed'] is False, 'Observed control scope/replay metadata changed')
    require(control['native_authorized'] is True and control['native_mathematical_acceptance_granted'] is False and
            control['platform_session_attested'] is False and control['global_goal_status'] == 'OPEN',
            'Observed control/acceptance/provenance metadata changed')
    require(batch['own_actual_control'] ==
            {key: control[key] for key in ('researcher_id', 'session_id', 'claim_id', 'execution_record_id',
                                         'run_id', 'run_generation')}, 'Certificate/observed control join mismatch')
    evidence = batch['control_evidence']
    require(evidence['context_sha256'] == hashlib.sha256(raw).hexdigest() and
            evidence['Source_scope_proof'] == control['source_scope_proof'] and
            evidence['actual_receipts'] == control['actual_receipts'] and
            evidence['native_authority_granted_by_local_code'] is False, 'Observed control byte/reference binding mismatch')
    credit = batch['construction_credit']
    require(credit['local_helper_native_identity'] is None and credit['shared_owner_nonblind'] is True and
            credit['independent_consumer_is_separate_not_imported'] is True and
            credit['Root_contribution'] == 'Structural branch bound and compact complete certificate design',
            'Construction credit/UNKNOWN helper disclosure changed')
    return {'control_metadata_sha256': hashlib.sha256(raw).hexdigest(),
            'metadata_only_no_native_receipt_path_opened': True,
            'fresh_native_liveness_or_authority_created_by_consumer': False,
            'native_mathematical_acceptance_asserted': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--portable', required=True)
    parser.add_argument('--problem', required=True)
    parser.add_argument('--certificate', '--batch', dest='certificate', required=True)
    parser.add_argument('--control-evidence', required=True)
    parser.add_argument('--prior-q2-1-ledger', required=True)
    parser.add_argument('--prior-q2-1-review-pack', required=True)
    parser.add_argument('--prior-q2-1-checkpoint', required=True)
    parser.add_argument('--diagnostic-root')
    parser.add_argument('--source-only-root')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    input_paths = {'portable': args.portable, 'problem': args.problem, 'certificate': args.certificate,
                   'control_evidence': args.control_evidence, 'prior_q2_1_ledger': args.prior_q2_1_ledger,
                   'prior_q2_1_review_pack': args.prior_q2_1_review_pack,
                   'prior_q2_1_Source_checkpoint': args.prior_q2_1_checkpoint}
    isolated = None
    if args.source_only_root:
        root = Path(args.source_only_root).resolve()
        supplied = {Path(path).resolve() for path in input_paths.values()}
        require(args.diagnostic_root is None and len(supplied) == 7 and
                all(path.parent == root for path in supplied) and
                set(root.iterdir()) == supplied and all(path.is_file() for path in supplied),
                'Source-only validation root must contain only the seven exact supplied inputs')
        require(not (root / 'cases').exists() and not (root / 'BATCH_COMPLETE_PROOF.json').exists() and
                not (root / 'COMPLETE_VERBOSE_ORIGINALS.tar.gz').exists(),
                'Source-only root contains forbidden local diagnostics')
        isolated = {'only_seven_exact_inputs': True, 'local_cases_absent': True,
                    'aggregate_verbose_proof_absent': True, 'raw_diagnostic_archive_absent': True}
    portable_raw, portable = read_json(args.portable)
    problem_raw, problem = read_json(args.problem)
    require(hashlib.sha256(portable_raw).hexdigest() == PORTABLE_SHA, 'Common portable Source pin mismatch')
    require(hashlib.sha256(problem_raw).hexdigest() == PROBLEM_SHA, 'Original 272-case Source pin mismatch')
    require(problem['common_basis_sha256'] == PORTABLE_SHA, 'Original common-basis join mismatch')
    prior = verify_prior_source_input(args.prior_q2_1_ledger, args.prior_q2_1_review_pack, args.prior_q2_1_checkpoint)
    batch_raw, batch = read_json(args.certificate)
    control_raw, control = read_json(args.control_evidence)
    control_join = verify_observed_control_metadata(control, batch, control_raw)
    report = verify_batch(portable, problem, batch, args.diagnostic_root)
    report['task_id'] = TASK_ID
    report['publication_id'] = PUBLICATION_ID
    report['prior_q2_1_Source_input'] = prior
    report['observed_control_metadata_join'] = control_join
    report['source_only_input_environment'] = isolated
    report['input_pins'] = []
    for name, path in input_paths.items():
        content = Path(path).read_bytes()
        report['input_pins'].append({'input': name, 'filename': Path(path).name, 'bytes': len(content),
                                     'sha256': hashlib.sha256(content).hexdigest(), 'git_blob_sha1': git_blob(content)})
    report['reused_own_frozen_math_core_source_sha256'] = 'ffbdf63c3d7c9574537bae55d98c36f84484e469636198e46212d566f6c626dc'
    report['scientific_search_or_producer_execution'] = False
    report['repeated_check_is_saved_certificate_validation_not_new_census'] = True
    report['prior_q2_1_native_publication_receipt_required'] = False
    output = Path(args.output)
    require(not output.exists(), 'Refuse to overwrite existing portable independent verification')
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: report[key] for key in ('status', 'new_pattern_count', 'new_domain_counts', 'totals',
                      'all_remaining271_saved_trees_complete', 'all_original272_relaxed_classes_EMPTY_with_prior_input',
                      'global_T6_complete', 'source_only_input_environment')}, indent=2))


if __name__ == '__main__':
    main()
