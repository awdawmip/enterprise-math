"""Lossless textual evidence transport; no scientific arithmetic is performed."""
from pathlib import Path
import argparse
import base64
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'readable_evidence'
UNITS = ('gram_research', 'point_queries', 'character_certificates', 'integrated_sampler')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def build():
    records = []
    for unit in UNITS:
        for path in sorted((ROOT/unit).glob('*.gz')):
            raw = path.read_bytes()
            relative = path.relative_to(ROOT).as_posix()
            chunks = []
            for i, start in enumerate(range(0, len(raw), 98304)):
                target = OUT / unit / (path.name+f'.part{i:03d}.b64.txt')
                target.parent.mkdir(parents=True, exist_ok=True)
                data = base64.b64encode(raw[start:start+98304])+b'\n'
                target.write_bytes(data)
                chunks.append({'index': i, 'path': target.relative_to(ROOT).as_posix(),
                               'text_sha256': sha(data), 'raw_bytes': min(98304,len(raw)-start)})
            records.append({'restore_path': relative, 'bytes':len(raw),
                            'sha256':sha(raw), 'chunks':chunks})
    index = {'schema':'LOSSLESS_BASE64_EVIDENCE_V1',
        'purpose':'Complete original gzip bytes; text files are not summaries.',
        'binary_files_are_restored_not_stored_in_git_tree':True, 'artifacts':records}
    (OUT/'INDEX.json').write_text(json.dumps(index,indent=2)+'\n',encoding='utf-8')
    return index


def restore(index):
    for item in index['artifacts']:
        raw = []
        for number, part in enumerate(item['chunks']):
            assert number == part['index']
            path = (ROOT/part['path']).resolve()
            path.relative_to(ROOT.resolve())
            data = path.read_bytes()
            assert sha(data) == part['text_sha256']
            decoded = base64.b64decode(data.strip(),validate=True)
            assert len(decoded) == part['raw_bytes']
            raw.append(decoded)
        data = b''.join(raw)
        assert len(data)==item['bytes'] and sha(data)==item['sha256']
        target = (ROOT/item['restore_path']).resolve()
        target.relative_to(ROOT.resolve())
        if target.exists():
            assert target.read_bytes()==data, 'refusing to replace nonmatching existing evidence'
        else:
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(data)
    return len(index['artifacts'])


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--restore',action='store_true')
    args=parser.parse_args()
    index=json.loads((OUT/'INDEX.json').read_text()) if args.restore else build()
    print(json.dumps({'artifacts_verified':restore(index),
                      'chunks':sum(len(i['chunks']) for i in index['artifacts'])}))
