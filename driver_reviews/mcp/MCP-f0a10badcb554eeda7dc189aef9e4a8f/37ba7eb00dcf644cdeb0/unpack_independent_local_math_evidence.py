"""Restore reviewer evidence bytes only. Does not execute mathematical code."""
import argparse,base64,hashlib,json,zlib
from pathlib import Path,PurePosixPath

def sha(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def unique(pairs):
 d={}
 for k,v in pairs:
  if k in d:raise ValueError('duplicate key')
  d[k]=v
 return d

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('capsule',type=Path);p.add_argument('destination',type=Path);args=p.parse_args()
 j=json.loads(args.capsule.read_bytes(),object_pairs_hook=unique)
 assert j['schema']=='Q3_GENUINE_INDEPENDENT_LOCAL_FROZEN_MATH_EVIDENCE_CAPSULE_V1'
 assert j['phase']=='LOCAL_FROZEN_PRE_PUBLICATION_AUDIT'
 assert j['native_math_acceptance'] is False
 gz=base64.b64decode(j['payload'],validate=True);assert sha(gz)==j['gzip_sha256']
 d=zlib.decompressobj(31);raw=d.decompress(gz,j['original_container_bytes']+1);assert not d.unconsumed_tail;raw+=d.flush();assert d.eof and not d.unused_data
 assert len(raw)==j['original_container_bytes'] and sha(raw)==j['original_container_sha256']
 inner=json.loads(raw,object_pairs_hook=unique);assert set(inner)=={'files'}
 expected={x['path']:x for x in j['files']};assert len(expected)==len(j['files'])==j['file_count'];seen=set()
 for r in inner['files']:
  assert set(r)=={'path','content_base64'};name=r['path'];q=PurePosixPath(name);assert not q.is_absolute() and '..' not in q.parts and '\\' not in name
  assert name in expected and name not in seen;seen.add(name)
  b=base64.b64decode(r['content_base64'],validate=True);pin=expected[name];assert len(b)==pin['bytes'] and sha(b)==pin['sha256'] and blob(b)==pin['git_blob_sha1']
  path=args.destination/name;path.parent.mkdir(parents=True,exist_ok=True);assert not path.exists();path.write_bytes(b)
 assert seen==set(expected)
 print(json.dumps({'status':'PASS_REVIEWER_EVIDENCE_BYTES_ONLY','members':len(seen),'native_math_acceptance':False}))
if __name__=='__main__':main()
