"""Read/hash/JSON-shape checks only; never import or execute mathematics."""
import ast
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
PACKAGE = Path('D:/em/TEMP/rb-cm24-source-exposed-full-v3-20260909')
ROOT = Path('D:/em/research-rb-cm24-source-exposed-20260909')
REL = 'research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909'
FROZEN = PACKAGE.joinpath('frozen-source')
START = dt.datetime.now(dt.timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()


def pin(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': sha(raw), 'blob': blob(raw), 'bytes': len(raw)}


publication_raw = PACKAGE.joinpath('publication.json').read_bytes()
assert sha(publication_raw) == '843bc000fd927108c72d792a86f5a77ede2e6afe16e2b3dda4f0ec0901d9cdc6'
publication = json.loads(publication_raw)
files = publication['files']
assert len(files) == 40 and len({x['path'] for x in files}) == 40
all_file_pins = []
for item in files:
    actual = pin(FROZEN.joinpath(item['path']))
    assert all(actual[key] == item[key] for key in ('sha256', 'blob', 'bytes'))
    assert FROZEN.joinpath(item['path']).read_bytes() == item['content'].encode('utf-8')
    all_file_pins.append(dict(actual, repository_path=item['path']))

source_freeze = ROOT.joinpath(REL, 'source_freeze.json')
assert pin(source_freeze)['sha256'] == '85946a8cb4e736021cef6cd311c8cfffbde1cce34fe728255db4b6703f5887f2'
binding_path = FROZEN.joinpath(REL, 'checkpoints/placement_source_binding.json')
source_pins = []
for kind, path in [('original_formula', source_freeze), ('historical_placement', binding_path)]:
    for item in json.loads(path.read_bytes())['source_pins']:
        actual = pin(ROOT.joinpath(item['path']))
        assert actual['sha256'] == item['sha256'] and actual['bytes'] == item['bytes']
        assert actual['blob'] == item.get('blob', item.get('git_blob'))
        source_pins.append(dict(actual, kind=kind, immutable_source_commit=item['source_commit']))
assert len(source_pins) == 12

run = FROZEN.joinpath(REL, 'runs/placement_v3_final')
receipt = json.loads(run.joinpath('receipt.json').read_bytes())
assert receipt['all_pass'] and receipt['complete'] and receipt['selected_sources_unchanged']
assert len(receipt['commands']) == 3
for name in ('check_exact_map.py', 'test_exact_map.py', 'exact_map_proof.md'):
    raw = FROZEN.joinpath(REL, name).read_bytes()
    assert raw == run.joinpath(name + '.frozen').read_bytes()
    assert sha(raw) == receipt['source_pins'][name]['sha256']
    assert len(raw) == receipt['source_pins'][name]['bytes']
assert sha(run.joinpath('replay.py').read_bytes()) == receipt['runner_sha256']
for command in receipt['commands']:
    assert command['exit_code'] == 0 and not command['timed_out']
    assert command['outer_timeout_seconds'] == 600
    for stream in ('stdout', 'stderr'):
        assert sha(run.joinpath(command['label'] + '.' + stream).read_bytes()) == command[stream + '_sha256']
test_log = run.joinpath('focused-tests.stderr').read_text(encoding='utf-8')
assert test_log.count(' ... ok\n') == 13 and 'Ran 13 tests in 0.880s\n\nOK\n' in test_log
assert run.joinpath('selected-static.stdout').read_text(encoding='utf-8').strip() == 'EXACT_ARITHMETIC_POLICY: PASS (2 files)'
certificate_raw = FROZEN.joinpath(REL, 'exact_map_certificate.json').read_bytes()
assert certificate_raw == run.joinpath('certificate.json').read_bytes()
assert sha(certificate_raw) == receipt['certificate_sha256']
assert len(certificate_raw) == receipt['certificate_bytes']
stdout = json.loads(run.joinpath('certificate.stdout').read_bytes())
assert stdout['sha256'] == sha(certificate_raw) and stdout['bytes'] == len(certificate_raw)
certificate = json.loads(certificate_raw)
assert certificate['identity_status'] == 'FULL_FUNCTION_FIELD_ODE_CLEARED_IDENTITY_PASS'
assert certificate['task_verdict'] == 'INCOMPLETE' and certificate['no_blind_or_formal_acceptance'] is True
assert certificate['complete_ring_remainder'] == []
assert certificate['source_freeze_sha256'] == pin(source_freeze)['sha256']
assert certificate['resource_policy_sha256'] == pin(ROOT.joinpath(REL, 'execution_policy.json'))['sha256']
full_binding = json.loads(FROZEN.joinpath(REL, 'checkpoints/full_map_v3_binding.json').read_bytes())
for name, key in [('check_exact_map.py', 'checker_sha256'), ('test_exact_map.py', 'test_sha256'),
                  ('exact_map_proof.md', 'proof_sha256'), ('exact_map_certificate.json', 'certificate_sha256')]:
    assert full_binding[key] == pin(FROZEN.joinpath(REL, name))['sha256']
assert full_binding['actual_receipt_sha256'] == pin(run.joinpath('receipt.json'))['sha256']

polynomial_lists = []


def walk(value, address='$'):
    if isinstance(value, dict):
        for key, child in value.items():
            walk(child, address + '.' + key)
    elif isinstance(value, list):
        if value and isinstance(value[0], dict) and set(value[0]) == {'exponents', 'coefficient'}:
            seen = []
            for row in value:
                assert set(row) == {'exponents', 'coefficient'}
                powers, coeff = row['exponents'], row['coefficient']
                assert type(coeff) is int and coeff != 0
                assert len(powers) == 10 and all(type(x) is int and x >= 0 for x in powers)
                assert powers[0] < 4 and powers[1] < 2 and powers[2] < 2 and powers[7] < 2
                assert all(powers[x] == 0 for x in (3, 4, 5, 8, 9))
                seen.append(tuple(powers))
            assert seen == sorted(set(seen))
            polynomial_lists.append({'address': address, 'terms': len(value)})
        else:
            for i, child in enumerate(value):
                walk(child, address + '[' + str(i) + ']')


walk(certificate)
fiber = certificate['special_fiber_checkpoint']
assert len(fiber['coprimality_chains']) == 6
for chain in fiber['coprimality_chains'].values():
    assert chain['terminal_nonzero_constant']
    assert all(row['exponents'][6] == 0 for row in chain['terminal_nonzero_constant'])
    assert all(step['multiplier'] for step in chain['steps'])
assert all(fiber['nonzero_witnesses'].values())
placement = fiber['placement_checkpoint']
assert placement['geometric_twist_triple_for_Xnew'] == ['Tplus', 'T0', 'Tminus']
assert set(placement['L_rational_square_class_representatives_for_Xnew']) == {'zero', 'one', 'lambda'}
for row in placement['L_rational_square_class_representatives_for_Xnew'].values():
    assert row['cleared_reconstruction_remainder'] == []
    assert all(row[k] for k in ('gamma', 'alpha_numerator', 'alpha_denominator', 'u_numerator', 'u_denominator'))
match = certificate['frozen_classification_match']
old = json.loads(ROOT.joinpath('research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/squareclass_rr_certificate.json').read_bytes())
assert match['historical_row_one_based'] == 42
assert match['historical_row'] == old['patterns']['4+2+0+0']['rows'][41]
assert match['historical_row']['RR_section_dimensions_0_1_lambda'] == [3, 1, 2]
assert match['historical_row']['infinity_empty_representative'] == [1, 2, 2, 1, 1, 1]

code = FROZEN.joinpath(REL, 'check_exact_map.py').read_text(encoding='utf-8')
syntax = ast.parse(code)
assert not any(isinstance(node, (ast.Div, ast.FloorDiv, ast.Mod)) for node in ast.walk(syntax))
test_syntax = ast.parse(FROZEN.joinpath(REL, 'test_exact_map.py').read_text(encoding='utf-8'))
test_names = [node.name for node in ast.walk(test_syntax) if isinstance(node, ast.FunctionDef) and node.name.startswith('test_')]
assert len(test_names) == 13

result = {
    'schema': 'RB_CM24_FULL_V3_INDEPENDENT_READ_EVIDENCE_V1',
    'status': 'READ_ONLY_BYTE_LOG_AND_SERIALIZATION_CHECKS_PASS',
    'started_at': START, 'finished_at': dt.datetime.now(dt.timezone.utc).isoformat(),
    'actual_argv': sys.orig_argv, 'collector_sha256': sha(Path(__file__).read_bytes()),
    'mathematical_execution_by_reviewer': False,
    'author_run_replay_or_tests_executed_by_reviewer': False,
    'publication': pin(PACKAGE.joinpath('publication.json')),
    'all_40_publication_files': all_file_pins,
    'original_7_plus_placement_5_source_pins': source_pins,
    'final_receipt': pin(run.joinpath('receipt.json')),
    'recorded_author_commands_and_logs_verified': receipt['commands'],
    'selected_source_archive_matches': True,
    'final_certificate_matches_primary_archive_and_stdout': True,
    'polynomial_serialization_only': {'nonempty_polynomial_lists': len(polynomial_lists),
        'total_serialized_terms_including_repeated_evidence': sum(x['terms'] for x in polynomial_lists),
        'all_sorted_unique_integer_normal_form_rows': True,
        'no_polynomial_identity_recomputed': True},
    'six_coprimality_receipts_terminal_nonzero_and_multipliers_present': True,
    'three_Xprime_square_class_reconstruction_records_present': True,
    'old_frozen_row_42_full_object_matches': True,
    'recorded_author_arithmetic': certificate['arithmetic'],
    'test_names_read_and_matching_actual_log': test_names,
    'mathematical_deductions_reviewed': 'See REVIEW.md; paper deductions are distinguished from author-program checks.',
    'proof_full_read': pin(FROZEN.joinpath(REL, 'exact_map_proof.md')),
    'checker_full_read': pin(FROZEN.joinpath(REL, 'check_exact_map.py')),
    'root_comparison_read_after_independent_derivation': pin(Path('D:/em/TEMP/rb-cm24-source-exposed-owner-review-20260909/review-complete-fibers-placement-v3.md')),
    'authority': 'Source-exposed peer paper/code review only; no formal Result, Driver disposition, claim or parent completion.'
}
target = OUT.joinpath('receipt.json')
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'status': result['status'], 'files': len(all_file_pins), 'source_pins': len(source_pins),
    'polynomial_structure': result['polynomial_serialization_only'], 'receipt': str(target), 'sha256': sha(target.read_bytes())}, indent=2))
