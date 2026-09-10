from __future__ import annotations
import copy
import hashlib
import json
import math
import tempfile
import unittest
from decimal import Decimal, localcontext
from pathlib import Path
from nollm_visual_toolkit import core
from nollm_visual_toolkit import multiplication_lab as lab

class MultiplicationLabTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spf=lab.smallest_factors(65536)
        cls.data=core.demo_hex(65536)
        cls.phi=lab.phases(cls.spf,lab.prime_phases(cls.spf))

    def test_source_demo_fingerprint_is_released_baseline(self):
        self.assertEqual(core.fingerprint(self.data),'94df92927ff6952c86344ee2f38b428d273c7e749cb41343e25d5c2c5ae51160')

    def test_factorization_all_65536_integers(self):
        self.assertIsNone(lab.factors(0,self.spf));self.assertEqual(lab.factors(1,self.spf),[])
        for n in range(1,65536):
            fs=lab.factors(n,self.spf)
            self.assertEqual(math.prod(p**e for p,e in fs),n)
            for p,e in fs:self.assertEqual(self.spf[p],p);self.assertGreater(e,0)

    def test_golden_integer_formula_against_decimal(self):
        with localcontext() as ctx:
            ctx.prec=70; a=(Decimal(3)-Decimal(5).sqrt())/2
            for rank in (1,2,3,7,11,97,1024,6542,65536):
                self.assertEqual(lab.golden_tick(rank),int(rank*65536*a)%65536)

    def test_all_feasible_multiplication_pairs_2_to_127(self):
        for k in range(2,128):
            self.assertEqual(lab.phase_audit(self.phi,k)['phase_failures'],0)

    def test_override_effect_is_exact_valuation_multiple(self):
        a=lab.prime_phases(self.spf);diff=(8192-a[5])%65536
        b=lab.phases(self.spf,lab.prime_phases(self.spf,overrides={5:8192}))
        for n in range(1,65536):
            e=dict(lab.factors(n,self.spf)).get(5,0)
            self.assertEqual((b[n]-self.phi[n])%65536,e*diff%65536)

    def test_zero_phase_not_uniform(self):
        phi=lab.phases(self.spf,lab.prime_phases(self.spf,'zero'));d=lab.diagnostics(phi)
        self.assertEqual(d['angular_counts'][0],65535)
        self.assertAlmostEqual(d['angular_cv'],math.sqrt(63))

    def test_radix_four_true_and_two_false(self):
        self.assertEqual(lab.legacy_audit(self.data['records'],4)['coordinate_failures'],0)
        self.assertGreater(lab.legacy_audit(self.data['records'],2)['coordinate_failures'],0)
        self.assertEqual(lab.legacy_audit(self.data['records'],2)['first_witness']['n'],2)

    def test_declared_hex_product(self):
        self.assertEqual(lab.hex_product((0,1),(0,1)),(-1,1))

    def test_round_cell_centers(self):
        for q in range(-20,21):
            for r in range(-20,21):
                self.assertEqual(lab.rounded_hex(q+r/2,math.sqrt(3)*r/2),(q,r))

    def test_conservation_of_identity_counts(self):
        d=lab.diagnostics(self.phi)
        self.assertEqual(sum(d['angular_counts']),65535)
        self.assertEqual(d['occupied_cells']+d['excess_identities_if_collapsed'],65536)
        self.assertGreater(d['collision_groups'],0)

    def test_invalid_count(self):
        for n in (True,0,15,65537,16.0):
            with self.assertRaises(ValueError):lab.smallest_factors(n)

    def test_invalid_phases(self):
        for override in ({4:10},{5:-1},{5:65536},{5:True}):
            with self.assertRaises(ValueError):lab.prime_phases(self.spf,overrides=override)
        with self.assertRaises(ValueError):lab.prime_phases(self.spf,'unknown')

    def test_invalid_scale_and_multiplier(self):
        for s in (0,4,float('nan'),True):
            with self.assertRaises(ValueError):lab.diagnostics(self.phi,s)
        for k in (1,0,65536,True):
            with self.assertRaises(ValueError):lab.phase_audit(self.phi,k)

    def test_payload_no_mutation_of_source(self):
        p=lab.make_payload(256)
        self.assertEqual(p['data'],core.demo_hex(256))
        self.assertEqual(p['data_sha256'],core.fingerprint(p['data']))
        self.assertIsNone(p['boundary']['zero_phase'])

    def test_generated_html_reproducible_and_offline(self):
        with tempfile.TemporaryDirectory() as d:
            a=lab.build_lab(Path(d)/'a.html',count=256).read_bytes()
            b=lab.build_lab(Path(d)/'b.html',count=256).read_bytes()
            self.assertEqual(a,b);self.assertNotIn(b'__LAB_PAYLOAD__',a)
            self.assertNotIn(b'<script src=',a)
            self.assertIn(b'NumberFieldLab',a)

    def test_override_key_must_be_integer(self):
        with self.assertRaises(ValueError):lab.prime_phases(self.spf,overrides={5.0:12})

    def test_gallery_embeds_preview_without_network(self):
        with tempfile.TemporaryDirectory() as d:
            path=lab.build_lab_site(d,count=16);text=path.read_text()
            self.assertIn('frame.srcdoc=code',text)
            self.assertNotIn('__EMBEDDED_LAB__',text)
            self.assertEqual(json.loads((Path(d)/'manifest.json').read_text())['records'],16)
            self.assertEqual(path.read_bytes(),lab.build_lab_site(d,count=16).read_bytes())

    def test_no_implicit_native_upgrade(self):
        p=lab.make_payload(16)
        self.assertEqual(p['data']['kind'],'hex')
        self.assertIn('NOT_X6',p['boundary']['typed_observer'])

if __name__=='__main__':unittest.main(verbosity=2)
