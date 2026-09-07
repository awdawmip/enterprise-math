from __future__ import annotations
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
from functools import lru_cache
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import types
from unittest.mock import patch

parser = argparse.ArgumentParser(
    description='Replay the frozen bounded BRC migration review; no full selected-case suite.')
parser.add_argument('repo', nargs='?', type=Path,
                    default=Path(__file__).resolve().parents[3],
                    help='repository root; defaults to this package directory layout')
ROOT = parser.parse_args().repo.resolve()
OUT = Path(__file__).resolve().parent
UNIT = ROOT.joinpath('experiments/owner_shell_length_20260907')
BASE = '5eddb6ea23761d928197b3d8227a5b42a7975a34'
EXPECTED_BASE_TREE = '8c0a6c8d0383b3063ae97d00be069db1613c726e'
# Both tree IDs were independently read before packaging. Reproduction needs
# only the published BASE object, not the previous local-only review commit.
ORIGINAL_REVIEW_BASE = '9c8ba08cb82f0d071dfd91c0bdcf17f8220f08c6'
baseline_tree = subprocess.run(
    ['git', 'rev-parse', BASE + '^{tree}'], cwd=ROOT,
    capture_output=True, check=True, text=True).stdout.strip()
assert baseline_tree == EXPECTED_BASE_TREE, baseline_tree
sys.path.insert(0, str(UNIT))
import shell_length as sl
import validate_brc_runtime as validation

