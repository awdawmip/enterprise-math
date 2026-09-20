from __future__ import annotations
import copy
import json
import math
import tempfile
import unittest
from pathlib import Path
from nollm_visual_toolkit import multiplicative as m

class MultiplicativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full=m.build_field();cls.small=m.build_field(m.config(1024))
    def test_all_labels_preserved(self):
        self.assertEqual([r['n'] for r in self.full['records']],list(range(65536)))
        self.assertEqual(len({r['id'] for r in self.full['records']}),65536)
    def test_zero_is_not_a_phase(self):
        r=self.full['records'][0];self.assertIsNone(r['phase']);self.assertIsNone(r['omega'])
        self.assertEqual(m.multiplication(self.full,0,7)['ideal_relative_error'],0)
    def test_identity(self):
        self.assertEqual(self.full['records'][1]['phase'],0)
        self.assertEqual(self.full['records'][1]['ideal'],[1,0])
    def test_all_ordered_pairs(self):
        r=m.all_pair_audit(self.full)
        self.assertEqual(r['ordered_positive_pairs'],736957)
        self.assertEqual(r['phase_failures'],0);self.assertEqual(r['omega_failures'],0)
    def test_factorization_all(self):
        for n in range(1,65536):
            f=m.factors(n,self.full);self.assertEqual(math.prod(p**e for p,e in f),n)
            self.assertEqual(sum(e for p,e in f),self.full['records'][n]['omega'])
    def test_phases_exact_integer(self):
        for r in self.full['records'][1:]:
            self.assertIsInstance(r['phase'],int);self.assertTrue(0<=r['phase']<65536)
    def test_prime_count(self):
        self.assertEqual(sum(r['prime'] for r in self.full['records']),6542)
    def test_custom_phase_valuation_effect(self):
        other=m.build_field(m.config(1024,overrides={'5':12345}))
        delta=(12345-self.small['prime_phase'][5])%65536
        for n in range(1,1024):
            e=dict(m.factors(n,self.small)).get(5,0)
            self.assertEqual((other['records'][n]['phase']-self.small['records'][n]['phase'])%65536,e*delta%65536)
        self.assertEqual(m.all_pair_audit(other)['phase_failures'],0)
    def test_mixed_all_pairs(self):
        f=m.build_field(m.config(scheme='mixed'))
        self.assertEqual(m.all_pair_audit(f)['phase_failures'],0)
        self.assertGreater(m.statistics(f)['distinct_phases'],20000)
    def test_radial_is_not_uniform(self):
        f=m.build_field(m.config(1024,'radial'))
        self.assertEqual(m.all_pair_audit(f)['phase_failures'],0)
        self.assertGreater(m.statistics(f)['area_sector_cv'],5)
    def test_spiral_is_not_multiplicative(self):
        f=m.build_field(m.config(1024,'spiral'))
        self.assertNotEqual(m.multiplication(f,5,7)['phase_defect'],0)
        self.assertGreater(m.all_pair_audit(f)['phase_failures'],0)
    def test_scale_changes_display_not_phase(self):
        f=m.build_field(m.config(1024,scale=2))
        for a,b in zip(f['records'],self.small['records']):
            self.assertEqual(a['phase'],b['phase'])
            for x,y in zip(a['ideal'],b['ideal']):self.assertAlmostEqual(x,2*y)
    def test_radius_exact_numerical(self):
        for r in self.full['records']:
            self.assertAlmostEqual(math.hypot(*r['ideal']),math.sqrt(r['n']),places=10)
    def test_nearest_center_bound(self):
        s=m.statistics(self.full)
        self.assertLessEqual(s['max_display_quantization_error'],1/math.sqrt(3)+1e-10)
    def test_density_population_and_zero_boundary(self):
        s=m.statistics(self.full)
        self.assertEqual(sum(map(sum,s['grid'])),65535)
        self.assertEqual(s['positive_population'],65535)
    def test_collisions_preserve_identities(self):
        d=m.hex_data(self.full)
        self.assertEqual(len(d['records']),65536)
        self.assertEqual(d['schema'],'NOLLM_VISUAL_DATA_V2')
        self.assertEqual(len({tuple(r['coord']) for r in d['records']}),44731)
        self.assertTrue(all('phase' in r['fields'] for r in d['records']))
    def test_out_of_range_no_wrap(self):
        d=m.multiplication(self.full,65535,65535)
        self.assertFalse(d['in_range']);self.assertEqual(d['product'],4294836225)
    def test_floating_test_distinct_from_phase(self):
        for a in range(1,128):
            d=m.multiplication(self.full,a,129)
            self.assertEqual(d['phase_defect'],0);self.assertLess(d['ideal_relative_error'],3e-14)
    def test_invalid_inputs(self):
        for x in (0,15,65537,True,3.5):
            with self.assertRaises(ValueError):m.config(x)
        for x in (-1,0,5,float('nan'),True):
            with self.assertRaises(ValueError):m.config(scale=x)
        for o in ({'4':2},{'05':2},{'5':-1},{'5':True},{'5':65536},{'2':.5}):
            with self.assertRaises(ValueError):m.config(overrides=o)
    def test_invalid_labels(self):
        for a,b in ((-1,3),(65536,3),(True,2),(3.5,7)):
            with self.assertRaises(ValueError):m.multiplication(self.full,a,b)
    def test_configuration_exact_shape(self):
        c=m.config();c['arbitrary']='reject'
        with self.assertRaises(ValueError):m.checked_config(c)
    def test_deterministic_html(self):
        with tempfile.TemporaryDirectory() as td:
            a=m.render(Path(td)/'a.html',m.config(16));b=m.render(Path(td)/'b.html',m.config(16))
            self.assertEqual(a.read_bytes(),b.read_bytes());self.assertNotIn('__LAB_SEED__',a.read_text())
    def test_json_preserves_raw_phase_and_origin(self):
        d=m.hex_data(self.small);self.assertEqual(json.loads(json.dumps(d)),d)
        self.assertIsNone(d['records'][0]['fields']['phase'])
        self.assertIn('NOT Nollm physical layer',d['metadata']['layer_semantics'])

if __name__=='__main__':unittest.main(verbosity=2)
