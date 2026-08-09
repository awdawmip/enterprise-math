import pathlib
import unittest


class ReusableInterfaceLeanImportTests(unittest.TestCase):
    def test_reusable_interface_is_exposed_by_root_target(self) -> None:
        root = pathlib.Path("EnterpriseMath.lean").read_text(encoding="utf-8")
        self.assertIn(
            "import EnterpriseMath.State.ReusableInterface",
            root,
        )


if __name__ == "__main__":
    unittest.main()
