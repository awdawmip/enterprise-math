"""Strict byte-only restoration of the frozen fair-mathematics capsule."""
import argparse, base64, hashlib, json, re, zlib
from pathlib import Path, PurePosixPath

def check(condition, message):
    if not condition: raise ValueError(message)

def obj(pairs):
    result = {}
    for k,v in pairs:
        check(k not in result, 'duplicate JSON key'); result[k]=v
    return result

def load(raw):
    return json.loads(raw.decode('utf-8'), object_pairs_hook=obj,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))

def b64(text):
    check(isinstance(text,str) and text.isascii(), 'base64 string')
    raw=base64.b64decode(text,validate=True)
    check(base64.b64encode(raw).decode()==text,'canonical base64'); return raw

def pin(raw):
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
            'git_blob_sha1':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}

def recover(capsule, output):
    raw=capsule.read_bytes(); check(len(raw)<=1<<20,'outer file size')
    a=load(raw); check(a['schema']=='FAIR_MATH_WHOLE_ORIGINALS_CAPSULE_V1','schema')
    check(a['codec']=='single-gzip-base64-json-binary-members','codec')
    compressed=b64(a['payload_base64']); check(len(compressed)==a['gzip_bytes'],'gzip size')
    check(hashlib.sha256(compressed).hexdigest()==a['gzip_sha256'],'gzip hash')
    size=a['inner_json_bytes']; check(type(size) is int and 0<size<=32<<20,'inner size')
    stream=zlib.decompressobj(16+zlib.MAX_WBITS)
    plain=stream.decompress(compressed,size+1)
    check(len(plain)<=size and not stream.unconsumed_tail,'decompression bound')
    plain+=stream.flush()
    check(stream.eof and not stream.unused_data and not stream.unconsumed_tail,'single gzip/CRC/EOF')
    check(len(plain)==size and hashlib.sha256(plain).hexdigest()==a['inner_json_sha256'],'inner pin')
    inner=load(plain); check(inner['schema']=='FAIR_MATH_WHOLE_BINARY_ORIGINALS_V1','inner schema')
    expected={p['path']:p for p in a['files']}; check(len(expected)==len(a['files']),'unique pins')
    check(len(inner['files'])==len(expected)==a['file_count'],'file count')
    seen=set(); total=0; result=[]
    for member in inner['files']:
        name=member['path']; path=PurePosixPath(name)
        check(not path.is_absolute() and str(path)==name and all(re.fullmatch(r'[A-Za-z0-9_.-]+',s) and s not in {'.','..'} for s in path.parts),'safe path')
        check(name not in seen and name in expected,'unique expected member');seen.add(name)
        meta={k:v for k,v in member.items() if k!='content_base64'}
        check(meta==expected[name],'whole member metadata')
        data=b64(member['content_base64']); actual=pin(data)
        check(all(actual[k]==meta[k] for k in actual),'whole byte pin')
        target=output/path;target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists(): check(target.read_bytes()==data,'existing byte conflict')
        else: target.write_bytes(data)
        total+=len(data);result.append(meta)
    check(seen==set(expected) and total==a['original_member_bytes'],'coverage/total')
    return {'capsule':str(capsule),'group':a['group'],'files':result,'file_count':len(result),'original_bytes':total,'math_executed':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('capsule',type=Path);p.add_argument('output',type=Path)
    args=p.parse_args();print(json.dumps(recover(args.capsule,args.output),ensure_ascii=False))
