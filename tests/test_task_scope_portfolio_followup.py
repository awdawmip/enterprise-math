"""Completed Tasks return to the portfolio through the real first-review writer.

Every case runs in a fresh process: canonical bootstrap installs module wrappers.
No tests issue claims, invoke research, or write outside their temporary fixture.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
CASES = ("open_parent", "absent_parent", "parked_parent", "invalid_specs", "invalid_driver", "historical_generation",
         "review_pin_race", "duplicate_packet_race", "result_pin_postcheck",
         "second_review_race", "packet_bytes_race", "publication_pin_postcheck")


def run_case(case):
    import contextlib
    import copy
    import hashlib
    import io
    from unittest import mock

    sys.path.insert(0, str(REPO))
    from tests import test_result_writer_canonical_post_audit as fixture
    from tools import research_result_records as records
    from tools import active_turn_liveness
    from tools import research_runtime_guard
    from control_plane import research_control_bootstrap as bootstrap
    from control_plane import research_driver_followup_transaction as transaction
    from control_plane import check_driver_followup_nonoperational_review_fault_isolated as followup_check
    from tests.test_research_task_record_compatibility import _write_current_record
    import research_driver_followup as impl
    import research_driver_followup_guard as guard
    import research_objective_records as objectives

    fixture.setUpModule()
    setup = fixture.ResultWriterCanonicalPostAuditTests()
    setup.setUp()
    root = setup.root
    try:
        def write(relative, value):
            path = root.joinpath(relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(records._write_tx.json_bytes(value))
            return path

        def capture(relative):
            path = root.joinpath(relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(REPO.joinpath(relative).read_bytes())
            return json.loads(path.read_bytes()) if relative.endswith('.json') else None

        # The prior fixture supplies real ER/output pins, an exact historical
        # Result quarantine and source-backed active Driver authority. Replace
        # only its TEMP review and TEMP verdict for this completed-Task scenario.
        setup.first_path.unlink()
        result = {k: v for k, v in records.result_map(root)[fixture.TARGET_ID].items() if not k.startswith('_')}
        result.update(result_id='RR-TASK-SCOPE-FIXTURE', terminal_verdict='PASS', hard_target_disposition='SATISFIED',
                      unresolved_residue='Parent classification remains open outside this Task.')
        # Do not rewrite a legacy normalized record under its exact legacy pin.
        # This is a new TEMP Result, backed by the fixture's copied ER/outputs.
        root.joinpath(fixture.TARGET_PATH).unlink()
        compatibility_path = root.joinpath(records._base.COMPATIBILITY_FILE)
        compatibility = json.loads(compatibility_path.read_bytes())
        compatibility['result_normalizations'] = [row for row in compatibility['result_normalizations']
                                                   if row['result_id'] != fixture.TARGET_ID]
        write(records._base.COMPATIBILITY_FILE, compatibility)
        target_path = write(f"research_result_records/{result['task_id']}/{result['result_id']}.json", result)
        publication = capture(f"research_task_records/{result['task_id']}/{result['publication_id']}.json")
        parent = publication['parent_objective_id']
        objective_path = write(f'research_objective_heads/{parent}.json',
                               {'objective_id': parent, 'objective_status': 'OPEN'})
        parent_status = 'OPEN'
        if case == 'absent_parent':
            objective_path.unlink()
            parent_status = 'ABSENT_NOT_CLOSED'
        elif case == 'parked_parent':
            write(f'research_objective_heads/{parent}.json', {'objective_id': parent, 'objective_status': 'PARKED'})
            parent_status = 'PARKED'
        elif case == 'historical_generation':
            _write_current_record(root, task_id=result['task_id'], publication_id='TP2-CURRENT-FIXTURE',
                                  parent_objective_id=parent, publication_generation=2,
                                  supersedes_publication_id=result['publication_id'])
        capture('research_driver_followup_legacy_reviews.json')
        # Legacy integrity is checked against the actual immutable source tree,
        # not duplicated as unrelated incomplete Results in this small fixture.
        baseline_audit = guard.baseline_audit
        policy = capture('research_taskbook_policy.json')
        for relative in policy['policy_inputs']:
            capture(relative)
        registry = json.loads(REPO.joinpath('research_driver_review_authority_quarantines.json').read_bytes())
        row = registry['entries'][0]
        write('research_driver_review_authority_quarantines.json', {**registry, 'entries': [row]})
        historical_review = capture(row['review_record_path'])
        historical_result = capture(historical_review['result_record_path'])
        capture(historical_review['review_path'])
        capture(f"research_execution_records/{historical_result['task_id']}/{historical_result['execution_record_id']}.json")
        for relative in {historical_result['return_path'], historical_result['taskbook_path'],
                         *(item['path'] for item in historical_result['output_manifest'])}:
            capture(relative)

        spec = {
            'decision': impl.TASK_SCOPE_DECISION, 'terminal_scope': 'TASK', 'tasks': [],
            'gate_decisions': [
                {'gate': gate, 'decision': 'SATISFIED_BY_REVIEWED_RESULT',
                 'reason': 'The bounded fixture gate was satisfied by the pinned return.',
                 'evidence_refs': [result['return_path']]} for gate in impl.GATES
            ],
            'portfolio_continuation': {
                'source_result_id': result['result_id'], 'parent_objective_id': parent,
                'action': 'REEVALUATE_CANONICAL_PORTFOLIO',
                'dispatcher': 'research_control_dispatch.py',
                'next_action': 'Read fresh events and session observations; run the canonical dispatcher for remaining parent work.',
                'remaining_parent_scope': ['Parent classification is outside the completed finite Task.'],
                'evidence_refs': [result['return_path']],
            },
        }
        spec_path = write('fixtures/completed-task-followup.json', spec)
        args = copy.copy(setup.args)
        args.result_id = result['result_id']
        args.disposition = 'ACCEPTED'
        args.followup_spec = str(spec_path)
        args.followup_created_at = '2026-09-08T08:00:00+00:00'
        guard._bind_guard(root)
        captured = io.StringIO()
        rejected = []
        with mock.patch.object(guard, 'baseline_audit', side_effect=lambda _root=root: baseline_audit(REPO)), \
             mock.patch.object(records, '_install_canonical_write_view', side_effect=lambda: bootstrap.install(root)), \
             contextlib.redirect_stdout(captured):
            if case in {'invalid_specs', 'invalid_driver', 'historical_generation'}:
                # Each rejection enters the real public first-review command.
                # No write candidate or permission/claim adapter is substituted.
                changes = [
                    ('INCOMPLETE', {'terminal_verdict': 'INCOMPLETE'}, {}, {}, 'PASS/SUCCESS'),
                    ('negative_boundary', {'terminal_verdict': 'NEGATIVE_BOUNDARY'}, {}, {}, 'PASS/SUCCESS'),
                    ('partial_target', {'hard_target_disposition': 'PARTIAL'}, {}, {}, 'SATISFIED'),
                    ('nonaccepted', {}, {}, {'disposition': 'REQUEST_REVISION'}, 'ACCEPTED'),
                    ('parent_scope', {}, {'terminal_scope': 'PARENT'}, {}, 'terminal_scope TASK'),
                    ('missing_scope', {}, {'terminal_scope': None}, {}, 'terminal_scope TASK'),
                    ('missing_continuation', {}, {'portfolio_continuation': None}, {}, 'exact typed'),
                    ('new_task', {}, {'tasks': [{}]}, {}, 'cannot publish new tasks'),
                ]
                for field, value, fragment in (
                    ('source_result_id', 'RR-OTHER', 'Result mismatch'),
                    ('parent_objective_id', 'OBJ-OTHER', 'parent Objective mismatch'),
                    ('action', 'GRANT_CLAIM', 'reevaluate'),
                    ('dispatcher', 'other_scheduler.py', 'research_control_dispatch'),
                    ('next_action', '', 'concrete next_action'),
                    ('remaining_parent_scope', [], 'remaining_parent_scope'),
                    ('evidence_refs', [], 'evidence_refs'),
                ):
                    continuation = copy.deepcopy(spec['portfolio_continuation'])
                    continuation[field] = value
                    changes.append((field, {}, {'portfolio_continuation': continuation}, {}, fragment))
                required = copy.deepcopy(spec['gate_decisions']); required[0]['decision'] = 'REQUIRED'
                changes.append(('required_gate', {}, {'gate_decisions': required}, {}, 'REQUIRED'))
                changes.append(('missing_gate', {}, {'gate_decisions': spec['gate_decisions'][:-1]}, {}, 'exactly 6'))
                if case == 'invalid_driver':
                    changes = [('inactive_driver', {}, {}, {'driver_id': 'EM-DVR-FFFF'}, 'ACTIVE authority')]
                elif case == 'historical_generation':
                    changes = [('historical_generation', {}, {}, {}, 'current operational Task publication')]
                for label, result_changes, spec_changes, arg_changes, fragment in changes:
                    write(target_path.relative_to(root).as_posix(), {**result, **result_changes})
                    write(spec_path.relative_to(root).as_posix(), {**spec, **spec_changes})
                    changed_args = copy.copy(args)
                    for key, value in arg_changes.items():
                        setattr(changed_args, key, value)
                    with mock.patch.object(records._write_tx, 'commit', wraps=records._write_tx.commit) as commit:
                        try:
                            records.command_review_with_authority(changed_args)
                        except ValueError as exc:
                            assert fragment in str(exc), (label, str(exc))
                        else:
                            raise AssertionError('invalid first review was accepted: ' + label)
                        commit.assert_not_called()
                    rejected.append(label)
                write(target_path.relative_to(root).as_posix(), result)
                write(spec_path.relative_to(root).as_posix(), spec)
                assert not list(root.joinpath('research_result_reviews', result['result_id']).glob('*.json'))
                assert not list(root.joinpath('research_driver_followups').glob('*/*.json'))
                print_value = {'case': case, 'status': 'PASS', 'rejected_before_write': rejected}
            else:
                original_materialize = guard.materialize
                original_check = followup_check.audit
                altered = []

                def materialize_with_race(**kwargs):
                    if case == 'review_pin_race':
                        target_path.write_bytes(target_path.read_bytes() + b'\n')
                        altered.append(target_path)
                    return original_materialize(**kwargs)

                def postcheck_with_race(local_root):
                    packets = list(root.joinpath('research_driver_followups').glob('*/*.json'))
                    assert len(packets) == 1
                    packet_path = packets[0]
                    frozen = json.loads(packet_path.read_bytes())
                    if case == 'duplicate_packet_race':
                        duplicate = {**frozen, 'packet_id': 'DFU-ANOTHER-FIXTURE'}
                        altered.append(write('research_driver_followups/DR-OTHER/DFU-ANOTHER-FIXTURE.json', duplicate))
                    elif case == 'result_pin_postcheck':
                        target_path.write_bytes(target_path.read_bytes() + b'\n'); altered.append(target_path)
                    elif case == 'second_review_race':
                        review_paths = list(root.joinpath('research_result_reviews', result['result_id']).glob('*.json'))
                        another = json.loads(review_paths[0].read_bytes())
                        another['review_id'] = 'DR-SECOND-FIXTURE'
                        altered.append(write(f"research_result_reviews/{result['result_id']}/DR-SECOND-FIXTURE.json", another))
                    elif case == 'packet_bytes_race':
                        packet_path.write_bytes(packet_path.read_bytes() + b'\n'); altered.append(packet_path)
                    elif case == 'publication_pin_postcheck':
                        _write_current_record(root, task_id=result['task_id'], publication_id='TP2-LATER-FIXTURE',
                                              parent_objective_id=parent, publication_generation=2,
                                              supersedes_publication_id=result['publication_id'])
                        altered.extend([root.joinpath('research_tasks/TP2-LATER-FIXTURE.md'),
                                        root.joinpath('research_task_records', result['task_id'], 'TP2-LATER-FIXTURE.json')])
                    return original_check(local_root)

                failure = None
                with mock.patch.object(guard, 'materialize', side_effect=materialize_with_race), \
                     mock.patch.object(followup_check, 'audit', side_effect=postcheck_with_race):
                    try:
                        assert records.command_review_with_authority(args) == 0
                    except ValueError as exc:
                        failure = str(exc)
                if case.endswith('race') or case in {'result_pin_postcheck', 'publication_pin_postcheck'}:
                    expected = {'review_pin_race': 'current Result bytes',
                                'duplicate_packet_race': 'unique exact review packet',
                                'result_pin_postcheck': 'current Result bytes',
                                'second_review_race': 'unknown review',
                                'publication_pin_postcheck': 'current operational Task publication',
                                'packet_bytes_race': 'frozen candidate bytes'}[case]
                    assert failure and expected in failure, (case, failure)
                    # The committed first DR stays; only the transaction's own
                    # unchanged packet is rolled back. External drift is kept.
                    reviews = list(root.joinpath('research_result_reviews', result['result_id']).glob('*.json'))
                    assert reviews
                    packets = list(root.joinpath('research_driver_followups').glob('*/*.json'))
                    assert set(packets) == {p for p in altered if 'research_driver_followups' in p.parts}
                    for path in altered:
                        assert path.exists()
                    print_value = {'case': case, 'status': 'PASS', 'rejection': failure,
                                   'persisted_first_review_preserved': True}
                else:
                    assert failure is None, failure
                    print_value = None
            if print_value is not None:
                pass
            else:
                payload = json.loads(captured.getvalue())
                packet = payload['followup']
                impl.validate_packet(packet, root)
                state = records.task_result_state(result['task_id'], root=root, publication_id=result['publication_id'])
                # A second invocation of either existing materializer cannot
                # manufacture a second packet for the same review authority.
                for materializer in (guard.materialize, impl.nontransactional_materialize):
                    try:
                        materializer(review_id=packet['review_id'], spec=spec, created_at=args.followup_created_at, root=root)
                    except ValueError as exc:
                        assert 'existing review/packet identity' in str(exc), str(exc)
                    else:
                        raise AssertionError('duplicate follow-up accepted')
                assert state['terminal'] is True, state
                assert state['terminal_scope'] == 'TASK', state
                assert state['driver_followup_state'] == 'TASK_SCOPE_CLOSED_PORTFOLIO_CONTINUATION', state
                assert state['parent_completion_granted'] is False
                assert state['parent_final_granted'] is False
                assert packet['parent_status_at_materialization'] == parent_status
                assert packet['source_result_record_sha256'] == 'sha256:' + hashlib.sha256(target_path.read_bytes()).hexdigest()
                head = objectives.current_head(parent, root)
                assert (head is None if parent_status == 'ABSENT_NOT_CLOSED' else head['objective_status'] == parent_status)
                assert not packet['task_publications']
                # Mutations of the typed packet remain fail-closed at replay.
                for field, value in (('parent_final_granted', True), ('parent_completion_granted', None),
                                     ('parent_status_at_materialization', 'CLOSED'), ('terminal_scope', 'PARENT'),
                                     ('source_result_record_sha256', 'sha256:' + '0' * 64)):
                    with unittest.TestCase().assertRaises(ValueError):
                        impl.validate_packet({**packet, field: value}, root)
                if case == 'open_parent':
                    # A later, independently published generation changes the
                    # current task, not the integrity of an old immutable packet.
                    _write_current_record(root, task_id=result['task_id'], publication_id='TP2-LATER-FIXTURE',
                                          parent_objective_id=parent, publication_generation=2,
                                          supersedes_publication_id=result['publication_id'])
                    impl.validate_packet(packet, root)
                    with unittest.TestCase().assertRaisesRegex(ValueError, 'current operational Task publication'):
                        transaction._validate_packet_candidate(packet, root, persisted=True)
                liveness = {key: False for key in active_turn_liveness._BOOL_FIELDS}
                liveness['executable_next_actions'] = 1
                live = research_runtime_guard.pre_final_gate(
                    {'research_mode': 'RESEARCH_DRIVER', 'parent_liveness': liveness}, root=root)
                assert live['final_allowed'] is False and live['authorized'] is False, live
                assert live['required_action'] == 'EXECUTE_SELECTED_NEXT_ACTION_NOW'
                print_value = {'case': case, 'status': 'PASS', 'terminal_scope': 'TASK',
                               'parent_status': parent_status, 'parent_final_allowed': live['final_allowed']}
        print(json.dumps(print_value))
    finally:
        setup.doCleanups()


class TaskScopePortfolioFollowupTests(unittest.TestCase):
    def run_fresh_case(self, case):
        done = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(Path(__file__).resolve()), '--case', case],
                              cwd=REPO, capture_output=True, text=True, encoding='utf-8', timeout=90)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertEqual(json.loads(done.stdout)['status'], 'PASS')


for _case in CASES:
    setattr(TaskScopePortfolioFollowupTests, 'test_' + _case,
            lambda self, case=_case: self.run_fresh_case(case))


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--case':
        run_case(sys.argv[2])
    else:
        unittest.main()
