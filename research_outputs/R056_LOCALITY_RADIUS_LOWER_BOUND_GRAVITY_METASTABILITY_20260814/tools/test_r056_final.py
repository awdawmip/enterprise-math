import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class R056FinalTests(unittest.TestCase):
    def test_frozen_hashes(self):
        expected={
        "R056_LOCALITY_MODEL.json":"1f610591b3f32b1540da1fa55733faeb1ec1a1fff054902affb087626cda729a",
        "R056_SHELL_ESCAPE_PROTOCOL.json":"746d154f39f108c75c779cbeceb5ae6b35c4bb692c62486a2209766b316bb45a",
        "R056_COMPUTATION_REGISTRY.json":"d87e107b814090d4ec528a7a593d0119b26666fa82070a6e5c967f6dd6be09ea",
        "R056_MULTI_REPLACEMENT_IDENTITY.json":"a07325d019f9ebced6108d69f831aa72570fa3d2a3e43cd2726c1cb11f6cf8f6",
        "R056_THEOREM_COUNTEREXAMPLE_LEDGER.json":"3f4506c6b177cf021929075c2835621eeda742051e80f471adda2482a8fcc27c"}
        for f,h in expected.items():
            self.assertEqual(hashlib.sha256((ROOT/f).read_bytes()).hexdigest(),h)
    def test_holdout(self):
        d=json.loads((ROOT/"R056_HOLDOUT_RESULTS.json").read_text())
        self.assertEqual(d["holdout_radii"],[7,9,11,13,17,24])
        self.assertTrue(all(x["holdout_validation_status"]=="PASS" for x in d["results"]))
    def test_final_classification(self):
        m=json.loads((ROOT/"R056_LOCALITY_SCALING_ATLAS.json").read_text())
        self.assertEqual(m["primary_classification"],"FINITE_LOCAL_COOPERATIVE_ESCAPE_FOUND")
        self.assertEqual(m["exact_theorem"]["statement"],"rho_m(r)=3")
if __name__=="__main__": unittest.main(verbosity=2)
