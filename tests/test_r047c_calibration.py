import importlib.util, unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'research'/'r047c'/'check_r047c_calibration.py'
spec=importlib.util.spec_from_file_location('r047c_checker',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
class TestR047CCalibration(unittest.TestCase):
    def test_artifact_integrity(self): self.assertTrue(m.validate_artifacts())
    def test_rpe(self): self.assertTrue(m.check_rpe())
    def test_csr(self): self.assertTrue(m.check_csr())
    def test_balance(self): self.assertTrue(m.check_balance_conservation())
if __name__=='__main__': unittest.main()
