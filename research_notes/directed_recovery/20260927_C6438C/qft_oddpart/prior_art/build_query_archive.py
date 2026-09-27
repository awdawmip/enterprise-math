"""Validate actual query readback and prepare a two-file GK archive delta.

Metadata only: no provider request, publication or scientific computation.
The publisher must merge catalog_additions into its fresh current catalog.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import types

HERE = Path(__file__).resolve().parent
GK = Path('D:/knowledge/chatgpt-global-knowledge')
BASE = '06788df022dbd11720132b4ed0882ce8e41b3b8a'
OUT = HERE / 'canonical_archive'
ISSUE = 'https://github.com/awdawmip/kimi-query-bridge/issues/2497'
CHECKED = '2026-09-27T02:28:01+00:00'


def packed(x):
    return (json.dumps(x, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode('utf-8')


def digest(x):
    return hashlib.sha256(x).hexdigest()


def read(name):
    return json.loads((HERE/name).read_bytes())


def git(path):
    return subprocess.check_output(['git', '-C', str(GK), 'show', BASE+':'+path])


def write(path, value):
    target = HERE/path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(value if isinstance(value, bytes) else packed(value))


def main():
    snapshots = {}
    deps = {}
    for path in ('tools/professional_query_cache.py', 'tools/professional_query_execution.py',
                 'sources/professional/policy.json', 'sources/professional/catalog.json'):
        data = git(path)
        snapshots[path] = data
        deps[path] = {'commit': BASE, 'sha256': digest(data)}
        write('canonical_archive/base_snapshot/'+path, data)
    cache = types.ModuleType('current_cache_validator')
    execution = types.ModuleType('current_execution_validator')
    exec(compile(snapshots['tools/professional_query_cache.py'].decode(), 'canonical_cache', 'exec'), cache.__dict__)
    exec(compile(snapshots['tools/professional_query_execution.py'].decode(), 'canonical_execution', 'exec'), execution.__dict__)
    policy = json.loads(snapshots['sources/professional/policy.json'])
    catalog = json.loads(snapshots['sources/professional/catalog.json'])
    request, result = read('KQB_REQUEST.json'), read('KQB_RESULT.json')
    issue = read('KQB_ISSUE_READBACK.json')['structuredContent']['issue']
    assert json.loads(issue['body']) == request
    assert len(request['request']['jobs']) == len(result['results']) == 1
    job, child = request['request']['jobs'][0], result['results'][0]
    request_digest = digest(cache.canonical(request['request']))
    assert request_digest == result['github_request']['request_sha256']
    assert request['request']['id'] == result['request_id']
    for field in ('conversation_id', 'turn_id'):
        assert request[field] == result['github_request'][field]
    assert child['source'] == job['db'] == 'scholar'
    assert child['operation'] == job['op'] == 'paper_search'
    assert child['query'] == job['q']
    assert result['state'] == 'FAILED' and child['state'] == 'PARTIAL'
    assert child['coverage']['complete'] is False and len(child['records']) == 8
    comments = read('KQB_FINAL_READBACK.json')['structuredContent']['comments']
    def body(comment_id):
        comment = next(c for c in comments if c['id'] == comment_id)
        match = re.search(r'```json\s*([\s\S]*?)\s*```', comment['body'])
        return json.loads(match.group(1))
    intake = body(5851939513)
    assert body(5851940064) == result
    identity = {'source': job['db'], 'operation': job['op'], 'subject': job['q'],
        'parameters': {k:v for k,v in job.items() if k not in ('db','op','q')},
        'scope': 'current', 'version': None}
    need = {'professional_evidence_required': True, 'identity': identity,
            'category': 'literature_search', 'required_fields': ['title','url']}
    # Exact-identity gate across every catalog record at the read authority.
    # The later quartic record is separately routed as unrelated in CACHE_DECISION.md.
    old_records = [json.loads(git(entry['path'])) for entry in catalog['records']]
    before = cache.decide(need, old_records, policy, CHECKED)
    assert before['action'] == 'QUERY_REQUIRED'
    write('CACHE_GATE_VALIDATION.json', {'canonical': BASE, 'catalog_record_count': len(old_records),
        'need': need, 'exact_identity_gate': before,
        'scope_review': 'CACHE_DECISION.md; includes the later unrelated quartic PARTIAL archive',
        'validation_scope': 'Offline reproduction of the pre-submission catalog identity decision; this script sends no query.'})
    receipt = {'schema': execution.SCHEMA,
        'task_ref': 'sep27-qft-oddpart/prior_art/KQB2497',
        'task_started_at': issue['created_at'], 'checked_at': CHECKED,
        'timestamp_scope': 'The receipt starts at the actual submission phase; cache preparation preceded it.',
        'provider': 'scholar', 'operation': 'paper_search', 'transport': 'GITHUB_ISSUE',
        'cache_decision': 'QUERY_REQUIRED', 'outcome': 'PARTIAL_READBACK',
        'conversation_id': request['conversation_id'], 'turn_id': request['turn_id'],
        'batch_id': result['request_id'], 'request_sha256': request_digest,
        'request': request['request'],
        'attempts': [{'at': issue['created_at'], 'client': 'authorized GitHub connector create_issue',
            'method': 'POST', 'endpoint_kind': 'GITHUB_REQUEST_ISSUE',
            'request_issue_url': ISSUE, 'batch_id': result['request_id'],
            'request_sha256': request_digest, 'evidence_ref': 'KQB_CREATED.json'}],
        'github_check': {'at': CHECKED, 'evidence_ref': 'KQB_FINAL_READBACK.json and KQB_READBACK_CLOCK.json',
            'batch_id': result['request_id'], 'request_match': True,
            'result_ref': ISSUE+'#issuecomment-5851940064',
            'provider': 'scholar', 'operation': 'paper_search', 'job_state': 'PARTIAL',
            'coverage_complete': False, 'raw_evidence_ref': 'KQB_RESULT.json'},
        'query_budget': {'mode': 'standard', 'shared_limit': 3, 'accepted_tasks': 1,
                         'retries': 0, 'pending_batches': 0},
        'authority': 'Actual provider bibliography, not full paper text or independent scientific admission'}
    execution.validate_execution(receipt, receipt['task_ref'])
    receipt['local_validator_result'] = 'PASS'
    write('KQB_EXECUTION_RECEIPT.json', receipt)
    extracted = deepcopy(child)
    omitted = []
    for index, paper in enumerate(extracted['records']):
        if 'abstract' in paper:
            del paper['abstract']
            omitted.append(f'source_result.records[{index}].abstract')
    payload = {'schema': 'KQB_METADATA_AND_STATUS_EXTRACTION_V1',
        'extraction': {'omitted_fields': omitted,
            'scope': 'All eight bibliographic records and returned status/cost fields; abstract snippets omitted; no full paper text.'},
        'submitted_request': request, 'intake_receipt': intake,
        'batch_context': {k:v for k,v in result.items() if k != 'results'},
        'source_result': extracted}
    raw_bytes = packed(payload)
    raw_sha = digest(raw_bytes)
    raw_path = f'sources/professional/raw/scholar/{raw_sha}.json'
    write('canonical_archive/files/'+raw_path, raw_bytes)
    rec_id = 'PQ-20260927-KQB2497-SCHOLAR-SHOR-DECISION-DIAGRAM'
    observed = datetime.fromtimestamp(child['observed_at'], timezone.utc).isoformat()
    record = {'schema': cache.SCHEMA, 'id': rec_id, 'identity': identity,
        'category': 'literature_search', 'cache_key': cache.cache_key(identity, 'literature_search'),
        'observed_at': observed, 'ingested_at': CHECKED,
        'expires_at': cache.expiry(observed, 'literature_search', policy, 'CONFLICT'),
        'state': 'CONFLICT',
        'coverage': sorted(set().union(*(set(p) for p in extracted['records'])) |
            {'batch_state','child_state','provider_call_accounting','intake_receipt'}),
        'raw': {'path': raw_path, 'sha256': raw_sha, 'representation': 'provider_result_json',
            'completeness': 'PARTIAL', 'redactions': [],
            'extraction': 'Exact JSON-field extraction of metadata/status/cost/request/intake; abstracts omitted. Stored-byte hash is distinct from provider HTTP raw hash.'},
        'evidence': {'url': ISSUE+'#issuecomment-5851940064',
            'batch_id': result['request_id'], 'request_id': child['request_id'],
            'provider_request_id': child['provider_request_id'],
            'source_status': child['state'], 'batch_status': result['state'],
            'client_request_sha256': request_digest, 'request_hash': child['request_hash'],
            'batch_request_hash': result['request_hash'],
            'original_observed_at_epoch': child['observed_at'],
            'original_completed_at_epoch': child['completed_at'],
            'original_batch_completed_at': result['completed_at'],
            'coverage': child['coverage'], 'retrieval_verified': child['retrieval_verified'],
            'provider_raw_file_sha256': child['raw_file_sha256'],
            'provider_raw_tool_response_sha256': child['raw_tool_response_sha256'],
            'provider_query_calls_confirmed': child['provider_query_calls_confirmed'],
            'provider_query_calls_unknown': child['provider_query_calls_unknown'],
            'billable_calls': child['billable_calls'],
            'bridge_kimi_llm_calls': child['bridge_kimi_llm_calls'],
            'upstream_internal_llm_calls': child['upstream_internal_llm_calls'],
            'authority_level': 'PROVIDER_BIBLIOGRAPHIC_METADATA_NOT_FULL_TEXT',
            'state_note': 'Outer FAILED/child PARTIAL preserved; not NO_HIT, not a clean VALID complete cache. No same-query silent refresh.'},
        'import_kind': 'CURRENT_TASK_BRIDGE_RESULT_ARCHIVE',
        'projects': ['enterprise-math','kimi-query-bridge'], 'supersedes': []}
    cache.validate_record(record, policy, OUT/'files')
    rec_path = f'sources/professional/records/{rec_id}.json'
    write('canonical_archive/files/'+rec_path, record)
    after = cache.decide(need, [record], policy, CHECKED, OUT/'files')
    assert after['action'] == 'CONFLICT_NEEDS_INSTRUCTION' and not after['provider_query']
    additions = [{'cache_key': record['cache_key'], 'category': record['category'],
        'id': rec_id, 'path': rec_path, 'subject': identity['subject']}]
    files = []
    for path in (raw_path, rec_path):
        data = (OUT/'files'/path).read_bytes()
        files.append({'path': path, 'bytes': len(data), 'sha256': digest(data),
            'git_blob_sha1': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()})
    manifest = {'schema': 'LOCAL_PROFESSIONAL_ARCHIVE_DELTA_V1',
        'status': 'LOCAL_VALIDATED_PENDING_CANONICAL_PUBLICATION_AND_READBACK',
        'authority_base': BASE, 'dependencies': deps, 'ingested_at': CHECKED,
        'publication_files': files, 'catalog_additions': additions,
        'catalog_full_replacement_included': False,
        'record_validation': 'PASS', 'execution_validation': 'PASS', 'same_query_gate_check': after,
        'remote_writes_performed_by_script': False, 'provider_queries_performed_by_script': 0,
        'publication_rule': 'Publish both files and merge this one catalog entry into the latest catalog atomically; retain all intervening entries including KQB2495. Read back hashes before claiming ARCHIVED_VERIFIED.',
        'generator_sha256': digest(Path(__file__).read_bytes())}
    write('canonical_archive/ARCHIVE_MANIFEST.json', manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
