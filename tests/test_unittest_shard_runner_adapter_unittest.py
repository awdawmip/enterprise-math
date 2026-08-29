import tempfile
import unittest
from pathlib import Path

from scripts import run_unittest_shard as runner


class UnittestShardRunnerAdapterTests(unittest.TestCase):
    def _module(self, root: str, name: str, source: str) -> Path:
        path = Path(root) / name
        path.write_text(source, encoding="utf-8")
        return path

    def test_zero_argument_top_level_tests_are_executed(self):
        with tempfile.TemporaryDirectory() as td:
            path = self._module(
                td,
                "test_top_level.py",
                """
def test_one():
    assert 1 + 1 == 2


def test_two():
    assert 'ab'.upper() == 'AB'
""",
            )
            suite = runner.load_file_suite(path)
            self.assertEqual(2, suite.countTestCases())
            result = unittest.TestResult()
            suite.run(result)
            self.assertTrue(result.wasSuccessful())
            self.assertEqual(2, result.testsRun)

    def test_unittest_cases_and_top_level_tests_both_execute(self):
        with tempfile.TemporaryDirectory() as td:
            path = self._module(
                td,
                "test_mixed.py",
                """
import unittest

class Case(unittest.TestCase):
    def test_class_case(self):
        self.assertTrue(True)


def test_top_level_case():
    assert 3 * 3 == 9
""",
            )
            suite = runner.load_file_suite(path)
            self.assertEqual(2, suite.countTestCases())
            result = unittest.TestResult()
            suite.run(result)
            self.assertTrue(result.wasSuccessful())
            self.assertEqual(2, result.testsRun)

    def test_required_fixture_parameter_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            path = self._module(
                td,
                "test_fixture.py",
                """
def test_needs_fixture(tmp_path):
    assert tmp_path
""",
            )
            with self.assertRaisesRegex(
                runner.TestDiscoveryContractError,
                "unsupported fixture/async semantics",
            ):
                runner.load_file_suite(path)

    def test_async_top_level_test_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            path = self._module(
                td,
                "test_async.py",
                """
async def test_async_case():
    return None
""",
            )
            with self.assertRaisesRegex(
                runner.TestDiscoveryContractError,
                "unsupported fixture/async semantics",
            ):
                runner.load_file_suite(path)


if __name__ == "__main__":
    unittest.main()
