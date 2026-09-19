from __future__ import annotations
import tempfile,unittest
from pathlib import Path
from nollm_visual_toolkit import unit_log_phase_lab as u
from nollm_visual_toolkit import reciprocal_phase_lab as r
from nollm_visual_toolkit import multiplication_lab as m

class UnitLogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.spf=m.smallest_factors(65536)
    def test_group_table(self):
        for b in (6,8,11):
            t=u.dlog_table(b);self.assertEqual(len(t),1<<b);self.assertEqual(t[1],0)
    def test_direct_multiplication(self):
        for b in (8,11):
            M=1<<b;tab=u.dlog_table(b)
            for k in (2,3,5,7,11,31):
                pk=u.direct_phase(k,b,tab)
                for n in range(1,65536//k):self.assertEqual(u.direct_phase(k*n,b,tab),(u.direct_phase(n,b,tab)+pk)%M)
    def test_prime_adapter_equals_direct_all(self):
        for b in (8,11):
            M=1<<b;pt=u.prime_table(self.spf,b);via=r.phase_values(self.spf,pt,M);direct=u.phase_values_direct(65536,b);self.assertEqual(via,direct)
    def test_two_is_45_degrees(self):
        self.assertEqual(u.direct_phase(2,11),256);self.assertEqual(u.direct_phase(2,16),8192)
    def test_components_no_factorization_contract(self):
        v,e,t=u.components(3*5**4*2**7,11);self.assertEqual(v,7);self.assertIn(e,(0,1));self.assertTrue(0<=t<2048)
    def test_payload_preserves_source(self):
        p=u.payload(256,11);self.assertEqual(p['phase_bits'],11);self.assertEqual(p['data']['kind'],'hex');self.assertIn('unitlog',p)
    def test_template_patch(self):self.assertIn("S.mode==='unitlog'?P.unitlog[p]",u.patched_template())
    def test_reproducible_site(self):
        with tempfile.TemporaryDirectory() as d:
            a=u.build_site(d,count=256).read_bytes();b=u.build_site(d,count=256).read_bytes();self.assertEqual(a,b);self.assertTrue((Path(d)/'unit-log-11bit.html').exists())
if __name__=='__main__':unittest.main(verbosity=2)
