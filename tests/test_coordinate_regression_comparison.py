"""Fail-closed comparison across one source-pinned governance evolution."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'coordinate_regressions', ROOT / 'tools/check_coordinate_regressions.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
REVIEWED_AFTER_BLOB = 'fcc87fd7e0528ab7d2bf028deba0e982896aecc4'


class CoordinateRegressionComparisonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='em-regression-gate-')
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name) / 'baseline'
        self.current = Path(self.tmp.name) / 'current'
        for root, content in ((self.base, 'synthetic historical test source\n'),
                              (self.current, 'synthetic current test source\n')):
            file = root / gate.EVOLUTION_FILE
            file.parent.mkdir(parents=True)
            file.write_text(content, encoding='utf-8')
        self.policy = {
            'body_style_required': False,
            'core_invariants': ['V2_PUBLICATION_REQUIRES_SUBSTANTIVE_NONPLACEHOLDER_BODY'],
        }
        self.write_policy()
        for key, root in (('BEFORE_TEST_BLOB', self.base), ('AFTER_TEST_BLOB', self.current)):
            patch = mock.patch.object(gate, key, gate.git_blob_sha1(root / gate.EVOLUTION_FILE))
            patch.start()
            self.addCleanup(patch.stop)
        self.shared = ('tests.fixture.SharedTests', 'test_preserved')
        self.old = {self.shared: None}
        self.old.update({(gate.EVOLUTION_CLASS, name): None for name in gate.BEFORE_CASES})
        self.new = {self.shared: None}
        self.new.update({(gate.EVOLUTION_CLASS, name): None for name in gate.AFTER_CASES})

    def write_policy(self):
        (self.current / gate.EVOLUTION_POLICY).write_text(json.dumps(self.policy), encoding='utf-8')

    def compare(self, old=None, new=None):
        return gate.compare_results(self.old if old is None else old,
                                    self.new if new is None else new,
                                    self.base, self.current)

    def test_identical_population_retains_original_strict_comparison(self):
        same = {self.shared: None}
        result = self.compare(same, same)
        self.assertEqual(result['status'], 'NO_NEW_COORDINATE_REGRESSION')
        self.assertTrue(result['regression_population_unchanged'])
        self.assertEqual(result['semantic_evolutions'], [])

    def test_identical_historical_failure_is_retained_not_marked_passed(self):
        same = {self.shared: 'AssertionError\nexact evidence'}
        result = self.compare(same, same)
        self.assertEqual(result['baseline_failures'], 1)
        self.assertEqual(result['candidate_failures'], 1)
        self.assertFalse(result['complete_suite_green'])
        self.assertFalse(result['candidate_suite_green'])
        self.assertEqual(result['retained_failures'][0]['detail'], same[self.shared])

    def test_improved_historical_failure_remains_reported(self):
        result = self.compare({self.shared: 'old failure'}, {self.shared: None})
        self.assertTrue(result['candidate_suite_green'])
        self.assertFalse(result['complete_suite_green'])
        self.assertEqual(result['baseline_failure_evidence'][0]['detail'], 'old failure')

    def test_new_failure_with_unchanged_identity_is_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'New failing test'):
            self.compare({self.shared: None}, {self.shared: 'new failure'})

    def test_changed_retained_failure_is_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'Changed failure'):
            self.compare({self.shared: 'old detail'}, {self.shared: 'new detail'})

    def test_semantic_evolution_is_explicit_and_preserves_old_failure_fact(self):
        key = (gate.EVOLUTION_CLASS, 'test_twenty_four_errors_require_the_new_validated_isolation')
        self.old[key] = 'historical failure still failed'
        result = self.compare()
        self.assertIn('DECLARED_SEMANTIC_EVOLUTION', result['status'])
        self.assertFalse(result['regression_population_unchanged'])
        self.assertEqual(result['shared_test_identities_compared'], 1)
        self.assertEqual(result['baseline_tests_executed'], 5)
        self.assertEqual(result['candidate_tests_executed'], 5)
        change = result['semantic_evolutions'][0]
        self.assertEqual(change['source_commit'], 'dd7b10b680fc7a0c69e551ccf793f7e77d131b65')
        self.assertFalse(change['same_semantics_claimed'])
        self.assertEqual(len(change['historical_cases']), 4)
        self.assertEqual(len(change['current_cases']), 4)
        self.assertEqual(sum(x['outcome'] == 'failed' for x in change['historical_cases']), 1)
        self.assertEqual(result['baseline_failure_evidence'][0]['detail'], self.old[key])
        self.assertFalse(result['complete_suite_green'])
        self.assertTrue(result['candidate_suite_green'])

    def test_every_current_evolution_test_must_pass(self):
        for name in gate.AFTER_CASES:
            new = dict(self.new)
            new[(gate.EVOLUTION_CLASS, name)] = 'failure'
            with self.subTest(name=name), self.assertRaisesRegex(
                    AssertionError, 'Current semantic-evolution tests must all pass'):
                self.compare(new=new)

    def test_shared_new_failure_still_fails_during_registered_evolution(self):
        self.new[self.shared] = 'new failure'
        with self.assertRaisesRegex(AssertionError, 'New failing test'):
            self.compare()

    def test_shared_unchanged_failure_keeps_full_evidence(self):
        self.old[self.shared] = self.new[self.shared] = 'same exact failure'
        result = self.compare()
        self.assertEqual(result['retained_failures'][0]['detail'], 'same exact failure')
        self.assertFalse(result['candidate_suite_green'])

    def test_unknown_add_delete_and_rename_fail_without_evolution(self):
        old = {self.shared: None, ('tests.fixture', 'test_other'): None}
        for operation in ('add', 'delete', 'rename'):
            new = dict(old)
            if operation in ('delete', 'rename'):
                del new[self.shared]
            if operation in ('add', 'rename'):
                new[('tests.fixture', 'test_unknown')] = None
            with self.subTest(operation=operation), self.assertRaisesRegex(
                    AssertionError, 'outside registered semantic evolution'):
                self.compare(old, new)

    def test_unknown_population_changes_alongside_evolution_fail(self):
        for operation in ('add', 'delete', 'rename'):
            new = dict(self.new)
            if operation in ('delete', 'rename'):
                del new[self.shared]
            if operation in ('add', 'rename'):
                new[('tests.fixture', 'test_unknown')] = None
            with self.subTest(operation=operation), self.assertRaisesRegex(
                    AssertionError, 'outside registered semantic evolution'):
                self.compare(new=new)

    def test_partial_or_restored_transition_is_not_accepted(self):
        for operation in ('missing_old', 'missing_new', 'restored_old'):
            old, new = dict(self.old), dict(self.new)
            if operation == 'missing_old':
                del old[(gate.EVOLUTION_CLASS, next(iter(gate.BEFORE_CASES)))]
            elif operation == 'missing_new':
                del new[(gate.EVOLUTION_CLASS, next(iter(gate.AFTER_CASES)))]
            else:
                new[(gate.EVOLUTION_CLASS, next(iter(gate.BEFORE_CASES)))] = None
            with self.subTest(operation=operation), self.assertRaisesRegex(
                    AssertionError, 'outside registered semantic evolution'):
                self.compare(old, new)

    def test_historical_source_drift_is_rejected(self):
        (self.base / gate.EVOLUTION_FILE).write_text('changed historical source')
        with self.assertRaisesRegex(AssertionError, 'Historical semantic-evolution test source changed'):
            self.compare()

    def test_current_source_drift_with_same_names_is_rejected(self):
        (self.current / gate.EVOLUTION_FILE).write_text('same names, changed assertions')
        with self.assertRaisesRegex(AssertionError, 'requires explicit review'):
            self.compare()

    def test_missing_historical_source_is_not_a_bypass(self):
        (self.base / gate.EVOLUTION_FILE).unlink()
        with self.assertRaises(FileNotFoundError):
            self.compare()

    def test_policy_reversal_or_weakened_content_contract_is_rejected(self):
        original = copy.deepcopy(self.policy)
        for operation in ('required_true', 'false_as_integer', 'mandatory_sections',
                          'old_invariant', 'missing_content_invariant'):
            self.policy = copy.deepcopy(original)
            if operation == 'required_true':
                self.policy['body_style_required'] = True
            elif operation == 'false_as_integer':
                self.policy['body_style_required'] = 0
            elif operation == 'mandatory_sections':
                self.policy['mandatory_body_sections'] = ['fixed heading']
            elif operation == 'old_invariant':
                self.policy['core_invariants'].append('V2_PUBLICATION_REQUIRES_FILLED_MANDATORY_BODY_SECTIONS')
            else:
                self.policy['core_invariants'] = []
            self.write_policy()
            with self.subTest(operation=operation), self.assertRaisesRegex(
                    AssertionError, 'publication policy does not support'):
                self.compare()

    def test_missing_current_policy_is_not_a_bypass(self):
        (self.current / gate.EVOLUTION_POLICY).unlink()
        with self.assertRaises(FileNotFoundError):
            self.compare()

    def test_current_checkout_matches_reviewed_source_and_current_policy(self):
        self.assertEqual(gate.git_blob_sha1(ROOT / gate.EVOLUTION_FILE), REVIEWED_AFTER_BLOB)
        with mock.patch.object(gate, 'AFTER_TEST_BLOB', REVIEWED_AFTER_BLOB):
            gate.validate_evolution_sources(self.base, ROOT)

    def write_report(self, cases):
        suite = ET.Element('testsuite')
        for attributes, problem in cases:
            case = ET.SubElement(suite, 'testcase', attributes)
            if problem is not None:
                tag, message, detail = problem
                node = ET.SubElement(case, tag, {'message': message})
                node.text = detail
        out = Path(self.tmp.name) / 'junit.xml'
        ET.ElementTree(suite).write(out, encoding='utf-8')
        return out

    def test_junit_preserves_failure_details_and_normalizes_only_root(self):
        out = self.write_report([
            ({'classname': 'tests.fixture', 'name': 'test_pass'}, None),
            ({'classname': 'tests.fixture', 'name': 'test_fail'},
             ('failure', 'specific message', str(self.base) + '/test.py: details')),
        ])
        parsed = gate.parse_report(self.base, out)
        self.assertIsNone(parsed[('tests.fixture', 'test_pass')])
        self.assertEqual(parsed[('tests.fixture', 'test_fail')],
                         'specific message\n$ROOT/test.py: details')

    def test_junit_skip_error_duplicate_missing_and_empty_fail(self):
        good = {'classname': 'tests.fixture', 'name': 'test_case'}
        cases = {
            'skip': [(good, ('skipped', 'reason', 'detail'))],
            'error': [(good, ('error', 'reason', 'detail'))],
            'duplicate': [(good, None), (good, None)],
            'missing': [({'name': 'test_case'}, None)],
            'empty': [],
        }
        for operation, rows in cases.items():
            with self.subTest(operation=operation), self.assertRaises(AssertionError):
                gate.parse_report(self.base, self.write_report(rows))

    def test_runner_executes_original_complete_file_list(self):
        out = self.write_report([({'classname': 'tests.fixture', 'name': 'test_case'}, None)])
        with mock.patch.object(gate.subprocess, 'run', return_value=mock.Mock(returncode=0)) as run:
            gate.run(self.current, out)
        command = run.call_args.args[0]
        self.assertEqual(command[1:4], ['-m', 'pytest', '-q'])
        self.assertEqual(command[4:-1], gate.FILES)
        self.assertEqual(len(gate.FILES), 7)
        self.assertEqual(run.call_args.kwargs['cwd'], self.current)

    def test_runner_infrastructure_error_cannot_be_treated_as_old_failure(self):
        with mock.patch.object(gate.subprocess, 'run', return_value=mock.Mock(returncode=2)):
            with self.assertRaisesRegex(RuntimeError, 'Test infrastructure failure'):
                gate.run(self.current, Path(self.tmp.name) / 'absent.xml')

    def test_main_runs_both_populations_before_comparison_and_cleans_up(self):
        with (mock.patch.object(gate.tempfile, 'mkdtemp', return_value=self.tmp.name),
              mock.patch.object(gate.subprocess, 'run') as process,
              mock.patch.object(gate, 'run', side_effect=[self.old, self.new]) as run,
              mock.patch.object(gate, 'compare_results', side_effect=AssertionError('fixture comparison')) as compare):
            with self.assertRaisesRegex(AssertionError, 'fixture comparison'):
                gate.main()
        self.assertEqual(run.call_count, 2)
        self.assertEqual(run.call_args_list[0].args[0], Path(self.tmp.name) / 'baseline')
        self.assertEqual(run.call_args_list[1].args[0], ROOT)
        self.assertEqual(compare.call_args.args[:2], (self.old, self.new))
        self.assertEqual(process.call_args.args[0][:3], ['git', 'worktree', 'remove'])

    def test_comparison_does_not_mutate_result_evidence(self):
        original = copy.deepcopy((self.old, self.new))
        self.compare()
        self.assertEqual((self.old, self.new), original)


if __name__ == '__main__':
    unittest.main()
