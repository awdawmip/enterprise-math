#!/usr/bin/env python3
"""Verify and recover the complete UTF-8 evidence from the Source container."""
import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('container', type=Path)
parser.add_argument('--output', type=Path)
args = parser.parse_args()
container = json.loads(args.container.read_text())
assert container['codec'] == 'gzip+base64-utf8-json'
raw = gzip.decompress(base64.b64decode(container['payload'], validate=True))
assert len(raw) == container['original_bytes']
assert hashlib.sha256(raw).hexdigest() == container['original_sha256']
bundle = json.loads(raw)
assert len(bundle['files']) == container['file_count']
pins = {row['path']: row for row in container['files']}
assert len(pins) == container['file_count']
seen = set()
for row in bundle['files']:
    path = Path(row['path'])
    assert not path.is_absolute() and '..' not in path.parts
    assert row['path'] not in seen
    seen.add(row['path'])
    data = row['content'].encode('utf-8')
    pin = pins[row['path']]
    assert len(data) == pin['bytes']
    assert hashlib.sha256(data).hexdigest() == pin['sha256']
    assert hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == pin['git_blob_sha1']
    if args.output:
        target = args.output / path
        assert not target.exists()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
assert seen == set(pins)
print(json.dumps({'complete_files_verified': len(seen), 'all_bytes_hashes_blobs_match': True}))
