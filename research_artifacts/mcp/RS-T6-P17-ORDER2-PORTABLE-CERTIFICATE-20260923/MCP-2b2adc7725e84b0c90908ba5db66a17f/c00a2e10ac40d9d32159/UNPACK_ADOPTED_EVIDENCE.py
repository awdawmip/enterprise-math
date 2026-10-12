#!/usr/bin/env python3
"""Restore exact Source-adopted UTF8 originals; no mathematical or native action."""
import argparse,base64,gzip,hashlib,json
from pathlib import Path
def need(c,m):
 if not c:raise ValueError(m)
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
a=argparse.ArgumentParser();a.add_argument('--pack',required=True);a.add_argument('--output',required=True);args=a.parse_args()
outer=json.loads(Path(args.pack).read_text(encoding='utf-8'))
need(outer['schema']=='T6_SOURCE_ADOPTED_EVIDENCE_GZIP_UTF8_CONTAINER_V1' and outer['codec']=='gzip+base64-utf8-json','Wrong codec')
raw=gzip.decompress(base64.b64decode(outer['payload'],validate=True))
need(len(raw)==outer['uncompressed_json_bytes'] and hashlib.sha256(raw).hexdigest()==outer['uncompressed_json_sha256'],'Payload byte pin mismatch')
payload=json.loads(raw.decode('utf-8'));manifest={x['path']:x for x in outer['files']}
need(len(manifest)==len(payload['files'])==outer['original_count'],'Original count mismatch')
target=Path(args.output);target.mkdir(parents=True,exist_ok=True);seen=set();total=0
for item in payload['files']:
 p=Path(item['path']);need(not p.is_absolute() and '..' not in p.parts and item['path'] not in seen,'Unsafe or duplicate member')
 seen.add(item['path']);b=item['content'].encode('utf-8');pin=manifest[item['path']]
 need(len(b)==pin['bytes'] and hashlib.sha256(b).hexdigest()==pin['sha256'] and blob(b)==pin['git_blob_sha1'],'Member byte pin mismatch')
 out=target/p;out.parent.mkdir(parents=True,exist_ok=True)
 if out.exists():need(out.read_bytes()==b,'Refuse to replace different existing bytes')
 else:
  with out.open('xb') as f:f.write(b)
 total+=len(b)
need(seen==set(manifest),'Member closure mismatch')
print(json.dumps({'status':'SOURCE_ADOPTED_ORIGINALS_FULL_BYTE_ROUNDTRIP_PASS','original_count':len(seen),'original_bytes':total,'scientific_execution_or_native_authority':False,'global_T6_complete':False}))

