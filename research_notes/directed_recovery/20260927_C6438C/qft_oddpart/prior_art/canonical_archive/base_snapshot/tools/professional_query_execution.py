"""Check a source-bound execution receipt; no network or server side effects.

This validates structure and consistency, not the truth of supplied tool evidence.
Callers must bind evidence_ref to actual current-task tool output. Never store tickets.
"""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
import re
from typing import Any
from uuid import UUID

SCHEMA = 'PROFESSIONAL_QUERY_EXECUTION_RECEIPT_V1'
BLOCKERS = {'USER_FORBIDS_QUERY', 'AUTHORIZATION_MISSING', 'NO_VALID_TICKET',
            'UNSUPPORTED_OPERATION', 'CURRENT_QUOTA_LIMIT', 'NO_AVAILABLE_TOOL',
            'PLATFORM_PROHIBITION', 'CURRENT_CACHE_GAP', 'CURRENT_CACHE_CONFLICT',
            'CURRENT_CACHE_RECOVERY_REQUIRED', 'IDENTITY_UNRESOLVED'}
CACHE_BLOCKER_GATES = {'CURRENT_CACHE_GAP':'GAP_NEEDS_INSTRUCTION',
                       'CURRENT_CACHE_CONFLICT':'CONFLICT_NEEDS_INSTRUCTION',
                       'CURRENT_CACHE_RECOVERY_REQUIRED':'RECOVER_STORED_SOURCE',
                       'IDENTITY_UNRESOLVED':'RESOLVE_IDENTITY'}


def _text(x: Any, field: str) -> str:
    if not isinstance(x, str) or not x.strip():
        raise ValueError('Missing execution evidence: ' + field)
    if re.search(r'[?&]t=|Bearer\s+|github_pat_|ghp_', x):
        raise ValueError('Do not persist credentials in receipts')
    return x


def _time(x: Any) -> datetime:
    d = datetime.fromisoformat(_text(x, 'timestamp').replace('Z', '+00:00'))
    if d.tzinfo is None:
        raise ValueError('Execution timestamps require timezone')
    return d.astimezone(timezone.utc)


