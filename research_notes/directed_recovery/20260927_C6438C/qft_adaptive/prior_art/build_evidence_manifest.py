"""Metadata-only readback binding and publication allowlist; no scientific execution.

No query, provider retry, GitHub write, or cache insertion occurs here.
The policy validator's literal PROVIDER_ERROR/ERROR mismatch is retained.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import types

HERE = Path(__file__).resolve().parent
GK = Path('D:/knowledge/chatgpt-global-knowledge')
REF = '06788df022dbd11720132b4ed0882ce8e41b3b8a'
CHECKED = '2026-09-27T03:00:57+00:00'


def read(name):
    return json.loads((HERE / name).read_bytes())


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(name, obj):
    (HERE / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2,
                                      allow_nan=False) + '\n', encoding='utf-8')


def module(path, name):
    source = subprocess.check_output(['git', '-C', str(GK), 'show', REF + ':' + path])
    mod = types.ModuleType(name)
    exec(compile(source.decode('utf-8'), REF + ':' + path, 'exec'), mod.__dict__)
    return mod, {'repository': 'awdawmip/chatgpt-global-knowledge', 'commit': REF,
                 'path': path, 'sha256': sha(source)}


def main():
    cache, cache_pin = module('tools/professional_query_cache.py', 'cache_metadata')
    validator, validator_pin = module('tools/professional_query_execution.py', 'execution_metadata')
    request, result = read('KQB_REQUEST.json'), read('KQB_RESULT.json')
    issue = read('KQB_ISSUE_READBACK.json')['structuredContent']['issue']
    assert json.loads(issue['body']) == request
    assert len(request['request']['jobs']) == len(result['results']) == 1
    job, child = request['request']['jobs'][0], result['results'][0]
    digest = sha(cache.canonical(request['request']))
    assert digest == result['github_request']['request_sha256']
    assert request['request']['id'] == result['request_id']
    assert request['conversation_id'] == result['github_request']['conversation_id']
    assert request['turn_id'] == result['github_request']['turn_id']
    assert job['db'] == child['source'] == 'arxiv'
    assert job['op'] == child['operation'] == 'paper_search'
    assert job['q'] == child['query']
    assert result['state'] == 'FAILED' and child['state'] == 'PROVIDER_ERROR'
    assert child['records'] == [] and child['retrieval_verified'] is False
    assert child['provider_query_calls_confirmed'] == 1
    assert 'provider_request_id' not in child
    comments = read('KQB_FINAL_READBACK.json')['structuredContent']['comments']

    def body(comment_id):
        comment = next(c for c in comments if c['id'] == comment_id)
        match = re.search(r'```json\s*([\s\S]*?)\s*```', comment['body'])
        return json.loads(match.group(1))

    intake = body(5852137656)
    assert body(5852140481) == result
    assert intake['request_id'] == result['request_id']
    assert intake['request_sha256'] == digest
    assert datetime.fromisoformat(CHECKED) >= datetime.fromisoformat(result['completed_at'])
    receipt = {
        'schema': validator.SCHEMA,
        'task_ref': 'sep27-qft-adaptive/prior_art/KQB2499',
        'task_started_at': issue['created_at'], 'checked_at': CHECKED,
        'timestamp_scope': 'Actual submission phase; cache preparation preceded this timestamp.',
        'provider': 'arxiv', 'operation': 'paper_search', 'transport': 'GITHUB_ISSUE',
        'cache_decision': 'QUERY_REQUIRED', 'outcome': 'PROVIDER_ERROR',
        'conversation_id': request['conversation_id'], 'turn_id': request['turn_id'],
        'batch_id': result['request_id'], 'request_sha256': digest,
        'request': request['request'],
        'attempts': [{'at': issue['created_at'], 'client': 'authorized GitHub connector create_issue',
                      'method': 'POST', 'endpoint_kind': 'GITHUB_REQUEST_ISSUE',
                      'request_issue_url': issue['url'], 'batch_id': result['request_id'],
                      'request_sha256': digest, 'evidence_ref': 'KQB_CREATED.json'}],
        'github_check': {'at': CHECKED, 'evidence_ref': 'KQB_FINAL_READBACK.json and KQB_READBACK_CLOCK.json',
                         'batch_id': result['request_id'], 'request_match': True,
                         'result_ref': issue['url'] + '#issuecomment-5852140481',
                         'provider': 'arxiv', 'operation': 'paper_search',
                         'job_state': child['state'], 'coverage_complete': False,
                         'raw_evidence_ref': 'KQB_RESULT.json'},
        'query_budget': {'mode': 'standard', 'shared_limit': 3, 'accepted_tasks': 1,
                         'provider_calls_confirmed': 1, 'retries': 0, 'pending_batches': 0,
                         'billable_calls': None},
        'readback_validation': {'result': 'PASS', 'scope': 'Exact request body/digest, issue, batch, turn, provider, query and full result comment match.'},
        'source_cache_written': False,
        'source_cache_reason': 'Failed provider call with no records; no provider_request_id supplied. Not a NO_HIT or success cache.',
        'authority': 'Failed retrieval provenance only; no scientific evidence or admission.',
        'validator_source': validator_pin,
    }
    try:
        validator.validate_execution(receipt, receipt['task_ref'])
        receipt['canonical_validator_result'] = 'PASS'
    except Exception as exc:
        receipt['canonical_validator_result'] = 'REJECTED_LITERAL_STATE_VOCABULARY'
        receipt['canonical_validator_error'] = str(exc)
        receipt['validator_exception_scope'] = 'Raw child state is retained verbatim. Current validator expects ERROR for outcome PROVIDER_ERROR. This is not mislabeled as a validator PASS.'
    write('KQB_EXECUTION_RECEIPT.json', receipt)
    write('KQB_READBACK_MATCH.json', {
        'schema': 'MATCHED_FAILED_PROVIDER_READBACK_V1', 'status': 'PASS',
        'scientific_execution': False, 'canonicalizer': cache_pin,
        'request_sha256': digest, 'issue': 2499,
        'intake_comment': 5852137656, 'result_comment': 5852140481,
        'batch_id': result['request_id'], 'child_id': child['request_id'],
        'batch_state': result['state'], 'child_state': child['state'],
        'provider_request_id': None, 'records': 0, 'confirmed_provider_calls': 1,
        'request_body_equal': True, 'result_comment_equal': True,
        'checked_at': CHECKED, 'retry_submitted': False,
    })
    external = []
    for path in [HERE.parent/'precision_theory'/'ADAPTIVE_NATIVE_PRECISION_INTERFACE.md',
                 HERE.parent/'nonzero_structure'/'ACTIVE_WINDOW_FLOOR_MOMENTS.md']:
        external.append({'path': str(path), 'sha256_at_read': sha(path.read_bytes()),
                         'read_scope': 'Complete symbolic text; no execution or admission.'})
    write('READING_EVIDENCE.json', {
        'schema': 'PRIMARY_READING_AND_SCOPE_EVIDENCE_V1', 'date_utc': '2026-09-27',
        'gk': {'canonical': REF, 'helper': 'PASS / LEASE_REUSED',
               'entrypoints': ['00_BOOTSTRAP.md', 'OPERATING_MANUAL.md', 'CODEX_SYNC_PROTOCOL.md'],
               'method': 'Shipped helper and immutable git reads; policy reuse and reread, not dirty worktree authority.'},
        'rp1': {'repository': 'awdawmip/enterprise-math',
                'commit': '3d2e729c4cce0f8df228795599266e4582be3505',
                'path': 'research_notes/HEARTBEAT_RP1_LOW_PRECISION_RIDGE_20260927.md',
                'blob': 'ce983db7cf6610c9400450f649ce189c6b2398ec',
                'status': 'COMPLETE_HEARTBEAT_READ', 'raw': 'RP1_READBACK.json',
                'underlying_bundle_proof': 'NOT_READ; listed bundle identifier did not resolve as EM Git commit during attempted proof fetch',
                'failure_raw': 'RP1_BUNDLE_COMMIT_REMOTE_UNAVAILABLE.json'},
        'mass_weighted': {'repository': 'awdawmip/enterprise-math',
                'commit': '951cc16cb09635fae9f93230d96030fdaa2035b3',
                'path': 'research_notes/directed_recovery/20260927_C6438C/qft_row_queries/point_queries/MASS_WEIGHTED_APPROXIMATION_BOUND.md',
                'blob': '32b746b30b9a0602715e44c662cae5c5a15044a0',
                'status': 'COMPLETE_NOTE_READ', 'raw': 'MASS_BOUND_READBACK.json'},
        'papers': [
            {'title': 'Asymptotic Analysis of Regular Sequences',
             'authors': ['Clemens Heuberger', 'Daniel Krenn'],
             'url': 'https://arxiv.org/pdf/1810.13178v5', 'version_date': '2025-11-29',
             'method': 'Official arXiv PDF opened and exact relevant text read via web tool',
             'sections_read': ['3.1 definition and linear representation', '3.2 Theorem A and hypotheses', '12.2 Lemma 12.2 and complete proof'],
             'printed_pages': ['5-7', '37'], 'whole_paper_read': False,
             'usable': 'Given finite digital representation: exact digit recurrence for summatory function.',
             'limit': 'Does not supply small AP representation or a certified finite mass-error bound without construction/constants.'},
            {'title': 'Time-uniform, nonparametric, nonasymptotic confidence sequences',
             'authors': ['Steven R. Howard', 'Aaditya Ramdas', 'Jon McAuliffe', 'Jasjeet Sekhon'],
             'url': 'https://arxiv.org/pdf/1810.08240',
             'version_status': 'Unversioned official PDF as retrieved; no unverified version number asserted.',
             'method': 'Official arXiv PDF opened and exact relevant text read via web tool',
             'sections_read': ['4.1 Theorem 4 and estimand/predictability definitions', '5 comparison warning for naive empirical-variance substitution'],
             'printed_pages': ['13-14', '18'], 'whole_paper_read': False,
             'usable': 'Bounded adapted data with predictable predictors admit time-uniform average-conditional-mean confidence bounds.',
             'limit': 'Changing policies do not have one stationary success parameter; theorem not a cheap quantum-error certificate.'}],
        'sibling_sources': external,
        'reused_query': {'issue': 2497, 'archive_commit': 'ed11167f4102d004e010643d74c00f0c658556a0',
                         'status': 'PARTIAL/CONFLICT retained', 'raw': 'REUSED_CACHE_READBACK.json'},
        'new_query': {'issue': 2499, 'status': 'PROVIDER_ERROR', 'records': 0,
                      'retrieval_verified': False, 'raw': 'KQB_FINAL_READBACK.json'},
        'scientific_execution': False, 'remote_archive_written_by_this_unit': False,
    })
    names = [
        'ACTIVE_WINDOW_REVIEW.md', 'ADAPTIVE_PRECISION_AND_AP_BRIDGES.md',
        'CACHE_DECISION.md', 'KQB_CREATED.json', 'KQB_EXECUTION_RECEIPT.json',
        'KQB_FINAL_READBACK.json', 'KQB_FIRST_READBACK.json', 'KQB_ISSUE_READBACK.json',
        'KQB_READBACK_CLOCK.json', 'KQB_READBACK_MATCH.json', 'KQB_REQUEST.json',
        'KQB_RESULT.json', 'MASS_BOUND_READBACK.json', 'READING_EVIDENCE.json',
        'REUSED_CACHE_READBACK.json', 'RP1_BUNDLE_COMMIT_REMOTE_UNAVAILABLE.json',
        'RP1_READBACK.json', 'build_evidence_manifest.py',
    ]
    write('PUBLICATION_MANIFEST.json', {
        'schema': 'FROZEN_LOCAL_PUBLICATION_ALLOWLIST_V1',
        'scope': 'This task directory only; no external dependencies or paper full texts repackaged.',
        'status': 'SYMBOLIC_AND_SOURCE_READING_ONLY / NOT_ADMITTED',
        'professional_query': 'One confirmed failed provider call, no retry or successful cache insertion.',
        'files': [{'path': name, 'bytes': (HERE/name).stat().st_size,
                   'sha256': sha((HERE/name).read_bytes())} for name in names],
        'manifest_not_self_hashed': True,
        'publication_file_count_including_this_manifest': len(names)+1,
    })
    print(json.dumps({'files': len(names)+1,
                      'readback_match': 'PASS',
                      'validator': receipt['canonical_validator_result'],
                      'validator_error': receipt.get('canonical_validator_error'),
                      'manifest_sha256': sha((HERE/'PUBLICATION_MANIFEST.json').read_bytes()),
                      'external': external}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
