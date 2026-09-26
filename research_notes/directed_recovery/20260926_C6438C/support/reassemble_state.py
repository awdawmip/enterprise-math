"""Reassemble the complete retained state from verified small GitHub blobs."""
from pathlib import Path
import gzip, hashlib, json
ROOT=Path(__file__).resolve().parent
m=json.loads((ROOT/'STATE_PARTS_MANIFEST.json').read_text(encoding='utf-8'))
parts=[]
for row in m['parts']:
    data=(ROOT/row['path']).read_bytes()
    if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256']:
        raise ValueError('state part differs: '+row['path'])
    parts.append(data)
data=b''.join(parts)
if len(data)!=m['bytes'] or hashlib.sha256(data).hexdigest()!=m['sha256']:
    raise ValueError('assembled state differs')
if hashlib.sha256(gzip.decompress(data)).hexdigest()!=m['uncompressed_sha256']:
    raise ValueError('uncompressed complete state differs')
target=ROOT/m['target']
if target.exists() and target.read_bytes()!=data:
    raise ValueError('refusing to overwrite a different existing state')
target.write_bytes(data)
print(json.dumps({'complete_state':str(target),'bytes':len(data),'sha256':m['sha256']}))
