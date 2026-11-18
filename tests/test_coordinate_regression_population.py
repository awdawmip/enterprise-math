"""Exercise the pinned coordinate comparison without fetching a baseline worktree."""
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools import check_coordinate_regressions as gate


class CoordinateRegressionPopulationTests(unittest.TestCase):
    def setUp(self):
        self.common = ('tests.example.Contract', 'test_common')
        self.old = {(gate.X6_JUNIT_CLASS, k): None for k in gate.X6_SUCCESSORS}
        self.new = {(gate.X6_JUNIT_CLASS, k): None for k in gate.X6_SUCCESSORS.values()}
        self.old[self.common] = self.new[self.common] = None

    def test_ratified_change_accepts_real_recovery_and_reports_old_failure_separately(self):
        key = (gate.X6_JUNIT_CLASS, 'test_twenty_four_errors_require_the_new_validated_isolation')
        self.old[key] = 'historical heading diagnostics'
        gate.compare_population(self.old, self.new)
        name = gate.X6_SUCCESSORS[key[1]]
        self.new[gate.X6_JUNIT_CLASS, name] = self.old[key]
        with self.assertRaisesRegex(AssertionError, 'Failed successor'):
            gate.compare_population(self.old, self.new)

    def test_missing_or_unrelated_replacement_fails_even_with_same_count(self):
        self.new.pop(next(iter(self.new)))
        with self.assertRaisesRegex(AssertionError, 'Changed regression population'):
            gate.compare_population(self.old, self.new)
        self.new['tests.unrelated.Other', next(iter(gate.X6_SUCCESSORS.values()))] = None
        with self.assertRaisesRegex(AssertionError, 'Changed regression population'):
            gate.compare_population(self.old, self.new)

    def test_all_baseline_cases_remain_required_and_extra_passing_tests_are_allowed(self):
        extra = ('tests.extra', 'test_other')
        self.old[extra] = None
        with self.assertRaisesRegex(AssertionError, 'Changed regression population'):
            gate.compare_population(self.old, self.new)
        del self.old[extra]
        self.new[extra] = None
        gate.compare_population(self.old, self.new)
        self.new[extra] = 'new regression'
        with self.assertRaisesRegex(AssertionError, 'New failing test'):
            gate.compare_population(self.old, self.new)

    def test_common_failure_must_match_in_full(self):
        self.old[self.common] = self.new[self.common] = 'error\nfull historical detail'
        gate.compare_population(self.old, self.new)
        for candidate in ('error\nchanged detail', 'new error'):
            self.new[self.common] = candidate
            with self.assertRaisesRegex(AssertionError, 'New or changed failure'):
                gate.compare_population(self.old, self.new)
        self.new[self.common] = None
        gate.compare_population(self.old, self.new)
        self.old[self.common], self.new[self.common] = None, 'new failure'
        with self.assertRaisesRegex(AssertionError, 'New or changed failure'):
            gate.compare_population(self.old, self.new)

    def test_changed_named_tests_require_the_ratified_assertions(self):
        with tempfile.TemporaryDirectory() as work:
            root = Path(work)
            source = root / gate.X6_TEST_FILE
            source.parent.mkdir()
            subprocess.run(['git', 'init', '-q'], cwd=root, check=True)
            approved = b'# original accepted tests\n'
            blob = subprocess.check_output(['git', 'hash-object', '-w', '--stdin'],
                                           cwd=root, input=approved).decode().strip()
            with patch.object(gate, 'X6_TEST_BLOB', blob):
                source.write_bytes(approved)
                with patch.object(gate, 'run') as run:
                    self.assertEqual('CURRENT_TEST_FILE_MATCHES_RATIFIED_BLOB',
                                     gate.verify_successor_evidence(root, root))
                    run.assert_not_called()
                source.write_bytes(b'# superficially passing substitute\n')

                def fail_original(root_arg, out, targets):
                    self.assertEqual(root, root_arg)
                    self.assertEqual(set(gate.X6_SUCCESSORS.values()),
                                     {t.rsplit('::', 1)[1] for t in targets})
                    archived = Path(targets[0].split('::', 1)[0])
                    self.assertEqual(source.parent, archived.parent)
                    self.assertEqual(approved, archived.read_bytes())
                    return {(gate.X6_JUNIT_CLASS, t.rsplit('::', 1)[1]): 'real failure'
                            for t in targets}

                with patch.object(gate, 'run', side_effect=fail_original):
                    with self.assertRaisesRegex(AssertionError, 'Ratified X6 contract failed'):
                        gate.verify_successor_evidence(root, root)
                self.assertEqual([source], list(source.parent.glob('*.py')))


if __name__ == '__main__':
    unittest.main()
