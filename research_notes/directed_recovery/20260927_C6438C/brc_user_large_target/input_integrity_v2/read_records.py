"""Read saved native receipts only; no scientific imports or arithmetic rerun."""
from pathlib import Path
from collections import Counter
import ast
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[1] / 'sep27-brc-native-tool-discovery/read_native_port_review.py'
PIN = 'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825'
sha = lambda value: hashlib.sha256(value).hexdigest()
packed = (ROOT/'INPUT_RESULTS.json.gz').read_bytes()
raw = gzip.decompress(packed)
data = json.loads(raw)
summary = json.loads((ROOT/'INPUT_SUMMARY.json').read_bytes())
assert sha(packed) == summary['gzip_sha256'] and sha(raw) == summary['raw_sha256']
assert len(raw) == summary['raw_bytes'] and len(packed) == summary['gzip_bytes']
assert sha((ROOT/'check_inputs_native.py').read_bytes()) == summary['source_sha256']
assert sha((ROOT/'PLAN.md').read_bytes()) == summary['plan_sha256']
source = SOURCE.read_bytes()
assert sha(source) == PIN
tree = ast.parse(source)
selected = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in ('trace', 'stream')]
assert len(selected) == 2
counts = Counter()
catalog = data['native_source']['native_arithmetic']['native_adder']['columns']
namespace = {'Counter': Counter, 'counts': counts, 'catalog': catalog}
exec(compile(ast.Module(body=selected, type_ignores=[]), str(SOURCE), 'exec'), namespace)
ops = data['arithmetic_operations']
assert [op['operation'] for op in ops] == ['multiply', 'compare', 'compare', 'divide']
namespace['stream'](ops, data['arithmetic_cost'])
inputs = data['binding']['inputs']
mul, full, block, div = [op['trace'] for op in ops]
assert (mul['left'], mul['right'], mul['value']) == (inputs['supplied_p'], inputs['supplied_q'], data['product'])
assert (full['left'], full['right'], full['relation']) == (data['product'], inputs['N_complete'], data['complete_comparison']['relation'])
assert (block['left'], block['right'], block['relation']) == (data['product'], inputs['displayed_block'], data['block_comparison']['relation'])
assert (div['value'], div['modulus'], div['quotient'], div['remainder']) == (inputs['N_complete'], data['product'], data['complete_division']['quotient'], data['complete_division']['remainder'])
for key in ('product', 'product_equals_complete', 'product_equals_block', 'complete_divisible_by_product', 'complete_division', 'arithmetic_cost'):
    assert summary[key] == data[key]
actual = json.loads((ROOT/'ACTUAL_EXECUTION_TOOL_RESULT.json').read_bytes())
assert actual['result']['exit_code'] == 0 and json.loads(actual['result']['output']) == summary
review = {'status': 'PASS_SAVED_RECORDS_ONLY', 'counts': dict(counts), 'raw_sha256': sha(raw), 'reader_source_sha256': sha(Path(__file__).read_bytes()), 'bound_reader_sha256': PIN, 'scope': 'All four native operation traces and exact input/output links; no primality or factoring claim; no scientific rerun'}
with (ROOT/'RECORD_REVIEW.json').open('x', encoding='utf-8') as stream:
    stream.write(json.dumps(review, indent=2)+'\n')
print(json.dumps(review, indent=2))
