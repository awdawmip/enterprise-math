import importlib.util
import pathlib
import unittest

HERE=pathlib.Path(__file__).resolve().parent
CHECKER=HERE.parent/'research'/'r047p'/'check_r047p_foundation.py'

class R047PFoundationChecks(unittest.TestCase):
    def test_frozen_foundation_checker(self):
        spec=importlib.util.spec_from_file_location('r047p_checker',CHECKER)
        mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        self.assertEqual(len(list(mod.checks())),7)

if __name__=='__main__': unittest.main()
