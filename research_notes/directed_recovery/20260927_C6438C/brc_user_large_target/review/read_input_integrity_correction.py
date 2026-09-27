"""Stdlib-only v2 saved-record review and preservation of the v1 failure."""
from pathlib import Path
from collections import Counter
import ast
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / 'input_integrity_v2'
BASE = ROOT.parent / 'sep27-brc-native-tool-discovery/read_native_port_review.py'
BASE_PIN = 'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825'
sha = lambda value: hashlib.sha256(value).hexdigest()
packed = (V2 / 'INPUT_RESULTS.json.gz').read_bytes()
raw = gzip.decompress(packed)
data = json.loads(raw)
summary = json.loads((V2 / 'INPUT_SUMMARY.json').read_bytes())
started = json.loads((V2 / 'STARTED.json').read_bytes())
assert data['binding'] == started
assert (len(raw), sha(raw), len(packed), sha(packed)) == (
    summary['raw_bytes'], summary['raw_sha256'], summary['gzip_bytes'], summary['gzip_sha256'])
for name, field in [('check_inputs_native.py', 'source_sha256'), ('PLAN.md', 'plan_sha256')]:
    assert sha((V2 / name).read_bytes()) == started[field] == summary[field]
assert sha(Path(started['guard_path']).read_bytes()) == started['guard_sha256']
assert started['guard']['activity_allowed'] is True
assert started['guard']['persistence_allowed'] is True
assert started['guard']['sync_debt_events'] == []
for path, expected in data['native_source']['files'].items():
    assert sha(Path(path).read_bytes()) == expected
native = data['native_source']['native_arithmetic']
paths = {
    'lazy_modular': ROOT.parent / 'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
    'sparse_modular': ROOT.parent / 'sep26-shor-general/sparse/sparse_modular.py',
    'typed_integer_prechecks': ROOT.parent / 'sep26-shor-general/completion/typed_integer_prechecks.py',
}
for key, path in paths.items():
    assert sha(path.read_bytes()) == native['files_sha256'][key]
vendor = ROOT.parent / 'sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py'
assert sha(vendor.read_bytes()) == native['native_adder']['vendor']['sha256']
source = BASE.read_bytes()
assert sha(source) == BASE_PIN
selected = [node for node in ast.parse(source).body
            if isinstance(node, ast.FunctionDef) and node.name in ('trace', 'stream')]
assert len(selected) == 2
counts = Counter()
namespace = {'Counter': Counter, 'counts': counts, 'catalog': native['native_adder']['columns']}
exec(compile(ast.Module(body=selected, type_ignores=[]), str(BASE), 'exec'), namespace)
ops = data['arithmetic_operations']
assert [op['operation'] for op in ops] == ['multiply', 'compare', 'compare', 'divide']
namespace['stream'](ops, data['arithmetic_cost'])
inputs = started['inputs']
mul, complete, block, division = [row['trace'] for row in ops]
assert (mul['left'], mul['right'], mul['value']) == (inputs['supplied_p'], inputs['supplied_q'], data['product'])
assert data['product_operation'] == 0
for trace, key, right, index in ((complete, 'complete_comparison', inputs['N_complete'], 1),
                                  (block, 'block_comparison', inputs['displayed_block'], 2)):
    assert (trace['left'], trace['right']) == (data['product'], right)
    assert (trace['relation'], trace['low_difference'], index) == (
        data[key]['relation'], data[key]['low_difference'], data[key]['operation'])
assert (division['value'], division['modulus'], division['quotient'], division['remainder'], 3) == (
    inputs['N_complete'], data['product'], data['complete_division']['quotient'],
    data['complete_division']['remainder'], data['complete_division']['operation'])
assert data['product_equals_complete'] is (complete['relation'] == 0)
assert data['product_equals_block'] is (block['relation'] == 0)
assert data['complete_divisible_by_product'] is (division['remainder'] == 0)
for key in ('product', 'product_equals_complete', 'product_equals_block',
            'complete_divisible_by_product', 'complete_division', 'arithmetic_cost'):
    assert summary[key] == data[key]
assert len(data['all_native_records']) == summary['actual_native_calls'] == 1
assert data['all_native_records'][0]['entrypoint'] == 'recurrent_mass_power'
assert data['arithmetic_cost']['native_kernel_calls_delta'] == 0
actual = json.loads((V2 / 'ACTUAL_EXECUTION_TOOL_RESULT.json').read_bytes())
assert actual['result']['exit_code'] == 0
assert json.loads(actual['result']['output']) == summary
failure_file = ROOT / 'input_integrity/FAILED.json.gz'
failure = json.loads(gzip.decompress(failure_file.read_bytes()))
assert failure['stage'] == 'IMPORT_FROZEN_WRAPPERS'
assert failure['error_type'] == 'AttributeError'
assert "has no attribute 'old'" in failure['error']
assert not any(k in failure for k in ('native_source', 'arithmetic_operations', 'all_native_records'))
v1_actual = json.loads((ROOT / 'input_integrity/ACTUAL_EXECUTION_TOOL_RESULT.json').read_bytes())
assert v1_actual['result']['exit_code'] == 1
report = {
    'status': 'PASS_SAVED_RECORDS_ONLY_WITH_V1_REVIEW_CORRECTION',
    'counts': dict(counts), 'arithmetic_cost': data['arithmetic_cost'],
    'catalog_calls': len(data['all_native_records']),
    'v2_raw_sha256': sha(raw), 'v2_gzip_sha256': sha(packed),
    'v2_source_sha256': started['source_sha256'], 'v2_plan_sha256': started['plan_sha256'],
    'v1_failed_gzip_sha256': sha(failure_file.read_bytes()),
    'v1_stage': failure['stage'], 'v1_error': failure['error'],
    'reader_sha256': sha(Path(__file__).read_bytes()), 'reused_io_functions_sha256': BASE_PIN,
    'scope': 'Saved wiring/catalog lookup and administrative counts only. No scientific import, arithmetic oracle, rerun, primality or factoring claim.'
}
with (ROOT / 'review/INPUT_INTEGRITY_RECORD_CORRECTION.json').open('x', encoding='utf-8') as out:
    out.write(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
