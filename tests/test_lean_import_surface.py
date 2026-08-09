import pathlib
import unittest


class LeanImportSurfaceTests(unittest.TestCase):
    def test_p018_formal_modules_are_exposed_by_root_target(self) -> None:
        root = pathlib.Path("EnterpriseMath.lean").read_text(encoding="utf-8")
        required = (
            "import EnterpriseMath.Precision.QuotientBasin",
            "import EnterpriseMath.State.OperationCongruence",
            "import EnterpriseMath.State.ContextSeparation",
            "import EnterpriseMath.State.TransportProtocol",
        )
        for line in required:
            with self.subTest(import_line=line):
                self.assertIn(line, root)


if __name__ == "__main__":
    unittest.main()
