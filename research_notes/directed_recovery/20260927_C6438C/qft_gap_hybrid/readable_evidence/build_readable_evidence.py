"""Lossless gzip transport; shared publication selection, no scientific execution."""
from pathlib import Path
import argparse
import base64
import hashlib
import json
from evidence_selection import ROOT, selected_sources, canonical_relative, validate_readable_index

OUT = ROOT/'readable_evidence'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def build():
    sources, history = selected_sources()
    records = []
    for path in sources:
        if path.suffix != '.gz':
            continue
        raw = path.read_bytes()
        relative = path.relative_to(ROOT).as_posix()
        chunks = []
        for i, start in enumerate(range(0, len(raw), 98304)):
            target = OUT/path.parent.relative_to(ROOT)/(path.name + f'.part{i:03d}.b64.txt')
            target.parent.mkdir(parents=True, exist_ok=True)
            data = base64.b64encode(raw[start:start+98304]) + b'\n'
            if target.exists() and target.read_bytes() != data:
                raise ValueError('Refusing to replace changed readable chunk; use a new package')
            target.write_bytes(data)
            chunks.append({'index': i, 'path': target.relative_to(ROOT).as_posix(),
                           'text_sha256': sha(data), 'raw_bytes': min(98304, len(raw)-start)})
        records.append({'restore_path': relative, 'bytes': len(raw),
                        'sha256': sha(raw), 'chunks': chunks})
    index = {'schema': 'LOSSLESS_BASE64_EVIDENCE_V1',
             'purpose': 'Complete exact original gzip bytes; not summaries.',
             'binary_files_are_restored_not_stored_in_git_tree': True,
             'historical_validation_disposition': history, 'artifacts': records}
    validate_readable_index(index, sources)
    (OUT/'INDEX.json').write_text(json.dumps(index, indent=2)+'\n', encoding='utf-8')
    return index


def restore(index):
    seen, seen_chunks = set(), set()
    for item in index['artifacts']:
        name = item['restore_path']
        if name in seen:
            raise ValueError('Duplicate restored artifact')
        seen.add(name)
        target = canonical_relative(name)
        raw = []
        for number, part in enumerate(item['chunks']):
            if number != part['index'] or part['path'] in seen_chunks:
                raise ValueError('Duplicate/out-of-order chunk')
            seen_chunks.add(part['path'])
            if not part['path'].startswith('readable_evidence/'):
                raise ValueError('Chunk outside readable evidence')
            data = canonical_relative(part['path']).read_bytes()
            decoded = base64.b64decode(data.strip(), validate=True)
            if sha(data) != part['text_sha256'] or len(decoded) != part['raw_bytes']:
                raise ValueError('Chunk digest/size mismatch')
            raw.append(decoded)
        data = b''.join(raw)
        if len(data) != item['bytes'] or sha(data) != item['sha256']:
            raise ValueError('Restored gzip digest/size mismatch')
        if target.exists() and target.read_bytes() != data:
            raise ValueError('Refusing to replace nonmatching original evidence')
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    return len(seen)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--restore', action='store_true')
    args = parser.parse_args()
    index = json.loads((OUT/'INDEX.json').read_bytes()) if args.restore else build()
    print(json.dumps({'artifacts_verified': restore(index),
                      'chunks': sum(len(i['chunks']) for i in index['artifacts'])}))
