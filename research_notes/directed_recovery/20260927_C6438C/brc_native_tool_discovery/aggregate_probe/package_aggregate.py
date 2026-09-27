"""Freeze exact administrative bytes; no scientific imports or reruns."""
from pathlib import Path
import base64,gzip,hashlib,json,sys
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
PREFIX='research_notes/directed_recovery/20260927_C6438C/brc_native_tool_discovery/'
MANIFEST=HERE/'AGGREGATE_EVIDENCE_MANIFEST.json'

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def prepare():
    assert not MANIFEST.exists(), 'Frozen manifest already exists'
    names=['LOCAL_SECTION_HIT_ANALYSIS.md','HIGH_DENSITY_SECTION_RESONANCE.md',
           'ARBITRARY_HORIZON_T1_BRIDGE.md','SYMBOLIC_FRONTIER_REVIEW.md',
           'AGGREGATE_THEORY_FRONTIER.md',
           'aggregate_probe/PLAN.md','aggregate_probe/aggregate_probe.py',
           'aggregate_probe/AGGREGATE_PRE_RUN_REVIEW.md','aggregate_probe/STARTED.json',
           'aggregate_probe/AGGREGATE_SUMMARY.json','aggregate_probe/RESULTS_AND_CONTINUE.md',
           'aggregate_probe/AGGREGATE_EXECUTION_REVIEW.md',
           'aggregate_probe/AGGREGATE_RECORD_REVIEW.json',
           'aggregate_probe/read_aggregate_records.py','aggregate_probe/package_aggregate.py']
    compressed=(HERE/'AGGREGATE_RESULTS.json.gz').read_bytes()
    raw=gzip.decompress(compressed)
    assert digest(compressed)=='fb518cb7ee42100b9043f43adee43e1ad47045abde6f8461dc3b729ca4272a4c'
    assert digest(raw)=='ad310010570d01a7edae1229289f2a8484f2e2ce5a581e274166522fe5fb687a'
    encoded=base64.b64encode(compressed).decode('ascii')
    chunks=[]
    for offset in range(0,len(encoded),80000):
        name='aggregate_probe/AGGREGATE_RESULTS.json.gz.part'+str(len(chunks))+'.b64'
        with (BASE/name).open('xb') as stream:
            stream.write((encoded[offset:offset+80000]+'\n').encode())
        names.append(name)
        chunks.append(name)
    manifest={'status':'FROZEN_LOCAL_BYTES_PUBLICATION_RECEIPT_SEPARATE',
              'prior_science_commit':'3f1d462c76aaf4e4b0b08d07582ad1a086b7120a',
              'remote_prefix':PREFIX,'files':[],
              'compressed_evidence':{'path':'aggregate_probe/AGGREGATE_RESULTS.json.gz',
                 'gzip_bytes':len(compressed),'gzip_sha256':digest(compressed),
                 'raw_bytes':len(raw),'raw_sha256':digest(raw),
                 'base64_chunks_in_order':chunks}}
    for name in names:
        value=(BASE/name).read_bytes()
        value.decode('utf-8')
        manifest['files'].append({'path':name,'bytes':len(value),'sha256':digest(value),'git_blob_sha1':blob(value)})
    with MANIFEST.open('x',encoding='utf-8',newline='\n') as stream:
        stream.write(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'file_count':len(names)+1,'manifest':str(MANIFEST)}))

def payloads():
    manifest=json.loads(MANIFEST.read_bytes())
    out=[]
    for entry in manifest['files']+[{'path':'aggregate_probe/AGGREGATE_EVIDENCE_MANIFEST.json'}]:
        value=(BASE/entry['path']).read_bytes()
        if 'sha256' in entry:
            assert digest(value)==entry['sha256'] and blob(value)==entry['git_blob_sha1']
        out.append({'path':PREFIX+entry['path'],'content':value.decode('utf-8'),'git_blob_sha1':blob(value)})
    print(json.dumps(out))

if __name__=='__main__':
    prepare() if len(sys.argv)==1 else payloads()
