"""Read already committed event members; never imports scientific code."""
from pathlib import Path
import gzip
import hashlib
import json
import sys

root = Path(sys.argv[1])
index = (root/'MEMBER_INDEX.jsonl').read_bytes().splitlines(keepends=True)
rows = [json.loads(line) for line in index if line.endswith(b'\n')]
selected = {}
for row in rows:
    if row['kind'] in ('adjacent_power_begin', 'adjacent_bit_end', 'signed_main_result', 'complete_result'):
        selected[row['kind']] = row
out = {'completed_members': len(rows), 'events': {}}
with (root/'EVIDENCE.jsonl.gz').open('rb') as stream:
    for kind, row in selected.items():
        stream.seek(row['offset'])
        packed = stream.read(row['compressed_bytes'])
        assert hashlib.sha256(packed).hexdigest() == row['compressed_sha256']
        raw = gzip.decompress(packed)
        assert hashlib.sha256(raw).hexdigest() == row['raw_sha256']
        event = json.loads(raw)
        assert event['sequence'] == row['sequence'] and event['kind'] == kind
        if kind == 'adjacent_power_begin':
            out['events'][kind] = {'bits': len(event['public_bits']), 'E': event['E']}
        elif kind == 'adjacent_bit_end':
            out['events'][kind] = {'completed_bits': event['bit_index']+1, 'pair': event['after']}
        else:
            out['events'][kind] = event
print(json.dumps(out, indent=2))
