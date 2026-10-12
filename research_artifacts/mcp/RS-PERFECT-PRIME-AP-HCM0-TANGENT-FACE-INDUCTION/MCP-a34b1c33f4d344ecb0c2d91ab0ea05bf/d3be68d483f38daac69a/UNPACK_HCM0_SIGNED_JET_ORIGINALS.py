#!/usr/bin/env python3
"""Restore complete Source originals with strict byte/hash/CRC validation."""
import argparse
import base64
import hashlib
import json
import pathlib
import zlib


def unique_object(pairs):
    result={}
    for key,value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: '+key)
        result[key]=value
    return result


def restore(capsule_path,output):
    capsule=json.loads(pathlib.Path(capsule_path).read_text(),object_pairs_hook=unique_object)
    if capsule['schema']!='HCM0_SIGNED_JET_COMPLETE_ORIGINALS_CAPSULE_V1':
        raise ValueError('unexpected capsule schema')
    compressed=base64.b64decode(capsule['payload_base64'],validate=True)
    if len(compressed)!=capsule['gzip_bytes']:
        raise ValueError('compressed length mismatch')
    if hashlib.sha256(compressed).hexdigest()!=capsule['gzip_sha256']:
        raise ValueError('compressed SHA mismatch')
    z=zlib.decompressobj(31)
    raw=z.decompress(compressed,capsule['inner_json_bytes']+1)+z.flush()
    if not z.eof or z.unused_data or z.unconsumed_tail:
        raise ValueError('gzip CRC/EOF or trailing member failure')
    if len(raw)!=capsule['inner_json_bytes'] or hashlib.sha256(raw).hexdigest()!=capsule['inner_json_sha256']:
        raise ValueError('inner byte/SHA mismatch')
    inner=json.loads(raw,object_pairs_hook=unique_object)
    if len(inner['files'])!=capsule['file_count']:
        raise ValueError('original count mismatch')
    dest=pathlib.Path(output)
    dest.mkdir(parents=True,exist_ok=True)
    seen=set()
    total=0
    restored=[]
    outer={f['path']:f for f in capsule['files']}
    if len(outer)!=capsule['file_count']:
        raise ValueError('duplicate manifest path')
    for f in inner['files']:
        p=pathlib.PurePosixPath(f['path'])
        if p.is_absolute() or '..' in p.parts or f['path'] in seen:
            raise ValueError('unsafe or duplicate member path')
        seen.add(f['path'])
        data=base64.b64decode(f['content_base64'],validate=True)
        sha=hashlib.sha256(data).hexdigest()
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        metadata={k:v for k,v in f.items() if k!='content_base64'}
        if metadata!=outer[f['path']] or len(data)!=f['bytes'] or sha!=f['sha256'] or blob!=f['git_blob_sha1']:
            raise ValueError('member metadata/byte/hash mismatch: '+f['path'])
        target=dest/f['path']
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() and target.read_bytes()!=data:
            raise ValueError('existing distinct original preserved: '+str(target))
        target.write_bytes(data)
        total+=len(data)
        restored.append(metadata)
    if total!=capsule['original_member_bytes']:
        raise ValueError('original byte total mismatch')
    return {'status':'PASS_COMPLETE_ORIGINAL_RESTORATION','files':restored,'original_bytes':total}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('capsule')
    parser.add_argument('output')
    args=parser.parse_args()
    print(json.dumps(restore(args.capsule,args.output),indent=2))
