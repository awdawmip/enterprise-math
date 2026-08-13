import json, subprocess, sys, unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent

class R052BExactTests(unittest.TestCase):
    def test_synthetic_exact_checker(self):
        cp=subprocess.run([sys.executable,str(HERE/"check_r052b_exact.py"),
                           "--synthetic-only","--artifact-dir",str(HERE)],
                          check=True,text=True,capture_output=True)
        data=json.loads(cp.stdout)
        self.assertEqual(data["overall"],"PASS")
        self.assertEqual(data["pair_count"],10)
        self.assertEqual(data["primitive_half_lifts"],[-1,1])
        self.assertFalse(data["floating_point_used"])

    def test_protocol_frozen_pair_order(self):
        data=json.loads((HERE/"R052B_COMPARABILITY_PROTOCOL.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["role_order"]),5)
        self.assertEqual(data["pair_enumeration_rule"],
                         "All 10 unordered pairs i<j in role_order; no omissions and no directional double counting.")

if __name__=="__main__":
    unittest.main()
