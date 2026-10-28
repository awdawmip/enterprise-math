"""Real local first-review/follow-up transactions for accepted incomplete Tasks.

Synthetic scientific declarations and Source manifests are confined to temporary
fixtures. No test evaluates mathematics, creates live roles or contacts services.
Fresh processes isolate the canonical bootstrap's installed module wrappers.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
CASES = ('accepted', 'invalid_specs', 'binding_variants', 'authority', 'invalid_manifest', 'rollback', 'postcheck',
         'second_review', 'synthesis', 'successor', 'successor_substitution_attack', 'successor_scope_attack', 'successor_new_block_attack')


def run_case(case):
    import contextlib
    import copy
    import hashlib
    import io
    from unittest import mock
    sys.path.insert(0, str(REPO))
    from tests import test_result_writer_canonical_post_audit as fixture
    from tools import research_result_records as records
    from tools import research_dispatch_core as dispatch
    from tools import research_runtime_reducer
    from control_plane import research_control_bootstrap as bootstrap
    from control_plane import research_continuation as continuation
    from control_plane import research_runtime_guard_core as runtime
    from control_plane import research_dependency_release as dependency
    import research_driver_followup as impl
    import research_driver_followup_guard as guard
    import research_driver_authority as driver
    fixture.setUpModule()
    setup = fixture.ResultWriterCanonicalPostAuditTests()
    setup.setUp()
    root = setup.root
    try:
        def write(relative, value):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(records._write_tx.json_bytes(value))
            return path

        def capture(relative):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((REPO / relative).read_bytes())
            return json.loads(path.read_bytes()) if relative.endswith('.json') else None

        setup.first_path.unlink()
        result = {k: v for k, v in records.result_map(root)[fixture.TARGET_ID].items() if not k.startswith('_')}
        result.update(result_id='RR-ACCEPTED-INCOMPLETE-FIXTURE', terminal_verdict='NO_GO',
                      hard_target_disposition='SCOPED_NEGATIVE_RESULT; ORIGINAL_PROCESS_UNKNOWN',
                      method_harvest='CANDIDATE_NOT_TOOL',
                      unresolved_residue='Original process chronology and revised source firewall remain UNKNOWN.')
        root.joinpath(fixture.TARGET_PATH).unlink()
        compatibility = json.loads(root.joinpath(records._base.COMPATIBILITY_FILE).read_bytes())
        compatibility['result_normalizations'] = [r for r in compatibility['result_normalizations'] if r['result_id'] != fixture.TARGET_ID]
        write(records._base.COMPATIBILITY_FILE, compatibility)
        target_path = write(f"research_result_records/{result['task_id']}/{result['result_id']}.json", result)
        original_bytes = target_path.read_bytes()
        publication = capture(f"research_task_records/{result['task_id']}/{result['publication_id']}.json")
        parent = publication['parent_objective_id']
        parent_path = write(f'research_objective_heads/{parent}.json', {'objective_id': parent, 'objective_status': 'OPEN'})
        parent_bytes = parent_path.read_bytes()
        capture('research_driver_followup_legacy_reviews.json')
        baseline_audit = guard.baseline_audit
        capture('research_taskbook_policy.json')
        capture('research_taskbook_contract.json')
        registry = capture('research_driver_review_authority_quarantines.json')
        row = registry['entries'][0]
        write('research_driver_review_authority_quarantines.json', {**registry, 'entries': [row]})
        historical_review = capture(row['review_record_path'])
        historical_result = capture(historical_review['result_record_path'])
        capture(historical_review['review_path'])
        capture(f"research_execution_records/{historical_result['task_id']}/{historical_result['execution_record_id']}.json")
        for relative in {historical_result['return_path'], historical_result['taskbook_path'], *(r['path'] for r in historical_result['output_manifest'])}:
            capture(relative)

        # Enable the actual prospective authority/independence boundary. This
        # TEMP DA adds an explicit synthetic session; no live DA is changed.
        capture(continuation.POLICY)
        da = copy.deepcopy(setup.driver_authority)
        da.pop('_record_path', None)
        body = json.loads(da['source_body'])
        body['session_id'] = 'fixture-scientific-driver-session'
        da['source_body'] = json.dumps(body)
        da['source_body_sha256'] = 'sha256:' + hashlib.sha256(da['source_body'].encode()).hexdigest()
        write(setup.driver_authority['_record_path'], da)
        source = '1' * 40  # trusted fixture-loader snapshot, never a live Source claim
        write('EM_CONTINUATION_WRITE_SANDBOX.json', {'schema': 'ENTERPRISE_MATH_ISOLATED_WRITE_SANDBOX_V1', 'source_commit': source, 'isolated': True})
        scope = 'Synthetic bounded result accepted; original process is not certified.'
        setup.review_path.write_text('# CONTROL FIXTURE\n\n' + scope + '\n', encoding='utf-8')
        interface_path = write('driver_reviews/FIXTURE_INTERFACE.json', {
            'reviewer': fixture.DRIVER_ID, 'result_id': result['result_id'], 'publication_id': result['publication_id'],
            'scope': 'Synthetic bounded model only', 'statement': 'Synthetic fixture statement, not mathematics.',
            'hypotheses': ['All six frozen hypotheses are part of this complete fixture document.'],
            'unresolved': ['Original chronology and revised source firewall UNKNOWN; no Task/parent closure.']})
        def pin(path):
            raw = path.read_bytes()
            return {'repository': 'awdawmip/enterprise-math',
                    'path': path.relative_to(root).as_posix(),
                    'git_blob_sha1': hashlib.sha1(f'blob {len(raw)}\0'.encode() + raw).hexdigest(),
                    'sha256': hashlib.sha256(raw).hexdigest()}
        original_report_bytes = setup.review_path.read_bytes()
        scope_binding = {'schema': impl.RESULT_SCOPE_BINDING_SCHEMA, 'scientific_driver_id': fixture.DRIVER_ID,
            'result_id': result['result_id'], 'publication_id': result['publication_id'], 'historical_source_commit': '2' * 40,
            'interface_artifact': pin(interface_path), 'scope_quote_sha256': hashlib.sha256(scope.encode('utf-8')).hexdigest(),
            'consumption': 'FULL_DOCUMENT', 'covered_fields': ['scope', 'statement', 'hypotheses', 'unresolved']}
        def binding_text(value):
            return ('<!-- ' + impl.RESULT_SCOPE_BINDING_SCHEMA + '\n' + json.dumps(value, ensure_ascii=False, indent=2) + '\n-->\n')
        setup.review_path.write_bytes(original_report_bytes + b'\n' + binding_text(scope_binding).encode('utf-8'))
        assert setup.review_path.read_bytes().startswith(original_report_bytes)
        pins = [pin(setup.review_path), pin(interface_path)]
        write('EM_SOURCE_BLOBS.json', {'schema': 'ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1', 'source_commit': source,
                                     'blobs': {p['path']: p['git_blob_sha1'] for p in pins}})
        args = copy.copy(setup.args)
        args.result_id, args.disposition = result['result_id'], 'ACCEPTED'
        args.reviewer_session_id = body['session_id']
        args.reviewer_contribution_ids_json = '[]'
        args.source_commit = source
        args.followup_created_at = '2026-10-15T20:15:00+00:00'
        view = records.result_map(root)[result['result_id']]
        candidate = records.review_result(result=view, driver_id=args.driver_id, disposition='ACCEPTED',
            review_path=setup.review_path, destination_class='NONE', destination_ref_or_none='', reviewed_at=args.reviewed_at, root=root)
        spec = {'decision': impl.RESULT_CONTINUATION_DECISION, 'tasks': [],
                'gate_decisions': [{'gate': name, 'decision': 'SATISFIED_BY_REVIEWED_RESULT',
                    'reason': 'Explicit synthetic gate judgment; no process or completion inference.',
                    'evidence_refs': [args.review_path]} for name in impl.GATES],
                'result_continuation': {
                    'source_result_id': result['result_id'], 'parent_objective_id': parent, 'original_terminal_verdict': 'NO_GO',
                    'accepted_result_scope': scope,
                    'scope_evidence': {'scientific_review_id': candidate['review_id'], 'historical_source_commit': '2' * 40, 'report_artifact': pins[0],
                        'interface_artifact': pins[1], 'selected_scope_pointer': '/scope', 'consumption': 'FULL_DOCUMENT'},
                    'original_process_status': 'UNKNOWN', 'unresolved_obligations': [{
                        'kind': 'ORIGINAL_PROCESS_PROVENANCE', 'status': 'UNKNOWN',
                        'description': 'Original read chronology and revised source firewall remain uncertified.',
                        'evidence_refs': [pins[1]['path']]}],
                    'action': 'REEVALUATE_CANONICAL_PORTFOLIO', 'dispatcher': 'research_control_dispatch.py',
                    'next_action': 'Resolve the exact process obligation through current canonical control authority.',
                    'remaining_parent_scope': ['Parent classification remains OPEN.'],
                    'evidence_refs': [p['path'] for p in pins],
                    'task_completion_granted': False, 'parent_completion_granted': False, 'parent_final_granted': False}}
        spec_path = write('fixtures/accepted-incomplete.json', spec)
        args.followup_spec = str(spec_path)
        guard._bind_guard(root)
        captured = io.StringIO()
        with mock.patch.object(guard, 'baseline_audit', side_effect=lambda _root=root: baseline_audit(REPO)), \
             mock.patch.object(records, '_install_canonical_write_view', side_effect=lambda: bootstrap.install(root)), \
             contextlib.redirect_stdout(captured):
            if case == 'invalid_specs':
                variants = []
                for field, value in [('original_terminal_verdict', 'PASS'), ('source_result_id', 'RR-OTHER'),
                    ('parent_objective_id', 'OTHER'), ('accepted_result_scope', 'Invented scientific scope'),
                    ('original_process_status', 'COMPLIANT'), ('unresolved_obligations', []),
                    ('task_completion_granted', True), ('parent_completion_granted', True), ('parent_final_granted', True),
                    ('remaining_parent_scope', []), ('evidence_refs', []), ('next_action', '')]:
                    changed = copy.deepcopy(spec); changed['result_continuation'][field] = value
                    variants.append((field, changed, {}))
                for field, value in [('scientific_review_id', 'DR-OTHER'), ('consumption', 'SCOPE_LABEL_ONLY'), ('selected_scope_pointer', '/statement')]:
                    changed = copy.deepcopy(spec); changed['result_continuation']['scope_evidence'][field] = value
                    variants.append((field, changed, {}))
                for field, value in [('sha256', '0' * 64), ('git_blob_sha1', '0' * 40), ('path', '../outside.json')]:
                    changed = copy.deepcopy(spec); changed['result_continuation']['scope_evidence']['interface_artifact'][field] = value
                    variants.append((field, changed, {}))
                for field, value in [('terminal_scope', 'TASK'), ('tasks', [{}]), ('extra', True)]:
                    variants.append((field, {**spec, field: value}, {}))
                changed = copy.deepcopy(spec); changed['gate_decisions'][0]['decision'] = 'REQUIRED'
                variants.append(('required_gate', changed, {}))
                changed = copy.deepcopy(spec); changed['gate_decisions'][2]['decision'] = 'NOT_REQUIRED'
                variants.append(('prior_art_skip', changed, {}))
                variants.append(('missing_gate', {**spec, 'gate_decisions': spec['gate_decisions'][:-1]}, {}))
                variants.append(('missing_spec', spec, {'followup_spec': None}))
                variants.append(('wrong_disposition', spec, {'disposition': 'REQUEST_REVISION'}))
                variants.append(('tool_destination', spec, {'destination_class': 'TOOL'}))
                for label, changed, changes in variants:
                    write(spec_path.relative_to(root).as_posix(), changed)
                    changed_args = copy.copy(args)
                    for key, value in changes.items(): setattr(changed_args, key, value)
                    with mock.patch.object(records._write_tx, 'commit', wraps=records._write_tx.commit) as commit:
                        with unittest.TestCase().assertRaises(ValueError, msg=label): records.command_review_with_authority(changed_args)
                        commit.assert_not_called()
                write(spec_path.relative_to(root).as_posix(), spec)
                for changes in ({'terminal_verdict': 'PASS'}, {'method_harvest': 'GLOBAL_TOOL_FAMILY'}):
                    write(target_path.relative_to(root).as_posix(), {**result, **changes})
                    with mock.patch.object(records._write_tx, 'commit', wraps=records._write_tx.commit) as commit:
                        with unittest.TestCase().assertRaises(ValueError): records.command_review_with_authority(args)
                        commit.assert_not_called()
                target_path.write_bytes(original_bytes)
                assert not list(root.joinpath('research_result_reviews', result['result_id']).glob('*.json'))
            elif case == 'authority':
                for changes in ({'reviewer_session_id': 'borrowed-session'}, {'reviewer_contribution_ids_json': json.dumps([result['researcher_id']])},
                                {'driver_id': 'EM-DVR-FFFF'}, {'source_commit': '2' * 40}):
                    changed_args = copy.copy(args)
                    for key, value in changes.items(): setattr(changed_args, key, value)
                    with mock.patch.object(records._write_tx, 'commit', wraps=records._write_tx.commit) as commit:
                        with unittest.TestCase().assertRaises(ValueError): records.command_review_with_authority(changed_args)
                        commit.assert_not_called()
                from tests.test_research_task_record_compatibility import _write_current_record
                _write_current_record(root, task_id=result['task_id'], publication_id='TP2-LATER-ACCEPTED-FIXTURE',
                    parent_objective_id=parent, publication_generation=2, supersedes_publication_id=result['publication_id'])
                with mock.patch.object(records._write_tx, 'commit', wraps=records._write_tx.commit) as commit:
                    with unittest.TestCase().assertRaisesRegex(ValueError, 'current operational Task publication'):
                        records.command_review_with_authority(args)
                    commit.assert_not_called()
            elif case == 'binding_variants':
                variants = []
                for field, value in [('schema', 'WRONG'), ('scientific_driver_id', 'EM-DVR-FFFF'), ('result_id', 'RR-OTHER'),
                    ('publication_id', 'TP2-OTHER'), ('historical_source_commit', '4' * 40), ('scope_quote_sha256', '0' * 64),
                    ('consumption', 'SCOPE_LABEL_ONLY'), ('covered_fields', ['scope', 'statement']), ('extra', True)]:
                    variants.append((field, binding_text({**scope_binding, field: value})))
                variants.extend([
                    ('legacy_no_block', ''),
                    ('missing_field', binding_text({k: v for k, v in scope_binding.items() if k != 'scope_quote_sha256'})),
                    ('duplicate_block', binding_text(scope_binding) * 2),
                    ('wrong_version_marker', binding_text(scope_binding).replace(impl.RESULT_SCOPE_BINDING_SCHEMA, 'ENTERPRISE_MATH_ACCEPTED_RESULT_SCOPE_BINDING_V2')),
                    ('mixed_version_marker', binding_text(scope_binding) + binding_text(scope_binding).replace(impl.RESULT_SCOPE_BINDING_SCHEMA, 'ENTERPRISE_MATH_ACCEPTED_RESULT_SCOPE_BINDING_V2')),
                    ('duplicate_key', binding_text(scope_binding).replace('{\n', '{\n  "scope_quote_sha256": "duplicate",\n', 1)),
                    ('nested_duplicate_key', binding_text(scope_binding).replace('"repository":', '"repository": "duplicate", "repository":', 1)),
                    ('malformed_json', binding_text(scope_binding).replace('{\n', '{ INVALID\n', 1)),
                    ('literal_backslash_n', binding_text(scope_binding).replace('\n', '\\n')),
                ])
                original_interface = interface_path.read_bytes()
                variants.extend((name, binding_text(scope_binding)) for name in ('missing_hypotheses', 'missing_unresolved'))
                for label, appendix in variants:
                    setup.review_path.write_bytes(original_report_bytes + b'\n' + appendix.encode('utf-8'))
                    interface_path.write_bytes(original_interface)
                    if label.startswith('missing_') and label in {'missing_hypotheses', 'missing_unresolved'}:
                        document = json.loads(original_interface)
                        document.pop(label.removeprefix('missing_'))
                        write(interface_path.relative_to(root).as_posix(), document)
                    changed = copy.deepcopy(spec)
                    report_pin, interface_pin = pin(setup.review_path), pin(interface_path)
                    changed['result_continuation']['scope_evidence'].update(report_artifact=report_pin, interface_artifact=interface_pin)
                    changed_candidate = records.review_result(result=view, driver_id=args.driver_id, disposition='ACCEPTED',
                        review_path=setup.review_path, destination_class='NONE', destination_ref_or_none='', reviewed_at=args.reviewed_at, root=root)
                    changed['result_continuation']['scope_evidence']['scientific_review_id'] = changed_candidate['review_id']
                    write('EM_SOURCE_BLOBS.json', {'schema': 'ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1', 'source_commit': source,
                        'blobs': {p['path']: p['git_blob_sha1'] for p in (report_pin, interface_pin)}})
                    write(spec_path.relative_to(root).as_posix(), changed)
                    with mock.patch.object(records._write_tx, 'commit', wraps=records._write_tx.commit) as commit:
                        with unittest.TestCase().assertRaises(ValueError, msg=label): records.command_review_with_authority(args)
                        commit.assert_not_called()
            elif case == 'invalid_manifest':
                path = root / 'EM_SOURCE_BLOBS.json'
                original = json.loads(path.read_bytes())
                for changes in ({'schema': 'INVALID'}, {'source_commit': '3' * 40}, {'blobs': {}},
                                {'blobs': {p['path']: '0' * 40 for p in pins}}):
                    write('EM_SOURCE_BLOBS.json', {**original, **changes})
                    with mock.patch.object(records._write_tx, 'commit', wraps=records._write_tx.commit) as commit:
                        with unittest.TestCase().assertRaises(ValueError): records.command_review_with_authority(args)
                        commit.assert_not_called()
                path.unlink()
                with unittest.TestCase().assertRaises(ValueError): records.command_review_with_authority(args)
            else:
                original_materialize = guard.materialize
                def materialize(**kwargs):
                    if case == 'rollback':
                        interface_path.write_bytes(interface_path.read_bytes() + b'\n')
                    return original_materialize(**kwargs)
                if case.startswith('successor'):
                    # Persist the genuine first review, simulating a recoverable
                    # materialization interruption. A new current Driver later
                    # consumes exactly its original scientific scope and author.
                    with mock.patch.object(guard, 'materialize', side_effect=ValueError('fixture interruption')):
                        with unittest.TestCase().assertRaisesRegex(ValueError, 'fixture interruption'):
                            records.command_review_with_authority(args)
                    successor = copy.deepcopy(da)
                    did, sid, cid = 'EM-DVR-FADE01', 'fixture-successor-session', 999000001
                    successor.update(driver_id=did, authority_record_id=driver._record_id(did, 'AUTHORIZE', cid), source_comment_id=cid,
                        source_comment_url=f'https://api.github.com/repos/awdawmip/enterprise-math/issues/comments/{cid}')
                    successor_body = {**body, 'driver_id': did, 'session_id': sid}
                    successor['source_body'] = json.dumps(successor_body)
                    successor['source_body_sha256'] = 'sha256:' + hashlib.sha256(successor['source_body'].encode()).hexdigest()
                    write(f"research_driver_authority_records/{did}/{successor['authority_record_id']}.json", successor)
                    with unittest.TestCase().assertRaisesRegex(ValueError, 'authenticated DA session'):
                        guard.materialize(review_id=candidate['review_id'], spec=spec, created_at=args.followup_created_at,
                            root=root, publishing_driver_id=did, publisher_session_id=args.reviewer_session_id)
                    if case != 'successor':
                        review_files = list(root.joinpath('research_result_reviews', result['result_id']).glob('*.json'))
                        assert len(review_files) == 1
                        frozen_review = review_files[0].read_bytes()
                        if case == 'successor_substitution_attack':
                            # Exact independent v1 attack: replace all four
                            # interface science sections, genuine CURRENT
                            # manifest and every spec content pin, keeping the
                            # original scientific DR and report unchanged.
                            document = json.loads(interface_path.read_bytes())
                            document.update(scope='Attacker scope', statement='Attacker theorem',
                                hypotheses=['Attacker weakened hypotheses'], unresolved=['Attacker removes original process residue'])
                            write(interface_path.relative_to(root).as_posix(), document)
                            changed_pin = pin(interface_path)
                            spec['result_continuation']['scope_evidence']['interface_artifact'] = changed_pin
                            write('EM_SOURCE_BLOBS.json', {'schema': 'ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1', 'source_commit': source,
                                'blobs': {pins[0]['path']: pins[0]['git_blob_sha1'], changed_pin['path']: changed_pin['git_blob_sha1']}})
                            pattern = 'immutable scientific scope binding mismatch: interface_artifact'
                        elif case == 'successor_scope_attack':
                            spec['result_continuation']['accepted_result_scope'] = '# CONTROL FIXTURE'
                            pattern = 'immutable scientific scope binding mismatch: scope_quote_sha256'
                        else:
                            setup.review_path.write_bytes(setup.review_path.read_bytes() + b'\n' + binding_text(scope_binding).encode())
                            changed_pin = pin(setup.review_path)
                            spec['result_continuation']['scope_evidence']['report_artifact'] = changed_pin
                            write('EM_SOURCE_BLOBS.json', {'schema': 'ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1', 'source_commit': source,
                                'blobs': {changed_pin['path']: changed_pin['git_blob_sha1'], pins[1]['path']: pins[1]['git_blob_sha1']}})
                            pattern = 'review'
                        with unittest.TestCase().assertRaisesRegex(ValueError, pattern):
                            guard.materialize(review_id=candidate['review_id'], spec=spec, created_at=args.followup_created_at,
                                root=root, publishing_driver_id=did, publisher_session_id=sid)
                        assert review_files[0].read_bytes() == frozen_review
                        assert not list(root.joinpath('research_driver_followups').glob('*/*.json'))
                        print(json.dumps({'case': case, 'status': 'PASS', 'attack': 'REJECTED'}), file=sys.__stdout__)
                        return
                    packet = guard.materialize(review_id=candidate['review_id'], spec=spec, created_at=args.followup_created_at,
                        root=root, publishing_driver_id=did, publisher_session_id=sid)
                    assert packet['driver_id'] == fixture.DRIVER_ID
                    assert packet['materialization_publisher']['driver_id'] == did
                else:
                    from control_plane import check_driver_followup_nonoperational_review_fault_isolated as followup_check
                    original_audit = followup_check.audit
                    def audit(local_root):
                        if case == 'postcheck':
                            interface_path.write_bytes(interface_path.read_bytes() + b'\n')
                        return original_audit(local_root)
                    with mock.patch.object(guard, 'materialize', side_effect=materialize), \
                         mock.patch.object(followup_check, 'audit', side_effect=audit):
                        if case in {'rollback', 'postcheck'}:
                            with unittest.TestCase().assertRaises(ValueError): records.command_review_with_authority(args)
                            assert len(list(root.joinpath('research_result_reviews', result['result_id']).glob('*.json'))) == 1
                            assert not list(root.joinpath('research_driver_followups').glob('*/*.json'))
                            print(json.dumps({'case': case, 'status': 'PASS'}), file=sys.__stdout__); return
                        assert records.command_review_with_authority(args) == 0
                    packet = json.loads(captured.getvalue())['followup']
                impl.validate_packet(packet, root)
                state = records.task_result_state(result['task_id'], root, result['publication_id'])
                assert state['state'] == impl.RESULT_CONTINUATION_STATE and state['terminal'] is False, state
                assert state['result_continuation']['original_process_status'] == 'UNKNOWN'
                definition = dispatch.registered_definition(publication, root)
                frozen = dispatch._overlay_result_state(definition, {'state': 'READY', 'dispatch_state': 'NEEDS_DISPATCH'}, root, state)
                assert frozen['state'] == 'FROZEN_RETURN' and frozen['dispatch_state'] == 'AWAITING_TASK_CONTROL_CONTINUATION', frozen
                assert frozen['claim_id'] is None and frozen['terminal'] is False
                route = continuation._route(frozen)
                assert route['required_role'] == 'RESEARCH_DRIVER' and route['execution_authorized'] is False
                for purpose in ('execution', 'adopt'):
                    with unittest.TestCase().assertRaisesRegex(ValueError, 'closed by result state'):
                        runtime.canonicalize_registration({'task': {'task_id': result['task_id']}}, purpose=purpose, root=root)
                event = {dispatch.GITHUB_META_KEY: {'created_at': '2026-10-15T20:30:00+00:00'}}
                assert 'without an explicit reopen' in dispatch._claim_result_gate_reason(event, state, root)
                gate = {'canonical_main': source, 'result_id': result['result_id'], 'result_record_sha256': packet['source_result_record_sha256'],
                        'review_id': candidate['review_id'], 'followup_id': packet['packet_id']}
                with unittest.TestCase().assertRaisesRegex(ValueError, 'no longer has current terminal'):
                    dependency._current_gate({'publication_id': result['publication_id'], 'gate_evidence': gate},
                        {'task_id': result['task_id'], 'required_artifact': 'ACCEPTED_RESULT'}, {result['task_id']: publication},
                        records.result_map(root), research_runtime_reducer.parse_time(args.followup_created_at), root)
                # A task-global parallel synthesis cannot convert one accepted
                # but incomplete source into Task completion or execution.
                base = {**state, 'state': 'TERMINAL', 'terminal': True, 'parallel_result_ids': [result['result_id']]}
                with mock.patch.object(records._base, 'task_result_state', return_value=base):
                    parallel = records._task_result_state_operational(result['task_id'], root, result['publication_id'])
                assert parallel['state'] == impl.RESULT_CONTINUATION_STATE and parallel['terminal'] is False
                assert dispatch._overlay_result_state(definition, {}, root, parallel)['dispatch_state'] != 'COMPLETE'
                if case in {'second_review', 'synthesis'}:
                    later = copy.copy(args); later.followup_spec = None
                    later.review_path = 'driver_reviews/FIXTURE_SECOND_REVIEW.md'
                    root.joinpath(later.review_path).write_text('A separately pinned synthetic second review.\n')
                    captured.seek(0); captured.truncate()
                    assert records.command_review_with_authority(later) == 0
                    reopened = records.task_result_state(result['task_id'], root, result['publication_id'])
                    assert reopened['state'] == 'AWAITING_DRIVER_REVIEW' and reopened['terminal'] is False, reopened
                    assert len(reopened['parallel_review_ids']) == 2
                    with unittest.TestCase().assertRaises(ValueError): impl.validate_packet(packet, root)
                    if case == 'synthesis':
                        import research_review_evidence as evidence
                        from datetime import datetime, timezone
                        intake = evidence.create_intake(result['result_id'], args.driver_id, root)
                        with unittest.TestCase().assertRaises(ValueError):
                            guard.materialize(review_id=candidate['review_id'], spec=spec,
                                created_at=datetime.now(timezone.utc).isoformat(), root=root,
                                publishing_driver_id=args.driver_id, publisher_session_id=args.reviewer_session_id)
                        for number in (1, 2):
                            evidence.create_reference_pass(intake['intake_id'], number, args.driver_id,
                                f'Synthetic complete-set reference pass {number}; no scientific inference.',
                                'SHARED_CONTROL_CONTEXT_DISCLOSED', root)
                        evidence.create_synthesis(intake['intake_id'], 'ACCEPTED', args.driver_id,
                            'Consume the original fixed scope; original process UNKNOWN and Task incomplete.', root,
                            operational_destination_class='NONE')
                        authority = guard.authority_for_result(result['result_id'], root)
                        synthesized = guard.materialize(review_id=authority['review_id'], spec=spec,
                            created_at=datetime.now(timezone.utc).isoformat(), root=root,
                            publishing_driver_id=args.driver_id, publisher_session_id=args.reviewer_session_id)
                        impl.validate_packet(synthesized, root)
                        synthesized_state = records.task_result_state(result['task_id'], root, result['publication_id'])
                        assert synthesized_state['state'] == impl.RESULT_CONTINUATION_STATE and synthesized_state['terminal'] is False
                        assert synthesized['result_continuation']['scope_evidence']['scientific_review_id'] == candidate['review_id']
                assert target_path.read_bytes() == original_bytes
                assert parent_path.read_bytes() == parent_bytes
                assert not packet['task_publications']
                if case == 'accepted':
                    # Native review snapshots have no Git history. A later real
                    # Source snapshot retains these exact immutable artifacts;
                    # replay rechecks CURRENT membership, not historical Git.
                    assert not (root / '.git').exists()
                    assert packet['scope_source_snapshot']['source_commit'] == source
                    assert packet['scope_source_snapshot']['verification_basis'] == 'CURRENT_SOURCE_MEMBERSHIP'
                    assert packet['scope_source_snapshot']['historical_membership_reverified'] is False
                    assert packet['result_continuation']['scope_evidence']['historical_source_commit'] != source
                    advanced = '3' * 40
                    write('EM_CONTINUATION_WRITE_SANDBOX.json', {'schema': 'ENTERPRISE_MATH_ISOLATED_WRITE_SANDBOX_V1',
                        'source_commit': advanced, 'isolated': True})
                    write('EM_SOURCE_BLOBS.json', {'schema': 'ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1', 'source_commit': advanced,
                        'blobs': {p['path']: p['git_blob_sha1'] for p in pins}})
                    impl.validate_packet(packet, root)
                    assert records.task_result_state(result['task_id'], root, result['publication_id'])['terminal'] is False
        print(json.dumps({'case': case, 'status': 'PASS'}))
    finally:
        setup.doCleanups()


class AcceptedResultTaskOpenTests(unittest.TestCase):
    def test_cases(self):
        for case in CASES:
            with self.subTest(case=case):
                done = subprocess.run([sys.executable, '-B', str(Path(__file__).resolve()), '--case', case],
                                      cwd=REPO, capture_output=True, text=True, timeout=90)
                self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
                self.assertEqual(json.loads(done.stdout)['status'], 'PASS')


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--case': run_case(sys.argv[2])
    else: unittest.main()
