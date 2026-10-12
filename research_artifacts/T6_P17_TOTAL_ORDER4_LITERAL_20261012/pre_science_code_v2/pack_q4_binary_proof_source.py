"""Lossless byte-only converter for a future genuine binary proof, not a census.

All raw proof bytes survive; completeness is never inferred by this packer.
Input is already Source-adopted separately and is referenced, not duplicated.
"""
import argparse,base64,hashlib,json
from pathlib import Path
from q4_dfs_wire import header
from order4_exact_math_and_input import COMMON_SHA,INPUT_SHA

def pins(raw):
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
            'git_blob_sha1':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}

def json_bytes(value):return (json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()

def pack(binary,destination):
    raw=Path(binary).read_bytes()
    if raw[:76]!=header(COMMON_SHA,INPUT_SHA) or not 76<len(raw)<=1881352:
        raise ValueError('Wrong header or unjustified binary-size ceiling')
    dest=Path(destination)
    if dest.exists():raise ValueError('Refuse to overwrite a prior custody packet')
    dest.mkdir(parents=True)
    source_pin=pins(raw);encoded=base64.b64encode(raw).decode('ascii')
    pieces=[encoded[i:i+900000] for i in range(0,len(encoded),900000)]
    rows=[];offset=0
    for i,payload in enumerate(pieces):
        name=f'Q4_EXACT_DFS_BINARY_SOURCE_PART_{i+1:02}_OF_{len(pieces):02}.json'
        part={'schema':'T6_Q4_BINARY_PROOF_LOSSLESS_SOURCE_PART_V1','part_index':i,'part_count':len(pieces),
              'raw_sha256':source_pin['sha256'],'payload_base64':payload}
        data=json_bytes(part)
        if len(data)>1048576:raise ValueError('Outer file cap exceeded')
        (dest/name).write_bytes(data)
        rows.append({'path':name,**pins(data),'base64_offset':offset,'base64_characters':len(payload)})
        offset+=len(payload)
    manifest={'schema':'T6_Q4_BINARY_PROOF_LOSSLESS_SOURCE_MANIFEST_V1','proof_encoding':'T6Q4DFS1',
        'scope_status':'UNVERIFIED_BY_BYTE_PACKER','raw_bytes':len(raw),'raw_sha256':source_pin['sha256'],
        'raw_git_blob_sha1':source_pin['git_blob_sha1'],'compression':'none',
        'encoded_bytes':len(raw),'encoded_sha256':source_pin['sha256'],
        'base64_characters':len(encoded),'part_count':len(rows),'parts':rows,
        'common_sha256':COMMON_SHA,'ordered_input_sha256':INPUT_SHA,'case_count':30992}
    data=json_bytes(manifest)
    (dest/'Q4_EXACT_DFS_BINARY_SOURCE_MANIFEST.json').write_bytes(data)
    assert base64.b64decode(''.join(pieces),validate=True)==raw
    return {'manifest':pins(data),'part_count':len(rows),'parts':rows,'raw_original':source_pin,
            'whole_raw_roundtrip':True,'whole_custody_outer_bytes':sum(r['bytes'] for r in rows)+len(data),
            'mathematical_complete_proof_asserted':False,'scientific_execution':False}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--pack',action='store_true')
    parser.add_argument('--binary');parser.add_argument('--output');args=parser.parse_args()
    if not args.pack:print(json.dumps({'status':'LOCAL_CODEC_NO_ACTUAL_PROOF'}));return
    if not args.binary or not args.output:parser.error('Explicit binary and new output required')
    print(json.dumps(pack(args.binary,args.output)))

if __name__=='__main__':main()
