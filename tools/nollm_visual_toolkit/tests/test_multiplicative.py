from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
from nollm_visual_toolkit import multiplicative as m


class MultiplicativeFieldTests(unittest.TestCase):
    def test_phase_two_is_zero(self):
        for seed in (0, 1, 123456789, 0xFFFFFFFF):
            self.assertEqual(m.prime_phase_code(2, seed), 0)

    def test_factorization(self):
        spf = m.smallest_prime_factors(200)
        self.assertEqual(m.factorization(1, spf), ())
        self.assertEqual(m.factorization(60, spf), ((2, 2), (3, 1), (5, 1)))
        self.assertEqual(m.factorization(121, spf), ((11, 2),))

    def test_phase_accumulator_exact_additivity(self):
        spf = m.smallest_prime_factors(4095)
        for a in range(1, 64):
            for b in range(1, 64):
                self.assertEqual(
                    m.phase_accumulator(a*b, spf=spf),
                    m.phase_accumulator(a, spf=spf) + m.phase_accumulator(b, spf=spf),
                )

    def test_carrier_certificate(self):
        cert = m.carrier_certificate(4096)
        self.assertTrue(cert['phase_accumulator_additive_on_checked_products'])
        self.assertGreater(cert['pairs_checked'], 1000)
        self.assertEqual(cert['phase_accumulator_failures'], [])

    def test_config_boundary(self):
        cfg = m.multiplicative_config(count=1024)
        self.assertEqual(cfg['schema'], m.FIELD_SCHEMA)
        self.assertEqual(cfg['carrier']['prime_2_intrinsic_phase_code'], 0)
        self.assertTrue(cfg['claim_boundary']['observer_coordinates_do_not_replace_carrier'])
        self.assertEqual(len(m.config_fingerprint(cfg)), 64)

    def test_html_is_self_contained_and_escaped(self):
        with tempfile.TemporaryDirectory() as d:
            p = m.multiplicative_html(Path(d)/'field.html', count=512)
            text = p.read_text(encoding='utf-8')
            self.assertIn('Multiplicative Memory Field Lab', text)
            self.assertIn('NollmMultiplicativeLab', text)
            self.assertNotIn('https://', text)
            self.assertNotIn('http://', text)
            self.assertIn('NOLLM_MULTIPLICATIVE_FIELD_V1', text)

    def test_invalid_inputs(self):
        for kwargs in [
            {'count':1}, {'seed':-1}, {'radial_exponent':0},
            {'frame_strength':float('inf')}, {'sectors':2}, {'block_size':8},
        ]:
            with self.assertRaises(ValueError):
                m.multiplicative_config(**kwargs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
