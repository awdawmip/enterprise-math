"""Administrative exact-byte packaging only; no scientific imports or replay."""
from pathlib import Path
import base64, gzip, hashlib, json, sys

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
PREFIX='research_notes/directed_recovery/20260927_C6438C/brc_native_tool_discovery/'
MANIFEST=HERE/'HBW_EVIDENCE_MANIFEST.json'

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def prepare():
    assert not MANIFEST.exists(), 'Frozen manifest already exists'
    files=['HBW_MARKED_SECTION_CONJUGACY.md','AGGREGATE_HBW_SECTION_BRIDGE.md',
           'AGGREGATE_HBW_SECTION_REVIEW.md','AGGREGATE_WITNESS_PROBE_AUDIT.md',
           'HBW_AGGREGATE_PROGRESS.md',
           'hbw_marked_section/PLAN.md','hbw_marked_section/hbw_marked_section.py',
           'hbw_marked_section/PRE_RUN_REVIEW.md','hbw_marked_section/STARTUP_GUARD.json',
           'hbw_marked_section/STARTED.json','hbw_marked_section/HBW_MARKED_SUMMARY.json',
           'hbw_marked_section/HBW_MARKED_EXECUTION_REVIEW.md',
           'hbw_marked_section/read_hbw_marked_records.py',
           'hbw_marked_section/HBW_MARKED_RECORD_REVIEW.json',
           'hbw_marked_section/package_hbw.py']
    compressed=(HERE/'HBW_MARKED_RESULTS.json.gz').read_bytes()
    raw=gzip.decompress(compressed)
    assert digest(compressed)=='b782880a3786c0441d80bc4a7ba865dd4918f79d9482325c76edf9c0721cadd2'
    assert digest(raw)=='92306d3d74f39a2b5b6b6d499c901a8cffe8dbdcde946b48e01fd1ff48198a7d'
    encoded=base64.b64encode(compressed).decode('ascii')
    chunks=[]
    for offset in range(0,len(encoded),80000):
        name='hbw_marked_section/HBW_MARKED_RESULTS.json.gz.part'+str(len(chunks))+'.b64'
        content=(encoded[offset:offset+80000]+'\n').encode()
        with (BASE/name).open('xb') as stream:
            stream.write(content)
        chunks.append(name)
        files.append(name)
    manifest={'status':'FROZEN_LOCAL_BYTES_PUBLICATION_RECEIPT_SEPARATE',
              'prior_package_commit':'742f4c75566466751f1071015e0eb7d8249986e2',
              'remote_prefix':PREFIX,
              'compressed_evidence':{'path':'hbw_marked_section/HBW_MARKED_RESULTS.json.gz',
                 'gzip_bytes':len(compressed),'gzip_sha256':digest(compressed),
                 'raw_bytes':len(raw),'raw_sha256':digest(raw),
                 'base64_chunks_in_order':chunks},
              'files':[]}
    for name in files:
        value=(BASE/name).read_bytes()
        value.decode('utf-8')
        manifest['files'].append({'path':name,'bytes':len(value),'sha256':digest(value),'git_blob_sha1':blob(value)})
    with MANIFEST.open('x',encoding='utf-8',newline='\n') as stream:
        stream.write(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'files':len(files)+1,'manifest':str(MANIFEST)}))

def payloads():
    manifest=json.loads(MANIFEST.read_bytes())
    out=[]
    for entry in manifest['files']+[{'path':'hbw_marked_section/HBW_EVIDENCE_MANIFEST.json'}]:
        value=(BASE/entry['path']).read_bytes()
        if 'sha256' in entry:
            assert digest(value)==entry['sha256'] and blob(value)==entry['git_blob_sha1']
        out.append({'path':PREFIX+entry['path'],'content':value.decode('utf-8'),'git_blob_sha1':blob(value)})
    print(json.dumps(out))

if __name__=='__main__':
    prepare() if len(sys.argv)==1 else payloads()
