"""Export a profile receipt only when every immutable prefix batch completed."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
from run import audit

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--directory', type=Path, required=True)
parser.add_argument('--work', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
bindings = json.loads((HERE/'input_bindings.json').read_text())
assert sha256((HERE/'front_sharded.cpp').read_bytes()).hexdigest() == bindings['derived_source_sha256']
for row in bindings['native_input_bindings']:
    assert sha256((args.work/row['path']).read_bytes()).hexdigest() == row['sha256'], row['path']
assert sha256((args.work/'manifest.json').read_bytes()).hexdigest() == bindings['profile_manifest_sha256']
result = audit(args.directory)
assert result['complete'] and result['found'] == 0
assert result['source_sha256'] == bindings['derived_source_sha256']
assert result['profile_manifest_sha256'] == bindings['profile_manifest_sha256']
counts = {(s, c): n for s, c, n in (tuple(map(int, item.split('-'))) for item in result['tag'].split('_'))}
assert sum(counts.values()) == 12 and sum(s*n for (s, c), n in counts.items()) == 125
assert sum(c*n for (s, c), n in counts.items()) == result['cost']
result['prefix_plan_sha256'] = sha256((args.directory/'plan.json').read_bytes()).hexdigest()
result['receipt_scope'] = 'All disjoint top-level prefix intervals; unchanged original native predicates and recursion'
args.output.write_text(json.dumps(result, sort_keys=True)+'\n')
print(json.dumps(result, sort_keys=True))
