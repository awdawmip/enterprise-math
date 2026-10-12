"""Bounded Task-only negative alternatives and exact-author RVS assessments.

Temporary fixtures use real report/Result hashes, native review builders and
native intake/reference/synthesis reducers. Canonical readers are fixture-bound;
these tests neither grant live roles nor write Source, credentials or services.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import research_driver_followup as followup
import research_driver_followup_guard as guard
import research_review_evidence as evidence
from tools import research_result_records as canonical

DRIVER = 'EM-DVR-A1B2C3'
OTHER = 'EM-DVR-D4E5F6'
CLAUSE = 'Kill: an exact declared mechanism obstruction completes this Task; the parent theorem remains open.'


class NegativeTaskAssessmentTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='em-negative-assessment-fixture-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.book = self.root / 'research_tasks/negative.md'
        self.book.parent.mkdir(parents=True)
        self.book.write_text('# Fixture Task\n\n' + CLAUSE + '\n', encoding='utf-8')
        self.result = {
            'record_schema': followup.result_impl.RESULT_SCHEMA,
            'result_id': 'RR-NEGATIVE-FIXTURE', 'task_id': 'TASK-NEGATIVE-FIXTURE',
            'publication_id': 'TP2-NEGATIVE-FIXTURE', 'execution_record_id': 'ER-FIXTURE',
            'terminal_verdict': 'NEGATIVE_BOUNDARY',
            'hard_target_disposition': 'DECLARED_MECHANISM_OBSTRUCTED; PARENT_OPEN',
            'taskbook_path': 'research_tasks/negative.md',
            'taskbook_blob_sha1': followup.result_impl._blob(self.book),
            'next_control_plane_recommendation': 'Retain the existing outer-determinant successor.',
        }
        self.result_path = self.root / 'research_result_records/TASK-NEGATIVE-FIXTURE/RR-NEGATIVE-FIXTURE.json'
        self.persist_result()
        self.publication = {
            'task_id': self.result['task_id'], 'publication_id': self.result['publication_id'],
            'parent_objective_id': 'OBJ-PARENT', 'taskbook_path': self.result['taskbook_path'],
            'taskbook_blob_sha1': self.result['taskbook_blob_sha1'],
        }
        self.sources = []
        self.excluded = set()
        self.authority = None
        for patch in (
            mock.patch.object(canonical, 'iter_reviews', side_effect=lambda root: [r for r in self.sources if r['review_id'] not in self.excluded]),
            mock.patch.object(canonical, 'result_map', side_effect=lambda root: {self.result['result_id']: self.result}),
            mock.patch.object(followup.research_task_records, 'iter_records', side_effect=lambda root: [self.publication]),
            mock.patch.object(followup.research_task_records, 'current_records', side_effect=lambda root: {self.result['task_id']: self.publication}),
            mock.patch.object(followup, 'review_map', side_effect=lambda root: {self.authority['review_id']: self.authority}),
            mock.patch.object(followup, 'result_map', side_effect=lambda root: {self.result['result_id']: self.result}),
            mock.patch.object(followup, '_objective_head', return_value={'objective_id': 'OBJ-PARENT', 'objective_status': 'OPEN'}),
        ):
            patch.start()
            self.addCleanup(patch.stop)
        self.gates = [{'gate': name, 'decision': 'SATISFIED_BY_REVIEWED_RESULT',
                       'reason': 'Explicit fixture judgment; no parent promotion.',
                       'evidence_refs': ['fixture/negative-return']} for name in followup.GATES]
        self.continuation = {
            'source_result_id': self.result['result_id'], 'parent_objective_id': 'OBJ-PARENT',
            'action': 'REEVALUATE_CANONICAL_PORTFOLIO', 'dispatcher': 'research_control_dispatch.py',
            'next_action': 'Read the existing successor and fresh portfolio state.',
            'remaining_parent_scope': ['All-m outer determinant remains open.'],
            'evidence_refs': ['fixture/existing-successor'],
        }

    def persist_result(self):
        self.result_path.parent.mkdir(parents=True, exist_ok=True)
        raw = {k: v for k, v in self.result.items() if not k.startswith('_')}
        self.result_path.write_text(json.dumps(raw, indent=2) + '\n', encoding='utf-8')
        self.result['_record_path'] = self.result_path.relative_to(self.root).as_posix()

    def assessment(self, driver=DRIVER):
        result = self.result
        value = {
            'schema': followup.TASK_COMPLETION_ASSESSMENT_SCHEMA, 'driver_id': driver,
            'task_id': result['task_id'], 'publication_id': result['publication_id'],
            'result_id': result['result_id'],
            'result_record_sha256': 'sha256:' + hashlib.sha256(self.result_path.read_bytes()).hexdigest(),
            'original_hard_target_disposition': result['hard_target_disposition'],
            'disposition': 'SATISFIED', 'terminal_scope': 'TASK',
            'assessment': 'The exact declared negative alternative is met; no parent nonvanishing theorem is claimed.',
        }
        if result['terminal_verdict'] == 'NEGATIVE_BOUNDARY':
            value['negative_return_evidence'] = {
                'schema': followup.NEGATIVE_TASK_ALTERNATIVE_SCHEMA,
                'taskbook_path': result['taskbook_path'],
                'taskbook_blob_sha1': result['taskbook_blob_sha1'],
                'taskbook_sha256': 'sha256:' + hashlib.sha256(self.book.read_bytes()).hexdigest(),
                'negative_return_clause': CLAUSE,
                'completion_basis': 'DECLARED_TASKBOOK_NEGATIVE_ALTERNATIVE',
                'parent_completion_granted': False,
            }
        return value

    def review(self, assessment=None, driver=DRIVER, disposition='ACCEPTED', text=None):
        number = len(self.sources)
        report = self.root / f'driver_reviews/fixture-{number}.md'
        report.parent.mkdir(parents=True, exist_ok=True)
        body = f'# Temporary fixture report {number}\n'
        if assessment is not None:
            body += ('\n<!-- ' + followup.TASK_COMPLETION_ASSESSMENT_SCHEMA + '\n'
                     + json.dumps(assessment, indent=2) + '\n-->\n')
        report.write_text(body if text is None else text, encoding='utf-8')
        row = followup.result_impl.review_result(
            result=self.result, driver_id=driver, disposition=disposition, review_path=report,
            destination_class='NONE', destination_ref_or_none='',
            reviewed_at='2026-10-12T18:00:00+00:00', root=self.root,
        )
        relative = f"research_result_reviews/{self.result['result_id']}/{row['review_id']}.json"
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(row, indent=2) + '\n', encoding='utf-8')
        row['_review_path'] = relative
        self.sources.append(row)
        self.authority = {**row, 'review_authority_kind': 'IMMUTABLE_REVIEW'}
        return row

    def synthesize(self, driver=DRIVER):
        intake = evidence.create_intake(self.result['result_id'], driver, self.root)
        for number in (1, 2):
            evidence.create_reference_pass(intake['intake_id'], number, driver,
                f'Fixture exact-set pass {number}; shared context is disclosed.',
                'SHARED_CONTROL_CONTEXT_DISCLOSED', self.root)
        evidence.create_synthesis(intake['intake_id'], 'ACCEPTED', driver,
            'Fixture bounded negative Task alternative; parent remains open.', self.root,
            operational_destination_class='NONE')
        self.authority = guard.authority_for_result(self.result['result_id'], self.root)
        self.assertEqual(self.authority['review_authority_kind'], 'REVIEW_SYNTHESIS')
        return self.authority

    def build(self, **overrides):
        args = dict(review_id=self.authority['review_id'], decision=followup.TASK_SCOPE_DECISION,
                    gate_decisions=self.gates, task_publications=[], driver_id=self.authority['driver_id'],
                    created_at='2026-10-12T19:00:00+00:00', root=self.root,
                    terminal_scope='TASK', portfolio_continuation=self.continuation)
        args.update(overrides)
        return followup.build_packet(**args)

    def test_negative_immutable_assessment_builds_only_task_packet_without_rewriting_inputs(self):
        self.review(self.assessment())
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        packet = self.build()
        followup.validate_packet(packet, self.root, current_publication_required=True)
        self.assertEqual(packet['terminal_scope'], 'TASK')
        self.assertFalse(packet['parent_completion_granted'])
        self.assertFalse(packet['parent_final_granted'])
        self.assertEqual(packet['parent_status_at_materialization'], 'OPEN')
        self.assertEqual(packet['task_publications'], [])
        self.assertEqual(self.result['terminal_verdict'], 'NEGATIVE_BOUNDARY')
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_negative_requires_explicit_evidence_even_with_literal_satisfied(self):
        for target in ('SATISFIED', 'DECLARED_MECHANISM_OBSTRUCTED; PARENT_OPEN'):
            with self.subTest(target=target):
                self.result['hard_target_disposition'] = target
                self.persist_result()
                for body in (None, {k: v for k, v in self.assessment().items() if k != 'negative_return_evidence'}):
                    self.review(body)
                    with self.assertRaisesRegex(ValueError, 'assessment'):
                        self.build()

    def test_exact_assessment_fields_actor_result_hash_original_target_and_scope_rejected(self):
        for field, value in (
            ('driver_id', OTHER), ('task_id', 'OTHER-TASK'), ('publication_id', 'TP2-OTHER'),
            ('result_id', 'RR-OTHER'), ('result_record_sha256', 'sha256:' + '0' * 64),
            ('original_hard_target_disposition', 'SATISFIED_BY_REINTERPRETATION'),
            ('disposition', 'PARTIAL'), ('terminal_scope', 'PARENT'), ('assessment', ''),
            ('extra', 'not allowed'),
        ):
            with self.subTest(field=field):
                self.review({**self.assessment(), field: value})
                with self.assertRaisesRegex(ValueError, 'assessment'):
                    self.build()

    def test_negative_evidence_exact_fields_pins_clause_and_parent_flag_rejected(self):
        variants = [('schema', 'WRONG'), ('taskbook_path', 'research_tasks/other.md'),
                    ('taskbook_blob_sha1', 'sha1:' + '0' * 40), ('taskbook_sha256', 'sha256:' + '0' * 64),
                    ('negative_return_clause', 'Task completed by control alone'),
                    ('negative_return_clause', ''), ('completion_basis', 'PARENT_THEOREM_PROVED'),
                    ('parent_completion_granted', True), ('extra', False)]
        for field, value in variants:
            with self.subTest(field=field, value=value):
                assessment = self.assessment()
                assessment['negative_return_evidence'][field] = value
                self.review(assessment)
                with self.assertRaises(ValueError):
                    self.build()
        assessment = self.assessment()
        del assessment['negative_return_evidence']['negative_return_clause']
        self.review(assessment)
        with self.assertRaisesRegex(ValueError, 'exact negative_return_evidence'):
            self.build()

    def test_raw_taskbook_and_publication_pin_drift_rejected(self):
        self.review(self.assessment())
        original = self.book.read_bytes()
        self.book.write_bytes(original + b'Changed\n')
        with self.assertRaisesRegex(ValueError, 'byte binding'):
            self.build()
        self.book.write_bytes(original)
        self.publication['taskbook_blob_sha1'] = 'sha1:' + '0' * 40
        with self.assertRaisesRegex(ValueError, 'exact published Taskbook'):
            self.build()

    def test_report_and_raw_result_drift_rejected(self):
        row = self.review(self.assessment())
        report = self.root / row['review_path']
        original = report.read_bytes()
        report.write_bytes(original + b'Changed\n')
        with self.assertRaisesRegex(ValueError, 'bytes drifted'):
            self.build()
        report.write_bytes(original)
        self.result_path.write_bytes(self.result_path.read_bytes() + b' ')
        with self.assertRaisesRegex(ValueError, 'pin current Result bytes'):
            self.build()

    def test_rvs_uses_unique_valid_same_author_preserving_old_wrong_typed_report(self):
        wrong = self.assessment()
        wrong['original_hard_target_disposition'] = 'WRONG_OLD_TYPED_INTERPRETATION'
        old = self.review(wrong)
        old_bytes = (self.root / old['review_path']).read_bytes()
        self.review(None, driver=OTHER)
        self.review(self.assessment())
        self.synthesize()
        packet = self.build()
        followup.validate_packet(packet, self.root, current_publication_required=True)
        self.assertEqual(packet['review_id'], self.authority['review_id'])
        self.assertFalse(packet['parent_completion_granted'])
        self.assertEqual((self.root / old['review_path']).read_bytes(), old_bytes)

    def test_rvs_does_not_borrow_other_drivers_valid_assessment(self):
        self.review(None)
        self.review(self.assessment(OTHER), driver=OTHER)
        self.synthesize()
        with self.assertRaisesRegex(ValueError, 'exactly one.*found 0'):
            self.build()

    def test_rvs_two_valid_same_driver_assessments_reject_without_timestamp_winner(self):
        self.review(self.assessment())
        changed = self.assessment()
        changed['assessment'] += ' Another separately pinned judgment.'
        self.review(changed)
        self.synthesize()
        with self.assertRaisesRegex(ValueError, 'exactly one.*found 2'):
            self.build()

    def test_rvs_canonical_quarantine_and_new_review_set_drift_reject(self):
        old = self.review(None, driver=OTHER)
        self.review(self.assessment())
        self.synthesize()
        self.excluded.add(old['review_id'])
        with self.assertRaises(ValueError):
            self.build()
        self.excluded.clear()
        saved_authority = self.authority
        self.review(None, driver=OTHER)
        self.authority = saved_authority
        with self.assertRaisesRegex(ValueError, 'current exact accepted synthesis'):
            self.build()

    def test_rvs_raw_actor_or_projection_publication_mismatch_rejected(self):
        self.review(None, driver=OTHER)
        self.review(self.assessment())
        self.synthesize()
        self.authority['driver_id'] = OTHER
        with self.assertRaisesRegex(ValueError, 'raw synthesis differs'):
            self.build()
        self.authority['driver_id'] = DRIVER
        self.authority['publication_id'] = 'TP2-OTHER'
        with self.assertRaises(ValueError):
            self.build()

    def test_rvs_other_source_report_drift_is_fatal_not_skipped_as_ineligible(self):
        other = self.review(None, driver=OTHER)
        self.review(self.assessment())
        self.synthesize()
        path = self.root / other['review_path']
        path.write_bytes(path.read_bytes() + b'Changed\n')
        with self.assertRaisesRegex(ValueError, 'bytes drifted'):
            self.build()

    def test_rvs_second_read_binding_failure_is_not_swallowed(self):
        self.review(None, driver=OTHER)
        self.review(self.assessment())
        self.synthesize()
        original = followup._driver_task_assessment_report
        calls = 0
        def checked(*args):
            nonlocal calls
            calls += 1
            if calls == 3:
                raise followup.DriverFollowupError('simulated second-read report binding drift')
            return original(*args)
        with mock.patch.object(followup, '_driver_task_assessment_report', side_effect=checked):
            with self.assertRaisesRegex(ValueError, 'second-read report binding drift'):
                self.build()

    def test_negative_explicit_incomplete_targets_stay_rejected(self):
        for target in ('PARTIAL', 'INCOMPLETE', 'NEGATIVE_BOUNDARY', 'BLOCKED'):
            with self.subTest(target=target):
                self.result['hard_target_disposition'] = target
                self.persist_result()
                self.review(self.assessment())
                with self.assertRaisesRegex(ValueError, 'cannot retype'):
                    self.build()

    def test_parent_scope_new_tasks_missing_gates_and_closed_parent_stay_rejected(self):
        self.review(self.assessment())
        for change, message in (({'terminal_scope': 'PARENT'}, 'terminal_scope TASK'),
                                ({'task_publications': [{'task_id':'OTHER','publication_id':'TP2-OTHER','task_role':'OTHER'}]}, 'cannot publish new tasks')):
            with self.subTest(change=change):
                with self.assertRaisesRegex(ValueError, message):
                    self.build(**change)
        gates = copy.deepcopy(self.gates)
        gates[0]['decision'] = 'REQUIRED'
        with self.assertRaisesRegex(ValueError, 'REQUIRED'):
            self.build(gate_decisions=gates)
        gates = copy.deepcopy(self.gates)
        next(g for g in gates if g['gate'] == 'EXTERNAL_PRIOR_ART_DUPLICATION')['decision'] = 'NOT_REQUIRED'
        with self.assertRaisesRegex(ValueError, 'EXTERNAL_PRIOR_ART'):
            self.build(gate_decisions=gates)
        with mock.patch.object(followup, '_objective_head', return_value={'objective_id':'OBJ-PARENT','objective_status':'CLOSED'}):
            with self.assertRaisesRegex(ValueError, 'parent'):
                self.build()
        packet = self.build()
        for flag in ('parent_completion_granted', 'parent_final_granted'):
            with self.subTest(flag=flag):
                with self.assertRaisesRegex(ValueError, 'parent completion/final'):
                    followup.validate_packet({**packet, flag: True}, self.root)

    def test_current_publication_mismatch_stays_rejected(self):
        self.review(self.assessment())
        self.publication = {**self.publication, 'publication_id': 'TP2-NEW'}
        with self.assertRaises(ValueError):
            self.build()

    def test_existing_positive_pass_success_paths_and_literal_rvs_keep_working(self):
        for verdict in ('PASS', 'SUCCESS', 'AUDIT_COMPLETE'):
            with self.subTest(verdict=verdict):
                self.result.update(terminal_verdict=verdict, hard_target_disposition='SATISFIED')
                self.persist_result()
                self.review(None)
                packet = self.build()
                self.assertEqual(packet['terminal_scope'], 'TASK')
        # Start a clean current set, retaining its raw files as nonoperational history.
        self.sources.clear()
        self.review(None)
        self.review(None, driver=OTHER)
        self.synthesize()
        self.build()

    def test_pass_nonliteral_rvs_uses_existing_ten_field_assessment(self):
        self.result.update(terminal_verdict='PASS', hard_target_disposition='ACHIEVED_BY_EXACT_PROOF')
        self.persist_result()
        value = self.assessment()
        self.assertEqual(len(value), 10)
        self.review(value)
        self.review(None, driver=OTHER)
        self.synthesize()
        self.build()


if __name__ == '__main__':
    unittest.main()
