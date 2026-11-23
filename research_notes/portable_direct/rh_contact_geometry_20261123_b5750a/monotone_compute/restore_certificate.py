#!/usr/bin/env python3
"""Restore the exact large JSON certificate from its verified Source chunks."""
from pathlib import Path
import base64
import hashlib
import json
import lzma


def main():
    root = Path(__file__).resolve().parent
    metadata = json.loads((root / 'certificate_storage/ENCODING.json').read_text())
    chunks = []
    for row in metadata['parts']:
        data = (root / row['path']).read_bytes()
        assert len(data) == row['bytes']
        assert hashlib.sha256(data).hexdigest() == row['sha256']
        chunks.append(data)
    compressed = base64.b64decode(b''.join(chunks), validate=True)
    assert len(compressed) == metadata['compressed_bytes']
    assert hashlib.sha256(compressed).hexdigest() == metadata['compressed_sha256']
    data = lzma.decompress(compressed)
    assert len(data) == metadata['raw_bytes']
    assert hashlib.sha256(data).hexdigest() == metadata['raw_sha256']
    output = root / metadata['output_name']
    if output.exists():
        assert output.read_bytes() == data, 'Existing file differs; preserve it before restoring.'
        status = 'EXISTING_BYTES_VERIFIED'
    else:
        output.write_bytes(data)
        status = 'RESTORED_AND_VERIFIED'
    print(json.dumps({'status': status, 'path': str(output), 'bytes': len(data),
                      'sha256': metadata['raw_sha256']}))


if __name__ == '__main__':
    main()
