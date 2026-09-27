"""Administrative byte packaging only; never import or rerun science."""
from pathlib import Path
import base64, gzip, hashlib, json, sys

BASE = Path(__file__).resolve().parent
PREFIX = 'research_notes/directed_recovery/20260927_C6438C/brc_native_tool_discovery/'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def prepare():
    files = ['EXPERIMENT_PLAN.md', 'native_relative_port.py', 'STARTUP_GUARD.json',
        'PARTIAL_COLLISION_CANDIDATE.md', 'WITNESS_QUOTIENT_CANDIDATE.md',
        'TRACE_OR_FACTOR_CANDIDATE.md', 'NATIVE_PORT_REVIEW.md',
        'RELATIVE_PORT_SUMMARY.json', 'SAVED_RECORD_AUDIT.json',
        'audit_saved_relative_port.py', 'read_native_port_review.py',
        'NATIVE_PORT_REVIEW_RECORD.json', 'RESULTS_AND_CONTINUE.md',
        'conic_transport/EXPERIMENT_PLAN.md', 'conic_transport/conic_transport.py',
        'conic_transport/STARTED.json', 'conic_transport/CONIC_SUMMARY.json',
        'conic_transport/CONIC_REVIEW.md',
        'trace_conflict/EXPERIMENT_PLAN.md', 'trace_conflict/trace_conflict.py',
        'trace_conflict/STARTED.json', 'trace_conflict/TRACE_SUMMARY.json',
        'GEOMETRIC_PROGRESS.md', 'GEOMETRY_CONIC_INTERFACE.md', 'HBW_BRIDGE_AUDIT.md',
        'package_evidence.py', 'restore_evidence.py']
    for name in ['GEOMETRIC_EXECUTION_REVIEW.md', 'read_geometric_records.py',
                 'GEOMETRIC_EXECUTION_REVIEW_RECORD.json', 'HBW_MARKED_SECTION_CONJUGACY.md']:
        if (BASE/name).is_file():
            files.append(name)
    compressed = []
    for filename in ['RELATIVE_PORT_RESULTS.json.gz', 'conic_transport/CONIC_RESULTS.json.gz',
                     'trace_conflict/TRACE_RESULTS.json.gz']:
        raw = (BASE/filename).read_bytes()
        unpacked = gzip.decompress(raw)
        encoded = base64.b64encode(raw).decode('ascii')
        chunks = []
        for offset in range(0, len(encoded), 80000):
            name = filename+'.part'+str(len(chunks))+'.b64'
            content = (encoded[offset:offset+80000]+'\n').encode()
            destination = BASE/name
            if destination.exists():
                assert destination.read_bytes() == content
            else:
                destination.write_bytes(content)
            files.append(name)
            chunks.append(name)
        compressed.append({'path': filename, 'gzip_bytes': len(raw), 'gzip_sha256': digest(raw),
                           'raw_bytes': len(unpacked), 'raw_sha256': digest(unpacked),
                           'base64_chunks_in_order': chunks})
    manifest = {'status': 'LOCAL_BYTE_PACKAGE_READY_NOT_YET_PUBLISHED',
                'source_ref_used': '2e81851d62c869a20b47ae083a24dde1a4c0420c',
                'remote_prefix': PREFIX, 'compressed_evidence': compressed,
                'files': []}
    for name in files:
        raw = (BASE/name).read_bytes()
        raw.decode('utf-8')
        manifest['files'].append({'path': name, 'bytes': len(raw), 'sha256': digest(raw),
            'git_blob_sha1': hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()})
    (BASE/'EVIDENCE_MANIFEST.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'file_count':len(files)+1, 'compressed_evidence':compressed},indent=2))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        prepare()
    else:
        manifest = json.loads((BASE/'EVIDENCE_MANIFEST.json').read_bytes())
        entries = manifest['files']+[{'path':'EVIDENCE_MANIFEST.json'}]
        if sys.argv[1] == 'list':
            print(json.dumps([PREFIX+e['path'] for e in entries]))
        else:
            entry = entries[int(sys.argv[1])]
            raw = (BASE/entry['path']).read_bytes()
            if 'sha256' in entry:
                assert digest(raw) == entry['sha256']
            print(json.dumps({'path':PREFIX+entry['path'], 'content':raw.decode('utf-8'),
                'git_blob_sha1':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}))