def validate_execution(r: dict[str, Any], task_ref: str | None = None) -> None:
    if not isinstance(r, dict) or r.get('schema') != SCHEMA:
        raise ValueError('Current task needs an execution receipt, not a plan')
    for name in ('task_ref', 'provider', 'operation', 'cache_decision', 'outcome'):
        _text(r.get(name), name)
    if task_ref is not None and r['task_ref'] != task_ref:
        raise ValueError('Receipt belongs to another task')
    started, checked = _time(r.get('task_started_at')), _time(r.get('checked_at'))
    if checked < started:
        raise ValueError('Check precedes current task')
    outcome = r['outcome']
    if outcome == 'CACHE_REUSED':
        c = r.get('cache', {})
        if r['cache_decision'] not in {'REUSED_VALID_CACHE', 'REUSED_NEGATIVE_CACHE'}:
            raise ValueError('Cache reuse needs a matching cache-gate decision')
        for k in ('record_ref', 'raw_ref', 'validation_evidence_ref'):
            _text(c.get(k), k)
        if c.get('representation') != 'provider_result_json' or c.get('provider') != r['provider']:
            raise ValueError('Public sources/analysis are not dedicated-provider cache')
        if c.get('scope_match') is not True:
            raise ValueError('Cache scope must match')
        if not started <= _time(c.get('validated_at')) <= checked:
            raise ValueError('Revalidate actual cache in current task')
        if _time(c.get('observed_at')) > checked:
            raise ValueError('Future cache observation')
        if c.get('expires_at') is None:
            if c.get('scope') != 'fixed_version' or not c.get('version'):
                raise ValueError('Timeless cache requires fixed version')
        elif _time(c['expires_at']) <= checked:
            raise ValueError('Cache is expired')
        if r.get('attempts'):
            raise ValueError('Do not claim cache-only reuse after new submission')
        return
    if outcome == 'BLOCKED_BEFORE_SUBMISSION':
        b = r.get('blocker', {})
        if b.get('code') not in BLOCKERS:
            raise ValueError('Historical failure or untested client is not a blocker')
        if b['code'] in CACHE_BLOCKER_GATES and r['cache_decision'] != CACHE_BLOCKER_GATES[b['code']]:
            raise ValueError('Cache/identity blocker needs the corresponding actual gate decision')
        _text(b.get('evidence_ref'), 'current blocker evidence')
        _text(b.get('detail'), 'current blocker detail')
        if not started <= _time(b.get('observed_at')) <= checked:
            raise ValueError('Blocker must be observed in current task')
        if r.get('attempts'):
            raise ValueError('Submission was attempted; cannot label it unattempted')
        return
    if outcome not in {'READBACK_VERIFIED', 'ATTEMPTED_UNCONFIRMED', 'PENDING_READBACK',
                       'PROVIDER_ERROR', 'NO_HIT', 'PARTIAL_READBACK'}:
        raise ValueError('Unknown outcome; plans/public fallback are not execution')
    batch = _text(r.get('batch_id'), 'batch ID')
    digest = _text(r.get('request_sha256'), 'client request digest')
    if not re.fullmatch(r'[a-f0-9]{64}', digest):
        raise ValueError('Invalid request digest')
    attempts = r.get('attempts', [])
    transport = r.get('transport', 'WEBSITE_GET')
    if transport not in {'WEBSITE_GET', 'GITHUB_ISSUE'}:
        raise ValueError('Unknown submission transport')
    request_issue_urls = set()
    if r['cache_decision'] == 'RESUME_PENDING_BATCH':
        old = r.get('pending_origin', {})
        _text(old.get('evidence_ref'), 'prior submission evidence')
        first = _time(old.get('submitted_at'))
        if first > started or old.get('batch_id') != batch or old.get('request_sha256') != digest:
            raise ValueError('Pending batch identity mismatch')
        if attempts:
            raise ValueError('Resume means readback, not re-submission')
    else:
        if r['cache_decision'] != 'QUERY_REQUIRED' or not attempts:
            raise ValueError('Query-required task cannot finish without an actual attempt')
        times = []
        for a in attempts:
            _text(a.get('evidence_ref'), 'submit tool evidence')
            _text(a.get('client'), 'client')
            if transport == 'WEBSITE_GET':
                if a.get('method') != 'GET' or a.get('endpoint_kind') != 'EXACT_AUTHENTICATED_SUBMIT':
                    raise ValueError('HEAD/root/search/planning is not submission')
            else:
                if a.get('method') != 'POST' or a.get('endpoint_kind') != 'GITHUB_REQUEST_ISSUE':
                    raise ValueError('GitHub submission requires an actual request Issue create')
                request = r.get('request', {})
                if not isinstance(request, dict):
                    raise ValueError('GitHub request must be its original immutable object')
                mode = request.get('mode', 'standard')
                if mode not in ('standard', 'deep_research'):
                    raise ValueError('Invalid GitHub request mode')
                job_limit = 10 if mode == 'deep_research' else 3
                if (request.get('id') != batch or request.get('v') != 1
                        or request.get('redacted') is not True or not isinstance(request.get('jobs'), list)
                        or not 1 <= len(request['jobs']) <= job_limit):
                    raise ValueError('GitHub batch exceeds its mode task limit or has invalid identity/privacy fields')
                expected = hashlib.sha256(json.dumps(request, ensure_ascii=False, sort_keys=True,
                    separators=(',', ':'), allow_nan=False).encode()).hexdigest()
                if expected != digest:
                    raise ValueError('GitHub request digest does not match original request')
                _text(r.get('conversation_id'), 'conversation ID')
                try:
                    if str(UUID(r.get('turn_id'))) != r['turn_id']:
                        raise ValueError()
                except (ValueError, TypeError, AttributeError):
                    raise ValueError('GitHub request requires its original canonical turn UUID') from None
                issue_url = a.get('request_issue_url')
                if issue_url is None and outcome == 'ATTEMPTED_UNCONFIRMED' and a.get('creation_response_received') is False:
                    pass  # Actual create response was lost; reconcile instead of inventing an Issue.
                elif (not isinstance(issue_url, str) or not re.fullmatch(
                        r'https://github[.]com/awdawmip/kimi-query-bridge/issues/[1-9][0-9]*', issue_url)):
                    raise ValueError('Missing exact authorized GitHub request Issue URL')
                else:
                    request_issue_urls.add(issue_url)
            if a.get('batch_id') != batch or a.get('request_sha256') != digest:
                raise ValueError('Do not change batch identity on uncertain outcomes')
            when = _time(a.get('at'))
            if not started <= when <= checked:
                raise ValueError('Historical attempt cannot satisfy current task')
            times.append(when)
        first = min(times)
    read = r.get('github_check', {})
    _text(read.get('evidence_ref'), 'GitHub readback evidence')
    when = _time(read.get('at'))
    if not started <= when <= checked or (when-first).total_seconds() < 30:
        raise ValueError('Readback must be current and at least 30 seconds after submission')
    if read.get('batch_id') != batch:
        raise ValueError('Old/other batch is not current readback')
    if len(request_issue_urls) > 1:
        raise ValueError('Do not duplicate an uncertain batch in multiple request Issues')
    if outcome in {'READBACK_VERIFIED', 'NO_HIT', 'PROVIDER_ERROR', 'PARTIAL_READBACK'}:
        if read.get('request_match') is not True:
            raise ValueError('Need matched request and sub-item identity')
        _text(read.get('result_ref'), 'result issue/comment')
        if read.get('provider') != r['provider'] or read.get('operation') != r['operation']:
            raise ValueError('Wrong provider/operation')
        expected = {'READBACK_VERIFIED':'COMPLETED', 'NO_HIT':'NO_HIT', 'PROVIDER_ERROR':'ERROR',
                    'PARTIAL_READBACK':'PARTIAL'}[outcome]
        if read.get('job_state') != expected:
            raise ValueError('HTTP 200/PUBLISHED/other job is not provider success')
        if request_issue_urls and not any(read['result_ref'].startswith(url + '#issuecomment-') for url in request_issue_urls):
            raise ValueError('GitHub result must be read from the original request Issue')
        if outcome in {'READBACK_VERIFIED', 'PARTIAL_READBACK'}:
            _text(read.get('raw_evidence_ref'), 'actually read raw fields')
        if outcome == 'PARTIAL_READBACK' and read.get('coverage_complete') is not False:
            raise ValueError('Partial readback must disclose incomplete coverage')
    elif outcome == 'ATTEMPTED_UNCONFIRMED' and read.get('batch_found') is not False:
        raise ValueError('Unconfirmed receipt needs an actual missing-batch check')
    elif outcome == 'PENDING_READBACK' and read.get('batch_found') is not True:
        raise ValueError('Pending readback needs the matching pending batch')
