"""Exercise the real isolated pytest worker without running an entire shard."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest import mock

from scripts import run_unittest_shard as runner


class PytestShardAdapterTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def module(self, name, source):
        path = self.root / name
        path.write_text(textwrap.dedent(source), encoding='utf-8')
        return path

    def worker(self, *paths):
        env = dict(os.environ, PYTEST_DISABLE_PLUGIN_AUTOLOAD='1')
        env.pop('PYTEST_ADDOPTS', None)
        return subprocess.run([sys.executable, str(Path(runner.__file__).resolve()),
                               '--pytest-files', *map(str, paths)], cwd=runner.ROOT,
                              env=env, text=True, capture_output=True, timeout=45)

    def test_classification_is_static_and_preserves_pure_unittest(self):
        ordinary = self.module('test_plain.py', '''
            import unittest
            class TestPlain(unittest.TestCase):
                def test_plain(self): pass
        ''')
        fixture = self.module('test_fixture.py', '''
            raise AssertionError('classification must not import')
            def test_uses_fixture(tmp_path): pass
        ''')
        lifecycle = self.module('test_lifecycle.py', '''
            def teardown_module(): pass
            def test_plain(): pass
        ''')
        marked = self.module('test_marked.py', '''
            @some_mark
            def test_plain(): pass
        ''')
        self.assertEqual(([ordinary], [fixture, lifecycle, marked]),
                         runner.partition_files([ordinary, fixture, lifecycle, marked]))

    def test_mixed_module_parameters_fixture_teardown_and_bootstrap_execute_once(self):
        marker = self.root / 'events.txt'
        path = self.module('test_mixed.py', f'''
            from pathlib import Path
            import unittest
            import pytest
            from tools import research_dispatch
            assert research_dispatch._canonical_control_bootstrap_installed
            marker = Path({str(marker)!r})
            def event(value):
                with marker.open('a') as stream: stream.write(value + '\\n')
            event('import')
            @pytest.fixture
            def resource():
                event('setup')
                yield 3
                event('teardown')
            @pytest.mark.parametrize('value', [1, 2])
            def test_parameter(value, resource):
                assert value < resource
                event('parameter-' + str(value))
            class Mixed(unittest.TestCase):
                def test_unit(self): event('unit')
            def teardown_module(): event('module-teardown')
        ''')
        result = self.worker(path)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('cases=3 collection_skipped=0', result.stdout)
        events = marker.read_text().splitlines()
        self.assertEqual(1, events.count('import'))
        self.assertEqual(1, events.count('unit'))
        self.assertEqual(2, events.count('setup'))
        self.assertEqual(2, events.count('teardown'))
        self.assertEqual(1, events.count('module-teardown'))
        self.assertEqual({'parameter-1', 'parameter-2'}, {event for event in events if event.startswith('parameter-')})

    def test_explicit_test_and_module_skips_remain_visible(self):
        path = self.module('test_skip.py', '''
            import pytest
            @pytest.mark.skip(reason='visible fixture skip')
            def test_skipped(): raise AssertionError('must skip')
        ''')
        result = self.worker(path)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('visible fixture skip', result.stdout)
        self.assertIn('cases=1', result.stdout)
        module_skip = self.module('test_module_skip.py', '''
            import pytest
            pytest.skip('visible module skip', allow_module_level=True)
        ''')
        result = self.worker(module_skip)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('visible module skip', result.stdout)
        self.assertIn('cases=0 collection_skipped=1', result.stdout)

    def test_empty_collection_missing_fixture_and_failure_are_nonzero(self):
        cases = {
            'empty': 'VALUE = 3',
            'fixture': 'def test_missing(nonexistent_fixture): pass',
            'failure': 'def test_failed(): assert False',
            'import': "raise RuntimeError('collection failure')",
            'async': 'async def test_async(): pass',
        }
        for label, source in cases.items():
            with self.subTest(label=label):
                result = self.worker(self.module('test_' + label + '.py', source))
                self.assertNotEqual(0, result.returncode, result.stdout + result.stderr)
        # An empty file must fail even when another file has runnable cases.
        result = self.worker(self.module('test_empty_mixed.py', 'VALUE = 3'),
                             self.module('test_one.py', 'def test_one(): assert True'))
        self.assertNotEqual(0, result.returncode)
        self.assertIn('zero-case files=', result.stderr)

    def test_pytest_files_use_one_child_and_cannot_inherit_selection_options(self):
        files = [self.root / 'test_a.py', self.root / 'test_b.py']
        with mock.patch.dict(os.environ, {'PYTEST_ADDOPTS': '-k silently_drop'}), \
                mock.patch.object(runner.subprocess, 'run') as run:
            run.return_value.returncode = 1
            self.assertEqual(1, runner.run_pytest_files(files))
        self.assertEqual(1, run.call_count)
        arguments = run.call_args.args[0]
        self.assertEqual([str(path.resolve()) for path in files], arguments[-2:])
        self.assertNotIn('PYTEST_ADDOPTS', run.call_args.kwargs['env'])
        self.assertEqual('1', run.call_args.kwargs['env']['PYTEST_DISABLE_PLUGIN_AUTOLOAD'])


if __name__ == '__main__':
    unittest.main()
