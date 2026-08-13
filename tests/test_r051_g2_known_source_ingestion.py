import importlib.util, pathlib, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('r051g2', ROOT/'tools'/'check_r051_g2_known_source_ingestion.py')
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
class TestR051G2KnownSourceIngestion(unittest.TestCase):
    def test_exact_packet(self):
        self.assertEqual(MOD.check(ROOT/'research_outputs'/'R051'), [])
    def test_exact_k1_sidecar(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/'x.sha256'; p.write_bytes(MOD.EXPECTED_K1_SHA.encode('ascii'))
            self.assertTrue(MOD.verify_k1_sidecar(p))
    def test_sidecar_rejects_extra_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/'x.sha256'; p.write_bytes((MOD.EXPECTED_K1_SHA+'\n').encode('ascii'))
            with self.assertRaises(ValueError): MOD.verify_k1_sidecar(p)
if __name__=='__main__': unittest.main()
