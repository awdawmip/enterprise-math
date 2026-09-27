"""Restore and verify published bytes; this never executes scientific code."""
from pathlib import Path
import base64, gzip, hashlib, json

BASE = Path(__file__).resolve().parent
manifest = json.loads((BASE/'EVIDENCE_MANIFEST.json').read_bytes())
for entry in manifest['files']:
    raw = (BASE/entry['path']).read_bytes()
    assert len(raw) == entry['bytes']
    assert hashlib.sha256(raw).hexdigest() == entry['sha256'], entry['path']
for record in manifest['compressed_evidence']:
    encoded = ''.join((BASE/name).read_text(encoding='ascii').strip() for name in record['base64_chunks_in_order'])
    raw = base64.b64decode(encoded, validate=True)
    assert len(raw) == record['gzip_bytes']
    assert hashlib.sha256(raw).hexdigest() == record['gzip_sha256']
    uncompressed = gzip.decompress(raw)
    assert len(uncompressed) == record['raw_bytes']
    assert hashlib.sha256(uncompressed).hexdigest() == record['raw_sha256']
    destination = BASE/record['path']
    if destination.exists():
        assert destination.read_bytes() == raw
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('xb') as stream:
            stream.write(raw)
print(json.dumps({'status':'EXACT_BYTES_VERIFIED_NO_SCIENTIFIC_RERUN',
                  'files':len(manifest['files']), 'compressed_records':len(manifest['compressed_evidence'])}))
