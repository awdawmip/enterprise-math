"""Reconstruct the exact observed event snapshot; this grants no execution authority."""
from pathlib import Path
import argparse,gzip,hashlib,json

parser=argparse.ArgumentParser()
parser.add_argument('--repo-root',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
here=Path(__file__).resolve().parent
manifest=json.loads((here/'event_reconstruction.json').read_bytes())
archive=args.repo_root/manifest['base_archive_path']
compressed=archive.read_bytes()
assert 'sha256:'+hashlib.sha256(compressed).hexdigest()==manifest['base_archive_sha256']
raw=gzip.decompress(compressed)
assert 'sha256:'+hashlib.sha256(raw).hexdigest()==manifest['base_uncompressed_sha256']
base=json.loads(raw);assert len(base)==manifest['base_count']
increment=json.loads((here/manifest['incremental_path']).read_bytes())
assert len(increment)==manifest['incremental_count']
merged={item['id']:item for item in base}
for item in increment:merged[item['id']]=item
comments=sorted(merged.values(),key=lambda item:item['id'])
assert len(comments)==manifest['full_actual_count']
out=(json.dumps(comments,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
digest='sha256:'+hashlib.sha256(out).hexdigest()
assert digest==manifest['full_actual_sha256']
if args.output.exists():
    assert args.output.read_bytes()==out,'Refuse to overwrite different event bytes'
else:
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(out)
print(json.dumps({'state':'PASS','count':len(comments),'sha256':digest,'output':str(args.output),'fresh_after_recorded_observation':False,'execution_authorized':False},ensure_ascii=True))
