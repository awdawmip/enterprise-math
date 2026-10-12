"""Strict standalone byte-restorer; no mathematics or native operations."""
import base64,gzip,hashlib,json,pathlib,sys,zlib
def pairs(rows):
 d={}
 for k,v in rows:
  if k in d:raise ValueError('duplicate JSON key')
  d[k]=v
 return d
def loads(b):return json.loads(b,object_pairs_hook=pairs)
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+bytes([0])+b).hexdigest()
def b64(s):
 b=base64.b64decode(s,validate=True)
 if base64.b64encode(b).decode()!=s:raise ValueError('noncanonical base64')
 return b
def unpack(src,dst):
 c=loads(pathlib.Path(src).read_bytes())
 if c['schema']!='Q4_F9_COMPACT_COMPLETE_REVIEW_EVIDENCE_CAPSULE_V1' or c['encoding']!='SINGLE_GZIP_JSON_MEMBER_ARRAY_BASE64':raise ValueError('schema')
 if not 0<c['payload_bytes']<=4000000:raise ValueError('payload limit')
 z=zlib.decompressobj(31);p=z.decompress(b64(c['payload_gzip_base64']),c['payload_bytes']+1)
 if not z.eof or z.unused_data or z.unconsumed_tail or len(p)!=c['payload_bytes'] or sha(p)!=c['payload_sha256']:raise ValueError('gzip/length/hash')
 rows=loads(p); names=set(); out=pathlib.Path(dst); verified=[]
 if not isinstance(rows,list) or len(rows)!=c['member_count']:raise ValueError('member count')
 for r in rows:
  q=pathlib.PurePosixPath(r['path'])
  if q.is_absolute() or '..' in q.parts or not q.parts or str(q)!=r['path'] or r['path'] in names:raise ValueError('unsafe/duplicate path')
  names.add(r['path']); b=b64(r['content_base64'])
  if len(b)!=r['bytes'] or sha(b)!=r['sha256'] or blob(b)!=r['git_blob_sha1']:raise ValueError('member pin')
  verified.append((q,b))
 if sum(len(b) for q,b in verified)!=c['member_total_bytes']:raise ValueError('total')
 if out.exists() and any(out.iterdir()):raise ValueError('nonempty output')
 out.mkdir(parents=True,exist_ok=True)
 for q,b in verified:
  p=out.joinpath(*q.parts);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 print(json.dumps({'status':'PURE_BYTE_RESTORATION_PASS','members':len(verified),'bytes':c['member_total_bytes']}))
if __name__=='__main__':unpack(*sys.argv[1:])
