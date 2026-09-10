from __future__ import annotations
import tempfile,unittest
from pathlib import Path
from nollm_visual_toolkit import reciprocal_phase_lab as r
from nollm_visual_toolkit import multiplication_lab as m

class ReciprocalPhaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.spf=m.smallest_factors(65536)
    def test_inverse_definition_16(self):
        t=r.tables(self.spf,16)['inverse'];self.assertEqual(t[2],8192)
        for p in (3,5,7,11,13,65521):self.assertEqual(t[p]*p%65536,1)
    def test_inverse_definition_11(self):
        t=r.tables(self.spf,11)['inverse'];self.assertEqual(t[2],256)
        for p in (3,5,7,11,13):self.assertEqual(t[p]*p%2048,1)
    def test_phase_addition(self):
        M=2048;t=r.tables(self.spf,11)['inverse'];phi=r.phase_values(self.spf,t,M)
        for k in (2,3,5,7,11,31):
            for n in range(1,65536//k):self.assertEqual(phi[k*n],(phi[k]+phi[n])%M)
    def test_invalid_bits(self):
        for b in (5,25,True,6.0):
            with self.assertRaises(ValueError):r.modulus(b)
    def test_payload_preserves_source(self):
        p=r.payload(256,11);self.assertEqual(p['phase_bits'],11);self.assertEqual(p['modulus'],2048);self.assertEqual(p['data']['kind'],'hex')
    def test_template_patch_unique(self):self.assertIn("S.mode==='inverse'?P.inverse[p]",r.patched_template())
    def test_build_reproducible(self):
        with tempfile.TemporaryDirectory() as d:
            a=r.build(Path(d)/'a.html',count=256,phase_bits=11).read_bytes();b=r.build(Path(d)/'b.html',count=256,phase_bits=11).read_bytes();self.assertEqual(a,b);self.assertIn(b'inverse',a)
    def test_site_has_both_resolutions(self):
        with tempfile.TemporaryDirectory() as d:
            p=r.build_site(d,count=256);self.assertTrue(p.exists());self.assertTrue((Path(d)/'reciprocal-11bit.html').exists());self.assertTrue((Path(d)/'reciprocal-16bit.html').exists())
if __name__=='__main__':unittest.main(verbosity=2)
