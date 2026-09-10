import copy
import json
import tempfile
import unittest
from pathlib import Path
from nollm_visual_toolkit import phase32_lab as m

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full=m.build();cls.small=m.build(dict(count=256))
    def test_all_65536_ids_and_zero(self):
        self.assertEqual(len(self.full['phase']),65536)
        self.assertIsNone(m.factors(self.full,0));self.assertEqual(m.position(self.full,0),0j)
        self.assertEqual(m.factors(self.full,1),[])
        self.assertEqual(len(self.full['primes']),6542)
    def test_all_phase_products_in_range(self):
        f=self.full['phase']
        for a in range(1,65536):
            for b in range(1,65536//a + (65536%a>0)):
                if a*b<65536:self.assertEqual(f[a*b],(f[a]+f[b])%m.DEN)
    def test_reconstruct_every_factorization(self):
        for n in range(1,65536):
            v=1
            for p,e in m.factors(self.full,n):v*=p**e
            self.assertEqual(v,n)
    def test_perturb_only_multiples_and_valuation(self):
        f=self.small['phase'];t=m.build(dict(count=256,overrides={'5':1234567}));delta=(1234567-f[5])%m.DEN
        for n in range(1,256):
            e=dict(m.factors(t,n)).get(5,0)
            self.assertEqual((t['phase'][n]-f[n])%m.DEN,e*delta%m.DEN)
    def test_hash_multiplicative(self):
        f=m.build(dict(count=256,mode='hash',seed=123))['phase']
        for a in range(1,256):
            for b in range(1,256//a):self.assertEqual(f[a*b],(f[a]+f[b])%m.DEN)
    def test_spiral_control_fails(self):
        f=m.build(dict(count=256,mode='spiral'))
        self.assertNotEqual(m.multiplication(f,2,2)['phase_defect_uint32'],0)
    def test_continuous_error_and_zero(self):
        for a,b in [(1,65535),(2,3),(5,7),(11,13),(31,37),(127,251),(0,23)]:
            self.assertLess(m.multiplication(self.full,a,b)['continuous_relative_error'],1e-13)
    def test_outside_no_wrap(self):
        r=m.multiplication(self.full,65535,2);self.assertEqual(r['product'],131070);self.assertFalse(r['in_domain'])
    def test_hex_six_directions(self):
        for c in [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]:
            z=complex(c[0]+c[1]/2,m.math.sqrt(3)*c[1]/2)
            self.assertEqual(m.quantize(z),c)
    def test_metrics_count_all_positive(self):
        r=m.metrics(self.small)
        self.assertEqual(sum(r['angular_counts']),255);self.assertEqual(sum(r['equal_area_counts']),255)
        self.assertEqual(r['occupied_cells']+r['collision_excess'],255)
    def test_invalid(self):
        for c in [dict(count=65537),dict(count=True),dict(seed=-1),dict(pitch=0),dict(unknown=2),dict(overrides={'4':3}),dict(overrides={'05':3}),dict(overrides={'5':m.DEN}),dict(a=-1),dict(zoom=float('nan'))]:
            with self.assertRaises(ValueError):m.build(c)
    def test_camera_invariance(self):
        x=m.build(dict(count=256,yaw=1.2,tilt=.8,view='layers'))
        self.assertEqual(x['phase'],self.small['phase']);self.assertEqual(m.metrics(x),m.metrics(self.small))
    def test_zero_position_grid(self):self.assertEqual(m.quantize(0j),(0,0))
    def test_deterministic_html_and_config(self):
        with tempfile.TemporaryDirectory() as d:
            a=m.render(Path(d)/'one.html');b=m.render(Path(d)/'two.html')
            self.assertEqual(a.read_bytes(),b.read_bytes());self.assertNotIn('__CONFIG__',a.read_text())
    def test_site_three_pages_and_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            index=m.build_site(d,count=32)
            manifest=json.loads((Path(d)/'manifest.json').read_text())
            self.assertEqual(len(manifest['pages']),3)
            self.assertTrue(index.exists())
            for page in manifest['pages']:
                raw=(Path(d)/page['href']).read_bytes()
                self.assertEqual(m.hashlib.sha256(raw).hexdigest(),page['sha256'])
            old=index.read_bytes();self.assertEqual(m.build_site(d,32).read_bytes(),old)
    def test_v2_adapter_retains_identities(self):
        d=m.hex_data(self.small)
        self.assertEqual(d['schema'],'NOLLM_VISUAL_DATA_V2')
        self.assertEqual(len(d['records']),256)
        for n,r in enumerate(d['records']):
            self.assertEqual(r['id'],str(n));self.assertEqual(r['n'],n)
            self.assertEqual(r['fields']['phase_denominator'],m.DEN)
        self.assertIsNone(d['records'][0]['fields']['omega'])
    def test_config_copy_not_mutated(self):
        c=dict(overrides={'5':77});d=copy.deepcopy(c);m.build(c);self.assertEqual(c,d)

if __name__=='__main__':unittest.main(verbosity=2)