PINNED = {
    'shell_length.py': '31c09afd186ecc86d608fdfeb3b014091f22a3b40bcbdc32d568fe0c0db8aa18',
    'validate_brc_runtime.py': '956126dae579767e65dd9f4f80ab04947a8cc1bdbaa9e34c6e41125dea2a21ec',
    'validate_brc_runtime.json': 'c4b454f6b84ed774d8471d685106c143ebea98d689c28cf7aba1ae9817d4fae9',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def frozen():
    got = {name: sha(UNIT.joinpath(name)) for name in PINNED}
    assert got == PINNED, got
    return got

before = frozen()
limit = sys.get_int_max_str_digits()
evidence = json.loads(UNIT.joinpath('validate_brc_runtime.json').read_text(encoding='utf-8'))
assert evidence['helper_sha256'] == PINNED['shell_length.py']
assert evidence['validation_sha256'] == PINNED['validate_brc_runtime.py']
assert evidence['frozen_v1_validation_sha256'] == sha(UNIT.joinpath('validate_selected_cases.json'))
assert evidence['original_validation_source_sha256'] == sha(UNIT.joinpath('validate_selected_cases.py'))
assert evidence['status'] == 'PASS' and evidence['selected_case_count'] == 61
sources = {}
for rel, pinned in evidence['source_dependencies'].items():
    baseline = subprocess.run(['git', 'show', BASE + ':' + rel], cwd=ROOT, capture_output=True, check=True).stdout
    data = ROOT.joinpath(rel).read_bytes()
    assert data == baseline and hashlib.sha256(data).hexdigest() == pinned
    sources[rel] = {'sha256': pinned, 'baseline_bytes_equal': True}

# Execute only two old endpoint constructors as a typed historical comparison,
# never the full old selected-case runner or either legacy multiplicity routine.
old_src = subprocess.run(['git', 'show', BASE + ':experiments/owner_shell_length_20260907/shell_length.py'], cwd=ROOT, capture_output=True, check=True).stdout
old = types.ModuleType('historical_shell_length_oracle')
old.__file__ = str(UNIT.joinpath('shell_length.py'))
exec(compile(old_src, old.__file__, 'exec'), old.__dict__)

# Independent shortest signed-word count: sum over the last occupied axis.
# This oracle uses only integer addition, with no quotient or root evaluation.
@lru_cache(None)
def last_axis_count(magnitudes):
    if not any(magnitudes):
        return 1
    total = 0
    for axis, amount in enumerate(magnitudes):
        if amount:
            prior = list(magnitudes)
            prior[axis] -= 1
            total += last_axis_count(tuple(prior))
    return total

def decode_fields(fields):
    result = {}
    for key, value in fields.items():
        if type(value) is dict:
            assert set(value) == {'encoding', 'value'} and value['encoding'] == 'hex'
            result[key] = int(value['value'], 16)
        else:
            result[key] = value
    return result

facade_calls = []
real_divide, real_root = sl.brc_evaluate_division, sl.brc_evaluate_root

def capture_divide(expr):
    assert type(expr.numerator) is int and expr.numerator >= 0
    assert type(expr.denominator) is int and expr.denominator > 0
    value = real_divide(expr)
    facade_calls.append(asdict(value))
    return value

def capture_root(expr):
    assert type(expr.radicand) is int and expr.radicand >= 0 and expr.degree == 2
    value = real_root(expr)
    facade_calls.append(asdict(value))
    return value

checks = []
payloads = []
selected = json.loads(UNIT.joinpath('validate_selected_cases.json').read_text(encoding='utf-8'))
selected_ns = {entry['N'] for entry in selected['selected_cases']}
with patch.object(sl, 'brc_evaluate_division', capture_divide), patch.object(sl, 'brc_evaluate_root', capture_root):
    for n, signs in [(60, (1, -1, 1, -1, 1, -1)), (61, (-1, 1, -1, 1, -1, 1))]:
        assert n not in selected_ns
        facade_calls.clear()
        payload = sl.certificate(n, signs=signs)
        old_endpoint, old_details = old.construct_endpoint(n, signs=signs)
        assert payload['raw_signed_endpoint'] == old_endpoint
        for field, value in old_details.items():
            assert payload['construction'][field] == value, (n, field)
        assert payload['status'] == 'ENDPOINT_VERIFIED'
        assert payload['verification']['valid']
        assert len(payload['joint_twenty_slices']) == 20
        for row in payload['joint_twenty_slices']:
            assert len(row['axes']) == 3
        count = int(payload['shortest_path_multiplicity']['count_decimal'])
        independent_count = last_axis_count(tuple(abs(x) for x in old_endpoint))
        assert count == independent_count
        encoded = json.loads(json.dumps(payload))
        observed = [decode_fields(row['trace']) for row in encoded['arithmetic_trace']]
        assert observed == facade_calls, 'facade evaluation/trace sequence mismatch'
        for row in encoded['arithmetic_trace']:
            validation.verify_trace(row)
        assert 'arithmetic_trace' not in payload['construction']
        assert 'arithmetic_trace' not in payload['verification']
        checks.append({'case': 'new_endpoint_count_and_trace_bijection', 'N': n, 'endpoint': old_endpoint,
                       'count': count, 'trace_count': len(observed),
                       'signed_triple': old_details['three_odd_squares_signed'], 'status': 'PASS'})
        payloads.append(payload)

# N=60 has D=19: candidate (1,1) fails and (1,3) succeeds.
try:
    sl.construct_endpoint(60, search_budget=1)
except sl.ResourceLimit as error:
    assert 'after 1 candidates' in str(error)
else:
    raise AssertionError('one candidate budget accepted a two-candidate witness')
endpoint, detail = sl.construct_endpoint(60, search_budget=2)
assert detail['candidates_checked'] == 2 and sl.verify_endpoint(60, endpoint)['valid']
checks.append({'case': 'exact_candidate_budget_one_reject_two_accept', 'N': 60, 'status': 'PASS'})

# Force an invalid signed-square triple; no Hadamard division may run first.
attempted_purposes = []
real_division_wrapper = sl._divide

def track_division(numerator, denominator, purpose, ledger):
    attempted_purposes.append(purpose)
    assert numerator >= 0
    return real_division_wrapper(numerator, denominator, purpose, ledger)

with patch.object(sl, '_three_odd_squares', return_value=((101, 1, 1), 1)), patch.object(sl, '_divide', track_division):
    try:
        sl.construct_endpoint(61)
    except ArithmeticError as error:
        assert str(error) == 'Hadamard nonnegativity failed'
    else:
        raise AssertionError('negative Hadamard numerator accepted')
assert 'Hadamard coordinate' not in attempted_purposes
checks.append({'case': 'negative_hadamard_rejected_before_natural_division', 'status': 'PASS'})

# Encode exactly at and above the 2048-bit threshold and independently round trip.
encoded_kinds = []
for numerator in [(1 << 2048) - 1, 1 << 2048]:
    ledger = []
    sl._divide(numerator, 1, 'independent hex boundary', ledger)
    encoded = json.loads(json.dumps(ledger))
    assert decode_fields(encoded[0]['trace'])['numerator'] == numerator
    validation.verify_trace(encoded[0])
    encoded_kinds.append(type(encoded[0]['trace']['numerator']).__name__)
assert encoded_kinds == ['int', 'dict']
assert sys.get_int_max_str_digits() == limit
checks.append({'case': 'hex_threshold_exact_json_and_decimal_limit_preserved', 'decimal_limit': limit, 'status': 'PASS'})

# Independent additional corruption signatures, not a rerun of 1641 traces.
records = payloads[0]['arithmetic_trace']
division_record = next(r for r in records if r['trace']['evaluation_kind'] == 'BRC_DIVISION_EVALUATION')
root_record = next(r for r in records if r['trace']['evaluation_kind'] == 'BRC_ROOT_EVALUATION')
corruptions = []
for name, record, field, value in [
    ('wrong_quotient', division_record, 'quotient', division_record['trace']['quotient'] + 1),
    ('zero_denominator', division_record, 'denominator', 0),
    ('boolean_integer', division_record, 'remainder', False),
    ('wrong_root_basin', root_record, 'next_power', root_record['trace']['next_power'] + 1),
]:
    changed = deepcopy(record)
    changed['trace'][field] = value
    corruptions.append((name, changed))
missing = deepcopy(root_record)
del missing['trace']['collapsed_radicand']
corruptions.append(('missing_root_field', missing))
for name, corrupted in corruptions:
    try:
        validation.verify_trace(corrupted)
    except AssertionError:
        pass
    else:
        raise AssertionError('trace corruption accepted: ' + name)
checks.append({'case': 'five_additional_trace_corruption_signatures_rejected', 'signatures': [name for name, _ in corruptions], 'status': 'PASS'})

assert frozen() == before
assert sys.get_int_max_str_digits() == limit
report = {
    'schema': 'owner_shell_brc_independent_bounded_review_v1',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Independent bounded source/API migration review, not a formal V2 review or all-N proof.',
    'status': 'PASS_FINITE_BOUNDARIES_NO_MATERIAL_DEFECT_FOUND',
    'baseline': BASE,
    'baseline_tree': baseline_tree,
    'baseline_equivalence': {
        'original_review_local_commit': ORIGINAL_REVIEW_BASE,
        'original_review_tree_pin': EXPECTED_BASE_TREE,
        'public_tree_matches_original_review': baseline_tree == EXPECTED_BASE_TREE,
        'provenance': 'Both commit trees independently read as equal before packaging; replay requires only the published baseline object.'
    },
    'runtime': {'python': sys.version.split()[0], 'assertions_enabled': __debug__,
                'repo_root': str(ROOT), 'package_default_repo_root': str(OUT.parents[2])},
    'replay_scope': 'Exactly the existing two independent endpoint cases and original boundary/fault injections, with no added mathematical cases.',
    'input_sha256': before, 'source_dependencies': sources,
    'golden_evidence_bindings': 'PASS; inspected frozen result without rerunning its 61 cases or 1641 traces',
    'checks': checks,
    'script_sha256': sha(Path(__file__)),
    'policy': 'ENTERPRISE_MATH_EXACT_ARITHMETIC_RUNTIME_POLICY_V2',
    'global_knowledge_canonical': '990d7c1b3a7c63ab4c81b356a28ca88be953c2e8',
    'boundaries': [
        'Arithmetic traces prove local exact evaluations; they are not a certificate authenticity signature or an all-N mathematical proof.',
        'Upper_length scalar API is retained; upper_length_evaluation and optional ledger expose its three BRC evaluations.',
        'Search budget bounds tested candidate pairs, not arbitrary-precision CPU time or memory.',
        'Multiplicity event/readout resource outcomes remain separate from endpoint existence; default budget is unchanged.',
        'Only review.py/review.json/REVIEW.md are added in the dedicated package directory. Frozen reviewed files, catalog, old TEMP evidence, coordinates, facade, and untracked proof are unchanged; no remote action.'
    ]
}
output = OUT.joinpath('review.json')
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'status': report['status'], 'checks': checks, 'report': str(output), 'report_sha256': sha(output)}, ensure_ascii=False))
