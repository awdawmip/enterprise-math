"""Prepare local GK source records; no network or remote writes.

Only files/ is the proposed atomic publication. Existing catalog entries are
read from an explicit commit and retained verbatim as JSON values.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import types

HERE = Path(__file__).resolve().parent
REPO = Path('D:/knowledge/chatgpt-global-knowledge')
BASE = 'f44ed5959c92e6e088c61c102951d1ab2c5e98d4'
OUT = HERE / 'canonical_archive'

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def sha(data):
    return hashlib.sha256(data).hexdigest()

def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode('utf-8')

def write(relative, data):
    p = OUT / relative
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    return p

def comment_json(comment):
    match = re.search(r'```json\s*([\s\S]*?)\s*```', comment['body'])
    if not match:
        raise ValueError('actual JSON comment body missing')
    return json.loads(match.group(1))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ingested-at', required=True)
    args = parser.parse_args()
    dependencies = {}
    paths = ['sources/professional/catalog.json', 'sources/professional/policy.json',
             'tools/professional_query_cache.py',
             'knowledge/procedures/PROFESSIONAL_QUERY_CACHE_POLICY_20260919.md']
    snapshots = {}
    for path in paths:
        data = git('show', BASE+':'+path)
        snapshots[path] = data
        dependencies[path] = {'commit': BASE,
            'git_blob_sha1': git('rev-parse', BASE+':'+path).decode().strip(),
            'sha256': sha(data)}
        write('base_snapshot/'+path, data)
    module = types.ModuleType('canonical_cache_validator')
    exec(compile(snapshots['tools/professional_query_cache.py'].decode('utf-8'),
                 'canonical:tools/professional_query_cache.py', 'exec'), module.__dict__)
    policy = json.loads(snapshots['sources/professional/policy.json'])
    catalog = json.loads(snapshots['sources/professional/catalog.json'])
    original_entries = deepcopy(catalog['records'])
    result = json.loads((HERE/'KQB_2489_RESULT.json').read_text(encoding='utf-8'))
    request = json.loads((HERE/'KQB_2489_REQUEST.json').read_text(encoding='utf-8'))
    issue = json.loads((HERE/'KQB_2489_ISSUE_READBACK.json').read_text(encoding='utf-8'))
    assert json.loads(issue['structuredContent']['issue']['body']) == request
    assert sha(module.canonical(request['request'])) == result['github_request']['request_sha256']
    raw_readback = json.loads((HERE/'KQB_2489_RAW_READBACK.json').read_text(encoding='utf-8'))
    comments = raw_readback['structuredContent']['comments']
    intake = next(comment_json(c) for c in comments if c['id'] == 5850846653)
    returned = next(comment_json(c) for c in comments if c['id'] == 5850847340)
    assert returned == result
    rejected_readback = json.loads((HERE/'KQB_2488_REJECTION_READBACK.json').read_text(encoding='utf-8'))
    rejection = comment_json(rejected_readback['value']['structuredContent']['comments'][0])
    assert rejection['state'] == 'REJECTED' and rejection['detail'] == 'INVALID_TURN_ID'
    assert result['state'] == 'FAILED' and len(result['results']) == 2
    additions = []
    records = []
    published = []
    batch_context = {k: v for k, v in result.items() if k != 'results'}
    for job, child in zip(request['request']['jobs'], result['results']):
        source = child['source']
        assert source == job['db'] and child['query'] == job['q']
        assert child['state'] == 'PARTIAL' and len(child['records']) == 8
        extracted = deepcopy(child)
        removed = []
        for index, paper in enumerate(extracted['records']):
            if 'abstract' in paper:
                del paper['abstract']
                removed.append(f'source_result.records[{index}].abstract')
        payload = {'schema': 'KQB_METADATA_AND_STATUS_EXTRACTION_V1',
                   'extraction': {'omitted_fields': removed,
                      'scope': 'All returned bibliographic metadata and provider status/cost fields; abstracts omitted; no full paper text.'},
                   'submitted_request': request,
                   'intake_receipt': intake,
                   'batch_context': batch_context,
                   'source_result': extracted,
                   'preceding_rejected_intake': rejection}
        raw_bytes = encoded(payload)
        raw_digest = sha(raw_bytes)
        raw_path = f'sources/professional/raw/{source}/{raw_digest}.json'
        write('files/'+raw_path, raw_bytes)
        published.append(raw_path)
        rec_id = 'PQ-20260927-KQB2489-'+source.upper()+'-'+('CT-FOURIER-SPARSE' if source == 'arxiv' else 'QFT-MPS-ENTANGLEMENT')
        identity = {'source': source, 'operation': job['op'], 'subject': job['q'],
                    'parameters': {k: v for k, v in job.items() if k not in {'db','op','q'}},
                    'scope': 'current', 'version': None}
        observed = datetime.fromtimestamp(child['observed_at'], timezone.utc).isoformat()
        record = {'schema': module.SCHEMA, 'id': rec_id, 'identity': identity,
                  'category': 'literature_search',
                  'cache_key': module.cache_key(identity, 'literature_search'),
                  'observed_at': observed, 'ingested_at': args.ingested_at,
                  'expires_at': module.expiry(observed, 'literature_search', policy, 'CONFLICT'),
                  'state': 'CONFLICT',
                  'coverage': sorted(set().union(*(set(p) for p in extracted['records']))
                                     | {'batch_state','child_state','provider_call_accounting','intake_receipt'}),
                  'raw': {'path': raw_path, 'sha256': raw_digest,
                          'representation': 'provider_result_json', 'completeness': 'PARTIAL',
                          'extraction': 'JSON-field extraction of all eight bibliographic records, actual status/cost fields, request and intake receipts. Abstracts omitted; no paper full text saved. Stored-byte digest is not the provider HTTP-response digest.',
                          'redactions': []},
                  'evidence': {
                      'url': 'https://github.com/awdawmip/kimi-query-bridge/issues/2489#issuecomment-5850847340',
                      'batch_id': result['request_id'], 'request_id': child['request_id'],
                      'provider_request_id': child['provider_request_id'],
                      'source_status': child['state'], 'batch_status': result['state'],
                      'client_request_sha256': result['github_request']['request_sha256'],
                      'request_hash': child['request_hash'], 'batch_request_hash': result['request_hash'],
                      'original_observed_at_epoch': child['observed_at'],
                      'original_completed_at_epoch': child['completed_at'],
                      'original_batch_completed_at': result['completed_at'],
                      'coverage': child['coverage'],
                      'retrieval_verified': child['retrieval_verified'],
                      'provider_query_calls_confirmed': child['provider_query_calls_confirmed'],
                      'provider_query_calls_unknown': child['provider_query_calls_unknown'],
                      'billable_calls': child['billable_calls'],
                      'bridge_kimi_llm_calls': child['bridge_kimi_llm_calls'],
                      'upstream_internal_llm_calls': child['upstream_internal_llm_calls'],
                      'preceding_rejection_url': 'https://github.com/awdawmip/kimi-query-bridge/issues/2488#issuecomment-5850837213',
                      'preceding_rejection_status': 'REJECTED',
                      'preceding_rejection_detail': 'INVALID_TURN_ID',
                      'authority_level': 'PROVIDER_BIBLIOGRAPHIC_METADATA_NOT_FULL_TEXT_OR_INDEPENDENT_SCIENTIFIC_VALIDATION',
                      'state_note': 'Outer FAILED and child PARTIAL preserved. CONFLICT blocks clean-valid-cache reuse or silent within-lifetime requery; the returned metadata may be inspected with its stated coverage. Official primary papers were separately read for the project report.'},
                  'import_kind': 'CURRENT_TASK_BRIDGE_RESULT_ARCHIVE',
                  'projects': ['enterprise-math','kimi-query-bridge'], 'supersedes': []}
        module.validate_record(record, policy, OUT/'files')
        rec_path = f'sources/professional/records/{rec_id}.json'
        write('files/'+rec_path, encoded(record))
        published.append(rec_path)
        entry = {'cache_key': record['cache_key'], 'category': record['category'],
                 'id': rec_id, 'path': rec_path, 'subject': identity['subject']}
        additions.append(entry)
        catalog['records'].append(entry)
        records.append(record)
    assert catalog['records'][:-2] == original_entries
    assert len({x['id'] for x in catalog['records']}) == len(catalog['records'])
    catalog_path = 'sources/professional/catalog.json'
    write('files/'+catalog_path, encoded(catalog))
    published.append(catalog_path)
    decisions = []
    for record in records:
        need = {'professional_evidence_required': True, 'identity': record['identity'],
                'category': record['category'], 'required_fields': ['title','url']}
        decision = module.decide(need, records, policy, args.ingested_at, OUT/'files')
        assert decision['action'] == 'CONFLICT_NEEDS_INSTRUCTION' and not decision['provider_query']
        decisions.append(decision)
    files = []
    for path in published:
        data = (OUT/'files'/path).read_bytes()
        blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        files.append({'path': path, 'bytes': len(data), 'sha256': sha(data), 'git_blob_sha1': blob,
                      'base_blob_sha1': dependencies[catalog_path]['git_blob_sha1'] if path == catalog_path else None})
    manifest = {'schema': 'LOCAL_PROFESSIONAL_ARCHIVE_STAGE_V1',
                'status': 'LOCAL_VALIDATED_ARCHIVE_PENDING_REMOTE_PUBLICATION_AND_READBACK',
                'base_commit': BASE, 'dependencies': dependencies,
                'ingested_at': args.ingested_at, 'publication_files': files,
                'catalog_additions': additions, 'base_catalog_entries_retained': len(original_entries),
                'record_validation': 'PASS', 'same_query_gate_checks': decisions,
                'remote_writes_performed': False, 'provider_queries_performed_by_this_script': 0,
                'publication_rule': 'Publish all five files atomically; if catalog CAS base changed, merge only the two additions into the new catalog without replacing intervening entries; then validate and read back all hashes.',
                'generator_sha256': sha(Path(__file__).read_bytes())}
    write('ARCHIVE_MANIFEST.json', encoded(manifest))
    print(json.dumps(manifest, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
