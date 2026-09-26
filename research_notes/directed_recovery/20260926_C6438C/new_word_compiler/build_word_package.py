"""Byte-only packaging of complete evidence for connector-sized readbacks."""
from pathlib import Path
import gzip,hashlib,json

ROOT=Path(__file__).resolve().parent
CHUNK=190000
EXCLUDE={'WORD_MANIFEST.json'}

def metadata(path,raw):
    return {'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
            'git_blob_sha1':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}

def main():
    entries=[];artifacts=[]
    destination=ROOT/'byte_parts'
    destination.mkdir(exist_ok=True)
    for path in sorted(ROOT.iterdir()):
        if not path.is_file() or path.name in EXCLUDE:
            continue
        raw=path.read_bytes()
        if len(raw)<=CHUNK:
            entries.append(metadata(path.name,raw))
            continue
        if not path.name.endswith('.json.gz'):
            raise ValueError('Only complete compressed artifacts may be byte-split: '+path.name)
        parts=[]
        for i,start in enumerate(range(0,len(raw),CHUNK)):
            name=f'byte_parts/{path.name}.part{i:04d}'
            part=raw[start:start+CHUNK]
            (ROOT/name).write_bytes(part)
            row=metadata(name,part)
            entries.append(row);parts.append(row)
        joined=b''.join((ROOT/p['path']).read_bytes() for p in parts)
        assert joined==raw
        expanded=gzip.decompress(joined)
        artifacts.append({**metadata(path.name,raw),'parts':parts,
            'uncompressed_bytes':len(expanded),
            'uncompressed_sha256':hashlib.sha256(expanded).hexdigest(),
            'whole_local_file_excluded_from_remote_tree':True})
    result={'schema':'COMPLETE_NATIVE_WORD_PACKAGE_V1',
        'activity':'RA-CAAAC604CB513AEA8BBC1DFC',
        'status':'AUTHOR_EXECUTED_SHARED_CONTEXT_UNREVIEWED_NOT_ADMITTED',
        'root_files_and_exact_binary_parts':entries,'complete_split_artifacts':artifacts,
        'excluded_directories':['__pycache__','prior_4300_digit_cap','restored_artifacts'],
        'chunk_bytes':CHUNK,'byte_splitting_is_scientifically_lossless':True,
        'scope':'Complete evidence, not summaries substituted for full states; byte packaging is not a scientific execution'}
    (ROOT/'WORD_MANIFEST.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'files_without_manifest':len(entries),'split_artifacts':len(artifacts),
        'published_bytes_without_manifest':sum(f['bytes'] for f in entries)}))

if __name__=='__main__':main()
