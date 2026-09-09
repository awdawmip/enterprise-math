"""Execution-intent recursive directory scopes survive Result manifest freezing."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from control_plane import research_result_records_impl as results
from tools import research_execution_records as executions
from tests.test_research_task_record_compatibility import _write_current_record, _write_semantic_fixture


class RecursiveResultOutputScopeTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='em-result-recursive-output-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        _write_semantic_fixture(self.root)
        task_id = 'RS-RECURSIVE-SCOPE-FIXTURE'
        _write_current_record(self.root, task_id=task_id, publication_id='TP2-RECURSIVE-SCOPE-FIXTURE',
                              parent_objective_id='OBJ-SCOPE-FIXTURE', claimable=True)
        self.allowed = ['research_artifacts/FIXTURE/checkpoints/**',
                        'research_artifacts/FIXTURE/runs/**',
                        'research_returns/FIXTURE.md']
        self.execution = executions.prepare_intent(
            task_id=task_id, claim_id='fixture-recursive-scope', researcher_id='EM-FIXTURE-A1B2C3',
            theorem_owner='Temporary fixture owner', execution_branch='research/fixture',
            execution_branch_base='a' * 40, allowed_outputs=self.allowed, owner_lease_minutes=120,
            prepared_at='2026-09-09T00:00:00+00:00', root=self.root)
        path = self.root.joinpath('research_execution_records', task_id, self.execution['execution_record_id'] + '.json')
        path.parent.mkdir(parents=True)
        self.execution_bytes = (json.dumps(self.execution, indent=2) + '\n').encode('utf-8')
        path.write_bytes(self.execution_bytes)
        self.execution_path = path
        self.return_path = self.file('research_returns/FIXTURE.md')

    def file(self, relative):
        path = self.root.joinpath(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b'Finite local fixture.\n')
        return path

    def freeze(self, paths):
        return results.freeze_result(
            execution_record_id=self.execution['execution_record_id'], return_path=self.return_path,
            output_paths=paths, owner_head='b' * 40, terminal_verdict='PASS',
            hard_target_disposition='SATISFIED', unresolved_residue='NONE', method_harvest='RESULT_ONLY',
            independence_status='NOT_APPLICABLE', source_exposure_status='NOT_APPLICABLE',
            next_control_plane_recommendation='Review the temporary fixture.',
            frozen_at='2026-09-09T00:01:00+00:00', root=self.root)

    def test_prepare_then_freeze_recursive_checkpoints_and_runs(self):
        paths = [self.file('research_artifacts/FIXTURE/checkpoints/full_map_v3_binding.json'),
                 self.file('research_artifacts/FIXTURE/runs/identity_v3/nested/receipt.json')]
        record = self.freeze(paths)
        manifest = {row['path']: row for row in record['output_manifest']}
        self.assertEqual(set(manifest), {p.relative_to(self.root).as_posix() for p in paths + [self.return_path]})
        for path in paths:
            self.assertEqual(manifest[path.relative_to(self.root).as_posix()]['sha256'],
                             'sha256:' + hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual(self.execution_path.read_bytes(), self.execution_bytes)
        self.assertEqual(self.execution['allowed_outputs'], self.allowed)

    def test_sibling_directory_and_prefix_lookalike_remain_outside(self):
        for relative in ('research_artifacts/FIXTURE/checkpoints-other/binding.json',
                         'research_artifacts/FIXTURE/runs-other/receipt.json',
                         'research_artifacts/OTHER/runs/receipt.json',
                         'research_artifacts/FIXTURE/checkpoints/../outside.json'):
            with self.subTest(relative=relative):
                with self.assertRaisesRegex(results.ResultRecordError, 'outside execution authorization'):
                    self.freeze([self.file(relative)])

    def test_outside_repository_is_rejected_before_scope_matching(self):
        with tempfile.TemporaryDirectory(prefix='em-outside-scope-') as directory:
            path = Path(directory).joinpath('receipt.json')
            path.write_bytes(b'Outside.\n')
            with self.assertRaisesRegex(results.ResultRecordError, 'inside repository root'):
                self.freeze([path])

    def test_existing_exact_star_and_directory_rules_are_unchanged(self):
        for rule, relative in (('exact.json', 'exact.json'), ('legacy/*', 'legacy/deep/file.json'),
                               ('directory/', 'directory/file.json'), ('legacy-prefix*', 'legacy-prefix.txt'),
                               ('runs\\**', 'runs/deep/file.json')):
            with self.subTest(rule=rule):
                self.assertTrue(results._allowed_output(relative, [rule]))
        self.assertFalse(results._allowed_output('exact.json.backup', ['exact.json']))
        self.assertFalse(results._allowed_output('run-other/file.json', ['runs/**']))


if __name__ == '__main__':
    unittest.main()
