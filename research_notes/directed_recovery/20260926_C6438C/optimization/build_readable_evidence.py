"""Create connector-readable base64 chunks; restore exact gzip bytes without recomputation."""
from pathlib import Path
import argparse, base64, hashlib, json

ROOT=Path(__file__).resolve().parent
INDEX=ROOT/'readable_evidence'/'INDEX.json'
N=196608

def build():
    records=[]
    for p in sorted(ROOT.rglob('*.gz')):
        data=p.read_bytes()
        if len(data)<=1_000_000:
            continue
        target=INDEX.parent/p.parent.name/p.name
        target.mkdir(parents=True,exist_ok=True)
        parts=[]
        for i,start in enumerate(range(0,len(data),N)):
            raw=data[start:start+N]
            path=target/f'{i:04d}.b64.txt'
            path.write_text(base64.b64encode(raw).decode()+'\n',encoding='ascii')
            parts.append({'path':path.relative_to(ROOT).as_posix(),'bytes':len(raw),
                          'sha256':hashlib.sha256(raw).hexdigest()})
        records.append({'target':p.relative_to(ROOT).as_posix(),'bytes':len(data),
                        'sha256':hashlib.sha256(data).hexdigest(),'parts':parts})
    INDEX.write_text(json.dumps({'encoding':'base64 chunks, concatenated in listed order',
                                'files':records},indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'large_files':len(records),'parts':sum(len(r['parts']) for r in records)}))

def restore(output):
    for item in json.loads(INDEX.read_text(encoding='utf-8'))['files']:
        parts=[]
        for part in item['parts']:
            b=base64.b64decode((ROOT/part['path']).read_text(encoding='ascii').strip(),validate=True)
            assert len(b)==part['bytes'] and hashlib.sha256(b).hexdigest()==part['sha256']
            parts.append(b)
        data=b''.join(parts)
        assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256']
        p=output/item['target'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        print(json.dumps({'restored':str(p),'bytes':len(data),'sha256':item['sha256']}))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',action='store_true')
    parser.add_argument('--restore-to',type=Path)
    args=parser.parse_args()
    if args.build: build()
    elif args.restore_to: restore(args.restore_to)
    else: parser.error('choose --build or --restore-to')
