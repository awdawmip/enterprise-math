"""Byte-only strict q4 code/preparation restorer; never executes restored code."""
import argparse,base64,hashlib,json,zlib
from pathlib import Path,PurePosixPath

def unique(pairs):
    result={}
    for k,v in pairs:
        if k in result:raise ValueError('Duplicate JSON key')
        result[k]=v
    return result

def parse(raw):
    def nofloat(_):raise ValueError('Floating/nonfinite metadata')
    return json.loads(raw,object_pairs_hook=unique,parse_float=nofloat,parse_constant=nofloat)

def b64(text):
    raw=base64.b64decode(text,validate=True)
    if base64.b64encode(raw).decode()!=text:raise ValueError('Noncanonical Base64')
    return raw

def fingerprint(raw):
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
            'git_blob_sha1':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}

def restore(capsule_path,destination,expected_sha):
    outer_raw=Path(capsule_path).read_bytes()
    if hashlib.sha256(outer_raw).hexdigest()!=expected_sha:raise ValueError('Outer wholeSHA mismatch')
    outer=parse(outer_raw)
    if outer['schema']!='T6_Q4_LOCAL_IMPLEMENTATION_PREPARATION_LOSSLESS_BYTE_CONTAINER_V1':raise ValueError('Wrong schema')
    compressed=b64(outer['payload_base64'])
    if hashlib.sha256(compressed).hexdigest()!=outer['gzip_sha256']:raise ValueError('CompressedSHA')
    size=outer['container_bytes']
    if type(size) is not int or not 0<size<=64*1048576:raise ValueError('Decode length bound')
    stream=zlib.decompressobj(31);raw=stream.decompress(compressed,size+1)
    if len(raw)!=size or not stream.eof or stream.unused_data or stream.unconsumed_tail:
        raise ValueError('Length/CRC/singlegzip/EOF')
    if hashlib.sha256(raw).hexdigest()!=outer['container_sha256']:raise ValueError('ContainerSHA')
    files=parse(raw)['files'];pins={x['path']:x for x in outer['originals']}
    if len(pins)!=len(outer['originals']) or len(files)!=outer['original_count']:raise ValueError('Manifest inventory')
    members={}
    for row in files:
        name=row['path'];parts=PurePosixPath(name)
        if parts.is_absolute() or '\\' in name or any(x in ('','.','..') for x in name.split('/')):
            raise ValueError('Unsafe member path')
        if name in members or name not in pins:raise ValueError('Duplicate/unknown member')
        data=b64(row['content_base64'])
        if any(fingerprint(data)[k]!=pins[name][k] for k in ('bytes','sha256','git_blob_sha1')):
            raise ValueError('Member fullbytepin')
        members[name]=data
    if set(members)!=set(pins) or sum(map(len,members.values()))!=outer['original_bytes']:raise ValueError('Closure')
    dest=Path(destination)
    if dest.exists():raise ValueError('Exclusive fresh restore directory required')
    dest.mkdir(parents=True)
    for name,data in members.items():
        target=dest/name;target.parent.mkdir(parents=True,exist_ok=True)
        with target.open('xb') as handle:handle.write(data)
    return {'status':'PASS_ALL_ORIGINAL_BYTES','originals':len(members),'bytes':sum(map(len,members.values())),
            'code_execution':False,'scientific_execution':False,'native_Source_authority':False}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('capsule');parser.add_argument('destination')
    parser.add_argument('--expected-sha256',required=True);args=parser.parse_args()
    print(json.dumps(restore(args.capsule,args.destination,args.expected_sha256)))
