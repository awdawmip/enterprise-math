import importlib.util, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('r051check', ROOT/'tools'/'check_r051_quantitative_holdout.py')
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
class TestR051QuantitativeHoldout(unittest.TestCase):
    def test_exact_packet(self):
        self.assertEqual(MOD.check(ROOT/'research_outputs'/'R051'), [])
if __name__=='__main__': unittest.main()
