"""Losslessly restore this genuine Driver's independent review evidence.

Usage: python unpack_t6_order2_driver_review_evidence.py PACK.json DEST
Optional --run-checker requires --source-root (all exact Source953 files in
repository-relative layout) and --old-q2-source-root (exact Sourcec406 files).
This never runs the scientific producer or its consumers.
"""
from pathlib import Path
import argparse,base64,gzip,hashlib,json,subprocess,sys

def require(value,message):
    if not value:raise ValueError(message)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pack',type=Path)
    parser.add_argument('destination',type=Path)
    parser.add_argument('--run-checker',action='store_true')
    parser.add_argument('--source-root',type=Path)
    parser.add_argument('--old-q2-source-root',type=Path)
    args=parser.parse_args()
    pack=json.loads(args.pack.read_text())
    require(pack['schema']=='T6_DRIVER_FULL272_INDEPENDENT_REVIEW_EVIDENCE_PACKED_V1','pack schema')
    raw=gzip.decompress(base64.b64decode(pack['payload'],validate=True))
    require(len(raw)==pack['uncompressed_json_bytes'] and hashlib.sha256(raw).hexdigest()
            ==pack['uncompressed_json_sha256'],'complete packed JSON bytes')
    body=json.loads(raw)
    pins={row['path']:row for row in pack['files']}
    require(len(pins)==len(body['files'])==pack['original_count'],'unique complete member list')
    total=0
    seen=set()
    args.destination.mkdir(parents=True,exist_ok=True)
    for member in body['files']:
        path=Path(member['path'])
        require(not path.is_absolute() and '..' not in path.parts,'safe relative member')
        require(member['path'] not in seen,'duplicate member')
        seen.add(member['path'])
        value=member['content'].encode()
        pin=pins[member['path']]
        require(len(value)==pin['bytes'] and hashlib.sha256(value).hexdigest()==pin['sha256']
                and hashlib.sha1(b'blob '+str(len(value)).encode()+b'\0'+value).hexdigest()
                ==pin['git_blob_sha1'],'exact original member bytes/hash/blob')
        target=args.destination/path
        target.parent.mkdir(parents=True,exist_ok=True)
        require(not target.exists() or target.read_bytes()==value,'refuse differing existing original')
        target.write_bytes(value)
        total+=len(value)
    require(total==pack['original_byte_total'],'complete original byte total')
    if args.run_checker:
        require(args.source_root is not None and args.old_q2_source_root is not None,
                'both exact scientific Source roots required')
        codes={'reviewer_order2_math_core.py':'569c130db1a3ed04be5e66cdd2f699a766b091fe340d5888a90c3252dcaf9f1a',
               'reviewer_order2_complete_source_check.py':'df119d83e1c081932e1a964d52b47474a4ef8546dd91fc0e882a1f3ef0dfd6ee'}
        for name,sha in codes.items():
            value=(args.pack.parent/name).read_bytes()
            require(hashlib.sha256(value).hexdigest()==sha,'exact own published checker')
            target=args.destination/name
            require(not target.exists() or target.read_bytes()==value,'refuse differing checker')
            target.write_bytes(value)
        subprocess.run([sys.executable,str(args.destination/'reviewer_order2_complete_source_check.py'),
                        '--source-root',str(args.source_root.resolve()),
                        '--old-q2-source-root',str(args.old_q2_source_root.resolve()),
                        '--old-q2-review-dir',str((args.destination/'prior-q2-review').resolve())],check=True)
        receipt=args.destination/'FULL272_INDEPENDENT_SOURCE_MATHEMATICAL_REVIEW_RECEIPT.json'
        require(hashlib.sha256(receipt.read_bytes()).hexdigest()==pins[receipt.name]['sha256'],
                'byte-identical complete independent mathematical receipt')
    print(f'LOSSLESS_OWN_REVIEW_PASS: {len(seen)} originals, {total} bytes; producer not executed')

if __name__=='__main__':main()
